---
title: International SMS Guidelines & Local Calling
summary: A consolidated reference for Telnyx SMS guidelines across supported countries,
  covering alphanumeric sender ID requirements, content restrictions, and opt-out
  rules, together with an overview of the PSTN replacement / local calling feature
  for high-completion-rate voice calls.
sources:
- url: https://support.telnyx.com/en/articles/6534652-colombia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6589563-suriname-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596161-bangladesh-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601004-burkina-faso-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601061-cameroon-sms-guidelines
- url: https://support.telnyx.com/en/articles/6622229-pstn-replacement-local-calling-with-telnyx
- url: https://support.telnyx.com/en/articles/6661326-congo-sms-guidelines
- url: https://support.telnyx.com/en/articles/6661342-congo-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670411-egypt-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670439-equatorial-guinea-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670465-ethiopia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670834-gabon-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670843-gambia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670870-ghana-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674630-kenya-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675104-malawi-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675247-mali-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675690-mauritania-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677999-mozambique-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678890-namibia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679084-nigeria-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679407-rwanda-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680003-sao-tome-and-principe-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680041-senegal-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680053-seychelles-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680089-sierra-leone-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683355-togo-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683433-uganda-sms-guidelines
updated_at: 2026-06-11T11:22:00Z
---

# International SMS Guidelines & Local Calling

*Part 1 of 2 — see also: [Part 2](international-sms-guidelines-local-calling--part-2.md)*

A consolidated reference for Telnyx SMS guidelines across supported countries, covering alphanumeric sender ID requirements, content restrictions, and opt-out rules, together with an overview of the PSTN replacement / local calling feature for high-completion-rate voice calls.

## Country SMS Reference

The table below summarises per-country SMS settings. Where a country requires alphanumeric sender ID registration, see the [International SMS Guidelines & Local Calling#Alphanumeric Sender ID Registration](international-sms-guidelines-local-calling-alphanumeric-sender-id-registration.md) section for the process.

| Country | MCC | Dial Code | Alpha Sender ID Support | Registration |
|---|---|---|---|---|
| Bangladesh | 470 | 880 | Supported | Required (all networks; unregistered rejected) |
| Burkina Faso | 613 | 226 | Supported, maintained | Not required |
| Cameroon | 624 | 237 | Supported | Required on MTN (62401); otherwise overwritten to generic or not delivered |
| Colombia | 732 | 57 | Overwritten to random local long code or short code | N/A |
| Congo | 629 | 242 | Supported | Required on MTN (62910); otherwise overwritten to generic or not delivered |
| Dem. Rep. of the Congo | 630 | 243 | Supported | Required on Vodacom (63001); otherwise replaced by generic or short code |
| Egypt | 602 | 20 | Supported | Required on Etisalat (60203); otherwise overwritten to generic or not delivered |
| Equatorial Guinea | 627 | 240 | Supported, maintained | Not required |
| Ethiopia | 636 | 251 | Supported | Required on MTN (63601); otherwise overwritten to generic or not delivered |
| Gabon | 628 | 241 | Supported | Required (all networks; unregistered rejected) |
| Gambia | 607 | 220 | Supported, maintained | Not required |
| Ghana | 620 | 233 | Supported | Required on MTN (62001); otherwise overwritten to generic or not delivered |
| Kenya | 639 | 254 | Supported | Required (all networks) |
| Malawi | 650 | 265 | Supported | Required (all networks; unregistered rejected) |
| Mali | 610 | 223 | Supported | Required for local traffic; not required for international traffic |
| Mauritania | 609 | 222 | Supported, maintained | Not required |
| Mozambique | 643 | 258 | Supported | May be replaced by generic on Movitel (64303) to ensure delivery |
| Namibia | 649 | 264 | Supported, maintained | Not required (occasionally replaced by generic to ensure delivery) |
| Nigeria | 621 | 234 | Supported | Required (all networks; unregistered rejected) |
| Rwanda | 635 | 250 | Supported | Required on MTN (63510); otherwise overwritten to generic or not delivered |
| Sao Tome and Principe | 626 | 239 | Supported, maintained | Not required |
| Senegal | 608 | 221 | Supported, maintained | Not required |
| Seychelles | 633 | 248 | Supported, maintained | Not required |
| Sierra Leone | 619 | 232 | Supported, maintained | Not required |
| Suriname | 746 | 597 | Supported, maintained | Not required |
| Togo | 615 | 228 | Supported, maintained | Not required |
| Uganda | 641 | 256 | Supported | Required on MTN (64110); otherwise overwritten to generic or not delivered |

Generic alpha sender IDs are not recommended for any destination. Alpha senders should always be directly related to the message content.

## Alphanumeric Sender ID Registration

For countries that require registration (Bangladesh, Gabon, Kenya, Malawi, Nigeria, and network-specific cases listed above), submit the following information along with a copy of your Business Registration to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):

1. Sender ID to be registered
2. Message/content type
3. Message/content example
4. Company name (and brand name if different)
5. Website of brand or company
6. Company country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested sender ID. If the relationship between your company/brand and the requested sender ID is not clear, provide additional supporting documentation detailing the business case.

### Recommendations for Registered Traffic

- **Consent (opt-in proof)** should be obtained before sending any marketing communications.
- **Opt-out options** must always be included in traffic. For Colombia, the recognised opt-out keywords are *Salir* or *Cancelar*.

## Content Restrictions by Country

| Country | Restrictions |
|---|---|
| Colombia | Commercial/marketing content only allowed 08:00–21:00; outside these hours requires explicit end-user consent. Adult content only to legal-age end-users who previously requested it. Opt-out required (*Salir* / *Cancelar*). |
| Ethiopia | Local banking and promotional traffic is not allowed. |
| Gambia | Religious, political, and adult traffic is prohibited. |
| Kenya | Political, religious, gambling, adult, and P2P content is prohibited. |
| Nigeria | Religious, gambling, political, and adult traffic is prohibited. |

Countries not listed above (e.g., Burkina Faso, Equatorial Guinea, Mauritania, Mozambique, Namibia, Sao Tome and Principe, Seychelles, Suriname, Togo) have no specific content restrictions documented, but all traffic must comply with the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging).
