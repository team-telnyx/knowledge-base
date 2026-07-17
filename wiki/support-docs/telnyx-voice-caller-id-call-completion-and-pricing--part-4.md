---
title: 'Telnyx Voice: Caller ID, Call Completion, and Pricing'
summary: A consolidated reference for Telnyx voice services covering Caller ID Number
  (CID) and Caller ID Name (CNAM) configuration, the Caller ID Number Policy, pricing
  and billing, LRN and number lookup, US local and rural call completion, PSTN replacement
  and local calling, and troubleshooting inbound and outbound call failures.
sources:
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/articles/2185372-where-can-i-see-pricing-options
- url: https://support.telnyx.com/en/articles/3317613-billing-decimal-values-considered
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- url: https://support.telnyx.com/en/articles/4096828-us-rural-call-completion
- url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
- url: https://support.telnyx.com/en/articles/6622229-pstn-replacement-local-calling-with-telnyx
updated_at: 2026-07-17T09:05:14Z
---

# Telnyx Voice: Caller ID, Call Completion, and Pricing

*Part 4 of 5 — see also: [Part 1](telnyx-voice-caller-id-call-completion-and-pricing--part-1.md), [Part 2](telnyx-voice-caller-id-call-completion-and-pricing--part-2.md), [Part 3](telnyx-voice-caller-id-call-completion-and-pricing--part-3.md), [Part 5](telnyx-voice-caller-id-call-completion-and-pricing--part-5.md)*

A consolidated reference for Telnyx voice services covering Caller ID Number (CID) and Caller ID Name (CNAM) configuration, the Caller ID Number Policy, pricing and billing, LRN and number lookup, US local and rural call completion, PSTN replacement and local calling, and troubleshooting inbound and outbound call failures.

## PSTN Replacement and Local Calling

A call is considered **local** when the caller's number (CLI) and the destination number (CLD) belong to the same country — for example, a UK number calling another UK number. Local calls cannot enter a country through international exchanges; if a business tries to make a local-looking call using standard international routing, downstream carriers in that country will block or reject it, resulting in failed calls, SIP 503 errors, and poor call completion rates.

Telnyx solves this by routing calls directly through **Tier-1 carrier partners within each country**, bypassing international exchanges entirely:

1. The caller originates a call from anywhere in the world.
2. The call arrives at the Telnyx network.
3. Telnyx identifies the destination country and routes the call via its direct in-country Tier-1 carrier interconnect.
4. The call is delivered locally — the callee sees a local number and receives the call as if it originated from within their country.

Key benefits:

- **Higher call completion rates** — calls are no longer blocked at international exchanges.
- **Local caller ID delivered correctly** — the callee sees a local number, not an international one.
- **Establish local presence** — build customer trust by appearing local in every market.
- **No extra charges or configuration** — the feature is built into your Telnyx-issued local number.

### Requirements

There are no additional fees or complex setup steps. You need a Telnyx number with the **Local Calling** feature enabled:

1. Log in to the [Telnyx Portal](https://portal.telnyx.com).
2. Navigate to **Numbers → Buy numbers**.
3. Select the destination country.
4. Filter results by the **Local Calling** feature.
5. Choose a number and complete the purchase.

Alternatively, email [numbering@telnyx.com](mailto:numbering@telnyx.com) to request a number, or port your existing number to Telnyx. Use the same number as CLI on outbound calls.

### Without the Local Calling Feature

If you cannot purchase a Telnyx local number, it is recommended to use a CLI from a different country than the destination. Calls with a matching foreign CLI are the most likely to be blocked. If you use a non-Telnyx number from the same locale as the destination, the call will not be accepted (outside of the US/CAN).

If call forwarding is enabled on a local number, local calling may not complete successfully if the caller's CLI matches the forwarded destination number. Telnyx can only guarantee local call completion when the originating number is used as the CLI.

### Supported Countries

Telnyx supports local calling for the following countries (country codes in parentheses):

Albania (+355), Argentina (+54), Australia (+61), Austria (+43), Bahrain (+973), Bangladesh (+88), Belgium (+32), Belize (+501), Benin (+229), Bolivia (+591), Bosnia and Herzegovina (+387), Brazil (+55), Bulgaria (+359), Cameroon (+237), Chile (+56), China (+86), Colombia (+57), Costa Rica (+506), Croatia (+385), Cyprus (+357), Czech Republic (+420), Democratic Republic of the Congo (+243), Denmark (+45), Dominican Republic (+1829), El Salvador (+503), Estonia (+372), Ecuador (+593), Finland (+358), France (+33), French Guiana (+594), Georgia (+995), Germany (+49), Ghana (+233), Greece (+30), Guadeloupe (+590), Guatemala (+502), Honduras (+504), Hong Kong (+852), Hungary (+36), Indonesia (+62), Ireland (+353), Israel (+972), Italy (+39), Japan (+81), Kenya (+254), Latvia (+371), Lithuania (+370), Luxembourg (+352), Malaysia (+60), Martinique (+596), Mexico (+52), Mozambique (+258), Netherlands (+31), New Zealand (+64), Nicaragua (+505), Nigeria (+234), Norway (+47), Oman (+968), Pakistan (+92), Panama (+507), Paraguay (+595), Peru (+51), Philippines (+63), Poland (+48), Portugal (+351), Romania (+40), Russia (+7), Rwanda (+250), Réunion (+262), Saudi Arabia (+966), Serbia (+381), Singapore (+65), Slovakia (+421), Slovenia (+386), South Africa (+27), South Korea (+82), Spain (+34), Sweden (+46), Switzerland (+41), Taiwan (+886), Thailand (+66), U.S. Virgin Islands (+1340), United Arab Emirates (+971), United Kingdom (+44), Uzbekistan (+998), Vietnam (+84), Zambia (+260).

Telnyx continues to expand its global presence. While DID/numbers can be purchased from more countries than listed, countries not listed only have inbound local calling guaranteed at this time, not outbound local calling. Contact [sales@telnyx.com](mailto:sales@telnyx.com) to discuss specific requirements.
