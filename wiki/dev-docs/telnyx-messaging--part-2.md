---
title: Telnyx Messaging
summary: Telnyx Messaging is a unified API for application-to-person (A2P) messaging
  across 10DLC long codes, toll-free numbers, short codes, alphanumeric sender IDs,
  RCS, and WhatsApp. This page covers sender type selection, messaging profiles, phone
  number configuration, 10DLC and toll-free registration, campaign management, message
  encoding, MMS, rate limiting, number pooling, opt-in/opt-out compliance, webhooks,
  error codes, spend limits, RCS, WhatsApp Business messaging, hosted SMS, international
  compliance, and common use cases like 2FA and appointment reminders.
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
- url: https://developers.telnyx.com/docs/messaging/messages/2fa/index
- url: https://developers.telnyx.com/docs/messaging/messages/advanced-opt-in-out/index
- url: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id/index
- url: https://developers.telnyx.com/docs/messaging/messages/appointment-reminder
- url: https://developers.telnyx.com/docs/messaging/messages/chat-sdk-adapter
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
- url: https://developers.telnyx.com/docs/messaging/messages/group-messaging
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration/index
- url: https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-capabilities/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-deeplinks
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index
- url: https://developers.telnyx.com/docs/messaging/messages/receive-message
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-rcs-webhooks/index
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks/index
- url: https://developers.telnyx.com/docs/messaging/messages/schedule-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-an-rcs-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-receive-mms/index
- url: https://developers.telnyx.com/docs/messaging/messages/short-code/index
- url: https://developers.telnyx.com/docs/messaging/messages/smart-encoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
updated_at: 2026-07-17T09:15:02Z
---

# Telnyx Messaging

*Part 2 of 5 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 3](telnyx-messaging--part-3.md), [Part 4](telnyx-messaging--part-4.md), [Part 5](telnyx-messaging--part-5.md)*

Telnyx Messaging is a unified API for application-to-person (A2P) messaging across 10DLC long codes, toll-free numbers, short codes, alphanumeric sender IDs, RCS, and WhatsApp. This page covers sender type selection, messaging profiles, phone number configuration, 10DLC and toll-free registration, campaign management, message encoding, MMS, rate limiting, number pooling, opt-in/opt-out compliance, webhooks, error codes, spend limits, RCS, WhatsApp Business messaging, hosted SMS, international compliance, and common use cases like 2FA and appointment reminders.

## 10DLC Registration

10DLC (10-Digit Long Code) is the industry standard for A2P messaging on US long code numbers. Registration provides higher throughput, better deliverability, and reduced carrier filtering.

### Registration Flow

1. **Create Brand** — Register your business identity with The Campaign Registry (TCR). Instant.
2. **Vet Brand** — Third-party vetting determines your trust score (0–100). 1–7 business days.
3. **Create Campaign** — Register your messaging use case. Instant (pending carrier approval).
4. **Assign Numbers** — Link phone numbers to your campaign. Instant.

### Brand Entity Types

| Entity Type | API Value | Vetting Required |
| --- | --- | --- |
| Private for-profit | `PRIVATE_PROFIT` | Yes |
| Public for-profit | `PUBLIC_PROFIT` | Yes |
| Non-profit | `NON_PROFIT` | Yes |
| Government | `GOVERNMENT` | Yes |
| Sole Proprietor | `SOLE_PROPRIETOR` | OTP only |

### Vetting Score Impact

Your vetting score (0–100) directly determines your messaging throughput.

| Score Range | T-Mobile Daily Cap | AT&T SMS TPM | Category |
| --- | --- | --- | --- |
| 0–24 | 2,000/day | 1 MPS | Low |
| 25–49 | 10,000/day | 4 MPS | Medium-Low |
| 50–74 | 50,000/day | 10 MPS | Medium |
| 75–89 | 100,000/day | 25 MPS | High |
| 90–100 | 200,000+/day | 75 MPS | Highest |

### AT&T Message Classes

| Class | Use Case | Vetting Score | SMS TPM | MMS TPM |
| --- | --- | --- | --- | --- |
| A | Standard (Dedicated) | 75–100 | 4,500 | 2,400 |
| B | Standard (Mixed/Marketing) | 75–100 | 4,500 | 2,400 |
| C | Standard (Dedicated) | 50–74 | 2,400 | 1,200 |
| D | Standard (Mixed/Marketing) | 50–74 | 2,400 | 1,200 |
| E | Standard (Dedicated) | 1–49 | 240 | 150 |
| F | Standard (Mixed/Marketing) | 1–49 | 240 | 150 |
| T | Low Volume Mixed | Any | 75 | 50 |
| W | Sole Proprietor | N/A | 15 | 50 |
| K | Political | — | 4,500 | 2,400 |
| P | Charity / Nonprofit | — | 2,400 | 1,200 |
| S | Social | — | 9,000 | 2,400 |
| X | Emergency / Public Safety | — | 4,500 | 2,400 |
| G | Proxy (per number) | — | 60 | 50 |
| N | Agents & Franchises (per number) | — | 60 | 50 |

### T-Mobile Brand Tiers

| Brand Tier | Vetting Score | Daily SMS Cap |
| --- | --- | --- |
| Top | 75–100 | 200,000 |
| High | 50–74 | 40,000 |
| Medium | 25–49 | 10,000 |
| Basic | 1–24 | 2,000 |
| Sole Proprietor | N/A | 1,000 |

T-Mobile caps are per brand, not per campaign. Unvetted brands default to the Basic tier unless listed on the Russell 3000 index.

### Campaign Use Case Types

**Standard use cases:**

| Use Case | Description |
| --- | --- |
| `CUSTOMER_CARE` | Support and service messages |
| `DELIVERY_NOTIFICATION` | Order and shipping updates |
| `ACCOUNT_NOTIFICATION` | Account alerts and changes |
| `MARKETING` | Promotional content |
| `2FA` | Two-factor authentication codes |
| `SECURITY_ALERT` | Security-related notifications |
| `POLLING_VOTING` | Surveys and polls |
| `CHARITY` | Nonprofit fundraising and awareness |
| `POLITICAL` | Political campaigns and advocacy |
| `MIXED` | Multiple message types (most common) |

**Special use cases:**

| Use Case | Description |
| --- | --- |
| `LOW_VOLUME` | Under 6,000 messages/month |
| `SOLE_PROPRIETOR` | Individual/small business without EIN |
| `EMERGENCY` | Life-threatening alerts |
| `AGENTS_FRANCHISES` | ISVs sending on behalf of clients |
| `SWEEPSTAKES` | Contests and giveaways |

### Sole Proprietor Registration

Sole Proprietor brands have specific constraints: 1 campaign, 1 phone number, max 3 SP brands per mobile number, low throughput. Registration requires identity verification via SMS OTP before campaigns can be created.

**Fees:**

| Item | Amount | Frequency |
| --- | --- | --- |
| Brand Registration | $4.00 | One-time (after verification) |
| Campaign Vetting | $15.00 | Per submission |
| Monthly Maintenance | $2.00 | Monthly |

### ISV & Reseller Architecture

ISVs, resellers, and SaaS platforms sending on behalf of customers need a partner campaign architecture. Telnyx acts as the downstream CSP — campaigns are registered at an upstream CSP and shared to Telnyx for number assignment and messaging.

**Multi-tenant patterns:**

- **One brand + campaign per customer** (recommended for agencies): Isolated throughput per customer, independent compliance status.
- **Shared campaign across customers** (best for SaaS): Simpler setup, but throughput is shared and one customer's violations affect all.
- **Hybrid** (recommended for growth): High-volume customers get dedicated brands + campaigns; low-volume customers share a platform campaign.

For ISV campaigns, use the `AGENTS_FRANCHISES` use case type. Each campaign undergoes manual review by TCR (5–10 business days).

### Disallowed Use Cases

The following use cases will be rejected or result in very low throughput:

- Unsolicited messaging (cold outreach, lead generation spam)
- Non-direct lending (3rd party auto loans, payday loans)
- Indirect debt collection
- Cannabis or CBD marketing
- Gambling (unless licensed)
- SHAFT content (Sex, Hate, Alcohol, Firearms, Tobacco)
- Sweepstakes and "free giveaway" campaigns

## Toll-Free Verification

Toll-free numbers (800, 888, 877, 866, 855, 844, 833) used for SMS/MMS require carrier verification. Starting February 17, 2026, three Business Registration Number (BRN) fields are required for all new submissions:

- `businessRegistrationNumber` — Official government-issued business registration identifier
- `businessRegistrationType` — Type or classification (e.g., `EIN`, `CRA`, `ABN`, `VAT`, `SSN`)
- `businessRegistrationCountry` — ISO 3166-1 alpha-2 country code

**Verification timeline:** 1–2 weeks. Unverified toll-free numbers have limited throughput (~0.25 MPS) and may experience carrier filtering. Verified numbers support up to 20 MPS.

## Short Codes

Short codes are 5- or 6-digit numbers designed for high-volume A2P messaging, offering up to 1,000 MPS. Provisioning takes 8–12 weeks and requires carrier certification. Vanity codes (memorable numbers) are available but subject to availability.

## Sending Messages

### Send Your First Message

```bash
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "+15551234567",
    "to": "+15559876543",
    "text": "Hello, world!"
  }'
```

The `from` field determines your sender type automatically:

- Phone number (`+15551234567`) → Long code or toll-free
- Short code (`12345`) → Short code
- Alphanumeric (`"MyBrand"`) → Alphanumeric sender ID

### E.164 Format

Always include the `+` prefix, country code, and full number with no spaces or punctuation.

| Country | Format | Example |
| --- | --- | --- |
| US/Canada | +1 + 10 digits | `+15551234567` |
| UK | +44 + 10–11 digits | `+447911123456` |
| Germany | +49 + 10–11 digits | `+4915123456789` |
| Australia | +61 + 9 digits | `+61412345678` |
| Brazil | +55 + 10–11 digits | `+5511987654321` |
| India | +91 + 10 digits | `+919876543210` |

### Scheduled Messages

Schedule messages for future delivery using the `send_at` parameter:

- `send_at` must be at least 5 minutes and no more than 5 days in the future
- Scheduling accuracy is up to 1 minute
- Maximum of 1 million scheduled messages at any given time
- Cancellation available up to 1 minute before send time

### Group Messaging

Send group MMS to up to 8 recipients per conversation using `/v2/messages/group_mms`. All messages are billed at MMS rates. US and Canada destinations only. Requires v2 webhook version on your messaging profile.
