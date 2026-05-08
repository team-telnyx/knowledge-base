---
title: Smoke Page Two
summary: Second fixture page — exists so the manifest table has more than one row.
sources:
- url: https://example.com/smoke/page-two
  content_hash: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
- url: https://example.com/smoke/page-two-supplement
  content_hash: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
updated_at: 2026-05-08T10:00:00Z
---

# Smoke Page Two

Second fixture page — exists so the manifest table has more than one row.

## Multi-source

This page declares two sources so the publish PR's source-manifest table rendering is exercised against the multi-source-per-page case (one row per source, same `Page` filename across rows). The hashes are sentinel values (`bbbb…` / `cccc…`) — not real SHA-256s.

## Disposable

Same disposal rule as Smoke Page One: close the PR and delete the branch when the smoke run is done.
