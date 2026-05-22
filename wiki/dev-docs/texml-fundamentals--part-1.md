---
title: TeXML Fundamentals
summary: TeXML is Telnyx’s XML-based markup language for building programmable voice
  call flows with simple, sequential “verbs” and “nouns.” This page explains what
  TeXML is, how TeXML Applications fetch and run your instructions, quick ways to
  host XML with TeXML Bin, using dynamic templates and HTTP requests, and how TeXML
  aligns with Twilio’s TwiML for fast migration.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
  content_hash: 44926f6fe1cdd9db555df44e6663d8d682b8d0d09aa667c7871761f5298f3597
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
  content_hash: cdc8eea33def935c1c4adf405b8ca4050bd9daee2cab77e9a2ed7d982f3c7cae
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart
  content_hash: 423683bc710e343878daf7cb12062097ff9dcc03f94be8ef93398906030dee8a
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic
  content_hash: bdd4ecaf617ffeb47b5e20f2858f95e8b338f0f50dd6d1f1dd74c6901aa61ce0
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching
  content_hash: 30586d67aef7fbe6013710694cba378084f7f5c77c095e5911d8fb45555ffe1c
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter
  content_hash: 95b262ca75a1f895956d5675895bcd12649dab5a80c5a39bc6ae5545e10d49e5
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests
  content_hash: ef808de2ca1772907239fbb75f9d7e2387cb79e2087b640b617a0f3117cd2612
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
  content_hash: 0fbd8134313bac0367ec56e73c772504a60d4fa08cae006714ed5bc52de178d7
updated_at: 2026-05-20T09:36:55Z
---

# TeXML Fundamentals

*Part 1 of 2 — see also: [Part 2](texml-fundamentals--part-2.md)*

TeXML is Telnyx’s XML-based markup language for building programmable voice call flows with simple, sequential “verbs” and “nouns.” This page explains what TeXML is, how TeXML Applications fetch and run your instructions, quick ways to host XML with TeXML Bin, using dynamic templates and HTTP requests, and how TeXML aligns with Twilio’s TwiML for fast migration.

## What TeXML is
TeXML is an XML-based instruction set that controls how Telnyx handles phone calls. A TeXML response is valid XML with a single <Response> root containing ordered commands:
- Verbs: actions to perform (for example, Say, Dial, Gather, Record, Hangup)
- Nouns: the targets or content of those actions (for example, Number, Sip)
The TeXML interpreter reads from the top of your document and executes instructions in order. See [TeXML Interpreter](texml-interpreter.md) and [TeXML and TwiML Compatibility](texml-and-twiml-compatibility.md) for supported verbs and nouns and migration notes.

## TeXML Applications (webhook configuration)
A TeXML Application ties your numbers/SIP subdomains to a webhook that returns TeXML. Key settings:
- Application name: label for identification.
- AnchorSite: preferred data center; choose a specific site or latency-based selection (Telnyx pings your webhook host to route to the closest site).
- Voice method: HTTP method used to fetch your TeXML (GET default, or POST).
- Webhook URL: where Telnyx fetches TeXML when a call starts; you can also point this at a TeXML Bin URL.
- Webhook Failover URL: backup if the primary URL fails.
- Call progress events URL and Status Callback Method: where/how Telnyx posts call status updates.
- Hang-up on timeout: maximum seconds to wait for an initial TeXML response before ending the call.
- DTMF type: how touch-tones are handled.
- Enable Call Cost: opt in to cost webhooks.
Create/manage in Mission Control Portal (Voice → Programmable Voice → TeXML Applications) or via the API.

## Getting started in 5 steps (simple TTS)
- Step 1: Create a Telnyx account, buy a number, and create a TeXML Application. Ensure you can receive webhooks and send commands via the Voice API. See [TeXML Quickstart: Simple Text-to-Speech Demo](texml-quickstart-simple-text-to-speech-demo.md).
- Step 2: Author a minimal TeXML file to speak text then hang up:
```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>This is TeXML text to speech setup in seconds! The call will now hangup.</Say>
  <Hangup/>
</Response>
```
- Step 3: Host your XML. The fastest option is TeXML Bin: upload in Portal (Voice → Settings → TeXML Bin) and use the provided URL.
- Step 4: In your TeXML Application, set Voice Method to GET and set the webhook URL to your XML (or select the TeXML Bin file). Assign your phone number to the application.
- Step 5: Call your Telnyx number; you’ll hear the text-to-speech.

## TeXML Bin (no‑code XML hosting)
TeXML Bin stores and serves your TeXML, so you don’t need to run a server.
- Simple voicemail:
```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Thank you for calling YYZ co. Please leave a message.</Say>
  <Record playBeep="true" finishOnKey="*9"/>
</Response>
```
- Simple call forward:
```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Sip>ext1@sip.xyzco.com</Sip>
    <Sip>ext3@sip.xyzco.com</Sip>
    <Sip>ext4@sip.xyzco.com</Sip>
  </Dial>
</Response>
```
After uploading, select the file in your TeXML Application, assign a number, and test. See [TeXML Bin Simple Voicemail and Call Forwarding](texml-bin-simple-voicemail-and-call-forwarding.md).

## How Telnyx fetches your instructions
- Inbound calls: When a call hits a number or SIP subdomain assigned to your TeXML Application, Telnyx fetches TeXML from the application’s Webhook URL and runs it.
- Outbound calls:
  - Using TeXML Application: Initiate via TeXML Calls API; Telnyx fetches from the Url you pass and executes. See [TeXML Instruction Fetching](texml-instruction-fetching.md).
  - Using SIP trunking: Configure a SIP connection to “Park Outbound Calls.” Telnyx parks the outbound leg, fetches from the connection’s URL, then proceeds—no TeXML Application required.

## Request parameters and response requirements
When Telnyx fetches TeXML:
- Method: GET or POST (configurable; GET by default)
- Failover: Telnyx will use your Failover URL if the primary is unavailable
- Parameters include (examples): AccountSid, CallSid, From, To, CallerId, CallingPartyType (sip|pstn), FromSipUri, ToSipUri, ConnectionId. Format: query string for GET, form-encoded for POST.
- Your response must be valid XML with a single <Response> root and return HTTP 200 OK. Keep responses small and fast to generate.
Example response:
```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Welcome to the Telnyx TeXML service.</Say>
  <Gather timeout="5" numDigits="1">
    <Say>Press 1 to continue.</Say>
  </Gather>
</Response>
```
See [TeXML Instruction Fetching](texml-instruction-fetching.md) for full parameter details and examples.

## Dynamic content with Mustache templates
You can template TeXML using Mustache so values are injected at fetch time from URL parameters or Telnyx-sent parameters (for example, CallSid, From, To). Common patterns:
- Insert a single value passed in the webhook URL:
```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Number>{{PhoneNumber}}</Number>
  </Dial>
</Response>
```
Call setup can include Url=https://example.com/texml.xml?PhoneNumber=+18771234567 to populate the variable.
- Iterate over a list (e.g., PhoneNumbers[]=...&PhoneNumbers[]=...):
```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    {{#PhoneNumbers}}
      <Number>{{.}}</Number>
    {{/PhoneNumbers}}
  </Dial>
</Response>
```
- Conditional content with if/else using == and != operators (for example, branch by From). See [TeXML Bin Dynamic Content](texml-bin-dynamic-content.md) and [TeXML Interpreter](texml-interpreter.md) for syntax and examples.

## Sending HTTP requests from TeXML
Use the HttpRequest verb to integrate with external systems directly from TeXML (no server required). You can set method, headers, and body, and optionally wait for the response.
- Basic structure:
```
<Response>
  <HttpRequest>
    <Request url="https://example.com" method="POST">
      <Headers>
        <Header><Key>Authorization</Key><Value>Bearer API_key</Value></Header>
        <Header><Key>Content-Type</Key><Value>application/json</Value></Header>
      </Headers>
      <Body><![CDATA[{"key":"value"}]]></Body>
    </Request>
  </HttpRequest>
</Response>
```
- Synchronous behavior: Requests are asynchronous by default; you can make them wait for a response by setting the async attribute to true and optionally map fields from the response into variables for subsequent callbacks.
- Secrets: Store API keys via the TeXML Secrets API, then reference them in TeXML with {{#secret}}name{{/secret}}. Secrets are redacted from logs and callbacks.
- Example use case: Look up caller details in a CRM, then notify a Slack channel, all from TeXML. See [Sending HTTP requests in TeXML - tutorial](sending-http-requests-in-texml-tutorial.md) for end‑to‑end patterns.

## Twilio/TwiML compatibility overview
TeXML is designed for straightforward Twilio → Telnyx migration: your existing TwiML verbs and nouns are interpreted by the TeXML translator. Highlights:
- Telnyx-only additions: HttpRequest and AIGather are supported in TeXML (not in TwiML).
- Not supported in TeXML: TwiML Pay verb and nouns like Client, Room, VirtualAgent.
- REST endpoints: TeXML provides Twilio‑style REST endpoints for calls, conferences, recordings, streams, SIPREC, queues, and more.
See [TeXML and TwiML Compatibility](texml-and-twiml-compatibility.md) for the full verb/noun matrix and REST endpoint mapping.
