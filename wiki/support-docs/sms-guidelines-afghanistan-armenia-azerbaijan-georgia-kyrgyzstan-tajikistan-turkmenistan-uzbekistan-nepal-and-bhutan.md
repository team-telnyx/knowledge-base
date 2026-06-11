---
title: 'SMS Guidelines: Afghanistan, Armenia, Azerbaijan, Georgia, Kyrgyzstan, Tajikistan,
  Turkmenistan, Uzbekistan, Nepal, and Bhutan'
summary: A consolidated reference for sending SMS to 10 Asian markets, covering MCC
  and dialing codes, Alphanumeric Sender ID rules (registration, rejections, and overwriting
  behaviors), the Telnyx registration process, and universal best practices for consent,
  opt-out, and compliance.
sources:
- url: https://support.telnyx.com/en/articles/6592387-afghanistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6592510-armenia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596144-azerbaijan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670856-georgia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674794-kyrgyzstan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683287-tajikistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683390-turkmenistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683454-uzbekistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678903-nepal-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596425-bhutan-sms-guidelines
updated_at: 2026-05-21T08:27:01Z
---

# SMS Guidelines: Afghanistan, Armenia, Azerbaijan, Georgia, Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan, Nepal, and Bhutan

A consolidated reference for sending SMS to 10 Asian markets, covering MCC and dialing codes, Alphanumeric Sender ID rules (registration, rejections, and overwriting behaviors), the Telnyx registration process, and universal best practices for consent, opt-out, and compliance.

## Overview
Most destinations covered here require Alphanumeric Sender ID (alpha SID) registration before traffic will deliver reliably. Unregistered alpha SIDs may be rejected outright or overwritten to a generic alpha/numeric originator by local networks. Always ensure you have consent and provide clear opt-out instructions, and review Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging

## How to register an Alphanumeric Sender ID
To request alpha SID registration with Telnyx, email alpha_sender_id@telnyx.com with:
- Sender ID to be registered
- Message/content type and an example
- Company name (and brand name if different)
- Company/brand website
- Company country of origin
- Expected monthly volumes
- Email linked to your Telnyx account
- A copy of your Business Registration

Notes
- A valid business case is required. If the relationship between your brand and the requested alpha SID isn’t clear, include supporting documentation that explains the use case.

## Country-by-country requirements
### Afghanistan (MCC 412, Dial Code 93)
- Alpha SID registration required; messages from unregistered sender IDs will be rejected.

### Armenia (MCC 374, Dial Code 283)
- Alpha SIDs are supported with registration. Without registration, alpha SIDs may be overwritten to a generic alpha or rejected. Registration is advised.

### Azerbaijan (MCC 400, Dial Code 994)
- Alpha SID registration required.

### Georgia (MCC 282, Dial Code 995)
- Alpha SIDs are supported and maintained; no registration required.
- No content restrictions noted for this destination (still adhere to Telnyx AUP).

### Kyrgyzstan (MCC 437, Dial Code 996)
- Alpha SID registration required.

### Tajikistan (MCC 436, Dial Code 992)
- Alpha SID registration required; messages from unregistered sender IDs will be rejected.

### Turkmenistan (MCC 438, Dial Code 993)
- All alpha SIDs are overwritten to either a random long code or a generic alpha to ensure delivery.

### Uzbekistan (MCC 434, Dial Code 998)
- Alpha SID registration required. Occasionally, registered alpha SIDs may be overwritten to a random short code to ensure delivery. See short code overview: https://telnyx.com/products/sms-short-code

### Nepal (MCC 429, Dial Code 977)
- Alpha SIDs are supported.
- Network-specific: For Ncell (42902), alpha SIDs are only supported with registration. Without registration, alpha SIDs are overwritten to a generic alpha or may not deliver.
- Use of generic alpha SIDs is not recommended; the alpha should directly reflect the sender/brand related to the message content.

### Bhutan (MCC 402, Dial Code 975)
- Alpha SID registration required; messages from unregistered sender IDs will be rejected.

## Best practices and compliance
- Obtain explicit consent (proof of opt-in) before sending, especially for marketing traffic.
- Include clear opt-out instructions in messages.
- Keep alpha SIDs directly related to your brand and message content; avoid generic senders where discouraged.
- Plan lead time for registration and be prepared to provide business documentation and use-case details.
- Always adhere to Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
