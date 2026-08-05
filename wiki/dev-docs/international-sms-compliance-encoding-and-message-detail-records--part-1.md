---
title: International SMS Compliance, Encoding, and Message Detail Records
summary: A consolidated reference covering country-specific SMS compliance requirements
  for the top international destinations, SMS message encoding and segment calculation,
  and how to use Message Detail Records (MDRs) to track delivery, cost, and errors.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
updated_at: 2026-08-05T13:56:16Z
---

# International SMS Compliance, Encoding, and Message Detail Records

*Part 1 of 6 — see also: [Part 2](international-sms-compliance-encoding-and-message-detail-records--part-2.md), [Part 3](international-sms-compliance-encoding-and-message-detail-records--part-3.md), [Part 4](international-sms-compliance-encoding-and-message-detail-records--part-4.md), [Part 5](international-sms-compliance-encoding-and-message-detail-records--part-5.md), [Part 6](international-sms-compliance-encoding-and-message-detail-records--part-6.md)*

A consolidated reference covering country-specific SMS compliance requirements for the top international destinations, SMS message encoding and segment calculation, and how to use Message Detail Records (MDRs) to track delivery, cost, and errors.

## Overview

Sending SMS internationally requires compliance with country-specific regulations for sender IDs, opt-in consent, content restrictions, and registration requirements. This guide covers the top 10 international messaging destinations and their specific rules, alongside the technical details of message encoding and how to track delivery using Message Detail Records (MDRs).

Regulations change frequently. Always verify current requirements with [Telnyx support](https://support.telnyx.com) before launching messaging in a new country.

## Sender ID types by country

Not every sender type works in every country. Here is what is supported in the top international destinations:

| Country | Alphanumeric ID | Long Code | Short Code | Toll-Free | Pre-Registration |
| --- | --- | --- | --- | --- | --- |
| 🇺🇸 United States | ❌ | ✅ (10DLC) | ✅ | ✅ | 10DLC required |
| 🇨🇦 Canada | ❌ | ✅ | ✅ | ✅ | Short code approval |
| 🇬🇧 United Kingdom | ✅ | ✅ | ✅ | — | Recommended |
| 🇩🇪 Germany | ✅ | ✅ | ✅ | — | No |
| 🇫🇷 France | ✅ | ✅ | ✅ | — | OACP required |
| 🇪🇸 Spain | ✅ | ✅ | ✅ | — | No |
| 🇦🇺 Australia | ✅ | ✅ | ✅ | — | Sender ID registration |
| 🇮🇳 India | ✅ (registered) | ❌ | ❌ | — | DLT mandatory |
| 🇧🇷 Brazil | ✅ | ✅ | ✅ | — | No |
| 🇲🇽 Mexico | ✅ | ✅ | ✅ | — | No |

Alphanumeric sender IDs are **not supported** for US and Canadian destinations. Use [10DLC](10dlc-quickstart.md), [toll-free](toll-free-verification--part-1.md), or [short codes](short-code-messaging.md) instead.

## Countries requiring pre-registration

Several countries require sender ID or entity registration before you can send messages. Failing to register results in blocked traffic or filtered messages.

### Mandatory registration

🇮🇳 **India — DLT Registration (Mandatory)**

India requires **Distributed Ledger Technology (DLT)** registration for all A2P SMS. This is the most complex international registration requirement.

**What you need:**

1. **Entity registration** on a DLT platform (JioConnect, Vodafone DLT, Airtel DLT, or BSNL DLT)
2. **Header (sender ID) registration** — your alphanumeric sender ID must be approved
3. **Template registration** — every message template must be pre-approved
4. **Content category** — transactional, promotional, or service

**Registration steps:**

1. Register as a business entity on one of the DLT platforms
2. Submit your sender ID (called "header") for approval
3. Create and submit message templates
4. Provide Telnyx with your DLT Entity ID, registered headers, and template IDs

**Message categories:**

| Category | Allowed Hours | DND Filtering | Example |
| --- | --- | --- | --- |
| Transactional | 24/7 | Exempt | OTP, order confirmations |
| Service (Implicit) | 24/7 | Exempt | Account updates to existing customers |
| Promotional | 9 AM – 9 PM IST | Applies | Marketing, offers, discounts |

Promotional messages to users on the Do Not Disturb (DND) registry will be blocked. Transactional and service messages are exempt from DND filtering.

**Template format:**

```
Dear {#var#}, your order {#var#} has been shipped.
Track at {#var#}. Delivery by {#var#}.
```

Variables are marked with `{#var#}` and the template must match exactly at delivery time.

🇫🇷 **France — OACP Registration**

France requires registration through the **Off-net Application-to-Person (OACP)** framework for commercial SMS.

**Requirements:**

- Sender ID must be registered with French carriers
- Opt-out must include "STOP" at no cost to the recipient
- Commercial messages restricted to 8 AM – 8 PM local time
- No commercial SMS on Sundays or public holidays
- CNIL (French data authority) consent rules apply

**Registration process:**

1. Submit sender ID registration through Telnyx support
2. Provide business documentation (SIRET number for French businesses)
3. Allow 5–10 business days for approval

Unregistered sender IDs may be silently filtered by French carriers.

🇦🇺 **Australia — Sender ID Registration**

Australia's ACMA requires sender ID registration for A2P messaging.

**Requirements:**

- Alphanumeric sender IDs must be registered with carriers
- Messages must include opt-out instructions
- Commercial messages must comply with the Spam Act 2003
- Sender must have consent (express or inferred)

**Registration:**

1. Submit sender ID through Telnyx support
2. Provide Australian Business Number (ABN) or equivalent
3. Typical approval: 3–5 business days

🇸🇬 **Singapore — SSIR Registration**

Singapore's SMS Sender ID Registry (SSIR) requires all organizations to register sender IDs.

**Requirements:**

- Mandatory SSIR registration since January 2023
- Unregistered alphanumeric sender IDs display as "Likely-SCAM"
- Registration through SGNIC (Singapore Network Information Centre)

**Process:**

1. Register on the SSIR portal (sgnic.sg)
2. Submit sender ID with business documentation
3. Link registered sender ID to Telnyx account via support

### Recommended (not mandatory) registration

| Country | Registration | Benefit |
| --- | --- | --- |
| 🇬🇧 United Kingdom | Sender ID pre-registration | Higher delivery rates, reduced filtering |
| 🇩🇪 Germany | None required | — |
| 🇪🇸 Spain | None required | — |
| 🇧🇷 Brazil | Sender ID registration | Better deliverability |
| 🇲🇽 Mexico | None required | — |
