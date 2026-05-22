---
title: 'Central & Eastern Europe: SMS Guidelines'
summary: Consolidated Telnyx SMS delivery rules for Bosnia and Herzegovina, Belarus,
  Cyprus, Czechia, Hungary, Moldova, Poland, Romania, Russia, Slovakia, Turkey, and
  Ukraine, including MCC/dial codes, alphanumeric Sender ID support and registration,
  operator overwrites, content restrictions, and special procedures.
sources:
- url: https://support.telnyx.com/en/articles/6561206-hungary-sms-guidelines
  content_hash: 159f30c2dfad393eb96a2ac83591d05c3c7c1e33051f9f28b6d7b673c4fb50d1
- url: https://support.telnyx.com/en/articles/6561237-czech-republic-czechia-sms-guidelines
  content_hash: cb1b4a016d99f271dc25b8478a9b48c87773706825928d3460df262d84167fcf
- url: https://support.telnyx.com/en/articles/6561262-romania-sms-guidelines
  content_hash: a5c652507fa644d0e3916abfe1a3059ea42d6ee6ca5c90353ae0bde4757f7862
- url: https://support.telnyx.com/en/articles/6680109-slovakia-sms-guidelines
  content_hash: a98d9439134eaaa15b9fd1dff0c8921ae0d74e27fe89bf3ae0e3a4d244391797
- url: https://support.telnyx.com/en/articles/6545167-poland-sms-guidelines
  content_hash: a62cb1d03e40292439d3b86f6166cd65bc5c39fb0997b4acbf82fb6ef9eb51cb
- url: https://support.telnyx.com/en/articles/6563904-ukraine-sms-guidelines
  content_hash: fa0daad1fc649cf35dedf4b4e0f3b8ef926e3c59a9f46dcbde8fd55bbffebf43
- url: https://support.telnyx.com/en/articles/6564053-moldova-sms-guidelines
  content_hash: 090cbe9e8fff632b39ab198fee215d0d5349630106e1bdd1576b2dd018679d33
- url: https://support.telnyx.com/en/articles/6596227-belarus-sms-guidelines
  content_hash: 5bf7e2bd7c2a13c489642c40c98b41ba7101b90b5c2099f5ceced8a26e33bcd6
- url: https://support.telnyx.com/en/articles/6683563-russian-federation-sms-guidelines
  content_hash: 8034070eed053f6fbb950fd4f315f97df1ddb87538fdebb05f7aaf22414f5340
- url: https://support.telnyx.com/en/articles/6596434-bosnia-and-herzegovina-sms-guidelines
  content_hash: 5b07b15d990fb88a1cda754863a3caf1564d390962310be6411b59fc93bf7e4c
- url: https://support.telnyx.com/en/articles/6665171-cyprus-sms-guidelines
  content_hash: a68a4fcf5e36914bc22af0096c286da76c3bbb61ae119235c1bf89623f6825e3
- url: https://support.telnyx.com/en/articles/6564056-turkey-sms-guidelines
  content_hash: b0387149bc4e8e3f8e9032e3336fc46b5e0e95badbe3f55d71a9afd3b2226e9a
updated_at: 2026-05-21T08:15:31Z
---

# Central & Eastern Europe: SMS Guidelines

Consolidated Telnyx SMS delivery rules for Bosnia and Herzegovina, Belarus, Cyprus, Czechia, Hungary, Moldova, Poland, Romania, Russia, Slovakia, Turkey, and Ukraine, including MCC/dial codes, alphanumeric Sender ID support and registration, operator overwrites, content restrictions, and special procedures.

## Overview and scope
This page summarizes current Telnyx SMS requirements and behaviors across the following destinations: Bosnia and Herzegovina, Belarus, Cyprus, Czech Republic (Czechia), Hungary, Moldova, Poland, Romania, Russian Federation, Slovakia, Turkey, and Ukraine. Always ensure your use complies with Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging.

## General requirements and best practices
- Obtain prior consent (opt-in) and provide clear opt-out instructions where applicable, especially for marketing.
- Use brand-aligned alphanumeric Sender IDs; avoid “generic” Sender IDs in markets that discourage them (e.g., Poland, Ukraine).
- Expect operator-enforced changes when registration isn’t supported or completed: Sender IDs may be overwritten to a local long code, short code, or a generic alpha to ensure delivery.
- Be aware of content filtering. For example, URLs in Romania may be blocked unless whitelisted (see country details below).

## Sender ID registration: common submission package
Where alphanumeric Sender ID registration is required or offered, you’ll generally need to email alpha_sender_id@telnyx.com with:
1) Sender ID to be registered
2) Message/content type (Transactional/Promotional/Notification)
3) Message/content example(s)
4) Company name (and Brand name if different)
5) Website of brand or company
6) Company country of origin
7) Expected monthly volumes
8) Email linked to your Telnyx account
+ A copy of your Business Registration

Notes:
- Russia: Monthly recurring cost of $250 per registered Sender ID.
- Turkey: A country-specific form is required; see the Turkey section for the link.
- Some markets do not accept registrations (e.g., Ukraine), while others do not require them (e.g., Poland, Slovakia, Moldova, Bosnia and Herzegovina, Cyprus).

## Country-by-country details
### Bosnia and Herzegovina (MCC 218, Dial Code 387)
- Alphanumeric Sender IDs supported and maintained; no registration required.
- No specific content restrictions noted.

### Belarus (MCC 257, Dial Code 375)
- Alphanumeric Sender ID registration is required; unregistered Sender IDs will be rejected.
- Provide the standard registration package (see above) and a clear business case aligning the brand and Sender ID.
- Recommendations: obtain opt-in and include clear opt-out in messaging.

### Cyprus (MCC 357, Dial Code 280)
- Alphanumeric Sender IDs supported and maintained; no registration required.
- No specific content restrictions noted.

### Czech Republic (Czechia) (MCC 230, Dial Code 420)
- Alphanumeric Sender IDs are partially supported.
- Registration is possible toward T‑Mobile (23001) and O2 (23002).
- Without registration, alphanumeric Sender IDs may be overwritten to a random short code or a generic sender to ensure delivery.
- For registration guidance, contact alpha_sender_id@telnyx.com.

### Hungary (MCC 216, Dial Code 36)
- All alphanumeric Sender IDs are overwritten to a random local long code or short code to ensure delivery (registration not available).

### Moldova (MCC 259, Dial Code 373)
- Alphanumeric Sender IDs supported and maintained; no registration required.
- No specific content restrictions noted.

### Poland (MCC 260, Dial Code 48)
- Alphanumeric Sender IDs supported and maintained; no registration required.
- Avoid generic alphanumeric Sender IDs; use brand-related Sender IDs.
- No specific content restrictions noted.

### Romania (MCC 226, Dial Code 40)
- Alphanumeric Sender IDs are partially supported.
- Maintained toward Telekom (22603) and Lycamobile (22616).
- Overwritten to a random short code toward Vodafone (22601), Orange (22610), and DigiMobil (22605).
- Messages containing URLs may be blocked; URL whitelisting is possible—contact alpha_sender_id@telnyx.com.

### Russian Federation (MCC 250, Dial Code 7)
- Alphanumeric Sender IDs supported with registration; registration is required.
- Without registration, Sender IDs may be overwritten to a generic alpha or may not deliver.
- Monthly recurring cost: $250 per Sender ID. Submit the standard registration package to alpha_sender_id@telnyx.com.

### Slovakia (MCC 231, Dial Code 421)
- Alphanumeric Sender IDs supported and maintained; no registration required.
- No specific content restrictions noted.

### Turkey (MCC 286, Dial Code 90)
- Alphanumeric Sender IDs supported with registration; registration is required.
- A 4‑character code beginning with “B” is appended at the end of the message content by the terminating operator per ICTA guidelines.
- Gambling traffic is prohibited.
- Submit the standard registration package and complete the Turkey-specific form: https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/ltcafuzd/2398133417/cb58fd0192712828878b2de2f88b/Turkey+SIDreg.doc
- Contact: alpha_sender_id@telnyx.com.

### Ukraine (MCC 255, Dial Code 380)
- Due to the ongoing situation, SMS delivery is best-effort.
- Alphanumeric Sender IDs are partially supported; registration is not possible.
- Alphanumeric Sender IDs may occasionally be overwritten to a random short code to ensure delivery.
- Avoid generic Sender IDs; use brand-aligned IDs related to message content.
