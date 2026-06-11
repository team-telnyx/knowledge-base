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
