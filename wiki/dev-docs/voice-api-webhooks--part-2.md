---
title: Voice API Webhooks
summary: Voice API webhooks are HTTP callbacks that notify your application in real
  time when events occur during a call. Each event delivers a JSON payload to a configured
  URL, and your application can respond with call control commands to drive the call
  flow.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks
updated_at: 2026-08-05T14:04:53Z
---

# Voice API Webhooks

*Part 2 of 2 — see also: [Part 1](voice-api-webhooks--part-1.md)*

Voice API webhooks are HTTP callbacks that notify your application in real time when events occur during a call. Each event delivers a JSON payload to a configured URL, and your application can respond with call control commands to drive the call flow.

## Event types

The following event types are fired by the Voice API. Each event type appears in the `event_type` field of the webhook payload.

### Call state

| Event | Description | Triggered by |
| --- | --- | --- |
| `call.initiated` | A new call leg has been created | [Dial](https://developers.telnyx.com/api-reference/call-commands/dial), [Transfer](https://developers.telnyx.com/api-reference/call-commands/transfer-call), or an inbound call |
| `call.answered` | The call has been answered | [Answer](https://developers.telnyx.com/api-reference/call-commands/answer-call), or remote party picks up |
| `call.hold` | The call has been placed on hold | The call is held |
| `call.unhold` | The call has been taken off hold | The call is unheld |
| `call.hangup` | The call has ended | [Hangup](https://developers.telnyx.com/api-reference/call-commands/hangup-call), Reject, or remote hangup |
| `call.bridged` | Two call legs have been connected | [Bridge](https://developers.telnyx.com/api-reference/call-commands/bridge-calls), [Transfer](https://developers.telnyx.com/api-reference/call-commands/transfer-call) |

### Audio playback

| Event | Description | Triggered by |
| --- | --- | --- |
| `call.playback.started` | Audio file playback has started | [Play audio](https://developers.telnyx.com/api-reference/call-commands/play-audio-url), [Gather using audio](https://developers.telnyx.com/api-reference/call-commands/gather-using-audio) |
| `call.playback.ended` | Audio file playback has finished | Playback completes or [Stop playback](https://developers.telnyx.com/api-reference/call-commands/stop-audio-playback) |
| `call.speak.started` | Text-to-speech playback has started | [Speak text](https://developers.telnyx.com/api-reference/call-commands/speak-text) |
| `call.speak.ended` | Text-to-speech playback has finished | Speak completes or [Stop playback](https://developers.telnyx.com/api-reference/call-commands/stop-audio-playback) |

### DTMF and gather

| Event | Description | Triggered by |
| --- | --- | --- |
| `call.dtmf.received` | A DTMF digit was received | Caller presses keypad during [Gather using audio](https://developers.telnyx.com/api-reference/call-commands/gather-using-audio) or [Gather using speak](https://developers.telnyx.com/api-reference/call-commands/gather-using-speak) |
| `call.gather.ended` | A gather operation has completed | Gather finishes (timeout, max digits, or terminating key) |

### Recording

| Event | Description | Triggered by |
| --- | --- | --- |
| `call.recording.saved` | A call recording has been saved | [Recording stop](https://developers.telnyx.com/api-reference/call-commands/recording-stop), or call ends while recording |

### Answering machine detection (AMD)

| Event | Description | Triggered by |
| --- | --- | --- |
| `call.machine.detection.ended` | Standard AMD has determined human vs. machine | [Dial](https://developers.telnyx.com/api-reference/call-commands/dial) with `answering_machine_detection` enabled |
| `call.machine.greeting.ended` | Machine greeting has finished (beep detected) | [Dial](https://developers.telnyx.com/api-reference/call-commands/dial) with `answering_machine_detection` set to detect greeting end |
| `call.machine.premium.detection.ended` | Premium AMD has determined human vs. machine | [Dial](https://developers.telnyx.com/api-reference/call-commands/dial) with premium AMD enabled |
| `call.machine.premium.greeting.ended` | Premium AMD greeting/beep detection completed | [Dial](https://developers.telnyx.com/api-reference/call-commands/dial) with premium AMD greeting detection |

### Media forking

| Event | Description | Triggered by |
| --- | --- | --- |
| `call.fork.started` | Media forking has started | [Forking start](https://developers.telnyx.com/api-reference/call-commands/forking-start) |
| `call.fork.stopped` | Media forking has stopped | [Forking stop](https://developers.telnyx.com/api-reference/call-commands/forking-stop), or call ends |

### Queue

| Event | Description | Triggered by |
| --- | --- | --- |
| `call.enqueued` | Call was placed in a queue | [Enqueue](https://developers.telnyx.com/api-reference/call-commands/enqueue-call) |
| `call.dequeued` | Call was removed from a queue | Dequeue command or call ends |

### Transcription

| Event | Description | Triggered by |
| --- | --- | --- |
| `call.transcription` | Real-time transcription data received | [Transcription start](https://developers.telnyx.com/api-reference/call-commands/transcription-start) |

### Streaming

| Event | Description | Triggered by |
| --- | --- | --- |
| `streaming.started` | Media streaming has started | [Streaming start](https://developers.telnyx.com/api-reference/call-commands/streaming-start) |
| `streaming.stopped` | Media streaming has stopped | [Streaming stop](https://developers.telnyx.com/api-reference/call-commands/streaming-stop), or call ends |

## Response codes

Your webhook endpoint's HTTP response determines whether delivery is considered successful:

| Code | Meaning | Behavior |
| --- | --- | --- |
| **2xx** | Success | Webhook acknowledged |
| **3xx** | Redirect | Followed (up to 3 redirects) |
| **408, 429** | Timeout / Rate limited | Retried |
| **Other 4xx** | Client error | Not retried |
| **5xx** | Server error | Retried |

## Debugging deliveries

Use the [Webhook Deliveries API](https://developers.telnyx.com/api-reference/webhooks/list-webhook-deliveries) to inspect delivery history for your account. You can filter by status, event type, and time range — useful for diagnosing missed or failed webhooks.

```bash
# List failed voice webhook deliveries from the last hour
curl -X GET "https://api.telnyx.com/v2/webhook_deliveries?filter[status][eq]=failed&filter[event_type]=call.initiated" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Each delivery record includes the full webhook payload, HTTP status codes, and attempt-level details (request/response headers and bodies). See [Get a webhook delivery](https://developers.telnyx.com/api-reference/webhooks/find-webhook_delivery-details-by-id) for the full response schema.

## Best practices

1. **Return 2xx immediately** — acknowledge receipt within a few seconds, then process asynchronously.
2. **Implement idempotency** — webhooks may be delivered more than once. Use the event `id` to deduplicate.
3. **Verify signatures** — validate the `Telnyx-Signature-Ed25519` header to confirm webhook authenticity. See [Webhook signing](https://developers.telnyx.com/development/api-fundamentals/webhooks/receiving-webhooks#webhook-signing).
4. **Use `command_id`** — include a `command_id` in your call control commands to prevent duplicate command processing. Commands with duplicate IDs within 60 seconds are ignored.
5. **Monitor failures** — track failed webhook deliveries and configure a failover URL for critical applications.
