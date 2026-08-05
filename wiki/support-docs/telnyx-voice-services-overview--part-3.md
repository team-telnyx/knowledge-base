---
title: Telnyx Voice Services Overview
summary: This page consolidates Telnyx support documentation covering company locations,
  voice termination coverage, call completion (local and rural), rate sheets and LRN-based
  pricing, N11 and emergency dialing, inbound call screening, and PSTN replacement
  / local calling features.
sources:
- url: https://support.telnyx.com/en/articles/1130646-where-is-telnyx-located
- url: https://support.telnyx.com/en/articles/1130658-how-do-i-know-if-a-rate-has-changed
- url: https://support.telnyx.com/en/articles/1130664-countries-that-telnyx-offers-termination-in
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/articles/4096828-us-rural-call-completion
- url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
- url: https://support.telnyx.com/en/articles/4567969-united-states-n11-codes
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
- url: https://support.telnyx.com/en/articles/6622229-pstn-replacement-local-calling-with-telnyx
- url: https://support.telnyx.com/en/articles/6974437-updates-to-global-conversational-rate-deck
- url: https://support.telnyx.com/en/articles/8037040-inbound-call-screening
- url: https://support.telnyx.com/en/articles/8712528-dialing-emergency-services
- url: https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers
- url: https://support.telnyx.com/en/articles/9039036-emergency-services-and-ipnd-in-australia
updated_at: 2026-08-05T13:30:13Z
---

# Telnyx Voice Services Overview

*Part 3 of 5 — see also: [Part 1](telnyx-voice-services-overview--part-1.md), [Part 2](telnyx-voice-services-overview--part-2.md), [Part 4](telnyx-voice-services-overview--part-4.md), [Part 5](telnyx-voice-services-overview--part-5.md)*

This page consolidates Telnyx support documentation covering company locations, voice termination coverage, call completion (local and rural), rate sheets and LRN-based pricing, N11 and emergency dialing, inbound call screening, and PSTN replacement / local calling features.

## PSTN Replacement and Local Calling

A call is considered **local** when the caller's number (CLI) and the destination number (CLD) belong to the same country — for example, a UK number calling another UK number, or a Brazilian number calling another Brazilian number.

Local calls cannot enter a country through international exchanges. If a global business tries to make a local-looking call using standard international routing, downstream carriers in that country will block or reject it to protect their network from spoofing and unauthorised CLI usage. This results in failed calls, SIP 503 errors, and poor call completion rates.

### The Telnyx local calling solution

Telnyx routes calls directly through Tier-1 carrier partners within each country, bypassing international exchanges entirely:

1. The caller originates a call from anywhere in the world.
2. The call arrives at the Telnyx network.
3. Telnyx identifies the destination country and routes the call via its direct in-country Tier-1 carrier interconnect.
4. The call is delivered locally — the callee sees a local number and receives the call as if it originated from within their country.

This allows a business to establish a genuine local presence in any supported country, regardless of where the team or infrastructure is physically located.

### Key benefits

- Higher call completion rates — calls are no longer blocked at international exchanges
- Local caller ID delivered correctly — the callee sees a local number, not an international one
- Establish local presence — build customer trust by appearing local in every market
- No extra charges or configuration — the feature is built into Telnyx-issued local numbers

### Requirements for using Local Calling

There are no additional fees or complex setup steps. You simply need a Telnyx number with the **Local Calling** feature enabled.

**Step 1 — Get a local number with the Local Calling feature**

Purchase a number directly in the Telnyx Portal:

1. Log in to the [Telnyx Portal](https://portal.telnyx.com).
2. Navigate to **Numbers → Buy numbers**.
3. Select the destination country.
4. Filter results by the **Local Calling** feature.
5. Choose a number and complete the purchase.

Alternatively, email [numbering@telnyx.com](mailto:numbering@telnyx.com) to request a number, or port an existing number to Telnyx — see the porting policy & procedure guide. Use this same number as CLI on outbound calls. Review the Caller ID Policy and Number Formats for localisation preferences.

### If you don't use the local calling feature

If you cannot purchase a Telnyx local number, it is recommended to use a CLI from a different country than the destination. Calls with a matching foreign CLI are the most likely to be blocked. Using a non-Telnyx number from the same locale as the destination will not be accepted (outside of the US/CAN).

> **Note:** If call forwarding is enabled on a local number, local calling may not complete successfully if the caller's CLI matches the forwarded destination number. Telnyx can only guarantee local call completion when the originating number is used as the CLI.

### Supported countries

Telnyx currently supports local calling for the following countries:

| Country | Country Code |
| --- | --- |
| Albania | +355 |
| Argentina | +54 |
| Australia | +61 |
| Austria | +43 |
| Bahrain | +973 |
| Bangladesh | +88 |
| Belgium | +32 |
| Belize | +501 |
| Benin | +229 |
| Bolivia | +591 |
| Bosnia and Herzegovina | +387 |
| Brazil | +55 |
| Bulgaria | +359 |
| Cameroon | +237 |
| Chile | +56 |
| China | +86 |
| Colombia | +57 |
| Costa Rica | +506 |
| Croatia | +385 |
| Cyprus | +357 |
| Czech Republic | +420 |
| Democratic Republic of the Congo | +243 |
| Denmark | +45 |
| Dominican Republic | +1829 |
| El Salvador | +503 |
| Estonia | +372 |
| Ecuador | +593 |
| Finland | +358 |
| France | +33 |
| French Guiana | +594 |
| Georgia | +995 |
| Germany | +49 |
| Ghana | +233 |
| Greece | +30 |
| Guadeloupe | +590 |
| Guatemala | +502 |
| Honduras | +504 |
| Hong Kong | +852 |
| Hungary | +36 |
| Indonesia | +62 |
| Ireland | +353 |
| Israel | +972 |
| Italy | +39 |
| Japan | +81 |
| Kenya | +254 |
| Latvia | +371 |
| Lithuania | +370 |
| Luxembourg | +352 |
| Malaysia | +60 |
| Martinique | +596 |
| Mexico | +52 |
| Mozambique | +258 |
| Netherlands | +31 |
| New Zealand | +64 |
| Nicaragua | +505 |
| Nigeria | +234 |
| Norway | +47 |
| Oman | +968 |
| Pakistan | +92 |
| Panama | +507 |
| Paraguay | +595 |
| Peru | +51 |
| Philippines | +63 |
| Poland | +48 |
| Portugal | +351 |
| Romania | +40 |
| Russia | +7 |
| Rwanda | +250 |
| Réunion | +262 |
| Saudi Arabia (KSA) | +966 |
| Serbia | +381 |
| Singapore | +65 |
| Slovakia | +421 |
| Slovenia | +386 |
| South Africa | +27 |
| South Korea | +82 |
| Spain | +34 |
| Sweden | +46 |
| Switzerland | +41 |
| Taiwan | +886 |
| Thailand | +66 |
| U.S. Virgin Islands | +1340 |
| United Arab Emirates | +971 |
| United Kingdom | +44 |
| Uzbekistan | +998 |
| Vietnam | +84 |
| Zambia | +260 |

Telnyx continues to expand its global presence. While DID/numbers can be purchased from more countries than listed above, countries not listed only have inbound local calling guaranteed at this time, not outbound local calling. For other use cases, contact an Account Manager or Sales representative at [sales@telnyx.com](mailto:success@telnyx.com).

## N11 Codes (United States)

N11 codes provide three-digit dialing access to special services. In the United States, the FCC administers N11 codes and recognizes 211, 311, 511, 711, 811, and 911 as nationally assigned, while not disturbing other traditional uses.

| N11 Code | Description | Supported |
| --- | --- | --- |
| 211 | Community Information and Referral Services | No |
| 311 | Non-Emergency Police and Other Governmental Services | No |
| 411 | Local Directory Assistance | No |
| 511 | Traffic and Transportation Information (US); Provision of Weather and Traveller Information Services (Canada) | No |
| 611 | Repair Service |  |
| 711 | Telecommunications Relay Service (TRS) | Yes |
| 811 | Access to One Call Services to Protect Pipeline and Utilities from Excavation Damage (US) | Yes |
| 911 | Emergency | Yes |
| 988 (call and text) | National Suicide Prevention Lifeline | Yes |

Telnyx does not currently provide directory listing services.

For N11 outbound calls there are no caller ID (CLI) validations enforced, as Telnyx prioritizes connecting these calls. However, for 911, if an invalid CLI or a CLI without an emergency address is used, the call is classified as unregistered at a cost of $100 per call. Ensure you send valid caller IDs from numbers on your account that have emergency services enabled and with an address.
