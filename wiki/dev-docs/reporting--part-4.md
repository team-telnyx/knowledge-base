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

*Part 4 of 4 — see also: [Part 1](reporting--part-1.md), [Part 2](reporting--part-2.md), [Part 3](reporting--part-3.md)*

Telnyx provides several reporting tools for inspecting usage, costs, and session-level activity across its products. The Usage Reports API exposes aggregated, queryable usage data; Session Analysis reconstructs the full event and cost tree for individual sessions (especially AI-powered calls); and On-Demand Reports offers a natural-language interface on top of Usage Report data.

## On-Demand Reports

On-Demand Reports lets you query your Telnyx usage data using natural language. Instead of building filters and exporting CSVs, you describe the report you want in plain English and the system generates it.

### Overview

On-Demand Reports uses AI to translate natural language into structured queries against your [Usage Reports](usage-reports.md) data. You can request specific chart types, date ranges, groupings, and breakdowns — all from a single text input.

### Getting Started

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Navigate to **Reporting** > **[On-Demand Reports](https://portal.telnyx.com/#/reporting/on-demand-reports)**.
3. Type a query describing the report you need and submit it.

![On-Demand Reports query interface](https://mintcdn.com/telnyx/CK2IQbzSNcAAKyBl/img/on-demand-reports-interface.png?fit=max&auto=format&n=CK2IQbzSNcAAKyBl&q=85&s=9d46a27d7c53622e0f622c592cac3f68)

### Example Queries

- "Daily wireless spend for the last 10 days"
- "Number of messages by direction for last week as a pie chart"
- "Weekly total calls last quarter"
- "Average SIP cost for last 2 weeks as line graph"
- "SIP usage for the last month as a table"

### What You Can Do

| Capability | Description |
| --- | --- |
| Natural language queries | Describe reports in plain English instead of building filters manually |
| Chart type selection | Request bar charts, pie charts, line graphs, or tabular breakdowns |
| Date range control | Specify relative ("last 10 days") or absolute ("in February") time periods |
| Grouping and breakdowns | Group data by direction, product, day, week, or other dimensions |

### Current Limitations

- Queries run against **v2 Usage Report data** only. Products and dimensions available in Usage Reports are available here.
- **Not a general knowledge assistant** — the system answers questions about your Telnyx usage data, not general questions.
- This is the first release. Coverage and capabilities will expand over time.
