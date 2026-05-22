---
title: 'SMS Guidelines: Afghanistan, Armenia, Azerbaijan, Georgia, Kyrgyzstan, Tajikistan,
  Turkmenistan, Uzbekistan, Nepal, and Bhutan'
summary: A consolidated reference for sending SMS to 10 Asian markets, covering MCC
  and dialing codes, Alphanumeric Sender ID rules (registration, rejections, and overwriting
  behaviors), the Telnyx registration process, and universal best practices for consent,
  opt-out, and compliance.
sources:
- url: https://support.telnyx.com/en/articles/6592387-afghanistan-sms-guidelines
  content_hash: a14457507030f58de13a90690ea57e908adfd98df7a9bae788e8a0fb0c3d1081
- url: https://support.telnyx.com/en/articles/6592510-armenia-sms-guidelines
  content_hash: 7caecaceeae8fded104b17d37a9a1386eec76dcc7b3013150de79db3134e1325
- url: https://support.telnyx.com/en/articles/6596144-azerbaijan-sms-guidelines
  content_hash: 6987a2bebc377883a7ca54de88ae6121dbcfba8c1aeed3ce9843f876d545f95b
- url: https://support.telnyx.com/en/articles/6670856-georgia-sms-guidelines
  content_hash: ccf7f20146aab1d2b99282fc5aeb3e16d22b1a6c7779b21aeb7684d3c7d19514
- url: https://support.telnyx.com/en/articles/6674794-kyrgyzstan-sms-guidelines
  content_hash: 8c1f8738a35226575467eeff4974edffc6e835792a1e4d3f0bd6025109b4c657
- url: https://support.telnyx.com/en/articles/6683287-tajikistan-sms-guidelines
  content_hash: 0eef699b99cc4aecbe1a6f0f481adb9159311ca75872b508c0051e13fdda85e6
- url: https://support.telnyx.com/en/articles/6683390-turkmenistan-sms-guidelines
  content_hash: 967c1f046e2ea4bdea6166dc7a3e696419b9dfe75d1196f33ccfe52bd149c42a
- url: https://support.telnyx.com/en/articles/6683454-uzbekistan-sms-guidelines
  content_hash: 8b02540a2054db00c54eb7f7cf3be2df52ed28c755ce17417af236455f6e0936
- url: https://support.telnyx.com/en/articles/6678903-nepal-sms-guidelines
  content_hash: bb5551b5737fab4da32a77fcffb240c9cf1496593cd1d8cd32c8e9ef7262edb6
- url: https://support.telnyx.com/en/articles/6596425-bhutan-sms-guidelines
  content_hash: 41541576949f0ed3c9a5bed84476a6a0137bb3eb2bbb2c292ab08a9dc0a3d5cb
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
