---
title: Phone Number Reputation
summary: Associate phone numbers for monitoring, query spam scores and risk levels, and manage ongoing reputation tracking.
sources:
  - url: https://developers.telnyx.com/docs/branded-calling/number-reputation/phone-numbers
    content_hash: afbbbe00046fb00b7aecf5eccc10c851e1de3287994d403b7e38d0eb664b7cba
updated_at: 2026-04-10T00:00:00Z
---

# Phone Number Reputation

Associate phone numbers for monitoring, query spam scores and risk levels, and manage ongoing reputation tracking.

## Overview

Once your enterprise is [approved for Number Reputation](number-reputation-settings.md), you can associate phone numbers for monitoring. Each number gets its own reputation data with spam risk levels and granular scores.

## Associate phone numbers

Add phone numbers for reputation monitoring:

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12025551234", "+12025555678"]
  }'
```

* Up to **100 numbers** per request
* **Atomic operation** — all numbers succeed or all fail
* Numbers must be **US local** in **E.164 format**
* Numbers must be in-service and belong to your account

## Query reputation

### Cached query (free)

Returns the most recent stored reputation data:

```bash theme={null}
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/+12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Fresh query (billed)

Fetches live data from Hiya:

```bash theme={null}
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/+12025551234?fresh=true \
  -H "Authorization: Bearer YOUR_API_KEY"
```

If no cached data exists for a number, a fresh query is automatically triggered regardless of the `fresh` parameter.

## Reputation data model

Each number returns a `reputation_data` object:

```json theme={null}
{
  "data": {
    "phone_number": "+12025551234",
    "reputation_data": {
      "spam_risk": "low",
      "spam_category": null,
      "maturity_score": 82,
      "connection_score": 75,
      "engagement_score": 68,
      "sentiment_score": 90,
      "last_refreshed_at": "2026-03-24T12:00:00Z"
    }
  }
}
```

### Spam risk

| Value    | Meaning                                      |
| :------- | :------------------------------------------- |
| `low`    | Number has a clean reputation                |
| `medium` | Some risk indicators present                 |
| `high`   | Number is likely flagged as spam by carriers |

### Granular scores (0–100)

| Score              | What it measures                                                      |
| :----------------- | :-------------------------------------------------------------------- |
| `maturity_score`   | How established the number is based on calling history over time      |
| `connection_score` | How often recipients answer calls from this number                    |
| `engagement_score` | Whether recipients stay on the call after answering                   |
| `sentiment_score`  | Whether recipients want ongoing contact (blocking/reporting behavior) |

A `null` score means there isn't enough data to make a determination.

### Spam categories

If a number is flagged, `spam_category` indicates the label assigned by analytics engines: "Telemarketer", "Survey", "Debt Collector", "Nonprofit", "Political", etc.

## List all monitored numbers

```bash theme={null}
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Supports pagination with `page[number]` and `page[size]` query parameters.

## Remove a number from monitoring

```bash theme={null}
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/+12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Simplified endpoints

If your account has only one enterprise, you can skip the `enterprise_id` path parameter:

| Method | Simplified path                         |
| :----- | :-------------------------------------- |
| GET    | `/v2/reputation/numbers`                |
| GET    | `/v2/reputation/numbers/{phone_number}` |
| DELETE | `/v2/reputation/numbers/{phone_number}` |

```bash theme={null}


## Related Pages

- [Number Reputation](../runbooks/number-reputation.md)
- [Number Reputation Settings](../runbooks/number-reputation-settings.md)
- [Number Reputation Quickstart](../tutorial/number-reputation-quickstart.md)
- [Number Reservations](../runbooks/number-reservations.md)
- [Phone Number Messaging Configuration](../runbooks/phone-number-messaging-configuration.md)
