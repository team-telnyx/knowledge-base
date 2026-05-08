---
title: Smoke Page One
summary: Fixture page exercising the AITS-100 publish step end-to-end. Not real content.
sources:
- url: https://example.com/smoke/page-one
  content_hash: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
updated_at: 2026-05-08T10:00:00Z
---

# Smoke Page One

Fixture page exercising the AITS-100 publish step end-to-end. Not real content.

## What this page is for

This file is part of a smoke fixture used to validate the publish pipeline against the live `team-telnyx/knowledge-base` repo. It does not represent any real Telnyx documentation surface. Close the PR and delete the branch when the smoke run is done.

## Identifying it as fixture

The `sources[].url` points at `example.com/smoke/...`. The `content_hash` is a sentinel value (`aaaa…`) rather than a real SHA-256. Both make this file unambiguously a smoke artifact in the manifest table.
