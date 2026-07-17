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

*Part 2 of 6 — see also: [Part 1](number-reputation--part-1.md), [Part 3](number-reputation--part-3.md), [Part 4](number-reputation--part-4.md), [Part 5](number-reputation--part-5.md), [Part 6](number-reputation--part-6.md)*

Number Reputation is a Telnyx monitoring product that reports the spam reputation of US outbound calling numbers. It is governed by separate Terms of Service from Branded Calling and requires an Enterprise, an accepted ToS, a signed Letter of Authorization, and two independent approval gates (reputation `status` and `loa_status`) before phone numbers can be associated, queried, auto-refreshed, and submitted for remediation.

## Quickstart

You need a verified or enterprise-level Telnyx account, an API key, at least one US phone number on your account in E.164 format, and a signed LOA (rendered from Telnyx in Step 3).

### Step 1: Accept the Number Reputation Terms of Service

Read the full terms at [telnyx.com/terms/reputation-services](https://telnyx.com/terms/reputation-services).

```
curl -X POST https://api.telnyx.com/v2/terms_of_service/number_reputation/agree \
  -H "Authorization: Bearer YOUR_API_KEY"
```

This is a one-time step per account. If you skip it, **Step 5 (enable) returns `403`**.

To check whether you've already agreed, call `GET /v2/terms_of_service/status?product_type=number_reputation`. That endpoint **defaults to `branded_calling`**, so you must pass `product_type=number_reputation` to read the Number Reputation status. Likewise, `GET /v2/terms_of_service/agreements` also defaults to `branded_calling` — pass `?product_type=number_reputation` to scope the list to Number Reputation.

### Step 2: Create an enterprise

If you don't already have an enterprise, create one. An Enterprise can serve Number Reputation, Branded Calling, or both — you don't need a separate one.

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

### Step 3: Render the Letter of Authorization (LOA)

Telnyx renders a pre-filled LOA **PDF** from your enterprise record. You do **not** upload your own template — you render the Telnyx one, sign it, and upload the signed copy back.

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/loa \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -o loa.pdf \
  -d '{}'
```

The response body is the **PDF itself** (`application/pdf`); `-o loa.pdf` saves it to disk. Rendering the LOA is **not billable**.

**Optional body fields** (both optional):

| Field | Description |
| --- | --- |
| `agent` | A third-party reseller / partner block, used only when a partner manages the enterprise's numbers. Omit when the enterprise works directly with Telnyx. |
| `signature` | Embeds a signature image in the rendered PDF. When omitted, the PDF is returned **unsigned** for you to sign manually. |

To render with the agent (reseller) block:

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/loa \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -o loa.pdf \
  -d '{
    "agent": {
      "legal_name": "Reseller LLC",
      "dba": "Reseller",
      "street_address": "500 Market St",
      "extended_address": "Suite 200",
      "city": "San Francisco",
      "administrative_area": "CA",
      "postal_code": "94105",
      "country": "US",
      "contact_name": "Pat Partner",
      "contact_title": "Account Manager",
      "contact_email": "pat@reseller.com",
      "contact_phone": "+13125550000"
    }
  }'
```

To embed a signature at render time instead of signing the PDF by hand:

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/loa \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -o loa.pdf \
  -d '{
    "signature": {
      "image_base64": "BASE64_ENCODED_SIGNATURE_IMAGE",
      "signer_name": "Jane Smith"
    }
  }'
```

### Step 4: Sign the LOA and upload it to the Documents API

If you did not embed a `signature` at render time, open `loa.pdf` and sign it (e-signature or wet signature). Save the signed copy, then upload it to the [Telnyx Documents API](/api-reference/documents/upload-a-document):

```
curl -X POST https://api.telnyx.com/v2/documents \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@loa.pdf"
```

The response contains the document id:

```
{
  "data": {
    "id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c"
  }
}
```

Save `data.id` — you'll pass it as `loa_document_id` in the next step.

### Step 5: Enable Number Reputation

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "loa_document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
    "check_frequency": "business_daily"
  }'
```

`check_frequency` is optional and defaults to `business_daily`. Enabling reputation is a **billable action**.

### Step 6: Wait for both approval gates

Your enterprise details are submitted for automated vetting and Telnyx reviews your signed LOA. Poll the reputation settings until **both** `status` and `loa_status` read `approved`:

```
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

```
{
  "data": {
    "status": "approved",
    "loa_status": "approved"
  }
}
```

| Field | Gate |
| --- | --- |
| `status` | Activation lifecycle: `pending` → `approved` (or `rejected` — see `rejection_reasons`). |
| `loa_status` | LOA review: `pending` → `approved` (or `rejected` — replace the LOA). |

You **cannot add numbers** until both are `approved`.

### Step 7: Associate phone numbers

Once both gates are `approved`, add phone numbers for monitoring:

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12025551234", "+12025555678"]
  }'
```

Up to 100 numbers per request. This is an atomic operation — all numbers succeed or all fail. Numbers must be **US** numbers in E.164 format (`+1NPANXXXXXX`), in-service, and belong to your Telnyx phone-number inventory. Non-US numbers are rejected. Adding numbers is a **billable action**.

In the request body, phone numbers are JSON string values, so the leading `+` is written literally (`"+12025551234"`). In **path parameters** (the get/delete-by-number endpoints below) URL-encode the `+` as **`%2B`**.

A freshly added number has `reputation_data: null` until Telnyx collects its first refresh. Querying it (Step 8) triggers an immediate lookup. Because the number has no cached data yet, that first query performs a **live (billed)** lookup even from the "Cached" endpoint; cached reads are free only once data exists.

### Step 8: Query reputation

URL-encode the leading `+` of the phone number in the path as **`%2B`** — e.g. `+12025551234` becomes `%2B12025551234`.

**Cached (free, once data exists)** — returns the most recent stored reputation data:

```
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/%2B12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The **first** query on a number with no cached reputation data triggers a live, **billed** lookup regardless of this endpoint; only subsequent reads are free.

**Fresh — live query (billed)** — fetches live data from the reputation feed:

```
curl "https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/%2B12025551234?fresh=true" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

If no cached data exists for a number, a fresh query is automatically triggered regardless of the `fresh` parameter — so a brand-new number always returns live data on its first GET (and counts as a billed query). If the analytics networks don't have data for the number yet, `reputation_data` will still be `null`.

The response includes:

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

### Step 9: Manage ongoing monitoring

**Change auto-refresh frequency:**

```
curl -X PATCH https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/frequency \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"check_frequency": "daily"}'
```

The enterprise's reputation `status` must be `approved`; a request made while it is still `pending` returns `400 Bad Request`.

**Remove a number from monitoring:**

```
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/numbers/%2B12025551234 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Disable Number Reputation entirely:**

```
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Portal setup

You can also set up Number Reputation from the [Telnyx Portal](https://portal.telnyx.com) — the full workflow (accept ToS, create enterprise, render LOA, enable monitoring, add numbers, query scores) is available in the UI. The API and Portal are fully interchangeable.
