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
