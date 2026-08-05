---
title: Telnyx Voice API, TeXML, and Device Setup Guide
summary: A consolidated reference covering Telnyx account basics, Voice API and TeXML
  application configuration, debugging tools, conference calling, and step-by-step
  setup instructions for several SIP desk and conference phones.
sources:
- url: https://support.telnyx.com/en/articles/1130644-do-i-have-to-sign-a-contract
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
- url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
- url: https://support.telnyx.com/en/articles/5807663-panasonic-kx-tgp-550
- url: https://support.telnyx.com/en/articles/5807979-konftel-300wx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup
- url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
- url: https://support.telnyx.com/en/collections/133140-voice-api-essentials
- url: https://support.telnyx.com/en/collections/17907095-texml-tutorials
updated_at: 2026-08-05T13:29:28Z
---

# Telnyx Voice API, TeXML, and Device Setup Guide

*Part 1 of 3 — see also: [Part 2](telnyx-voice-api-texml-and-device-setup-guide--part-2.md), [Part 3](telnyx-voice-api-texml-and-device-setup-guide--part-3.md)*

A consolidated reference covering Telnyx account basics, Voice API and TeXML application configuration, debugging tools, conference calling, and step-by-step setup instructions for several SIP desk and conference phones.

## Account and Contract Basics

No contract is required to use Telnyx. You can open an account for free at any time and use it for as long as you want. Telnyx includes world-class support for all customers and does not add hidden fees. Support is available through the AI Assistant (24/7), the NOC team (24/7), the Porting team (9am–7pm CT, Monday–Friday), and the Numbering team (9am–5pm CT, Monday–Friday).

## Conference Calling

Telnyx supports conference calls through several options:

- **Voice API (recommended):** Build and control conference calls programmatically.
- **TeXML:** Create simple conference rooms using XML instructions.
- **SIP trunking:** Use Telnyx with PBX systems such as Asterisk or 3CX.
- **Video API:** Build audio/video conferencing applications.

For a simple setup, start with the TeXML `<Conference>` verb. For full control, use the Voice API Call Control commands. For a working example, follow the conferencing demo tutorial. See the [TeXML Conference documentation](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference), the [Voice API Conference commands](https://developers.telnyx.com/api-reference/conference-commands), and the [conferencing tutorial](https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo).

## TeXML and Voice API Compatibility

Avoid combining TeXML and Telnyx Voice API/Call Control commands in the same application. TeXML converts XML instructions into Voice API commands and tracks call state in the background; mixing the two products may work for simple cases but will eventually cause errors or confusing behavior. The same applies to AI Assistants, which use TeXML under the hood.

Common scenarios to avoid:

- Using `call_control_id` from a TeXML webhook to issue Voice API commands (for example, transfer, bridge, hangup).
- Calling `streaming_start` on a call that is already using the TeXML `<Stream>` verb.
- Mixing TeXML `<Dial>` with Voice API bridge commands on the same call.
- Issuing Call Control commands on AI Assistant calls.

If you need Call Control flexibility, use the Voice API from the start rather than TeXML. If you need both paradigms for different parts of your application, use separate connections — a TeXML Application for TeXML calls and a Voice API Application for Call Control calls. Note that TeXML webhooks use form-encoded parameters, while Voice API webhooks use JSON; if your application handles both, ensure your server can parse both formats correctly.

## TeXML Bin: Simple Voicemail and Call Forwarding

TeXML Bin lets you upload TeXML files to storage and use them for call flows without writing code. TeXML is an XML-based data structure that controls calls with Telnyx and is the quickest way to get started with Programmable Voice using a simple `.xml` file. The TeXML Translator starts at the top of your file and executes commands sequentially in the order they appear.

To create a simple voicemail and call forwarding application:

1. **Create your XML.** Use the TeXML editor in the Mission Control Portal under Programmable Voice > TeXML Bin.

   Simple voicemail:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <Response>
      <Say>Thank you for calling YYZ co. Please leave a message.</Say>
      <Record playBeep="true" finishOnKey="*9" />
   </Response>
   ```

   Simple call forward:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <Response>
      <Dial>
        <Sip>ext1@sip.xyzco.com</Sip>
        <Sip>ext3@sip.xyzco.com</Sip>
        <Sip>ext4@sip.xyzco.com</Sip>
      </Dial>
   </Response>
   ```

   ![Simple Voicemail](_images/25b2f5e401c4dbaf.png)

2. **Set up your XML application in Mission Control.** Select your script from the drop-down list when configuring the application.

   ![Editing your TeXML Application](_images/3cd347c0670319a7.png)

3. **Test your application.** Assign a phone number to the application, dial the number from the PSTN, leave a message, and retrieve your voicemail.

   ![Assigning a number to an application](_images/de9840c1d337d832.png)

   ![Retrieving your Voicemail](_images/0cc81ca6102ea818.png)

## Configuring Call Control and TeXML Applications

The Call Control / TeXML applications section is located in the Mission Control Portal under Voice > Programmable Voice. From there you can create Voice Apps (Call Control Voice API) and TeXML Apps.

### Voice App settings

- **Voice App Name:** Assign a name to manage the application.
- **AnchorSite® Selection:** "Latency" routes media through the site with the lowest round-trip time to the user's connection, calculated using ICMP ping messages. This can be disabled by specifying a site to handle all media.
- **Send a webhook to the URL:** Enter the URL where webhook events will be sent. You can also configure a fail-over URL that Telnyx will use if two consecutive delivery attempts to the primary URL fail. The URL must include a scheme such as `https`.
- **Use Webhook API version:** Choose V1 or V2. V2 is recommended because it contains a richer feature set and V1 will be deprecated.
- **Enable "hang-up" on timeout:** Specify the number of seconds Telnyx will wait for commands from your application before hanging up.
- **Custom webhook retry delay (seconds):** Specify a delay before retrying an unsuccessful webhook delivery. If not set, Telnyx retries immediately.
- **DTMF Type:** Choose RFC 2833 (default, preferred, not audible on the call), Inband (digits passed as normal audio tones), or SIP INFO (mainly used for SIP-to-SIP calls; type is negotiated between parties).
- **RTCP Capture:** Enable to build QoS Reports under Debugging > SIP Call Flow Tool.
- **Call Cost Webhook Event:** Enable to send the call cost webhook.

### Inbound settings

- **Subdomain:** Specify a subdomain that can be used to receive calls to a Connection from a SIP endpoint (for example, `example.sip.telnyx.com` can be called using `sip:@example.sip.telnyx.com`). Configure the SIP subdomain receive settings to allow calls from anyone or only from connections.
- **Inbound Channel Limit:** Limit the total number of inbound calls to phone numbers associated with this connection.
- **Enable Shaken/Stir headers:** Select yes to receive attestation information in webhooks for incoming calls.
- **Codecs:** Select the codecs Telnyx should offer on your calls. Force specific codecs by checking only one box.

### Outbound settings

- **Outbound Voice Profile:** Assign your application to an outbound voice profile to make outbound calls.
- **Outbound Channel Limit:** Limit the total number of outbound calls to phone numbers associated with this connection.

The application ID is shown in the application settings and is used to reference or trigger API calls programmatically.

### TeXML App settings

- **TeXML App Name:** Assign a name to manage the application.
- **Voice Method:** HTTP request method Telnyx uses to interact with your XML Translator webhooks (GET or POST).
- **Send a TeXML webhook to the URL:** Enter the URL where XML translator webhook events will be sent. You can also configure a fail-over URL.
- **Status Callback Method:** HTTP request method Telnyx uses when requesting the Status Callback URL.
- **Send information about call progress events to the URL:** Specify the URL for Telnyx to send call progress events.
- **Enable "hang-up" on timeout:** Specify the number of seconds to wait for the application before hanging up.
- **DTMF Type:** RFC 2833, Inband, or SIP INFO (same options as Voice Apps).
- **Call Cost Webhook Event:** Enable to send the call cost webhook.

Inbound and outbound settings for TeXML Apps mirror those for Voice Apps (subdomain, channel limits, Shaken/Stir headers, codecs, outbound voice profile, outbound channel limit).
