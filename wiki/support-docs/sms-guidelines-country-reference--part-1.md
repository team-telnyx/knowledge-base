---
title: 'SMS Guidelines: Country Reference'
summary: Consolidated Telnyx SMS guidelines for 15 destinations (Botswana, Brazil,
  Brunei Darussalam, Burkina Faso, Czech Republic, Japan, Laos PDR, Lesotho, Namibia,
  New Zealand, Poland, South Africa, Thailand, Timor-Leste, and Vietnam), covering
  MCC, dial code, Alphanumeric Sender ID support and registration requirements, content
  restrictions, and delivery-report behavior.
sources:
- url: https://support.telnyx.com/en/articles/6531712-brazil-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545167-poland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545173-south-africa-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561237-czech-republic-czechia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6600928-botswana-sms-guidelines
- url: https://support.telnyx.com/en/articles/6600934-brunei-darussalam-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601004-burkina-faso-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674476-japan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674798-laos-pdr-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674813-lesotho-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678890-namibia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679036-new-zealand-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683302-thailand-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683340-timor-leste-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683467-vietnam-sms-guidelines
updated_at: 2026-07-17T09:11:08Z
---

# SMS Guidelines: Country Reference

*Part 1 of 2 — see also: [Part 2](sms-guidelines-country-reference--part-2.md)*

Consolidated Telnyx SMS guidelines for 15 destinations (Botswana, Brazil, Brunei Darussalam, Burkina Faso, Czech Republic, Japan, Laos PDR, Lesotho, Namibia, New Zealand, Poland, South Africa, Thailand, Timor-Leste, and Vietnam), covering MCC, dial code, Alphanumeric Sender ID support and registration requirements, content restrictions, and delivery-report behavior.

## Overview

This page consolidates Telnyx SMS guidelines for 15 destinations across the Americas, Europe, Africa, Asia, and Oceania. Each destination entry lists the Mobile Country Code (MCC), international dial code, and the rules governing Alphanumeric (Alpha) Sender IDs, including whether registration is required, whether sender IDs are overwritten, and any content or delivery-report restrictions. All senders must also comply with the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md).

## Botswana

- **MCC:** 652
- **Dial Code:** 267
- Alphanumeric Sender IDs are supported. Registration is not possible.
- The use of generic Alpha Sender IDs is not recommended as these can be rejected or blocked by local Operators. Alphanumeric Sender IDs should be directly related to the message content.

## Brazil

- **MCC:** 724
- **Dial Code:** 55
- Alpha Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code). Registration is not possible.
- Brazil is a destination that supports SMSC-DLR only; positive DLRs are to be expected. Handset delivery reports are not possible.

## Brunei Darussalam

- **MCC:** 528
- **Dial Code:** 673
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Burkina Faso

- **MCC:** 613
- **Dial Code:** 226
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Czech Republic (Czechia)

- **MCC:** 230
- **Dial Code:** 420
- Alphanumeric Sender IDs are partially supported. Alphanumeric Sender ID registration is possible towards T-Mobile (23001) and O2 (23002).
- Without registration to these networks, Alphanumeric Sender IDs can be overwritten to a random Short Code or a Generic Sender to ensure delivery.
- For more information on Alpha Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Japan

- **MCC:** 440
- **Dial Code:** 81
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- SMS containing URLs as part of the message body could be filtered.

## Laos PDR

- **MCC:** 457
- **Dial Code:** 856
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Lesotho

- **MCC:** 651
- **Dial Code:** 266
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Namibia

- **MCC:** 649
- **Dial Code:** 264
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- Occasionally Alphanumeric Sender IDs might be replaced by a Generic Alphanumeric Sender ID to ensure delivery.
- There are no restrictions with regards to content towards this destination.

## New Zealand

- **MCC:** 530
- **Dial Code:** 64
- All Alphanumeric Sender IDs will be overwritten to a random [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.
- Due to local restrictions, dedicated short codes are the best way to improve delivery towards this destination. Without a dedicated short code, message delivery is to be considered as best-effort delivery only.

## Poland

- **MCC:** 260
- **Dial Code:** 48
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.
- There are no restrictions with regards to content towards this destination.

## South Africa

- **MCC:** 655
- **Dial Code:** 27
- All Alphanumeric Sender IDs will be overwritten to a random Local Long Code.

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
- Occasionally the Alphanumeric Sender ID might be overwritten to a random [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Vietnam

- **MCC:** 452
- **Dial Code:** 84
- Alphanumeric Sender IDs are supported with registration. Alphanumeric Sender ID registration is required.
- The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.
- Vietnam is a destination that supports SMSC-DLR only; positive DLRs are to be expected. Handset delivery reports are not possible.
- For more information on Alpha Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## SMS Resources for South Africa and New Zealand

For South Africa and New Zealand, Telnyx publishes additional SMS resources covering the SMS landscape, compliance, pricing, MMS, opt-in, traffic types, hosted SMS, CTIA guidelines, and bulk SMS best practices. Useful starting points include:

- [SMS API product features](https://telnyx.com/products/sms-api)
- [MMS API product features](https://telnyx.com/products/mms-api)
- [Messaging API pricing](https://telnyx.com/pricing/messaging)
- [SMS opt-in guide](https://telnyx.com/resources/sms-opt-in)
- [SMS number type guide](https://telnyx.com/resources/sms-numbers-traffic-types)
- [Guide to hosted SMS](https://telnyx.com/resources/hosted-sms-how-to-guide)
- [Mastering CTIA guidelines](https://telnyx.com/resources/CTIA-SMS-guidelines)
- [Guide to compliant bulk SMS](https://telnyx.com/resources/bulk-sms-guide)
- [SMS compliance and regulations](https://telnyx.com/resources/how-to-ensure-compliance-with-sms-regulations)
