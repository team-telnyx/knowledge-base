---
title: TeXML Quickstarts, Conferencing, Voicemail, Fax, and Routing on Telnyx
summary: A consolidated guide to building voice flows with TeXML (including voicemail,
  call forwarding, and conferencing), understanding TeXML vs. Voice API compatibility,
  enabling Telnyx voicemail on SIP Connections, configuring fax over T.38/G.711 with
  common errors, and using Round Robin routing for inbound load balancing.
sources:
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
- url: https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx
- url: https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail
- url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
- url: https://support.telnyx.com/en/articles/8174793-round-robin-routing
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/4967498-fax-api-error-list
- url: https://support.telnyx.com/en/collections/17907095-texml-tutorials
- url: https://support.telnyx.com/en/collections/3968239-telnyx-fax-configuration-errors
updated_at: 2026-05-20T14:32:55Z
---

# TeXML Quickstarts, Conferencing, Voicemail, Fax, and Routing on Telnyx

*Part 1 of 2 — see also: [Part 2](texml-quickstarts-conferencing-voicemail-fax-and-routing-on-telnyx--part-2.md)*

A consolidated guide to building voice flows with TeXML (including voicemail, call forwarding, and conferencing), understanding TeXML vs. Voice API compatibility, enabling Telnyx voicemail on SIP Connections, configuring fax over T.38/G.711 with common errors, and using Round Robin routing for inbound load balancing.

## TeXML overview and TeXML Bin
TeXML is an XML-based way to control Telnyx calls, executing verbs/nouns in order from top to bottom. TeXML Bin lets you store XML in Telnyx and run call flows without hosting your own server. You can author and manage files in the Mission Control Portal TeXML editor (Programmable Voice → TeXML Bin).

See also: [TeXML Bin Simple Voicemail and Call Forwarding](texml-bin-simple-voicemail-and-call-forwarding.md), [TeXML tutorials](texml-tutorials.md).

## Quickstart: simple voicemail with TeXML
Create a TeXML file like:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Thank you for calling YYZ co. Please leave a message.</Say>
  <Record playBeep="true" finishOnKey="*9" />
</Response>
```

Then:
- Create a TeXML Application and select your XML.
- Assign a phone number to the application.
- Call from the PSTN and leave a message; retrieve recordings from your Portal call recordings for quick validation.

Reference: [TeXML Bin Simple Voicemail and Call Forwarding](texml-bin-simple-voicemail-and-call-forwarding.md).

## Quickstart: simple SIP call forwarding with TeXML
Forward inbound calls to SIP endpoints:

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

Attach this TeXML to a TeXML Application and assign a number as above.

## Configure TeXML Applications and numbers
- Buy a number in the Mission Control Portal (Voice-capable).
- Create a TeXML Application and either select a TeXML Bin file or point the webhook URL to your existing TwiML/TeXML web app.
- During development, expose your local app with ngrok and set the application URL accordingly (for example, http://<your-subdomain>.ngrok.io/voice).

See also: [Twilio TwiML Conference on Telnyx](twilio-twiml-conference-on-telnyx.md).

## Conference calling with TeXML/TwiML on Telnyx
A minimal conference room:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Conference>My superior Telnyx conference</Conference>
  </Dial>
</Response>
```

Moderator-style controls use <Conference> attributes such as:
- startConferenceOnEnter: hold others until moderator joins
- endConferenceOnExit: end the conference when moderator leaves

You can generate TwiML/TeXML with popular Twilio SDKs (Python, PHP, Node, Java, .NET, Ruby) and have Telnyx execute it. Language-specific examples and ngrok setup are in [Twilio TwiML Conference on Telnyx](twilio-twiml-conference-on-telnyx.md).

## TeXML vs. Voice API (Call Control): compatibility and best practices
Avoid mixing TeXML instructions with Voice API commands on the same call. TeXML manages call state internally; injecting Call Control (transfer/bridge/hangup, media streaming, etc.) into a TeXML-managed call can create state conflicts and hard-to-debug behavior. This also applies to calls handled by AI Assistants (they use TeXML under the hood).

Common anti-patterns to avoid:
- Using a call_control_id from a TeXML webhook to send Voice API commands
- Calling streaming_start while using the TeXML <Stream> verb
- Mixing TeXML <Dial> with Voice API bridge commands
- Issuing Call Control on AI Assistant calls

Notes:
- TeXML webhooks are form-encoded; Voice API webhooks are JSON. Ensure your server parses both if you use both paradigms across different connections.
- If you need full Call Control flexibility, build with the Voice API from the start and keep TeXML and Voice API on separate connections.

Details: [TeXML and Telnyx Voice API compatibility](texml-and-telnyx-voice-api-compatibility.md).

## Telnyx built-in Voicemail on SIP Connections (PIN, *98, webhooks)
Separate from the TeXML-based voicemail above, Telnyx offers a built-in voicemail feature for numbers assigned to SIP Connections.

Key points:
- Enable per number in Portal → Numbers → My Numbers → edit number → Voice tab → Voicemail.
- Set a mandatory PIN when enabling voicemail.
- To check voicemail: dial *98 from a device whose Caller ID is set to the voicemail-enabled number, then authenticate with PIN.
- Webhook: calls.voicemail.completed is delivered to your SIP Connection webhook URL with fields such as call_session_id, from, to, and recording_url.
- Early-version limitations: no custom greeting; no automatic email upon deposit.
- Manage programmatically via Voicemail API endpoints:
  - Get: https://developers.telnyx.com/api/voicemail/get-voicemail
  - Create: https://developers.telnyx.com/api/voicemail/create-voicemail
  - Update: https://developers.telnyx.com/api/voicemail/update-voicemail

See: [Setting Up Telnyx Voicemail](setting-up-telnyx-voicemail.md).

## Fax over Telnyx (T.38 and G.711) setup
Outbound fax
- Create a SIP Connection; create an Outbound Profile and attach the connection.
- By default, Telnyx sends a T.38 re-INVITE after fax tone detection. You can change “T.38 Re-invite Initiated By” to Telnyx (default), Customer, or Disabled (forces G.711 fax) in the connection’s outbound settings.

Inbound fax
- Create a SIP Connection; buy a number; assign the connection to the number.
- By default, Telnyx expects the customer to send a T.38 re-INVITE; if none, the call proceeds with G.711. You can force acceptance by enabling T.38 Fax Gateway on the number (My Numbers → gear → Expert Configuration → Enable T.38 Fax Gateway). Unchecking that option prevents T.38 re-INVITEs.

Fax device best practices
- Set baud rate to 9600 or below.
- Disable Error Correction Mode (ECM).
- Use “normal” resolution.
- Disable dial tone detection only if outbound dialing fails.
- SRTP is not supported when T.38 is enabled.

Full walkthrough: [Fax service with Telnyx (via T.38 or G711)](fax-service-with-telnyx-via-t-38-or-g711.md).

## Programmable Fax: common errors and reporting
Programmable Fax webhook events include a failure_reason for quick triage (for example: file_size_limit_exceeded, page_count_limit_exceeded, file_download_failed, fax_initial_communication_timeout, fax_signaling_error, receiver_no_response, receiver_unallocated_number, service_unavailable). Inbound errors include cases like carrier_lost, sender_canceled, and sender_call_dropped.

Notes:
- Telnyx does not automatically retry failed outbound faxes; implement retries in your application.
- Fax API CDR CSV reports include numeric result codes (e.g., 0 OK, 2 initial communication timeout, 14 bad response to DCS/training, 49 call dropped prematurely).

Reference: [Fax API - Error List](fax-api-error-list.md).

## Round Robin routing for inbound load balancing
Round Robin distributes inbound calls evenly across all IPs on a SIP Connection. Behavior notes:
- Distribution is based on inbound attempts, not current active calls.
- Built-in failover: if the first target IP fails, Telnyx tries subsequent IPs in order until one answers or all are exhausted.
- Enable via Connection → Basic Settings → Default Routing Method → Round Robin.

Learn more: [Round Robin Routing](round-robin-routing.md).
