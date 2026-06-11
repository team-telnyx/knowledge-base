---
title: Asia-Pacific SMS Guidelines
summary: Country-specific SMS guidelines for destinations across the Asia-Pacific
  region, covering sender ID requirements, registration procedures, content restrictions,
  and delivery considerations.
sources:
- url: https://support.telnyx.com/en/articles/6592456-angola-sms-guidelines
  content_hash: 69041587767ba2827e2959cabb72f8b0ef8ed9930ab3e8616315117e1dd3cfdf
- url: https://support.telnyx.com/en/articles/6600934-brunei-darussalam-sms-guidelines
  content_hash: 92c453f23399e0ca47b5ba12c0a48f3dbae60217388b62c1a9e50c7d06008a61
- url: https://support.telnyx.com/en/articles/6674367-hong-kong-sms-guidelines
  content_hash: f38d47da5d8595e8158722080bda790119852514f1ce2513b28297cae2301e5b
- url: https://support.telnyx.com/en/articles/6674476-japan-sms-guidelines
  content_hash: 51eeeee9bcd7a7ce49741f186438b1b0479c4066ea88978176cd3be06dd028af
- url: https://support.telnyx.com/en/articles/6679031-new-caledonia-sms-guidelines
  content_hash: 865f59db10b02b8045abd5103efbbf46dcd25a781d30aba7df1418154ba5363f
- url: https://support.telnyx.com/en/articles/6679036-new-zealand-sms-guidelines
  content_hash: 178422367dab89c14790ea0012fb376f57c844767451984cf9b3204e62614bea
- url: https://support.telnyx.com/en/articles/6679161-palau-sms-guidelines
  content_hash: d2bf99b10cedcd5bbd2e8e699cc4bc36a724d809e6899d50621b8e30a23064ac
- url: https://support.telnyx.com/en/articles/6680103-singapore-sms-guidelines
  content_hash: 8ad3383cd3baf2418f080d0eb5e7922880e71cff3e9f2ba7469632389693c22c
- url: https://support.telnyx.com/en/articles/6683277-taiwan-sms-guidelines
  content_hash: 1ba7197237ab0b9942de8eed3c482f53e4c00012ba3f9c4215f610e17344cedc
- url: https://support.telnyx.com/en/articles/6683302-thailand-sms-guidelines
  content_hash: 172fa22348203377f53724ba5b7121162138d25988dd255cef021424402831e0
- url: https://support.telnyx.com/en/articles/6683467-vietnam-sms-guidelines
  content_hash: 92f442dce2fb7d3e67e305edf90c49bdf593761c05e051a3ddb339b786089974
- url: https://support.telnyx.com/en/articles/6683726-kiribati-sms-guidelines
  content_hash: 81ba82ed302add12a0c9529f510812de7c7c7e02bed2a844831dc3c09972d964
- url: https://support.telnyx.com/en/articles/6683734-korea-sms-guidelines
  content_hash: 5bbd0ce1aef28051e52fa0fe7cd2ccde433c215e66d016eca0077d4154c78660
updated_at: 2026-06-11T11:22:38Z
---

# Asia-Pacific SMS Guidelines

Country-specific SMS guidelines for destinations across the Asia-Pacific region, covering sender ID requirements, registration procedures, content restrictions, and delivery considerations.

## Overview

This page consolidates SMS guidelines for Asia-Pacific destinations on the Telnyx platform. Each country has specific requirements for Alphanumeric Sender IDs, content restrictions, and delivery characteristics. Always refer to the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging) when sending traffic to any destination.

## Country Reference Table

| Country | MCC | Dial Code | Sender ID Policy |
|---|---|---|---|
| Angola | 631 | 244 | Supported, no registration required |
| Brunei Darussalam | 528 | 673 | Supported, no registration required |
| Hong Kong | 454 | 852 | Registration required |
| Japan | 440 | 81 | Supported, no registration required |
| Kiribati | 545 | 686 | Supported, no registration required |
| New Caledonia | 546 | 687 | Supported, no registration required |
| New Zealand | 530 | 64 | Overwritten to random short code |
| Palau | 552 | 680 | Supported, no registration required |
| Singapore | 525 | 65 | Mandatory registration (IMDA) |
| South Korea | 450 | 82 | Overwritten to random local long code |
| Taiwan | 466 | 886 | Overwritten to random local long code |
| Thailand | 520 | 66 | Registration required |
| Vietnam | 452 | 84 | Registration required |

## No Registration Required

The following destinations support Alphanumeric Sender IDs without registration. There are no content restrictions unless otherwise noted:

- **Angola** (MCC 631, +244)
- **Brunei Darussalam** (MCC 528, +673)
- **Kiribati** (MCC 545, +686)
- **New Caledonia** (MCC 546, +687)
- **Palau** (MCC 552, +680)

## Registration Required

### Hong Kong (MCC 454, +852)

Alphanumeric Sender ID registration is required. All messages from unregistered Sender IDs will be rejected.

To register, send the following details along with a copy of your Business Registration to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):

1. Sender ID to be registered
2. Message/content type
3. Message/content example
4. Company name (and brand name if different)
5. Website of brand or company
6. Company country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested Alphanumeric Sender ID. If the relationship between your company/brand and the requested Sender ID is not clear, provide additional supporting documentation.

**Additional recommendations:**
- Obtain consent (proof of opt-in) before sending marketing SMS
- Include clear opt-out options in traffic
- Handsets in Hong Kong commonly follow a "2 numbers, 1 SIM card" model (one Chinese number +86 and one HK number +852), which can cause delivery issues

### Singapore (MCC 525, +65)

Mandatory registration of Alphanumeric Sender IDs has been enforced by the Infocomm Media Development Authority (IMDA) since January 31, 2023. From that date until July 31, 2023, messages with unregistered Sender IDs were flagged and overwritten with "Likely-SCAM." After July 31, 2023, messages with unregistered Alphanumeric Sender IDs are blocked entirely.

Registration involves fees. Contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for more information.

**Content restrictions:** Religious, gambling, political, and adult traffic is prohibited.

### Thailand (MCC 520, +66)

Alphanumeric Sender IDs are supported but registration is required. Contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for registration details.

**Content restrictions:** Religious, gambling, political, and adult traffic is prohibited.

### Vietnam (MCC 452, +84)

Alphanumeric Sender ID registration is required. Generic Alpha Sender IDs are not recommended; Sender IDs should be directly related to the message content. Contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for registration details.

**Delivery note:** Vietnam supports SMSC-DLR only. Positive DLRs are expected, but handset delivery reports are not possible.

## Sender ID Overwritten

### New Zealand (MCC 530, +64)

All Alphanumeric Sender IDs are overwritten to a random short code to ensure delivery. Due to local restrictions, dedicated short codes are the best way to improve delivery. Without a dedicated short code, message delivery is best-effort only.

### South Korea (MCC 450, +82)

All Alphanumeric Sender IDs are overwritten to a random local long code to ensure delivery. The following text is added to all messages by default:

- **[Web 발신]** — indicates A2P traffic
- **[국제발신]** — indicates the message was sent from abroad

**Content restrictions:** Gambling and adult content is not permitted.

### Taiwan (MCC 466, +886)

All Alphanumeric Sender IDs are overwritten to a random local long code to ensure delivery.

## Other Country-Specific Notes

### Japan (MCC 440, +81)

Alphanumeric Sender IDs are supported with no registration required. However, SMS containing URLs in the message body may be filtered.

## General Recommendations

- Always comply with the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging)
- For Alphanumeric Sender ID registration inquiries, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com)
- For more on messaging products and compliance, see [SMS API](sms-api.md) and [MMS API](mms-api.md) documentation on the Telnyx site
