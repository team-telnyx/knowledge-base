#!/usr/bin/env python3
"""Helpers for monthly full LLMWiki refresh workflows.

The GitHub Actions jobs intentionally pull the LLMWiki compiler from the
compiler repo at runtime. This script only handles the artifact-repo concerns:

- prepare checked-in support docs as a compiler source snapshot
- strip volatile `content_hash:` lines from generated wiki pages
- install one compiled workspace without touching the other workspace
- rebuild the flattened top-level wiki index from workspace indexes

Keeping this glue in the artifact repo lets the compiler keep evolving without
copy/pasting its internals into GitHub Actions. Tiny blast radius, fewer goblins.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

FRONTMATTER_RE = re.compile(r"\A---\n(?P<meta>.*?)\n---\n(?P<body>.*)\Z", re.DOTALL)
CONTENT_HASH_LINE_RE = re.compile(r"^\s*content_hash:\s*[0-9a-fA-F]{64}\s*$")
INDEX_ENTRY_RE = re.compile(r"^- \[(?P<title>.*?)]\((?P<link>[^)]+)\) — (?P<summary>.*)$")
SKIP_SOURCE_NAMES = {"_collection.md", "_manifest.md"}


@dataclass(frozen=True)
class IndexEntry:
    workspace: str
    title: str
    link: str
    summary: str


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


def prepare_support_sources(source_root: Path, llmwiki_dir: Path) -> dict[str, object]:
    """Copy checked-in support docs into LLMWiki's expected sources tree.

    LLMWiki's loader only requires `source_url` frontmatter; it recomputes source
    hashes from body content. We skip collection marker files because the full
    compiler should synthesize article knowledge, not folder labels.
    """

    output_root = llmwiki_dir / "wikis" / "support-docs" / "sources" / "support-docs"
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    copied: list[str] = []
    skipped: list[str] = []
    for source in sorted(source_root.rglob("*.md")):
        rel = source.relative_to(source_root)
        if source.name.startswith("_") or source.name in SKIP_SOURCE_NAMES:
            skipped.append(rel.as_posix())
            continue
        text = source.read_text(encoding="utf-8")
        meta, _body = parse_frontmatter(text)
        if not meta.get("source_url"):
            skipped.append(rel.as_posix())
            continue
        dest = output_root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        copied.append(rel.as_posix())

    manifest = {
        "source_root": source_root.as_posix(),
        "output_root": output_root.as_posix(),
        "copied_count": len(copied),
        "skipped_count": len(skipped),
        "copied": copied,
        "skipped": skipped,
    }
    (output_root / "_prepared_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def strip_content_hashlines(path: Path) -> dict[str, int]:
    files_seen = 0
    files_changed = 0
    lines_removed = 0
    for md in sorted(path.rglob("*.md")):
        files_seen += 1
        original = md.read_text(encoding="utf-8")
        kept: list[str] = []
        removed_here = 0
        for line in original.splitlines(keepends=True):
            line_without_newline = line.rstrip("\r\n")
            if CONTENT_HASH_LINE_RE.match(line_without_newline):
                removed_here += 1
                continue
            kept.append(line)
        if removed_here:
            md.write_text("".join(kept), encoding="utf-8")
            files_changed += 1
            lines_removed += removed_here
    return {
        "files_seen": files_seen,
        "files_changed": files_changed,
        "content_hash_lines_removed": lines_removed,
    }


def install_workspace(workspace: str, compiled_wiki_root: Path, wiki_root: Path) -> dict[str, str]:
    src = compiled_wiki_root / workspace
    if not src.is_dir():
        raise FileNotFoundError(f"Compiled workspace not found: {src}")
    dest = wiki_root / workspace
    if dest.exists():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dest)
    return {"installed_from": src.as_posix(), "installed_to": dest.as_posix()}


def remove_workspace_indexes(wiki_root: Path) -> dict[str, object]:
    """Delete per-workspace index files after the root index has been flattened."""

    removed: list[str] = []
    for index_path in iter_workspace_indexes(wiki_root):
        index_path.unlink()
        removed.append(index_path.as_posix())
    return {"removed_count": len(removed), "removed": removed}


def iter_workspace_indexes(wiki_root: Path) -> Iterable[Path]:
    for path in sorted(wiki_root.glob("*/index.md")):
        if path.parent.name.startswith("."):
            continue
        yield path


def entries_from_workspace_index(index_path: Path, wiki_root: Path) -> list[IndexEntry]:
    workspace = index_path.parent.name
    entries: list[IndexEntry] = []
    for line in index_path.read_text(encoding="utf-8").splitlines():
        match = INDEX_ENTRY_RE.match(line)
        if not match:
            continue
        link = match.group("link")
        if link.startswith("http://") or link.startswith("https://"):
            prefixed = link
        else:
            prefixed = (Path(workspace) / link).as_posix()
        entries.append(
            IndexEntry(
                workspace=workspace,
                title=match.group("title"),
                link=prefixed,
                summary=match.group("summary"),
            )
        )
    return entries


def rebuild_root_index(wiki_root: Path) -> dict[str, object]:
    entries: list[IndexEntry] = []
    for index_path in iter_workspace_indexes(wiki_root):
        entries.extend(entries_from_workspace_index(index_path, wiki_root))

    entries.sort(key=lambda e: (e.title.casefold(), e.workspace, e.link))
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    lines = [
        "---",
        "title: Telnyx Knowledge Base Index",
        f"updated_at: {now}",
        "---",
        "",
        "# Telnyx Knowledge Base Index",
        "",
    ]
    for entry in entries:
        lines.append(f"- [{entry.title}]({entry.link}) — {entry.summary}")
    lines.append("")
    index_path = wiki_root / "index.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    workspace_counts: dict[str, int] = {}
    for entry in entries:
        workspace_counts[entry.workspace] = workspace_counts.get(entry.workspace, 0) + 1
    return {
        "index_path": index_path.as_posix(),
        "entry_count": len(entries),
        "workspace_counts": workspace_counts,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Monthly LLMWiki refresh helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare-support-sources")
    prepare.add_argument("--source-root", type=Path, default=Path("support-docs"))
    prepare.add_argument("--llmwiki-dir", type=Path, required=True)

    strip = subparsers.add_parser("strip-content-hashlines")
    strip.add_argument("--path", type=Path, required=True)

    install = subparsers.add_parser("install-workspace")
    install.add_argument("--workspace", required=True)
    install.add_argument("--compiled-wiki-root", type=Path, required=True)
    install.add_argument("--wiki-root", type=Path, default=Path("wiki"))

    remove_indexes = subparsers.add_parser("remove-workspace-indexes")
    remove_indexes.add_argument("--wiki-root", type=Path, default=Path("wiki"))

    rebuild = subparsers.add_parser("rebuild-root-index")
    rebuild.add_argument("--wiki-root", type=Path, default=Path("wiki"))

    args = parser.parse_args()
    if args.command == "prepare-support-sources":
        result = prepare_support_sources(args.source_root, args.llmwiki_dir)
    elif args.command == "strip-content-hashlines":
        result = strip_content_hashlines(args.path)
    elif args.command == "install-workspace":
        result = install_workspace(args.workspace, args.compiled_wiki_root, args.wiki_root)
    elif args.command == "remove-workspace-indexes":
        result = remove_workspace_indexes(args.wiki_root)
    elif args.command == "rebuild-root-index":
        result = rebuild_root_index(args.wiki_root)
    else:  # pragma: no cover - argparse enforces this
        raise AssertionError(args.command)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
