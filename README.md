# Telnyx Knowledge Base

A git-versioned knowledge repository for Telnyx support content and AI-consumable wiki artifacts.

This repo now has two related jobs:

1. **Source of truth for the published Telnyx Support Knowledge Base** — Markdown files under `support-docs/` are synced to the Telnyx-published Pylon Knowledge Base.
2. **Compiled LLM wiki corpus** — Markdown under `wiki/` is generated from `support-docs/` plus scraped developer documentation so AI agents can answer Telnyx product questions from a citation-friendly corpus.

## Overview

`support-docs/` is the canonical, git-reviewed source for Telnyx Support Knowledge Base articles that are managed by this repository. When a support article is added or edited here and merged to `main`, automation syncs that content into Pylon.

`wiki/` is a derived artifact. It is not the place to make primary content edits. It is generated from source material and consumed by downstream agents/indexers such as the Knowledge Agent.

The important distinction:

- **Support KB publishing source:** `support-docs/`
- **AI/wiki consumption artifact:** `wiki/`
- **Developer docs source:** `developers.telnyx.com`, scraped during the monthly LLMWiki refresh

## Repository structure

```text
SCHEMA.md                         # Canonical generated wiki page + index format
support-docs/                     # Source of truth for managed Telnyx Support KB articles
support-docs/_tree.json           # Collection metadata from the support-docs import
wiki/                             # Compiled LLM wiki consumed by agents/indexers
wiki/index.md                     # Single flattened catalog for the generated wiki
scripts/pylon_sync_kb.py          # Syncs support-docs Markdown into Pylon
scripts/incremental_support_docs_wiki.py
                                  # Deterministically updates wiki pages for changed support docs
scripts/monthly_llmwiki_refresh.py
                                  # Glue for monthly full LLMWiki refresh jobs
.github/workflows/pylon-kb-sync.yml
.github/workflows/incremental-support-docs-wiki.yml
.github/workflows/monthly-llmwiki-refresh.yml
```

The internal organization of `wiki/` is generated and may evolve. Consumers should navigate via `wiki/index.md` rather than hard-coding paths.

## Content ownership model

### `support-docs/` is authoritative for managed support articles

For support articles represented in this repository, edit `support-docs/` first. Those files are the source that gets published to the Telnyx Support Knowledge Base.

Each article should keep its `source_url` frontmatter pointing at the corresponding public support article URL when one exists. The sync process uses stable source paths, source URLs, slugs, and content hashes to decide whether to create, update, skip, or unlist Pylon articles.

### `wiki/` is generated

Do not hand-edit `wiki/` for normal content corrections. Update the source material instead:

- Support KB issue: edit `support-docs/`.
- Developer docs issue: fix the upstream developer docs source, then let the monthly refresh scrape/compile it.
- LLMWiki synthesis/indexing issue: update the compiler/glue or run a reviewed full refresh PR.

Hand edits to `wiki/` should be rare and treated as emergency fixes only, because the next generated refresh can overwrite them.

## What happens when support content changes

### Pull request touching `support-docs/**`

When a PR adds, modifies, moves, or deletes support-doc Markdown:

1. `Incremental Support Docs Wiki Corpus` runs in check mode.
2. It detects changed files under `support-docs/**/*.md`.
3. It runs `scripts/incremental_support_docs_wiki.py` locally in the workflow.
4. It verifies the PR includes the required deterministic `wiki/` updates for the changed support docs.
5. `Sync Pylon Knowledge Base` runs in dry-run/check mode. It validates that the sync script can process the changed source content without writing to Pylon.
6. Maintainers review the source article changes and generated wiki changes together.

The incremental wiki update intentionally does **not** run the full LLMWiki compiler. It keeps day-to-day article updates small and reviewable.

### Merge to `main` touching `support-docs/**`

After the PR is merged:

1. `Sync Pylon Knowledge Base` runs with `apply=true` on `main`.
2. `scripts/pylon_sync_kb.py` reads `support-docs/` and syncs eligible articles to Pylon.
3. New articles are created in Pylon and published.
4. Modified articles are updated in Pylon and published.
5. Managed articles that disappear from the eligible source set are unlisted rather than hard-deleted.
6. The incremental wiki workflow can commit deterministic `wiki/` updates on `main` when needed.

By default, the Pylon sync skips:

- `support-docs/_uncategorized/`
- Messaging roots such as `133103-telnyx-sms-guide/`
- WhatsApp roots such as `18868947-whatsapp-business/`

Those can be included manually through workflow-dispatch inputs when the relevant teams are ready.

### Adding a new support article

To add a new managed support KB article:

1. Add a Markdown file under the correct `support-docs/<collection>/` folder.
2. Include frontmatter with the article's `source_url` when available.
3. Use a clear H1 title in the body.
4. Run or let CI run the incremental wiki update.
5. Review the PR diff, including any generated `wiki/` changes.
6. Merge after approval.
7. The main-branch Pylon sync publishes the new article.

### Modifying an existing support article

To update an existing support KB article:

1. Edit the Markdown file in `support-docs/`.
2. Keep the `source_url` stable unless the public article URL intentionally changed.
3. Let CI verify the incremental wiki artifact update.
4. Merge after approval.
5. The Pylon sync updates the corresponding Pylon article if the content hash changed.

### Moving or deleting a support article

Moves are supported, but be careful with slugs and collection placement:

- Moving a file changes its GitHub source path marker.
- The Pylon sync primarily relies on stable article slugs/source URLs to match existing articles.
- Removed managed articles are unlisted, not hard-deleted.

For bulk reorganizations, use a dedicated PR and review the Pylon dry-run output before merge.

## LLMWiki refresh model

There are two wiki-refresh paths.

### Incremental support-doc updates

Workflow:

```text
.github/workflows/incremental-support-docs-wiki.yml
```

Purpose:

- Keep `wiki/` reasonably fresh when individual support articles change.
- Produce small deterministic diffs.
- Avoid full-corpus regrouping on ordinary article edits.

This workflow uses the checked-in script:

```bash
python scripts/incremental_support_docs_wiki.py
```

It does not pull or run the full LLMWiki compiler.

### Monthly full LLMWiki refresh

Workflow:

```text
.github/workflows/monthly-llmwiki-refresh.yml
```

Schedule:

```text
First Sunday of each month at 07:23 UTC
```

Purpose:

- Pull the latest LLMWiki compiler from `team-telnyx/LLMWiki`.
- Prepare checked-in `support-docs/` as the support-doc source corpus.
- Scrape `developers.telnyx.com` into a dev-doc source snapshot.
- Full-compile support docs and developer docs separately.
- Rebuild a single flattened `wiki/index.md`.
- Open a reviewable PR with the generated wiki diff and compiler SHA.

Default compiler source:

```text
team-telnyx/LLMWiki@main
```

Manual runs can override `llmwiki_ref` to test a branch, tag, or SHA.

The monthly job keeps compiler improvements on a controlled cadence without making every support article edit subject to full-corpus LLM regrouping.

## Pylon sync behavior

Workflow:

```text
.github/workflows/pylon-kb-sync.yml
```

On pull requests, it runs as a validation/dry-run path. On pushes to `main`, it applies changes to Pylon.

Important behavior:

- Article creates/updates publish immediately.
- Idempotency uses hidden GitHub source markers and content hashes.
- Managed removals unlist articles instead of hard-deleting them.
- `_uncategorized`, Messaging, and WhatsApp content are skipped by default.
- Manual workflow dispatch supports dry runs, write runs, inclusion of skipped roots, and max-article caps for smoke tests.

## Schema and catalog

Because the wiki is consumed by downstream agents and tools, generated pages follow a defined format.

- [`SCHEMA.md`](SCHEMA.md) describes expected page frontmatter, filenames, internal links, and the index catalog.
- [`wiki/index.md`](wiki/index.md) is the top-level catalog and entry point for navigating the generated wiki.

Treat `wiki/index.md` as derived. It is rebuilt by automation, not hand-maintained.

## Consumers

This repo is designed to be consumed by:

- Pylon, for the published Telnyx Support Knowledge Base sourced from `support-docs/`.
- AI agents and retrieval systems, for answering Telnyx product questions from the generated `wiki/` corpus.

Because the generated wiki pages are Markdown with explicit source metadata, the same corpus can back agentic-retrieval pipelines, vector indexes, or other consumption shapes. Consumers that need short-term stability should pin to a specific commit.

## Local setup

```bash
git clone git@github.com:team-telnyx/knowledge-base.git
cd knowledge-base
```

There is no required build step for reading the repo. The automation scripts are Python and are run by GitHub Actions.

Useful local checks:

```bash
python3 -m py_compile scripts/incremental_support_docs_wiki.py scripts/monthly_llmwiki_refresh.py scripts/pylon_sync_kb.py
```

## Contributing

For managed support KB content, open PRs against `support-docs/` and include the generated incremental `wiki/` changes when CI asks for them.

For developer docs content, fix the upstream developer documentation source. The monthly LLMWiki refresh will scrape and compile it into the generated wiki.

All PRs — automated or hand-authored — require maintainer approval before merging.
