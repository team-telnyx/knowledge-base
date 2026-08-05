---
title: Programmable Voice - L1 Accounts Restirctions to Sending Commands
summary: A consolidated reference for Telnyx Programmable Voice covering account restrictions
  for L1 verified accounts, sending commands and receiving webhooks, media streaming
  over WebSockets, noise suppression, call queueing, and Pay over Voice.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/l1-accounts-restirctions
- url: https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming
- url: https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/pay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/queueing-calls
- url: https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks
- url: https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands
updated_at: 2026-08-05T14:04:29Z
---

# Programmable Voice - L1 Accounts Restirctions to Sending Commands

*Part 1 of 4 — see also: [Part 2](programmable-voice-l1-accounts-restirctions-to-sending-commands--part-2.md), [Part 3](programmable-voice-l1-accounts-restirctions-to-sending-commands--part-3.md), [Part 4](programmable-voice-l1-accounts-restirctions-to-sending-commands--part-4.md)*

A consolidated reference for Telnyx Programmable Voice covering account restrictions for L1 verified accounts, sending commands and receiving webhooks, media streaming over WebSockets, noise suppression, call queueing, and Pay over Voice.

## L1 Verified Account Restrictions

Accounts with L1 verification are restricted in the following ways when using Programmable Voice:

- All machine-generated speak commands are pre-pended with the announcement: "This is an automated call generated on the Telnyx platform, please report any abuse to fraud@telnyx.com". This currently applies to:
  - `/v2/calls`
  - `/v2/calls/:call_control_id/actions/transfer`
  - `/v2/calls/:call_control_id/actions/gather_using_audio`
  - `/v2/calls/:call_control_id/actions/gather_using_speak`
  - `/v2/calls/:call_control_id/actions/playback_start`
  - `/v2/calls/:call_control_id/actions/speak`
  - `/v2/calls/:call_control_id/actions/gather_using_ai`
  - `/v2/calls/:call_control_id/actions/ai_assistant_start`
  - The TeXML verbs: `Play`, `Say`, `AIGather`
- Limited to a maximum of 100 outbound calls per day.
- Limited to 10 outbound calls per hour.

## Sending Commands

A Voice API command is sent with a `call_control_id`. The `call_control_id` allows a user to communicate to Telnyx the `call_leg` to control, and helps Telnyx route the call to the location where the call is being managed, resulting in the lowest possible latency for Call Control interactions.

### Authentication

Like all other Telnyx API V2 requests, Voice API command requests must be authenticated by sending the `Authorization` header with an API Key value.

| Credential Type | HTTP Header Format |
| --- | --- |
| API Key | `Authorization: Bearer YOUR_API_KEY` |

### Example: Answering a Call

To answer a call, send a POST request to the `/actions/answer` endpoint:

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  https://api.telnyx.com/v2/calls/428c31b6-7af4-4bcb-b7f5-5013ef9657c1/actions/answer
```

### Available Commands and Expected Webhooks

| Command | Expected Webhooks |
| --- | --- |
| Answer call | `call.answered` |
| Bridge call | `call.bridged` for Leg A, `call.bridged` for Leg B |
| Dial | `call.initiated`, `call.answered` or `call.hangup`, `call.machine.detection.ended` (if `answering_machine_detection` was requested), `call.machine.greeting.ended` (if `answering_machine_detection` was requested to detect the end of machine greeting) |
| Forking start | `call.fork.started`, `call.fork.stopped` |
| Forking stop | `call.fork.stopped` |
| Gather using audio | `call.playback.started`, `call.playback.ended`, `call.dtmf.received` (many), `call.gather.ended` |
| Gather using speak | `call.dtmf.received` (many), `call.gather.ended` |
| Hangup | `call.hangup`, `call.recording.saved` (if the call is being recorded) |
| Play audio url | `call.playback.started`, `call.playback.ended` |
| Playback stop command | `call.playback.ended` or `call.speak.ended` |
| Recording start | no webhooks |
| Recording stop | `call.recording.saved` |
| Reject call | `call.hangup` |
| Send DTMF | no webhooks |
| Speak text | `call.speak.started`, `call.speak.ended` |
| Transfer call | `call.initiated`, `call.bridged` to Leg B, `call.answered` or `call.hangup` |

### Response Codes

| HTTP Status Code | Message | Description |
| --- | --- | --- |
| 200 | OK | The request succeeded. |
| 403 | Forbidden | The request was valid, however the user is not authorized to perform this action. |
| 404 | Not Found | The requested resource could not be found. |
| 422 | Invalid Parameters | The request has invalid parameters or the call is no longer active. |

## Receiving Webhooks

When a Voice API command is sent and a successful response (200 OK) is received, a webhook will be delivered to the primary URL specified on the Voice API Application associated with the call. If that URL does not resolve, or the application returns a non-200 OK response, the webhook will be delivered to the failover URL, if one has been specified.

To minimize webhook delivery time, Telnyx:

- Does not enforce the order in which webhooks are delivered.
- Retries webhook delivery if the application does not respond within a certain time threshold.

As a result, applications may encounter out-of-order, simultaneous (or near simultaneous), and duplicate webhooks. Duplicate webhooks may cause applications to issue duplicate commands. To instruct Telnyx to ignore duplicate commands, send a `command_id` parameter as part of commands. Commands with duplicate `command_id`s within 60 seconds will be ignored.

### Example Webhook

When an incoming call is placed to a number associated with a Voice API Application, a callback for the incoming call is received:

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

| Field | Description |
| --- | --- |
| `record_type` | Description of the record. |
| `event_type` | The type of event detected by the Telnyx system. |
| `id` | Unique id for the webhook. |
| `occurred_at` | ISO-8601 datetime of when the event occurred. |
| `call_control_id` | Call id used to issue commands via Voice API. |
| `connection_id` | Voice API App ID (formerly Telnyx connection ID) used in the call. |
| `call_leg_id` | ID that is unique to the call and can be used to correlate webhook events. |
| `call_session_id` | ID that is unique to the call session and can be used to correlate webhook events. A call session is a group of related call legs that logically belong to the same phone call, e.g. an inbound and outbound leg of a transferred call. |
| `client_state` | State received from a command. |
| `from` | Number or SIP URI placing the call. |
| `to` | Destination number or SIP URI of the call. |
| `direction` | Whether the call is 'incoming' or 'outgoing'. |
| `state` | Whether the call is in 'bridging' or 'parked' state. |
