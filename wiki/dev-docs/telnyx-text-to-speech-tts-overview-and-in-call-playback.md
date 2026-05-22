---
title: Telnyx Text-to-Speech (TTS) Overview and In-Call Playback
summary: 'A concise guide to Telnyx Text-to-Speech: how to generate audio via WebSocket
  streaming or REST, how to play TTS during live calls, available voice models and
  providers, and options for designing custom voices.'
sources:
- url: https://developers.telnyx.com/docs/voice/tts/overview/index
  content_hash: 2ac1743826e3714db988ee03fff1f97add834e43b200610395b33b05b957991c
- url: https://developers.telnyx.com/docs/voice/tts/in-call-playback
  content_hash: 02e185de3ea3d334d6f300ff50c264c1c6851dff03a886120e85b170ab8c69ec
updated_at: 2026-05-20T10:07:12Z
---

# Telnyx Text-to-Speech (TTS) Overview and In-Call Playback

A concise guide to Telnyx Text-to-Speech: how to generate audio via WebSocket streaming or REST, how to play TTS during live calls, available voice models and providers, and options for designing custom voices.

## Interfaces for Text-to-Speech
- WebSocket streaming: real-time synthesis where you send text and receive audio chunks as they’re generated.
- REST API: HTTP POST that returns audio as binary, base64, or an async URL; OpenAI SDK–compatible.
- In-call playback: speak during live calls via Voice API commands or TeXML.

## Voice Options and Providers
- Telnyx voices: Natural, NaturalHD, Ultra, Kokoro, Qwen3TTS, xAI Grok.
- Third-party providers: AWS Polly, Azure, ElevenLabs, Minimax, MurfAI, Rime, Resemble, Inworld.

## Custom Voices with Voice Design Lab
Clone and design custom voices on select providers: Qwen3TTS, Minimax, ElevenLabs, and Resemble.

## In-Call Playback Options
- Voice API: use the speak command to synthesize and play TTS on an active call (see Speak Text command reference: https://developers.telnyx.com/api-reference/call-commands/speak-text). Full Voice API docs: https://developers.telnyx.com/docs/voice/programmable-voice
- TeXML: use the <Say> element to play synthesized speech in call flows. TeXML docs: https://developers.telnyx.com/docs/voice/texml
- AI Assistants: configure the assistant’s voice model to enable spoken responses. AI Assistants overview: https://developers.telnyx.com/docs/inference/ai-assistants

## Voice Selection Format for In-Call TTS
In-call TTS uses the same voice identifier format as WebSocket and REST:

Provider.Model.VoiceId

All models (including Ultra) are supported for in-call playback.

## Resources and Next Steps
- Text-to-Speech overview: https://developers.telnyx.com/docs/voice/tts/overview
- WebSocket streaming docs (lifecycle, configuration, messages, errors, examples): https://developers.telnyx.com/docs/voice/tts/websocket-streaming
- REST API overview and reference: https://developers.telnyx.com/docs/voice/tts/rest-api
- Pronunciation dictionaries: https://developers.telnyx.com/docs/voice/tts/pronunciation-dictionaries
- Pricing for REST TTS: https://developers.telnyx.com/docs/voice/tts/rest-api/pricing
- In-call playback guide: https://developers.telnyx.com/docs/voice/tts/in-call-playback
