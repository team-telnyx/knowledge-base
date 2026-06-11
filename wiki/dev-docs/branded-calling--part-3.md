---
title: Branded Calling
summary: Branded Calling displays your verified business identity (name, logo, call
  reason) on recipients' phones before they answer, increasing answer rates and building
  trust. The product suite also includes Number Reputation, a standalone monitoring
  tool that reports spam risk scores for your outbound numbers.
sources:
- url: https://developers.telnyx.com/docs/branded-calling/bc-phone-numbers/index
- url: https://developers.telnyx.com/docs/branded-calling/brands/index
- url: https://developers.telnyx.com/docs/branded-calling/call-reasons/index
- url: https://developers.telnyx.com/docs/branded-calling/enterprises/index
- url: https://developers.telnyx.com/docs/branded-calling/infringement-claims/index
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/index
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/loa
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/phone-numbers
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/quickstart
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/remediation
- url: https://developers.telnyx.com/docs/branded-calling/number-reputation/settings
- url: https://developers.telnyx.com/docs/branded-calling/overview
- url: https://developers.telnyx.com/docs/branded-calling/quickstart
- url: https://developers.telnyx.com/docs/branded-calling/terms-of-service/index
updated_at: 2026-06-11T10:26:56Z
---

# Branded Calling

*Part 3 of 6 — see also: [Part 1](branded-calling--part-1.md), [Part 2](branded-calling--part-2.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md), [Part 6](branded-calling--part-6.md)*

Branded Calling displays your verified business identity (name, logo, call reason) on recipients' phones before they answer, increasing answer rates and building trust. The product suite also includes Number Reputation, a standalone monitoring tool that reports spam risk scores for your outbound numbers.

## Branded Calling Phone Numbers

After a DIR reaches `verified` status, attach your Telnyx phone numbers. Outbound calls from those numbers automatically display the DIR's name, logo, and call reason on supported carriers and devices. Numbers are added in **batches**; each `POST` creates one batch, and the batch is the unit that goes through carrier-network vetting.

### Pre-conditions

- The DIR must be in `verified` status (returns `400` otherwise).
- Phone numbers must already be in your Telnyx phone-number inventory.
- Numbers must be in strict E.164 format: leading `+` followed by 10–15 digits (no spaces, dashes, or parentheses).
- A signed **Letter of Authorization (LOA)** must accompany every add request. Upload it to the Telnyx Documents API first and reference the returned `id` as a `document_id`.

Adding phone numbers is **billable**. See [Telnyx pricing](https://telnyx.com/pricing/numbers).

### API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/v2/dir/{dir_id}/loa` | Render the DIR's Letter of Authorization as a PDF |
| `POST` | `/v2/dir/{dir_id}/phone_numbers` | Add phone numbers (creates a batch) |
| `GET` | `/v2/dir/{dir_id}/phone_numbers` | List phone numbers attached to a DIR |
| `DELETE` | `/v2/dir/{dir_id}/phone_numbers` | Remove phone numbers from a DIR |
| `GET` | `/v2/dir/{dir_id}/phone_number_batches` | List batches for a DIR |
| `GET` | `/v2/dir/{dir_id}/phone_number_batches/{batch_id}` | Get one batch with its numbers |

Each path also has an enterprise-scoped form: `/v2/enterprises/{enterprise_id}/dir/{dir_id}/phone_numbers` (and the `phone_number_batches` variants). Both forms share the same request and response contract.

### Render the LOA (Optional)

Telnyx can generate a pre-filled LOA PDF instead of writing your own:

```
curl -X POST https://api.telnyx.com/v2/dir/{dir_id}/loa \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -o loa.pdf \
  -d '{
    "phone_numbers": ["+12025551234", "+12025555678"]
  }'
```

- `phone_numbers`: 1–15 numbers in `+E164` format (the same numbers you will authorize).
- `agent`: optional. Third-party reseller/partner block; omit when working with Telnyx directly.
- `signature`: optional. Embeds a signature image and printed name. When omitted, the PDF is unsigned for manual signing.

Sign the rendered PDF, upload it to the Telnyx Documents API, and reference the returned `document_id` as a `letter_of_authorization` document when adding numbers.

### Adding Phone Numbers (Creating a Batch)

1. Upload the signed LOA to the Documents API:

```
curl -X POST https://api.telnyx.com/v2/documents \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@loa.pdf"
```

2. Add the numbers, referencing the returned `document_id`:

```
curl -X POST https://api.telnyx.com/v2/dir/{dir_id}/phone_numbers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12125551234", "+12125555678"],
    "documents": [
      {
        "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
        "document_type": "letter_of_authorization",
        "description": "LOA covering this set of numbers."
      }
    ]
  }'
```

Key rules:
- A `documents` array with **at least one `letter_of_authorization`** entry is required (1–20 documents).
- The `phone_numbers` array must contain **1–15 numbers** per request.
- The batch is **atomic**: if any number fails validation (invalid format, duplicate within the request, not in your inventory, already attached to another DIR, or `permanently_rejected`), the entire request is rejected with `400` and nothing is written. The error response identifies offending numbers per failure category.
- A `400` is also returned if the DIR cannot accept new numbers (e.g. a `suspended` DIR with an open infringement claim).

### Phone Number Statuses

| Status | Meaning |
|--------|---------|
| `submitted` | Awaiting verification. |
| `in_review` | Under review by the vetting agent. |
| `verified` | Successfully verified and active for this DIR. |
| `unsuccessful` | An unexpected system error occurred. |
| `suspended` | Temporarily suspended. |
| `expired` | Past expiration date. |
| `permanently_rejected` | Terminally rejected by an admin. Cannot be re-added to any DIR. |

### Inspecting Batches

```
# List batches
curl -g "https://api.telnyx.com/v2/dir/{dir_id}/phone_number_batches?page[size]=20" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get one batch with its numbers
curl https://api.telnyx.com/v2/dir/{dir_id}/phone_number_batches/{batch_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Listing Numbers

```
curl -g "https://api.telnyx.com/v2/dir/{dir_id}/phone_numbers?page[size]=50" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Standard JSON:API pagination (`page[number]`, `page[size]`, max 250).

### Removing Numbers

```
curl -X DELETE https://api.telnyx.com/v2/dir/{dir_id}/phone_numbers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12125551234", "+12125555678"]
  }'
```

Up to **100 phone numbers per request**. This call supports **partial success**: numbers that can be removed are returned under `data`; numbers that can't (not associated, invalid, etc.) come back in `meta.errors`. If every number fails, the response is `400`. Removing a number tears down its registration and frees it to be attached to a different DIR.
