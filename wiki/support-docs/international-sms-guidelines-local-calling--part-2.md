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

*Part 2 of 2 — see also: [Part 1](international-sms-guidelines-local-calling--part-1.md)*

A consolidated reference for Telnyx SMS guidelines across supported countries, covering alphanumeric sender ID requirements, content restrictions, and opt-out rules, together with an overview of the PSTN replacement / local calling feature for high-completion-rate voice calls.

## PSTN Replacement and Local Calling

A call is **local** when the caller's number (CLI) and the destination number (CLD) belong to the same country. Local calls cannot enter a country through international exchanges; if they do, downstream carriers block or reject them as potential spoofing, resulting in failed calls and SIP 503 errors.

### How Telnyx Solves This

Telnyx routes calls directly through **Tier-1 carrier partners within each country**, bypassing international exchanges:

1. Your caller originates a call from anywhere in the world.
2. The call arrives at the Telnyx network.
3. Telnyx identifies the destination country and routes via its direct in-country Tier-1 carrier interconnect.
4. The call is delivered locally; the callee sees a local number.

### Key Benefits

- **Higher call completion rates** — calls are not blocked at international exchanges.
- **Local caller ID delivered correctly** — the callee sees a local number, not an international one.
- **Establish local presence** — build customer trust by appearing local.
- **No extra charges or configuration** — the feature is built into your Telnyx-issued local number.

### Requirements

No additional fees or complex setup is needed. You simply need a Telnyx number with the **Local Calling** feature enabled:

1. Log in to the [Telnyx Portal](https://portal.telnyx.com).
2. Navigate to **Numbers → Buy numbers**.
3. Select the destination country.
4. Filter results by the **Local Calling** feature.
5. Choose a number and complete the purchase.
6. Use this number as the CLI on your outbound calls.

Alternatively, email [numbering@telnyx.com](mailto:numbering@telnyx.com) to request a number, or port an existing number to Telnyx (see the [porting policy & procedure](https://support.telnyx.com/en/articles/1130630-porting-policy-procedure) guide). Review the [Caller ID Policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) and [Number Formats](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats) for localisation preferences.

### Important Notes

- If you cannot purchase a Telnyx local number, use a CLI from a **different country** than the destination. Calls with a matching foreign CLI are the most likely to be blocked.
- Non-Telnyx numbers are routed via Tier-2 international routes where caller ID delivery and call completion are **best-effort and not guaranteed**.
- If call forwarding is enabled on your local number, local calling may not complete successfully if the caller's CLI matches the forwarded destination number. Telnyx only guarantees local call completion when the originating number is used as the CLI.

### Supported Countries for Local Calling

Telnyx continues to expand coverage. Countries not listed below only have inbound local calling guaranteed at this time.

| Country | Code | | Country | Code |
|---|---|---|---|---|
| Albania | +355 | | Latvia | +371 |
| Argentina | +54 | | Lithuania | +370 |
| Australia | +61 | | Luxembourg | +352 |
| Austria | +43 | | Malaysia | +60 |
| Bahrain | +973 | | Martinique | +596 |
| Bangladesh | +88 | | Mexico | +52 |
| Belgium | +32 | | Mozambique | +258 |
| Belize | +501 | | Netherlands | +31 |
| Benin | +229 | | New Zealand | +64 |
| Bolivia | +591 | | Nicaragua | +505 |
| Bosnia and Herzegovina | +387 | | Nigeria | +234 |
| Brazil | +55 | | Norway | +47 |
| Bulgaria | +359 | | Oman | +968 |
| Cameroon | +237 | | Pakistan | +92 |
| Chile | +56 | | Panama | +507 |
| China | +86 | | Paraguay | +595 |
| Colombia | +57 | | Peru | +51 |
| Costa Rica | +506 | | Philippines | +63 |
| Croatia | +385 | | Poland | +48 |
| Cyprus | +357 | | Portugal | +351 |
| Czech Republic | +420 | | Romania | +40 |
| Dem. Rep. of the Congo | +243 | | Russia | +7 |
| Denmark | +45 | | Rwanda | +250 |
| Dominican Republic | +1829 | | Réunion | +262 |
| El Salvador | +503 | | Saudi Arabia (KSA) | +966 |
| Estonia | +372 | | Serbia | +381 |
| Ecuador | +593 | | Singapore | +65 |
| Finland | +358 | | Slovakia | +421 |
| France | +33 | | Slovenia | +386 |
| French Guiana | +594 | | South Africa | +27 |
| Georgia | +995 | | South Korea | +82 |
| Germany | +49 | | Spain | +34 |
| Ghana | +233 | | Sweden | +46 |
| Greece | +30 | | Switzerland | +41 |
| Guadeloupe | +590 | | Taiwan | +886 |
| Guatemala | +502 | | Thailand | +66 |
| Honduras | +504 | | U.S. Virgin Islands | +1340 |
| Hong Kong | +852 | | United Arab Emirates | +971 |
| Hungary | +36 | | United Kingdom | +44 |
| Indonesia | +62 | | Uzbekistan | +998 |
| Ireland | +353 | | Vietnam | +84 |
| Israel | +972 | | Zambia | +260 |
| Italy | +39 | | | |
| Japan | +81 | | | |
| Kenya | +254 | | | |

For requirements beyond the countries listed, contact your Account Manager or [sales@telnyx.com](mailto:sales@telnyx.com).
