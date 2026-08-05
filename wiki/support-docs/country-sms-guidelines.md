---
title: Country SMS Guidelines
summary: Telnyx SMS sending guidelines for 15 destinations, covering MCC, dial codes,
  Alphanumeric Sender ID support, registration requirements, content restrictions,
  and country-specific delivery rules.
sources:
- url: https://support.telnyx.com/en/articles/6531603-france-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601081-central-african-republic-sms-guidelines
- url: https://support.telnyx.com/en/articles/6661387-cook-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665126-cuba-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665699-djibouti-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670819-french-polynesia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674331-haiti-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674798-laos-pdr-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679036-new-zealand-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679369-qatar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679992-san-marino-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680123-solomon-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683302-thailand-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683340-timor-leste-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683726-kiribati-sms-guidelines
updated_at: 2026-08-05T13:36:28Z
---

# Country SMS Guidelines

Telnyx SMS sending guidelines for 15 destinations, covering MCC, dial codes, Alphanumeric Sender ID support, registration requirements, content restrictions, and country-specific delivery rules.

## Overview

This page consolidates Telnyx SMS guidelines for the following destinations: France, Central African Republic, Cook Islands, Cuba, Djibouti, French Polynesia, Haiti, Laos PDR, New Zealand, Qatar, San Marino, Solomon Islands, Thailand, Timor-Leste, and Kiribati. Each entry lists the country MCC and dial code, Alphanumeric Sender ID support and registration requirements, content restrictions, and any country-specific delivery rules. All senders must comply with the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md).

## France

- **MCC:** 208
- **Dial Code:** 33
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- As of March 1, 2026, the use of special characters in Alphanumeric Senders is not allowed.
- Telnyx advises the use of Alphanumeric Sender IDs for all [A2P](https://telnyx.com/resources/what-is-a2p-messaging) traffic towards this destination.
- When sending towards MVNO NRJ (20826) and Truphone (20812), Alphanumeric Sender IDs will be replaced by either a random local number or a [Short Code](https://telnyx.com/products/sms-short-code).
- Local operators do not allow marketing/promotional traffic to be sent on Sundays and French Public Holidays, between 10 pm and 8 am. Messages attempted during this time will be queued and delivery will be attempted afterwards.
- All marketing/promotional traffic should include a clear option to opt-out as part of the message content. The fragment **STOP au 36179** must be added at the end of the message. If missing, this will be added automatically.
- **Anti-Phishing measures:** French operators have implemented an additional check (Whitelisting) on a group of Alphanumeric Sender IDs. Traffic using these Alphanumeric Sender IDs will only be possible through the submission of a duly signed Letter of Authorization.

## Central African Republic

- **MCC:** 623
- **Dial Code:** 236
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Cook Islands

- **MCC:** 682
- **Dial Code:** 548
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Cuba

- **MCC:** 368
- **Dial Code:** 53
- Alphanumeric Sender IDs are supported with registration. Alphanumeric Sender ID registration is required.
- Senders composed of a combination of letters and numbers are not supported.
- Provision times for Alphanumeric Registration: up to 6 months.
- For more information on Alpha Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Djibouti

- **MCC:** 253
- **Dial Code:** 638
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.
- There are no restrictions with regards to content towards this destination.

## French Polynesia

- **MCC:** 547
- **Dial Code:** 689
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Haiti

- **MCC:** 372
- **Dial Code:** 509
- Alphanumeric Sender IDs are supported.
- For Network NATCOM (37203), Alphanumeric Sender IDs are only supported with registration. Without registration to this network, Alpha Senders will be overwritten to Generic Alpha Sender IDs or will not deliver.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.
- For more information on Alpha Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Laos PDR

- **MCC:** 457
- **Dial Code:** 856
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## New Zealand

- **MCC:** 530
- **Dial Code:** 64
- All Alphanumeric Sender IDs will be overwritten to a random [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.
- Due to local restrictions, dedicated short codes are the best way to improve delivery towards this destination. Without a dedicated short code, message delivery is to be considered as best-effort delivery only.

## Qatar

- **MCC:** 427
- **Dial Code:** 974
- Alphanumeric Sender IDs are supported with registration. Alphanumeric Sender ID registration is required.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.
- Religious, political, or adult traffic is prohibited.
- For more information on Alpha Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## San Marino

- **MCC:** 292
- **Dial Code:** 378
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Solomon Islands

- **MCC:** 540
- **Dial Code:** 677
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Thailand

- **MCC:** 520
- **Dial Code:** 66
- Alphanumeric Sender IDs are supported with registration. Alphanumeric Sender ID registration is required.
- Religious, gambling, political, or adult traffic is prohibited.
- For more information on Alpha Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Timor-Leste

- **MCC:** 514
- **Dial Code:** 670
- Alphanumeric Sender IDs are supported. No registration is required.
- Occasionally, Alphanumeric Sender IDs might be overwritten to a random [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Kiribati

- **MCC:** 545
- **Dial Code:** 686
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Additional SMS Resources

For Cook Islands and New Zealand, the following Telnyx resources are available:

- [SMS API](https://telnyx.com/products/sms-api) product features
- [MMS API](https://telnyx.com/products/mms-api) product features
- [Messaging API pricing](https://telnyx.com/pricing/messaging)
- [SMS opt-in guide](https://telnyx.com/resources/sms-opt-in)
- [SMS number type guide](https://telnyx.com/resources/sms-numbers-traffic-types)
- [Guide to hosted SMS](https://telnyx.com/resources/hosted-sms-how-to-guide)
- [Mastering CTIA guidelines](https://telnyx.com/resources/CTIA-SMS-guidelines)
- [Guide to compliant bulk SMS](https://telnyx.com/resources/bulk-sms-guide)
- [SMS compliance and regulations](https://telnyx.com/resources/how-to-ensure-compliance-with-sms-regulations)
