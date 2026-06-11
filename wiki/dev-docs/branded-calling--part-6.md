---
title: Branded Calling
summary: Branded Calling displays your verified business identity (name, logo, call
  reason) on recipients' phones before they answer, increasing answer rates and building
  trust. The product suite also includes Number Reputation, a standalone monitoring
  tool that reports spam risk scores for your outbound numbers.
sources:
- url: https://developers.telnyx.com/docs/branded-calling/bc-phone-numbers/index
  content_hash: debb007ee49891994ea401e02c887ad13b0521f0b89cddd7cb4421594a8e41d2
- url: https://developers.telnyx.com/docs/branded-calling/brands/index
  content_hash: d7dd6d2fc597ac691e1f0cc2e597d92b6ab715abbac6d5ec85737edafcd73ae4
- url: https://developers.telnyx.com/docs/branded-calling/call-reasons/index
  content_hash: 0b7d23e8323cf824998deb0018b22cfa92290e87ed5caa18348736228278aa0e
- url: https://developers.telnyx.com/docs/branded-calling/enterprises/index
  content_hash: ea494c25e5674f7af4d7bd93e8c97fa47e8495f74bed3bb664a5bfa9c99f4d0c
- url: https://developers.telnyx.com/docs/branded-calling/infringement-claims/index
  content_hash: 72fe22e5d63bb8c4ee9c974872c3753988b581e78f6520962276643f6cb2c233
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/index
  content_hash: c5c5b8ee48261de2fb805a21f1ca5cd4418f5401a23ed8a0ca6edec6c7c3c75d
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/loa
  content_hash: beda6ac9071f4a130bedcebb3cd5077ac68c0ca652598311f9f38947eba1b3a8
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/phone-numbers
  content_hash: e5d0d27ffcadb97813d905efd4e75d344b0859db71bfe57b4c9981098c9c09cc
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/quickstart
  content_hash: 60ead21d3f92cebde649908350018489c215df87a9222b2e06b556efb5b445eb
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/remediation
  content_hash: fa879241122ea6342b3ae622ae10c798755e316d4d5aafc63c9917641133e27f
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/settings
  content_hash: 2abbc661fd47fb2586a33628324c07c43d9f354776b3eba72d46df167a9f570b
- url: https://developers.telnyx.com/docs/branded-calling/overview
  content_hash: 2b42495e07c0ae08434015582c7d932a65cf52da73015c584ce70d8d2284dfaf
- url: https://developers.telnyx.com/docs/branded-calling/quickstart
  content_hash: 36004a809e0491b179b6814e6e8fd2de2b478785d3b52b1d02236c2cc8d55a2d
- url: https://developers.telnyx.com/docs/branded-calling/terms-of-service/index
  content_hash: 0e5c0224ea69ee19a62fa84db715f599ec276306ebd921c2bc405394d6cf9a8b
updated_at: 2026-06-11T10:26:56Z
---

# Branded Calling

*Part 6 of 6 — see also: [Part 1](branded-calling--part-1.md), [Part 2](branded-calling--part-2.md), [Part 3](branded-calling--part-3.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md)*

Branded Calling displays your verified business identity (name, logo, call reason) on recipients' phones before they answer, increasing answer rates and building trust. The product suite also includes Number Reputation, a standalone monitoring tool that reports spam risk scores for your outbound numbers.

## Number Reputation Phone Numbers and Monitoring

Once both approval gates are `approved`, associate phone numbers for reputation monitoring.

### Associate Phone Numbers

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12025551234", "+12025555678"]
  }'
```

- Up to **100 numbers** per request, **atomic** (all succeed or all fail).
- Numbers must be **US** numbers in **E.164 format**, in-service, and belong to your Telnyx inventory.
- Billable action.
- A freshly added number has `reputation_data: null` until the first refresh.

In request bodies, the leading `+` is written literally (`"+12025551234"`). In **path parameters**, URL-encode the `+` as `%2B`.

### Query Reputation

**Cached query** (free, once data exists):

```
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/%2B12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Fresh query** (billed — fetches live data from the reputation feed):

```
curl "https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/%2B12025551234?fresh=true" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

If no cached data exists, a fresh query is automatically triggered regardless of the `fresh` parameter — the first GET on a new number always returns live data and counts as a billed query.

### Reputation Data Model

```json
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

Every field inside `reputation_data` is nullable. The whole object is `null` until the first refresh.

### List All Monitored Numbers

```
curl "https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Supports pagination (`page[number]`, `page[size]`, 1-based). Defaults to `page[size]=10` for the enterprise-scoped endpoint (capped at 250). Filter with `filter[phone_number][contains]` (partial match) or `filter[phone_number][eq]` (exact match).

### Force a Refresh

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/refresh \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12025551234"]
  }'
```

Up to 100 numbers per call. Billable. Returns per-number outcome with `success` and `error` fields. Subject to per-enterprise rate limits.

### Remove a Number from Monitoring

```
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/%2B12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Simplified Endpoints

If your account has only one enterprise, you can skip the `enterprise_id`:

| Method | Simplified Path |
|--------|----------------|
| GET | `/v2/reputation/numbers` |
| GET | `/v2/reputation/numbers/{phone_number}` |
| DELETE | `/v2/reputation/numbers/{phone_number}` |

Remember to URL-encode the `+` as `%2B` in the path.

## Number Reputation Remediation

When a monitored number has an elevated `spam_risk`, you can submit it for **reputation remediation** — a request to the call-analytics networks to re-evaluate the number's classification. Remediation is **asynchronous** and does **not** guarantee removal from any spam or block list; it is a re-evaluation request only. Even after successful remediation, downstream spam filters and carriers may still block or label calls.

Both Number Reputation approval gates must be cleared and the Number Reputation ToS accepted before submitting remediation requests.

### Submit Numbers for Remediation

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
|-------|----------|-------------|
| `phone_numbers` | yes | E.164 format. **1 to 2,000** per request. Must belong to this enterprise. |
| `call_purpose` | yes | Free-text description (1–2,000 chars). |
| `contact_email` | no | Contact email for tracking (max 255 chars). |
| `webhook_url` | no | `https://` URL for status notifications (max 2,048 chars). |

Returns `202 Accepted` with initial `status` of `pending`. A number already in an in-flight remediation request returns `409 Conflict`. Numbers not belonging to this enterprise return `422 Unprocessable Entity`.

### Count Fields

| Field | Meaning |
|-------|----------|
| `phone_numbers_count` | Total numbers in the batch, including any later cancelled. |
| `phone_numbers_submitted` | Numbers accepted for remediation (queued + processed). |
| `phone_numbers_ineligible` | Numbers rejected before submission (e.g., in a cooldown window). |

### Get a Remediation Request

```
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/remediation/{request_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

A completed request includes populated `results` with per-number outcome buckets. Not found or wrong enterprise returns `404`.

### Remediation Status Values

| `status` | Meaning |
|----------|----------|
| `pending` | Accepted and queued. |
| `in_progress` | Under review by the analytics networks. |
| `completed` | Review finished. Inspect `results`. |
| `failed` | Could not be processed. |
| `cancelled` | Cancelled. |

`results` is `null` while pending and populated once results are available.

### Per-Number Result Buckets

Each number falls into exactly one bucket. Empty buckets are returned as empty arrays (never omitted):

| Bucket | Meaning |
|--------|----------|
| `remediated` | Successfully re-evaluated and cleared. |
| `not_flagged` | Not flagged, so no remediation needed. |
| `requires_review` | Needs further review; remains flagged. |
| `ineligible` | Rejected before submission (e.g., in cooldown). |
| `refused` | Re-evaluation declined; number remains flagged. |

### List Remediation Requests

```
curl -g "https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/remediation?page[number]=1&page[size]=20" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

List items are a **slim shape** — they omit `results`, `webhook_url`, and the count breakdown. Call GET by ID for full detail. Pagination is JSON:API, 1-based, `page[size]` defaults to 20 (max 250).

Filters:

| Filter | Description |
|--------|-------------|
| `filter[status]` | `pending`, `in_progress`, `completed`, `failed`, or `cancelled`. |
| `filter[created_at][gte]` | Created on or after an ISO 8601 timestamp. |
| `filter[created_at][lte]` | Created on or before an ISO 8601 timestamp. |
