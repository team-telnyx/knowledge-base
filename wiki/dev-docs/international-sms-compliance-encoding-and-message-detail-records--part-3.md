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

*Part 3 of 6 — see also: [Part 1](international-sms-compliance-encoding-and-message-detail-records--part-1.md), [Part 2](international-sms-compliance-encoding-and-message-detail-records--part-2.md), [Part 4](international-sms-compliance-encoding-and-message-detail-records--part-4.md), [Part 5](international-sms-compliance-encoding-and-message-detail-records--part-5.md), [Part 6](international-sms-compliance-encoding-and-message-detail-records--part-6.md)*

A consolidated reference covering country-specific SMS compliance requirements for the top international destinations, SMS message encoding and segment calculation, and how to use Message Detail Records (MDRs) to track delivery, cost, and errors.

## Country-by-country reference

### 🇬🇧 United Kingdom

| Setting | Value |
| --- | --- |
| **Sender types** | Alphanumeric (recommended), long code, short code |
| **Alphanumeric length** | 3–11 characters |
| **Regulation** | PECR + UK GDPR |
| **Regulator** | ICO (Information Commissioner's Office) |
| **Pre-registration** | Recommended (improves deliverability) |
| **Opt-out** | STOP keyword or unsubscribe link |
| **Time restrictions** | None (best practice: 8 AM – 9 PM) |

**Send with alphanumeric sender ID:**

```bash
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "YourBrand",
    "to": "+447700900123",
    "text": "Hi! Your delivery is scheduled for tomorrow between 2-4 PM. Reply STOP to opt out.",
    "messaging_profile_id": "YOUR_MESSAGING_PROFILE_ID"
  }'
```

### 🇮🇳 India

| Setting | Value |
| --- | --- |
| **Sender types** | Alphanumeric only (6 characters, registered header) |
| **Regulation** | TRAI + DLT framework |
| **Regulator** | TRAI (Telecom Regulatory Authority of India) |
| **Pre-registration** | **Mandatory** — DLT entity, header, and template registration |
| **Opt-out** | Handled via DLT/DND registry |
| **Time restrictions** | Promotional: 9 AM – 9 PM IST only |

India requires both **sender ID registration** and **message template approval** before any messages can be sent. Contact [Telnyx support](https://support.telnyx.com) to initiate India DLT registration.

### 🇩🇪 Germany

| Setting | Value |
| --- | --- |
| **Sender types** | Alphanumeric, long code |
| **Regulation** | GDPR + UWG (Competition Act) + TTDSG |
| **Regulator** | BfDI (Federal Data Protection Commissioner) |
| **Pre-registration** | Not required |
| **Opt-out** | Must be free and easy (STOP keyword or link) |
| **Time restrictions** | None legally, best practice 8 AM – 9 PM |

### 🇫🇷 France

| Setting | Value |
| --- | --- |
| **Sender types** | Alphanumeric (registered via OACP), long code, short code |
| **Regulation** | GDPR + Code des postes et des communications |
| **Regulator** | CNIL + ARCEP |
| **Pre-registration** | **Required** — OACP sender ID registration |
| **Opt-out** | "STOP" at no cost to recipient (mandatory) |
| **Time restrictions** | **8 AM – 8 PM, no Sundays/holidays** (mandatory for commercial) |

### 🇦🇺 Australia

| Setting | Value |
| --- | --- |
| **Sender types** | Alphanumeric (registered), long code, short code |
| **Regulation** | Spam Act 2003 + Privacy Act 1988 |
| **Regulator** | ACMA |
| **Pre-registration** | Required (sender ID registration) |
| **Opt-out** | Functional unsubscribe within 5 business days |
| **Time restrictions** | None legally, best practice 9 AM – 8 PM AEST |

### 🇧🇷 Brazil

| Setting | Value |
| --- | --- |
| **Sender types** | Alphanumeric, long code, short code |
| **Regulation** | LGPD + Consumer Protection Code |
| **Regulator** | ANPD (National Data Protection Authority) |
| **Pre-registration** | Recommended |
| **Opt-out** | Easy mechanism required |
| **Time restrictions** | 9 PM – 9 AM quiet hours (industry standard) |

### 🇲🇽 Mexico

| Setting | Value |
| --- | --- |
| **Sender types** | Alphanumeric, long code, short code |
| **Regulation** | LFPDPPP (Federal Data Protection Law) |
| **Regulator** | INAI |
| **Pre-registration** | Not required |
| **Opt-out** | Mechanism required in privacy notice |
| **Time restrictions** | None legally |
