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

*Part 1 of 6 — see also: [Part 2](branded-calling--part-2.md), [Part 3](branded-calling--part-3.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md), [Part 6](branded-calling--part-6.md)*

Branded Calling displays your verified business identity (name, logo, call reason) on recipients' phones before they answer, increasing answer rates and building trust. The product suite also includes Number Reputation, a standalone monitoring tool that reports spam risk scores for your outbound numbers.

## Overview and How It Works

Branded Calling replaces the bare phone number or "Spam Likely" label recipients see with your business name, logo, and call reason. The flow is:

1. Register your business as an **Enterprise** and create a **Display Identity Record (DIR)** with your name, logo, and call reason.
2. Telnyx vets the DIR, verifying your business identity, IP ownership, and compliance.
3. Associate your Telnyx phone numbers with the verified DIR.
4. When you place a call from those numbers, Telnyx signs it with a cryptographic token (SHAKEN PASSporT) containing your DIR's rich call data.
5. The terminating carrier verifies the signature and renders your DIR info on the recipient's device.

Branded Calling is built on an industry-wide CTIA registry. Telnyx handles all ecosystem interactions on your behalf. Coverage is strongest on major US carriers with compatible devices; currently the product is US-to-US only. Branded Calling is in **beta** — see [Making calls with Branded Calling](https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling) for the latest availability.

## Resource Hierarchy and Key Concepts

```
Enterprise (your organization, registered once)
├── Display Identity Record (DIR — the display identity)
│   ├── Phone-number Batch (unit of carrier-network vetting)
│   │   ├── Phone Number (+15551234567)
│   │   └── Phone Number (+15559876543)
│   └── Call Reasons ["Customer Service", "Appointment Reminder"]
├── Display Identity Record (another identity)
│   └── …
└── Terms of Service Agreement (Branded Calling)
```

| Term | Description |
|------|-------------|
| **Enterprise** | Top-level business registration. Required before creating DIRs. |
| **Display Identity Record (DIR)** | Defines what recipients see (name, logo, call reason). Must be vetted and approved. |
| **Vetting** | Verification process that validates your DIR identity and business information. |
| **Call Reason** | Text shown to recipients explaining why you're calling (e.g. "Appointment Reminder"). |
| **Batch** | Phone numbers are added in batches; each `POST` creates one batch, and the batch is the unit of carrier-network vetting. |

An Enterprise can have multiple DIRs. Each DIR has its own display name, logo, call reasons, and phone numbers. A phone number belongs to **exactly one** DIR at a time.

## Account Requirements

All Branded Calling and Number Reputation endpoints require a **verified** or **enterprise-level** Telnyx account. Trial and standard paid accounts cannot access these features. You also need an [API key](https://portal.telnyx.com/#/app/api-keys) and at least one US Telnyx phone number in your inventory (in E.164 format).

## Terms of Service

Two separate Terms of Service exist — one for Branded Calling and one for Number Reputation. Each must be accepted before using its respective product.

### Branded Calling ToS

Accept at [telnyx.com/terms/branded-calling](https://telnyx.com/terms/branded-calling):

```
curl -X POST https://api.telnyx.com/v2/terms_of_service/branded_calling/agree \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Idempotent. Check status:

```
curl "https://api.telnyx.com/v2/terms_of_service/status?product_type=branded_calling" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Additional endpoints: `GET /v2/terms_of_service/agreements` (list past agreements, paginated) and `GET /v2/terms_of_service/agreements/{agreement_id}`. The `product_type` query parameter defaults to `branded_calling`.

### Number Reputation ToS

Accept at [telnyx.com/terms/reputation-services](https://telnyx.com/terms/reputation-services):

```
curl -X POST https://api.telnyx.com/v2/terms_of_service/number_reputation/agree \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Check status with `GET /v2/terms_of_service/status?product_type=number_reputation`. The `product_type` parameter **defaults to `branded_calling`**, so you must explicitly pass `number_reputation`. The same applies to `GET /v2/terms_of_service/agreements`.

## Enterprises

An Enterprise represents your business entity on the Telnyx platform. Register it once and reuse it for all Branded Calling work.

### Required Fields

| Field | Description |
|-------|-------------|
| `legal_name` | Registered legal name (3-64 chars) |
| `doing_business_as` | DBA name (max 255 chars) |
| `organization_type` | `commercial`, `government`, or `non_profit` |
| `organization_legal_type` | `corporation`, `llc`, `partnership`, `nonprofit`, or `other` |
| `country_code` | ISO 3166-1 alpha-2 (`US` and `CA` currently supported) |
| `role_type` | `enterprise` (own DIRs) or `bpo` (calling on behalf of others). Defaults to `enterprise`. |
| `jurisdiction_of_incorporation` | State/province/country of registration |
| `website` | Your business website |
| `fein` | Federal EIN (`XX-XXXXXXX` or `XXXXXXXXX`) |
| `industry` | Fixed set (e.g. `technology`, `healthcare`, `retail`, `finance`, `legal`, `insurance`); unrecognized values return `400` |
| `number_of_employees` | One of `1-10`, `11-50`, `51-200`, `201-500`, `501-2000`, `2001-10000`, `10001+` |
| `organization_contact` | Object: `first_name`, `last_name`, `email`, `job_title`, `phone_number` |
| `billing_contact` | Object: `first_name`, `last_name`, `email`, `phone_number` |
| `organization_physical_address` | Physical business address |
| `billing_address` | Billing address |

Optional: `customer_reference` (free-form identifier, max 255 chars).

### Create an Enterprise

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
    "role_type": "enterprise",
    "jurisdiction_of_incorporation": "Delaware",
    "website": "https://acmeplumbing.example.com",
    "fein": "12-3456789",
    "industry": "technology",
    "number_of_employees": "51-200",
    "organization_contact": { ... },
    "billing_contact": { ... },
    "organization_physical_address": { ... },
    "billing_address": { ... }
  }'
```

Save the returned `id` as your `enterprise_id`.

### Activate Branded Calling on the Enterprise

Branded Calling is a **paid** product that must be explicitly activated per enterprise. Without activation, DIR creation returns `400` with `code=10015`.

```
curl -X POST https://api.telnyx.com/v2/enterprises/{enterprise_id}/branded_calling \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Activation completes **asynchronously**; if DIR creation returns `400` immediately after, wait and retry. Both endpoints are idempotent. A `403` means the Branded Calling ToS hasn't been accepted yet.

Activating Branded Calling and adding phone numbers are **billable**. See [Telnyx pricing](https://telnyx.com/pricing/numbers).
