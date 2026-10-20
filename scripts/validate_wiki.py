#!/usr/bin/env python3
"""Validate existing corpus conventions and flattened index targets, offline."""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def validate(wiki_root: Path) -> list[str]:
    errors = []
    pages = sorted(wiki_root.rglob('*.md'))
    if not pages:
        return [f'{wiki_root}: no Markdown pages found']
    for page in pages:
        text = page.read_text(encoding='utf-8')
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            errors.append(f'{page}: missing or unclosed frontmatter')
        if not re.search(r'^# .+', text, re.MULTILINE):
            errors.append(f'{page}: missing H1')
    index = wiki_root / 'index.md'
    if not index.is_file():
        errors.append(f'{index}: missing flattened index')
        return errors
    # Validate the generated index's canonical links, not arbitrary prose links
    # whose formats and external availability are outside this corpus contract.
    for link in re.findall(r'^- \[.*?\]\(([^)]+)\)', index.read_text(encoding='utf-8'), re.MULTILINE):
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (wiki_root / unquote(url.path)).resolve()
        if not target.is_relative_to(wiki_root.resolve()) or not target.is_file():
            errors.append(f'{index}: missing or out-of-corpus target: {link}')
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--wiki-root', type=Path, default=Path('wiki'))
    args = parser.parse_args()
    errors = validate(args.wiki_root)
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Wiki Markdown and flattened index targets are valid.')


if __name__ == '__main__':
    main()
