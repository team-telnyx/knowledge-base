"""Make scraped support collection cards readable on GitHub.

The site reads collection links to recover hierarchy and membership. This
script keeps every URL and its order intact while separating card titles
from descriptions.
"""

from __future__ import annotations

import hashlib
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "support-docs"
SUPPORT_LINK = re.compile(
    r"\[([^\]\n]+)\]\((https?://support\.telnyx\.com/en/(?:articles|collections)/(\d+-[^/)#?]+)[^)]*)\)"
)
ADJACENT_LINKS = re.compile(r"\]\((https?://support\.telnyx\.com/en/(?:articles|collections)/[^)]+)\)\[")


def normalized(value: str) -> str:
    ascii_text = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", ascii_text.lower())


def split_card(match: re.Match[str], counts: Counter[str]) -> str:
    label, url, slug = match.groups()
    if label.startswith("## "):
        return match.group(0)

    canonical = normalized(slug.split("-", 1)[1])
    boundary = next(
        (index for index in range(1, len(label) + 1) if normalized(label[:index]) == canonical),
        None,
    )
    if boundary is None:
        counts["uncertain_labels"] += 1
        return match.group(0)

    while boundary < len(label) and label[boundary] in "?!:.)":
        boundary += 1
    title, description = label[:boundary], label[boundary:].strip()
    if not description:
        return match.group(0)

    counts["split_cards"] += 1
    return f"[{title}]({url})\n\n{description}"


def update_hash(content: str) -> str:
    frontmatter, body = content.split("---", 2)[1:]
    if not re.search(r"(?m)^content_hash:", frontmatter):
        return content
    digest = hashlib.sha256(body.encode()).hexdigest()
    frontmatter = re.sub(r"(?m)^content_hash:.*$", f"content_hash: {digest}", frontmatter)
    return "---" + frontmatter + "---" + body


def format_collection(content: str, counts: Counter[str]) -> str:
    frontmatter, body = content.split("---", 2)[1:]
    formatted = ADJACENT_LINKS.sub(r"](\1)\n\n[", body)
    formatted = SUPPORT_LINK.sub(lambda match: split_card(match, counts), formatted)
    if formatted == body:
        return content
    return update_hash("---" + frontmatter + "---" + formatted)


def main() -> None:
    counts: Counter[str] = Counter()
    for path in sorted(ROOT.glob("en--collections--*.md")):
        original = path.read_text()
        updated = format_collection(original, counts)
        if updated != original:
            path.write_text(updated)
            counts["collection_files"] += 1
    print(dict(counts))


if __name__ == "__main__":
    main()
