# Telnyx Knowledge Base

A git-versioned knowledge repository for Telnyx support content and AI-consumable wiki artifacts.

This repo has three related jobs:

1. **Source of truth for the published Telnyx Support Knowledge Base** — Markdown files under `support-docs/` are the reviewed source for support articles.
2. **Compiled LLM wiki corpus** — Markdown under `wiki/` is generated from `support-docs/` plus scraped developer documentation so AI agents can answer Telnyx product questions from a citation-friendly corpus.
3. **Support website** — `website/` renders `support-docs/` as a static site deployed to `support.telnyx.com`.

## Overview

`support-docs/` is the canonical, git-reviewed source for Telnyx Support Knowledge Base articles managed by this repository.

`wiki/` is a derived artifact. It is not the place to make primary content edits. It is generated from source material and consumed by downstream agents/indexers such as the Knowledge Agent.

The important distinction:

- **Support KB publishing source:** `support-docs/`
- **AI/wiki consumption artifact:** `wiki/`
- **Developer docs source:** `developers.telnyx.com`, scraped during the monthly LLMWiki refresh
- **Website:** `website/`, built from `support-docs/` and deployed on merge to `main`

## Repository structure

```text
SCHEMA.md                         # Canonical generated wiki page + index format
support-docs/                     # Source of truth for managed Telnyx Support KB articles
support-docs/_manifest.json       # Snapshot manifest: file and asset listing
support-docs/_images/             # Screenshots and other assets referenced by articles
wiki/                             # Compiled LLM wiki consumed by agents/indexers
wiki/index.md                     # Single flattened catalog for the generated wiki
website/                          # React/Vite static site for support.telnyx.com
scripts/incremental_support_docs_wiki.py
                                  # Deterministically updates wiki pages for changed support docs
scripts/monthly_llmwiki_refresh.py
                                  # Glue for monthly full LLMWiki refresh jobs
.github/workflows/deploy.yml      # Builds website/ and deploys it to S3 on merge to main
.github/workflows/external-pr-check.yml
.github/workflows/incremental-support-docs-wiki.yml
.github/workflows/monthly-llmwiki-refresh.yml
```

`support-docs/` is currently a flat snapshot: articles live directly in the directory as `en--articles--<id>-<slug>.md`, with YAML frontmatter (`source_url`, `title`, `description`, `scraped`, `content_hash`) and an H1 title in the body. `_manifest.json` lists all files and assets in the snapshot.

The internal organization of `wiki/` is generated and may evolve. Consumers should navigate via `wiki/index.md` rather than hard-coding paths.

## Content ownership model

### `support-docs/` is authoritative for managed support articles

For support articles represented in this repository, edit `support-docs/` first. Those files are the source that gets published to the Telnyx Support Knowledge Base website.

Each article should keep its `source_url` frontmatter pointing at the corresponding public support article URL when one exists.

### `wiki/` is generated

Do not hand-edit `wiki/` for normal content corrections. Update the source material instead:

- Support KB issue: edit `support-docs/`.
- Developer docs issue: fix the upstream developer docs source, then let the monthly refresh scrape/compile it.
- LLMWiki synthesis/indexing issue: update the compiler/glue or run a reviewed full refresh PR.

Hand edits to `wiki/` should be rare and treated as emergency fixes only, because the next generated refresh can overwrite them.

## What happens when support content changes

### Pull request touching `support-docs/**`

1. `Incremental Support Docs Wiki Corpus` runs in check mode: it detects changed files under `support-docs/**/*.md`, runs `scripts/incremental_support_docs_wiki.py`, and verifies the PR includes the required deterministic `wiki/` updates for the changed support docs.
2. `External Contribution Check` restricts external PRs to modifying existing files only (no adds, deletes, or renames).
3. Maintainers review the source article changes and generated wiki changes together.

The incremental wiki update intentionally does **not** run the full LLMWiki compiler. It keeps day-to-day article updates small and reviewable.

### Merge to `main` touching `support-docs/**` or `website/**`

1. `Deploy - build and deploy to production` builds the website from `support-docs/` and syncs it to `s3://support.telnyx.com/`.
2. The incremental wiki workflow can commit deterministic `wiki/` updates on `main` when needed.

### Adding a new support article

1. Add a Markdown file to `support-docs/` following the `en--articles--<id>-<slug>.md` naming convention, and add it to `_manifest.json`.
2. Include frontmatter with the article's `source_url` when available.
3. Use a clear H1 title in the body.
4. Run or let CI run the incremental wiki update.
5. Review the PR diff, including any generated `wiki/` changes.
6. Merge after approval — the deploy workflow publishes the article to the website.

### Modifying an existing support article

1. Edit the Markdown file in `support-docs/`.
2. Keep the `source_url` stable unless the public article URL intentionally changed.
3. Let CI verify the incremental wiki artifact update.
4. Merge after approval.

## Website

`website/` is a React 19 + Vite single-page app built and run with [Bun](https://bun.sh). All commands run from the `website/` directory:

```bash
cd website
bun install
```

### Run locally (dev)

```bash
bun run dev
```

This first regenerates the content from `../support-docs` (see the pipeline below), then starts the Vite dev server with hot reload at [http://localhost:5173](http://localhost:5173). Re-run the command after changing anything under `support-docs/` — content is generated at startup, not watched.

### Run the built version

```bash
bun run build      # full production build into website/dist
bun run preview    # serve website/dist at http://localhost:4173
```

`build` runs the whole production pipeline: content generation, `tsc`-independent Vite build, and route-file generation. `preview` serves the resulting `dist/` exactly as produced, which is the closest local approximation of the S3 deployment (one difference: the dev/preview server falls back to `index.html` for unknown paths on its own, while production relies on the generated route files and the S3 error document).

Other useful scripts:

```bash
bun run type-check    # tsc --noEmit
bun run gen-content   # regenerate content without building
```

### How the build works

The content pipeline (`website/scripts/build-content.ts`, runs as a `prebuild`/`predev` step) reads `support-docs/`, cleans scraper noise from article bodies, rewrites legacy help-center links, copies theme fonts and referenced images into `website/public/`, emits per-article JSON for on-demand loading, and generates a typed content manifest. When `support-docs/_tree.json` is absent (the current flat snapshot), it derives topic collections from keyword rules. A postbuild step (`website/scripts/generate-route-files.ts`) materializes every route — including legacy `/en/articles/...` URLs — as a static file so deep links work on S3, plus a `404.html` fallback.

Deployment runs from `.github/workflows/deploy.yml` on pushes to `main`, using OIDC role assumption for AWS credentials.

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

## Schema and catalog

Because the wiki is consumed by downstream agents and tools, generated pages follow a defined format.

- [`SCHEMA.md`](SCHEMA.md) describes expected page frontmatter, filenames, internal links, and the index catalog.
- [`wiki/index.md`](wiki/index.md) is the top-level catalog and entry point for navigating the generated wiki.

Treat `wiki/index.md` as derived. It is rebuilt by automation, not hand-maintained.

## Consumers

This repo is designed to be consumed by:

- The support website at `support.telnyx.com`, built from `support-docs/`.
- AI agents and retrieval systems, for answering Telnyx product questions from the generated `wiki/` corpus.

Because the generated wiki pages are Markdown with explicit source metadata, the same corpus can back agentic-retrieval pipelines, vector indexes, or other consumption shapes. Consumers that need short-term stability should pin to a specific commit.

## Local setup

```bash
git clone git@github.com:team-telnyx/knowledge-base.git
cd knowledge-base
```

There is no required build step for reading the repo. The automation scripts are Python and are run by GitHub Actions. For website development, see the [Website](#website) section.

Useful local checks:

```bash
python3 -m py_compile scripts/incremental_support_docs_wiki.py scripts/monthly_llmwiki_refresh.py
```

## Contributing

For managed support KB content, open PRs against `support-docs/` and include the generated incremental `wiki/` changes when CI asks for them.

For developer docs content, fix the upstream developer documentation source. The monthly LLMWiki refresh will scrape and compile it into the generated wiki.

All PRs — automated or hand-authored — require maintainer approval before merging.
