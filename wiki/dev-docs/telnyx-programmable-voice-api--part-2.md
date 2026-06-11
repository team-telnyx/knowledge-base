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

*Part 2 of 3 — see also: [Part 1](telnyx-programmable-voice-api--part-1.md), [Part 3](telnyx-programmable-voice-api--part-3.md)*

The Telnyx Programmable Voice API enables integration of voice calling capabilities into applications, providing granular control over inbound and outbound calls through commands, webhooks, media streaming, IVR, call queueing, noise suppression, and SIPREC recording.

## Building IVR Applications

Interactive Voice Response (IVR) applications are built by reacting to webhook events with Voice API commands. The basic IVR flow is:

1. **Answer the incoming call** — respond to `call.initiated` with the `answer` command.
2. **Present options** — on `call.answered`, use `gather_using_speak` to play a prompt and collect DTMF input.
3. **Interpret button presses** — on `call.gather.ended`, extract `digits` from the payload and act accordingly (e.g. `transfer`, `bridge`, `hangup`).

### Python with Flask

Install dependencies:

```bash
pip install flask telnyx python-dotenv
```

Set environment variables `TELNYX_API_KEY` and `TELNYX_PUBLIC_KEY` in a `.env` file. A Flask route receives webhooks, parses `request.json['data']`, checks `record_type` and `event_type`, and issues commands via the `telnyx` SDK.

Use `client_state` (Base64-encoded) to distinguish inbound from outbound legs. For example, encode the call direction into `client_state` when answering, then check for its presence on `call.answered` before presenting the gather prompt — this prevents the transferred leg from also hearing the IVR.

A reusable `IVR` class can generate prompts from a JSON config file, mapping digits to phone numbers for transfer.

### Node.js with Express

Install dependencies:

```bash
npm install telnyx express --save
```

Store API key, connection ID, and forwarding number in a config module. Construct `client_state` as a JSON object Base64-encoded with `Buffer.from(JSON.stringify(state)).toString("base64")`. Decode on receipt with `Buffer.from(encoded, "base64").toString("ascii")`.

A Find Me/Follow Me IVR flow:
1. On `call.initiated` (incoming), dial the forwarding number with `client_state` set to `stage-bridge` and the bridge ID stored inside.
2. On `call.answered` with `client_state` of `stage-bridge`, issue `gather_using_speak` with accept/reject options and update `client_state` to `stage-dial`.
3. On `call.gather.ended`, if digit is `1` bridge the calls; if `2`, answer the parked call for voicemail and hang up the forwarded leg.

Every webhook must be replied to with `200 OK`, otherwise Telnyx will retry delivery.

### Ruby with Sinatra

Install gems:

```bash
gem install telnyx sinatra dotenv
```

Set `TELNYX_API_KEY`, `TELNYX_PUBLIC_KEY`, and `TELNYX_APP_PORT` in `.env`. Create a `Telnyx::Call` object from the webhook's `call_control_id` and use a `case` statement on `event_type` to dispatch commands.

The `gather_using_speak` command accepts `valid_digits` to restrict input and `invalid_payload` for the message played on invalid entry. On `call.gather.ended`, check that `status` is not `call_hangup` before using `speak`.

### Exposing Local Servers with Ngrok

All three approaches require exposing the local server to the internet for webhook delivery. [Ngrok](https://ngrok.com/) tunnels a local port to a public URL. Run `ngrok http <port>` and add the resulting URL (e.g. `https://abc123.ngrok.io/webhook`) to the Voice API Application's webhook URL field in the Mission Control Portal.

## Media Streaming

Media Streaming provides instant access to raw call media over WebSockets, enabling sentiment analysis, AI-powered voice applications, and real-time media forking without degrading call quality.

### Requesting Streaming

Add `stream_url` and `stream_track` to either the **Dial** or **Answer** command:

- `stream_url` — the WebSocket destination address (e.g. `wss://yourdomain.com`)
- `stream_track` — which track to stream: `inbound_track` (default), `outbound_track`, or `both_tracks`

When the WebSocket connection is established, a `connected` event is sent. Then a `start` event provides metadata including `call_control_id`, `call_session_id`, `from`, `to`, `client_state`, `tags`, `media_format` (encoding, sample rate, channels), and `stream_id`.

Media events follow, each containing a Base64-encoded RTP payload (no headers) in the `payload` field. Event order is not guaranteed; use `chunk` numbers for reassembly. A `streaming.started` webhook is also sent, and when the call ends a `streaming.stopped` webhook and a WebSocket `stop` event are delivered.

Only one streaming/fork operation is supported per call. If RTP forking is requested, the WebSocket stream will be stopped and replaced.

### Bidirectional Media Streaming

Set `stream_bidirectional_mode` to `rtp` to enable sending RTP back to the call via WebSocket. Send media events with Base64-encoded RTP payloads in chunks of 20 ms to 30 seconds. Only one bidirectional RTP stream per call is supported.

#### Supported Bidirectional Codecs

- PCMU, 8 kHz (default)
- PCMA, 8 kHz
- G722, 8 kHz
- OPUS, 8 kHz / 16 kHz
- AMR-WB, 8 kHz / 16 kHz
- L16, 16 kHz (reduced latency, no transcoding overhead for AI integrations)

Set the codec with the `stream_bidirectional_codec` parameter on dial, answer, or streaming start commands. Audio sent in a different encoding than the call's native codec will be transcoded, which may degrade quality.

### Sending Media Files

Send Base64-encoded MP3 files through the WebSocket. Payloads are queued and played in order. Limitations: one media payload per second; must be Base64-encoded MP3.

### WebSocket Control Messages

- **Clear** (`{"event": "clear"}`) — immediately stops playback and clears the media queue.
- **Mark** — send a mark after a media message; when the preceding media finishes, the same mark is returned. Marks on idle streams are returned immediately; clearing also returns all queued marks.
- **DTMF** — DTMF events on the call are delivered over the WebSocket with `digit`, `occurred_at`, and `sequence_number` fields. The `occurred_at` timestamp is captured server-side and can be used to ensure proper ordering since events may arrive out of order.
- **Error** — sent when something goes wrong, with codes: `100002` (unknown error), `100003` (malformed frame), `100004` (invalid media — not Base64), `100005` (rate limit reached).

### Example Integrations

- [Node.js WebSocket handler with transcription](https://github.com/team-telnyx/demo-node-telnyx/tree/master/websocket-demos/websocket)
- [DeepGram transcription integration](https://github.com/team-telnyx/demo-node-telnyx/tree/master/websocket-demos/websocket-deepgram-transcription)
- [OpenAI speech-to-speech integration](https://github.com/team-telnyx/demo-node-telnyx/tree/master/websocket-demos/websoket-openai-demo)
- [Pipecat chatbot in Python](https://github.com/pipecat-ai/pipecat-examples/tree/main/telnyx-chatbot)
