# knowledge-base Schema

**Version:** `0.1.0` (draft)
**Status:** Experimental. Expect breaking changes until `1.0.0`.

This document defines the canonical structure of the knowledge-base wiki so that downstream consumers — retrieval agents, indexers, renderers — can rely on a stable contract.

Two file types are covered:

1. **Document pages** — the knowledge content itself, under `wiki/**`.
2. **Index** — the top-level catalog at `wiki/index.md`.

## Versioning

The schema follows [Semantic Versioning](https://semver.org/) and is tracked by git tags on this repository.

- **Major bump** — breaking change to required fields, paths, or structure.
- **Minor bump** — additive change (new optional fields, new sections).
- **Patch bump** — clarifications, typos, non-behavioural edits.

Consumers should pin to a specific tag and bump deliberately.

## Document pages

Every Markdown file under `wiki/` (except `index.md` files) is a **document page**.

### File layout

- Extension: `.md`.
- Filename: kebab-case, ASCII, no spaces. Example: `number-porting.md`.
- Location: under `wiki/<area>/`, where `<area>` is one of the product areas listed in the README.
- Paths are stable. Renaming a file is a breaking change for consumers that pin to a path. Prefer adding a new file and marking the old one deprecated over renaming.

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
- `[[wikilinks]]` (Obsidian style) are not permitted in this schema version.
- External links are fully-qualified HTTPS.

### Size guidance

Target ≤ 8 000 characters per page. Longer pages should be split across multiple files with cross-links. This is guidance, not enforced in v0.1.

## Index

`wiki/index.md` is the wiki's catalog.

### Frontmatter (YAML)

Required keys:

| Key | Type | Description |
|---|---|---|
| `title` | `str` | Human-readable catalog title (e.g. `knowledge-base Index`). |
| `updated_at` | `str` (ISO 8601) | When the index was last regenerated. |

### Body

- An H1 matching `title`.
- One H2 per product area, in the order defined in the README.
- Under each H2, a bulleted list of entries of the form:
  `- [Page Title](relative/path.md) — one-line summary.`
- Entries are sorted alphabetically by title within each area.
- Areas with no pages yet appear with an explicit placeholder line (e.g. `_No pages yet._`).

The index is a derived artifact and can be regenerated from page frontmatter and paths.

### Example entry

```markdown
## Numbers

- [Number Porting](numbers/number-porting.md) — How to port existing phone numbers into Telnyx.
```

## Validation

Schema conformance will be enforced by a CI job that runs on every PR. That job lands in a follow-up PR; until then, this document is the authoritative contract.

## Out of scope for v0.1

Intentionally deferred to keep the initial contract small while the wider architecture settles:

- Per-section stable IDs beyond H2 anchors.
- `page_id` for rename-safe references.
- Procedural-memory / correction pages.
- Multi-language variants.
- Per-page deprecation / redirect metadata.
- Per-area sub-indexes (`wiki/<area>/index.md`).

Each of these has a plausible answer. Pinning them now would force churn later once real consumer needs surface.
