---
title: 10DLC Messaging
summary: 10DLC (10-Digit Long Code) is the industry standard for application-to-person
  (A2P) messaging on US long code numbers. Registering your brand and campaigns with
  The Campaign Registry (TCR) through Telnyx provides higher throughput, better deliverability,
  and reduced carrier filtering. Your brand's vetting score directly determines your
  messaging throughput limits across AT&T, T-Mobile, and other carriers.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/10dlc-rate-limits/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/brand-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/isv-reseller-onboarding
- url: https://developers.telnyx.com/docs/messaging/10dlc/phone-number-assignment
- url: https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/sole-proprietor/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/troubleshooting/index
- url: https://developers.telnyx.com/docs/messaging/getting-started/choosing-your-sender-type/index
updated_at: 2026-06-11T10:36:45Z
---

# 10DLC Messaging

*Part 1 of 5 — see also: [Part 2](10dlc-messaging--part-2.md), [Part 3](10dlc-messaging--part-3.md), [Part 4](10dlc-messaging--part-4.md), [Part 5](10dlc-messaging--part-5.md)*

10DLC (10-Digit Long Code) is the industry standard for application-to-person (A2P) messaging on US long code numbers. Registering your brand and campaigns with The Campaign Registry (TCR) through Telnyx provides higher throughput, better deliverability, and reduced carrier filtering. Your brand's vetting score directly determines your messaging throughput limits across AT&T, T-Mobile, and other carriers.

## Overview and Registration Flow

10DLC registration is required for A2P messaging to US mobile numbers (enforced by carriers since 2023). The registration process involves four steps:

| Step | What Happens | Timeline |
| --- | --- | --- |
| 1. Create Brand | Register your business identity with TCR | Instant |
| 2. Vet Brand | Third-party vetting determines your trust score (0–100) | 1–7 business days |
| 3. Create Campaign | Register your messaging use case | Instant (pending carrier approval) |
| 4. Assign Numbers | Link phone numbers to your campaign | Instant |

Vetting is critical — your brand's vetting score directly determines your throughput limits, especially on AT&T and T-Mobile. See [10DLC Rate Limits and Throughput](10dlc-rate-limits-and-throughput.md) for details.

**Prerequisites:**
- A Telnyx account with API access
- Your API key
- Business information: legal name, EIN/Tax ID, address, phone, email, website

## Brand Registration

A brand represents your registered business identity in the 10DLC ecosystem. Before creating campaigns or sending A2P messages, you must register your brand with TCR through the Telnyx API.

### Brand Entity Types

| Entity Type | API Value | Description | Vetting Required |
| --- | --- | --- | --- |
| Private for-profit | `PRIVATE_PROFIT` | Private companies (LLC, Inc, etc.) | Yes |
| Public for-profit | `PUBLIC_PROFIT` | Publicly traded companies | Yes |
| Non-profit | `NON_PROFIT` | 501(c)(3) or equivalent | Yes |
| Government | `GOVERNMENT` | Federal, state, or local government | Yes |
| Sole Proprietor | `SOLE_PROPRIETOR` | Individuals without EIN | OTP only |

Sole Proprietor brands have significant limitations: 1 campaign, 1 phone number, low throughput. Use standard registration if your business has an EIN. For full Sole Proprietor details, see the [Sole Proprietor Registration](#sole-proprietor-registration) section below.

### Creating a Brand

**Required fields:** `entityType`, `displayName`, `companyName`, `ein` (format `XX-XXXXXXX`), `phone` (E.164), `street`, `city`, `state`, `postalCode`, `country` (`US` or `CA`), `email`, `website`, `vertical`.

**Optional fields:** `altBusinessId`, `altBusinessIdType` (`DUNS`, `GIIN`, `LEI`), `stockSymbol` (required for `PUBLIC_PROFIT`), `stockExchange`.

```
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

### Brand Statuses

| Status | Meaning |
| --- | --- |
| `SELF_DECLARED` | Brand created, not yet verified |
| `VERIFIED` | Identity verified by TCR |
| `VETTED_VERIFIED` | Third-party vetting completed |
| `UNVERIFIED` | Verification failed — see troubleshooting |

### Updating a Brand

Use `PUT /v2/10dlc/brand/{brandId}` to update details. Changing core fields (company name, EIN) may trigger re-verification.

### Industry Verticals

Valid values: `PROFESSIONAL`, `REAL_ESTATE`, `HEALTHCARE`, `HUMAN_RESOURCES`, `ENERGY`, `ENTERTAINMENT`, `RETAIL`, `TRANSPORTATION`, `AGRICULTURE`, `INSURANCE`, `POSTAL`, `EDUCATION`, `HOSPITALITY`, `FINANCIAL`, `POLITICAL`, `GAMBLING`, `LEGAL`, `CONSTRUCTION`, `NGO`, `MANUFACTURING`, `GOVERNMENT`, `TECHNOLOGY`, `COMMUNICATION`.

## Brand Vetting

Vetting is performed by a third-party partner (e.g., Aegis/Campaign Verify) and produces a trust score from 0 to 100. Without vetting, brands default to the lowest throughput tier.

```
curl -X POST https://api.telnyx.com/v2/10dlc/brand/{brandId}/externalVetting \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "evpId": "AEGIS",
    "vettingClass": "STANDARD"
  }'
```

### Vetting Classes

| Class | Cost | Use Case |
| --- | --- | --- |
| `STANDARD` | ~$4 | Default for most brands |
| `ENHANCED` | ~$40 | Higher trust scores, faster approval |

**Idempotency:** Submitting the same `evpId` + `vettingClass` for a brand that already has a successful vetting (within the last 180 days) or one currently being processed returns `400` with error code `10012` ("Duplicate resource"). Failed vettings are excluded from this check, so you can retry immediately. To retrieve existing vettings, use `GET /v2/10dlc/brand/{brandId}/externalVetting`.

Vetting typically takes 1–7 business days. You can create campaigns before vetting completes, but throughput will be limited until a score is assigned.

### Maximizing Your Vetting Score

1. **Website is live** and matches your brand information
2. **EIN matches** your legal business name exactly (IRS records)
3. **Phone number** is findable via Google for your business
4. **Email domain** matches your website domain
5. **Business address** is verifiable

If your initial score is below 75, consider requesting enhanced vetting for a more thorough review. Contact [Telnyx support](mailto:support@telnyx.com) for guidance.
