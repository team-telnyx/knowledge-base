---
title: Telnyx Voice API Resources
summary: Covers the TeXML REST API resource types—applications, calls, conferences,
  queues, recordings, SIPREC sessions, streams, transcriptions, and secrets—along
  with the Text-to-Speech system including in-call playback and pronunciation dictionaries.
sources:
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/applications/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/calls/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/conference-participants/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/conferences/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/queues/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/recordings/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/secrets/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/siprec/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/streams/index
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/transcripts/index
- url: https://developers.telnyx.com/docs/voice/tts/in-call-playback
- url: https://developers.telnyx.com/docs/voice/tts/overview/index
- url: https://developers.telnyx.com/docs/voice/tts/pronunciation-dictionaries/index
updated_at: 2026-06-11T10:46:12Z
---

# Telnyx Voice API Resources

*Part 2 of 3 — see also: [Part 1](telnyx-voice-api-resources--part-1.md), [Part 3](telnyx-voice-api-resources--part-3.md)*

Covers the TeXML REST API resource types—applications, calls, conferences, queues, recordings, SIPREC sessions, streams, transcriptions, and secrets—along with the Text-to-Speech system including in-call playback and pronunciation dictionaries.

## Recordings and Transcriptions

A recording object represents an audio recording generated during a call or conference. It tracks metadata such as format, duration, start/end times, and storage locations.

### Creating recordings

Recordings are created in the following situations:

1. **Outbound call with recording enabled via REST API** — Telnyx begins recording when the call is answered. ([Initiate an outbound call](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call))
2. **`<Record>` verb** — Each execution produces a distinct recording object. ([`<Record>` documentation](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record))
3. **`<Dial>` with recording attributes** — Recording begins when the outbound call leg is created. ([`<Dial>` documentation](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial))
4. **`<Dial>` to `<Conference>` with recording** — Conference recording is initiated. ([`<Conference>` documentation](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference))
5. **REST API manual start** — Dynamically triggered on any existing call. ([Request recording for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/request-recording-for-a-call))
6. **Conference participant dialed with recording** — Recording starts for the participant or entire session. ([Dial a new conference participant](https://developers.telnyx.com/api-reference/texml-rest-commands/dial-a-new-conference-participant))

### Fetching recordings

Recordings can be retrieved by:

- Recording ID — [Fetch recording resource](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recording-resource)
- Conference ID — [Fetch recordings for a conference](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recordings-for-a-conference)
- Call ID — [Fetch recordings for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-recordings-for-a-call)

### Controlling ongoing recordings

Active recordings can be managed via the [Update recording on a call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-recording-on-a-call) endpoint.

### Transcriptions

Transcriptions are enabled from TeXML in two scenarios:

1. **`<Transcription>` verb** — Telnyx initiates audio capture based on the verb's parameters and provides transcription results in status callbacks in real-time. ([`<Transcription>` documentation](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription))
2. **`<Record>` with transcription attributes** — Transcription is performed on the recorded audio once the recording is complete.

Completed transcriptions can be retrieved via the [Fetch a recording transcription resource](https://developers.telnyx.com/api-reference/texml-rest-commands/fetch-a-recording-transcription-resource) endpoint.

## SIPREC Sessions

A SIPREC session represents an active SIP Client Recording media session associated with a call. SIPREC enables delivery of call media to an external SIP recording server for compliance recording, monitoring, or archival. SIPREC client connectors must be configured in your Telnyx account beforehand. See the [SIPREC client tutorial](https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client) for setup information.

### Creating SIPREC sessions

1. **REST API** — Explicitly request a SIPREC session for an active call. Allows dynamic initiation at any point during the call lifecycle. ([Request a SIPREC session for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/request-siprec-session-for-a-call))
2. **`<Siprec>` verb** — Initiated synchronously when nested inside a `<Start>` verb as part of sequential TeXML execution. Subsequent instructions are processed only after the SIPREC session has been stopped. ([`<Siprec>` documentation](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec))

### Managing SIPREC sessions

Active SIPREC sessions can be updated or stopped via the [Update a SIPREC session for a call](https://developers.telnyx.com/api-reference/texml-rest-commands/updates-siprec-session-for-a-call) endpoint.

## Media Streams

A stream object represents an active media streaming session from a call, delivering real-time audio to an external destination via WebSockets.

### Creating streams

1. **REST API** — Explicitly start streaming from an active call. Allows dynamic initiation at any point during the call lifecycle. ([Start streaming media from a call](https://developers.telnyx.com/api-reference/texml-rest-commands/start-streaming-media-from-a-call))
2. **`<Stream>` verb** — Two operational modes:
   - **Asynchronous via `<Start>`** — Streaming begins in parallel with the ongoing call flow without interrupting other TeXML instructions.
   - **Synchronous via `<Connect>`** — The call flow waits for streaming to stop before proceeding to the next instruction.

In both cases, a stream object is created and associated with the active call.

### Managing and stopping streams

Active streams can be updated or stopped via the [Update streaming on a call](https://developers.telnyx.com/api-reference/texml-rest-commands/update-streaming-on-a-call) endpoint. When streaming stops, the stream object transitions to a completed state and WebSockets are closed.

## Secrets

The TeXML Secrets API provides a secure mechanism for storing, managing, and retrieving sensitive information required by TeXML applications—credentials, API keys, tokens, and other confidential values that should not be hardcoded into TeXML documents or exposed in source code. See the [tutorial on using secrets](https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests#using-secrets) for more information.

Secrets are created via the [Create a TeXML secret](https://developers.telnyx.com/api-reference/texml-rest-commands/create-a-texml-secret) endpoint.

## Text-to-Speech Overview

Telnyx TTS offers three integration interfaces:

- **WebSocket Streaming** — Real-time streaming. Send text, receive audio chunks as they are synthesized.
- **REST API** — HTTP POST returning audio as binary, base64, or async URL. OpenAI SDK compatible.
- **In-Call Playback** — TTS during live calls via Call Control `speak` or TeXML `<Say>`.

### Voice selection

Pre-built voices are available from Telnyx (Natural, NaturalHD, Ultra, Kokoro, Qwen3TTS, xAI Grok) and third-party providers (AWS Polly, Azure, ElevenLabs, Minimax, MurfAI, Rime, Resemble, Inworld). Custom voices can be created using Voice Design Lab (available on select providers: Qwen3TTS, Minimax, ElevenLabs, Resemble).

The voice format is `Provider.Model.VoiceId` and all models including Ultra are available for in-call playback.

### In-Call TTS Playback

In-call TTS plays synthesized speech during live voice calls:

- **Voice API** — Use the [`speak`](https://developers.telnyx.com/api-reference/call-commands/speak-text) command on an active call.
- **TeXML** — Use the `<Say>` element within a `<Response>`.
- **AI Assistants** — TTS is used for voice output; configure the voice model in assistant settings.
