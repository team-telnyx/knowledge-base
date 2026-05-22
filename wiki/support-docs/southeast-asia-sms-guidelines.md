---
title: 'Southeast Asia: SMS Guidelines'
summary: A consolidated view of Telnyx SMS requirements and best practices across
  Southeast Asia, including MCC/dial codes, Sender ID registration rules, content
  and formatting restrictions, URL policies, delivery-report nuances, and country-by-country
  specifics—plus where to register and get help.
sources:
- url: https://support.telnyx.com/en/articles/6531682-philippines-sms-guidelines
  content_hash: f7732c379c2f60ff3d7ac5863ba2e613bacb13e8d8839317e79d013102b00d17
- url: https://support.telnyx.com/en/articles/6600934-brunei-darussalam-sms-guidelines
  content_hash: d4652aabdb19e043e9907e9f04e9184552c60eb8a8839378436c4e0c8875597d
- url: https://support.telnyx.com/en/articles/6601049-cambodia-sms-guidelines
  content_hash: b04ba61a2ae523897a47e363cd5602db0cf3703a056cb5ca6e9d1019b212def2
- url: https://support.telnyx.com/en/articles/6674396-indonesia-sms-guidelines
  content_hash: d25f8a4225aa60bc4dc69566ad31a0b781d58e28c6e6ef4c31ca8564b682b460
- url: https://support.telnyx.com/en/articles/6674798-laos-pdr-sms-guidelines
  content_hash: 51fff84c0b07599c1eef3cb39141d07ad8b26deb61aa71763338bec4c5b68e98
- url: https://support.telnyx.com/en/articles/6675110-malaysia-sms-guidelines
  content_hash: 53b207176a76fa93aa319168f9bb2b0692059dcafe84f35217f1fb8d98aa0269
- url: https://support.telnyx.com/en/articles/6678010-myanmar-sms-guidelines
  content_hash: b7307cb717181021a0fc0f2639a11453e489bee23586f0b3506b7a8ebe82532d
- url: https://support.telnyx.com/en/articles/6680103-singapore-sms-guidelines
  content_hash: a78d4f5ba63b491828f842fd70b4ec9d504687c8790e333ba3c4fff8ae7c9dd1
- url: https://support.telnyx.com/en/articles/6683302-thailand-sms-guidelines
  content_hash: fd5b304944e8510ac7c7162b5f46b43affc8bd65765bf15bfd5e5804b714ab0a
- url: https://support.telnyx.com/en/articles/6683340-timor-leste-sms-guidelines
  content_hash: b79deada38dfb851e220f54cbe48a8caef936cdfeb414dd7a94751dee91c83a1
- url: https://support.telnyx.com/en/articles/6683467-vietnam-sms-guidelines
  content_hash: a5bf1f9dfbe3a95bb7926ffc0730c35157f11eba68ee6632dea5839c86fe0d29
updated_at: 2026-05-21T08:28:27Z
---

# Southeast Asia: SMS Guidelines

A consolidated view of Telnyx SMS requirements and best practices across Southeast Asia, including MCC/dial codes, Sender ID registration rules, content and formatting restrictions, URL policies, delivery-report nuances, and country-by-country specifics—plus where to register and get help.

## Regional overview and best practices
- Alphanumeric Sender ID registration is mandated in several markets (Indonesia, Myanmar, Singapore, Thailand, Vietnam, Philippines). Others support Alphanumeric Sender IDs without registration (Brunei Darussalam, Cambodia, Laos PDR, Timor-Leste — though some networks may still overwrite for delivery).
- Avoid generic Alpha Sender IDs like “Verify,” “OTP,” or “InfoSMS.” These are disallowed in the Philippines and discouraged in Vietnam; use a brand-aligned Sender ID.
- Content restrictions commonly include prohibitions on religious, gambling, political, or adult content (explicitly noted for Indonesia, Singapore, and Thailand).
- Consent and opt-out: Obtain proof of opt-in and provide a clear opt-out, especially for marketing SMS (recommended in Indonesia and Myanmar).
- URL policies vary by country:
  - Malaysia: any message containing a URL will be blocked.
  - Philippines: use branded URLs; avoid public URL shorteners due to spam/phishing risks.
- Sender ID overwriting can occur:
  - Malaysia: all Alphanumeric Sender IDs are overwritten to Short Code.
  - Timor-Leste: Alphanumeric Sender IDs may occasionally be overwritten to a random Short Code.
  - Philippines: local operators may overwrite even registered Alpha Sender IDs to optimize delivery.
- Delivery receipts: Vietnam supports SMSC-DLR only; handset delivery reports are not available.
- Always review Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging

## Sender ID registration package and contacts
- Where registration is required (e.g., Indonesia, Myanmar, Singapore, Thailand, Vietnam, Philippines), submit the following to alpha_sender_id@telnyx.com along with a copy of your Business Registration:
  1) Sender ID to be registered
  2) Message/content type
  3) Message/content example
  4) Company name (and Brand name if different)
  5) Website of brand or company
  6) Company country of origin
  7) Expected volumes per month
  8) Email linked to your Telnyx account
- Ensure a clear, valid business case tying your brand/company to the requested Sender ID; provide supporting documentation if the linkage is not obvious.
- Notes:
  - Singapore: IMDA mandates Alphanumeric Sender ID registration; unregistered traffic is blocked. Registration involves fees. See Alphanumeric Sender ID overview: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id

## Country-specific requirements
### Brunei Darussalam
- MCC: 528 | Dial Code: 673
- Alphanumeric Sender IDs supported and maintained; no registration required.
- No stated content restrictions to this destination.

### Cambodia
- MCC: 456 | Dial Code: 855
- Alphanumeric Sender IDs supported and maintained; no registration required.
- No stated content restrictions to this destination.

### Indonesia
- MCC: 510 | Dial Code: 62
- Alphanumeric Sender ID registration required; unregistered messages are rejected.
- Registration package and business-case proof required (see “Sender ID registration package and contacts”).
- Recommendations: obtain opt-in consent; include clear opt-out.
- Content restrictions: religious, gambling, political, or adult traffic is prohibited.

### Laos PDR
- MCC: 457 | Dial Code: 856
- Alphanumeric Sender IDs supported and maintained; no registration required.
- No stated content restrictions to this destination.

### Malaysia
- MCC: 502 | Dial Code: 60
- All Alphanumeric Sender IDs are overwritten to Short Code to ensure delivery.
- Required content header: start the message with “RM0.00 ,” “RM0.0 ,” or “RM0 ”. If omitted, operators will add it, which can affect message length.
- Include a brand/identifier or company name; missing identifiers may lead to filtering or fines.
- URLs: any message containing a URL in the body will be blocked.

### Myanmar
- MCC: 414 | Dial Code: 95
- Alphanumeric Sender ID registration required; unregistered messages are rejected.
- Registration package and business-case proof required (see “Sender ID registration package and contacts”).
- Recommendations: obtain opt-in consent; include clear opt-out.

### Philippines
- MCC: 515 | Dial Code: 63
- Alphanumeric Sender IDs must be pre-registered; a Letter of Authorization (LOA) is required for banking/financial institutions.
- Operators may overwrite Alpha Sender IDs (even when registered) to optimize delivery.
- Generic Alpha Sender IDs (e.g., Verify, OTP, InfoSMS) for transactional traffic are not allowed; submissions may be rejected.
- URL guidance: use branded URLs; avoid public URL shorteners due to spam/phishing risks.

### Singapore
- MCC: 525 | Dial Code: 65
- IMDA mandates Alphanumeric Sender ID registration; unregistered traffic is blocked (previously labeled “Likely-SCAM”). Registration involves fees.
- Content restrictions: religious, gambling, political, or adult traffic is prohibited.

### Thailand
- MCC: 520 | Dial Code: 66
- Alphanumeric Sender IDs are supported with registration; registration is required.
- Content restrictions: religious, gambling, political, or adult traffic is prohibited.

### Timor-Leste
- MCC: 514 | Dial Code: 670
- Alphanumeric Sender IDs supported; no registration required.
- Sender IDs may occasionally be overwritten to a random Short Code to ensure delivery.

### Vietnam
- MCC: 452 | Dial Code: 84
- Alphanumeric Sender IDs supported with registration; registration is required.
- Avoid generic Alpha Sender IDs; the Sender ID should be directly related to the message content.
- Delivery receipts: SMSC-DLR only; handset delivery reports are not available.
