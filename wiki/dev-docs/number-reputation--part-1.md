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

*Part 1 of 6 — see also: [Part 2](number-reputation--part-2.md), [Part 3](number-reputation--part-3.md), [Part 4](number-reputation--part-4.md), [Part 5](number-reputation--part-5.md), [Part 6](number-reputation--part-6.md)*

Number Reputation is a Telnyx monitoring product that reports the spam reputation of US outbound calling numbers. It is governed by separate Terms of Service from Branded Calling and requires an Enterprise, an accepted ToS, a signed Letter of Authorization, and two independent approval gates (reputation `status` and `loa_status`) before phone numbers can be associated, queried, auto-refreshed, and submitted for remediation.

## Overview

Number Reputation lets you query the spam reputation of your outbound calling phone numbers. For each number you get a reputation snapshot with spam risk level, granular scores, and a category label when the number is flagged. Number Reputation is a **standalone monitoring product** — it reports spam reputation and does not change how your calls are placed. It is governed by separate [Terms of Service](https://telnyx.com/terms/reputation-services) from Branded Calling, and is currently supported in the **US only** (Canadian numbers are not accepted).

## How it works

1. **Register your business** as an [Enterprise](enterprises.md) — an Enterprise can serve Number Reputation, Branded Calling, or both.
2. **Accept the Number Reputation Terms of Service** — a one-time step per account.
3. **Render, sign, and upload a Letter of Authorization (LOA)** to get a `loa_document_id` — see [Letter of Authorization (LOA)](letter-of-authorization-loa.md).
4. **Enable Number Reputation** with that `loa_document_id` (billable) — your details are submitted for automated vetting (takes minutes).
5. **Wait for both approval gates** — reputation `status` **and** `loa_status` must each be `approved`.
6. **Associate phone numbers** for monitoring (up to 100 per request, US numbers, E.164) — billable.
7. **Query reputation scores** — cached results are free, fresh (live) queries are billed.
8. **Automatic monitoring** re-checks your numbers on a configurable schedule.
9. **Remediate flagged numbers** — submit numbers for re-evaluation when spam risk is elevated.

## Resource hierarchy

```
Enterprise (your organization, registered once — shared with Branded Calling)
├── Number Reputation Settings (per-enterprise monitoring configuration)
│   ├── LOA Document (Letter of Authorization)
│   ├── Auto-refresh Schedule (business_daily, daily, weekly, biweekly, monthly, never)
│   └── Reputation Phone Numbers
│       └── Phone Number (+1NPANXXXXXX)
│           └── Reputation Data (spam_risk, scores, spam_category, last_refreshed_at)
├── Remediation Requests (batch re-evaluation of flagged numbers)
│   └── Remediation Phone Numbers (up to 2,000 per request)
└── Terms of Service Agreement (Number Reputation)
```

- An **Enterprise** can serve Number Reputation, Branded Calling, or both — you don't need to create a separate Enterprise for each product.
- **Number Reputation Settings** are per-enterprise: one LOA, one auto-refresh schedule, one activation lifecycle.
- Each **Phone Number** gets its own reputation data with spam risk levels and granular scores.
- **Remediation Requests** are batch submissions of flagged numbers for re-evaluation.

## Key concepts

| Term | Description |
| --- | --- |
| **Enterprise** | Your top-level business registration. Shared with Branded Calling. Required before enabling reputation monitoring. |
| **Letter of Authorization (LOA)** | A signed document authorizing Telnyx to manage your numbers' reputation with call-analytics networks. |
| **Reputation data** | Per-number snapshot: `spam_risk`, `spam_category`, four granular scores, and `last_refreshed_at`. |
| **Auto-refresh** | Scheduled re-checking of your numbers' reputation data. Configurable frequency. |
| **Remediation** | A request to call-analytics networks to re-evaluate a flagged number's classification. |
| **Terms of Service** | Separate from Branded Calling. Must be accepted before enabling monitoring. |

## Constraints

| Constraint | Limit |
| --- | --- |
| Phone number format | E.164 (`+1NPANXXXXXX`), US numbers only |
| Numbers per request | 100 (atomic — all-or-nothing) |
| Score range | 0-100 (`null` = insufficient data) |
| Account access | Verified and enterprise-level accounts only |
| Approval gates | Both reputation `status` **and** `loa_status` must be `approved` before numbers can be added |
| Terms of Service | Must be accepted before enabling (separate from Branded Calling ToS) |

## Ecosystem

Reputation data is sourced from the major call-analytics networks used by US carriers. When you register numbers, Telnyx registers them across that reputation feed on your behalf. You interact only with the Telnyx API.
