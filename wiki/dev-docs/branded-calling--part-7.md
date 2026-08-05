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

*Part 7 of 8 — see also: [Part 1](branded-calling--part-1.md), [Part 2](branded-calling--part-2.md), [Part 3](branded-calling--part-3.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md), [Part 6](branded-calling--part-6.md), [Part 8](branded-calling--part-8.md)*

Branded Calling is a Telnyx product (currently in beta, US-only) that displays a verified business identity — display name, logo, and call reason — on outbound calls instead of a bare number or "Spam Likely". The feature is built on a CTIA-managed industry registry and uses SHAKEN PASSporT tokens to deliver rich call data to supported carriers and devices. This page covers the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms of Service, activating the product, creating and vetting a Display Identity Record (DIR), attaching phone numbers in batches, configuring call reasons, handling infringement claims, and pricing.

## End-to-end quickstart

This walk-through takes you from a fresh account to a verified Display Identity Record (DIR) with phone numbers attached. You'll need a verified or enterprise-level Telnyx account and an API key.

### Before you begin

You'll need:

- A Telnyx account with **verified** or **enterprise** access and an [API key](https://portal.telnyx.com/#/app/api-keys).
- One or more **US** Telnyx phone numbers in your inventory. (Branded Calling is currently US-to-US; non-US numbers won't produce a branded result yet.)
- Your business legal details (legal name, EIN, jurisdiction of incorporation, addresses, contacts).
- A logo image, **256×256 BMP only**, ≤1 MB, hosted at a publicly-reachable HTTPS URL (optional, you can submit without one). Most design tools export PNG by default; convert to BMP with any standard image editor (Preview, Photoshop, ImageMagick, GIMP) before hosting.
- Supporting documents (e.g. business registration, letter of authorization). Upload each one through the [Telnyx Documents API](/api-reference/documents/upload-a-document) first; the API gives you back a `document_id` that you reference here.

### Step 1: Accept the Branded Calling Terms of Service

Read the full terms at [telnyx.com/terms/branded-calling](https://telnyx.com/terms/branded-calling).

```
curl -X POST https://api.telnyx.com/v2/terms_of_service/branded_calling/agree \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Idempotent — calling again after you've already agreed is a no-op.

### Step 2: Create an Enterprise

```
curl -X POST https://api.telnyx.com/v2/enterprises \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "legal_name": "Acme Healthcare Inc.",
    "doing_business_as": "Acme Healthcare",
    "organization_type": "commercial",
    "organization_legal_type": "corporation",
    "country_code": "US",
    "jurisdiction_of_incorporation": "Delaware",
    "website": "https://acmehealthcare.example.com",
    "fein": "12-3456789",
    "industry": "healthcare",
    "number_of_employees": "51-200",
    "organization_contact": {
      "first_name": "Jane",
      "last_name": "Smith",
      "email": "jane@acmehealthcare.example.com",
      "job_title": "VP Operations",
      "phone_number": "+12125551234"
    },
    "billing_contact": {
      "first_name": "Jane",
      "last_name": "Smith",
      "email": "billing@acmehealthcare.example.com",
      "phone_number": "+12125551234"
    },
    "organization_physical_address": {
      "country": "US",
      "administrative_area": "NY",
      "city": "New York",
      "postal_code": "10001",
      "street_address": "123 Main St"
    },
    "billing_address": {
      "country": "US",
      "administrative_area": "NY",
      "city": "New York",
      "postal_code": "10001",
      "street_address": "123 Main St"
    }
  }'
```

Save the `id` from the response — you'll need it for the activation step.

### Step 3: Activate Branded Calling on the enterprise

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/branded_calling \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Activation completes **asynchronously**. The enterprise body comes back immediately, but the registration finishes a few seconds later. If you create a DIR right away you may get `400` with `detail: "Branded calling registration has not completed"` for roughly 10 seconds. Wait and retry, or poll the enterprise until activation settles. Both endpoints are idempotent.

A `403` here means the Branded Calling Terms of Service hasn't been accepted yet (back to Step 1).

### Step 4: (Optional) Validate your call reasons up front

When a DIR's call reasons are *all* pre-approved, the call-reason vetting check passes automatically, which can speed up review (the DIR is still vetted and is not auto-approved). Run them through the validator before creating the DIR:

```
curl -X POST https://api.telnyx.com/v2/call_reasons/validate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '["Appointment Reminder", "Follow-Up Calls"]'
```

> The body is a **bare JSON array of strings**: do **not** wrap it in `{ "call_reasons": [...] }`.

If you instead send a mix that includes any custom string (for example `"Patient Follow-up"`, which is not on the pre-approved list), the response is `requires_manual_vetting: true` with the offending entries in `non_approved_reasons`. Custom reasons are still allowed; the call-reason check is then reviewed manually, which can take longer.

### Step 5: Create a DIR

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

### Step 6: Submit for vetting

```
curl -X POST https://api.telnyx.com/v2/dir/{dir_id}/submit \
  -H "Authorization: Bearer YOUR_API_KEY"
```

The DIR moves to `submitted`, then `in_review`. Telnyx then reviews and approves the DIR **out-of-band** (this is not instantaneous; pre-approved call reasons can shorten it). Wait for the DIR to reach `verified` before attaching phone numbers in Step 7.

### Step 7: Attach phone numbers

Once the DIR is `verified`, you can attach phone numbers. A signed **Letter of Authorization (LOA)** is required on every add request.

First upload your signed LOA to the [Telnyx Documents API](/api-reference/documents/upload-a-document) and capture the returned `id`:

```
# Step 7a - upload the signed LOA (multipart); the response includes the document id
curl -X POST https://api.telnyx.com/v2/documents \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@loa.pdf"
# Response includes "id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c"
```

Then add the numbers, referencing that `id` as `document_id`:

```
# Step 7b - add the numbers, with the LOA in the documents array
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

- A `documents` array with **at least one `letter_of_authorization`** entry is **required** (1-20 documents). The request is rejected with `400` if it's missing or has no LOA entry.
- Up to **15 numbers per request**.
- **Atomic**: if any number is invalid, already attached, or not in your inventory, the entire batch is rejected with `400` and nothing is written. The error response identifies the offending number(s); remove them and re-submit the rest.
- Numbers must be E.164 format and present in your Telnyx inventory.
- The DIR must be in `verified` status. Adding numbers to a DIR in any other status returns `400` with `detail` "...DIR must be verified".

Each `POST` creates one **batch**. Track batch progress through carrier-network vetting:

```
curl https://api.telnyx.com/v2/dir/{dir_id}/phone_number_batches \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Step 8: Make branded calls

Once a phone number reaches `verified` status, it is eligible to display your branded identity on outbound calls.

The recipient's experience depends on their carrier and device supporting branded calling. Coverage is strongest on major US carriers with compatible devices.
