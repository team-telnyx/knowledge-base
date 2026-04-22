# Contributing to knowledge-base

This repo is a **compiled LLM wiki** produced by [LLMWiki](https://github.com/team-telnyx/LLMWiki) scraping Telnyx's public documentation surfaces. It is **not** the authoring surface for Telnyx product docs.

Before opening a PR, check where the fix actually belongs.

## Where your change belongs

**Upstream source is wrong.** Fix it on support.telnyx.com or developers.telnyx.com. The next LLMWiki sync picks up the change. This is the default path for any content correction.

**Synthesis is wrong** (page misreads the source, broken cross-references, summary contradicts the source): open an issue or PR against [LLMWiki](https://github.com/team-telnyx/LLMWiki), where the prompts and ingest scripts live.

**Schema, catalog, or repo structure is wrong:** open an issue or PR here against `SCHEMA.md`, `wiki/index.md`, or the README. These are the changes that belong in this repo.

## Hand edits to wiki content

Hand-editing files under `wiki/**` is **discouraged**. Direct edits get overwritten on the next LLMWiki sync unless the upstream source or LLMWiki prompt also changes, so they paper over symptoms rather than fix root causes.

A direct PR here is acceptable in narrow cases — for example, a time-sensitive factual correction where the upstream fix is being filed in parallel — but it should be the exception, not the workflow. Always file the upstream or LLMWiki fix too.

All content additions and edits must conform to [`SCHEMA.md`](../SCHEMA.md): required frontmatter (`title`, `summary`, `sources`, `updated_at`), kebab-case filenames, stable paths, and standard Markdown relative links (no Obsidian `[[wikilinks]]`).

## External contributors

Corrections from outside Telnyx are welcome. External PRs are limited by [external-pr-check.yml](workflows/external-pr-check.yml) to editing existing files — no creating, deleting, or renaming. If you need to propose new content, open an issue first.

## Review

All PRs — automated or hand-authored, internal or external — require approval from a maintainer.

## Questions?

Open an issue.
