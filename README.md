# knowledge-base

A compiled **LLM wiki** assembled from Telnyx's public documentation surfaces — [support.telnyx.com](https://support.telnyx.com), [developers.telnyx.com](https://developers.telnyx.com), and related sources. Pages are Markdown with frontmatter that links back to the original articles, and the whole corpus is consumed by downstream agents (e.g. [knowledge-agent](https://github.com/team-telnyx/knowledge-agent)) rather than republished to any user-facing site.

## Overview

Raw articles and reference material from public Telnyx sources are scraped, synthesized into topical Markdown pages by [LLMWiki](https://github.com/team-telnyx/LLMWiki), and stored here as a queryable knowledge base. Every page cites its upstream sources via `sources:` frontmatter, so consumers can always trace a claim back to the authoritative article.

This repository is the **artifact layer** — purely Markdown + YAML, schema-defined, git-versioned. Any agent or indexer can consume it.

## Repository Structure

```
SCHEMA.md                # Canonical page + index format (see below)
wiki/                    # Compiled LLM wiki
├── index.md             # Top-level catalog of all pages
├── account/             # Billing, portal, API keys
├── ai/                  # AI products & APIs
├── fax/                 # Fax services
├── identity/            # Verify, lookup
├── messaging/           # SMS, MMS, 10DLC
├── networking/          # IP, private networking
├── numbers/             # Phone numbers, porting
├── storage/             # Cloud storage
├── voice/               # Voice & SIP products
└── wireless/            # IoT, SIM management
```

> **Note:** The product-area split is a starting point. Pages can be moved or regrouped as the corpus grows.

## Schema and catalog

Because the wiki is consumed by downstream agents and tools, pages follow a defined format.

- **[`SCHEMA.md`](SCHEMA.md)** is the canonical contract for page frontmatter, filenames, internal links, and the index catalog. Read it before adding or editing pages. The schema is versioned; the current version is `0.1.0` (draft) and consumers pin to a tag.
- **[`wiki/index.md`](wiki/index.md)** is the top-level catalog of pages grouped by product area. Every page is listed there with a one-line summary. Treat it as a derived artifact — regenerated from page frontmatter rather than hand-maintained out of band.

## File format

All content files are **Markdown (`.md`)** and must conform to [`SCHEMA.md`](SCHEMA.md) — required frontmatter (including `sources:` URLs), link conventions, and filename rules. The schema is what makes the corpus reliably consumable; Markdown on its own is not enough.

## How content gets here

Content lands through [LLMWiki](https://github.com/team-telnyx/LLMWiki), which runs ingest pipelines against the upstream sources and opens PRs into this repo. Hand-authored PRs are accepted for correcting synthesis errors, but the default authoring surface is LLMWiki — not this repo.

If the wiki is wrong because the **upstream source** is wrong, fix it upstream (support.telnyx.com / developers.telnyx.com) and the next sync will reflect it. If the wiki is wrong because the **synthesis** is wrong, open an issue or PR here or against LLMWiki's prompts.

All PRs — automated or hand-authored — require approval from a maintainer before merging.

## Consumers

- [**knowledge-agent**](https://github.com/team-telnyx/knowledge-agent) — LangGraph-based question-answering service that loads a pinned version of this wiki at startup.
- Additional retrieval backends (vector search, hybrid) are planned as part of the wider LLM-wiki evaluation.

## Local setup

```bash
git clone git@github.com:team-telnyx/knowledge-base.git
cd knowledge-base
```

No build step — the repo is pure content.
