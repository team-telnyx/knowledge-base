---
title: Reporting
summary: Telnyx provides several reporting tools for inspecting usage, costs, and
  session-level activity across its products. The Usage Reports API exposes aggregated,
  queryable usage data; Session Analysis reconstructs the full event and cost tree
  for individual sessions (especially AI-powered calls); and On-Demand Reports offers
  a natural-language interface on top of Usage Report data.
sources:
- url: https://developers.telnyx.com/docs/reporting/on-demand-reports/index
- url: https://developers.telnyx.com/docs/reporting/session-analysis/index
- url: https://developers.telnyx.com/docs/reporting/usage-reports/index
updated_at: 2026-08-05T14:01:58Z
---

# Reporting

*Part 1 of 4 — see also: [Part 2](reporting--part-2.md), [Part 3](reporting--part-3.md), [Part 4](reporting--part-4.md)*

Telnyx provides several reporting tools for inspecting usage, costs, and session-level activity across its products. The Usage Reports API exposes aggregated, queryable usage data; Session Analysis reconstructs the full event and cost tree for individual sessions (especially AI-powered calls); and On-Demand Reports offers a natural-language interface on top of Usage Report data.

## Overview

Telnyx's reporting stack is built around three complementary surfaces:

- **Usage Reports** — a flexible, single-endpoint API for aggregated usage and cost data across every Telnyx product.
- **Session Analysis** — an API that reconstructs the full event and cost tree for an individual session, which is especially useful for multi-product AI calls.
- **On-Demand Reports** — a natural-language interface in the Mission Control Portal that translates plain-English questions into Usage Report queries.

Together they cover both programmatic, bulk reporting and ad-hoc, conversational exploration of the same underlying usage data.
