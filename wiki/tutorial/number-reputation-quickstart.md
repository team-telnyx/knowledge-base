---
title: Number Reputation Quickstart
summary: Step-by-step guide to set up Number Reputation and start monitoring your phone numbers' spam scores.
sources:
  - url: https://developers.telnyx.com/docs/branded-calling/number-reputation/quickstart
    content_hash: 2b1e348d6d9cc1e84f4bbc7db4a7de4b640515680b3c186ff9b5ac4b6b56ea44
updated_at: 2026-04-10T00:00:00Z
---

# Number Reputation Quickstart

Step-by-step guide to set up Number Reputation and start monitoring your phone numbers' spam scores.

This guide walks you through enabling Number Reputation and querying your first spam score. You'll need a [verified or enterprise-level Telnyx account](../runbooks/account-levels-and-capabilities.md) and an API key.

## Prerequisites

* A Telnyx account with **verified** or **enterprise** level access
* An [API key](https://portal.telnyx.com/#/app/api-keys)
* At least one US local phone number on your account
* A signed Letter of Authorization (LOA) from the business entity

## Step 1: Accept Terms of Service

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/terms_of_service/number_reputation/agree \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Step 2: Create an enterprise

If you don't already have an enterprise, create one. See the [Enterprises overview](https://developers.telnyx.com/docs/branded-calling/enterprises/overview) for full field reference.

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/enterprises \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "legal_name": "Acme Corp",
    "doing_business_as": "Acme",
    "organization_type": "commercial",
    "country_code": "US",
    "website": "https://acme.com",
    "fein": "12-3456789",
    "industry": "technology",
    "number_of_employees": "51-200",
    "organization_legal_type": "corporation",
    "organization_contact": {
      "first_name": "Jane",
      "last_name": "Smith",
      "email": "jane@acme.com",
      "job_title": "CTO",
      "phone": "+12025551234"
    },
    "billing_contact": {
      "first_name": "Jane",
      "last_name": "Smith",
      "email": "billing@acme.com",
      "phone_number": "+12025551234"
    },
    "organization_physical_address": {
      "country": "US",
      "administrative_area": "CA",
      "city": "San Francisco",
      "postal_code": "94105",
      "street_address": "123 Main St"
    },
    "billing_address": {
      "country": "US",
      "administrative_area": "CA",
      "city": "San Francisco",
      "postal_code": "94105",
      "street_address": "123 Main St"
    }
  }'
```

Save the `id` from the response — this is your `enterprise_id`.

## Step 3: Upload a Letter of Authorization

Upload a signed LOA using the Telnyx Documents API. The LOA authorizes Telnyx to register your numbers with third-party analytics providers on your behalf.

Save the `document_id` from the response.

## Step 4: Enable Number Reputation

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "loa_document_id": "YOUR_DOCUMENT_ID"
  }'
```

Your enterprise details are sent to Hiya for automated vetting. This typically takes **minutes**. The status will change from `pending` to `approved`.

Check the status:

```bash theme={null}
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Step 5: Associate phone numbers

Once your enterprise is approved, add phone numbers for monitoring:

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12025551234", "+12025555678"]
  }'
```

Up to 100 numbers per request. This is an atomic operation — all numbers succeed or all fail. Numbers must be US local in E.164 format.

## Step 6: Query reputation

### Cached (free)

```bash theme={null}
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/+12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Fresh — live query (billed)

```bash theme={null}
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/+12025551234?fresh=true \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The response includes:

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

## Step 7: Manage ongoing monitoring

### Change auto-refresh frequency

```bash theme={null}
curl -X PATCH https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/frequency \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"check_frequency": "daily"}'
```

### Remove a number from monitoring

```bash theme={null}
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/+12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Disable Number Reputation entirely

```bash theme={null}
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Simplified endpoints

If your account has only one enterprise, you can use simplified endpoints without the `enterprise_id`:

```bash theme={null}


## Related Pages

- [Number Reputation](../runbooks/number-reputation.md)
- [Number Reputation Settings](../runbooks/number-reputation-settings.md)
- [Phone Number Reputation](../runbooks/phone-number-reputation.md)
- [Inference API Quickstart](../tutorial/inference-api-quickstart.md)
- [Number Reservations](../runbooks/number-reservations.md)
