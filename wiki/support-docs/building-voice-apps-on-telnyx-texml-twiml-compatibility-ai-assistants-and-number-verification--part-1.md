---
title: 'Building Voice Apps on Telnyx: TeXML, TwiML Compatibility, AI Assistants,
  and Number Verification'
summary: 'A consolidated guide to launching voice experiences on Telnyx: build call
  flows with TeXML (and TwiML compatibility), stand up conferencing, configure AI
  Assistants with tools and handoffs, and verify phone numbers including IVR and “Press
  1” DTMF methods.'
sources:
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
- url: https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx
- url: https://support.telnyx.com/en/articles/12232444-comprehensive-ai-assistants-configuration-walk-through
- url: https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr
- url: https://support.telnyx.com/en/articles/13854980-beta-how-to-verify-phone-numbers-using-dtmf-press-1-to-verify
updated_at: 2026-05-14T11:43:55Z
---

# Building Voice Apps on Telnyx: TeXML, TwiML Compatibility, AI Assistants, and Number Verification

*Part 1 of 2 — see also: [Part 2](building-voice-apps-on-telnyx-texml-twiml-compatibility-ai-assistants-and-number-verification--part-2.md)*

A consolidated guide to launching voice experiences on Telnyx: build call flows with TeXML (and TwiML compatibility), stand up conferencing, configure AI Assistants with tools and handoffs, and verify phone numbers including IVR and “Press 1” DTMF methods.

## Overview
Telnyx makes it simple to build voice applications without hosting infrastructure, or to reuse existing TwiML logic. This guide shows how to: create TeXML call flows (including voicemail, call forwarding, and conferencing), run dynamic webhooks using your current Twilio SDK-generated XML, configure AI Assistants end to end with tools and handoffs, and verify phone numbers via API or the Mission Control Portal—including behind IVRs and with DTMF “Press 1 to verify.”

## Prerequisites
- A Telnyx Mission Control Portal account: https://portal.telnyx.com/
- A Telnyx API key (for Verified Numbers and AI Assistants webhooks/tooling)
- At least one voice-capable phone number (buy in Mission Control)
- Optional: a publicly reachable webhook URL (use ngrok during development: https://ngrok.com/)

## Quickstart: TeXML Bin voicemail and call forwarding
TeXML is an XML-based call control language interpreted sequentially by Telnyx. TeXML Bin lets you upload XML directly in Mission Control—no app server required.

Steps:
1) Create XML in Mission Control: Programmable Voice → TeXML Bin.
2) Create a TeXML Application and select your uploaded script.
3) Assign a phone number to the application and test inbound calls.

Examples:
- Simple voicemail

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Thank you for calling YYZ co. Please leave a message.</Say>
  <Record playBeep="true" finishOnKey="*9"/>
</Response>
```

- Simple call forward

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

Tip: Retrieve recorded voicemails from the Call Recordings view in Mission Control.

## TwiML compatibility and conferencing with TeXML
You can point a Telnyx TeXML Application at your existing TwiML-generating web app (built with Twilio SDKs). Telnyx will POST call webhooks and execute the returned XML.

- Simple conference XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Conference>My superior Telnyx conference</Conference>
  </Dial>
</Response>
```

- Moderated conferences
  - Use <Conference> with:
    - startConferenceOnEnter=true to hold participants until the moderator joins
    - endConferenceOnExit=true to end the room when the moderator leaves
  - Identify the moderator using the webhook’s From parameter (e.g., match a specific E.164 number).

Language notes: You can keep your current Twilio SDK code (Python, PHP, Node.js, Java, .NET, Ruby) to generate TwiML; Telnyx will interpret it via your TeXML Application’s webhook URL.

## Configuring webhooks and local development with ngrok
- Create a TeXML Application and set the webhook URL to your app.
- During development, run: ngrok http <port> and paste the public URL into the application settings (append your route, e.g., /voice).
- Telnyx expects a 2xx response with XML instructions.

## AI Assistants: end-to-end configuration
AI Assistants let you handle inbound/outbound calling and messaging entirely within Telnyx.

1) In Mission Control, open AI → AI Assistants and create an assistant (use a template or start from a blank canvas).
2) Choose your model (e.g., open source like Qwen or a provider model). Store third-party API keys as integration secrets.
3) Set a Fallback model to ensure continuity if the primary model fails mid-call.
4) Author Instructions and Greeting. You can include dynamic variables (see dev docs: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
5) Optional: add a Dynamic variables webhook URL to fetch real-time context for the assistant.

## AI Assistant tools
By default, assistants can hang up. Add tools as needed:

- Webhook Tool
  - Name (no spaces), Description, Timeout (recommended 1000–5000 ms), Method (e.g., POST), and URL.
  - Advanced options: Headers (e.g., Authorization: Bearer ...), Path parameters, Query parameters, and Body parameters for custom metadata.

- Handoff Tool
  - Add a second assistant to collaborate on the call.
  - Voice modes: Unified voice (transparent handoff) or Distinct voices (conference-like experience).

- Transfer Tool
  - Transfer from a Telnyx-owned phone number or SIP URI to a target PSTN number or SIP URI.
  - Configure a friendly target name and optional custom SIP headers in the INVITE.

- SIP Refer Tool
  - Send a SIP REFER to hand the call off to another SIP domain/endpoint.
  - Configure target name, SIP address (e.g., sip:+14085551234@sip.example.com), SIP auth, optional Diversion/User-User headers, and custom headers.

- Send DTMF Tool
  - Enables assistants to send DTMF during a call (e.g., to navigate IVRs).

- Add MCP Server
  - Connect assistants to external tools/data via Model Context Protocol.
  - Types: HTTP (stateless request–response) or SSE (one-way server-to-client event stream).

## Transfers: when to use Transfer vs SIP Refer
- Transfer
  - Purpose: Move a call between endpoints within the same application/system.
  - Use when redirecting calls internally (e.g., to another department or live agent).
- SIP Refer
  - Purpose: Hand off a call to an external SIP infrastructure during a TeXML call.
  - Use when another SIP provider/system should take over call handling.

## Verified Numbers: verifying numbers behind IVR
Telnyx can verify numbers that sit behind IVRs by dialing a programmable DTMF extension sequence during the verification call.

Flow:
1) Initiate a verification with method=call and include an extension string.
2) Telnyx calls the number; the IVR answers.
3) Telnyx waits/dials the extension; the destination answers.
4) The verification code is played; the user enters it to complete verification.

Parameters:
- phone_number: E.164 format (e.g., +15741156782)
- verification_method: call
- extension: DTMF string where:
  - w = wait 0.5s, W = wait 1s, digits 0–9 and A–D allowed
  - Example: www2wW4w53ww3

How to trigger:
- API: Use the Create Verified Number endpoint (see API reference below). Include phone_number, verification_method=call, and extension.
- Portal: Numbers → Verified Numbers tab → enter number and extension → “Call me with a code.”

## Verified Numbers: Press 1 (DTMF) verification [BETA]
DTMF-based verification lets users verify by simply pressing 1 during the verification call. The announcement does not mention Telnyx.

How it works:
1) Initiate verification with verification_method=dtmf via API or Portal.
2) The target receives a call and is prompted to press 1.
3) On DTMF-1, the number is verified to your account; otherwise it fails and can be retried.

Usage:
- Single: send phone_number and verification_method=dtmf.
- Bulk: iterate over numbers and initiate separate requests; add small delays to avoid rate limiting.
- Status: GET the verified number resource to check state.

## Monitoring and webhooks for verifications
Instead of polling, include a verification_webhook_url when initiating verification to receive events such as caller_id_verification.completed. Payloads include fields like event_type, occurred_at, phone_number, verification_method, and verified_at.

## Best practices and troubleshooting
- Always use E.164 formatting.
- Test IVR extension sequences manually; add w/W waits for slower menus.
- Secure secrets via integration secrets and Authorization headers.
- For bulk DTMF verifications, throttle requests to avoid rate limits.
- If calls aren’t received, confirm number reachability and routing; if users don’t complete input/DTMF, retry.
- For webhooks, ensure public reachability and return 2xx quickly; use ngrok during development.
