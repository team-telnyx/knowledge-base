---
title: 'Telnyx Programmable Voice API: Outbound Voice Profiles, Commands, and Webhooks'
summary: A practical guide to building with the Telnyx Programmable Voice API—covering
  core concepts, outbound voice profiles, application setup, making calls, webhooks,
  commands, reliability practices, and recordings.
sources:
- url: https://developers.telnyx.com/docs/voice/outbound-voice-profiles
- url: https://developers.telnyx.com/docs/voice/overview/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/get-started/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks
- url: https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources
- url: https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
updated_at: 2026-05-20T09:31:54Z
---

# Telnyx Programmable Voice API: Outbound Voice Profiles, Commands, and Webhooks

*Part 1 of 2 — see also: [Part 2](telnyx-programmable-voice-api-outbound-voice-profiles-commands-and-webhooks--part-2.md)*

A practical guide to building with the Telnyx Programmable Voice API—covering core concepts, outbound voice profiles, application setup, making calls, webhooks, commands, reliability practices, and recordings.

## What the Programmable Voice API Enables
Telnyx Programmable Voice API lets you add outbound and inbound calling to your applications with real-time control. You can dial calls, play audio or TTS, gather input, bridge/transfer, transcribe, stream media, and more—while receiving webhooks for every key event.

## Core Building Blocks
- Voice API Application: Defines how calls are handled, including webhook URLs, codecs, and inbound/outbound limits. It’s sometimes referred to as a “connection” in Mission Control.
- Outbound Voice Profile: Controls how outbound traffic is routed, billed, and where it’s allowed. You must associate an outbound voice profile with your Voice API Application to place outbound calls.
- Webhooks: Real-time HTTP callbacks for events like call.initiated, call.answered, call.hangup, media playback start/end, recording saved, transcription, streaming, and more.

## Set Up Your Environment
- Telnyx account and API key (create and store securely).
- A purchased Telnyx phone number for the From identity.
- Destination and source numbers in E.164 format (e.g., +1234567890).
- A reachable webhook endpoint (use a tool like ngrok for local testing).

## Create a Voice API Application
In Mission Control: Real-Time Communication > Voice > Programmable Voice > Create Voice App.

Key configuration options:
- General
  - Application name and tags.
  - Webhook URL and optional failover URL.
  - Webhook API version (v2 recommended).
  - Anchor site for optimal media routing.
  - Custom webhook timeout and “hang up on timeout.”
  - DTMF type (RFC 2833 recommended).
  - Enable call cost webhooks.
- Inbound
  - SIP subdomain and who can call it (public internet vs. own connections).
  - Inbound channel limit.
  - SHAKEN/STIR headers.
  - Audio/video codecs.
- Outbound
  - Outbound voice profile (required for outbound calling).
  - Outbound channel limit.
- Numbers
  - Assign purchased numbers to this application for inbound/outbound handling.

## Configure Outbound Voice Profiles
Outbound voice profiles group outbound settings that govern where and how you can call and how billing is applied. Typical uses include:
- Enforcing allowed/destination restrictions (e.g., domestic only, specific countries).
- Applying billing/routing policies.
- Enabling default behaviors like recording outbound calls (can also be started programmatically per call).
Associate your profile with the Voice API Application’s Outbound settings so all calls via that app use the profile.

## Place Your First Outbound Call
- You’ll need: your API key, your Telnyx phone number (from), destination number (to), and the application ID (connection_id) from your Voice API Application.

cURL example:

```
curl --location 'https://api.telnyx.com/v2/calls' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --data '{
    "to": "+1234567890",
    "from": "+15551234567",
    "connection_id": "your_connection_id",
    "command_id": "unique-command-id-123"
  }'
```

Node.js example:

```
const axios = require('axios');

(async () => {
  const res = await axios.post(
    'https://api.telnyx.com/v2/calls',
    { to: '+1234567890', from: '+15551234567', connection_id: 'your_connection_id' },
    { headers: { Authorization: 'Bearer YOUR_API_KEY' } }
  );
  console.log('Call initiated:', res.data);
})();
```

Python example:

```
import requests

r = requests.post(
  'https://api.telnyx.com/v2/calls',
  headers={'Authorization': 'Bearer YOUR_API_KEY', 'Content-Type': 'application/json'},
  json={'to': '+1234567890', 'from': '+15551234567', 'connection_id': 'your_connection_id'}
)
print('Call initiated:', r.json())
```

Typical call flow:
1) You POST to /v2/calls.
2) Telnyx sends call.initiated.
3) As the call progresses you receive call.answered, call.bridged (if bridged), and ultimately call.hangup.
4) You can send commands at any point using the call_control_id from webhooks.

## How Voice API Webhooks Work
- Delivery: Telnyx POSTs events to your application’s primary webhook URL; if it fails, Telnyx uses the failover URL (if set).
- Ordering: Delivery order isn’t guaranteed; events can be out of order, concurrent, or duplicated.
- Acknowledge quickly: Return a 2xx ASAP and process asynchronously.
- Signature verification: Verify Telnyx-Signature-Ed25519 with Telnyx-Timestamp to confirm authenticity.

Webhook headers include:
- Content-Type: application/json (for POST)
- User-Agent: telnyx-webhooks
- Telnyx-Signature-Ed25519: signature for verification
- Telnyx-Timestamp: Unix timestamp of generation

Common payload envelope (v2):
- data.record_type: "event"
- data.event_type: e.g., call.initiated, call.answered, call.hangup
- data.id: unique event ID (use for idempotency)
- data.occurred_at: ISO-8601 timestamp
- data.payload: includes call_control_id, call_leg_id, call_session_id, connection_id, client_state, from, to, direction, state
- meta.attempt: delivery attempt number
- meta.delivered_to: destination URL

## Webhook Configuration Options
You can configure where and how events are delivered at multiple levels:
- Connection-level (Voice API Application): set webhook URL, failover URL, API version, timeouts.
- Per-command override: include webhook_url and webhook_url_method in a command to route only that command’s events to a different endpoint or as GET with query parameters.
- Event routing (advanced): route certain event types to different URLs.

## Common Voice API Webhook Events
Call state:
- call.initiated: a new call leg is created (via Dial/Transfer or inbound)
- call.answered: the call was answered
- call.hold / call.unhold: hold state changes
- call.hangup: the call ended
- call.bridged: two call legs connected (Bridge/Transfer)

Audio/TTS:
- call.playback.started / call.playback.ended (play audio)
- call.speak.started / call.speak.ended (text-to-speech)

DTMF and gather:
- call.dtmf.received, call.gather.ended

Recording:
- call.recording.saved (after recording stops or call ends)

AMD (answering machine detection):
- call.machine.detection.ended, call.machine.greeting.ended (standard)
- call.machine.premium.detection.ended, call.machine.premium.greeting.ended (premium)

Media forking and streaming:
- call.fork.started / call.fork.stopped
- streaming.started / streaming.stopped

Transcription:
- call.transcription (real-time transcript events)

Response codes from your webhook handler:
- 2xx: acknowledged
- 3xx: redirects followed (limited)
- 408/429 and 5xx: retried; other 4xx: not retried

## Sending Commands During a Call
- Address commands to a specific call leg using call_control_id.
- Authenticate with Authorization: Bearer YOUR_API_KEY.

Popular commands and their typical webhooks:
- Answer call → call.answered
- Bridge call → call.bridged on each bridged leg
- Dial → call.initiated, then call.answered or call.hangup; AMD events if enabled
- Play audio → call.playback.started, call.playback.ended
- Speak text (TTS) → call.speak.started, call.speak.ended
- Gather (audio/speak/AI) → DTMF events and call.gather.ended
- Transfer → new call.initiated for the B-leg, then call.bridged, then call.answered or call.hangup
- Record start/stop → stop triggers call.recording.saved
- Forking/Streaming start/stop → corresponding started/stopped events
- Hangup/Reject → call.hangup

Explore additional endpoints for conferences, queues, recordings, transcription, SIPREC, and active call queries in the API reference.
