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

*Part 3 of 6 — see also: [Part 1](number-reputation--part-1.md), [Part 2](number-reputation--part-2.md), [Part 4](number-reputation--part-4.md), [Part 5](number-reputation--part-5.md), [Part 6](number-reputation--part-6.md)*

Number Reputation is a Telnyx monitoring product that reports the spam reputation of US outbound calling numbers. It is governed by separate Terms of Service from Branded Calling and requires an Enterprise, an accepted ToS, a signed Letter of Authorization, and two independent approval gates (reputation `status` and `loa_status`) before phone numbers can be associated, queried, auto-refreshed, and submitted for remediation.

## Letter of Authorization (LOA)

Before Telnyx can register your phone numbers with the major call-analytics networks used by US carriers, you must provide a signed **Letter of Authorization (LOA)**. The LOA authorizes Telnyx to manage your numbers' reputation on your behalf. The LOA is the **#1 thing customers get stuck on**, so follow the steps in order.

There are two separate approval gates you must clear before you can add phone numbers:

1. Reputation `status` must be `approved` (the activation lifecycle).
2. `loa_status` must be `approved` (Telnyx reviews the signed LOA).

Both must be `approved`. They are tracked independently.

### LOA approval gate

| `loa_status` | Meaning |
| --- | --- |
| `pending` | Telnyx is reviewing the uploaded LOA. Numbers cannot be added yet. |
| `approved` | LOA accepted. Combined with reputation `status` = `approved`, you can add numbers. |
| `rejected` | LOA was not accepted. Replace it to retry. |

Reputation `status` and `loa_status` are **two separate gates**. Both must read `approved` before `POST .../reputation/numbers` will accept numbers.

### Replace a pending or rejected LOA

If your LOA is `rejected` — or it is still `pending` and you need to upload a corrected document — render a fresh PDF, sign and upload it to the Documents API to get a new `loa_document_id`, then point your reputation settings at it:

```
curl -X PATCH https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/loa \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "loa_document_id": "NEW_DOCUMENT_ID"
  }'
```

Replacing the LOA **resets `loa_status` back to `pending`**. The new document must be approved again before more numbers can be added. This is the recovery path for a rejected LOA.

You can only replace the LOA while `loa_status` is `pending` or `rejected`. Once `loa_status` is `approved`, the document is locked in and this `PATCH` returns **`400 Bad Request`** ("The authorization document cannot be changed after it has been approved."). To start over with a different LOA after approval, disable Number Reputation and re-enable it with the new document.

## Number Reputation Settings

Number Reputation Settings control the monitoring lifecycle for your enterprise. You enable reputation monitoring, configure how often numbers are checked, and manage the vetting status.

### Prerequisites

Before enabling Number Reputation, you need:

1. An [Enterprise](enterprises.md) registered on your account — an Enterprise can serve Number Reputation, Branded Calling, or both.
2. A signed **Letter of Authorization (LOA)** rendered, signed, and uploaded to the Documents API to obtain a `loa_document_id`. The LOA authorizes Telnyx to register your numbers with the major call-analytics networks used by US carriers.
3. Agreement to the Number Reputation [Terms of Service](https://telnyx.com/terms/reputation-services).

### Enable Number Reputation

Submit your LOA document ID to enable reputation monitoring:

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "loa_document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
    "check_frequency": "business_daily"
  }'
```

`check_frequency` is optional and defaults to `business_daily`. Your enterprise details are submitted for automated vetting. This typically takes **minutes**. Enabling reputation is a **billable action**. Enabling returns **`403`** if you have not agreed to the Number Reputation Terms of Service.

### Two approval gates

Two statuses must each read `approved` before you can add phone numbers — they are tracked independently:

| Status | Meaning |
| --- | --- |
| `status` | Activation lifecycle of the enterprise's reputation. `pending` → `approved` / `rejected`. |
| `loa_status` | Telnyx's review of the signed LOA. `pending` → `approved` / `rejected`. |

`status` and `loa_status` are **two separate gates**. Both must be `approved` before `POST .../reputation/numbers` will accept numbers. A `rejected` `loa_status` is recoverable — replace the LOA per the [Letter of Authorization (LOA)](letter-of-authorization-loa.md) guide.

### Vetting lifecycle

```
pending ──► approved    (activation approved)
pending ──► rejected    (check rejection_reasons in the response)
approved ──► (removed)   (reputation disabled via DELETE)
```

Once you disable reputation, the settings are removed: a subsequent `GET .../reputation` returns **`404 Not Found`** rather than a readable status. Check your current status:

```
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The response includes:

| Field | Description |
| --- | --- |
| `status` | Activation lifecycle: `pending`, `approved`, or `rejected`. (After you disable reputation the settings are removed and `GET` returns `404` instead of a status.) |
| `loa_status` | LOA review gate: `pending`, `approved`, or `rejected`. |
| `check_frequency` | Current auto-refresh schedule. |
| `loa_document_id` | Your uploaded LOA reference (nullable). |
| `rejection_reasons` | Array of reasons, populated when `status` is `rejected` (otherwise `null`). |
| `created_at` / `updated_at` | Timestamps. |

### Auto-refresh schedules

Telnyx automatically runs fresh reputation queries on all your registered numbers based on the configured `check_frequency`:

| Frequency | Schedule |
| --- | --- |
| `business_daily` | Mon-Fri **(default)** |
| `daily` | Every day including weekends |
| `weekly` | Once per week |
| `biweekly` | Every 2 weeks |
| `monthly` | Once per month |
| `never` | Manual only — use `?fresh=true` or a forced refresh |

**Change the schedule:**

```
curl -X PATCH https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/frequency \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"check_frequency": "daily"}'
```

The enterprise's reputation `status` must be `approved`. A frequency change requested while `status` is still `pending` is rejected with **`400 Bad Request`**. Choose a frequency that balances data freshness with cost. Each auto-refresh counts as a billed query per number.

### Disable Number Reputation

To stop monitoring entirely and remove the enterprise from reputation tracking:

```
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

This de-registers your numbers from the reputation feed and removes the reputation settings. A subsequent `GET .../reputation` returns `404 Not Found`; to monitor again you must re-enable with a fresh LOA.
