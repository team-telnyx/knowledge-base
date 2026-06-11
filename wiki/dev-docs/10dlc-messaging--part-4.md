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

*Part 4 of 5 — see also: [Part 1](10dlc-messaging--part-1.md), [Part 2](10dlc-messaging--part-2.md), [Part 3](10dlc-messaging--part-3.md), [Part 5](10dlc-messaging--part-5.md)*

10DLC (10-Digit Long Code) is the industry standard for application-to-person (A2P) messaging on US long code numbers. Registering your brand and campaigns with The Campaign Registry (TCR) through Telnyx provides higher throughput, better deliverability, and reduced carrier filtering. Your brand's vetting score directly determines your messaging throughput limits across AT&T, T-Mobile, and other carriers.

## Campaign Appeals

When campaigns are rejected, the appeal process differs based on campaign type and rejection reason.

### Native Campaign Appeals

- **Content issues:** Using the campaign update endpoint automatically resets status to `TCR_ACCEPTED` and re-enters the review queue.
- **External factors (e.g., website compliance):** Use the appeal API endpoint:

```
curl -X POST 'https://api.telnyx.com/10dlc/campaign/{campaignId}/appeal' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"appealReason": "The website has been updated to include the required privacy policy."}'
```

### Partner Campaign Appeals

For partner (shared) campaigns, the CSP sends a `CAMPAIGN_NUDGE` event to TCR after reviewing and approving customer changes. This nudging mechanism cannot be used with native campaigns.

### DCA Rejection Appeals

When a DCA (Direct Connect Aggregator) rejects a campaign:
- **External factors:** Customer fixes issues, notifies Telnyx, Telnyx generates a nudge webhook for the DCA
- **Content issues:** Customer updates content, notifies Telnyx, Telnyx generates a nudge webhook for the DCA

## Sole Proprietor Registration

Sole Proprietor registration enables individuals and small businesses without an EIN to register for 10DLC messaging. It requires identity verification via SMS OTP.

### Constraints

| Constraint | Limit |
| --- | --- |
| Campaigns per brand | 1 |
| Phone numbers per campaign | 1 |
| Mobile phone reuse | Max 3 SP brands per mobile number |
| Throughput | Low-volume (varies by carrier) |

### Registration Flow

1. **Create brand** with `entityType: "SOLE_PROPRIETOR"`, including `firstName`, `lastName`, `mobilePhone` fields. Brand remains in `PENDING` status until OTP verification.
2. **Trigger OTP** — `POST /v2/10dlc/brand/{brandId}/smsOtp` with `pinSms` (containing `@OTP_PIN@` placeholder) and `successSms`. OTP expires after 24 hours.
3. **Check OTP status** — `GET /v2/10dlc/brand/{brandId}/smsOtp`. Delivery statuses: `PENDING`, `DELIVERED_HANDSET`, `DELIVERY_FAILED`, `VERIFIED`, `EXPIRED`.
4. **Verify OTP PIN** — `PUT /v2/10dlc/brand/{brandId}/smsOtp` with `otpPin`. On success, brand status changes to `VERIFIED` and the brand registration fee is charged.
5. **Create campaign** with `usecase: "SOLE_PROPRIETOR"`. SP campaigns are typically auto-approved and become `ACTIVE` immediately.
6. **Assign phone number** — only one number per SP campaign.

### Fees

| Item | Amount | Frequency |
| --- | --- | --- |
| Brand Registration | $4.00 | One-time (charged after verification) |
| Campaign Vetting | $15.00 | Per submission |
| Monthly Maintenance | $2.00 | Monthly |

## ISV and Reseller Onboarding

If you're an ISV, reseller, or SaaS platform sending messages on behalf of customers, you need a **partner campaign** architecture.

### Key Concepts

- **Upstream CSP:** The Campaign Service Provider where you register brands and campaigns with TCR (can be Telnyx or another CSP)
- **Downstream CSP:** The messaging provider that sends traffic (Telnyx acts as your downstream CSP)
- **Shared / Partner Campaign:** A campaign registered at one CSP and shared to another for traffic delivery
- **Campaign Sharing:** The TCR process of granting a downstream CSP access to send traffic for a campaign

### Native vs. Partner Campaigns

| Feature | Native Campaign | Partner (Shared) Campaign |
| --- | --- | --- |
| Registration | Directly on Telnyx | On upstream CSP, shared to Telnyx |
| Brand ownership | Your Telnyx account | Your upstream CSP account |
| Campaign management | Telnyx API | Upstream CSP + Telnyx Partner API |
| Number assignment | Standard | Via partner campaign endpoints |
| Use case | Direct customer | ISV, reseller, multi-tenant |
| Appeal process | Direct API | CSP nudge mechanism |

### ISV Onboarding Steps

1. **Register brands** for each customer (each customer needs their own brand registered with TCR)
2. **Submit brands for vetting** — enhanced vetting is strongly recommended for ISV use cases
3. **Create campaigns** with the `AGENTS_FRANCHISES` use case type; sample messages must accurately reflect what your platform sends; message flow must describe how end users (not your clients) consent to receive messages
4. **Share campaign to Telnyx** — after approval at upstream CSP, share it so Telnyx can accept it
5. **Assign phone numbers** to the shared campaign
6. **Check sharing status** — possible statuses: `PENDING`, `ACCEPTED`, `DECLINED`
7. **Send messages** using the standard Send Message API

### Multi-Tenant Architecture Patterns

**Pattern 1: One brand + campaign per customer (recommended for agencies/resellers)** — Isolated throughput, independent compliance, clear separation. More registration overhead but better isolation.

**Pattern 2: Shared campaign across customers (for SaaS platforms with similar message types)** — Simpler setup, but throughput is shared and one customer's violations affect all.

**Pattern 3: Hybrid (recommended for growth)** — High-volume customers get dedicated brands + campaigns; low-volume customers share a platform campaign; migrate to dedicated as they grow.

### ISV Compliance Responsibilities

- Customer vetting — verify business legitimacy before registration
- Content monitoring — monitor message content for campaign compliance
- Opt-in verification — ensure customers collect proper consent
- Opt-out processing — STOP/HELP keywords must work across all customer traffic
- Volume management — don't exceed throughput limits
- Incident response — process to quickly disable a customer's messaging if they violate policies
- Record retention — keep opt-in records for at least 4 years per CTIA guidelines
- Sample message accuracy — registered samples must match actual production messages

## Choosing a Sender Type

10DLC is one of several sender types available. Choose based on your use case:

| | **10DLC Long Code** | **Toll-Free** | **Short Code** | **RCS** | **Alphanumeric** |
| --- | --- | --- | --- | --- | --- |
| **Throughput** | 3–75 MPS* | 3–150 MPS | 200+ MPS | 100+ MPS | 100+ MPS |
| **Daily Volume** | 10K–200K (T-Mobile)** | Unlimited | Unlimited | Unlimited | Unlimited |
| **Two-Way** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Voice** | ✅ | ✅ | ❌ | ❌ | ❌ |
| **MMS** | US/CA only | US/CA only | US/CA only | Rich media | ❌ |
| **Provisioning** | 2–3 business days | 2–3 business days | 2–6 weeks | 6–10 weeks | Instant |
| **Registration** | Brand + Campaign (TCR) | Toll-free verification | Carrier approval | Google verification | None |
| **Number Cost** | Low (~$1/mo) | Low (~$2/mo) | High (~$500–1000/mo) | Agent setup fee | Free |

\* Throughput varies based on TCR Trust Score. \** T-Mobile daily limits based on brand score.

**When to use 10DLC:** Required for A2P marketing in the US; good for local presence; supports voice + SMS on the same number. **When to consider alternatives:** Toll-free for fast provisioning and handset-level delivery receipts; short codes for very high volume (200+ MPS); alphanumeric sender IDs for international one-way messaging; RCS for rich media experiences.

US toll-free and short code numbers only work for US/CA destinations. For international messaging, use alphanumeric IDs or local numbers.
