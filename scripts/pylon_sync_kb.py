#!/usr/bin/env python3
"""Sync GitHub support-docs markdown into Pylon Knowledge Base articles.

Design choices for the Telnyx support-docs migration:
- Article creates/updates publish immediately (`is_published=true`).
- Removed/omitted managed GitHub docs are unlisted, never hard-deleted.
- Messaging/WhatsApp roots are skipped by default until the Messaging team signs off.
- `_uncategorized` is skipped by default because those articles lacked reliable collection
  placement in the Intercom scrape.
- Idempotency uses Pylon article slugs plus a hidden HTML marker containing the GitHub
  source path/hash.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import markdown  # type: ignore
except ImportError:  # pragma: no cover - exercised by CLI environment validation
    markdown = None

API_BASE = os.environ.get("PYLON_API_BASE", "https://api.usepylon.com").rstrip("/")
DEFAULT_SKIP_PREFIXES = (
    "133103-telnyx-sms-guide/",
    "18868947-whatsapp-business/",
    "_uncategorized/",
)
MARKER_RE = re.compile(
    r"github_source_path=(?P<path>[^\s]+)\s+github_source_sha256=(?P<hash>[a-f0-9]{64})"
)
ARTICLE_URL_RE = re.compile(r"/articles/(?P<id>\d+)-(?P<slug>[a-zA-Z0-9\-]+)")
COLLECTION_URL_RE = re.compile(r"/collections/(?P<id>\d+)-(?P<slug>[^\s]+)")


@dataclass(frozen=True)
class SourceArticle:
    path: Path
    rel_path: str
    title: str
    slug: str
    source_url: str
    source_hash: str
    body_html: str
    collection_key: str


class PylonClient:
    def __init__(self, token: str, *, apply: bool, delay_seconds: float = 0.0) -> None:
        self.token = token
        self.apply = apply
        self.delay_seconds = delay_seconds

    def request(self, method: str, path: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
        if self.delay_seconds:
            time.sleep(self.delay_seconds)
        data = None
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
        }
        if body is not None:
            data = json.dumps(body, separators=(",", ":")).encode("utf-8")
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(f"{API_BASE}{path}", data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                payload = resp.read().decode("utf-8")
                return json.loads(payload) if payload else {}
        except urllib.error.HTTPError as exc:
            response = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Pylon {method} {path} failed with HTTP {exc.code}: {response[:1000]}") from exc

    def list_paginated(self, path: str) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        cursor = None
        while True:
            sep = "&" if "?" in path else "?"
            page_path = f"{path}{sep}limit=100"
            if cursor:
                page_path += "&cursor=" + urllib.parse.quote(str(cursor))
            data = self.request("GET", page_path)
            rows.extend(data.get("data", []))
            pagination = data.get("pagination") or {}
            cursor = pagination.get("cursor")
            if not pagination.get("has_next_page"):
                return rows


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw_meta = text[4:end]
    body = text[end + 5 :]
    meta: dict[str, str] = {}
    for line in raw_meta.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, body


def extract_title(body: str, fallback: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    for line in body.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("[") and not stripped.lower().startswith("written by"):
            return stripped.replace(" | Telnyx Help Center", "").strip()
    return fallback


def source_slug_from_url(source_url: str, fallback: str) -> str:
    match = ARTICLE_URL_RE.search(source_url)
    if match:
        return match.group("slug")
    return slugify(fallback)


def slugify(value: str) -> str:
    value = value.lower().replace("&", "and")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "article"


def clean_markdown_body(body: str) -> str:
    lines = body.splitlines()
    cleaned: list[str] = []
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if idx < 12 and (
            stripped.endswith("| Telnyx Help Center")
            or stripped == "[Skip to main content](#main-content)"
            or stripped == "Table of contents"
        ):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip() + "\n"


def markdown_to_html(md_text: str) -> str:
    if markdown is None:
        raise SystemExit("Missing dependency: install with `python -m pip install markdown`.")
    return markdown.markdown(md_text, extensions=["extra", "sane_lists", "toc"])


def build_marker(rel_path: str, source_hash: str, source_url: str) -> str:
    return (
        f"<!-- github_source_path={html.escape(rel_path, quote=True)} "
        f"github_source_sha256={source_hash} "
        f"source_url={html.escape(source_url, quote=True)} -->"
    )


def load_source_articles(source_root: Path, skip_prefixes: tuple[str, ...]) -> list[SourceArticle]:
    articles: list[SourceArticle] = []
    for path in sorted(source_root.rglob("*.md")):
        if path.name.startswith("_"):
            continue
        rel_path = path.relative_to(source_root).as_posix()
        if any(rel_path.startswith(prefix) for prefix in skip_prefixes):
            continue
        raw = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        source_url = meta.get("source_url", "")
        if "/articles/" not in source_url:
            continue
        title = extract_title(body, path.stem)
        slug = source_slug_from_url(source_url, title)
        clean_body = clean_markdown_body(body)
        source_hash = hashlib.sha256((source_url + "\n" + clean_body).encode("utf-8")).hexdigest()
        body_html = build_marker(rel_path, source_hash, source_url) + "\n" + markdown_to_html(clean_body)
        collection_key = path.parent.relative_to(source_root).as_posix()
        articles.append(
            SourceArticle(
                path=path,
                rel_path=rel_path,
                title=title,
                slug=slug,
                source_url=source_url,
                source_hash=source_hash,
                body_html=body_html,
                collection_key=collection_key,
            )
        )
    return articles


def collection_title_from_key(key: str) -> str:
    name = key.rsplit("/", 1)[-1]
    return re.sub(r"^\d+-", "", name).replace("-", " ").casefold()


def map_collections(collections: list[dict[str, Any]]) -> dict[str, str]:
    by_slug = {str(c.get("slug") or ""): str(c["id"]) for c in collections if c.get("id")}
    by_title = {str(c.get("title") or "").casefold(): str(c["id"]) for c in collections if c.get("id")}
    mapped: dict[str, str] = {}
    tree_path = Path("support-docs/_tree.json")
    tree = json.loads(tree_path.read_text(encoding="utf-8")) if tree_path.exists() else {"collections": []}
    for record in tree.get("collections", []):
        key = record.get("path")
        if not key:
            continue
        title = str(record.get("title") or "").casefold()
        source_slug = str(record.get("source_slug") or "")
        intercom_id = str(record.get("intercom_collection_id") or "")
        candidates = [
            f"{intercom_id}-{slugify(record.get('title') or '')}" if intercom_id else "",
            f"{intercom_id}-{source_slug}" if intercom_id and source_slug else "",
            source_slug,
            slugify(record.get("title") or ""),
        ]
        for slug in candidates:
            if slug in by_slug:
                mapped[key] = by_slug[slug]
                break
        if key not in mapped and title in by_title:
            mapped[key] = by_title[title]
    return mapped


def article_marker(article: dict[str, Any]) -> tuple[str | None, str | None]:
    text = (article.get("current_draft_content_html") or "") + "\n" + (article.get("current_published_content_html") or "")
    match = MARKER_RE.search(text)
    if not match:
        return None, None
    return html.unescape(match.group("path")), match.group("hash")


def make_plan(
    source_articles: list[SourceArticle],
    pylon_articles: list[dict[str, Any]],
    collection_map: dict[str, str],
) -> tuple[list[tuple[str, SourceArticle, dict[str, Any] | None]], list[dict[str, Any]], list[str]]:
    by_slug = {str(a.get("slug") or ""): a for a in pylon_articles if a.get("slug")}
    by_marker_path: dict[str, dict[str, Any]] = {}
    marker_hash_by_id: dict[str, str] = {}
    for article in pylon_articles:
        marker_path, marker_hash = article_marker(article)
        if marker_path:
            by_marker_path[marker_path] = article
            if marker_hash:
                marker_hash_by_id[str(article["id"])] = marker_hash

    ops: list[tuple[str, SourceArticle, dict[str, Any] | None]] = []
    errors: list[str] = []
    active_paths = {source.rel_path for source in source_articles}

    for source in source_articles:
        if source.collection_key not in collection_map:
            errors.append(f"No Pylon collection matched for {source.rel_path} (collection key {source.collection_key})")
            continue
        existing = by_marker_path.get(source.rel_path) or by_slug.get(source.slug)
        if not existing:
            ops.append(("create", source, None))
            continue
        existing_hash = marker_hash_by_id.get(str(existing["id"]))
        desired_collection_id = collection_map[source.collection_key]
        needs_update = (
            existing_hash != source.source_hash
            or existing.get("title") != source.title
            or existing.get("collection_id") != desired_collection_id
            or existing.get("is_published") is not True
            or existing.get("is_unlisted") is not False
        )
        if needs_update:
            ops.append(("update", source, existing))
        else:
            ops.append(("noop", source, existing))

    stale: list[dict[str, Any]] = []
    for article in pylon_articles:
        marker_path, _ = article_marker(article)
        if marker_path and marker_path not in active_paths and not article.get("is_unlisted"):
            stale.append(article)
    return ops, stale, errors


def apply_ops(
    client: PylonClient,
    kb_id: str,
    author_user_id: str,
    collection_map: dict[str, str],
    ops: list[tuple[str, SourceArticle, dict[str, Any] | None]],
    stale: list[dict[str, Any]],
    max_articles: int | None,
) -> dict[str, int]:
    counts = {"create": 0, "update": 0, "noop": 0, "unlist": 0}
    write_count = 0
    for action, source, existing in ops:
        if action == "noop":
            counts["noop"] += 1
            continue
        if max_articles is not None and write_count >= max_articles:
            break
        collection_id = collection_map[source.collection_key]
        if action == "create":
            body = {
                "title": source.title,
                "slug": source.slug,
                "author_user_id": author_user_id,
                "body_html": source.body_html,
                "collection_id": collection_id,
                "is_published": True,
                "is_unlisted": False,
                "visibility_config": {"visibility": "public", "ai_agent_access": "inherit"},
            }
            if client.apply:
                client.request("POST", f"/knowledge-bases/{kb_id}/articles", body)
            counts["create"] += 1
            write_count += 1
        elif action == "update" and existing:
            body = {
                "title": source.title,
                "body_html": source.body_html,
                "is_published": True,
                "is_unlisted": False,
                "publish_updated_body_html": True,
                "visibility_config": {"visibility": "public", "ai_agent_access": "inherit"},
            }
            # Pylon's article PATCH schema does not expose collection_id changes. If the
            # collection is wrong, report it via plan output rather than guessing an unsupported field.
            if client.apply:
                client.request("PATCH", f"/knowledge-bases/{kb_id}/articles/{existing['id']}", body)
            counts["update"] += 1
            write_count += 1
    for article in stale:
        if max_articles is not None and write_count >= max_articles:
            break
        if client.apply:
            client.request("PATCH", f"/knowledge-bases/{kb_id}/articles/{article['id']}", {"is_unlisted": True})
        counts["unlist"] += 1
        write_count += 1
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", default="support-docs", type=Path)
    parser.add_argument("--apply", action="store_true", help="Actually write to Pylon. Default is dry-run.")
    parser.add_argument("--include-uncategorized", action="store_true", help="Sync _uncategorized articles too.")
    parser.add_argument("--include-messaging", action="store_true", help="Sync Messaging and WhatsApp roots too.")
    parser.add_argument("--max-articles", type=int, default=None, help="Maximum write operations to perform; useful for smoke tests.")
    parser.add_argument("--delay-seconds", type=float, default=float(os.environ.get("PYLON_SYNC_DELAY_SECONDS", "0.7")))
    args = parser.parse_args()

    token = os.environ.get("PYLON_API_TOKEN")
    kb_id = os.environ.get("PYLON_KNOWLEDGE_BASE_ID")
    author_user_id = os.environ.get("PYLON_AUTHOR_USER_ID")
    missing = [name for name, value in [("PYLON_API_TOKEN", token), ("PYLON_KNOWLEDGE_BASE_ID", kb_id), ("PYLON_AUTHOR_USER_ID", author_user_id)] if not value]
    if missing:
        raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
    assert token is not None
    assert kb_id is not None
    assert author_user_id is not None

    skip_prefixes = list(DEFAULT_SKIP_PREFIXES)
    if args.include_uncategorized:
        skip_prefixes = [p for p in skip_prefixes if p != "_uncategorized/"]
    if args.include_messaging:
        skip_prefixes = [p for p in skip_prefixes if p not in {"133103-telnyx-sms-guide/", "18868947-whatsapp-business/"}]

    client = PylonClient(token=token, apply=args.apply, delay_seconds=args.delay_seconds if args.apply else 0.0)
    source_articles = load_source_articles(args.source_root, tuple(skip_prefixes))
    collections = client.list_paginated(f"/knowledge-bases/{kb_id}/collections")
    pylon_articles = client.list_paginated(f"/knowledge-bases/{kb_id}/articles")
    collection_map = map_collections(collections)
    ops, stale, errors = make_plan(source_articles, pylon_articles, collection_map)

    counts = apply_ops(client, kb_id, author_user_id, collection_map, ops, stale, args.max_articles)
    planned = {"create": 0, "update": 0, "noop": 0, "unlist": len(stale)}
    for action, _, _ in ops:
        planned[action] += 1

    summary = {
        "mode": "apply" if args.apply else "dry-run",
        "source_articles": len(source_articles),
        "skip_prefixes": skip_prefixes,
        "pylon_articles_seen": len(pylon_articles),
        "pylon_collections_seen": len(collections),
        "planned": planned,
        "executed": counts,
        "errors": errors[:25],
        "error_count": len(errors),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
