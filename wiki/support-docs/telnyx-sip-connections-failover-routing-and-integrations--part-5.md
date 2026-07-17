---
title: 'Telnyx SIP Connections: Failover, Routing, and Integrations'
summary: This page consolidates Telnyx SIP Connection configuration, failover, and
  retry behavior across IP/FQDN-based, credential-based, and UAC (SIP Attach) connection
  types. It covers AnchorSite® media routing, DID assignment, the Telnyx + Vapi integration
  (imported-number and BYO SIP trunk flows), and PBX setup guides for Bicom PBXware
  and sipXecs.
sources:
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
- url: https://support.telnyx.com/en/articles/6128008-sipxecs-pbx-setup-config
updated_at: 2026-07-17T09:07:44Z
---

# Telnyx SIP Connections: Failover, Routing, and Integrations

*Part 5 of 7 — see also: [Part 1](telnyx-sip-connections-failover-routing-and-integrations--part-1.md), [Part 2](telnyx-sip-connections-failover-routing-and-integrations--part-2.md), [Part 3](telnyx-sip-connections-failover-routing-and-integrations--part-3.md), [Part 4](telnyx-sip-connections-failover-routing-and-integrations--part-4.md), [Part 6](telnyx-sip-connections-failover-routing-and-integrations--part-6.md), [Part 7](telnyx-sip-connections-failover-routing-and-integrations--part-7.md)*

This page consolidates Telnyx SIP Connection configuration, failover, and retry behavior across IP/FQDN-based, credential-based, and UAC (SIP Attach) connection types. It covers AnchorSite® media routing, DID assignment, the Telnyx + Vapi integration (imported-number and BYO SIP trunk flows), and PBX setup guides for Bicom PBXware and sipXecs.

## Telnyx + Vapi Integration

Use this guide to connect a Telnyx phone number to Vapi so your Vapi assistant can receive inbound calls and, if needed, place outbound calls through Telnyx. This article is for using a Telnyx number with Vapi; it is not for importing a Vapi assistant into Telnyx AI Assistants.

### Overview

There are two supported setup paths:

1. **Import an existing Telnyx number into Vapi** — Recommended for most customers. You keep the number in Telnyx and add it to Vapi from the Vapi dashboard.
2. **Use a BYO Telnyx SIP trunk with Vapi** — Use this only when you need custom SIP routing, SIP trunk credentials, or advanced inbound/outbound SIP configuration.

If you are not sure which option to use, start with the imported-number flow.

### Prerequisites

- An active Telnyx account
- An active Vapi account
- A Telnyx phone number with voice capability
- A Vapi assistant or squad ready to handle calls
- A dedicated Telnyx API v2 key for Vapi
- For outbound calls: a Telnyx Outbound Voice Profile with the destinations you plan to call enabled

Some Telnyx outbound destinations may require Level 2 verification or additional account approval before they can be activated.

### Step 1 — Create or Choose Your Vapi Assistant

In Vapi, create a new assistant or select an existing one. At minimum, configure:

- Assistant name
- First message or greeting
- Assistant instructions or system prompt
- Voice and model settings
- Any tools, webhooks, or transfer behavior required for your use case

See Vapi's phone quickstart at [https://docs.vapi.ai/quickstart/phone](https://docs.vapi.ai/quickstart/phone).

### Step 2 — Purchase or Choose a Telnyx Number

In the Telnyx Mission Control Portal:

1. Go to **Numbers**.
2. Purchase a voice-capable phone number, or choose an existing Telnyx number.
3. Copy the number in E.164 format (e.g., `+15551234567`).

### Step 3 — Create a Dedicated Telnyx API Key

Create a dedicated Telnyx API v2 key for this integration. Recommended practices:

- Name the key clearly (e.g., "Vapi integration").
- Store the key only in Vapi.
- Do not include API keys in screenshots, support tickets, shared documents, or chat messages.
- Rotate the key if it is exposed.
- Delete the key if the integration is no longer used.

See Telnyx API key guidance at [https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them](https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them).

### Step 4 — Import Your Telnyx Number into Vapi

In the Vapi dashboard:

1. Go to **Phone Numbers**.
2. Click **Create** or **Create a Phone Number**.
3. Select **Telnyx**.
4. Enter the Telnyx number details requested by Vapi.
5. Paste the dedicated Telnyx API key.
6. Save the phone number.
7. Assign the correct assistant or squad to the number's inbound settings.

Once saved, inbound calls to the Telnyx number should route to the assigned Vapi assistant. See Vapi's Telnyx import guide at [https://docs.vapi.ai/telnyx](https://docs.vapi.ai/telnyx).

### Step 5 — Enable Outbound Calling Through Telnyx

Skip this section if your assistant only needs to receive inbound calls.

1. Log in to the Telnyx Mission Control Portal.
2. Go to **Voice → Outbound Voice Profiles**.
3. Create a new Outbound Voice Profile or edit an existing one.
4. Enable the countries or destinations your assistant needs to call.
5. Under **Connections and Applications**, add **Vapi** as a connection.
6. Save the profile.

Outbound calls may fail if:

- The destination country is not enabled.
- The destination requires verification that has not been completed.
- Vapi is not attached to the correct Outbound Voice Profile.
- The caller ID is not valid or allowed for the attempted destination.

See Telnyx Outbound Voice Profile docs at [https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles/index](https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles/index).

### Step 6 — Test the Integration

**Test inbound calls:**

1. Call the Telnyx number.
2. Confirm the Vapi assistant answers.
3. Confirm the greeting and assistant behavior are correct.
4. Check Vapi call logs if the call does not reach the assistant.

**Test outbound calls:**

1. Start an outbound call from Vapi using the imported Telnyx number.
2. Use a destination in a country enabled in the Telnyx Outbound Voice Profile.
3. Confirm the call connects.
4. If the call fails, check Telnyx destination permissions, verification status, caller ID, and Voice Profile assignment.

### Advanced Option: BYO Telnyx SIP Trunk

Use this option only if the standard imported-number flow does not meet your routing requirements. At a high level, the SIP trunk setup requires you to:

1. Retrieve your Vapi private key.
2. Create or select a Telnyx SIP trunk.
3. Configure Telnyx inbound SIP routing to Vapi.
4. Assign the Telnyx phone number to the SIP trunk.
5. Set the Telnyx number's translated number to the Vapi SIP URI, such as `sip:<unique-id>@sip.vapi.ai`.
6. Create outbound SIP credentials in Telnyx if Vapi will place outbound calls through the trunk.
7. Create or update a Telnyx Outbound Voice Profile.
8. Attach the Telnyx SIP trunk to that Outbound Voice Profile.
9. Create the BYO SIP trunk credential in Vapi.
10. Add the phone number to Vapi using the SIP trunk credential.
11. Assign the assistant for inbound and outbound handling.

> **Important:** For Vapi BYO SIP trunk gateway configuration, use IP addresses for inbound-enabled gateways. Do not use `sip.telnyx.com` as the gateway value when inbound is enabled.

See Vapi's Telnyx SIP guide at [https://docs.vapi.ai/advanced/sip/telnyx](https://docs.vapi.ai/advanced/sip/telnyx) and SIP credential troubleshooting at [https://docs.vapi.ai/advanced/sip/troubleshoot-sip-trunk-credential-errors](https://docs.vapi.ai/advanced/sip/troubleshoot-sip-trunk-credential-errors).

### Vapi Integration Troubleshooting

- **Vapi cannot import the Telnyx number:** Confirm the number belongs to your Telnyx account, is active, is voice-capable, and is entered in E.164 format. Confirm the Telnyx API key is current and copied correctly.
- **Inbound calls do not reach Vapi:** Confirm the number appears in Vapi and has the correct assistant or squad assigned. If using SIP trunking, confirm the Telnyx number is assigned to the trunk and the translated number matches the Vapi SIP URI.
- **Vapi assistant does not answer:** Check the phone number's inbound settings in Vapi. Confirm the assistant is published/configured correctly and review Vapi call logs.
- **Outbound calls fail:** Confirm the Telnyx Outbound Voice Profile has the destination enabled and that Vapi or the SIP trunk is attached to the profile. Check whether the destination requires Level 2 verification.
- **Outbound fails only for some countries:** Check Telnyx destination permissions, account verification, and any regional restrictions in the Outbound Voice Profile.
- **Caller ID is wrong or rejected:** Confirm the Telnyx number or verified caller ID is allowed for outbound use. Transfer scenarios may require additional caller ID configuration.
- **SIP credential or gateway errors:** Use IP addresses for inbound-enabled Vapi gateways. Confirm SIP credentials are correct and any required IP allowlists include Vapi's SIP signaling IPs.

When contacting Telnyx Support at [support@telnyx.com](mailto:support@telnyx.com), include:

- Telnyx phone number involved
- Whether you used the imported-number flow or BYO SIP trunk flow
- Call direction: inbound or outbound
- Source number and destination number
- Approximate timestamp and timezone
- Vapi call ID, if available
- Telnyx CDR, SIP Call-ID, or call details, if available
- Screenshots of non-sensitive configuration pages

Do not include API keys, SIP passwords, Vapi private keys, or other secrets.
