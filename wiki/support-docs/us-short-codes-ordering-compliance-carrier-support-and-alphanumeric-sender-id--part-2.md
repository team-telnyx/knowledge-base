---
title: 'US Short Codes: Ordering, Compliance, Carrier Support, and Alphanumeric Sender
  ID'
summary: End-to-end guide to ordering and migrating US short codes with Telnyx, mandatory
  Short Code Registry (SCR) brand/content‑provider registration, key compliance requirements
  (CTA, HELP/STOP, terms and privacy), carrier notes, supported-carrier scope, and
  how Alphanumeric Sender ID works outside the US/Canada.
sources:
- url: https://support.telnyx.com/en/articles/10245573-us-short-code-ordering-process
- url: https://support.telnyx.com/en/articles/10245615-short-code-brand-and-content-provider-registration-process
- url: https://support.telnyx.com/en/articles/11385511-short-code-compliance-quick-reference-guide
- url: https://support.telnyx.com/en/articles/4967485-short-code-supported-carriers
- url: https://support.telnyx.com/en/articles/9311492-standards-for-us-short-code-keywords-help-stop-and-opt-in-confirmation
- url: https://support.telnyx.com/en/articles/9311566-regulatory-guidelines-for-us-short-code-marketing-and-opt-in-procedures
- url: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id
- url: https://support.telnyx.com/en/articles/4371498-sending-alphanumeric-sms-sender-id
updated_at: 2026-05-20T14:19:13Z
---

# US Short Codes: Ordering, Compliance, Carrier Support, and Alphanumeric Sender ID

*Part 2 of 2 — see also: [Part 1](us-short-codes-ordering-compliance-carrier-support-and-alphanumeric-sender-id--part-1.md)*

End-to-end guide to ordering and migrating US short codes with Telnyx, mandatory Short Code Registry (SCR) brand/content‑provider registration, key compliance requirements (CTA, HELP/STOP, terms and privacy), carrier notes, supported-carrier scope, and how Alphanumeric Sender ID works outside the US/Canada.

## Alphanumeric Sender ID (outside the US/Canada)
Alphanumeric Sender ID lets you set a brand or company name as the sender for one‑way international SMS. It is not supported by carriers in the US or Canada.

Key rules and capabilities
- Length: 3–11 characters; allowed: A–Z, a–z, 0–9, and space. The ID cannot be only numbers.
- Account level: Telnyx Level 2 verification is required.
- Country behavior varies: in some countries the ID is maintained; in others it may be overwritten to ensure delivery; many destinations require preregistration (and may have additional constraints like minimum volumes, local‑brand requirements, or use‑case vetting). Capabilities change over time.
- Full, country‑by‑country capabilities and prerequisites: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id

How to send with Alphanumeric Sender ID
- Prepare your Telnyx messaging profile and webhook settings as needed.
- When sending via Telnyx Messaging APIs, set the “from” value to your desired Alphanumeric Sender ID. Telnyx will apply destination‑specific rules and any approved registrations.
- API references: 
  - API v2 send message: https://developers.telnyx.com/api/messaging/send-message
  - Error codes: https://developers.telnyx.com/api/errors

For Alphanumeric registrations or questions, email alpha_sender_id@telnyx.com (include destination country/countries, estimated monthly volume, and a brief use‑case description). For other support, contact support@telnyx.com.

## Contacts and helpful links
- Forms and SCR registration questions: shortcode@telnyx.com
- Alphanumeric registration: alpha_sender_id@telnyx.com
- Telnyx Acceptable Use Policy: https://telnyx.com/acceptable-use-policy
- Submit a short code request in the Telnyx Portal: https://portal.telnyx.com/#/messaging-short-code
- Supported carriers list: https://support.telnyx.com/en/articles/4967485-short-code-supported-carriers
- Alphanumeric capabilities by country: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id
