"""Fail-closed review gate for same-repository documentation auto-merges."""

import base64
import json
import os
import re
import subprocess
import sys


def gh_json(*args):
    return json.loads(subprocess.check_output(["gh", *args], text=True))


def global_owners(contents):
    """Support the repository's single wildcard rule, not partial CODEOWNERS syntax."""
    rules = [line.split("#", 1)[0].split() for line in contents.splitlines()]
    rules = [rule for rule in rules if rule]
    if len(rules) != 1 or rules[0][0] != "*" or len(rules[0]) < 2:
        return set()
    owners = rules[0][1:]
    if not all(re.fullmatch(r"@[A-Za-z0-9-]+", owner) for owner in owners):
        return set()
    return {owner[1:].lower() for owner in owners}


def eligible(pr, reviews, owners, permission, repo, head, hold):
    if (
        pr["state"] != "open"
        or pr["draft"]
        or (pr["head"].get("repo") or {}).get("full_name") != repo
        or pr["head"]["sha"] != head
        or any(label["name"] == hold for label in pr["labels"])
    ):
        return False
    # Comments do not replace a prior approval or request for changes. A
    # dismissed review does replace its old state, as returned by the API.
    latest = {}
    for review in sorted(
        reviews, key=lambda review: (review.get("submitted_at") or "", review["id"])
    ):
        login = (review.get("user") or {}).get("login", "").lower()
        if login and review["state"] in {"APPROVED", "CHANGES_REQUESTED", "DISMISSED"}:
            latest[login] = review
    if any(review["state"] == "CHANGES_REQUESTED" for review in latest.values()):
        return False
    if permission in {"admin", "maintain", "write"} and pr["user"]["type"] != "Bot":
        return True
    author = pr["user"]["login"].lower()
    return any(
        login in owners
        and login != author
        and review["state"] == "APPROVED"
        and review["commit_id"] == head
        for login, review in latest.items()
    )


def main():
    repo, number, head = (os.environ[key] for key in ("REPO", "PR_NUMBER", "HEAD_SHA"))
    pr = gh_json("api", f"repos/{repo}/pulls/{number}")
    # Do not fetch reviews or owner configuration for a fork, even on manual reruns.
    if (pr["head"].get("repo") or {}).get("full_name") != repo:
        print("proceed=false")
        return
    author = pr["user"]["login"]
    try:
        permission = gh_json("api", f"repos/{repo}/collaborators/{author}/permission")[
            "permission"
        ]
    except subprocess.CalledProcessError:
        permission = "none"
    pages = gh_json(
        "api",
        "--paginate",
        "--slurp",
        f"repos/{repo}/pulls/{number}/reviews?per_page=100",
    )
    reviews = [review for page in pages for review in page]
    # Read CODEOWNERS from the live base branch, never from the PR branch.
    content = gh_json(
        "api",
        "--method",
        "GET",
        f"repos/{repo}/contents/.github/CODEOWNERS",
        "-f",
        f"ref={pr['base']['ref']}",
    )
    owners = global_owners(base64.b64decode(content["content"]).decode())
    proceed = eligible(
        pr, reviews, owners, permission, repo, head, os.environ["HOLD_LABEL"]
    )
    print(f"proceed={str(proceed).lower()}")
    print(
        "Review/author gate passed."
        if proceed
        else "Waiting for eligibility or code-owner approval.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
