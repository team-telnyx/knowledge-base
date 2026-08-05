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

*Part 2 of 6 — see also: [Part 1](international-sms-compliance-encoding-and-message-detail-records--part-1.md), [Part 3](international-sms-compliance-encoding-and-message-detail-records--part-3.md), [Part 4](international-sms-compliance-encoding-and-message-detail-records--part-4.md), [Part 5](international-sms-compliance-encoding-and-message-detail-records--part-5.md), [Part 6](international-sms-compliance-encoding-and-message-detail-records--part-6.md)*

A consolidated reference covering country-specific SMS compliance requirements for the top international destinations, SMS message encoding and segment calculation, and how to use Message Detail Records (MDRs) to track delivery, cost, and errors.

## Opt-in requirements by region

### Europe (GDPR + ePrivacy)

The EU's GDPR and ePrivacy Directive set the baseline for all EU/EEA countries:

1. **Explicit consent required** — Recipients must actively opt in to receive messages. Pre-checked boxes are **not valid consent** under GDPR.
2. **Purpose limitation** — Consent must specify what types of messages the user will receive. "We may contact you" is too vague.
3. **Right to withdraw** — Users must be able to opt out at any time, and the process must be as easy as opting in.
4. **Record keeping** — Maintain records of when and how consent was obtained. You must be able to prove consent if challenged.

**GDPR-compliant consent example:**

```
☐ I agree to receive appointment reminders and order updates from [Company]
  via SMS to the phone number provided. Message frequency: up to 4 msg/month.
  Reply STOP to unsubscribe. Msg & data rates may apply.
```

**Country variations within the EU:**

- **Germany:** Requires "double opt-in" (confirmation SMS after initial signup) as best practice
- **France:** CNIL requires explicit, separate consent for marketing SMS
- **Spain:** AEPD allows "soft opt-in" for existing customers (similar products/services only)
- **Italy:** Garante requires clear separation between service and marketing consent

### North America

| Requirement | United States | Canada |
| --- | --- | --- |
| Governing law | TCPA + CTIA guidelines | CASL |
| Consent type | Express written (marketing) / Express (transactional) | Express or implied |
| Opt-out mechanism | STOP keyword mandatory | Unsubscribe mechanism required |
| Record retention | Recommended 4+ years | Duration of consent |
| Pre-registration | 10DLC / toll-free verification | Short code approval |

### Asia-Pacific

| Country | Key requirement |
| --- | --- |
| 🇮🇳 India | DLT registration + template approval. DND registry filtering for promotional. |
| 🇦🇺 Australia | Express consent required (Spam Act 2003). Include sender identity + opt-out. |
| 🇸🇬 Singapore | SSIR registration. PDPA consent rules. No SMS between 9 PM – 9 AM without consent. |
| 🇯🇵 Japan | Act on Specified Commercial Transactions. Opt-out link required. Sender identification mandatory. |
| 🇰🇷 South Korea | Pre-approved templates only. 080 opt-out number required for commercial messages. |

### Latin America

| Country | Key requirement |
| --- | --- |
| 🇧🇷 Brazil | LGPD consent required. No messages between 9 PM – 9 AM. Include opt-out. |
| 🇲🇽 Mexico | LFPDPPP consent. Include sender identity. Opt-out mechanism required. |
| 🇨🇴 Colombia | SIC consent requirements. Habeas Data law. Pre-registration recommended. |
| 🇦🇷 Argentina | PDPA consent. National Do Not Call Registry must be checked. |

## Content restrictions

### Universally restricted content

These content types are restricted or prohibited in most countries:

| Content type | Status | Notes |
| --- | --- | --- |
| Cannabis / CBD | 🚫 Prohibited in most countries | Even where locally legal, carriers often block |
| Gambling | ⚠️ Heavily regulated | Requires specific licensing in most jurisdictions |
| Adult content | 🚫 Prohibited | Blocked by most carriers globally |
| Phishing / fraud | 🚫 Prohibited | Immediate account termination |
| Financial services | ⚠️ Regulated | Must comply with local financial advertising laws |
| Healthcare / pharma | ⚠️ Regulated | Prescription drug messaging restricted in many countries |
| Political campaigns | ⚠️ Varies by country | Some countries ban political SMS entirely |

### Country-specific restrictions

🇬🇧 **United Kingdom**

- **Financial promotions:** Must be approved by an FCA-authorized firm
- **Age-gated content:** Must use age verification for alcohol, gambling
- **Charity messaging:** Regulated by the Fundraising Regulator
- **Marketing hours:** No legal restriction, but industry best practice is 8 AM – 9 PM

🇩🇪 **Germany**

- **UWG (Competition Law):** Strict consent requirements for all commercial messages
- **Heilmittelwerbegesetz:** Restricts pharmaceutical advertising
- **Glücksspielstaatsvertrag:** Strict gambling advertising rules
- **Double opt-in:** Expected best practice for marketing consent

🇫🇷 **France**

- **Loi Hamon:** Right to opt out of all commercial solicitation
- **Time restrictions:** No commercial SMS 8 PM – 8 AM, Sundays, or public holidays
- **CNIL enforcement:** Active enforcement with significant fines
- **Language:** Commercial messages should be in French

🇮🇳 **India**

- **Promotional hours:** 9 AM – 9 PM IST only (mandatory, not best practice)
- **DND registry:** Promotional messages blocked to DND-registered numbers
- **Template approval:** Every message must match a pre-approved template
- **Scrubbing:** Numbers are checked against DND registry before delivery

🇧🇷 **Brazil**

- **LGPD compliance:** Explicit consent with specific purpose
- **Quiet hours:** 9 PM – 9 AM (industry standard)
- **Consumer code:** Price/offer messages must include full terms
- **Language:** Messages should be in Portuguese
