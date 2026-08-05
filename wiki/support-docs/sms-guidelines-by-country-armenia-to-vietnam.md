---
title: SMS Guidelines by Country - Armenia to Vietnam
summary: Telnyx SMS sending guidelines for 15 countries, covering MCC, dial codes,
  alphanumeric sender ID support, registration requirements, network-specific rules,
  and content restrictions.
sources:
- url: https://support.telnyx.com/en/articles/6592510-armenia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601061-cameroon-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601144-china-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670411-egypt-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670870-ghana-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674383-india-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674403-iran-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674476-japan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674630-kenya-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678903-nepal-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679138-oman-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680141-south-sudan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680225-sudan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683277-taiwan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683467-vietnam-sms-guidelines
updated_at: 2026-08-05T13:37:12Z
---

# SMS Guidelines by Country - Armenia to Vietnam

Telnyx SMS sending guidelines for 15 countries, covering MCC, dial codes, alphanumeric sender ID support, registration requirements, network-specific rules, and content restrictions.

## Overview

This page consolidates Telnyx SMS sending guidelines for the following countries: Armenia, Cameroon, China, Egypt, Ghana, India, Iran, Japan, Kenya, Nepal, Oman, South Sudan, Sudan, Taiwan, and Vietnam. Each country entry lists the Mobile Country Code (MCC), international dial code, alphanumeric sender ID support, registration requirements, and any network-specific or content restrictions.

For all destinations, senders must comply with the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md). For Alpha Sender ID registration or content whitelisting inquiries, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Country Guidelines

### Armenia
- **MCC:** 374
- **Dial Code:** 283
- Alphanumeric Sender IDs are supported with registration. Alpha Sender ID registration is required.
- Without registration, Alpha Sender IDs will be overwritten to a generic Alpha Sender ID, or rejected. Alpha Sender ID registration is advised.

### Cameroon
- **MCC:** 624
- **Dial Code:** 237
- Alphanumeric Sender IDs are supported.
- For Network MTN (62401), Alphanumeric Sender IDs are only supported with registration. Without registration to this network, Alpha Senders will be overwritten to Generic Alpha Sender IDs or will NOT deliver.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

### China
- **MCC:** 460
- **Dial Code:** 86
- Alphanumeric Sender IDs are not supported.
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.
- All message content has to be whitelisted by local operators. It is highly advised to pre-register message content templates.

### Egypt
- **MCC:** 602
- **Dial Code:** 20
- Alphanumeric Sender IDs are supported.
- For network Etisalat (60203), Alphanumeric Senders are only supported through registration. Without registration to this network, Alpha Senders will be overwritten to Generic Alpha Sender IDs or will NOT deliver.

### Ghana
- **MCC:** 620
- **Dial Code:** 233
- Alphanumeric Sender IDs are supported.
- For Network MTN (62001), Alphanumeric Sender IDs are only supported with registration. Without registration to this network, Alpha Senders will be overwritten to Generic Alpha Sender IDs or will NOT deliver.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

### India
- **MCC:** 404 - 405
- **Dial Code:** 91
- Alphanumeric Sender IDs are partially supported through registration. Only Local Alpha Sender IDs (Local Entities) can be registered (DLT registration process) while no registration is possible for International Alpha Sender IDs.
- International Alphanumeric Sender IDs will be overwritten to a random [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

### Iran
- **MCC:** 432
- **Dial Code:** 98
- [Alphanumeric Sender IDs](https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id) are partially supported.
- For network Righttel (43220), Alphanumeric Sender IDs are supported and will be maintained.
- Alphanumeric Sender ID registration is required for Network MCI (43211). For the remaining networks, Alphanumeric Senders will be overwritten to a random long code to ensure delivery.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

### Japan
- **MCC:** 440
- **Dial Code:** 81
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- SMS containing URLs as part of the message body could be filtered.

### Kenya
- **MCC:** 639
- **Dial Code:** 254
- Alphanumeric Sender IDs are supported with registration. Alphanumeric Sender ID registration is required.
- Political, religious, gambling, adult, and P2P content is prohibited.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

### Nepal
- **MCC:** 429
- **Dial Code:** 977
- Alphanumeric Sender IDs are supported.
- For Network Ncell (42902), Alphanumeric Sender IDs are only supported with registration. Without registration to this network, Alpha Senders will be overwritten to Generic Alpha Sender IDs or will NOT deliver.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

### Oman
- **MCC:** 422
- **Dial Code:** 968
- Alphanumeric Sender IDs are supported with registration. Alphanumeric Sender ID registration is required.
- Non-registered Alpha Sender IDs will either be rejected or overwritten. However, this is on a best-effort basis.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

### South Sudan
- **MCC:** 659
- **Dial Code:** 211
- Alphanumeric Sender IDs are supported.
- For Network MTN (65902), Alphanumeric Sender IDs are only supported with registration. Without registration to this network, Alpha Senders will be overwritten to Generic Alpha Sender IDs or will NOT deliver.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

### Sudan
- **MCC:** 634
- **Dial Code:** 249
- Alphanumeric Sender IDs are supported.
- For Network MTN (63402), Alphanumeric Sender IDs are only supported with registration. Without registration to this network, Alpha Senders will be overwritten to Generic Alpha Sender IDs or will NOT deliver.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

### Taiwan
- **MCC:** 466
- **Dial Code:** 886
- All Alphanumeric Sender IDs will be overwritten to a random Local Long Code to ensure delivery.

### Vietnam
- **MCC:** 452
- **Dial Code:** 84
- Alphanumeric Sender IDs are supported with registration. Alphanumeric Sender ID registration is required.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.
- Vietnam is a destination that supports SMSC-DLR only; as such, positive DLRs are to be expected. Handset delivery reports are not possible.

## Additional SMS Resources

- [SMS API](https://telnyx.com/products/sms-api) product features
- [MMS API](https://telnyx.com/products/mms-api) product features
- [Messaging API pricing](https://telnyx.com/pricing/messaging)
- [SMS opt-in guide](https://telnyx.com/resources/sms-opt-in)
- [SMS number type guide](https://telnyx.com/resources/sms-numbers-traffic-types)
- [Guide to hosted SMS](https://telnyx.com/resources/hosted-sms-how-to-guide)
- [Mastering CTIA guidelines](https://telnyx.com/resources/CTIA-SMS-guidelines)
- [Guide to compliant bulk SMS](https://telnyx.com/resources/bulk-sms-guide)
- [SMS compliance and regulations](https://telnyx.com/resources/how-to-ensure-compliance-with-sms-regulations)
