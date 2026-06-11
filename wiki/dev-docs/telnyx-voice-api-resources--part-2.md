---
title: Telnyx Voice API Resources
summary: Covers the TeXML REST API resource types—applications, calls, conferences,
  queues, recordings, SIPREC sessions, streams, transcriptions, and secrets—along
  with the Text-to-Speech system including in-call playback and pronunciation dictionaries.
sources:
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/applications/index
  content_hash: f2dc8ac0555aca4b1bc5cd8f6f0026e03d4f9302d0673a200734b2d78307ae27
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/calls/index
  content_hash: c4a93404708f0041869ea616e4776fee88b838677ab29bb77da46c5c37443fb1
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/conference-participants/index
  content_hash: 3dface952c3f9b06f20ab0ecca13b7b27503ed79861f155f05e97188a61dd5d2
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/conferences/index
  content_hash: dd9e4f35eadb36349dbcb062174031b45f97dbc4d52ca9ad93e1c9430a28d5f9
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/queues/index
  content_hash: 0b2aa6aa69905f12a4ea2a55bae0611bdedb35eadd23bff1b524e92e38693f6a
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/recordings/index
  content_hash: 562e866ba4e13aa4db303517917af30a402332f8c15aeb07d5ee0c8102522a21
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/secrets/index
  content_hash: 337a951a0d85b95e330c046de3232278072c410693f92ee6657c029a50fff146
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/siprec/index
  content_hash: 725be89e6deaff2d5e5a1a563d27ed8bc11e925d73b65a7a1e24d65434bb5bf9
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/streams/index
  content_hash: 56e64cf84743db7b33171b5fe084e558dcac20f2ec451806613bf05171639417
- url: https://developers.telnyx.com/docs/voice/texml/rest-api/transcripts/index
  content_hash: b323b65fe70abd1d1e4219d06bf9bd1882014e5d2fc5e4fd7fce97ca71dc24cb
- url: https://developers.telnyx.com/docs/voice/tts/in-call-playback
  content_hash: de08a5759d5522f0e6336ebfdcbffa6cf8b693a345982cb4c53cd65d42f8b6b3
- url: https://developers.telnyx.com/docs/voice/tts/overview/index
  content_hash: 0e4dafb6ba3146321a9be9ed2b4904eacdc54b2f5f88d57eb662abe749ab6054
- url: https://developers.telnyx.com/docs/voice/tts/pronunciation-dictionaries/index
  content_hash: d8aa81fc59d3ddfffb8692e4e6e6f0671d67f8be426d479a7953913d5b6803fd
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
