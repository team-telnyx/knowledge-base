---
title: Telnyx Programmable Voice
summary: 'Telnyx Programmable Voice provides multiple paradigms for building voice
  applications: the Voice API (Call Control) for programmatic call management, TeXML
  for XML-driven call flows, and AI Assistants for no-code conversational AI. This
  page covers configuration, compatibility, real-time transcription, third-party integrations,
  and migration guidance.'
sources:
- url: https://support.telnyx.com/en/articles/12232444-comprehensive-ai-assistants-configuration-walk-through
  content_hash: 8ad66d6c9ea440951f259f45a6639b7abdbc3762c8808b57774d2fe4d60f2783
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
  content_hash: 79afc77e4a975867133c6229080f1870df4e29203581a2478b9a3fc0d2156692
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
  content_hash: 796dc56257808f5e02f4e076a2b65788bfa9d791ab06a565014e8c8345ef7344
- url: https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx
  content_hash: d3098961d17ae5558a906b63a69ef91d005647ce75cf01b844d239258b3718c7
- url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
  content_hash: b446fc44af8df4f3f3b7050ef415b1fadccc6aa4e17e7af6463f1d2c863bfde2
- url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
  content_hash: 7f026b4e298be9c1cdbc1d17345b7f469b7d6c5245fb4dc81a485ebb089163d8
- url: https://support.telnyx.com/en/articles/8292490-real-time-transcription
  content_hash: 76a7beabc40726462c19c585a7ec962f8b56840817ff7da0a189c6186943a562
- url: https://support.telnyx.com/en/articles/9413928-telnyx-flow
  content_hash: 61bba2d7c7e49fcb586998819a9bd3107405f5a685d462e3cc484f5efe30ad1f
- url: https://support.telnyx.com/en/collections/133140-voice-api-essentials
  content_hash: b11a5bdfb665e039b8a9927cebf7acbfdb5f7c8a5f1fd43631989d2e8b27a947
- url: https://support.telnyx.com/en/collections/17907095-texml-tutorials
  content_hash: 95152862fbcb84bca63783a9ab66c43f144b2976be4888290a32c7a9b312d6d9
- url: https://support.telnyx.com/en/collections/9526270-telnyx-flow
  content_hash: da5c6979781c13f828bafee007d84d826b44739ecd4cba8ef4c0f7f8c1efbc0b
updated_at: 2026-06-11T11:40:11Z
---

# Telnyx Programmable Voice

*Part 1 of 3 — see also: [Part 2](telnyx-programmable-voice--part-2.md), [Part 3](telnyx-programmable-voice--part-3.md)*

Telnyx Programmable Voice provides multiple paradigms for building voice applications: the Voice API (Call Control) for programmatic call management, TeXML for XML-driven call flows, and AI Assistants for no-code conversational AI. This page covers configuration, compatibility, real-time transcription, third-party integrations, and migration guidance.

## Voice API (Call Control) Applications

Voice API applications — also called Call Control applications — are managed in the Mission Control Portal under **Voice > Programmable Voice**. They provide full programmatic control over calls via Telnyx API commands.

### Core settings

- **Voice App Name**: Assign a descriptive name when creating a new application.
- **AnchorSite® Selection**: Controls media routing. "Latency" mode routes media through the site with the lowest round-trip time (measured via ICMP ping). You can disable this by specifying a fixed site.
- **Webhook URL**: The URL where all webhook events are sent. A fail-over URL can also be configured; if two consecutive delivery attempts to the primary URL fail, Telnyx attempts delivery to the fail-over URL. The URL must include a scheme such as `https`.
- **Webhook API version**: Determines webhook format — V1 or V2. V2 is recommended as it has a richer feature set; V1 will be deprecated.
- **Hang-up on timeout**: When enabled, specify the number of seconds Telnyx waits for commands from your application before hanging up.
- **Custom webhook retry delay**: Delay in seconds before Telnyx retries an unsuccessful webhook delivery. If not set, Telnyx retries immediately.
- **DTMF Type**: Three options — **RFC 2833** (default, preferred, not audible), **Inband** (digits passed as normal audio tones), **SIP INFO** (mainly for SIP-to-SIP calls, negotiated between parties).
- **RTCP Capture**: Enable to build QoS reports via the SIP Call Flow Tool.
- **Call Cost Webhook Event**: Enable to receive call cost information via webhook.

### Inbound settings

- **Subdomain**: Specify a subdomain for receiving calls from SIP endpoints (e.g., `example.sip.telnyx.com`). Only the subdomain portion is needed; the Telnyx domain is appended automatically.
- **SIP subdomain receive settings**: Allow connections from anyone or only from specific connections.
- **Inbound Channel Limit**: Limit total inbound calls to numbers associated with this connection.
- **Enable SHAKEN/STIR headers**: Enable to receive attestation information in webhooks for incoming calls.
- **Codecs**: Select codecs Telnyx offers on calls. Force a specific codec by checking only one box.

### Outbound settings

- **Outbound Voice Profile**: Assign the application to an outbound voice profile to enable outbound calls.
- **Outbound Channel Limit**: Limit total outbound calls associated with this connection.

### Application ID

Each application is assigned a unique application ID visible in the application settings. This ID is used to reference or trigger API calls programmatically.

## TeXML Applications

TeXML (Telnyx XML) is an XML-based data structure for controlling calls, similar to Twilio's TwiML. TeXML Translator reads your XML file from top to bottom and executes commands sequentially. TeXML is the quickest way to get started with Programmable Voice using a simple `.xml` file.

### Core settings

- **TeXML App Name**: Assign a descriptive name when creating a new TeXML application.
- **Voice Method**: HTTP request method (`GET` or `POST`) Telnyx uses to interact with your XML Translator webhooks.
- **TeXML Webhook URL**: The URL where XML Translator webhook events are sent. A fail-over URL is also available.
- **Status Callback URL**: URL for Telnyx to send requests containing information about call progress events.
- **Status Callback Method**: HTTP method for status callback requests.
- **Hang-up on timeout**: Specify seconds to wait for application response before hanging up.
- **DTMF Type**: Same options as Voice API (RFC 2833, Inband, SIP INFO).
- **Call Cost Webhook Event**: Enable to receive call cost webhooks.

TeXML applications share the same inbound and outbound settings as Voice API applications (subdomain, channel limits, SHAKEN/STIR, codecs, outbound voice profile).

### TeXML Bin

TeXML Bin allows users to upload TeXML files to storage and use them for call flows without running application servers. Access the TeXML editor in the Mission Control Portal under **Programmable Voice > TeXML Bin**.

A simple voicemail example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Thank you for calling YYZ co. Please leave a message.</Say>
  <Record playBeep="true" finishOnKey="*9" />
</Response>
```

A simple call forward example:

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

After creating the XML, set up the TeXML application by selecting the script from the drop-down, assign a phone number, and test by dialing the number.

### Conference calls with TeXML

TeXML supports the `<Conference>` noun for conference calls. A moderated conference can hold all participants until the moderator joins (`startConferenceOnEnter`) and end the call for everyone when the moderator leaves (`endConferenceOnExit`). The `From` parameter in the webhook request identifies whether a caller is the moderator.

You can use existing Twilio SDKs (Python, PHP, Node.js, Java, .NET, Ruby) to generate TwiML/TeXML. The workflow is:

1. Buy a Telnyx phone number with voice capability.
2. Create a TeXML Application and point it at your web application URL.
3. Write a web application that returns TwiML/TeXML instructions.
4. Make the application accessible on the internet (use [ngrok](https://ngrok.com/) for development: `ngrok http 3000`).
5. Configure the TeXML Application's webhook URL to `http://<your ngrok subdomain>.ngrok.io/voice`.

## TeXML and Voice API Compatibility

**Do not combine TeXML and Voice API (Call Control) commands in the same application.** TeXML converts XML instructions into Voice API commands but also manages call state in the background. Mixing the two paradigms will eventually lead to errors or unexpected, hard-to-debug behavior.

This also applies to [AI Assistants](ai-assistants.md), which use TeXML under the hood — issuing Call Control commands on AI Assistant calls will cause state conflicts.

Common scenarios to avoid:

- Using `call_control_id` from a TeXML webhook to issue Voice API commands (e.g., transfer, bridge, hangup)
- Calling `streaming_start` on a call already using the TeXML `<Stream>` verb
- Mixing TeXML `<Dial>` with Voice API bridge commands on the same call
- Issuing Call Control commands on AI Assistant calls

If you need Call Control flexibility, use the Voice API from the start. If you need both paradigms for different parts of your application, use separate connections — a TeXML Application for TeXML calls and a Voice API Application for Call Control calls.

**Note:** TeXML webhooks use form-encoded parameters, while Voice API webhooks use JSON. If your application handles both, ensure your server can parse both formats correctly.
