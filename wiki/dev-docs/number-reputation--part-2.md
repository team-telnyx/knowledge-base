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

*Part 2 of 5 — see also: [Part 1](number-reputation--part-1.md), [Part 3](number-reputation--part-3.md), [Part 4](number-reputation--part-4.md), [Part 5](number-reputation--part-5.md)*

Number Reputation is a Telnyx product that monitors the spam reputation of US outbound calling numbers by querying the major call-analytics networks used by US carriers. It exposes per-number spam risk, granular scores, and category labels, and supports batch remediation requests to re-evaluate flagged numbers. The product is governed by its own Terms of Service and is currently US-only.

## Step 3: Render the Letter of Authorization (LOA)

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

## Step 4: Sign the LOA and upload it to the Documents API

Sign `loa.pdf` (e-signature or wet signature), then upload the signed copy to the [Telnyx Documents API](/api-reference/documents/upload-a-document):

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

## Step 5: Enable Number Reputation

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "loa_document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
    "check_frequency": "business_daily"
  }'
```

`check_frequency` is optional and defaults to `business_daily`. Your enterprise details are submitted for automated vetting. This typically takes **minutes**.

Enabling reputation is a **billable action**. See [Number Reputation Pricing](number-reputation-pricing.md) for current pricing. Enabling returns **`403`** if you have not agreed to the Number Reputation Terms of Service.

## Step 6: Wait for both approval gates

There are **two separate approval gates** you must clear before you can add phone numbers — they are tracked independently:

1. Reputation **`status`** must be `approved` — the activation lifecycle for the enterprise.
2. **`loa_status`** must be `approved` — Telnyx reviews your signed Letter of Authorization.

Both must read `approved` before `POST .../reputation/numbers` will accept numbers.

Poll the reputation settings until **both** `status` and `loa_status` read `approved`:

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
| `loa_status` | LOA review: `pending` → `approved` (or `rejected` — replace the LOA, see [Letter of Authorization (LOA)](letter-of-authorization-loa.md)). |

### LOA approval gate

| `loa_status` | Meaning |
| --- | --- |
| `pending` | Telnyx is reviewing the uploaded LOA. Numbers cannot be added yet. |
| `approved` | LOA accepted. Combined with reputation `status` = `approved`, you can add numbers. |
| `rejected` | LOA was not accepted. Replace it to retry. |

### Vetting lifecycle

```
pending ──► approved    (activation approved)
pending ──► rejected    (check rejection_reasons in the response)
approved ──► (removed)   (reputation disabled via DELETE)
```

Once you disable reputation, the settings are removed: a subsequent `GET .../reputation` returns **`404 Not Found`** rather than a readable status.

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

## Step 7: Associate phone numbers

Once both gates are `approved`, add phone numbers for monitoring:

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

Adding numbers is a **billable action**. See [Number Reputation Pricing](number-reputation-pricing.md) for current pricing.

In the request body, phone numbers are JSON string values, so the leading `+` is written literally (`"+12025551234"`). In **path parameters** (the get/delete-by-number endpoints below) URL-encode the `+` as **`%2B`**.

A freshly added number has `reputation_data: null` until Telnyx collects its first refresh. Querying it (Step 8) triggers an immediate lookup. Because the number has no cached data yet, that first query performs a **live (billed)** lookup even from the "Cached" endpoint; cached reads are free only once data exists.
