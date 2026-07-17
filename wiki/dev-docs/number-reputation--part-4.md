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

*Part 4 of 6 — see also: [Part 1](number-reputation--part-1.md), [Part 2](number-reputation--part-2.md), [Part 3](number-reputation--part-3.md), [Part 5](number-reputation--part-5.md), [Part 6](number-reputation--part-6.md)*

Number Reputation is a Telnyx monitoring product that reports the spam reputation of US outbound calling numbers. It is governed by separate Terms of Service from Branded Calling and requires an Enterprise, an accepted ToS, a signed Letter of Authorization, and two independent approval gates (reputation `status` and `loa_status`) before phone numbers can be associated, queried, auto-refreshed, and submitted for remediation.

## Phone Number Reputation

Once your enterprise is approved for Number Reputation — both reputation `status` **and** `loa_status` read `approved` — you can associate phone numbers for monitoring. Each number gets its own reputation data with spam risk levels and granular scores.

### Associate phone numbers

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12025551234", "+12025555678"]
  }'
```

- Up to **100 numbers** per request
- **Atomic operation** — all numbers succeed or all fail
- Numbers must be **US** numbers in **E.164 format** (`+1NPANXXXXXX`) — non-US numbers are rejected
- Numbers must be in-service and belong to your Telnyx phone-number inventory

Adding numbers is a **billable action**.

### Reputation data model

Each number returns a `reputation_data` object. The object is **`null` until the first refresh has been collected**, and every field inside it is nullable:

```
{
  "data": {
    "id": "16286ab3-038a-4a5c-9792-309026cf6b9e",
    "phone_number": "+12025551234",
    "enterprise_id": "4a6192a4-573d-446d-b3ce-aff9117272a6",
    "reputation_data": {
      "spam_risk": "low",
      "spam_category": null,
      "maturity_score": 82,
      "connection_score": 75,
      "engagement_score": 68,
      "sentiment_score": 90,
      "last_refreshed_at": "2026-03-24T12:00:00Z"
    },
    "created_at": "2026-04-26T18:06:51.940749Z",
    "updated_at": "2026-04-26T18:09:24.785211Z"
  }
}
```

**Spam risk:**

| Value | Meaning |
| --- | --- |
| `low` | Number has a clean reputation |
| `medium` | Some risk indicators present — the number may have been labeled as spam in the recent past |
| `high` | Number is likely flagged as spam by carriers |
| `null` | Not enough data yet |

**Granular scores (0-100):**

| Score | What it measures |
| --- | --- |
| `maturity_score` | How established the number is — based on call volume history over time. Available immediately after registration. |
| `connection_score` | Whether recipients choose to answer calls from this number. |
| `engagement_score` | Whether recipients stay on the call after answering. |
| `sentiment_score` | Whether recipients complain about or block calls from this number. |

A `null` score means there isn't enough data to make a determination. `maturity_score` is available immediately after registration because it uses pre-existing call traffic data. The other three scores start as `null` and populate after the number has sufficient call volume (minimum 4 hours, longer for low-volume numbers). Scores are updated hourly.

**Spam categories:**

If a number is flagged, `spam_category` is the category label assigned to it by the reputation feed. Known values include:

| Category | Description |
| --- | --- |
| `Telemarketer` | Number is flagged as a telemarketing caller |
| `Survey` | Number is flagged as a survey/polling caller |
| `Debt Collector` | Number is flagged as a debt collection caller |
| `Nonprofit` | Number is flagged as a nonprofit/fundraising caller |
| `Political` | Number is flagged as a political campaign caller |

Treat the field as an opaque string — the set may grow over time. It is `null` when the number is not flagged.

### List all monitored numbers

```
curl "https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Supports pagination with `page[number]` and `page[size]` query parameters. Page numbering is **1-based**; for this enterprise-scoped endpoint `page[size]` **defaults to 10** and is capped at 250. You can also filter by phone number with `filter[phone_number][contains]` (partial match) or `filter[phone_number][eq]` (exact match).

```
curl -g "https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers?page[number]=1&page[size]=20" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The simplified list endpoint (`/v2/reputation/numbers`) defaults to a `page[size]` of **20**, while this enterprise-scoped endpoint defaults to **10**. Pass `page[size]` explicitly if you depend on a specific page size.

### Force a refresh

Refresh the stored reputation data for specific numbers immediately, in addition to the scheduled `check_frequency`:

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/refresh \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12025551234"]
  }'
```

Up to 100 numbers per call. The response reports the per-number outcome:

```
{
  "data": {
    "results": [
      { "phone_number": "+12025551234", "success": true, "error": null }
    ],
    "total_requested": 1,
    "total_successful": 1,
    "total_failed": 0
  }
}
```

Forcing a refresh performs live reputation lookups, which are billable. Refreshes are subject to per-enterprise rate limits.

### Simplified endpoints

If your account has only one enterprise, you can skip the `enterprise_id` path parameter:

| Method | Simplified path |
| --- | --- |
| GET | `/v2/reputation/numbers` |
| GET | `/v2/reputation/numbers/{phone_number}` |
| DELETE | `/v2/reputation/numbers/{phone_number}` |

Remember to URL-encode the `+` as `%2B` in the `{phone_number}` path:

```
# List all monitored numbers (simplified)
curl https://api.telnyx.com/v2/reputation/numbers \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get reputation for a specific number (simplified)
curl https://api.telnyx.com/v2/reputation/numbers/%2B12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"

# Remove a specific number (simplified)
curl -X DELETE https://api.telnyx.com/v2/reputation/numbers/%2B12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```
