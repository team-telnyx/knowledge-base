---
title: Number Reputation
summary: Number Reputation is a Telnyx monitoring product that reports the spam reputation
  of US outbound calling numbers. It is governed by separate Terms of Service from
  Branded Calling and requires an Enterprise, an accepted ToS, a signed Letter of
  Authorization, and two independent approval gates (reputation `status` and `loa_status`)
  before phone numbers can be associated, queried, auto-refreshed, and submitted for
  remediation.
sources:
- url: https://developers.telnyx.com/docs/number-reputation/loa
- url: https://developers.telnyx.com/docs/number-reputation/overview
- url: https://developers.telnyx.com/docs/number-reputation/phone-numbers
- url: https://developers.telnyx.com/docs/number-reputation/pricing
- url: https://developers.telnyx.com/docs/number-reputation/quickstart
- url: https://developers.telnyx.com/docs/number-reputation/remediation
- url: https://developers.telnyx.com/docs/number-reputation/settings
updated_at: 2026-07-17T09:15:42Z
---

# Number Reputation

*Part 6 of 6 — see also: [Part 1](number-reputation--part-1.md), [Part 2](number-reputation--part-2.md), [Part 3](number-reputation--part-3.md), [Part 4](number-reputation--part-4.md), [Part 5](number-reputation--part-5.md)*

Number Reputation is a Telnyx monitoring product that reports the spam reputation of US outbound calling numbers. It is governed by separate Terms of Service from Branded Calling and requires an Enterprise, an accepted ToS, a signed Letter of Authorization, and two independent approval gates (reputation `status` and `loa_status`) before phone numbers can be associated, queried, auto-refreshed, and submitted for remediation.

## Pricing

Number Reputation pricing has three components:

| Component | Cost | Description |
| --- | --- |
| **Reputation monitoring** | $100/month per Enterprise | Recurring monthly fee to enable reputation monitoring on an enterprise. |
| **Reputation check** | $0.10 per check | Charged per reputation query. Cached reads are free; fresh (live) queries and auto-refreshes are billed. |
| **Remediation check** | $1.00 per check | Charged per number submitted for reputation remediation (re-evaluation). |

Rendering the LOA is **not billable**. You only pay once you enable reputation monitoring and add numbers. For the full pricing details, see the [Telnyx Numbers pricing page](https://telnyx.com/pricing/numbers).

### How billing works

| Action | Billed? |
| --- | --- |
| Render LOA PDF | No |
| Enable reputation monitoring | Yes ($100 MRC) |
| Add phone numbers | Yes ($0.10 per number per check) |
| Cached reputation query | No (free once data exists) |
| Fresh reputation query (`?fresh=true`) | Yes ($0.10 per check) |
| Forced refresh | Yes ($0.10 per check) |
| Auto-refresh (scheduled) | Yes ($0.10 per check per number) |
| Submit remediation request | Yes ($1.00 per number) |

Enterprise registration is free. An Enterprise can serve Number Reputation, Branded Calling, or both.
