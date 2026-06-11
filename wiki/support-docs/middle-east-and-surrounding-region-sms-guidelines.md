---
title: 'Middle East and Surrounding Region: SMS Guidelines'
summary: SMS guidelines for countries in the Middle East and surrounding region, covering
  MCC, dial codes, Alphanumeric Sender ID registration requirements, content restrictions,
  and additional compliance recommendations for each destination.
sources:
- url: https://support.telnyx.com/en/articles/6589557-iraq-sms-guidelines
  content_hash: 99c62d1053f011d5f4e60ef7cfedde6c0994e8dfeb0c647c45b04dddcea53c45
- url: https://support.telnyx.com/en/articles/6596158-bahrain-sms-guidelines
  content_hash: eed49dcb4a1a7250be774225378cd4b947d0ad3b7d2a948eaec943cee6742283
- url: https://support.telnyx.com/en/articles/6674403-iran-sms-guidelines
  content_hash: 74b5ef3a228ade918838e981f7b794fc5a5d55189beef72c5f07827d0f5b9d32
- url: https://support.telnyx.com/en/articles/6674487-jordan-sms-guidelines
  content_hash: 9eca7826cf740b827c8d6f52b23658054feb35392b97b529955d3f6332c4471e
- url: https://support.telnyx.com/en/articles/6674713-kuwait-sms-guidelines
  content_hash: b33bb229867467675167d252f705e34a476e21e28fb7a1040ac5eeb0397bd186
- url: https://support.telnyx.com/en/articles/6679138-oman-sms-guidelines
  content_hash: c78cd5248eda7c01da1afa7518cc3d3fc3837b4f0fdaa833038161b646310eba
- url: https://support.telnyx.com/en/articles/6679149-pakistan-sms-guidelines
  content_hash: a058a73d6427fce99799eec9045b311809907201725d1211b28447eb50ed5a46
- url: https://support.telnyx.com/en/articles/6679259-palestinian-territory-sms-guidelines
  content_hash: 74666bfe7accc3a1b3a8662beedde03a902b3b424ce07130aff9b06fe449a7d9
- url: https://support.telnyx.com/en/articles/6679369-qatar-sms-guidelines
  content_hash: 1cb8a6b8c2be0096e00aa216c527b84c005c5ee3036baf9a69ecfc25b169ec2f
- url: https://support.telnyx.com/en/articles/6680009-saudi-arabia-sms-guidelines
  content_hash: 763d4fc90e458b7380e07156c3ce195f549424c88de615d652afcb3db23a0f5f
- url: https://support.telnyx.com/en/articles/6680256-syria-sms-guidelines
  content_hash: 43fd3aa8801149020f5d642e3b26c2775a59c04f8f9d779774d76c29c2c26950
- url: https://support.telnyx.com/en/articles/6683390-turkmenistan-sms-guidelines
  content_hash: 59dcb33ac7dfb229b3b2a73dfa42a08991f8ffc1cd56e1b7b2642d750764aa36
- url: https://support.telnyx.com/en/articles/6683438-united-arab-emirates-sms-guidelines
  content_hash: 0c44e9a1728c953724cb51ab578031bf28feaa5c75d8547cb52a95413d46fe25
- url: https://support.telnyx.com/en/articles/6683484-yemen-sms-guidelines
  content_hash: bba57281930328ab395e671ce9961f3345666eae66d703de780a33c622f4b1ad
updated_at: 2026-06-11T11:21:39Z
---

# Middle East and Surrounding Region: SMS Guidelines

SMS guidelines for countries in the Middle East and surrounding region, covering MCC, dial codes, Alphanumeric Sender ID registration requirements, content restrictions, and additional compliance recommendations for each destination.

## Quick Reference

| Country | MCC | Dial Code | Alpha Sender ID Requirement |
|---|---|---|---|
| Bahrain | 426 | 973 | Supported, no registration required |
| Iran | 432 | 98 | Partially supported (network-dependent) |
| Iraq | 418 | 964 | Registration required |
| Jordan | 416 | 962 | Registration required |
| Kuwait | 419 | 965 | Registration required |
| Oman | 422 | 968 | Registration required |
| Pakistan | 410 | 92 | Registration required |
| Palestinian Territory | 425 | 970 | Registration required |
| Qatar | 427 | 974 | Registration required |
| Saudi Arabia | 420 | 966 | Registration required |
| Syria | 417 | 963 | Registration required |
| Turkmenistan | 438 | 993 | Overwritten (not supported) |
| United Arab Emirates | 424 | 971 | Registration required |
| Yemen | 421 | 967 | Registration required |

## Alphanumeric Sender ID Registration

### Standard Registration Process

For **Iraq, Jordan, Kuwait, Pakistan, Palestinian Territory, Syria, and Yemen**, Alphanumeric Sender ID registration is mandatory. Messages from unregistered Sender IDs will be rejected. To register, send the following information along with a copy of your Business Registration to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):

1. Sender ID to be registered
2. Message/Content type
3. Message/Content example
4. Company name (and Brand name if different)
5. Website of brand or company
6. Company Country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested Alphanumeric Sender ID. If the relationship between your company/brand and the requested Sender ID is not clear, provide additional supporting documentation detailing your business case.

### Enhanced Registration Process

**Saudi Arabia** and the **United Arab Emirates** require a more detailed registration. In addition to the standard information listed above, you must complete and submit a carrier-specific registration form (including signature, company letterhead, and stamp) along with a copy of your Business Registration or Certificate of Incorporation. For Saudi Arabia, the message/content type should specify Transactional, Promotional, or Notification.

- Saudi Arabia: NOC templates are available for KSA STC and KSA Zain
- UAE: A dedicated SID registration form must be completed

### Registration Without Detailed Process Specified

**Oman** and **Qatar** require Alphanumeric Sender ID registration, but specific form requirements are not detailed. Contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) to initiate registration.

### Countries Without Registration

- **Bahrain**: Alphanumeric Sender IDs are supported without registration
- **Turkmenistan**: All Alphanumeric Sender IDs are overwritten to a random long code or generic alphanumeric Sender ID; registration is not applicable
- **Iran**: See network-specific rules below

## Country-Specific Requirements

### Bahrain

Adult, political, and religious content will be blocked by local operators.

### Iran

Alphanumeric Sender ID support varies by network:

- **Righttel (43220)**: Alphanumeric Sender IDs are supported and maintained
- **MCI (43211)**: Alphanumeric Sender ID registration is required
- **All other networks**: Alphanumeric Sender IDs will be overwritten to a random long code to ensure delivery

The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

### Jordan

- Consent (Proof for Opt-in) should be obtained before sending any communications (e.g., Marketing SMS)
- Traffic should include clear Opt-Out options
- Promotional traffic can only be sent between 7:00 AM and 9:00 PM local time
- Alphanumeric Senders used for promotional traffic must include the prefix **"ADV"**

### Kuwait

- Consent (Proof for Opt-in) should be obtained before sending any communications (e.g., Marketing SMS)
- Traffic should include clear Opt-Out options
- Adult, religious, and political content is not permitted

### Oman

Non-registered Alpha Sender IDs will either be rejected or overwritten on a best-effort basis. The use of generic Alpha Sender IDs is not recommended; Alpha Senders should be directly related to the message content.

### Pakistan

- Consent (Proof for Opt-in) should be obtained before sending any communications (e.g., Marketing SMS)
- Traffic should include clear Opt-Out options
- Gambling-related traffic is not permitted

### Palestinian Territory

- Consent (Proof for Opt-in) should be obtained before sending any communications (e.g., Marketing SMS)
- Traffic should include clear Opt-Out options
- Personal loans, gambling, adult, and cryptocurrency-related traffic is prohibited

### Qatar

- Religious, political, or adult traffic is prohibited
- The use of generic Alpha Sender IDs is not recommended; Alpha Senders should be directly related to the message content

### Saudi Arabia

- Registration is only possible for International Brands
- For promotional traffic, the suffix **"AD"** must be added to the Alphanumeric Sender for traffic distinction
- If message content includes URLs, these must also be whitelisted as part of the Alphanumeric Sender ID registration process
- The use of shortened URL links (bit links) is not allowed
- Gambling, political, or adult traffic is prohibited

### Syria

- Consent (Proof for Opt-in) should be obtained before sending any communications (e.g., Marketing SMS)
- Traffic should include clear Opt-Out options

### United Arab Emirates

- For promotional traffic, the suffix **"AD"** must be added to the Alphanumeric Sender for traffic distinction
- Promotional traffic is not allowed between 9:00 PM and 7:00 AM local time; traffic submitted during this window will be queued and delivery attempted outside the restricted period
- Religious, gambling, political, or adult traffic is prohibited
- The use of generic Alpha Sender IDs is not recommended; Alpha Senders should be directly related to the message content

### Yemen

- Consent (Proof for Opt-in) should be obtained before sending any communications (e.g., Marketing SMS)
- Traffic should include clear Opt-Out options
- Occasionally, registered Alphanumeric Sender IDs might be overwritten to a random short code to ensure delivery

## Prohibited Content Summary

| Country | Adult | Political | Religious | Gambling | Other Restrictions |
|---|---|---|---|---|---|
| Bahrain | Blocked | Blocked | Blocked | — | — |
| Kuwait | Prohibited | Prohibited | Prohibited | — | — |
| Pakistan | — | — | — | Prohibited | — |
| Palestinian Territory | Prohibited | — | — | Prohibited | Personal loans, cryptocurrency |
| Qatar | Prohibited | Prohibited | Prohibited | — | — |
| Saudi Arabia | Prohibited | Prohibited | — | Prohibited | — |
| UAE | Prohibited | Prohibited | Prohibited | Prohibited | — |

## General Recommendations

Always refer to the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md) when sending SMS traffic to any destination. For questions about Alphanumeric Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).
