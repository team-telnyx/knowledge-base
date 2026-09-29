"""Remove copied Intercom link/feedback trailers from support article sources.

Only a terminal, plain-text "Related Articles" link list followed by the
Intercom feedback prompt qualifies. Authored sections (for example a Markdown
"## Related Articles" heading) remain part of the article.
"""

from __future__ import annotations

import hashlib
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "support-docs"
PROMPT = "\nDid this answer your question?"
RELATED = "\nRelated Articles\n"
REACTIONS = re.compile(r"[\s😞😐😃]*\Z")
LINK = re.compile(r"\[(?:[^\[\]]|\[[^\[\]]*\])*\]\(https?://[^)\n]+\)")
SEPARATOR = re.compile(r"\n---\s*\Z")


def remove_footer(content: str, counts: Counter[str]) -> str:
    prompt_at = content.rfind(PROMPT)
    if prompt_at < 0 or not REACTIONS.fullmatch(content[prompt_at + len(PROMPT) :]):
        return content

    related_at = content.rfind(RELATED, 0, prompt_at)
    if related_at >= 0:
        between = content[related_at + len(RELATED) : prompt_at]
        prefix = content[:related_at].rstrip()
        separator = SEPARATOR.search(prefix)
        if separator is None or LINK.sub("", between).strip():
            raise ValueError("Unrecognized copied footer: review this article manually")
        cleaned = prefix[: separator.start()].rstrip() + "\n"
        counts["related_blocks"] += 1
    else:
        cleaned = content[:prompt_at].rstrip() + "\n"
        counts["feedback_only"] += 1

    frontmatter, body = cleaned.split("---", 2)[1:]
    digest = hashlib.sha256(body.encode()).hexdigest()
    frontmatter = re.sub(r"(?m)^content_hash:.*$", f"content_hash: {digest}", frontmatter)
    return "---" + frontmatter + "---" + body


def main() -> None:
    counts: Counter[str] = Counter()
    for path in sorted(ROOT.glob("*.md")):
        if "en--collections--" in path.name:
            continue
        original = path.read_text()
        try:
            updated = remove_footer(original, counts)
        except ValueError as exc:
            raise ValueError(f"{path}: {exc}") from exc
        if updated != original:
            path.write_text(updated)
            counts["articles_updated"] += 1
    print(dict(counts))


if __name__ == "__main__":
    main()
