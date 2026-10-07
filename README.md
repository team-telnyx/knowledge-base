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
support-docs/_manifest.json       # Generated source inventory + snapshot asset listing
support-docs/_images/             # Screenshots and other assets referenced by articles
wiki/                             # Compiled LLM wiki consumed by agents/indexers
wiki/index.md                     # Single flattened catalog for the generated wiki
website/                          # React/Vite static site for support.telnyx.com
scripts/incremental_support_docs_wiki.py
                                  # Deterministically updates wiki pages for changed support docs
scripts/regenerate_support_docs_manifest.py
                                  # Regenerates the support-doc source inventory
scripts/monthly_llmwiki_refresh.py
                                  # Glue for monthly full LLMWiki refresh jobs
.github/workflows/deploy-website.yml
                                  # Builds website/ and deploys it to S3 on merge to main
.github/workflows/external-pr-check.yml
.github/workflows/incremental-support-docs-wiki.yml
.github/workflows/monthly-llmwiki-refresh.yml
```

`support-docs/` is currently a flat snapshot: article and collection sources live directly in the directory as `en--articles--<id>-<slug>.md` and `en--collections--<id>-<slug>.md`, with YAML frontmatter (`source_url`, `title`, `description`, `scraped`, `content_hash`) and an H1 title in the body. `_manifest.json` is generated metadata: `scripts/regenerate_support_docs_manifest.py` derives `pages_saved` and `files` from the checked-in Markdown tree while preserving the snapshot's scrape date and asset inventory. Do not edit its source-file inventory by hand.

Website ingestion uses `source_url` to identify the canonical `/en/articles/...` or `/en/collections/...` path. Current prefixed filenames remain supported for compatibility. A future clean `<id>-<slug>.md` filename must include a valid type-bearing `source_url`; otherwise ingestion fails rather than guessing whether it is an article or collection.

`source_url` metadata is authoritative and must be an HTTP or HTTPS URL on `support.telnyx.com` with no credentials or non-default port, and an English `/en/articles/<id>-<slug>` or `/en/collections/<id>-<slug>` path. Its identity need not match the storage filename.

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

1. `Incremental Support Docs Wiki Corpus` regenerates `_manifest.json`, detects changed files under `support-docs/**/*.md`, runs `scripts/incremental_support_docs_wiki.py`, and verifies the PR includes the required deterministic manifest and `wiki/` updates.
2. `External Contribution Check` restricts external PRs to modifying existing files only (no adds, deletes, or renames).
3. Maintainers review the source article changes and generated wiki changes together.
4. `Auto-merge internal support-doc PRs` squash-merges the PR without waiting for a maintainer when it comes from someone with write access (any Telnyx org member) on an in-repo branch, only touches `support-docs/` and the generated `wiki/support-docs/` / `wiki/index.md` artifacts, and every other check is green. Label a PR `no-auto-merge` to opt out. See [CONTRIBUTING.md](.github/CONTRIBUTING.md#review).

The incremental wiki update intentionally does **not** run the full LLMWiki compiler. It keeps day-to-day article updates small and reviewable.

### Merge to `main` touching `support-docs/**` or `website/**`

1. `Deploy website` builds the website from `support-docs/` and syncs it to `s3://support.telnyx.com/`.
2. The incremental wiki workflow can commit deterministic `wiki/` updates on `main` when needed.

### Adding a new support article

1. Add a Markdown file to `support-docs/` following the `en--articles--<id>-<slug>.md` naming convention.
2. Include frontmatter with the article's `source_url` when available.
3. Use a clear H1 title in the body.
4. Run the manifest and incremental wiki generators, or let CI report the required changes.
5. Review the PR diff, including any generated `wiki/` changes.
6. Merge after approval — the deploy workflow publishes the article to the website.

### Modifying an existing support article

1. Edit the Markdown file in `support-docs/`.
2. Keep the `source_url` stable unless the public article URL intentionally changed.
3. Let CI verify the generated manifest and incremental wiki artifact update.
4. Merge after approval.

## Website

`website/` uses React 19 to render complete static HTML at build time, Vite to
compile styles and a small search/filter script, and Bun to build and preview.
The current migration target is `https://d27az1l5lty0u1.cloudfront.net`.

```sh
cd website
bun install --frozen-lockfile
bun run build
bun run type-check
bun test
bun run verify
bun run preview:edge   # http://127.0.0.1:4173
```

`bun run dev` builds once and starts the same exact-key preview. Rebuild/restart
after edits. The preview executes the shared CloudFront routing logic and does
not hide missing objects behind an SPA fallback.

### Content and rendering

`build-content.ts` reads the checked-in Markdown inventory. Source URLs determine
canonical identity. It combines root snapshots, the verified 355 memberships in
66 pre-existing Intercom leaf collections, and explicit/source-evidenced article
ownership. No build fetches Intercom or creates new collection categories.

The migration inventory now has 906 articles and 115 existing collections,
including the previously omitted Telnyx Email and RCS roots. 902 article
memberships are recovered; four use the documented fallback. All collection
counts include unique available descendants; lists/filters show direct members.

Checked-in heading IDs, reviewed section aliases, image dimensions, and recovered
video links preserve functionality lost in the original scrape. Existing GitHub
article content is retained; published content absent from the repo is imported
separately. The two PR 51 consolidations remain removed and receive redirects.

`render-site.tsx` generates full HTML for every canonical path, initial titles,
descriptions, canonicals, Article/Breadcrumb JSON-LD, a sitemap, robots.txt, and an
LLM index. Article modification dates come from explicit source dates or actual
Git history, not build/scrape timestamps. CI checks out full history. Search loads
a small index only when used; article reading and ordinary navigation need no JS.

Builds default to the temporary origin and `noindex,follow`. `SITE_ORIGIN` controls
canonical/sitemap URLs. Indexability requires the explicit `SITE_INDEXABLE=true`
setting and production origin. Public-domain cutover remains outside this work.

### Routing and verification

The generated CloudFront Function and KeyValueStore provide same-host HTTP 301s
for `/en`, `/en/`, old titles, bare IDs, known old custom paths, and consolidated
articles. Unknown content URLs return 404. Deploying HTML alone does not install
this function. See [edge rollout](website/edge/README.md).

`bun run verify` checks all rendered pages, links/anchors, metadata, local images,
nonempty collections, sitemap coverage, and a 30 KB client-JS budget. Its report
explicitly lists the remaining editorial links to two retired guides rather than
claiming they work. Resolve these before declaring the migration complete. `bun run verify:strict`
is the no-exceptions release check and currently fails for those known links.

For Growth's real GSC/backlink URL export:

```sh
python3 scripts/audit-migration-urls.py growth.csv --output results.json
```

The audit records statuses, redirects and fragment targets, preserving supplied
click/impression/backlink weights. It supports `--url-column` and a local preview
origin. No traffic weight is fabricated when the export is absent.

The existing push-to-main workflow uploads to S3 using AWS OIDC. This local branch
has not been merged or deployed; the CloudFront routing rollout is separate.

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
python3 scripts/regenerate_support_docs_manifest.py --check
python3 -m unittest discover -s tests
python3 -m py_compile scripts/regenerate_support_docs_manifest.py scripts/incremental_support_docs_wiki.py scripts/monthly_llmwiki_refresh.py
```

## Contributing

For managed support KB content, open PRs against `support-docs/` and include the generated incremental `wiki/` changes when CI asks for them.

For developer docs content, fix the upstream developer documentation source. The monthly LLMWiki refresh will scrape and compile it into the generated wiki.

All PRs — automated or hand-authored — require maintainer approval before merging, except routine support-doc edits by Telnyx members, which the auto-merge workflow merges once CI is green (see [CONTRIBUTING.md](.github/CONTRIBUTING.md#review)).
