---
title: Toll-Free Verification
summary: Telnyx toll-free verification requires Business Registration Number (BRN)
  fields for all new submissions starting February 17, 2026. This page covers the
  required and optional fields, API usage for creating, retrieving, and updating verification
  requests, common rejection reasons, the resubmission process, delivery troubleshooting,
  and guidance on choosing between toll-free and 10DLC messaging.
sources:
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
updated_at: 2026-08-05T13:58:33Z
---

# Toll-Free Verification

*Part 1 of 6 — see also: [Part 2](toll-free-verification--part-2.md), [Part 3](toll-free-verification--part-3.md), [Part 4](toll-free-verification--part-4.md), [Part 5](toll-free-verification--part-5.md), [Part 6](toll-free-verification--part-6.md)*

Telnyx toll-free verification requires Business Registration Number (BRN) fields for all new submissions starting February 17, 2026. This page covers the required and optional fields, API usage for creating, retrieving, and updating verification requests, common rejection reasons, the resubmission process, delivery troubleshooting, and guidance on choosing between toll-free and 10DLC messaging.

## Overview

U.S. wireless carriers require toll-free numbers (800, 888, 877, 866, 855, 844, 833) used for SMS/MMS to complete verification. Starting **February 17, 2026**, three Business Registration Number (BRN) fields are required for all new toll-free verification submissions:

- `businessRegistrationNumber`
- `businessRegistrationType`
- `businessRegistrationCountry`

Submissions missing these fields will be rejected with HTTP 400. The new BRN fields provide carriers with verified business identity information, helping to reduce verification processing time, improve approval rates, ensure compliance with carrier policies, and prevent fraudulent messaging.

## Required Business Registration Fields

### businessRegistrationNumber

The official government-issued business registration identifier.

| Property | Value |
| --- | --- |
| **Type** | String |
| **Max Length** | 500 characters |
| **Required** | February 17, 2026 |
| **Nullable** | Currently yes, no after Feb 2026 |

**Examples by Country**:

| Country | Type | Example Format |
| --- | --- | --- |
| United States | EIN | `12-3456789` or `123456789` |
| Canada | Business Number | `123456789RC0001` |
| United Kingdom | Companies House | `12345678` |
| Australia | ABN | `51824753556` |
| Germany | VAT | `DE123456789` |

**Where to Find**:

- **US**: [IRS EIN Lookup](https://www.irs.gov/) — Check your EIN confirmation letter or SS-4 form
- **Canada**: CRA Business Number from your registration documents
- **UK**: [Companies House](https://www.gov.uk/get-information-about-a-company) registration certificate
- **Australia**: [ABN Lookup](https://abr.business.gov.au/)
- **EU**: VAT registration certificate from your national tax authority

### businessRegistrationType

The type or classification of your business registration.

| Property | Value |
| --- | --- |
| **Type** | String |
| **Max Length** | 500 characters |
| **Required** | February 17, 2026 |
| **Nullable** | Currently yes, no after Feb 2026 |

**Common Values**:

- `EIN` — U.S. Employer Identification Number
- `CRA` — Canadian Revenue Agency Business Number
- `Companies House` — UK company registration
- `ABN` — Australian Business Number
- `VAT` — European Union VAT registration
- `SSN` — For U.S. sole proprietors without EIN

### businessRegistrationCountry

ISO 3166-1 alpha-2 country code of the authority that issued the registration.

| Property | Value |
| --- | --- |
| **Type** | String |
| **Length** | Exactly 2 characters |
| **Format** | ISO 3166-1 alpha-2 |
| **Required** | February 17, 2026 |
| **Nullable** | Currently yes, no after Feb 2026 |

**Validation**:

- Must be exactly 2 letters
- Only alphabetic characters (A-Z)
- Automatically converted to uppercase (`"us"` → `"US"`)
- Returns HTTP 400 if invalid

**Example Values**: `US`, `CA`, `GB`, `AU`, `DE`, `FR`, `JP`. See the complete list at [ISO 3166-1 country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

## Optional Fields

These fields are optional but recommended for faster verification processing.

### doingBusinessAs

DBA, trade name, or brand name if different from your legal business name.

| Property | Value |
| --- | --- |
| **Type** | String |
| **Max Length** | 500 characters |
| **Required** | No |

**Example**: Legal name "Acme Corporation Inc.", DBA "Acme Services".

### entityType

Legal business entity classification.

| Property | Value |
| --- | --- |
| **Type** | Enum |
| **Required** | No |
| **Allowed Values** | `SOLE_PROPRIETOR`, `PRIVATE_PROFIT`, `PUBLIC_PROFIT`, `NON_PROFIT`, `GOVERNMENT` |

| Value | Description |
| --- | --- |
| `SOLE_PROPRIETOR` | Individual or sole proprietorship |
| `PRIVATE_PROFIT` | Private for-profit corporation (most common) |
| `PUBLIC_PROFIT` | Publicly traded for-profit company |
| `NON_PROFIT` | 501(c) or charitable organization |
| `GOVERNMENT` | Government entity or agency |

### optInConfirmationResponse

Message sent to subscribers confirming their opt-in.

| Property | Value |
| --- | --- |
| **Type** | String |
| **Max Length** | 500 characters |
| **Required** | No |

**Example**: `"You are now subscribed to Acme alerts. Reply STOP to unsubscribe. Msg&data rates may apply."`

### helpMessageResponse

Automated response when subscribers text HELP.

| Property | Value |
| --- | --- |
| **Type** | String |
| **Max Length** | 500 characters |
| **Required** | No |

**Example**: `"Acme Support: Call 1-800-555-0123 or email help@acme.com. Reply STOP to unsubscribe."`

### privacyPolicyURL

URL to your business privacy policy.

| Property | Value |
| --- | --- |
| **Type** | String |
| **Max Length** | 500 characters |
| **Required** | No |

**Example**: `"https://www.acme.com/privacy"`

### termsAndConditionURL

URL to your business terms and conditions.

| Property | Value |
| --- | --- |
| **Type** | String |
| **Max Length** | 500 characters |
| **Required** | No |

**Example**: `"https://www.acme.com/terms"`

### ageGatedContent

Indicates if messaging content requires age verification (18+ or 21+).

| Property | Value |
| --- | --- |
| **Type** | Boolean |
| **Default** | `false` |
| **Required** | No |

Set to `true` for alcohol, tobacco, cannabis, or other age-restricted content.

### optInKeywords

Keywords subscribers use to opt-in to your messaging program.

| Property | Value |
| --- | --- |
| **Type** | String |
| **Max Length** | 500 characters |
| **Required** | No |

**Example**: `"START, YES, SUBSCRIBE, JOIN"`
