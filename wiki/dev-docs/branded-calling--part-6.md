---
title: Branded Calling
summary: 'Branded Calling is a Telnyx beta product (US-only) that displays a verified
  business identity (name, logo, call reason) on outbound calls. This page covers
  the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms
  of Service, activating the product, creating and vetting a Display Identity Record
  (DIR), attaching phone numbers in batches, configuring call reasons, and handling
  infringement claims.'
sources:
- url: https://developers.telnyx.com/docs/branded-calling/bc-phone-numbers/index
- url: https://developers.telnyx.com/docs/branded-calling/brands/index
- url: https://developers.telnyx.com/docs/branded-calling/call-reasons/index
- url: https://developers.telnyx.com/docs/branded-calling/enterprises/index
- url: https://developers.telnyx.com/docs/branded-calling/infringement-claims/index
- url: https://developers.telnyx.com/docs/branded-calling/overview
- url: https://developers.telnyx.com/docs/branded-calling/pricing
- url: https://developers.telnyx.com/docs/branded-calling/quickstart
- url: https://developers.telnyx.com/docs/branded-calling/terms-of-service/index
updated_at: 2026-07-17T09:13:14Z
---

# Branded Calling

*Part 6 of 8 — see also: [Part 1](branded-calling--part-1.md), [Part 2](branded-calling--part-2.md), [Part 3](branded-calling--part-3.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md), [Part 7](branded-calling--part-7.md), [Part 8](branded-calling--part-8.md)*

Branded Calling is a Telnyx beta product (US-only) that displays a verified business identity (name, logo, call reason) on outbound calls. This page covers the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms of Service, activating the product, creating and vetting a Display Identity Record (DIR), attaching phone numbers in batches, configuring call reasons, and handling infringement claims.

## Phone Numbers

After your DIR reaches `verified` status, attach your Telnyx phone numbers to it. Outbound calls from those numbers automatically display the DIR's name, logo, and call reason on supported carriers and devices. Numbers are added in **batches**: each `POST` creates one batch, and the batch is the unit that goes through carrier-network vetting. A phone number can be attached to **only one DIR** at a time.

### Pre-conditions

- The DIR must be in `verified` status. Adding numbers to a DIR in any other status returns `400` (`detail`: "…DIR must be verified").
- The phone numbers must already be in your Telnyx phone-number inventory.
- Numbers must be in strict E.164 format: a leading `+` followed by 10-15 digits (no spaces, dashes, or parentheses).
- A signed **Letter of Authorization (LOA)** must accompany every add request. Upload it to the [Telnyx Documents API](/api-reference/documents/upload-a-document) first and reference the returned `id` as a `document_id`.

Adding phone numbers is **billable**.

### Phone number API endpoints

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v2/dir/{dir_id}/loa` | Render the DIR's Letter of Authorization as a PDF |
| `POST` | `/v2/dir/{dir_id}/phone_numbers` | Add phone numbers (creates a batch) |
| `GET` | `/v2/dir/{dir_id}/phone_numbers` | List phone numbers attached to a DIR |
| `DELETE` | `/v2/dir/{dir_id}/phone_numbers` | Remove phone numbers from a DIR |
| `GET` | `/v2/dir/{dir_id}/phone_number_batches` | List batches for a DIR |
| `GET` | `/v2/dir/{dir_id}/phone_number_batches/{batch_id}` | Get one batch with its numbers |

Each path above also has an equivalent form that includes the enterprise: `/v2/enterprises/{enterprise_id}/dir/{dir_id}/phone_numbers` (and the `phone_number_batches` variants). Both forms share the same request and response contract.

### Render the Letter of Authorization (optional)

You can have Telnyx generate a pre-filled LOA PDF for the DIR instead of writing your own. `POST /v2/dir/{dir_id}/loa` returns an `application/pdf`. The enterprise identity and DIR display name are filled in server-side; you supply the phone numbers you intend to authorize (the same list you will add below), and optionally a third-party `agent` block and a drawn `signature`.

```
curl -X POST https://api.telnyx.com/v2/dir/{dir_id}/loa \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -o loa.pdf \
  -d '{
    "phone_numbers": ["+12025551234", "+12025555678"]
  }'
```

- `phone_numbers`: 1-15 numbers in `+E164` format (the same numbers you authorize below).
- `agent`: optional. The third-party reseller/partner managing the numbers; omit when you work with Telnyx directly.
- `signature`: optional. When provided, the PDF embeds the signature image and printed name. When omitted, the PDF comes back unsigned so you can sign it externally.

Sign the rendered PDF, then upload it to the [Telnyx Documents API](/api-reference/documents/upload-a-document) and reference the returned `document_id` as a `letter_of_authorization` document when adding numbers.

### Adding phone numbers (creating a batch)

A `documents` array containing at least one Letter of Authorization is **required**. First upload the signed LOA to the [Telnyx Documents API](/api-reference/documents/upload-a-document):

```
# Step 1 - upload the signed LOA, returns a document id
curl -X POST https://api.telnyx.com/v2/documents \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@loa.pdf"
```

Then add the numbers, referencing the returned `document_id`:

```
# Step 2 - add the numbers with the LOA
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

- A `documents` array with **at least one `letter_of_authorization`** entry is required (1-20 documents).
- The `phone_numbers` array must contain **1-15 numbers per request**.
- The batch is **atomic**: if any number fails validation (invalid format, duplicate within the request, not in your inventory, already attached to another DIR, or in a terminal `permanently_rejected` state), the entire request is rejected with `400` and **nothing is written**. On success the response is `201` with `{"data": [...]}`. On failure the body is the standard Telnyx error envelope with one `errors[]` entry per failure category, identifying the offending numbers; remove them and re-submit the rest.
- A `400` is also returned if the DIR is in a status that cannot accept new numbers, including a `suspended` DIR with an open infringement claim (the `detail` then includes the open claim IDs).

### Phone number statuses

| Status | Meaning |
| --- | --- |
| `submitted` | Awaiting verification. |
| `in_review` | Under review by the vetting agent. |
| `verified` | Successfully verified and active for this DIR. |
| `unsuccessful` | An unexpected system error occurred. |
| `suspended` | Temporarily suspended. |
| `expired` | Past expiration date. |
| `permanently_rejected` | Terminally rejected by an admin. The number cannot be re-added to any DIR; attempting to add it returns `400`. |

### Inspecting batches

A batch is the unit of carrier-network vetting. Once a batch reaches `verified` (every number in it is `verified`), branded calling is active for the whole batch.

```
# List batches
curl -g "https://api.telnyx.com/v2/dir/{dir_id}/phone_number_batches?page[size]=20" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get one batch with its numbers
curl https://api.telnyx.com/v2/dir/{dir_id}/phone_number_batches/{batch_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Listing numbers

```
curl -g "https://api.telnyx.com/v2/dir/{dir_id}/phone_numbers?page[size]=50" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Standard JSON:API pagination (`page[number]`, `page[size]`, max 250).

### Removing numbers

```
curl -X DELETE https://api.telnyx.com/v2/dir/{dir_id}/phone_numbers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_numbers": ["+12125551234", "+12125555678"]
  }'
```

Up to **100 phone numbers per request**. This call is **partial-success**: numbers that can be removed are returned under top-level `data`, and numbers that can't (not associated, invalid, etc.) come back in a `meta.errors` array on the same response. If **every** number fails, the response is a `400` with the standard Telnyx error envelope.

Removing a number tears down its registration on the Branded Calling network and frees the number to be attached to a different DIR.
