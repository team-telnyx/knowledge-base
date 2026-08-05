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

*Part 4 of 5 — see also: [Part 1](number-reputation--part-1.md), [Part 2](number-reputation--part-2.md), [Part 3](number-reputation--part-3.md), [Part 5](number-reputation--part-5.md)*

Number Reputation is a Telnyx product that monitors the spam reputation of US outbound calling numbers by querying the major call-analytics networks used by US carriers. It exposes per-number spam risk, granular scores, and category labels, and supports batch remediation requests to re-evaluate flagged numbers. The product is governed by its own Terms of Service and is currently US-only.

## Reputation Remediation

When one of your monitored numbers is flagged with an elevated `spam_risk`, you can submit it for **reputation remediation** — a request to the call-analytics networks to re-evaluate the number's classification. You submit a batch of numbers, Telnyx forwards the request on your behalf, and you poll the request to track its status and per-number outcome.

Remediation is **asynchronous**. The submit call returns `202 Accepted` with a request id; the request then moves through processing states until it completes. Use the GET endpoints to poll status and per-number results.

Submitting a remediation request does **not** guarantee a number will be removed from any spam or block list. Remediation is a **re-evaluation request** to the call-analytics networks — the outcome may be that the number remains flagged (`requires_review` or `refused`).

Even after a number is successfully remediated, calls from it can **still be blocked or labeled** by downstream spam filters and carriers. Those systems are outside Telnyx's control, and a successful remediation does not override them.

Both Number Reputation approval gates must be cleared (reputation `status` **and** `loa_status` both `approved`) and the Number Reputation Terms of Service accepted before you can submit remediation requests.

### Submit numbers for remediation

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/remediation \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12025551234", "+12025555678"],
    "call_purpose": "Outbound appointment reminders for our dental clinic.",
    "contact_email": "ops@example.com",
    "webhook_url": "https://example.com/hooks/remediation"
  }'
```

| Field | Required | Description |
| --- | --- | --- |
| `phone_numbers` | yes | Phone numbers in E.164 format. **1 to 2,000** per request. Must belong to this enterprise. |
| `call_purpose` | yes | Free-text description of how the numbers are used (1 to 2,000 chars). |
| `contact_email` | no | A contact email for this remediation request, used for tracking and any follow-up (max 255 chars). |
| `webhook_url` | no | Optional `https://` URL to receive status notifications (max 2,048 chars). |

The endpoint returns **`202 Accepted`** with the persisted request and its initial `status` of `pending`:

```
{
  "data": {
    "id": "9f1c8a2e-5b3d-4e7a-9c11-2a6f0d3b4c55",
    "status": "pending",
    "phone_numbers_count": 2,
    "phone_numbers_submitted": 2,
    "phone_numbers_ineligible": 0,
    "call_purpose": "Outbound appointment reminders for our dental clinic.",
    "contact_email": "ops@example.com",
    "webhook_url": "https://example.com/hooks/remediation",
    "created_at": "2026-06-07T18:06:51.940749Z",
    "updated_at": "2026-06-07T18:06:51.940749Z",
    "tier1_completed_at": null,
    "tier2_completed_at": null,
    "results": null
  }
}
```

A number that already has an in-flight remediation request cannot be submitted again — the request returns **`409 Conflict`**. Numbers that do not belong to this enterprise return **`422 Unprocessable Entity`**.

### Count fields

| Field | Meaning |
| --- | --- |
| `phone_numbers_count` | Total numbers in the batch, including any later cancelled. May exceed the sum of the per-category result buckets. |
| `phone_numbers_submitted` | Numbers accepted for remediation (not rejected as ineligible). Counts numbers still queued as well as processed ones. |
| `phone_numbers_ineligible` | Numbers rejected before submission (for example, in a cooldown window). |

### Get a remediation request

Retrieve full detail for one request, including per-number results once they are available:

```
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/remediation/9f1c8a2e-5b3d-4e7a-9c11-2a6f0d3b4c55 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

A completed request includes the populated `results` object:

```
{
  "data": {
    "id": "9f1c8a2e-5b3d-4e7a-9c11-2a6f0d3b4c55",
    "status": "completed",
    "phone_numbers_count": 2,
    "phone_numbers_submitted": 2,
    "phone_numbers_ineligible": 0,
    "call_purpose": "Outbound appointment reminders for our dental clinic.",
    "contact_email": "ops@example.com",
    "webhook_url": "https://example.com/hooks/remediation",
    "created_at": "2026-06-07T18:06:51.940749Z",
    "updated_at": "2026-06-07T19:42:10.112233Z",
    "tier1_completed_at": "2026-06-07T19:10:04.000000Z",
    "tier2_completed_at": "2026-06-07T19:42:10.000000Z",
    "results": {
      "remediated": ["+12025551234"],
      "not_flagged": [],
      "requires_review": ["+12025555678"],
      "ineligible": [],
      "refused": []
    }
  }
}
```

A request that is not found — or does not belong to this enterprise — returns **`404 Not Found`**.

### Status values

`status` is the customer-facing meta-status:

| `status` | Meaning |
| --- | --- |
| `pending` | Request accepted and queued; not yet forwarded for review. |
| `in_progress` | Forwarded and under review by the call-analytics networks. |
| `completed` | Review finished. Inspect `results` for the per-number outcome. |
| `failed` | The request could not be processed. |
| `cancelled` | The request was cancelled. |

`results` is `null` while the request is still pending and is populated once results are available.

### Per-number result buckets

When `results` is populated, each number falls into exactly one bucket. Empty buckets are returned as empty arrays (never omitted), so you can iterate without null-checking each key:

| Bucket | Meaning |
| --- | --- |
| `remediated` | The number's classification was successfully re-evaluated and cleared. |
| `not_flagged` | The number was not flagged, so no remediation was needed. |
| `requires_review` | The number needs further review and remains flagged for now. |
| `ineligible` | The number was rejected before submission (for example, in a cooldown window). |
| `refused` | The re-evaluation request was declined; the number remains flagged. |

A number landing in the `remediated` bucket means the analytics networks re-evaluated and cleared it — it does **not** guarantee the number is removed from every spam list, and downstream carriers and spam filters may still block or label calls from it.

### List remediation requests

```
curl -g "https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/remediation?page[number]=1&page[size]=20" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

List items are a **slim shape** — they omit `results`, `webhook_url`, and the count breakdown. Call get by id for full detail.

```
{
  "data": [
    {
      "id": "9f1c8a2e-5b3d-4e7a-9c11-2a6f0d3b4c55",
      "status": "completed",
      "phone_numbers_count": 2,
      "call_purpose": "Outbound appointment reminders for our dental clinic.",
      "created_at": "2026-06-07T18:06:51.940749Z",
      "updated_at": "2026-06-07T19:42:10.112233Z",
      "tier1_completed_at": "2026-06-07T19:10:04.000000Z",
      "tier2_completed_at": "2026-06-07T19:42:10.000000Z"
    }
  ],
  "meta": {
    "page_number": 1,
    "page_size": 20,
    "total_results": 1,
    "total_pages": 1
  }
}
```

Pagination is JSON:API. Page numbering is **1-based**; `page[size]` **defaults to 20** and is capped at **250**.

### Filters

| Filter | Description |
| --- | --- |
| `filter[status]` | Filter by customer-facing status: `pending`, `in_progress`, `completed`, `failed`, or `cancelled`. |
| `filter[created_at][gte]` | Created on or after this ISO 8601 timestamp. |
| `filter[created_at][lte]` | Created on or before this ISO 8601 timestamp. |

```
curl -g "https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/remediation?filter[status]=completed&filter[created_at][gte]=2026-06-01T00:00:00Z" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Remediation webhooks

When you provide a `webhook_url` in the remediation request, Telnyx sends status notifications to that URL as the request progresses. The webhook events are:

| Event | Description |
| --- | --- |
| `number_reputation.remediation.tier1_complete` | First-tier review complete. The request continues to tier 2. |
| `number_reputation.remediation.completed` | Remediation finished. Inspect `results` for the per-number outcome. |
| `number_reputation.remediation.failed` | The request could not be processed. |

Webhook payloads include the remediation request `id`, `status`, and `results` (when populated). Ensure your webhook endpoint is publicly accessible and responds with `200` to acknowledge receipt.
