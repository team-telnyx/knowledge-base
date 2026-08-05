---
title: Choosing a Sender Type
summary: A guide to selecting the right Telnyx messaging sender type — 10DLC long
  code, toll-free, short code, RCS, or alphanumeric sender ID — based on use case,
  region, throughput, and registration requirements, with a quick-start example for
  sending your first message.
sources:
- url: https://developers.telnyx.com/docs/messaging/getting-started/choosing-your-sender-type/index
updated_at: 2026-08-05T13:53:35Z
---

# Choosing a Sender Type

*Part 1 of 2 — see also: [Part 2](choosing-a-sender-type--part-2.md)*

A guide to selecting the right Telnyx messaging sender type — 10DLC long code, toll-free, short code, RCS, or alphanumeric sender ID — based on use case, region, throughput, and registration requirements, with a quick-start example for sending your first message.

## Use Case Decision Tree

Not sure which sender type fits? Start with your primary use case:

**🔔 Transactional alerts (OTPs, order updates, appointment reminders)**

- **Toll-free** — Fast provisioning (2–3 days), high throughput, handset-level delivery receipts. Ideal for US/CA transactional messaging.
- **10DLC long code** — Good alternative if you want a local presence. Requires brand + campaign registration (2–3 business days).
- **Short code** — Best for very high volume (200+ MPS). Longer provisioning (2–6 weeks) and higher cost.

For OTP/2FA specifically, see the [Two-Factor Authentication](two-factor-authentication.md) guide.

**📢 Marketing & promotional campaigns**

- **10DLC long code** — Required for A2P marketing in the US. Register your brand and campaign through [10DLC Registration](10dlc-registration.md).
- **Toll-free** — Good for mixed marketing + transactional. Requires [Toll-Free Verification](toll-free-verification--part-1.md).
- **Short code** — Premium option for brand recognition and highest throughput.
- **RCS** — Rich media cards, carousels, and suggested actions for supported devices.

**💬 Conversational / two-way messaging**

- **10DLC long code** — Local number feel, supports voice + SMS on the same number.
- **Toll-free** — Works well for two-way if local presence isn't important.
- **RCS** — Rich interactive experience with read receipts, typing indicators, and suggested replies.

Alphanumeric sender IDs are **one-way only** — recipients cannot reply.

**🌍 International messaging**

- **Alphanumeric sender ID** — Supported in 100+ countries. No number procurement needed. Great for brand recognition internationally.
- **Local long codes** — Required in some countries. Use the coverage checker for availability.

US toll-free and short code numbers only work for US/CA destinations. For international, use alphanumeric IDs or local numbers.

**📱 Rich media experiences (images, buttons, carousels)**

- **RCS** — Full rich media support: images, video, carousels, suggested actions, branded sender profiles.
- **MMS via long code/toll-free** — Image and video support for US/CA only.

See the [RCS Getting Started](rcs-getting-started--part-1.md) guide for details.

## Sender Comparison

### Capabilities at a Glance

|  | **10DLC Long Code** | **Toll-Free** | **Short Code** | **RCS** | **Alphanumeric** |
| --- | --- | --- | --- | --- | --- |
| **Brand Recognition** | Local number | Brand | Brand | Brand (verified) | Brand name |
| **Throughput** | 3–75 MPS* | 3–150 MPS | 200+ MPS | 100+ MPS | 100+ MPS |
| **Daily Volume Limits** | 10K–200K (T-Mobile)** | Unlimited | Unlimited | Unlimited | Unlimited |
| **Two-Way Messaging** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **Voice Support** | ✅ Yes | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Delivery Receipts** | Carrier only | Handset | Handset | Handset | Handset |
| **MMS Support** | US/CA only | US/CA only | US/CA only | Rich media | ❌ No |
| **Opt-Out Management** | Telnyx managed | Network managed | Telnyx managed | Telnyx managed | N/A |

\* Throughput varies based on TCR Trust Score. \*\* T-Mobile daily limits based on TCR brand score; can be increased upon request.

### Registration & Cost Comparison

Understanding the time and cost investment for each sender type helps you plan your launch:

|  | **10DLC Long Code** | **Toll-Free** | **Short Code** | **RCS** | **Alphanumeric** |
| --- | --- | --- | --- | --- | --- |
| **Provisioning Time** | 2–3 business days | 2–3 business days | 2–6 weeks | 6–10 weeks | Instant |
| **Registration Required** | Brand + Campaign (TCR) | Toll-free verification | Carrier approval | Google verification | None |
| **Number Procurement Cost** | Low (~$1/mo) | Low (~$2/mo) | High (~$500–1000/mo) | Agent setup fee | Free |
| **Per-Message Cost** | Standard rates | Standard rates | Premium rates | Standard rates | Standard rates |
| **Renewal/Ongoing** | Annual brand vetting | One-time verification | Monthly lease | Ongoing | None |

## Regional Considerations

Sender type availability varies by country. Key regional considerations include:

**United States & Canada**

- **10DLC** is required for A2P messaging to US mobile numbers (enforced by carriers since 2023)
- **Toll-free** numbers work for both US and CA
- **Short codes** are country-specific (US short codes don't work in CA and vice versa)
- **MMS** is supported on long code, toll-free, and short code
- **RCS** is available for Android users

**Europe**

- **Alphanumeric sender IDs** are widely supported and commonly used
- Some countries require pre-registration of alphanumeric IDs (e.g., UK, France)
- **Local long codes** may be required for two-way messaging
- Short codes are available in select markets
- GDPR compliance required for all messaging

**Latin America**

- **Alphanumeric sender IDs** supported in most countries
- **Local long codes** recommended for better deliverability
- Some carriers require pre-approved sender IDs or templates
- WhatsApp is dominant — consider RCS as an alternative rich channel

**Asia Pacific**

- Regulations vary significantly by country
- **India** requires DLT registration and approved templates
- **Australia** supports alphanumeric IDs and local numbers
- Some countries require local entity for number procurement
