---
title: Text-to-Speech Overview
summary: Synthesize natural speech from text via WebSocket streaming, REST API, or in-call playback.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/overview/index
    content_hash: 68f510d97d5f9206205d8e5e495d1e861e2bda4d61ebb1bc56521804f70f8dc4
updated_at: 2026-04-10T00:00:00Z
---

# Text-to-Speech Overview

Synthesize natural speech from text via WebSocket streaming, REST API, or in-call playback.

## 1. Choose your interface

  - [WebSocket Streaming](../runbooks/lifecycle-2.md) — Real-time streaming. Send text, receive audio chunks as they're synthesized.

  - [REST API](../runbooks/rest-api.md) — HTTP POST. Get audio back as binary, base64, or async URL. OpenAI SDK compatible.

  - [In-Call Playback](../runbooks/in-call-playback.md) — TTS during live calls via Call Control `speak` or TeXML ``.

## 2. Choose a pre-built voice

  - [Telnyx](../runbooks/telnyx.md) — Natural, NaturalHD, Ultra, Kokoro, Qwen3TTS.

  - [Third-Party Providers](../runbooks/aws-polly.md) — AWS Polly, Azure, ElevenLabs, Minimax, MurfAI, Rime, Resemble, Inworld.

## 3. Or create your own

  - [Voice Design Lab](../runbooks/voice-cloning.md) — Clone and design custom voices. Available on select providers: Qwen3TTS, Minimax, ElevenLabs, Resemble.


## Related Pages

- [Text-to-Speech](../runbooks/text-to-speech.md)
- [Text-to-Speech (TTS)](../runbooks/text-to-speech-tts.md)
