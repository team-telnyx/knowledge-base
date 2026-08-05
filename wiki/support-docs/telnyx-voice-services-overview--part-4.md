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

*Part 4 of 5 — see also: [Part 1](telnyx-voice-services-overview--part-1.md), [Part 2](telnyx-voice-services-overview--part-2.md), [Part 3](telnyx-voice-services-overview--part-3.md), [Part 5](telnyx-voice-services-overview--part-5.md)*

This page consolidates Telnyx support documentation covering company locations, voice termination coverage, call completion (local and rural), rate sheets and LRN-based pricing, N11 and emergency dialing, inbound call screening, and PSTN replacement / local calling features.

## Dialing Emergency Services

Telnyx offers PSTN replacement for several countries, including the ability to dial emergency services in each. The complete global coverage Telnyx supports is available at the [Telnyx global coverage page](https://telnyx.com/global-coverage). The complete list of [Supported Emergency Numbers](supported-emergency-numbers.md) is also available.

### How Telnyx decides which country to dial

A SIP connection on your account can use several numbers for both inbound and outbound calls. When one connection carries numbers from different countries, Telnyx uses the caller ID of each call to determine which emergency number to dial. For example, dialing 911 with a Canadian caller ID routes the call to Canada, while dialing 911 with a Mexican caller ID routes the call to Mexico.

This allows a single connection to host numbers from many countries while still reaching each country's emergency services. The "Localization Settings" in the outbound section of SIP connection settings do not affect emergency dialing — they apply only to normal local calling.

### Number format for emergency dialing

Emergency service numbers are local numbers intended only for in-country dialing and do not support +E.164 or E.164 international formats. Always dial the local emergency number by itself, without a + sign or country code. Telnyx returns an invalid number error if the proper format is not used. For example, dialing +1911 or 1911 will fail; the correct format is just 911. A tech prefix can be used so long as nothing else is included — for example, with tech prefix 1234, dial 1234911.

### Registering an emergency address

In some countries, calling emergency services from a number without a registered Emergency Service Address can result in fines. In the US, the fine is $100 per call. Register an address for emergency services on all numbers used to dial emergency services. Per regulation, Telnyx always allows calls to emergency services regardless of whether the caller ID has a registered address. For security reasons, dialing to emergency numbers cannot be disabled.

## Supported Emergency Numbers

The complete list of emergency numbers supported by Telnyx's platform is provided in [Supported Emergency Numbers](supported-emergency-numbers.md). For the correct dialing format, see [Dialing Emergency Services](dialing-emergency-services.md).

## Emergency Services and IPND in Australia

### Dialing 000

The general emergency service number in Australia is "000". Emergency calls can be made without charge, whether the service is active, suspended, disconnected, or out of credit for a pre-paid service. When a person calls "000" they speak to a Telstra 000 Emergency Call Service Operator first, who transfers the call to the required Emergency Service Organisation (ESO) — Police, Fire, or Ambulance. The emergency response is provided by the requested ESO.

"000" can be called regardless of whether the mobile service is prepaid or postpaid. Prepaid services do not require credit to call "000". Even if the mobile account is inactive, disconnected, blocked, suspended, or there is no SIM in the phone, "000" can still be called. More information is available at [www.triplezero.gov.au](http://www.triplezero.gov.au).

### Dialing 112

"112" is a globally recognized Emergency Service Number (ESN) for mobile phones and is Australia's secondary ESN. It can be dialed from mobile phones in Australia and around the world with the same functionality as "000". Mobile phones sold in Australia since 2002 recognize "000" as the ESN. International mobile roamers visiting Australia, or users of mobile phones purchased overseas, can call either "000" or "112".

### Integrated Public Number Database (IPND)

Telnyx uploads customer name, address, and telephone numbers to the Integrated Public Number Database (IPND). The IPND serves as a repository of Public Number Customer Data (PNCD), broadly including telephone number, name, service address, and Directory Related Services information, used to assist in the provision of emergency services and law enforcement.

Data Users with access to PNCD include (but are not limited to) Directory Related Service Providers, Emergency Call Service Operators, and Enforcement Agencies. Because contact data is used in emergency cases, it is important to keep Telnyx updated with any changes so the IPND can be updated accordingly. For example, if the service address changes, contact Telnyx support to update the IPND so the new address can be used in case of emergency dispatches.

If the address provided is not the physical address from which calls are made, contact Telnyx support with the appropriate contact name and telephone number. To view the state of a phone number in IPND, update a phone number in IPND, or opt out of directory listings, contact [support@telnyx.com](mailto:support@telnyx.com) or use the chat function.
