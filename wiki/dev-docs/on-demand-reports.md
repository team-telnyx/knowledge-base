---
title: On-Demand Reports
summary: On-Demand Reports lets you ask plain‑English questions about your Telnyx
  usage and costs, then turns them into structured queries against your v2 Usage Reports
  data to return charts or tables directly in the Mission Control Portal.
sources:
- url: https://developers.telnyx.com/docs/reporting/on-demand-reports/index
  content_hash: 92f45cae00d665c64d2ea9d24e6f64cacee00dc8025efc4ebb5fe540fdf473ee
- url: https://developers.telnyx.com/docs/reporting/session-analysis
  content_hash: cec6220dc372b663503187f3523e10a32b9c56acb38ede20db0af13a7686ba61
- url: https://developers.telnyx.com/docs/reporting/usage-reports/index
  content_hash: ce62ebf4872249bef8ee242f81feff9f400734437ba832ce0b388171fb4bd8e8
updated_at: 2026-05-20T09:28:32Z
---

# On-Demand Reports

On-Demand Reports lets you ask plain‑English questions about your Telnyx usage and costs, then turns them into structured queries against your v2 Usage Reports data to return charts or tables directly in the Mission Control Portal.

## Overview
On-Demand Reports converts natural‑language prompts into structured queries that run against your v2 usage dataset. You can ask for specific chart types, time ranges, and breakdowns (for example, by direction or product) and get instant visualizations without building filters manually.

## How it works
- Your prompt is translated into a query over the same data surface used by [Usage Reports](usage-reports.md).
- Supported dimensions and metrics, product coverage, and date rules mirror the v2 Usage Reports API.
- Results can be rendered as bar, line, pie, or table outputs, based on what you request in the prompt.

## Getting started in Mission Control
1. Log in to the Mission Control Portal: https://portal.telnyx.com
2. Go to Reporting > On-Demand Reports.
3. Enter a prompt describing what you want, such as “Daily wireless spend for the last 10 days as a line chart,” then submit.

## Writing effective queries
- State the product or domain: “wireless,” “messaging,” “SIP,” “Voice API.”
- Specify the time period: relative (“last 2 weeks,” “last quarter”) or absolute (“in February,” “2024‑01‑01 to 2024‑01‑31”).
- Ask for a visualization: “as a pie chart,” “bar chart,” “line graph,” or “as a table.”
- Add breakdowns: “by direction,” “by country,” “by day/week,” “by messaging profile,” etc.

## Examples
- “Daily wireless spend for the last 10 days”
- “Number of messages by direction for last week as a pie chart”
- “Weekly total calls last quarter”
- “Average SIP cost for last 2 weeks as line graph”
- “SIP usage for the last month as a table”

## Capabilities
- Natural language queries over your usage and cost data
- Choice of bar, pie, line, or tabular outputs
- Flexible date ranges: relative (for example, “last 10 days”) or absolute (“in February 2026”)
- Grouping and breakdowns by common dimensions (for example, direction, product, day/week)

## Data sources and coverage
On-Demand Reports queries the v2 dataset behind [Usage Reports](usage-reports.md). Coverage and available fields follow that API’s product catalogs, dimensions, and metrics. Example supported products include:
- Sip‑Trunking (sip‑trunking)
- Messaging (messaging)
- Voice API (call‑control)
- Wireless (wireless)
- Cloud Storage (cloud‑storage)
- Inference (inference)
- Verify 2FA (verify‑2fa)
- Fax API (fax‑api)
- WebRTC (webrtc)
- Calls per Second (cps)
- Conference (conference)
- Video API (programmable‑video)
- Call Control Features (call‑control‑features)
- Customer Service Record (customer‑service‑record)
- Media Streaming (media‑streaming)
- Noise Suppression (noise‑suppression)
- Text to Speech (text‑to‑speech)
- Speech to Text (speech‑to‑text)
- Recording (recording)
- Forking (forking)
- Media Storage (media‑storage)
- Answering Machine Detection (amd)

Note: Availability of specific dimensions/metrics varies by product. If a prompt requests an unsupported field, the system may return an error or a simplified result.

## Date ranges and time zones
- The underlying v2 API supports relative date literals (for example, date_range=last_1_weeks) and explicit timestamps.
- Start dates are inclusive; end dates are exclusive in the API (for example, February is 2024‑02‑01 00:00:00 to 2024‑03‑01 00:00:00).
- Maximum report window is 31 days per query in the API.
- Billing usage is calculated in UTC. You can break down results by calendar day (date) or hour (date_time) dimensions when needed.

## Charting and grouping options
You can request:
- Chart type: bar, line, pie, or a simple table
- Time granularity: daily, weekly (implied by “by week”), or hourly via the underlying date_time dimension
- Breakdowns: by direction, product, country, connection/profile, and other product‑specific dimensions supported in [Usage Reports](usage-reports.md)

## When to use Session Analysis instead
Use [Session Analysis](session-analysis.md) when you need per‑session forensics rather than aggregate trends. Session Analysis builds a full event tree for one session, showing:
- Parent/child relationships across products (for example, call session → call control → AI voice assistant → inference turns)
- Per‑event and cumulative costs rolled up to the session total
- Links back to underlying detail records for troubleshooting and auditing
Choose On‑Demand Reports for trend monitoring and aggregated KPIs across time; choose Session Analysis to debug or cost‑analyze a specific call, conversation, or workflow.

## Tips and best practices
- Be explicit: include product, time range, and desired breakdowns in your prompt.
- Start broad, then refine: first get totals; then add breakdowns (for example, by direction or country) to pinpoint drivers.
- Need an export or programmatic integration? Use the [Usage Reports](usage-reports.md) API directly; it returns JSON and can also generate CSV (format=csv).

## Limitations
- Runs on v2 Usage Reports data only; the products and dimensions available there define what you can ask here.
- Not a general‑knowledge assistant; it answers about your Telnyx usage data only.
- Early release; coverage and capabilities will expand over time.

## Troubleshooting
- Missing metric or dimension: It may not be supported for the selected product in [Usage Reports](usage-reports.md). Try a different breakdown or remove that field.
- Empty or partial results: Check your time window (the API supports up to 31 days per query) and remember that billing usage is computed in UTC.
- Wrong visualization: Rephrase the prompt to explicitly request “as a bar chart/pie chart/line graph/as a table.”
- Need per‑session details or cost rollups: Switch to [Session Analysis](session-analysis.md).
