---
title: 10DLC Registration, Campaigns, and Rate Limits
summary: A consolidated reference for registering a 10DLC brand and campaign with
  The Campaign Registry (TCR) through Telnyx, submitting for external vetting, and
  understanding how the resulting vetting score controls carrier throughput on AT&T,
  T-Mobile, and Verizon.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/10dlc-rate-limits/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/brand-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-registration/index
updated_at: 2026-08-05T13:48:40Z
---

# 10DLC Registration, Campaigns, and Rate Limits

*Part 1 of 4 — see also: [Part 2](10dlc-registration-campaigns-and-rate-limits--part-2.md), [Part 3](10dlc-registration-campaigns-and-rate-limits--part-3.md), [Part 4](10dlc-registration-campaigns-and-rate-limits--part-4.md)*

A consolidated reference for registering a 10DLC brand and campaign with The Campaign Registry (TCR) through Telnyx, submitting for external vetting, and understanding how the resulting vetting score controls carrier throughput on AT&T, T-Mobile, and Verizon.

## Overview

10DLC (10-Digit Long Code) messaging on US long codes requires every sender to register a **brand** (their business identity) and at least one **campaign** (their messaging use case) with [The Campaign Registry (TCR)](https://www.campaignregistry.com/) before sending A2P traffic at scale. Telnyx exposes both registrations through the Mission Control Portal and the `/v2/10dlc/...` API family.

A brand's **vetting score (0–100)** is the single most important factor in determining throughput. Carriers (AT&T, T-Mobile, Verizon) each apply different rate limits, and understanding those limits is essential for capacity planning and for optimizing toward higher throughput.

## Brand entity types

TCR supports several entity types. Choose the one that matches your business structure:

| Entity Type | API Value | Description | Vetting Required |
| --- | --- | --- | --- |
| Private for-profit | `PRIVATE_PROFIT` | Private companies (LLC, Inc, etc.) | Yes |
| Public for-profit | `PUBLIC_PROFIT` | Publicly traded companies | Yes |
| Non-profit | `NON_PROFIT` | 501(c)(3) or equivalent | Yes |
| Government | `GOVERNMENT` | Federal, state, or local government | Yes |
| Sole Proprietor | `SOLE_PROPRIETOR` | Individuals without EIN | OTP only |

Sole Proprietor brands have significant limitations: 1 campaign, 1 phone number, low throughput. Use standard registration if your business has an EIN. See the [Sole Proprietor](sole-proprietor.md) guide for details.

## Brand registration flow

### Prerequisites

- A [Telnyx account](https://telnyx.com/sign-up) with API access
- Your [API key](https://portal.telnyx.com/#/app/api-keys)
- Business information: legal name, EIN/Tax ID, address, phone, email, website

### Step 1: Create a brand

Register your business identity by providing company details, contact information, and entity type.

**Required fields**

| Field | Type | Description |
| --- | --- | --- |
| `entityType` | string | Business entity type (see table above) |
| `displayName` | string | Brand display name (shown to carriers) |
| `companyName` | string | Legal company name (must match EIN records) |
| `ein` | string | Federal Tax ID / EIN (format: `XX-XXXXXXX`) |
| `phone` | string | Business phone in E.164 format |
| `street` | string | Business street address |
| `city` | string | City |
| `state` | string | State (2-letter abbreviation) |
| `postalCode` | string | ZIP code |
| `country` | string | Country code (`US` or `CA`) |
| `email` | string | Business contact email |
| `website` | string | Business website URL |
| `vertical` | string | Industry vertical (see [#Industry verticals](industry-verticals.md)) |

**Optional fields**

| Field | Type | Description |
| --- | --- | --- |
| `altBusinessId` | string | Alternative business ID (DUNS, GIIN, LEI) |
| `altBusinessIdType` | string | Type of alternative ID: `DUNS`, `GIIN`, or `LEI` |
| `stockSymbol` | string | Stock ticker (required for `PUBLIC_PROFIT`) |
| `stockExchange` | string | Exchange: `NYSE`, `NASDAQ`, `AMEX`, etc. |

```bash
curl -X POST https://api.telnyx.com/v2/10dlc/brand \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "entityType": "PRIVATE_PROFIT",
    "displayName": "Acme Corp",
    "companyName": "Acme Corporation",
    "ein": "12-3456789",
    "phone": "+15551234567",
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "postalCode": "10001",
    "country": "US",
    "email": "admin@acmecorp.com",
    "website": "https://acmecorp.com",
    "vertical": "TECHNOLOGY"
  }'
```

**Brand creation response**

```json
{
  "data": {
    "brandId": "BXXXXXX",
    "entityType": "PRIVATE_PROFIT",
    "displayName": "Acme Corp",
    "companyName": "Acme Corporation",
    "ein": "12-3456789",
    "identityStatus": "VERIFIED",
    "cspId": "TELNYX",
    "brandRelationship": "BASIC_ACCOUNT",
    "vertical": "TECHNOLOGY",
    "phone": "+15551234567",
    "email": "admin@acmecorp.com",
    "website": "https://acmecorp.com",
    "country": "US",
    "state": "NY",
    "city": "New York",
    "street": "123 Main St",
    "postalCode": "10001"
  }
}
```

### Step 2: Retrieve brand details

```bash
curl -X GET https://api.telnyx.com/v2/10dlc/brand/BXXXXXX \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Brand statuses**

| Status | Meaning |
| --- | --- |
| `SELF_DECLARED` | Brand created, not yet verified |
| `VERIFIED` | Identity verified by TCR |
| `VETTED_VERIFIED` | Third-party vetting completed |
| `UNVERIFIED` | Verification failed — see [#Common rejection reasons and fixes](common-rejection-reasons-and-fixes.md) |

### Step 3: Submit for external vetting

Vetting is performed by a third-party partner (e.g., Campaign Verify) and produces a **trust score from 0 to 100** that directly impacts your messaging throughput.

```bash
curl -X POST https://api.telnyx.com/v2/10dlc/brand/BXXXXXX/externalVetting \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "evpId": "AEGIS",
    "vettingClass": "STANDARD"
  }'
```

**Idempotency:** Submitting the same `evpId` + `vettingClass` for a brand that already has a successful vetting (within the last 180 days) or one currently being processed returns `400` with error code `10012` ("Duplicate resource"). Failed vettings are excluded from this check, so you can retry immediately after a real failure. To retrieve existing vettings, use `GET /v2/10dlc/brand/{brandId}/externalVetting`.

**Vetting classes**

| Class | Cost | Use Case |
| --- | --- | --- |
| `STANDARD` | ~$4 | Default for most brands |
| `ENHANCED` | ~$40 | Higher trust scores, faster approval |

### Step 4: Check vetting results

Vetting typically takes **1–7 business days**. You can poll or use webhooks to check the result.

```bash
curl -X GET https://api.telnyx.com/v2/10dlc/brand/BXXXXXX/externalVetting \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Step 5: Update a brand

If your brand details change (address, phone, etc.), update them via the API:

```bash
curl -X PUT https://api.telnyx.com/v2/10dlc/brand/BXXXXXX \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "phone": "+15559876543",
    "email": "newemail@acmecorp.com",
    "website": "https://www.acmecorp.com"
  }'
```

Updating certain fields (company name, EIN) may trigger re-verification. Contact support if you need to change core identity fields.

### List all brands

```bash
curl -X GET "https://api.telnyx.com/v2/10dlc/brand?page[size]=25" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Industry verticals

When creating a brand, specify your industry using one of these vertical values:

| Vertical | API Value |
| --- | --- |
| Professional Services | `PROFESSIONAL` |
| Real Estate | `REAL_ESTATE` |
| Healthcare | `HEALTHCARE` |
| Human Resources | `HUMAN_RESOURCES` |
| Energy | `ENERGY` |
| Entertainment | `ENTERTAINMENT` |
| Retail | `RETAIL` |
| Transportation | `TRANSPORTATION` |
| Agriculture | `AGRICULTURE` |
| Insurance | `INSURANCE` |
| Postal | `POSTAL` |
| Education | `EDUCATION` |
| Hospitality | `HOSPITALITY` |
| Financial | `FINANCIAL` |
| Political | `POLITICAL` |
| Gambling | `GAMBLING` |
| Legal | `LEGAL` |
| Construction | `CONSTRUCTION` |
| NGO | `NGO` |
| Manufacturing | `MANUFACTURING` |
| Government | `GOVERNMENT` |
| Technology | `TECHNOLOGY` |
| Communication | `COMMUNICATION` |
