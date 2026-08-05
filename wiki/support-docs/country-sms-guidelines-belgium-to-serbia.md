---
title: Country SMS Guidelines - Belgium to Serbia
summary: Reference summary of Telnyx SMS sending guidelines for 15 countries, including
  MCC, dial code, alphanumeric sender ID support, registration requirements, and destination-specific
  delivery notes.
sources:
- url: https://support.telnyx.com/en/articles/6531675-belgium-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531712-brazil-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545173-south-africa-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560660-austria-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561206-hungary-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561262-romania-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564226-costa-rica-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564249-bolivia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6570309-uruguay-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596434-bosnia-and-herzegovina-sms-guidelines
- url: https://support.telnyx.com/en/articles/6600928-botswana-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670856-georgia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670869-germany-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675034-macedonia-north-macedonia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683745-serbia-sms-guidelines
updated_at: 2026-08-05T13:36:42Z
---

# Country SMS Guidelines - Belgium to Serbia

Reference summary of Telnyx SMS sending guidelines for 15 countries, including MCC, dial code, alphanumeric sender ID support, registration requirements, and destination-specific delivery notes.

## Overview

This page consolidates Telnyx SMS guidelines for the following destinations: Austria, Belgium, Bolivia, Bosnia and Herzegovina, Botswana, Brazil, Costa Rica, Georgia, Germany, Hungary, Macedonia (North Macedonia), Romania, Serbia, South Africa, and Uruguay. Each country entry lists the Mobile Country Code (MCC), international dial code, and the rules governing Alphanumeric Sender IDs, including whether they are supported, overwritten, or require registration.

## Austria

- **MCC:** 232
- **Dial Code:** 43
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Belgium

- **MCC:** 206
- **Dial Code:** 32
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or Short Code to ensure delivery.

## Bolivia

- **MCC:** 736
- **Dial Code:** 591
- Alphanumeric Sender IDs are not supported. Registration is not possible.
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or Short Code to ensure delivery.

## Bosnia and Herzegovina

- **MCC:** 218
- **Dial Code:** 387
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Botswana

- **MCC:** 652
- **Dial Code:** 267
- Alphanumeric Sender IDs are supported. Registration is not possible.
- The use of generic Alpha Sender IDs is not recommended as these can be rejected or blocked by local operators. Alphanumeric Sender IDs should be directly related to the message content.

## Brazil

- **MCC:** 724
- **Dial Code:** 55
- Alpha Sender IDs will be overwritten to either a random Local Long Code or Short Code. Registration is not possible.
- Brazil is a destination that supports SMSC-DLR only; as such, positive DLRs are to be expected. Handset delivery reports are not possible.

## Costa Rica

- **MCC:** 712
- **Dial Code:** 506
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or Short Code to ensure delivery.

## Georgia

- **MCC:** 282
- **Dial Code:** 995
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Germany

- **MCC:** 262
- **Dial Code:** 49
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- There are no restrictions with regards to content towards this destination.

## Hungary

- **MCC:** 216
- **Dial Code:** 36
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or Short Code to ensure delivery.

## Macedonia (North Macedonia)

- **MCC:** 294
- **Dial Code:** 389
- Alphanumeric Sender IDs are supported and will be maintained; no registration is required.
- Occasionally Alphanumeric Sender IDs might be replaced by a Generic Alphanumeric Sender ID to ensure delivery.
- There are no restrictions with regards to content towards this destination.

## Romania

- **MCC:** 226
- **Dial Code:** 40
- Alphanumeric Sender IDs are partially supported.
- Towards networks Telekom (22603) and Lycamobile (22616), Alphanumeric Sender IDs will be maintained.
- Alphanumeric Sender IDs will be overwritten to a random Short Code to ensure delivery towards networks Vodafone (22601), Orange (22610), and DigiMobil (22605).
- Messages containing URLs as part of the content can be blocked by local operators. URL whitelisting is possible.

## Serbia

- **MCC:** 220
- **Dial Code:** 381
- Alphanumeric Sender IDs are supported with registration.
- Registration is possible to ensure Alphanumeric Senders can be maintained. Without registration, Alpha Senders will be overwritten to Generic Alpha Sender IDs.
- The registration of Alphanumeric Senders involves monthly fees.

## South Africa

- **MCC:** 655
- **Dial Code:** 27
- All Alphanumeric Sender IDs will be overwritten to a random Local Long Code.

## Uruguay

- **MCC:** 748
- **Dial Code:** 598
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or Short Code to ensure delivery.

## Compliance and Additional Resources

All destinations listed above are subject to the Telnyx [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md). For Romania URL whitelisting and Serbia Alphanumeric Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com). For Hungary-specific information, see the [Telnyx country-specific guidelines](https://telnyx.com/country-specific-guidelines).

South Africa has additional supporting resources covering the SMS landscape, compliance, pricing, MMS, opt-in, traffic types, hosted SMS, CTIA guidelines, and bulk SMS best practices. See the [SMS API](https://telnyx.com/products/sms-api), [MMS API](https://telnyx.com/products/mms-api), [Messaging API pricing](https://telnyx.com/pricing/messaging), [SMS opt-in guide](https://telnyx.com/resources/sms-opt-in), [SMS number type guide](https://telnyx.com/resources/sms-numbers-traffic-types), [hosted SMS guide](https://telnyx.com/resources/hosted-sms-how-to-guide), [CTIA guidelines](https://telnyx.com/resources/CTIA-SMS-guidelines), [bulk SMS guide](https://telnyx.com/resources/bulk-sms-guide), and [SMS compliance and regulations](https://telnyx.com/resources/how-to-ensure-compliance-with-sms-regulations) for further detail.
