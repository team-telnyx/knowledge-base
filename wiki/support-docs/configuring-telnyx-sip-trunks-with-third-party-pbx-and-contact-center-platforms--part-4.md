---
title: Configuring Telnyx SIP Trunks with Third-Party PBX and Contact Center Platforms
summary: This page consolidates Telnyx guidance for configuring SIP trunks between
  the Telnyx Mission Control Portal and a range of third-party PBX, dialer, and contact
  center platforms, including Avaya, Vicidial, OSDial, and GOautodial. It covers both
  IP-based and credentials-based authentication, dialplan setup, outbound and inbound
  campaign configuration, and lead import for contact center use cases, alongside
  notes on reseller support, call center service availability, Linksys ATA dialplan
  syntax, and the deprecation of the legacy Access Control List feature.
sources:
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130655-can-i-resell-your-services
- url: https://support.telnyx.com/en/articles/1130667-do-you-offer-service-to-call-centers
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
- url: https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
updated_at: 2026-08-05T13:28:15Z
---

# Configuring Telnyx SIP Trunks with Third-Party PBX and Contact Center Platforms

*Part 4 of 4 — see also: [Part 1](configuring-telnyx-sip-trunks-with-third-party-pbx-and-contact-center-platforms--part-1.md), [Part 2](configuring-telnyx-sip-trunks-with-third-party-pbx-and-contact-center-platforms--part-2.md), [Part 3](configuring-telnyx-sip-trunks-with-third-party-pbx-and-contact-center-platforms--part-3.md)*

This page consolidates Telnyx guidance for configuring SIP trunks between the Telnyx Mission Control Portal and a range of third-party PBX, dialer, and contact center platforms, including Avaya, Vicidial, OSDial, and GOautodial. It covers both IP-based and credentials-based authentication, dialplan setup, outbound and inbound campaign configuration, and lead import for contact center use cases, alongside notes on reseller support, call center service availability, Linksys ATA dialplan syntax, and the deprecation of the legacy Access Control List feature.

## Call Center Service Availability

Telnyx offers service to call centers, which are considered an ideal customer profile. Contact Telnyx any time to get started. According to the most recent data, there are at least [32,000 call centers](https://www.ibisworld.com/industry-statistics/number-of-businesses/telemarketing-call-centers-united-states/) in the United States.

## Linksys ATA Dialplan Reference

A dial plan (or dialplan) is a string of characters that determines how entered phone digits are interpreted and transmitted by your ATA device. It also tells the device if it should accept or reject a call. It facilitates calling, as well as blocking of certain call profiles (such as long distance or international). The basic dial plan provided in the configuration samples for the Linksys ATA devices should work with Telnyx.

### Linksys Dialplan Digit Sequence

| Digit Sequence | Function |
| --- | --- |
| 0 1 2 3 4 5 6 7 8 9 \* # | Characters available to use that map to a phone digit. |
| x | Any phone digit. |
| [sequence] | You can enter characters between brackets to create an allow-list of only certain digits. For example, if you enter the range [1-5], the user may only press the digits from 1 to 5. You can also use consecutive characters to denote skipping certain numbers. For example, [25-7\*] allows the user to press 2, 5, 6, 7 or \*. (Note that 4 is missing, as are 8 and 9.) |
| . (period) | You can use a period to accept zero or more entries of the number that precedes the zero. For example, **01.** allows the user to enter 0, 01, 011 and so on. |
| <dialed:substituted> | This is used for sequence substitution. For example, with this sequence **<:1555>xxxxxxx**, if the user dials a 7-digit number, the number 1555 is added to the beginning of the sequence. If the user presses 6782345, the system transmits 15556782345. |
| , (comma) | This can be used between digits to play an "outside line" dial tone after a trigger number or sequence. For example, with this sequence **9, 1x.** an "outside line" dial tone is sounded after the user presses 9, and continues until the user presses 1. |
| ! (exclamation point) | You can use this character to prohibit a dial sequence. For example, the sequence **1900xxxxxxx!** will make the system reject any 1-900 number. |
| S0 or L0 | Overrides the Short or Long inter-digit timer to 0 seconds. For example: **<:1555>[2-9]xxxxxxS2** on a seven-digit local call, wait two seconds to see if any more digits are dialed — after the delay expires, prefix the number with local area code +1-555 and send it. **1[2-9]xx[2-9]xxxxxxS0** indicates, if +1-areacode-number is dialed as eleven digits, do not wait for additional dialed digits and send immediately. |
| P# (where # is the duration of the pause in seconds) | Pauses # seconds. |

## Access Control List Deprecation

The Access Control List has been deprecated and is no longer active. No users can add or modify any IPs to the ACL at this moment, regardless of account level.
