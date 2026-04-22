# Telnyx Knowledge Base Schema

**Version:** `0.1.0` (draft)
**Status:** Light contract — stable enough to build against, but will evolve as the ingestion pipeline matures. Breaking changes are called out in commit messages rather than gated by formal version bumps.

This document describes the structure of the Telnyx Knowledge Base so downstream consumers — retrieval agents, indexers, renderers — know what to expect from the corpus.

Two file types are covered:

1. **Document pages** — the knowledge content itself, under `wiki/**`.
2. **Index** — the top-level catalog at `wiki/index.md`.

## Document pages

Every Markdown file under `wiki/` (except `index.md` files) is a **document page**.

### File layout

- Extension: `.md`.
- Filename: kebab-case, ASCII, no spaces. Example: `number-porting.md`.
- Location: under `wiki/`. The internal directory layout is determined by the ingestion pipeline.
- Paths may change when the ingestion pipeline regenerates or rewrites pages — full rewrites are fine. Consumers should navigate via `wiki/index.md` rather than hard-coding paths.

### Frontmatter (YAML)

Required keys:

| Key | Type | Description |
|---|---|---|
| `title` | `str` | Human-readable page title. |
| `summary` | `str` | One-sentence description. Used by indexes and retrieval shortlists. |
| `sources` | `list[Source]` | Non-empty list of the raw sources this page was synthesized from or written against. |
| `updated_at` | `str` (ISO 8601) | When the page content was last edited or re-synthesized. |

A `Source` is an object:

| Key | Type | Description |
|---|---|---|
| `url` | `str` | Fully-qualified HTTPS URL to the raw source (e.g. `https://developers.telnyx.com/docs/...`). |
| `content_hash` | `str` | SHA-256 (hex) of the source content at the time of synthesis. Enables drift detection. |

Optional keys:

| Key | Type | Description |
|---|---|---|
| `tags` | `list[str]` | Free-form topical tags for filtering. |
| `related` | `list[str]` | Relative paths to related pages. |

### Example

```yaml
---
title: Number Porting
summary: How to port existing phone numbers into Telnyx.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/overview
    content_hash: 8f14e45fceea167a5a36dedd4bea2543b6b1b8c7c9a50f7e3a1d9c9f9a7b6c5d
updated_at: 2026-04-21T00:00:00Z
tags: [numbers, porting]
---
```

### Body

- The body starts with an H1 matching `title` exactly. The duplication with frontmatter is intentional so the raw file reads naturally when viewed without a frontmatter-aware renderer.
- Subsequent sections use H2 and deeper. H2 headings are unique within the page so downstream consumers can use them as stable section anchors when chunking.
- Content is GitHub-flavored Markdown.

### Internal links

- Use standard Markdown relative links: `[Porting overview](../numbers/porting.md)`.
- `[[wikilinks]]` (Obsidian style) are not used.
- External links are fully-qualified HTTPS.

### Size guidance

Target ≤ 8 000 characters per page. Longer pages should be split across multiple files with cross-links. Guidance in v0.1, not enforced.

## Index

`wiki/index.md` is the wiki's catalog.

### Frontmatter (YAML)

Required keys:

| Key | Type | Description |
|---|---|---|
| `title` | `str` | Human-readable catalog title (e.g. `Telnyx Knowledge Base Index`). |
| `updated_at` | `str` (ISO 8601) | When the index was last regenerated. |

### Body

- An H1 matching `title`.
- A list of entries of the form: `- [Page Title](relative/path.md) — one-line summary.`
- Sectioning, ordering, and grouping are determined by the ingestion pipeline and may evolve. Consumers should parse the catalog by walking Markdown links rather than relying on a fixed section structure.

The index is a derived artifact and can be regenerated from page frontmatter and paths.

### Example entry

```markdown
## Numbers

- [Number Porting](numbers/number-porting.md) — How to port existing phone numbers into Telnyx.
```

## Validation

A CI job to check page conformance against this draft is planned; until then this document is the reference.

## Out of scope for v0.1

Intentionally deferred to keep the initial draft small while the wider architecture settles:

- Per-section stable IDs beyond H2 anchors.
- `page_id` for rename-safe references.
- Procedural-memory / correction pages.
- Multi-language variants.
- Per-page deprecation / redirect metadata.
