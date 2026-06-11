---
title: Telnyx Messaging
summary: Telnyx Messaging provides APIs and infrastructure for sending and receiving
  SMS, MMS, and RCS messages globally. This page covers phone number configuration,
  messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international
  compliance, and RCS with AI integration.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
  content_hash: d98fde358c8bb0a6117412a2971da4898405065ec7c3650984ae9a6494d9dcd3
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
  content_hash: 192a65ec89e4ea6a7be165a7b17a5e44f6ecd3121b756cc292aebd63a50fee49
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
  content_hash: e691bcb40f682bbc7d1087d2755ac4c3680e9cf93520f97c0d86645ab7657ad4
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
  content_hash: 458a86b8e1297624173a766ba456ed0768c0cb62eb8d60575ce3367c8625c318
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
  content_hash: 362df72c3dbe5bdfb19da2c433895133466aa88bd4ab4737f7754ecf0892fa18
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
  content_hash: f170f09f5d980d0e492e300a0e07ce6b1591881c60d71f8f506f2a02ad2cc34b
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
  content_hash: 62bd8025784ec0901f20d6bc1597886e9df41722271dcc11c7b8d8a86d2c94a1
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration/index
  content_hash: c088661a2d1c9ce8faaf92b86e072d0951aa7bf6301ed3bc75f1825e75c5b505
- url: https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index
  content_hash: 33d60e88cce1298b6009415cd6dc5afb26a05430927e0b5e286cd9ec8770efaa
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
  content_hash: 6adf9a29c630ce93d9fd16b676d2d2df67db1a1772c5e97c9e33646f6597ec0f
updated_at: 2026-06-11T10:38:14Z
---

# Telnyx Messaging

*Part 4 of 5 — see also: [Part 1](telnyx-messaging-2--part-1.md), [Part 2](telnyx-messaging-2--part-2.md), [Part 3](telnyx-messaging-2--part-3.md), [Part 5](telnyx-messaging-2--part-5.md)*

Telnyx Messaging provides APIs and infrastructure for sending and receiving SMS, MMS, and RCS messages globally. This page covers phone number configuration, messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international compliance, and RCS with AI integration.

## International SMS Compliance

Sending SMS internationally requires compliance with country-specific regulations for sender IDs, opt-in consent, content restrictions, and registration. Regulations change frequently; always verify current requirements with Telnyx support before launching in a new country.

### Sender ID types by country

| Country | Alphanumeric ID | Long Code | Short Code | Toll-Free | Pre-Registration |
|---|---|---|---|---|---|
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

Alphanumeric sender IDs are **not supported** for US and Canadian destinations. Use 10DLC, toll-free, or short codes instead.

### Mandatory pre-registration

**🇮🇳 India — DLT Registration**: India requires Distributed Ledger Technology (DLT) registration for all A2P SMS. You must register as a business entity on a DLT platform (JioConnect, Vodafone, Airtel, or BSNL DLT), submit your sender ID ("header") for approval, create and submit message templates using `{#var#}` variable syntax, and provide Telnyx with your DLT Entity ID, headers, and template IDs. Message categories:

| Category | Allowed Hours | DND Filtering | Example |
|---|---|---|---|
| Transactional | 24/7 | Exempt | OTP, order confirmations |
| Service (Implicit) | 24/7 | Exempt | Account updates |
| Promotional | 9 AM–9 PM IST | Applies | Marketing, offers |

**🇫🇷 France — OACP Registration**: Requires sender ID registration with French carriers via Telnyx support. Provide business documentation (SIRET number for French businesses). Allow 5–10 business days. Commercial messages restricted to 8 AM–8 PM, no Sundays/holidays. Unregistered sender IDs may be silently filtered.

**🇦🇺 Australia — Sender ID Registration**: Alphanumeric sender IDs must be registered with carriers. Provide Australian Business Number (ABN). Typical approval: 3–5 business days.

**🇸🇬 Singapore — SSIR Registration**: Mandatory since January 2023. Unregistered alphanumeric IDs display as "Likely-SCAM". Register on the SSIR portal (sgnic.sg) and link to your Telnyx account.

### Opt-in requirements by region

**Europe (GDPR + ePrivacy)**: Explicit consent required (pre-checked boxes are not valid). Consent must specify message types. Users must be able to opt out as easily as opting in. Maintain records of when and how consent was obtained. Country variations: Germany requires double opt-in; France requires separate consent for marketing; Spain allows soft opt-in for existing customers; Italy requires clear separation of service and marketing consent.

**North America**: US follows TCPA + CTIA guidelines (express written consent for marketing, STOP keyword mandatory). Canada follows CASL (express or implied consent, unsubscribe mechanism required).

**Asia-Pacific**: India requires DLT + template approval + DND filtering. Australia requires express consent under Spam Act 2003. Singapore requires SSIR registration + PDPA consent + no SMS 9 PM–9 AM without consent. Japan requires sender identification and opt-out link. South Korea requires pre-approved templates and 080 opt-out number.

**Latin America**: Brazil requires LGPD consent, quiet hours 9 PM–9 AM, and opt-out. Mexico requires LFPDPPP consent and opt-out. Colombia recommends pre-registration. Argentina requires checking the National Do Not Call Registry.

### Content restrictions

Universally restricted or prohibited: cannabis/CBD (prohibited by carriers even where locally legal), gambling (heavily regulated), adult content (prohibited), phishing/fraud (immediate account termination), financial services (regulated), healthcare/pharma (regulated), political campaigns (varies by country, some ban entirely).

Country-specific restrictions include: UK (FCA approval for financial promotions, age verification for age-gated content); Germany (UWG strict consent, pharmaceutical advertising restrictions, double opt-in expected); France (Loi Hamon opt-out rights, no commercial SMS 8 PM–8 AM or Sundays/holidays, messages should be in French); India (promotional hours 9 AM–9 PM only, DND filtering, template matching); Brazil (LGPD compliance, quiet hours 9 PM–9 AM, messages should be in Portuguese).

### Country-by-country reference

| Country | Sender Types | Regulation | Pre-Registration | Opt-Out | Time Restrictions |
|---|---|---|---|---|---|
| 🇬🇧 UK | Alphanumeric (rec.), long code, short code | PECR + UK GDPR | Recommended | STOP keyword or link | Best practice: 8 AM–9 PM |
| 🇩🇪 Germany | Alphanumeric, long code | GDPR + UWG + TTDSG | Not required | STOP keyword or link (free) | Best practice: 8 AM–9 PM |
| 🇫🇷 France | Alphanumeric (OACP), long code, short code | GDPR + Code des postes | Required (OACP) | "STOP" at no cost | 8 AM–8 PM, no Sundays/holidays |
| 🇦🇺 Australia | Alphanumeric (reg.), long code, short code | Spam Act 2003 + Privacy Act 1988 | Required | Unsubscribe within 5 business days | Best practice: 9 AM–8 PM AEST |
| 🇮🇳 India | Alphanumeric only (6-char header) | TRAI + DLT | Mandatory (DLT) | Via DLT/DND registry | Promotional: 9 AM–9 PM IST |
| 🇧🇷 Brazil | Alphanumeric, long code, short code | LGPD + Consumer Code | Recommended | Easy mechanism required | 9 PM–9 AM quiet hours |
| 🇲🇽 Mexico | Alphanumeric, long code, short code | LFPDPPP | Not required | In privacy notice | None legally |

### International messaging best practices

1. Check country requirements before launch — requirements vary significantly and change frequently.
2. Use the right sender type — alphanumeric IDs are preferred in most international markets (except US/Canada).
3. Localize messages in the recipient's language — many countries require this for commercial messaging.
4. Respect time zones and quiet hours — sending during business hours reduces complaints.
5. Include opt-out instructions in every message, using locally appropriate language.
6. Maintain consent records — GDPR requires proof of consent; keep records at least 4 years.
7. Monitor delivery rates by country using MDRs — sudden drops may indicate registration issues or content filtering.

### Multi-country messaging

For platforms sending to multiple countries, implement country-aware routing with different sender IDs, messaging profiles, and configurations per destination. Use a country code lookup to select the appropriate `from` value and `messaging_profile_id` before sending each message.
