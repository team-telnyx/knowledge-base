---
source_url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
title: "Telnyx + Vapi Integration"
description: "Below we'll cover the entire integration between us and… See Telnyx guidance and requirements Learn more about Telnyx + Vapi Integration with Telnyx."
scraped: 2026-07-08
content_hash: 18362aba0f282afd4294867cb422064635c4ecd06134ed782340becfcfe46cac
---







# Telnyx + Vapi Integration

Below we'll cover the entire integration between us and… See Telnyx guidance and requirements Learn more about Telnyx + Vapi Integration with Telnyx.

Z




## **Telnyx + Vapi Integration**

Use this guide to connect a Telnyx phone number to Vapi so your Vapi assistant can receive inbound calls and, if needed, place outbound calls through Telnyx.

This article is for using a Telnyx number with Vapi. It is not for importing a Vapi assistant into Telnyx AI Assistants.

## **Overview**

There are two supported setup paths:

1. **Import an existing Telnyx number into Vapi**
   Recommended for most customers. You keep the number in Telnyx and add it to Vapi from the Vapi dashboard.
2. **Use a BYO Telnyx SIP trunk with Vapi**
   Use this only when you need custom SIP routing, SIP trunk credentials, or advanced inbound/outbound SIP configuration.

If you are not sure which option to use, start with the imported-number flow.

## **Prerequisites**

Before you begin, make sure you have:

* An active Telnyx account.
* An active Vapi account.
* A Telnyx phone number with voice capability.
* A Vapi assistant or squad ready to handle calls.
* A dedicated Telnyx API v2 key for Vapi.
* For outbound calls: a Telnyx Outbound Voice Profile with the destinations you plan to call enabled.

Some Telnyx outbound destinations may require Level 2 verification or additional account approval before they can be activated.

## **1. Create or choose your Vapi assistant**

In Vapi, create a new assistant or select an existing one.

At minimum, configure:

* Assistant name.
* First message or greeting.
* Assistant instructions or system prompt.
* Voice and model settings.
* Any tools, webhooks, or transfer behavior required for your use case.

Vapi’s phone quickstart is available here: **<https://docs.vapi.ai/quickstart/phone>**

## **2. Purchase or choose a Telnyx number**

In the Telnyx Mission Control Portal:

1. Go to **Numbers**.
2. Purchase a voice-capable phone number, or choose an existing Telnyx number.
3. Copy the number in E.164 format, for example +15551234567.

## **3. Create a dedicated Telnyx API key**

Create a dedicated Telnyx API v2 key for this integration.

Recommended practices:

* Name the key clearly, for example Vapi integration.
* Store the key only in Vapi.
* Do not include API keys in screenshots, support tickets, shared documents, or chat messages.
* Rotate the key if it is exposed.
* Delete the key if the integration is no longer used.
* Telnyx API key guidance:
  ​**<https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them>**

## **4. Import your Telnyx number into Vapi**

In the Vapi dashboard:

1. Go to **Phone Numbers**.
2. Click **Create** or **Create a Phone Number**.
3. Select **Telnyx**.
4. Enter the Telnyx number details requested by Vapi.
5. Paste the dedicated Telnyx API key.
6. Save the phone number.
7. Assign the correct assistant or squad to the number’s inbound settings.

Once saved, inbound calls to the Telnyx number should route to the assigned Vapi assistant.

Vapi’s Telnyx import guide:
​



**<https://docs.vapi.ai/telnyx>**

## **5. Enable outbound calling through Telnyx**

Skip this section if your assistant only needs to receive inbound calls.

To enable outbound calling:

1. Log in to the Telnyx Mission Control Portal.
2. Go to **Voice > Outbound Voice Profiles**.
3. Create a new Outbound Voice Profile or edit an existing one.
4. Enable the countries or destinations your assistant needs to call.
5. Under **Connections and Applications**, add **Vapi** as a connection.
6. Save the profile.

Outbound calls may fail if:

* The destination country is not enabled.
* The destination requires verification that has not been completed.
* Vapi is not attached to the correct Outbound Voice Profile.
* The caller ID is not valid or allowed for the attempted destination.

Telnyx Outbound Voice Profile docs: **<https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles/index>**

## **6. Test the integration**

## **Test inbound calls**

1. Call the Telnyx number.
2. Confirm the Vapi assistant answers.
3. Confirm the greeting and assistant behavior are correct.
4. Check Vapi call logs if the call does not reach the assistant.

## **Test outbound calls**

1. Start an outbound call from Vapi using the imported Telnyx number.
2. Use a destination in a country enabled in the Telnyx Outbound Voice Profile.
3. Confirm the call connects.
4. If the call fails, check Telnyx destination permissions, verification status, caller ID, and Voice Profile assignment.

## **Advanced option: BYO Telnyx SIP trunk**

Use this option only if the standard imported-number flow does not meet your routing requirements.

At a high level, the SIP trunk setup requires you to:

1. Retrieve your Vapi private key.
2. Create or select a Telnyx SIP trunk.
3. Configure Telnyx inbound SIP routing to Vapi.
4. Assign the Telnyx phone number to the SIP trunk.
5. Set the Telnyx number’s translated number to the Vapi SIP URI, such as sip:<unique-id>@sip.vapi.ai.
6. Create outbound SIP credentials in Telnyx if Vapi will place outbound calls through the trunk.
7. Create or update a Telnyx Outbound Voice Profile.
8. Attach the Telnyx SIP trunk to that Outbound Voice Profile.
9. Create the BYO SIP trunk credential in Vapi.

1. Add the phone number to Vapi using the SIP trunk credential.
2. Assign the assistant for inbound and outbound handling.

Important: for Vapi BYO SIP trunk gateway configuration, use IP addresses for inbound-enabled gateways. Do not use sip.telnyx.com as the gateway value when inbound is enabled.

* Vapi’s Telnyx SIP guide: **<https://docs.vapi.ai/advanced/sip/telnyx>**
* Vapi SIP credential troubleshooting: **<https://docs.vapi.ai/advanced/sip/troubleshoot-sip-trunk-credential-errors>**

## **Troubleshooting**

|  |  |
| --- | --- |
| **Issue** | **What to check** |
| Vapi cannot import the Telnyx number | Confirm the number belongs to your Telnyx account, is active, is voice-capable, and is entered in E.164 format. Confirm the Telnyx API key is current and copied correctly. |
| Inbound calls do not reach Vapi | Confirm the number appears in Vapi and has the correct assistant or squad assigned. If using SIP trunking, confirm the Telnyx number is assigned to the trunk and the translated number matches the Vapi SIP URI. |
| Vapi assistant does not answer | Check the phone number’s inbound settings in Vapi. Confirm the assistant is published/configured correctly and review Vapi call logs. |
| Outbound calls fail | Confirm the Telnyx Outbound Voice Profile has the destination enabled and that Vapi or the SIP trunk is attached to the profile. Check whether the destination requires Level 2 verification. |
| Outbound fails only for some countries | Check Telnyx destination permissions, account verification, and any regional restrictions in the Outbound Voice Profile. |
| Caller ID is wrong or rejected | Confirm the Telnyx number or verified caller ID is allowed for outbound use. Transfer scenarios may require additional caller ID configuration. |
| SIP credential or gateway errors | Use IP addresses for inbound-enabled Vapi gateways. Confirm SIP credentials are correct and any required IP allowlists include Vapi’s SIP signaling IPs. |

## **Information to include when contacting Telnyx Support at** [support@telnyx.com](mailto:support@telnyx.com).

If the issue is not resolved, contact support with:

* Telnyx phone number involved.
* Whether you used the imported-number flow or BYO SIP trunk flow.
* Call direction: inbound or outbound.
* Source number and destination number.
* Approximate timestamp and timezone.
* Vapi call ID, if available.
* Telnyx CDR, SIP Call-ID, or call details, if available.
* Screenshots of non-sensitive configuration pages.

Do not include API keys, SIP passwords, Vapi private keys, or other secrets.

## **Related resources**

* Vapi: Import number from Telnyx — **<https://docs.vapi.ai/telnyx>**
* Vapi: Phone calls quickstart — **<https://docs.vapi.ai/quickstart/phone>**
* Vapi: Telnyx SIP integration — **<https://docs.vapi.ai/advanced/sip/telnyx>**
* Vapi: SIP trunk credential troubleshooting - **<https://docs.vapi.ai/advanced/sip/troubleshoot-sip-trunk-credential-errors>**
* Telnyx: Outbound Voice Profiles **<https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles/index>**
* Telnyx: API keys — **<https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them>**

---

Related Articles

[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[Yeastar S-Series: Telnyx SIP](https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip)[PBXes: Connecting a PBXes Trunk to Telnyx](https://support.telnyx.com/en/articles/5798240-pbxes-connecting-a-pbxes-trunk-to-telnyx)[BYOC: Telnyx & Genesys](https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys)[How External Call Transfers Work](https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work)

Did this answer your question?

😞😐😃
