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

*Part 2 of 4 — see also: [Part 1](programmable-voice-l1-accounts-restirctions-to-sending-commands--part-1.md), [Part 3](programmable-voice-l1-accounts-restirctions-to-sending-commands--part-3.md), [Part 4](programmable-voice-l1-accounts-restirctions-to-sending-commands--part-4.md)*

A consolidated reference for Telnyx Programmable Voice covering account restrictions for L1 verified accounts, sending commands and receiving webhooks, media streaming over WebSockets, noise suppression, call queueing, and Pay over Voice.

## Media Streaming over WebSockets

Media Streaming provides instant access to raw call media. It enables use cases such as sentiment analysis, AI-powered resolutions, and bringing your own AI engine to connect directly to call control for custom AI-powered voice applications.

When a call is established, Telnyx forks the call media so recipients receive it simultaneously. The Telnyx network ensures that call media can be duplicated, delivered, analyzed, and returned in real-time. The secondary delivery recipient never occupies the call stream, so quality is not degraded and connections are not dropped.

### Requesting Streaming Using the Dial Command

The dial command can be extended to request streaming using WebSockets:

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{
    "connection_id": "uuid",
    "to": "+18005550199",
    "from": "+18005550100",
    "stream_url": "wss://yourdomain.com",
    "stream_track": "inbound_track|outbound_track|both_tracks"
  }' \
  https://api.telnyx.com/v2/calls
```

The following additional attributes must be added to the request:

- `stream_url` — the destination address where the stream will be delivered.
- `stream_track` — specifies which track should be streamed. Options: `inbound_track` (default), `outbound_track`, `both_tracks`.

A regular confirmation is returned:

```json
{
  "data": {
    "call_control_id": "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ",
    "call_leg_id": "2dc6fc34-f9e0-11ea-b68e-02420a0f7768",
    "call_session_id": "2dc1b3c8-f9e0-11ea-bc5a-02420a0f7768",
    "is_alive": false,
    "record_type": "call"
  }
}
```

### Requesting Streaming Using the Answer Command

Using the same attributes, streaming can be requested while answering the call:

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{
    "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
    "command_id": "891510ac-f3e4-11e8-af5b-de00688a4901",
    "stream_url": "wss://yourdomain.com",
    "stream_track": "inbound_track|outbound_track|both_tracks"
  }' \
  https://api.telnyx.com/v2/calls/{call_control_id}/actions/answer
```

The confirmation that the call has been answered includes streaming details.

### Streaming Process Flow

When the WebSocket connection is established, the following event is sent:

```json
{
  "event": "connected",
  "version": "1.0.0"
}
```

Before the stream begins, the `streaming.started` webhook is sent. An event over WebSockets is then sent containing information in the `mediaFormat` section about the encoding and a `stream_id` that identifies a particular stream:

```json
{
  "event": "start",
  "sequence_number": "1",
  "start": {
    "user_id": "3E6F995F-85F7-4705-9741-53B116D28237",
    "call_control_id": "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ",
    "call_session_id": "ff55a038-6f5d-11ef-9692-02420aeffb1f",
    "from": "+13122010094",
    "to": "+13122123456",
    "tags": ["TAG1", "TAG2"],
    "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
    "media_format": {
      "encoding": "PCMU",
      "sample_rate": 8000,
      "channels": 1
    }
  },
  "stream_id": "32DE0DEA-53CB-4B21-89A4-9E1819C043BC"
}
```

Media events follow the start event. The payload contains a base64-encoded RTP payload (no headers). The order of events is not guaranteed; the chunk number can be used to reorder events.

When the call ends, the `streaming.stopped` webhook is sent, followed by a `stop` event over the WebSocket connection.

Only one streaming/fork operation is supported per call. If media forking is requested, the WebSocket stream will be stopped and replaced by an RTP connection.

### Bidirectional Media Streaming

#### Sending RTP Stream

The RTP stream can be sent to the call using WebSocket by setting `stream_bidirectional_mode` to `rtp`:

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{
    "connection_id": "uuid",
    "to": "+18005550199",
    "from": "+18005550100",
    "stream_url": "wss://yourdomain.com",
    "stream_track": "inbound_track|outbound_track|both_tracks",
    "stream_bidirectional_mode": "rtp"
  }' \
  https://api.telnyx.com/v2/calls
```

It can be requested using the `answer` and `streaming_start` commands in the same way. RTP streaming can be sent using media events:

```json
{
  "event": "media",
  "media": {
    "payload": "your base64 encoded RTP stream"
  }
}
```

Provided chunks of audio can be 20 milliseconds to 30 seconds in size. The number of bidirectional RTP streams per call is limited to 1.

#### RTP Stream Codec

Supported codecs for bidirectional streaming:

- PCMU, 8 kHz (default)
- PCMA, 8 kHz
- G722, 8 kHz
- OPUS, 8 kHz, 16 kHz
- AMR-WB, 8 kHz, 16 kHz
- L16, 16 kHz

When audio is sent using a different encoding than on the call, it will be transcoded, which may cause a degradation in quality. The L16 codec provides improved support for AI voice agent integrations by offering reduced latency and eliminating transcoding overhead when interfacing with many AI platforms that natively support linear PCM audio.

The codec can be set when streaming start is requested using `stream_bidirectional_codec`.

#### Sending Media Files

Media files can be sent back to the call through the WebSocket, similar to the `playback_start` command when using a base64-encoded mp3 file in the payload:

```json
{
  "event": "media",
  "media": {
    "payload": "your base64 encoded mp3 file"
  }
}
```

The payload, which is a base64-encoded mp3 file, will be played on the call. Multiple media messages will be queued and played in the order they were submitted. Limitations:

- Media payloads can only be submitted once per second.
- Media must be base64 encoded mp3.

#### Clear Message

Sending a clear message immediately stops the media playing on the stream and clears the media queue:

```json
{
  "event": "clear"
}
```

#### Mark Message

Mark messages can be used to keep track of media ending on the stream:

- A mark message can be sent to the stream after a media message.
- When the media immediately preceding the mark finishes, the same mark is received back.

Example mark message sent to the stream:

```json
{
  "event": "mark",
  "mark": {
    "name": "some_mark_name"
  }
}
```

Example mark message received from the stream:

```json
{
  "event": "mark",
  "stream_id": "32DE0DEA-53CB-4B21-89A4-9E1819C043BC",
  "sequence_number": "5",
  "mark": {
    "name": "some_mark_name"
  }
}
```

Submitting marks when no audio is played or queued will result in them being immediately sent back. Similarly, the `clear` message will also result in all queued marks being sent back.

#### DTMF Message

In case of DTMF events on the call, the following message is sent over WebSocket:

```json
{
  "event": "dtmf",
  "stream_id": "32DE0DEA-53CB-4B21-89A4-9E1819C043BC",
  "occurred_at": "2025-06-05T08:54:19.698408Z",
  "sequence_number": "5",
  "dtmf": {
    "digit": "1"
  }
}
```

The `occurred_at` field is a timestamp captured on the Telephony engine side. These are consumed as asynchronous events and in certain circumstances may arrive out of order. This field can be used to ensure proper order.

#### Error Message

In case of any error during media streaming, an error frame is sent:

```json
{
  "event": "error",
  "payload": {
    "code": 100002,
    "title": "unknown_error",
    "detail": "An unknown error occurred on the stream"
  },
  "stream_id": "uuid"
}
```

| Code | Title | Description |
| --- | --- | --- |
| 100002 | `unknown_error` | An unknown error occurred on the stream |
| 100003 | `malformed_frame` | Received frame was not formed correctly |
| 100004 | `invalid_media` | Media provided was not base64 encoded |
| 100005 | `rate_limit_reached` | Too many requests |

#### Example Integrations

The Telnyx GitHub repository contains several examples of integrations with external services using Media streaming:

- [Simple application that handles websocket streaming and provides transcription using Node JS](https://github.com/team-telnyx/demo-node-telnyx/tree/master/websocket-demos/websocket)
- [Integration with DeepGram transcription engine using Node JS](https://github.com/team-telnyx/demo-node-telnyx/tree/master/websocket-demos/websocket-deepgram-transcription)
- [Integration with OpenAI speech-2-speech engine using Node JS](https://github.com/team-telnyx/demo-node-telnyx/tree/master/websocket-demos/websoket-openai-demo)
- [Pipecat Telnyx Chatbot in Python](https://github.com/pipecat-ai/pipecat-examples/tree/main/telnyx-chatbot)
