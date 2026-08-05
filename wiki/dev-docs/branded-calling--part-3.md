---
title: Branded Calling
summary: 'Branded Calling is a Telnyx product (currently in beta, US-only) that displays
  a verified business identity — display name, logo, and call reason — on outbound
  calls instead of a bare number or "Spam Likely". The feature is built on a CTIA-managed
  industry registry and uses SHAKEN PASSporT tokens to deliver rich call data to supported
  carriers and devices. This page covers the full lifecycle: registering an Enterprise,
  accepting the Branded Calling Terms of Service, activating the product, creating
  and vetting a Display Identity Record (DIR), attaching phone numbers in batches,
  configuring call reasons, handling infringement claims, and pricing.'
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
updated_at: 2026-08-05T13:39:22Z
---

# Branded Calling

*Part 3 of 8 — see also: [Part 1](branded-calling--part-1.md), [Part 2](branded-calling--part-2.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md), [Part 6](branded-calling--part-6.md), [Part 7](branded-calling--part-7.md), [Part 8](branded-calling--part-8.md)*

Branded Calling is a Telnyx product (currently in beta, US-only) that displays a verified business identity — display name, logo, and call reason — on outbound calls instead of a bare number or "Spam Likely". The feature is built on a CTIA-managed industry registry and uses SHAKEN PASSporT tokens to deliver rich call data to supported carriers and devices. This page covers the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms of Service, activating the product, creating and vetting a Display Identity Record (DIR), attaching phone numbers in batches, configuring call reasons, handling infringement claims, and pricing.

## Display Identity Records (DIRs)

A **Display Identity Record** (DIR) defines what recipients see on their phone screen when you call. Each DIR has a display name, an optional logo, and 1-10 call reasons. DIRs must be vetted and approved by Telnyx before they become active. Once a DIR reaches `verified` status, calls placed from any phone number attached to it will display the branded identity on supported carriers and devices.

### Prerequisites

Before creating a DIR:

1. The parent **Enterprise** must exist (`POST /v2/enterprises`).
2. The Branded Calling **Terms of Service** must be accepted (`POST /v2/terms_of_service/branded_calling/agree`).
3. **Branded Calling must be activated** on the enterprise (`POST /v2/enterprises/{enterprise_id}/branded_calling`). Without this, DIR creation returns `400` with `code=10015`. Activation completes asynchronously; if DIR creation returns `400` immediately after, retry — both endpoints are idempotent.

### API endpoints

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v2/enterprises/{enterprise_id}/dir` | Create a new DIR under an enterprise |
| `GET` | `/v2/dir` | List DIRs across the account |
| `GET` | `/v2/enterprises/{enterprise_id}/dir` | List DIRs under one enterprise |
| `GET` | `/v2/dir/{dir_id}` | Get a DIR |
| `PATCH` | `/v2/dir/{dir_id}` | Update a DIR |
| `DELETE` | `/v2/dir/{dir_id}` | Delete a DIR |
| `POST` | `/v2/dir/{dir_id}/submit` | Submit for vetting |

### Required fields

These are the DIR-level required fields. Anything related to the legal entity (legal name, EIN, addresses, contacts, jurisdiction) lives on the parent **Enterprise**, not on the DIR.

| Field | Type | Description |
| --- | --- | --- |
| `display_name` | string | Shown to recipients. 1-35 characters, no emoji, not whitespace-only. |
| `authorizer_name` | string | Authorizer point-of-contact name. Max 255 chars. |
| `authorizer_email` | string | Authorizer point-of-contact email. |
| `certify_brand_is_accurate` | boolean | Must be `true`. |
| `certify_no_shaft_content` | boolean | Must be `true`. (SHAFT = Sex, Hate, Alcohol, Firearms, Tobacco.) |
| `certify_ip_ownership` | boolean | Must be `true`. |
| `call_reasons` | array | 1-10 strings, each 1-64 characters. |

### Optional fields

| Field | Type | Description |
| --- | --- | --- |
| `logo_url` | string | HTTPS URL (max 128 chars) to a 256×256 BMP image (≤1 MB). Telnyx downloads and validates it on every create / `PATCH`. |
| `documents` | array | Up to 20 entries of `{document_id, document_type, description?}`. Each `document_id` must come from a prior upload to the [Telnyx Documents API](/api-reference/documents/upload-a-document). |
| `reselling` | boolean | `true` if you resell calling services on behalf of others. Defaults to `false`. |

### Logo requirements

The logo must be a **BMP** image, exactly **256×256 pixels**, **≤1 MB**, **≤32-bit color depth**, hosted at a publicly-reachable HTTPS URL. PNG, JPEG, and other formats are rejected at create / `PATCH` time with a `400`. Most design tools export PNG by default; convert to BMP with any standard image editor (Preview, Photoshop, ImageMagick, GIMP).

### Document types

When you attach `documents` to a DIR, each entry's `document_type` must be one of:
`letter_of_authorization`, `business_registration`, `articles_of_incorporation`, `tax_document`, `ein_letter`, `trademark_registration`, `website_ownership`, `business_license`, `professional_license`, `government_id`, `utility_bill`, `bank_statement`, `other`

The actual file is uploaded separately via the [Telnyx Documents API](/api-reference/documents/upload-a-document); the `document_id` you receive from that upload is what you reference here.

### DIR statuses

| Status | Meaning |
| --- | --- |
| `draft` | Initial state. You're still preparing the DIR. Editable. |
| `submitted` | Vetting requested. Editing, deleting, and re-submitting are blocked. |
| `in_review` | Telnyx is actively reviewing. Same restrictions as `submitted`. |
| `verified` | Approved. Phone numbers can be attached. Editable (but any non-trivial PATCH moves the DIR back to `draft` and tears down the live registration). |
| `rejected` | Vetting failed for fixable reasons. Edit and re-submit. |
| `unsuccessful` | Vetting failed for a system reason. Edit and re-submit. |
| `suspended` | The normal state for a DIR with an attached infringement claim (Telnyx may pre-emptively suspend the DIR while a claim is `pending` or `contested`). While the claim is open, recover with `PUT /v2/dir/{dir_id}/infringement_update` — plain `PATCH` + `POST /submit` is blocked (`409`). A DIR can also remain `suspended` after a `modified` resolution, at which point the claim is closed and `PATCH` + `POST /submit` work normally. |
| `expired` | The one-year verification window has closed. Re-submit to renew. |
| `infringement_claimed` | Legacy status. A new infringement claim moves the DIR to `suspended`, not here; you will not normally see this state. Where it still exists, phone numbers cannot be added and `PATCH` is rejected with a `400`. |
| `permanently_rejected` | Terminal. Cannot be re-submitted. The only exit is `DELETE`. |

### Create a DIR

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/dir \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "display_name": "Acme Healthcare",
    "authorizer_name": "Jane Smith",
    "authorizer_email": "jane@acmehealthcare.example.com",
    "certify_brand_is_accurate": true,
    "certify_no_shaft_content": true,
    "certify_ip_ownership": true,
    "call_reasons": ["Appointment Reminder", "Follow-Up Calls"],
    "logo_url": "https://acmehealthcare.example.com/logo-256.bmp",
    "documents": [
      {
        "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
        "document_type": "business_registration",
        "description": "Certificate of incorporation."
      }
    ]
  }'
```

The DIR is created in `draft` status. Save the `id` — this is your `dir_id`.

### Submit for vetting

```
curl -X POST https://api.telnyx.com/v2/dir/{dir_id}/submit \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The DIR moves to `submitted`, then `in_review`. Telnyx then reviews and approves the DIR **out-of-band** (this is not instantaneous; pre-approved call reasons can shorten it). Wait for the DIR to reach `verified` before attaching phone numbers. Outcomes:

- `verified` — approved. Phone numbers can now be attached.
- `rejected` — fixable. Read `rejection_reasons` on the DIR and the `vetting_comment` / `rejection_reason` entries on `GET /v2/dir/{dir_id}/comments` for context, `PATCH` the offending fields, then `POST /submit` again.
- `unsuccessful` — system error. Same handling as rejected.
- `permanently_rejected` — terminal. The only exit is `DELETE /v2/dir/{dir_id}` (remove any attached phone numbers first, or the delete returns `400`).

While waiting, poll `GET /v2/dir/{dir_id}` for the current `status`. Use a sensible cadence (e.g. once every 30-60 seconds); don't poll in a tight loop. If `/submit` fails with a `400` and the DIR has an open infringement claim, resolve the claim first — see [Infringement Claims](infringement-claims.md).

### Update a DIR

```
curl -X PATCH https://api.telnyx.com/v2/dir/{dir_id} \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "display_name": "Updated Display Name",
    "call_reasons": ["Customer Service", "Billing Inquiry"]
  }'
```

`PATCH` is allowed in `draft`, `rejected`, `unsuccessful`, `suspended`, and `verified`.

- For `draft` / `rejected` / `unsuccessful`, `PATCH` is a pure edit. The status doesn't change. Call `POST /submit` to re-vet when ready.
- `suspended` means an infringement claim is attached. `PATCH` itself is allowed and leaves the status unchanged, but **`POST /submit` is blocked with a `409` while the claim is still `pending` or `contested`** (the `no_active_claims` gate). To revise content and re-vet during an open claim, use `PUT /v2/dir/{dir_id}/infringement_update` instead — see [Infringement Claims](infringement-claims.md). The plain `PATCH` + `POST /submit` flow only works once the claim is `resolved` (e.g. `resolution = modified`, which leaves the DIR `suspended` with the claim closed).
- For `verified`, a `PATCH` that actually changes a field flips the DIR back to `draft` and tears down the live registration. The DIR stops serving its branded identity on calls until you `POST /submit` and Telnyx re-approves it. Don't edit a live verified DIR unless you intend to take it out of service and re-vet it.
- If you provide `logo_url`, it is re-downloaded and re-validated on every `PATCH`. If validation fails the DIR isn't updated.
- `documents` are append-only; existing documents are never removed by a `PATCH`.

### Resubmit after rejection

When a DIR is `rejected` or `unsuccessful`, the headline reasons are in the `rejection_reasons` array on the DIR itself; the detailed reviewer notes appear on the comments thread. Read both. Fix the issues with `PATCH`, then submit again:

```
curl -X POST https://api.telnyx.com/v2/dir/{dir_id}/submit \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Delete a DIR

```
curl -X DELETE https://api.telnyx.com/v2/dir/{dir_id} \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Allowed in: `draft`, `rejected`, `unsuccessful`, `verified`, `suspended`, `expired`, `infringement_claimed`, and `permanently_rejected`. The mid-vetting statuses `submitted` and `in_review` return `400`.

The DIR must have **no phone numbers still attached**. If any numbers are attached, the delete returns `400` ("DIR has N phone number(s) still attached. Delete every phone first, then delete the DIR."). Remove them with `DELETE /v2/dir/{dir_id}/phone_numbers` first, then delete the DIR.

Returns `409` if the DIR has a `pending` or `contested` infringement claim. Customers can only contest the claim; Telnyx adjudicates resolution.
