---
title: Text-to-Speech
summary: Telnyx Text-to-Speech (TTS) provides synthesized speech across multiple interfaces
  (WebSocket streaming, REST API, and in-call playback) and a broad set of providers,
  including Telnyx-native models (Natural, NaturalHD, KokoroTTS, Qwen3TTS, Ultra,
  Grok, Bayan, Sukhan) and third-party providers (AWS Polly, Azure, ElevenLabs, Minimax,
  MurfAI, Rime, Resemble, Inworld, Fish Audio). This page consolidates the provider
  catalogue, voice formats, configuration parameters, pronunciation dictionaries,
  SSML support, and integration patterns for each surface.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/in-call-playback
- url: https://developers.telnyx.com/docs/voice/tts/overview
- url: https://developers.telnyx.com/docs/voice/tts/pronunciation-dictionaries/index
- url: https://developers.telnyx.com/docs/voice/tts/providers/aws/index
- url: https://developers.telnyx.com/docs/voice/tts/providers/aws/ssml-tags
- url: https://developers.telnyx.com/docs/voice/tts/providers/azure
- url: https://developers.telnyx.com/docs/voice/tts/providers/elevenlabs
- url: https://developers.telnyx.com/docs/voice/tts/providers/fishaudio
- url: https://developers.telnyx.com/docs/voice/tts/providers/inworld
- url: https://developers.telnyx.com/docs/voice/tts/providers/minimax
- url: https://developers.telnyx.com/docs/voice/tts/providers/resemble
- url: https://developers.telnyx.com/docs/voice/tts/providers/rime
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/bayan
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/grok
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/index
updated_at: 2026-08-05T14:07:22Z
---

# Text-to-Speech

*Part 1 of 5 — see also: [Part 2](text-to-speech--part-2.md), [Part 3](text-to-speech--part-3.md), [Part 4](text-to-speech--part-4.md), [Part 5](text-to-speech--part-5.md)*

Telnyx Text-to-Speech (TTS) provides synthesized speech across multiple interfaces (WebSocket streaming, REST API, and in-call playback) and a broad set of providers, including Telnyx-native models (Natural, NaturalHD, KokoroTTS, Qwen3TTS, Ultra, Grok, Bayan, Sukhan) and third-party providers (AWS Polly, Azure, ElevenLabs, Minimax, MurfAI, Rime, Resemble, Inworld, Fish Audio). This page consolidates the provider catalogue, voice formats, configuration parameters, pronunciation dictionaries, SSML support, and integration patterns for each surface.

## Overview

Telnyx Text-to-Speech (TTS) exposes synthesized speech through three integration surfaces:

- **WebSocket Streaming** — real-time streaming. Send text, receive audio chunks as they are synthesized.
- **REST API** — HTTP POST. Get audio back as binary, base64, or async URL. OpenAI SDK compatible.
- **In-Call Playback** — TTS during live calls via Call Control `speak` or TeXML `<Say>`.

Voices are addressed using a `Provider.Model.VoiceId` format. All models (including Ultra) are available for in-call playback.
