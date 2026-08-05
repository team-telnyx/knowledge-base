---
title: Number Reputation
summary: Number Reputation is a Telnyx product that monitors the spam reputation of
  US outbound calling numbers by querying the major call-analytics networks used by
  US carriers. It exposes per-number spam risk, granular scores, and category labels,
  and supports batch remediation requests to re-evaluate flagged numbers. The product
  is governed by its own Terms of Service and is currently US-only.
sources:
- url: https://developers.telnyx.com/docs/number-reputation/loa
- url: https://developers.telnyx.com/docs/number-reputation/overview
- url: https://developers.telnyx.com/docs/number-reputation/phone-numbers
- url: https://developers.telnyx.com/docs/number-reputation/pricing
- url: https://developers.telnyx.com/docs/number-reputation/quickstart
- url: https://developers.telnyx.com/docs/number-reputation/remediation
- url: https://developers.telnyx.com/docs/number-reputation/settings
updated_at: 2026-08-05T14:00:24Z
---

# Number Reputation

*Part 1 of 5 — see also: [Part 2](number-reputation--part-2.md), [Part 3](number-reputation--part-3.md), [Part 4](number-reputation--part-4.md), [Part 5](number-reputation--part-5.md)*

Number Reputation is a Telnyx product that monitors the spam reputation of US outbound calling numbers by querying the major call-analytics networks used by US carriers. It exposes per-number spam risk, granular scores, and category labels, and supports batch remediation requests to re-evaluate flagged numbers. The product is governed by its own Terms of Service and is currently US-only.

## Overview

Number Reputation lets you query the spam reputation of your outbound calling phone numbers. For each number you get a reputation snapshot with spam risk level, granular scores, and a category label when the number is flagged.

Number Reputation is a **standalone monitoring product**. It reports spam reputation and does not change how your calls are placed. It is governed by separate [Terms of Service](https://telnyx.com/terms/reputation-services) from Branded Calling.

Number Reputation is currently supported in the **US only**. Canadian numbers are not accepted.

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

## Prerequisites

- A Telnyx account with **verified** or **enterprise** level access
- An [API key](https://portal.telnyx.com/#/app/api-keys)
- At least one US phone number on your account, in E.164 format
- A signed Letter of Authorization (LOA) — you render this from Telnyx in Step 3

## Step 1: Accept the Number Reputation Terms of Service

Read the full terms at [telnyx.com/terms/reputation-services](https://telnyx.com/terms/reputation-services).

```
curl -X POST https://api.telnyx.com/v2/terms_of_service/number_reputation/agree \
  -H "Authorization: Bearer YOUR_API_KEY"
```

This is a one-time step per account. If you skip it, **Step 5 (enable) returns `403`**.

To check whether you've already agreed, call `GET /v2/terms_of_service/status?product_type=number_reputation`. That endpoint **defaults to `branded_calling`**, so you must pass `product_type=number_reputation` to read the Number Reputation status. Likewise, `GET /v2/terms_of_service/agreements` also defaults to `branded_calling` — pass `?product_type=number_reputation` to scope the list to Number Reputation.

## Step 2: Create an enterprise

If you don't already have an enterprise, create one. An Enterprise can serve Number Reputation, Branded Calling, or both — you don't need a separate one. See the [Enterprises](enterprises.md) overview for the full field reference.

```
curl -X POST https://api.telnyx.com/v2/enterprises \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "legal_name": "Acme Plumbing LLC",
    "doing_business_as": "Acme Plumbing",
    "organization_type": "commercial",
    "organization_legal_type": "llc",
    "country_code": "US",
    "jurisdiction_of_incorporation": "Delaware",
    "website": "https://acmeplumbing.example.com",
    "fein": "12-3456789",
    "industry": "technology",
    "number_of_employees": "51-200",
    "organization_contact": {
      "first_name": "Sam",
      "last_name": "Owner",
      "email": "sam@acmeplumbing.example.com",
      "job_title": "Compliance Lead",
      "phone_number": "+13125550000"
    },
    "billing_contact": {
      "first_name": "Alex",
      "last_name": "Bill",
      "email": "billing@acmeplumbing.example.com",
      "phone_number": "+13125550001"
    },
    "organization_physical_address": {
      "country": "US",
      "administrative_area": "IL",
      "city": "Chicago",
      "postal_code": "60601",
      "street_address": "100 Main St"
    },
    "billing_address": {
      "country": "US",
      "administrative_area": "IL",
      "city": "Chicago",
      "postal_code": "60601",
      "street_address": "100 Main St"
    }
  }'
```

Save the `id` from the response — this is your `enterprise_id`.
