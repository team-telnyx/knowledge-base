#!/usr/bin/env python3
"""List changed article paths, including both sides of renames and root files."""
import argparse
import subprocess


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def changed_support_docs(base: str, head: str, merge_base: bool = False) -> list[str]:
    head = git("rev-parse", "--verify", "--end-of-options", head + "^{commit}")
    if not base or set(base) == {"0"}:
        base = subprocess.check_output(["git", "hash-object", "-t", "tree", "--stdin"], input="", text=True).strip()
    else:
        base = git("rev-parse", "--verify", "--end-of-options", base + "^{commit}")
        if merge_base:
            base = git("merge-base", base, head)
    # Disabling rename detection includes the old path for cleanup as well as the new.
    raw = subprocess.check_output([
        "git", "diff", "--name-only", "-z", "--no-renames", "--diff-filter=ACMTD",
        base, head, "--", ":(glob)support-docs/**/*.md",
    ]).decode()
    paths = sorted(filter(None, raw.split("\0")))
    if any("\n" in path for path in paths):
        raise ValueError("Article paths containing newlines are unsupported")
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--merge-base", action="store_true")
    args = parser.parse_args()
    for path in changed_support_docs(args.base, args.head, args.merge_base):
        print(path)


if __name__ == "__main__":
    main()
