---
title: 'SMS Guidelines: Americas and Europe'
summary: Consolidated Telnyx SMS guidelines for Argentina, Belgium, Bolivia, Bulgaria,
  Chile, Colombia, Dominican Republic, Ecuador, El Salvador, Mexico, Paraguay, Peru,
  Romania, Uruguay, and Venezuela, covering MCC, dial codes, Alphanumeric Sender ID
  handling, per-network exceptions, and content restrictions.
sources:
- url: https://support.telnyx.com/en/articles/6531664-mexico-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531675-belgium-sms-guidelines
- url: https://support.telnyx.com/en/articles/6534652-colombia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561262-romania-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563862-bulgaria-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564188-argentina-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564249-bolivia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564549-peru-sms-guidelines
- url: https://support.telnyx.com/en/articles/6570309-uruguay-sms-guidelines
- url: https://support.telnyx.com/en/articles/6570320-paraguay-sms-guidelines
- url: https://support.telnyx.com/en/articles/6570364-chile-sms-guidelines
- url: https://support.telnyx.com/en/articles/6570385-ecuador-sms-guidelines
- url: https://support.telnyx.com/en/articles/6573669-venezuela-sms-guidelines
- url: https://support.telnyx.com/en/articles/6574078-el-salvador-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665730-dominican-republic-sms-guidelines
updated_at: 2026-07-17T09:10:59Z
---

# SMS Guidelines: Americas and Europe

Consolidated Telnyx SMS guidelines for Argentina, Belgium, Bolivia, Bulgaria, Chile, Colombia, Dominican Republic, Ecuador, El Salvador, Mexico, Paraguay, Peru, Romania, Uruguay, and Venezuela, covering MCC, dial codes, Alphanumeric Sender ID handling, per-network exceptions, and content restrictions.

## Overview

This page consolidates Telnyx SMS guidelines for a selection of countries across the Americas and Europe. Each country entry lists the Mobile Country Code (MCC), international dial code, and the rules governing Alphanumeric Sender IDs, including any per-network exceptions, registration requirements, content restrictions, and URL handling. All senders must also comply with the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md).

## Argentina

- **MCC:** 722
- **Dial Code:** 53
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Belgium

- **MCC:** 206
- **Dial Code:** 32
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Bolivia

- **MCC:** 736
- **Dial Code:** 591
- Alphanumeric Sender IDs are not supported. Registration is not possible.
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or Short Code to ensure delivery.

## Bulgaria

- **MCC:** 284
- **Dial Code:** 359
- [Alphanumeric Sender IDs](https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id) are partially supported. Registration is not possible.
- Towards networks Vivacom 24803 and Telenor 24805, Alphanumeric Sender IDs will be maintained.
- Alphanumeric Sender IDs will be overwritten to a random Local Long Code, Short Code, or generic Alphanumeric Sender ID to ensure delivery towards network A1 28401.

## Chile

- **MCC:** 730
- **Dial Code:** 56
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Colombia

- **MCC:** 732
- **Dial Code:** 57
- Alpha Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code).
- Commercial or marketing content can only be sent from 8:00am to 9:00pm. To send this type of traffic outside of these hours, explicit consent must be provided by the end-user.
- Opt-out options must always be included, using the words *Salir* or *Cancelar*.
- Adult content must only be sent to end-users of legal age if previously requested by them.

## Dominican Republic

- **MCC:** 370
- **Dial Code:** 1809
- Alphanumeric Sender IDs are supported. No registration is required.
- Occasionally an Alphanumeric Sender ID might be overwritten to a random [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Ecuador

- **MCC:** 740
- **Dial Code:** 593
- Alphanumeric Sender IDs are partially supported. Registration is not possible.
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery. Except for network CNT (74002), Alpha Sender IDs will be maintained and delivered dynamically to this network.

## El Salvador

- **MCC:** 706
- **Dial Code:** 503
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Mexico

- **MCC:** 334
- **Dial Code:** 52
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Paraguay

- **MCC:** 744
- **Dial Code:** 595
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Peru

- **MCC:** 716
- **Dial Code:** 51
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or Short Code to ensure delivery.

## Romania

- **MCC:** 226
- **Dial Code:** 40
- [Alphanumeric Sender IDs](https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id) are partially supported.
- Towards networks Telekom 22603 and Lycamobile 22616, Alphanumeric Sender IDs will be maintained.
- Alphanumeric Sender IDs will be overwritten to a random [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery towards networks Vodafone 22601, Orange 22610, and DigiMobil 22605.
- Messages containing URLs as part of the content can be blocked by local operators. URL whitelisting is possible.
- For more information on URL whitelisting, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Uruguay

- **MCC:** 748
- **Dial Code:** 598
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery.

## Venezuela

- **MCC:** 734
- **Dial Code:** 58
- Alphanumeric Sender IDs are partially supported. Registration is not possible.
- All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or [Short Code](https://telnyx.com/products/sms-short-code) to ensure delivery. Except for network Movilnet (73406), Alpha Sender IDs will be maintained and delivered dynamically to this network.

## Compliance

All senders must comply with the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md) regardless of destination country. Country-specific restrictions (such as Colombia's time-of-day rules for commercial content, opt-out language requirements, and adult content restrictions) apply in addition to the global policy.
