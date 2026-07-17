---
title: 'Telnyx SMS Guidelines: Eastern Europe, Caucasus, Central Asia, and Middle
  East'
summary: Consolidated Telnyx SMS guidelines for Armenia, Azerbaijan, Hungary, Iran,
  Kyrgyzstan, Oman, the Russian Federation, Saudi Arabia, Tajikistan, Turkey, Turkmenistan,
  Ukraine, the United Arab Emirates, Uzbekistan, and Yemen — covering MCC, dial code,
  Alphanumeric Sender ID registration requirements, and country-specific content and
  traffic restrictions.
sources:
- url: https://support.telnyx.com/en/articles/6561206-hungary-sms-guidelines
- url: https://support.telnyx.com/en/articles/6563904-ukraine-sms-guidelines
- url: https://support.telnyx.com/en/articles/6564056-turkey-sms-guidelines
- url: https://support.telnyx.com/en/articles/6592510-armenia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596144-azerbaijan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674403-iran-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674794-kyrgyzstan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679138-oman-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680009-saudi-arabia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683287-tajikistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683390-turkmenistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683438-united-arab-emirates-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683454-uzbekistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683484-yemen-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683563-russian-federation-sms-guidelines
updated_at: 2026-07-17T09:11:26Z
---

# Telnyx SMS Guidelines: Eastern Europe, Caucasus, Central Asia, and Middle East

*Part 1 of 2 — see also: [Part 2](telnyx-sms-guidelines-eastern-europe-caucasus-central-asia-and-middle-east--part-2.md)*

Consolidated Telnyx SMS guidelines for Armenia, Azerbaijan, Hungary, Iran, Kyrgyzstan, Oman, the Russian Federation, Saudi Arabia, Tajikistan, Turkey, Turkmenistan, Ukraine, the United Arab Emirates, Uzbekistan, and Yemen — covering MCC, dial code, Alphanumeric Sender ID registration requirements, and country-specific content and traffic restrictions.

## Overview

This page consolidates Telnyx SMS guidelines for a set of countries spanning Eastern Europe, the Caucasus, Central Asia, the Middle East, and one Central European country (Hungary). For each country the page lists the Mobile Country Code (MCC), international dial code, and the rules that govern Alphanumeric Sender IDs — including whether registration is required, what happens to unregistered senders, and any content or traffic restrictions that apply.

All senders must comply with the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md). Where Alphanumeric Sender ID registration is required, requests and supporting documentation should be sent to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com).

## Country Reference Table

| Country | MCC | Dial Code | Sender ID policy |
|---|---|---|---|
| Armenia | 374 | 283 | Registration required; unregistered senders overwritten to a generic Alpha Sender ID or rejected |
| Azerbaijan | 400 | 994 | Registration required; valid business case needed |
| Hungary | 216 | 36 | All Alphanumeric Sender IDs overwritten to a random Local Long Code or Short Code |
| Iran | 432 | 98 | Partially supported; Righttel (43220) supports and maintains Alpha Senders; MCI (43211) requires registration; other networks overwrite to a random long code |
| Kyrgyzstan | 437 | 996 | Registration required; valid business case needed |
| Oman | 422 | 968 | Registration required; non-registered senders rejected or overwritten (best-effort) |
| Russian Federation | 250 | 7 | Registration required; unregistered senders overwritten to a generic Alpha Sender ID or will not deliver; $250 monthly recurring fee per Sender ID |
| Saudi Arabia | 420 | 966 | Registration required; international brands only; "AD" suffix required for promotional traffic |
| Tajikistan | 436 | 992 | Registration required; unregistered senders rejected |
| Turkey | 286 | 90 | Registration required; operator appends a 4-character code beginning with "B" |
| Turkmenistan | 438 | 993 | All Alphanumeric Sender IDs overwritten to a random Long Code or Generic Alphanumeric Sender ID |
| Ukraine | 255 | 380 | Partially supported; registration not possible; best-effort delivery |
| United Arab Emirates | 424 | 971 | Registration required; "AD" suffix required for promotional traffic; time-of-day restrictions apply |
| Uzbekistan | 434 | 998 | Registration required; valid business case needed; occasional overwrite to a random Short Code |
| Yemen | 421 | 967 | Registration required; unregistered senders rejected; occasional overwrite to a random Short Code |

## Armenia

- **MCC:** 374
- **Dial Code:** 283

Alphanumeric Sender IDs are supported with registration. Without registration, Alpha Sender IDs will be overwritten to a generic Alpha Sender ID or rejected. Alpha Sender ID registration is advised.

## Azerbaijan

- **MCC:** 400
- **Dial Code:** 994

Alphanumeric Sender ID registration is required. Companies must have a valid business case for the requested Alphanumeric Sender ID; if the relationship between the company/brand and the requested sender is not clear, additional supporting documentation must be provided.

Consent (proof of opt-in) should be obtained before sending any communications, including marketing SMS. Traffic should include clear opt-out options.

## Hungary

- **MCC:** 216
- **Dial Code:** 36

All Alphanumeric Sender IDs will be overwritten to either a random Local Long Code or Short Code to ensure delivery. See the [Hungary country-specific guidelines](https://telnyx.com/country-specific-guidelines) for more detail.

## Iran

- **MCC:** 432
- **Dial Code:** 98

Alphanumeric Sender IDs are partially supported. For network Righttel (43220), Alphanumeric Sender IDs are supported and will be maintained. Alphanumeric Sender ID registration is required for network MCI (43211). For the remaining networks, Alphanumeric Senders will be overwritten to a random long code to ensure delivery.

The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

## Kyrgyzstan

- **MCC:** 437
- **Dial Code:** 996

Alphanumeric Sender ID registration is required. Companies must have a valid business case for the requested Alphanumeric Sender ID; if the relationship between the company/brand and the requested sender is not clear, additional supporting documentation must be provided.

Consent (proof of opt-in) should be obtained before sending any communications, including marketing SMS. Traffic should include clear opt-out options.

## Oman

- **MCC:** 422
- **Dial Code:** 968

Alphanumeric Sender IDs are supported with registration. Non-registered Alpha Sender IDs will either be rejected or overwritten; however, this is on a best-effort basis.

The use of generic Alpha Sender IDs is not recommended. Alpha Senders should be directly related to the message content.

## Russian Federation

- **MCC:** 250
- **Dial Code:** 7

Alphanumeric Sender IDs are supported with registration. Without registration, Alpha Senders will be overwritten to generic Alpha Sender IDs or will not deliver. For every Sender ID there is a monthly recurring cost of $250.

## Saudi Arabia

- **MCC:** 420
- **Dial Code:** 966

Alphanumeric Sender ID registration is required. Registration is only possible for international brands. For promotional traffic, the suffix "AD" must be added to the Alphanumeric Sender for traffic distinction. If message content includes URLs, these must also be whitelisted as part of the Alphanumeric Sender ID registration process; the use of shortened URL links (bit links) is not allowed. Gambling, political, or adult traffic is prohibited.

Registration forms are available for STC and Zain networks:

- [NOC_Template_KSA STC.docx](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/1073796842/308d5690074fc8fb94e2f15f/NOC_Template_KSA+STC.docx?expires=1783507500&signature=8355cfd98da30071c5db538108973bc39cc964d23d130a383f43689f13829241&req=dSAgFc53m4lbW%2FMW1HO4zdtYWo2JHv%2F%2BGq5XuAGUQx2IN3NkFBSRhxBPZoFJ%0Av%2BnwMsaeLDU%3D%0A)
- [NOC_Template_KSA Zain.docx](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/1073796960/f3c608e829ed1e141d9801f0/NOC_Template_KSA+Zain.docx?expires=1783507500&signature=655b971c58186ed720211935c32e22404202cab647c47d819767424d8d88634f&req=dSAgFc53m4hZWfMW1HO4za0KR56wHXRnapZ5oOYPSZE9b4Ie%2BT544zSmAzbX%0A%2BtJEx3VG1vg%3D%0A)

## Tajikistan

- **MCC:** 436
- **Dial Code:** 992

Alphanumeric Sender ID registration is required. All messages from unregistered Sender IDs will be rejected. Companies must have a valid business case for the requested Alphanumeric Sender ID; if the relationship between the company/brand and the requested sender is not clear, additional supporting documentation must be provided.

Consent (proof of opt-in) should be obtained before sending any communications, including marketing SMS. Traffic should include clear opt-out options.

## Turkey

- **MCC:** 286
- **Dial Code:** 90

Alphanumeric Sender IDs are supported with registration. A 4-character code beginning with the letter "B" will be added at the end of the message content by the terminating operator in line with the guidelines implemented by the Information and Communication Technologies Authority. Gambling traffic is not allowed towards Turkey.

The registration form is available here: [Turkey SIDreg.doc](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/ltcafuzd/2398133417/cb58fd0192712828878b2de2f88b/Turkey+SIDreg.doc?expires=1783507500&signature=1374af7c09056770df0dfa4bc003f3d0a5686f8a5b88c683dbc651c1cdfb65a9&req=diMuHsh9noVeXvMW1HO4zcA31PPvMq5%2BTPW3iqyRFbCBayeDkA62iVh1%2BfCe%0AzOFDM1ODVmA%3D%0A)

## Turkmenistan

- **MCC:** 438
- **Dial Code:** 993

All Alphanumeric Sender IDs will be overwritten to either a random Long Code or Generic Alphanumeric Sender ID to ensure delivery.
