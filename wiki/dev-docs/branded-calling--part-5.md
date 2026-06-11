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

*Part 5 of 6 — see also: [Part 1](branded-calling--part-1.md), [Part 2](branded-calling--part-2.md), [Part 3](branded-calling--part-3.md), [Part 4](branded-calling--part-4.md), [Part 6](branded-calling--part-6.md)*

Branded Calling displays your verified business identity (name, logo, call reason) on recipients' phones before they answer, increasing answer rates and building trust. The product suite also includes Number Reputation, a standalone monitoring tool that reports spam risk scores for your outbound numbers.

## Number Reputation Letter of Authorization

Before Telnyx can register your numbers with call-analytics networks, you must provide a signed LOA authorizing Telnyx to manage your numbers' reputation on your behalf. The LOA is the **#1 thing customers get stuck on** — follow these steps in order.

There are **two separate approval gates** tracked independently:
1. Reputation `status` must be `approved` (the activation lifecycle).
2. `loa_status` must be `approved` (Telnyx reviews the signed LOA).

**Both must be `approved`** before you can add phone numbers.

### Step-by-Step LOA Process

**1. Render the LOA as a PDF** (not billable):

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/loa \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -o loa.pdf \
  -d '{}'
```

The response body is the PDF itself. Optional body fields:
- `agent`: Third-party reseller/partner block (omit when working directly with Telnyx).
- `signature`: Embeds a signature image in the rendered PDF (`image_base64` + `signer_name`). When omitted, the PDF is unsigned for manual signing.

**2. Sign the PDF** (e-signature or wet signature) if you didn't embed a signature.

**3. Upload the signed PDF** to the Telnyx Documents API:

```
curl -X POST https://api.telnyx.com/v2/documents \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@loa.pdf"
```

Save the returned `data.id` as your `loa_document_id`.

**4. Enable reputation** with the `loa_document_id` (billable):

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "loa_document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
    "check_frequency": "business_daily"
  }'
```

**5. Wait for LOA approval.** Poll with `GET /v2/enterprises/{enterprise_id}/reputation`. `loa_status` moves `pending` → `approved` (or `rejected`).

### LOA Status Values

| `loa_status` | Meaning |
|--------------|----------|
| `pending` | Telnyx is reviewing. Numbers cannot be added yet. |
| `approved` | LOA accepted. Combined with `status` = `approved`, you can add numbers. |
| `rejected` | LOA not accepted. Replace it to retry (see below). |

### Replace a Pending or Rejected LOA

Render a fresh PDF, sign and upload it to get a new `loa_document_id`, then:

```
curl -X PATCH https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/loa \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "loa_document_id": "NEW_DOCUMENT_ID"
  }'
```

Replacing the LOA **resets `loa_status` back to `pending`**. You can only replace the LOA while `loa_status` is `pending` or `rejected`. Once `approved`, the document is locked — this `PATCH` returns `400`. To start over after approval, disable Number Reputation entirely and re-enable with the new document.

## Number Reputation Settings and Vetting

### Enable Number Reputation

Submit your LOA document ID to enable monitoring (billable). `check_frequency` is optional and defaults to `business_daily`. Enabling returns `403` if the Number Reputation ToS hasn't been accepted.

### Two Approval Gates

| Status | Meaning |
|--------|----------|
| `status` | Activation lifecycle: `pending` → `approved` / `rejected`. |
| `loa_status` | LOA review: `pending` → `approved` / `rejected`. |

Both must be `approved` before `POST .../reputation/numbers` will accept numbers. A `rejected` `loa_status` is recoverable by replacing the LOA.

### Check Current Status

```
curl https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Response includes `status`, `loa_status`, `check_frequency`, `loa_document_id`, `rejection_reasons` (populated when `status` is `rejected`), and timestamps.

### Auto-Refresh Schedules

| Frequency | Schedule |
|-----------|----------|
| `business_daily` | Mon–Fri **(default)** |
| `daily` | Every day including weekends |
| `weekly` | Once per week |
| `biweekly` | Every 2 weeks |
| `monthly` | Once per month |
| `never` | Manual only — use `?fresh=true` or forced refresh |

Change the schedule (requires `status` = `approved`):

```
curl -X PATCH https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation/frequency \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"check_frequency": "daily"}'
```

A frequency change while `status` is still `pending` returns `400`.

### Disable Number Reputation

```
curl -X DELETE https://api.telnyx.com/v2/enterprises/{enterprise_id}/reputation \
  -H "Authorization: Bearer YOUR_API_KEY"
```

This de-registers your numbers and removes the settings. A subsequent `GET .../reputation` returns `404`. To monitor again, re-enable with a fresh LOA.
