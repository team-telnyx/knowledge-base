---
title: Speech-to-Text
summary: 'Telnyx Speech-to-Text (STT) transcribes audio to text via three integration
  paths: WebSocket streaming for real-time partial and final transcripts, a REST API
  for synchronous file-based transcription, and in-call transcription for live voice
  calls. The platform supports multiple engines (Deepgram, Telnyx-hosted Whisper,
  Google, Azure, xAI, AssemblyAI, Speechmatics, Soniox, Parakeet, Reson8) selectable
  per request, with a single global endpoint and Bearer-token authentication.'
sources:
- url: https://developers.telnyx.com/docs/voice/stt/getting-started
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
- url: https://developers.telnyx.com/docs/voice/stt/migration
- url: https://developers.telnyx.com/docs/voice/stt/models
- url: https://developers.telnyx.com/docs/voice/stt/overview
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/index
updated_at: 2026-08-05T14:06:51Z
---

# Speech-to-Text

*Part 1 of 7 — see also: [Part 2](speech-to-text--part-2.md), [Part 3](speech-to-text--part-3.md), [Part 4](speech-to-text--part-4.md), [Part 5](speech-to-text--part-5.md), [Part 6](speech-to-text--part-6.md), [Part 7](speech-to-text--part-7.md)*

Telnyx Speech-to-Text (STT) transcribes audio to text via three integration paths: WebSocket streaming for real-time partial and final transcripts, a REST API for synchronous file-based transcription, and in-call transcription for live voice calls. The platform supports multiple engines (Deepgram, Telnyx-hosted Whisper, Google, Azure, xAI, AssemblyAI, Speechmatics, Soniox, Parakeet, Reson8) selectable per request, with a single global endpoint and Bearer-token authentication.

## Overview

Telnyx STT transcribes audio to text in three ways:

- **WebSocket Streaming** — Stream audio over a persistent WebSocket connection. Real-time partial and final transcripts.
- **File-Based Transcription** — Upload audio files via REST API. OpenAI-compatible endpoint.
- **In-Call Transcription** — Enable transcription during live voice calls via Call Control or TeXML.

All three paths use a single global endpoint and Bearer-token authentication with a Telnyx API key.

## Prerequisites

- A Telnyx account — [sign up here](https://telnyx.com/sign-up)
- An API key — create one in the [portal](https://portal.telnyx.com/#/app/api-keys)

No other setup is required.
