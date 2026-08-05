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

*Part 3 of 5 — see also: [Part 1](number-reputation--part-1.md), [Part 2](number-reputation--part-2.md), [Part 4](number-reputation--part-4.md), [Part 5](number-reputation--part-5.md)*

Number Reputation is a Telnyx product that monitors the spam reputation of US outbound calling numbers by querying the major call-analytics networks used by US carriers. It exposes per-number spam risk, granular scores, and category labels, and supports batch remediation requests to re-evaluate flagged numbers. The product is governed by its own Terms of Service and is currently US-only.

## Step 8: Query reputation

URL-encode the leading `+` of the phone number in the path as **`%2B`** — e.g. `+12025551234` becomes `%2B12025551234`.

### Cached query (free, once data exists)

Returns the most recent stored reputation data:

```
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/%2B12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The **first** query on a number with no cached reputation data triggers a live, **billed** lookup regardless of this endpoint; only subsequent reads are free.

### Fresh query (billed)

Fetches live data from the reputation feed:

```
curl "https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/%2B12025551234?fresh=true" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

If no cached data exists for a number, a fresh query is automatically triggered regardless of the `fresh` parameter — so a brand-new number always returns live data on its first GET (and counts as a billed query). If the analytics networks don't have data for the number yet, `reputation_data` will still be `null`.

Live (fresh) queries are billable. See [Number Reputation Pricing](number-reputation-pricing.md) for current pricing.

### Response shape

```
{
  "data": {
    "id": "8a4b1f5e-2f12-4c0c-9a98-9b3a7d8b8e62",
    "enterprise_id": "4a6192a4-573d-446d-b3ce-aff9117272a6",
    "phone_number": "+12025551234",
    "reputation_data": {
      "spam_risk": "low",
      "spam_category": null,
      "maturity_score": 82,
      "connection_score": 75,
      "engagement_score": 68,
      "sentiment_score": 90,
      "last_refreshed_at": "2026-04-26T18:09:24.785211Z"
    },
    "created_at": "2026-04-26T18:06:51.940749Z",
    "updated_at": "2026-04-26T18:09:24.785211Z"
  }
}
```

Every field in `reputation_data` is nullable, and the whole object is `null` until the first refresh has been collected.

## Reputation data model

Each registered number returns a `reputation_data` object with the following fields:

| Field | Values | Meaning |
| --- | --- | --- |
| `spam_risk` | `low` / `medium` / `high` / `null` | Overall spam-risk classification from the call-analytics networks used by US carriers. |
| `maturity_score` | 0-100 or `null` | How established the number is — based on call volume history over time. Available immediately after registration. |
| `connection_score` | 0-100 or `null` | Whether recipients choose to answer calls from this number. |
| `engagement_score` | 0-100 or `null` | Whether recipients stay on the call after answering. |
| `sentiment_score` | 0-100 or `null` | Whether recipients complain about or block calls from this number. |
| `spam_category` | string or `null` | Category label assigned by the reputation feed when the number is flagged. Treat as an opaque string — the set may grow over time. `null` means the number is not flagged. |
| `last_refreshed_at` | ISO 8601 timestamp or `null` | When the reputation data was last updated. `null` if no check has been performed yet. |

`maturity_score` is available immediately after registration because it uses pre-existing call traffic data. The other three scores start as `null` and populate after the number has sufficient call volume (minimum 4 hours, longer for low-volume numbers). Scores are updated hourly.

### Spam risk

| Value | Meaning |
| --- | --- |
| `low` | Number has a clean reputation |
| `medium` | Some risk indicators present — the number may have been labeled as spam in the recent past |
| `high` | Number is likely flagged as spam by carriers |
| `null` | Not enough data yet |

### Spam categories

If a number is flagged, `spam_category` is the category label assigned to it by the reputation feed. Known values include:

| Category | Description |
| --- | --- |
| `Telemarketer` | Number is flagged as a telemarketing caller |
| `Survey` | Number is flagged as a survey/polling caller |
| `Debt Collector` | Number is flagged as a debt collection caller |
| `Nonprofit` | Number is flagged as a nonprofit/fundraising caller |
| `Political` | Number is flagged as a political campaign caller |

Treat the field as an opaque string — the set may grow over time. It is `null` when the number is not flagged.

## List all monitored numbers

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

## Force a refresh

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

Forcing a refresh performs live reputation lookups, which are billable. See [Number Reputation Pricing](number-reputation-pricing.md) for current pricing. Refreshes are subject to per-enterprise rate limits.

## Auto-refresh schedules

Telnyx automatically runs fresh reputation queries on all your registered numbers based on the configured `check_frequency`:

| Frequency | Schedule |
| --- | --- |
| `business_daily` | Mon-Fri **(default)** |
| `daily` | Every day including weekends |
| `weekly` | Once per week |
| `biweekly` | Every 2 weeks |
| `monthly` | Once per month |
| `never` | Manual only — use `?fresh=true` or a forced refresh |

### Change the schedule

```
curl -X PATCH https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/frequency \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"check_frequency": "daily"}'
```

The enterprise's reputation `status` must be `approved`. A frequency change requested while `status` is still `pending` is rejected with **`400 Bad Request`**.

Choose a frequency that balances data freshness with cost. Each auto-refresh counts as a billed query per number — see [Number Reputation Pricing](number-reputation-pricing.md).

## Remove a number from monitoring

```
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/%2B12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Disable Number Reputation

To stop monitoring entirely and remove the enterprise from reputation tracking:

```
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

This de-registers your numbers from the reputation feed and removes the reputation settings. A subsequent `GET .../reputation` returns `404 Not Found`; to monitor again you must re-enable with a fresh LOA.
