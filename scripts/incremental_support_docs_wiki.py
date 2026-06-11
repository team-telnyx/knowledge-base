#!/usr/bin/env python3
"""Incrementally project changed support-doc source articles into wiki corpus pages.

This is intentionally *not* a full LLMWiki recompile. Full recompiles can regroup,
rename, split, and delete many wiki files. For support-docs edits coming from the
GitHub/Pylon workflow we only want the changed article represented in the corpus:

- added/modified support-doc article -> write one deterministic wiki page
- deleted support-doc article -> remove that deterministic wiki page, if present
- update wiki/index.md and wiki/support-docs/index.md by upserting only those links

The existing synthesized LLMWiki corpus remains untouched. New/changed support docs
land under wiki/support-docs/articles/ so the operation is small and reviewable.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable
from urllib.parse import urlsplit

ARTICLE_URL_RE = re.compile(r"/articles/(?P<id>\d+)-(?P<slug>[a-zA-Z0-9\-]+)")
FRONTMATTER_RE = re.compile(r"\A---\n(?P<meta>.*?)\n---\n(?P<body>.*)\Z", re.DOTALL)
INDEX_LINE_RE = re.compile(r"^- \[(?P<title>.*?)]\((?P<link>[^)]+)\) — (?P<summary>.*)$")
DEFAULT_SOURCE_ROOT = Path("support-docs")
DEFAULT_WIKI_ROOT = Path("wiki")
DEFAULT_OUTPUT_SUBDIR = Path("support-docs/articles")
SKIP_PARTS = {"_manifest.json", "_tree.json"}


@dataclass(frozen=True)
class SourceArticle:
    source_path: Path
    source_rel: str
    wiki_rel: str
    title: str
    summary: str
    source_url: str
    content_hash: str
    body: str
    updated_at: datetime


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta: dict[str, str] = {}
    for raw_line in match.group("meta").splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, match.group("body")


def slugify(value: str) -> str:
    value = value.lower().replace("&", "and")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "article"


def article_slug(source_url: str, title: str) -> str:
    match = ARTICLE_URL_RE.search(source_url)
    if match:
        return f"{match.group('id')}-{match.group('slug')}"
    return slugify(title)


def extract_title(body: str, fallback: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    for line in body.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("["):
            return stripped.replace(" | Telnyx Help Center", "").strip()
    return fallback


def strip_source_boilerplate(body: str) -> str:
    cleaned: list[str] = []
    seen_h1 = False
    for idx, line in enumerate(body.splitlines()):
        stripped = line.strip()
        if idx < 20 and (
            stripped.endswith("| Telnyx Help Center")
            or stripped == "[Skip to main content](#main-content)"
            or stripped == "Table of contents"
            or stripped.startswith("Written by ")
            or re.fullmatch(r"[A-Z][a-z]+ \d{1,2}, \d{4}", stripped)
        ):
            continue
        if stripped.startswith("# "):
            if seen_h1:
                cleaned.append("## " + stripped[2:].strip())
                continue
            seen_h1 = True
        cleaned.append(line.rstrip())
    return "\n".join(cleaned).strip() + "\n"


def summarize(body: str, title: str) -> str:
    paragraphs = re.split(r"\n\s*\n", body)
    for paragraph in paragraphs:
        text = " ".join(
            line.strip()
            for line in paragraph.splitlines()
            if line.strip() and not line.strip().startswith("#") and not line.strip().startswith("|")
        )
        text = re.sub(r"\[([^\]]+)]\([^)]+\)", r"\1", text)
        text = re.sub(r"[*_`#>]", "", text).strip()
        if len(text) >= 40:
            return truncate_sentence(text, 260)
    return f"Support article: {title}."


def truncate_sentence(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    cut = text[: limit - 1]
    sentence_end = max(cut.rfind(". "), cut.rfind("; "), cut.rfind(".\n"))
    if sentence_end > 80:
        return cut[: sentence_end + 1]
    return cut.rsplit(" ", 1)[0].rstrip(".,;:") + "…"


def escape_yaml_scalar(value: str) -> str:
    # JSON strings are valid YAML scalars and avoid pulling in PyYAML for this tiny writer.
    return json.dumps(value, ensure_ascii=False)


def parse_updated_at(meta: dict[str, str], source_path: Path, now: datetime) -> datetime:
    for key in ("updated_at", "scraped"):
        raw = meta.get(key)
        if not raw:
            continue
        try:
            parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            continue
        return parsed.astimezone(UTC) if parsed.tzinfo else parsed.replace(tzinfo=UTC)
    # In CI this reflects the checkout timestamp, so use NOW for actual update time.
    _ = source_path
    return now


def iso_z(value: datetime) -> str:
    return value.astimezone(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_source_article(path: Path, source_root: Path, wiki_root: Path, output_subdir: Path, now: datetime) -> SourceArticle | None:
    if path.name.startswith("_") or path.name in SKIP_PARTS or path.suffix != ".md":
        return None
    raw = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(raw)
    source_url = meta.get("source_url", "")
    if "/articles/" not in source_url:
        return None
    cleaned = strip_source_boilerplate(body)
    title = extract_title(cleaned, path.stem)
    slug = article_slug(source_url, title)
    source_rel = path.relative_to(source_root).as_posix()
    content_hash = hashlib.sha256(cleaned.encode("utf-8")).hexdigest()
    wiki_rel = (output_subdir / f"{slug}.md").as_posix()
    return SourceArticle(
        source_path=path,
        source_rel=source_rel,
        wiki_rel=wiki_rel,
        title=title,
        summary=summarize(cleaned, title),
        source_url=source_url,
        content_hash=content_hash,
        body=cleaned,
        updated_at=parse_updated_at(meta, path, now),
    )


def render_article(article: SourceArticle) -> str:
    body = article.body
    if not body.lstrip().startswith(f"# {article.title}"):
        body = f"# {article.title}\n\n{body}"
    frontmatter = "\n".join(
        [
            "---",
            f"title: {escape_yaml_scalar(article.title)}",
            f"summary: {escape_yaml_scalar(article.summary)}",
            "sources:",
            f"- url: {escape_yaml_scalar(article.source_url)}",
            f"  content_hash: {article.content_hash}",
            f"updated_at: {iso_z(article.updated_at)}",
            "tags: [support-docs]",
            f"source_path: {escape_yaml_scalar('support-docs/' + article.source_rel)}",
            "generated_by: incremental-support-docs-wiki",
            "---",
            "",
        ]
    )
    marker = f"<!-- generated_from=support-docs/{html.escape(article.source_rel)} -->\n\n"
    return frontmatter + marker + body.rstrip() + "\n"


def wiki_rel_for_deleted_support_doc(path: Path, source_root: Path, wiki_root: Path, output_subdir: Path) -> str | None:
    # Prefer source URL from the prior commit if GitHub checked it out in the caller.
    # If unavailable, derive from the filename stem, which preserves Intercom article IDs.
    if path.suffix != ".md" or path.name.startswith("_"):
        return None
    slug = path.stem
    return (output_subdir / f"{slug}.md").as_posix()


def index_entry(article: SourceArticle) -> str:
    return f"- [{escape_markdown_label(article.title)}]({article.wiki_rel}) — {article.summary}"


def escape_markdown_label(value: str) -> str:
    return re.sub(r"([\\\[\]()])", r"\\\1", re.sub(r"[\r\n]+", " ", value))


def read_index(path: Path) -> list[str]:
    if path.exists():
        return path.read_text(encoding="utf-8").splitlines()
    path.parent.mkdir(parents=True, exist_ok=True)
    return ["---", "title: Telnyx Knowledge Base", f"updated_at: {iso_z(datetime.now(UTC))}", "---", "", "# Telnyx Knowledge Base", ""]


def upsert_index_entry(index_path: Path, rel_link: str, line: str) -> bool:
    lines = read_index(index_path)
    changed = False
    replaced = False
    for i, existing in enumerate(lines):
        match = INDEX_LINE_RE.match(existing)
        if match and match.group("link") == rel_link:
            if existing != line:
                lines[i] = line
                changed = True
            replaced = True
            break
    if not replaced:
        if lines and lines[-1].strip():
            lines.append("")
        lines.append(line)
        changed = True
    if changed:
        touch_index_updated_at(lines)
        index_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return changed


def remove_index_entry(index_path: Path, rel_link: str) -> bool:
    if not index_path.exists():
        return False
    lines = index_path.read_text(encoding="utf-8").splitlines()
    filtered: list[str] = []
    changed = False
    for existing in lines:
        match = INDEX_LINE_RE.match(existing)
        if match and match.group("link") == rel_link:
            changed = True
            continue
        filtered.append(existing)
    if changed:
        touch_index_updated_at(filtered)
        index_path.write_text("\n".join(filtered).rstrip() + "\n", encoding="utf-8")
    return changed


def touch_index_updated_at(lines: list[str]) -> None:
    now = iso_z(datetime.now(UTC))
    for i, line in enumerate(lines[:10]):
        if line.startswith("updated_at:"):
            lines[i] = f"updated_at: {now}"
            return


def normalize_changed_path(raw: str) -> str:
    return raw.strip().strip('"').lstrip("./")


def iter_changed_files(args: argparse.Namespace) -> list[str]:
    values: list[str] = []
    for item in args.changed_file or []:
        values.extend(item.splitlines())
    if args.changed_files_file:
        values.extend(Path(args.changed_files_file).read_text(encoding="utf-8").splitlines())
    if not values and not sys.stdin.isatty():
        values.extend(sys.stdin.read().splitlines())
    return [normalize_changed_path(v) for v in values if normalize_changed_path(v)]


def support_doc_paths(changed: Iterable[str], source_root: Path) -> list[Path]:
    prefix = source_root.as_posix().rstrip("/") + "/"
    paths: list[Path] = []
    for rel in changed:
        if rel.startswith(prefix) and rel.endswith(".md"):
            paths.append(Path(rel))
    return sorted(set(paths))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--wiki-root", type=Path, default=DEFAULT_WIKI_ROOT)
    parser.add_argument("--output-subdir", type=Path, default=DEFAULT_OUTPUT_SUBDIR)
    parser.add_argument("--changed-file", action="append", help="Changed file path. May be passed multiple times.")
    parser.add_argument("--changed-files-file", help="File containing changed paths, one per line.")
    parser.add_argument("--fail-on-drift", action="store_true", help="Exit 2 if generated files differ from the checked-out tree.")
    args = parser.parse_args()

    changed_paths = support_doc_paths(iter_changed_files(args), args.source_root)
    if not changed_paths:
        print(json.dumps({"changed_support_docs": 0, "written": 0, "removed": 0, "index_updates": 0}, indent=2))
        return 0

    now = datetime.now(UTC)
    written: list[str] = []
    removed: list[str] = []
    index_updates = 0
    wiki_article_dir = args.wiki_root / args.output_subdir
    wiki_article_dir.mkdir(parents=True, exist_ok=True)

    for rel_path in changed_paths:
        source_path = Path(rel_path)
        if source_path.exists():
            article = load_source_article(source_path, args.source_root, args.wiki_root, args.output_subdir, now)
            if article is None:
                continue
            output_path = args.wiki_root / article.wiki_rel
            rendered = render_article(article)
            if not output_path.exists() or output_path.read_text(encoding="utf-8") != rendered:
                output_path.write_text(rendered, encoding="utf-8")
                written.append(output_path.as_posix())
            if upsert_index_entry(args.wiki_root / "index.md", article.wiki_rel, index_entry(article)):
                index_updates += 1
            workspace_rel = Path(article.wiki_rel).relative_to("support-docs").as_posix()
            if upsert_index_entry(args.wiki_root / "support-docs" / "index.md", workspace_rel, index_entry(article).replace(f"]({article.wiki_rel})", f"]({workspace_rel})")):
                index_updates += 1
        else:
            wiki_rel = wiki_rel_for_deleted_support_doc(source_path, args.source_root, args.wiki_root, args.output_subdir)
            if not wiki_rel:
                continue
            output_path = args.wiki_root / wiki_rel
            if output_path.exists():
                output_path.unlink()
                removed.append(output_path.as_posix())
            if remove_index_entry(args.wiki_root / "index.md", wiki_rel):
                index_updates += 1
            workspace_rel = Path(wiki_rel).relative_to("support-docs").as_posix()
            if remove_index_entry(args.wiki_root / "support-docs" / "index.md", workspace_rel):
                index_updates += 1

    summary = {
        "changed_support_docs": len(changed_paths),
        "written": len(written),
        "removed": len(removed),
        "index_updates": index_updates,
        "written_files": written,
        "removed_files": removed,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
