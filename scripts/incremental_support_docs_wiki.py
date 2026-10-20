#!/usr/bin/env python3
"""Incrementally project changed support-doc source articles into wiki corpus pages.

This is intentionally *not* a full LLMWiki recompile. Full recompiles can regroup,
rename, split, and delete many wiki files. For support-docs edits coming from the
GitHub/Pylon workflow we only want the changed article represented in the corpus:

- added/modified support-doc article -> write one deterministic wiki page
- deleted support-doc article -> remove that deterministic wiki page, if present
- update wiki/index.md by upserting only those links

The existing synthesized LLMWiki corpus remains untouched. New/changed support docs
land under wiki/support-docs/articles/ so the operation is small and reviewable.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable

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


def parse_updated_at(meta: dict[str, str]) -> datetime:
    for key in ("updated_at", "scraped"):
        raw = meta.get(key)
        if not raw:
            continue
        try:
            parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            continue
        return parsed.astimezone(UTC) if parsed.tzinfo else parsed.replace(tzinfo=UTC)
    # Missing source metadata must not make identical checkouts drift.
    return datetime(1970, 1, 1, tzinfo=UTC)


def iso_z(value: datetime) -> str:
    return value.astimezone(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_source_article(path: Path, source_root: Path, output_subdir: Path) -> SourceArticle | None:
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
    wiki_rel = (output_subdir / f"{slug}.md").as_posix()
    return SourceArticle(
        source_path=path,
        source_rel=source_rel,
        wiki_rel=wiki_rel,
        title=title,
        summary=summarize(cleaned, title),
        source_url=source_url,
        body=cleaned,
        updated_at=parse_updated_at(meta),
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


def owned_pages(wiki_root: Path, output_subdir: Path) -> dict[str, list[str]]:
    """Only remove pages explicitly owned by this generator; preserve synthesis."""
    result: dict[str, list[str]] = {}
    for path in sorted((wiki_root / output_subdir).rglob("*.md")):
        meta, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        if meta.get("generated_by") == "incremental-support-docs-wiki" and meta.get("source_path"):
            result.setdefault(meta["source_path"], []).append(path.relative_to(wiki_root).as_posix())
    return result


def index_entry(article: SourceArticle) -> str:
    return f"- [{escape_markdown_label(article.title)}]({article.wiki_rel}) — {article.summary}"


def escape_markdown_label(value: str) -> str:
    return re.sub(r"([\\\[\]()])", r"\\\1", re.sub(r"[\r\n]+", " ", value))


def read_index(path: Path) -> list[str]:
    if path.exists():
        return path.read_text(encoding="utf-8").splitlines()
    path.parent.mkdir(parents=True, exist_ok=True)
    return ["---", "title: Telnyx Knowledge Base", "updated_at: 1970-01-01T00:00:00Z", "---", "", "# Telnyx Knowledge Base", ""]


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
        # Preserve the corpus snapshot date; wall-clock edits make CI drift.
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
        # Preserve the corpus snapshot date; wall-clock edits make CI drift.
        index_path.write_text("\n".join(filtered).rstrip() + "\n", encoding="utf-8")
    return changed


def normalize_changed_path(raw: str) -> str:
    return raw.strip().strip('"').lstrip("./")


def iter_changed_files(args: argparse.Namespace) -> list[str]:
    values: list[str] = []
    for item in args.changed_file or []:
        values.extend(item.splitlines())
    if args.changed_files_file:
        values.extend(Path(args.changed_files_file).read_text(encoding="utf-8").splitlines())
    if not values and not args.reconcile and not sys.stdin.isatty():
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
    parser.add_argument("--reconcile", action="store_true", help="Rebuild all article projections and remove stale owned pages; preserve synthesized pages.")
    args = parser.parse_args()

    previous = owned_pages(args.wiki_root, args.output_subdir)
    changed = iter_changed_files(args)
    if args.reconcile:
        changed.extend(previous)
        changed.extend(path.as_posix() for path in args.source_root.rglob("*.md"))
    changed_paths = support_doc_paths(changed, args.source_root)
    if not changed_paths:
        print(json.dumps({"changed_support_docs": 0, "written": 0, "removed": 0, "index_updates": 0}, indent=2))
        return 0

    written: list[str] = []
    removed: list[str] = []
    index_updates = 0
    wiki_article_dir = args.wiki_root / args.output_subdir
    wiki_article_dir.mkdir(parents=True, exist_ok=True)

    articles: dict[Path, SourceArticle | None] = {}
    destinations: dict[str, Path] = {}
    for source_path in changed_paths:
        article = None
        if source_path.exists():
            article = load_source_article(source_path, args.source_root, args.output_subdir)
        if article is not None:
            if article.wiki_rel in destinations:
                raise ValueError(f"Duplicate article destination {article.wiki_rel}: {destinations[article.wiki_rel]} and {source_path}")
            destinations[article.wiki_rel] = source_path
            existing = args.wiki_root / article.wiki_rel
            if existing.exists():
                meta, _ = parse_frontmatter(existing.read_text(encoding="utf-8"))
                if meta.get("generated_by") != "incremental-support-docs-wiki":
                    raise ValueError(f"Refusing to overwrite unowned page: {existing}")
        articles[source_path] = article

    # Remove all old mappings before writing: a renamed source may sort before
    # its deleted path, and both can map to the same destination.
    for source_path, article in articles.items():
        # A rename is supplied as deletion + addition. Persisted source_path also
        # finds old URL slugs and sources that ceased to be article pages.
        for wiki_rel in previous.get(source_path.as_posix(), []):
            if article is not None and wiki_rel == article.wiki_rel:
                continue
            output_path = args.wiki_root / wiki_rel
            if output_path.exists():
                output_path.unlink()
                removed.append(output_path.as_posix())
            if remove_index_entry(args.wiki_root / "index.md", wiki_rel):
                index_updates += 1

    for article in articles.values():
        if article is not None:
            output_path = args.wiki_root / article.wiki_rel
            rendered = render_article(article)
            if not output_path.exists() or output_path.read_text(encoding="utf-8") != rendered:
                output_path.write_text(rendered, encoding="utf-8")
                written.append(output_path.as_posix())
            if upsert_index_entry(args.wiki_root / "index.md", article.wiki_rel, index_entry(article)):
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
    return 2 if args.fail_on_drift and (written or removed or index_updates) else 0


if __name__ == "__main__":
    raise SystemExit(main())
