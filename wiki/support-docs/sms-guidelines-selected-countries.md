---
title: 'SMS Guidelines: Selected Countries'
summary: Consolidated Telnyx SMS sending guidelines for a set of countries where Alphanumeric
  Sender ID registration is required, including MCC, dial codes, registration requirements,
  content restrictions, and country-specific rules.
sources:
- url: https://support.telnyx.com/en/articles/6589557-iraq-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596144-azerbaijan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596227-belarus-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601042-burundi-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601133-chad-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670834-gabon-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674396-indonesia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674794-kyrgyzstan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679062-niger-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679084-nigeria-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680009-saudi-arabia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683287-tajikistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683454-uzbekistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683484-yemen-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683563-russian-federation-sms-guidelines
updated_at: 2026-08-05T13:37:03Z
---

# SMS Guidelines: Selected Countries

Consolidated Telnyx SMS sending guidelines for a set of countries where Alphanumeric Sender ID registration is required, including MCC, dial codes, registration requirements, content restrictions, and country-specific rules.

## Overview

This page consolidates Telnyx SMS sending guidelines for the following countries, all of which require Alphanumeric Sender ID registration before traffic can be delivered:

| Country | MCC | Dial Code |
| --- | --- | --- |
| Azerbaijan | 400 | 994 |
| Belarus | 257 | 375 |
| Burundi | 642 | 257 |
| Chad | 622 | 235 |
| Gabon | 628 | 241 |
| Indonesia | 510 | 62 |
| Iraq | 418 | 964 |
| Kyrgyzstan | 437 | 996 |
| Niger | 614 | 227 |
| Nigeria | 621 | 234 |
| Russian Federation | 250 | 7 |
| Saudi Arabia | 420 | 966 |
| Tajikistan | 436 | 992 |
| Uzbekistan | 434 | 998 |
| Yemen | 421 | 967 |

## General Registration Requirements

Across all of the countries listed above, Alphanumeric Sender ID registration is required. In most of these destinations, any message sent from an unregistered Sender ID will be rejected. The Russian Federation is a partial exception: unregistered Alpha Senders will be overwritten to a Generic Alpha Sender ID or will not deliver.

To register an Alphanumeric Sender ID, send the items below along with a copy of your Business Registration to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):

1. Sender ID to be registered
2. Message/Content type (for Saudi Arabia and the Russian Federation, specify Transactional, Promotional, or Notification)
3. Message/Content example(s)
4. Company name (and Brand name if different)
5. Website of brand or company
6. Company Country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested Alphanumeric Sender ID. If the relationship between your company or brand and the requested Sender ID is not clear, provide additional supporting documentation detailing your business case.

## Country-Specific Rules

### Azerbaijan, Belarus, Burundi, Chad, Gabon, Iraq, Niger, Tajikistan

These countries follow the standard registration flow above. In each case, all messages from unregistered Sender IDs will be rejected.

### Indonesia

Follows the standard registration flow. In addition, religious, gambling, political, or adult traffic is prohibited.

### Kyrgyzstan

Follows the standard registration flow. The source does not state that unregistered Sender IDs will be rejected, but registration is still required.

### Nigeria

Follows the standard registration flow. In addition:

- Religious, gambling, political, or adult traffic is prohibited.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

### Russian Federation

Follows the standard registration flow, with the following differences:

- Unregistered Alpha Senders will be overwritten to Generic Alpha Sender IDs or will not deliver.
- Each registered Sender ID carries a monthly recurring cost of $250.
- The standard opt-in and opt-out recommendations are not listed for this destination; only the Acceptable Use Policy reference is provided.

### Saudi Arabia

Saudi Arabia has a distinct registration process. Complete the operator-specific NOC templates (including signature, company letterhead, and stamp) and return them to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com), along with the standard registration information above. The following templates are available:

- [NOC_Template_KSA STC.docx](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/1073796842/308d5690074fc8fb94e2f15f/NOC_Template_KSA+STC.docx?expires=1783507500&signature=8355cfd98da30071c5db538108973bc39cc964d23d130a383f43689f13829241&req=dSAgFc53m4lbW%2FMW1HO4zdtYWo2JHv%2F%2BGq5XuAGUQx2IN3NkFBSRhxBPZoFJ%0Av%2BnwMsaeLDU%3D%0A)
- [NOC_Template_KSA Zain.docx](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/1073796960/f3c608e829ed1e141d9801f0/NOC_Template_KSA+Zain.docx?expires=1783507500&signature=655b971c58186ed720211935c32e22404202cab647c47d819767424d8d88634f&req=dSAgFc53m4hZWfMW1HO4za0KR56wHXRnapZ5oOYPSZE9b4Ie%2BT544zSmAzbX%0A%2BtJEx3VG1vg%3D%0A)

Additional Saudi Arabia rules:

- Registration is only possible for International Brands.
- For promotional traffic, the suffix "AD" must be added to the Alphanumeric Sender for traffic distinction.
- If message content includes URLs, those URLs must also be whitelisted as part of the Alphanumeric Sender ID registration process. Shortened URL links (bit links) are not allowed.
- Gambling, political, or adult traffic is prohibited.

### Uzbekistan

Follows the standard registration flow. Occasionally, an Alphanumeric Sender ID may be overwritten to a random [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

### Yemen

Follows the standard registration flow. All messages from unregistered Sender IDs will be rejected. Occasionally, registered Alphanumeric Sender IDs may be overwritten to a random [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## General Recommendations

For all destinations on this page (except where noted above):

- Obtain consent (proof of opt-in) before sending any communications, including marketing SMS.
- Include clear opt-out options in your traffic.
- Refer to the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md) for full messaging policy details.
- For more information on Alpha Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Related Country Guidelines

- [Norway: SMS Guidelines](norway-sms-guidelines.md)
- [Iraq: SMS Guidelines](iraq-sms-guidelines.md)
- [Azerbaijan: SMS Guidelines](azerbaijan-sms-guidelines.md)
- [Belarus: SMS Guidelines](belarus-sms-guidelines.md)
- [Burundi: SMS Guidelines](burundi-sms-guidelines.md)
- [Chad: SMS Guidelines](chad-sms-guidelines.md)
- [Gabon: SMS Guidelines](gabon-sms-guidelines.md)
- [Indonesia: SMS Guidelines](indonesia-sms-guidelines.md)
- [Kyrgyzstan: SMS Guidelines](kyrgyzstan-sms-guidelines.md)
- [Niger: SMS Guidelines](niger-sms-guidelines.md)
- [Nigeria: SMS Guidelines](nigeria-sms-guidelines.md)
- [Russian Federation: SMS Guidelines](russian-federation-sms-guidelines.md)
- [Saudi Arabia: SMS Guidelines](saudi-arabia-sms-guidelines.md)
- [Tajikistan: SMS Guidelines](tajikistan-sms-guidelines.md)
- [Uzbekistan: SMS Guidelines](uzbekistan-sms-guidelines.md)
- [Yemen: SMS Guidelines](yemen-sms-guidelines.md)
- [Palestinian Territory: SMS Guidelines](palestinian-territory-sms-guidelines.md)
- [Pakistan: SMS Guidelines](pakistan-sms-guidelines.md)
- [Jordan: SMS Guidelines](jordan-sms-guidelines.md)
- [Kuwait: SMS Guidelines](kuwait-sms-guidelines.md)
- [Malawi: SMS Guidelines](malawi-sms-guidelines.md)
- [Tunisia: SMS Guidelines](tunisia-sms-guidelines.md)
- [Greece: SMS Guidelines](greece-sms-guidelines.md)
- [Turkey: SMS Guidelines](turkey-sms-guidelines.md)
- [Hong Kong: SMS Guidelines](hong-kong-sms-guidelines.md)
- [Algeria: SMS Guidelines](algeria-sms-guidelines.md)
- [Comoros: SMS Guidelines](comoros-sms-guidelines.md)
- [Rwanda: SMS Guidelines](rwanda-sms-guidelines.md)
- [Syria: SMS Guidelines](syria-sms-guidelines.md)
