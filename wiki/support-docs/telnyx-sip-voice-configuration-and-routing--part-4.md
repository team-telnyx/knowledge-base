---
title: Telnyx SIP Voice Configuration and Routing
summary: This page consolidates Telnyx support guidance on SIP voice configuration,
  covering SRV record handling, call forwarding, external call transfers, SIP registration,
  post-dial delay, round-robin routing, and the role of Via and Record-Route headers
  in successful call setup.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
- url: https://support.telnyx.com/en/articles/1130657-call-forwarding
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
- url: https://support.telnyx.com/en/articles/4453840-post-dial-delay-pdd
- url: https://support.telnyx.com/en/articles/8174793-round-robin-routing
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
updated_at: 2026-08-05T13:25:14Z
---

# Telnyx SIP Voice Configuration and Routing

*Part 4 of 4 — see also: [Part 1](telnyx-sip-voice-configuration-and-routing--part-1.md), [Part 2](telnyx-sip-voice-configuration-and-routing--part-2.md), [Part 3](telnyx-sip-voice-configuration-and-routing--part-3.md)*

This page consolidates Telnyx support guidance on SIP voice configuration, covering SRV record handling, call forwarding, external call transfers, SIP registration, post-dial delay, round-robin routing, and the role of Via and Record-Route headers in successful call setup.

## Telnyx + Vapi Integration

Vapi can be integrated with Telnyx in two ways: importing an existing Telnyx number into Vapi (recommended for most customers) or using a BYO Telnyx SIP trunk (for custom SIP routing, SIP trunk credentials, or advanced inbound/outbound SIP configuration). This article covers using a Telnyx number with Vapi, not importing a Vapi assistant into Telnyx AI Assistants.

Prerequisites include an active Telnyx account, an active Vapi account, a Telnyx phone number with voice capability, a Vapi assistant or squad, a dedicated Telnyx API v2 key for Vapi, and (for outbound calls) a Telnyx Outbound Voice Profile with the required destinations enabled. Some outbound destinations may require Level 2 verification or additional account approval.

To set up the integration:

1. Create or choose a Vapi assistant, configuring at minimum the name, first message or greeting, instructions or system prompt, voice and model settings, and any required tools, webhooks, or transfer behavior.
2. Purchase or choose a Telnyx number in the Mission Control Portal under Numbers, and copy it in E.164 format (e.g. `+15551234567`).
3. Create a dedicated Telnyx API v2 key named clearly (e.g. "Vapi integration"), store it only in Vapi, never include it in screenshots, support tickets, shared documents, or chat messages, rotate it if exposed, and delete it when no longer used.
4. In the Vapi dashboard, go to Phone Numbers, click Create, select Telnyx, enter the Telnyx number details, paste the dedicated Telnyx API key, save, and assign the correct assistant or squad to the number's inbound settings. Inbound calls should then route to the assigned Vapi assistant.
5. For outbound calling, in the Telnyx Mission Control Portal go to Voice > Outbound Voice Profiles, create or edit a profile, enable the required countries or destinations, add Vapi as a connection under Connections and Applications, and save.

Outbound calls may fail if the destination country is not enabled, the destination requires verification that has not been completed, Vapi is not attached to the correct Outbound Voice Profile, or the caller ID is not valid or allowed for the attempted destination.

Test inbound calls by calling the Telnyx number and confirming the Vapi assistant answers with the correct greeting and behavior; check Vapi call logs if the call does not reach the assistant. Test outbound calls by starting an outbound call from Vapi using the imported Telnyx number to a destination in a country enabled in the Outbound Voice Profile, and confirm the call connects. If it fails, check Telnyx destination permissions, verification status, caller ID, and Voice Profile assignment.

The BYO Telnyx SIP trunk option is for when the imported-number flow does not meet routing requirements. At a high level: retrieve the Vapi private key, create or select a Telnyx SIP trunk, configure Telnyx inbound SIP routing to Vapi, assign the Telnyx phone number to the SIP trunk, set the number's translated number to the Vapi SIP URI (e.g. `sip:<unique-id>@sip.vapi.ai`), create outbound SIP credentials in Telnyx if Vapi will place outbound calls through the trunk, create or update a Telnyx Outbound Voice Profile, attach the Telnyx SIP trunk to that profile, create the BYO SIP trunk credential in Vapi, add the phone number to Vapi using the SIP trunk credential, and assign the assistant for inbound and outbound handling. For Vapi BYO SIP trunk gateway configuration, use IP addresses for inbound-enabled gateways; do not use `sip.telnyx.com` as the gateway value when inbound is enabled.

Common troubleshooting scenarios:

- **Vapi cannot import the Telnyx number**: Confirm the number belongs to your Telnyx account, is active, is voice-capable, and is entered in E.164 format. Confirm the Telnyx API key is current and copied correctly.
- **Inbound calls do not reach Vapi**: Confirm the number appears in Vapi and has the correct assistant or squad assigned. If using SIP trunking, confirm the Telnyx number is assigned to the trunk and the translated number matches the Vapi SIP URI.
- **Vapi assistant does not answer**: Check the phone number's inbound settings in Vapi. Confirm the assistant is published/configured correctly and review Vapi call logs.
- **Outbound calls fail**: Confirm the Telnyx Outbound Voice Profile has the destination enabled and that Vapi or the SIP trunk is attached to the profile. Check whether the destination requires Level 2 verification.
- **Outbound fails only for some countries**: Check Telnyx destination permissions, account verification, and any regional restrictions in the Outbound Voice Profile.
- **Caller ID is wrong or rejected**: Confirm the Telnyx number or verified caller ID is allowed for outbound use. Transfer scenarios may require additional caller ID configuration.
- **SIP credential or gateway errors**: Use IP addresses for inbound-enabled Vapi gateways. Confirm SIP credentials are correct and any required IP allowlists include Vapi's SIP signaling IPs.

When contacting [support@telnyx.com](mailto:support@telnyx.com), include the Telnyx phone number involved, whether the imported-number flow or BYO SIP trunk flow was used, call direction (inbound or outbound), source and destination numbers, approximate timestamp and timezone, Vapi call ID if available, Telnyx CDR, SIP Call-ID, or call details if available, and screenshots of non-sensitive configuration pages. Do not include API keys, SIP passwords, Vapi private keys, or other secrets.
