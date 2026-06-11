---
title: Programmable Voice
summary: A comprehensive guide to Telnyx Programmable Voice features including AI
  assistants, conversational AI, answering machine detection, deepfake detection,
  conferencing, call center and call tracking applications, and command reliability
  patterns.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ai-assistant-start
  content_hash: 98741f32636161f55901706f46f8e1a44a9f23beb18370224ae446aa9a5bfd6f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection
  content_hash: d7a369042ca143eb9760583149e142a1545bfb5d5630b46841e04080ab398b40
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-center
  content_hash: 6743698486c30f4d9b6e0f9371ad72d04ae17b4c418bbcf4f1a1a72199ebcf9f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
  content_hash: 8762f879ea7719ba40f6a5fa4721b21367249a69fc022fc96c8486d34a5727f8
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
  content_hash: b6066b6a288f076617936c05582dd192c18263aa82d134eb52d14ab3a28b0518
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
  content_hash: 3de81d6148a7dd75fa2e2a36839abfc788546f0cfc98d4d7fbe35bc199cafbd7
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conversation-relay
  content_hash: 4b83741b3c773a4d36e4e5341557ead15eccf01625794e18a563f358764f1ecd
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
  content_hash: 25876583acfa3c5273554542ce524d05df1e663e9dd47fbd5d433dbd4ae70aaf
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
  content_hash: 0eccef25db89c30146704f1f025caac64b7b6a7fa062c496cf916f0ab68ba133
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
  content_hash: d2375c9c573083bca6581989d01b376e1cd7c24b5ae1c9a835ca334a49ec6df3
updated_at: 2026-06-11T10:41:58Z
---

# Programmable Voice

*Part 4 of 4 — see also: [Part 1](programmable-voice--part-1.md), [Part 2](programmable-voice--part-2.md), [Part 3](programmable-voice--part-3.md)*

A comprehensive guide to Telnyx Programmable Voice features including AI assistants, conversational AI, answering machine detection, deepfake detection, conferencing, call center and call tracking applications, and command reliability patterns.

## Conferencing

The Conference API (a subset of the Voice API) lets you create and manage conferences programmatically. A `call_control_id` is required to start a conference, so a call must already exist.

### Core Conference Flow

1. Receive `call.initiated` → answer the call.
2. On `call.answered`, either create a new conference (first caller) or join an existing one.
3. On `conference.ended`, clean up conference state.
4. On `call.hangup`, remove the caller from the active list.

### Conference Commands

- **Create conference**: `POST /v2/calls/{call_control_id}/actions/create_conf` with `name` and optional `beep_enabled`.
- **Join conference**: `POST /v2/calls/{call_control_id}/actions/join` with `call_control_id`.
- **Mute/Unmute participant**: `POST /v2/conferences/{conference_id}/actions/mute` or `unmute` with `call_control_ids`.
- **Hold/Unhold participant**: `POST /v2/conferences/{conference_id}/actions/hold` or `unhold` with `call_control_ids` and optional `audio_url`.
- **Recording start/stop**: `POST /v2/calls/{call_control_id}/actions/record_start` (supports `format` and `channels`) or `record_stop`.

### Client State

`client_state` is a base64-encoded value that helps you track where a caller is in your IVR flow. Because the Voice API is stateless and async, your application may receive multiple events of the same type. `client_state` lets you attach a unique identifier to a command flow, making it possible to distinguish between IVR levels or conversation stages.

### Webhook Verification

Telnyx signs every webhook. Verify the signature using your public key (available in the Portal) and the `HTTP_TELNYX_SIGNATURE_ED25519` and `HTTP_TELNYX_TIMESTAMP` headers. SDK methods like `Telnyx::Webhook::Signature.verify` (Ruby) or `\Telnyx\Webhook::constructEvent` (PHP) handle this automatically.

### SDK and Language Examples

Sample conferencing applications are available for [Python (Flask)](https://github.com/team-telnyx/python-conferencing-demo), [PHP (Slim)](https://github.com/team-telnyx/demo-conference-php), [Node.js (Express)](https://github.com/team-telnyx/demo-conference-node), and [Ruby (Sinatra)](https://github.com/team-telnyx/demo-conference-ruby).

## Call Center Application

You can build a call center using the Telnyx Voice API, TeXML, and Python AIOHTTP. The sample application ([GitHub repo](https://github.com/team-telnyx/demo-python-telnyx/tree/master/call-center-texml)) handles:

1. A user calls the main number and hears a TTS greeting.
2. The call is forwarded to multiple agents simultaneously (with recording enabled).
3. If one agent answers, the others stop ringing.
4. If no agent answers, a second TTS message plays and agents are dialed again.
5. If no agent answers on the second attempt, the user can leave a voicemail.
6. If the call is answered and ends, a TTS thank-you message plays.

### Portal Setup

1. **Create a TeXML Application** in the Portal. Set Voice Method to `GET` with a webhook URL like `https://{ngrok_url}/TeXML/inbound`. Set Status Callback Method to `POST` with a callback URL like `https://{ngrok_url}/TeXML/events`.
2. **Buy a phone number** and associate it with the TeXML Application.
3. **Create SIP Connections** (Credentials-based) for each agent. Under Inbound Options, set Receive SIP URI Calls to "From anyone". Set the webhook URL to `https://{ngrok_url}/outbound/event`.
4. **Create an Outbound Voice Profile** and associate all SIP Connections with it.

### Environment Setup

The application requires Python 3.6+ and the `aiohttp`, `apscheduler`, and `python-dotenv` packages. Run `python setup.py` to create a `.env` file with variables including `API_KEY`, `NGROK_URL`, and `OUTBOUND_PROFILE_ID`. Start the app with `PYTHONPATH=$(pwd)/ python call_center/main.py`.

### Customization

- **Hangup behavior**: Edit `answered.xml` to change the post-call experience (e.g., use `<Dial>` or `<Redirect>` instead of `<Say>`).
- **Custom audio**: Place `support_greeting.mp3` and `support_busy.mp3` in `/call_center/infrastructure/audio/`, then uncomment `<Play>` verbs and comment out `<Say>` verbs in the TeXML templates.
- **Voicemail**: Specify a recording status callback URL in `voicemail.xml` to receive the recording file URL when the call ends.

## Call Tracking Application

Call Tracking applications map purchased Telnyx phone numbers to forwarding numbers, route inbound calls via Call Control transfers, and store call metadata. Samples are available for [Python (Flask)](https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-call-tracking_call-control) and [Node.js (Express)](https://github.com/team-telnyx/demo-node-telnyx/tree/master/call-tracking).

### Core Flow

1. Search and order a phone number by area code or city/state.
2. Store a binding of Telnyx number → forwarding number.
3. Receive inbound calls, answer them, and transfer to the forwarding number.
4. On hangup, save call metadata (CNAM lookup, duration, timestamps) to a database.

### Portal Setup

1. Create a Call Control Application with your ngrok forwarding URL.
2. Create an Outbound Voice Profile and associate the Call Control Application.

### Environment Variables

Key variables: `TELNYX_API_KEY`, `TELNYX_PUBLIC_KEY`, `TELNYX_CONNECTION_ID`, `PORT` (Node) or database credentials (Python).

### Key API Operations

- **Number search**: `telnyx.AvailablePhoneNumber.list()` with filters for locality, rate center, features, and `quickship: true`.
- **Number order**: `telnyx.NumberOrder.create()` with `connection_id` and `messaging_profile_id`.
- **Number delete**: `telnyx.PhoneNumber.retrieve(id).delete()`.
- **CNAM lookup**: `telnyx.NumberLookup.retrieve(number)` for caller name information.
- **Call answer**: `call.answer()` on `call.initiated`.
- **Call transfer**: `call.transfer()` with `to` and `webhook_url` on `call.answered`.

### Bindings API (Node)

The Node sample exposes a RESTful `/bindings` endpoint: `POST` to create a binding (with `areaCode` and `destinationPhoneNumber`), and `GET` to list bindings and call information.

## Command Reliability and Retries

For improved reliability when using the Voice API:

- **`command_id`**: Send a unique `command_id` parameter (UUIDv4 recommended) with each command. This ensures idempotency if retries are needed.
- **Retry on 5XX errors**: If your application receives a 500 error, immediately retry the command.
- **Retry on latency >500 ms**: If no HTTP response is received within 500 ms, resend the identical command.

Telnyx actively monitors 5XX error rates, latency, and duplicate webhooks. Duplicate webhooks may occasionally be delivered; design your application to handle them gracefully.
