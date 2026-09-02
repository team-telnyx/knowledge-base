#!/usr/bin/env python3
"""Regenerate the support-doc source inventory from the checked-in tree."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_SOURCE_ROOT = Path("support-docs")
MANIFEST_NAME = "_manifest.json"


def source_files(source_root: Path) -> list[str]:
    """Return the sorted Markdown inventory relative to ``source_root``."""

    return sorted(
        path.relative_to(source_root).as_posix()
        for path in source_root.rglob("*.md")
        if path.is_file()
    )


def desired_manifest(source_root: Path) -> dict[str, Any]:
    """Return the manifest with its source-file inventory regenerated.

    Snapshot metadata such as ``scraped`` and ``assets`` is preserved. Only
    ``pages_saved`` and ``files`` are derived from the authoritative Markdown
    tree, so ordinary article additions, deletions, and renames cannot leave
    stale source entries behind.
    """

    manifest_path = source_root / MANIFEST_NAME
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError(f"{manifest_path} must contain a JSON object")

    files = source_files(source_root)
    manifest["pages_saved"] = len(files)
    manifest["files"] = files
    return manifest


def regenerate_manifest(source_root: Path, *, check: bool = False) -> bool:
    """Regenerate the manifest and return whether its contents were stale.

    In check mode the file is left untouched, allowing CI to validate it.
    """

    manifest_path = source_root / MANIFEST_NAME
    current = manifest_path.read_text(encoding="utf-8")
    desired = json.dumps(desired_manifest(source_root), indent=2) + "\n"
    changed = current != desired
    if changed and not check:
        manifest_path.write_text(desired, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root",
        type=Path,
        default=DEFAULT_SOURCE_ROOT,
        help="support-doc source directory (default: support-docs)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="report a stale manifest without rewriting it",
    )
    args = parser.parse_args()

    changed = regenerate_manifest(args.source_root, check=args.check)
    if args.check and changed:
        print(
            f"{args.source_root / MANIFEST_NAME} is stale; run "
            "python scripts/regenerate_support_docs_manifest.py"
        )
        return 1
    if changed:
        print(f"Regenerated {args.source_root / MANIFEST_NAME}")
    else:
        print(f"{args.source_root / MANIFEST_NAME} is up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
