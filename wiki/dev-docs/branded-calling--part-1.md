---
title: Branded Calling
summary: 'Branded Calling is a Telnyx beta product (US-only) that displays a verified
  business identity (name, logo, call reason) on outbound calls. This page covers
  the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms
  of Service, activating the product, creating and vetting a Display Identity Record
  (DIR), attaching phone numbers in batches, configuring call reasons, and handling
  infringement claims.'
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
updated_at: 2026-07-17T09:13:14Z
---

# Branded Calling

*Part 1 of 8 — see also: [Part 2](branded-calling--part-2.md), [Part 3](branded-calling--part-3.md), [Part 4](branded-calling--part-4.md), [Part 5](branded-calling--part-5.md), [Part 6](branded-calling--part-6.md), [Part 7](branded-calling--part-7.md), [Part 8](branded-calling--part-8.md)*

Branded Calling is a Telnyx beta product (US-only) that displays a verified business identity (name, logo, call reason) on outbound calls. This page covers the full lifecycle: registering an Enterprise, accepting the Branded Calling Terms of Service, activating the product, creating and vetting a Display Identity Record (DIR), attaching phone numbers in batches, configuring call reasons, and handling infringement claims.

## Overview

Branded Calling displays your verified business identity on the recipient's phone screen before they answer. Instead of seeing a bare phone number, or worse, "Spam Likely", recipients see your business name, logo, and the reason for your call. Branded Calling is currently in **beta** and supported in the **US only**. The exact information displayed depends on the carrier network, device manufacturer, device type, and OS version.

The product is built on an industry-wide registry managed by CTIA. Telnyx handles all ecosystem interactions on your behalf, so you interact only with the Telnyx API.

## How it works

1. You register your business as an **Enterprise** and create a display identity (**Display Identity Record**) with your name, logo, and call reason.
2. Telnyx vets the DIR, verifying your business identity, IP ownership, and compliance.
3. You associate your Telnyx phone numbers with the verified DIR.
4. When you place a call from those numbers, Telnyx automatically signs the call with a cryptographic token (SHAKEN PASSporT) containing your DIR's rich call data.
5. The terminating carrier verifies the signature and renders your DIR info on the recipient's device.

## Resource hierarchy

```
Enterprise (your organization, registered once)
├── Display Identity Record (DIR, the display identity)
│   ├── Phone-number Batch (the unit of carrier-network vetting)
│   │   ├── Phone Number (+15551234567)
│   │   └── Phone Number (+15559876543)
│   └── Call Reasons ["Customer Service", "Appointment Reminder"]
├── Display Identity Record (DIR, another identity)
│   └── Phone-number Batch
│       └── Phone Number (+15550001111)
└── Terms of Service Agreement (Branded Calling)
```

- An **Enterprise** can have multiple **Display Identity Records** (DIRs).
- Each **Display Identity Record** has its own display name, logo, call reasons, and phone numbers.
- A **Phone Number** belongs to exactly one Display Identity Record.
- Phone numbers are added in **batches**: each `POST` creates one batch, and the batch is the unit that goes through carrier-network vetting.
- **Call reasons** are set at the Display Identity Record level.

## Key concepts

| Term | Description |
| --- | --- |
| **Enterprise** | Your top-level business registration. Required before creating DIRs. |
| **Display Identity Record (DIR)** | Defines what recipients see (name, logo, call reason). |
| **Vetting** | The verification process that validates your DIR identity and business information. |
| **Call Reason** | Text shown to recipients explaining why you're calling (e.g. "Appointment Reminder"). |

## Pricing

Branded Calling pricing has three components:

| Component | Cost | Description |
| --- | --- | |
| **Enterprise registration** | Free | Registering your business as an Enterprise is free of charge. |
| **Brand registration (OTC)** | $50 one-time per Brand | A one-time fee when you create a Display Identity Record (Brand). |
| **Brand registration (MRC)** | $50/month per Brand | A recurring monthly fee for each active Brand. |
| **Branded Call Display** | $0.075 per call | Charged per call that displays your branded identity to the recipient. |

For the full pricing details, see the [Branded Calling pricing page](https://telnyx.com/pricing/branded-calling).

## Access requirements

All Branded Calling endpoints require a **verified** or **enterprise-level** Telnyx account. Trial and standard paid accounts cannot access these features. See [Account Levels and Capabilities](account-levels-and-capabilities.md) for details on upgrading.
