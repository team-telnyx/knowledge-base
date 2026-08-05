---
title: 10DLC Onboarding and Phone Number Assignment
summary: Comprehensive guide to registering brands, vetting, creating campaigns, and
  assigning phone numbers for 10DLC A2P messaging on Telnyx — covering both direct
  customer and ISV/reseller architectures, plus bulk operations, webhooks, appeals,
  and troubleshooting.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/isv-reseller-onboarding
- url: https://developers.telnyx.com/docs/messaging/10dlc/phone-number-assignment
- url: https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index
updated_at: 2026-08-05T13:48:57Z
---

# 10DLC Onboarding and Phone Number Assignment

*Part 1 of 5 — see also: [Part 2](10dlc-onboarding-and-phone-number-assignment--part-2.md), [Part 3](10dlc-onboarding-and-phone-number-assignment--part-3.md), [Part 4](10dlc-onboarding-and-phone-number-assignment--part-4.md), [Part 5](10dlc-onboarding-and-phone-number-assignment--part-5.md)*

Comprehensive guide to registering brands, vetting, creating campaigns, and assigning phone numbers for 10DLC A2P messaging on Telnyx — covering both direct customer and ISV/reseller architectures, plus bulk operations, webhooks, appeals, and troubleshooting.

## Overview

10DLC (10-Digit Long Code) is the industry standard for application-to-person (A2P) messaging on US long code numbers. Registering your brand and campaigns provides higher throughput, better deliverability, and reduced carrier filtering. The standard onboarding flow has four steps: create a brand, vet the brand, create a campaign, and assign phone numbers. Vetting is critical because the brand's vetting score directly determines throughput limits, especially on AT&T and T-Mobile.

| Step | What happens | Timeline |
| --- | --- | --- |
| Create Brand | Register your business identity with The Campaign Registry (TCR) | Instant |
| Vet Brand | Third-party vetting determines your trust score (0–100) | 1–7 business days |
| Create Campaign | Register your messaging use case | Instant (pending carrier approval) |
| Assign Numbers | Link phone numbers to your campaign | Instant |

If you are an ISV, reseller, or SaaS platform sending messages on behalf of your customers, you need a **partner campaign** architecture rather than a standard 10DLC registration. Direct customers sending only for their own business should follow the standard [10DLC Quickstart](10dlc-quickstart.md) flow.

## Who needs the ISV/reseller flow

| Scenario | You are… | Your architecture |
| --- | --- | --- |
| SaaS platform | Building messaging into your product | Partner campaign (shared across customers) |
| Reseller / agency | Managing messaging for clients | One brand + campaign per client, or shared |
| ISV | Offering white-label messaging | Partner campaign with downstream CSPs |

## Architecture overview

ISV/reseller 10DLC uses a **shared campaign** model where you register campaigns with your upstream CSP (Campaign Service Provider) and share them to Telnyx for number assignment and messaging.

- **Upstream CSP** — The Campaign Service Provider where you register brands and campaigns with TCR. This could be Telnyx (if you register directly) or another CSP.
- **Downstream CSP** — The messaging provider that sends traffic. Telnyx acts as your downstream CSP — you share campaigns **to** Telnyx for number assignment.
- **Shared / Partner Campaign** — A campaign registered at one CSP and shared to another for traffic delivery. Required for ISV architectures.
- **Campaign Sharing** — The TCR process of granting a downstream CSP access to send traffic for a campaign. Sharing must be accepted by the downstream CSP.

### Native vs. partner campaigns

| Feature | Native Campaign | Partner (Shared) Campaign |
| --- | --- | --- |
| Registration | Directly on Telnyx | On upstream CSP, shared to Telnyx |
| Brand ownership | Your Telnyx account | Your upstream CSP account |
| Campaign management | Telnyx API | Upstream CSP + Telnyx Partner API |
| Number assignment | Standard | Via partner campaign endpoints |
| Use case | Direct customer | ISV, reseller, multi-tenant |
| Appeal process | Direct API | CSP nudge mechanism |

## Prerequisites

Before starting, ensure you have:

1. **Telnyx account with messaging enabled** — [Sign up](https://telnyx.com/sign-up) and complete account verification. You need a Level 2 verified account.
2. **Upstream CSP account** — An account with a CSP where you register brands and campaigns (this can be Telnyx or another provider like Campaign Registry direct access).
3. **Customer business information** — For each customer: legal business name, EIN/tax ID, business address, website, authorized representative contact, and messaging use case details.
4. **Phone numbers** — 10DLC-eligible long code numbers on your Telnyx account. [Purchase numbers](https://portal.telnyx.com/#/app/numbers/buy-numbers) or use existing inventory.

## Step 1: Create a brand

A brand represents the business entity sending messages. Each customer needs their own brand registered with TCR.

### Required fields

| Field | Description | Example |
| --- | --- | --- |
| `entityType` | Business type | `PRIVATE_PROFIT`, `PUBLIC_PROFIT`, `NON_PROFIT`, `GOVERNMENT` |
| `displayName` | Brand display name | `Acme Corp` |
| `companyName` | Legal company name | `Acme Corporation` |
| `ein` | EIN/Tax ID | `12-3456789` |
| `phone` | Business phone | `+15551234567` |
| `street`, `city`, `state`, `postalCode`, `country` | Business address | — |
| `email` | Contact email | `admin@acmecorp.com` |
| `vertical` | Industry vertical | `TECHNOLOGY`, `HEALTHCARE`, `RETAIL`, etc. |

### Register via Telnyx (Native Brand)

```bash
curl -X POST https://api.telnyx.com/v2/10dlc/brand \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "PRIVATE_PROFIT",
    "companyName": "Customer Corp LLC",
    "ein": "12-3456789",
    "einIssuingCountry": "US",
    "phone": "+12025551234",
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "postalCode": "10001",
    "country": "US",
    "email": "compliance@customercorp.com",
    "website": "https://customercorp.com",
    "vertical": "TECHNOLOGY",
    "displayName": "Customer Corp"
  }'
```

```python
import telnyx
import os

telnyx.api_key = os.environ["TELNYX_API_KEY"]

brand = telnyx.Brand.create(
    entity_type="PRIVATE_PROFIT",
    company_name="Customer Corp LLC",
    ein="12-3456789",
    ein_issuing_country="US",
    phone="+12025551234",
    street="123 Main St",
    city="New York",
    state="NY",
    postal_code="10001",
    country="US",
    email="compliance@customercorp.com",
    website="https://customercorp.com",
    vertical="TECHNOLOGY",
    display_name="Customer Corp",
)
print(f"Brand ID: {brand.id}")
```

```javascript
import Telnyx from "telnyx";

const telnyx = new Telnyx(process.env.TELNYX_API_KEY);

const { data: brand } = await telnyx.messaging10dlc.brands.create({
  entityType: "PRIVATE_PROFIT",
  companyName: "Customer Corp LLC",
  ein: "12-3456789",
  einIssuingCountry: "US",
  phone: "+12025551234",
  street: "123 Main St",
  city: "New York",
  state: "NY",
  postalCode: "10001",
  country: "US",
  email: "compliance@customercorp.com",
  website: "https://customercorp.com",
  vertical: "TECHNOLOGY",
  displayName: "Customer Corp",
});
console.log(`Brand ID: ${brand.id}`);
```

### Register via external CSP

If using an external CSP (e.g., direct TCR access), register brands through their API and note the TCR Brand ID (format: `BXXXXXX`). You will need this when sharing campaigns to Telnyx.

### Portal flow

1. Navigate to [Brands](https://portal.telnyx.com/#/messaging-10dlc/brands) in Mission Control Portal.
2. Click **Create Brand** and enter your business information including legal name, EIN, address, and industry vertical.
3. Click **Save**. Your brand is now registered with The Campaign Registry.

## Step 2: Vet your brand

Brand vetting determines your trust score (0–100), which directly affects your messaging throughput. Higher scores unlock more messages per minute. For ISV use cases, **enhanced vetting is strongly recommended**.

```bash
curl -X POST https://api.telnyx.com/v2/10dlc/brand/{brandId}/vetting \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"vettingClass": "ENHANCED"}'
```

Check vetting status:

```bash
curl -s https://api.telnyx.com/v2/10dlc/brand/{brandId} \
  -H "Authorization: Bearer $TELNYX_API_KEY" | jq '.data.vettingScore'
```

Enhanced vetting costs a one-time fee and takes 1–7 business days. Brands with vetting scores above 75 get significantly higher throughput. You can create campaigns before vetting completes, but throughput will be limited until a score is assigned. See [10DLC Rate Limits](10dlc-rate-limits.md) for details.

### Portal flow

1. Click on the brand you want to vet on the [Brands](https://portal.telnyx.com/#/messaging-10dlc/brands) page.
2. Under the Vetting Request section, select **Aegis Mobile** as the provider and **Standard** as the vetting class.
3. Click **Apply for Vetting**. Results typically arrive within 1–7 business days.
