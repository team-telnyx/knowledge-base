---
title: Telnyx Programmable Voice API
summary: The Telnyx Programmable Voice API enables integration of voice calling capabilities
  into applications, providing granular control over inbound and outbound calls through
  commands, webhooks, media streaming, IVR, call queueing, noise suppression, and
  SIPREC recording.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/get-started/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ivr-demo/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/l1-accounts-restirctions
- url: https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming
- url: https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/queueing-calls
- url: https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks
- url: https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client
updated_at: 2026-06-11T10:42:33Z
---

# Telnyx Programmable Voice API

*Part 1 of 3 — see also: [Part 2](telnyx-programmable-voice-api--part-2.md), [Part 3](telnyx-programmable-voice-api--part-3.md)*

The Telnyx Programmable Voice API enables integration of voice calling capabilities into applications, providing granular control over inbound and outbound calls through commands, webhooks, media streaming, IVR, call queueing, noise suppression, and SIPREC recording.

## Prerequisites and Setup

To use the Programmable Voice API you need:

- A [Telnyx account](https://telnyx.com/sign-up)
- An API Key from the [Mission Control Portal](https://portal.telnyx.com/)
- Phone numbers in E.164 format (e.g. `+1234567890`)
- An Outbound Voice Profile configured and associated with a Voice API Application
- A Voice API Application with a webhook URL set up

A minimal outbound call can be initiated with a single HTTP POST:

```bash
curl --location 'https://api.telnyx.com/v2/calls' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YourAPIKey' \
--data '{
   "to":"+13125790015",
   "from":"+13125790968",
   "connection_id":"234423"
}'
```

## Core Concepts

- **Voice API Applications** — the backbone for handling incoming and outgoing calls, providing a framework for call routing, caller verification, and other use cases.
- **Outbound Voice Profile** — configures outbound call billing and controls traffic destinations. It must be associated with a Voice API Application and is essential for automated outbound calling, call forwarding, and international call management.
- **Webhooks** — real-time notifications about call events delivered to your server. They are integral for monitoring call progress, handling outcomes, and integrating with external systems. See the [Webhooks guide](https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks#example-receiving-a-webhook) for implementation details.
- **Client State** — a Base64-encoded value passed back and forth between your application and Telnyx. Because the Voice API is stateless and asynchronous, `client_state` lets you identify where a particular call leg is in your flow and ensure commands execute only under specific conditions. This is especially important when both inbound and outbound legs emit events to the same webhook endpoint.

## Sending Commands

Every Voice API command is sent with a `call_control_id`, which tells Telnyx which call leg to control and routes the command to the optimal location for the lowest possible latency.

### Authentication

All command requests require the `Authorization` header with an API Key:

| Credential Type | HTTP Header Format |
|---|---|
| API Key | `Authorization: Bearer YOUR_API_KEY` |

### Available Commands and Expected Webhooks

| Command | Expected Webhooks |
|---|---|
| Answer call | `call.answered` |
| Bridge call | `call.bridged` for Leg A, `call.bridged` for Leg B |
| Dial | `call.initiated`, `call.answered` or `call.hangup`, `call.machine.detection.ended` (if AMD requested), `call.machine.greeting.ended` (if AMD requested) |
| Forking start | `call.fork.started`, `call.fork.stopped` |
| Forking stop | `call.fork.stopped` |
| Gather using audio | `call.playback.started`, `call.playback.ended`, `call.dtmf.received` (many), `call.gather.ended` |
| Gather using speak | `call.dtmf.received` (many), `call.gather.ended` |
| Hangup | `call.hangup`, `call.recording.saved` (if recording) |
| Play audio URL | `call.playback.started`, `call.playback.ended` |
| Playback stop | `call.playback.ended` or `call.speak.ended` |
| Recording start | no webhooks |
| Recording stop | `call.recording.saved` |
| Reject call | `call.hangup` |
| Send DTMF | no webhooks |
| Speak text | `call.speak.started`, `call.speak.ended` |
| Transfer call | `call.initiated`, `call.bridged` to Leg B, `call.answered` or `call.hangup` |

### Command Response Codes

| HTTP Status | Message | Description |
|---|---|---|
| 200 | OK | The request succeeded. |
| 403 | Forbidden | The user is not authorized to perform this action. |
| 404 | Not Found | The requested resource could not be found. |
| 422 | Invalid Parameters | Invalid parameters or the call is no longer active. |

To prevent duplicate commands caused by duplicate webhooks, include a `command_id` parameter. Commands with duplicate `command_id` values within 60 seconds are ignored.

## Receiving Webhooks

Webhooks are delivered to the primary URL on the Voice API Application. If that URL fails or returns a non-200 response, delivery falls back to the failover URL if configured.

To minimize delivery time, Telnyx does not enforce webhook order and retries delivery if your application doesn't respond in time. As a result you may encounter out-of-order, near-simultaneous, or duplicate webhooks.

A typical `call.initiated` webhook payload looks like:

```json
{
  "data": {
    "record_type": "event",
    "event_type": "call.initiated",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "occurred_at": "2018-02-02T22:25:27.521992Z",
    "payload": {
      "call_control_id": "d14dbcee-880b-11eb-8204-02420a0f7568",
      "connection_id": "7267xxxxxxxxxxxxxx",
      "call_leg_id": "d14dbcee-880b-11eb-8204-02420a0f7568",
      "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
      "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
      "from": "+1-202-555-0133",
      "to": "+12025550131",
      "direction": "incoming",
      "state": "parked"
    }
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "http://example.com/webhooks"
  }
}
```

### Key Webhook Fields

| Field | Description |
|---|---|
| `record_type` | Description of the record |
| `event_type` | The type of event detected by the Telnyx system |
| `id` | Unique ID for the webhook |
| `occurred_at` | ISO-8601 datetime of when the event occurred |
| `call_control_id` | Call ID used to issue Voice API commands |
| `connection_id` | Voice API Application ID used in the call |
| `call_leg_id` | ID unique to the call leg; can correlate webhook events |
| `call_session_id` | ID unique to the call session (a group of related call legs) |
| `client_state` | State received from a previous command |
| `direction` | `incoming` or `outgoing` |
| `state` | `bridging` or `parked` |

### Webhook Signature Verification

To prevent spoofed webhooks, verify signatures using the `Telnyx::Webhook::Signature.verify` method (Ruby) or equivalent in other SDKs. Your Telnyx public key is read from environment variables, and verification checks the `HTTP_TELNYX_SIGNATURE_ED25519` and `HTTP_TELNYX_TIMESTAMP` headers against the payload body.
