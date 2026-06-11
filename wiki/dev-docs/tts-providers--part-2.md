---
title: TTS Providers
summary: Telnyx supports multiple text-to-speech providers — both native models and
  third-party services — accessible via WebSocket and REST APIs. Each provider has
  a unique voice format, set of models, audio formats, and voice settings.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/providers/aws
  content_hash: d05a4afe85f843d6710bf894dad997b1074e3d796c95417ea88b85ffe206d865
- url: https://developers.telnyx.com/docs/voice/tts/providers/azure
  content_hash: ec654193582d0de541ccd10d2b9c91c46ebe5cde8f1b552d2c2ae98c0c1c409a
- url: https://developers.telnyx.com/docs/voice/tts/providers/elevenlabs
  content_hash: 32a948591f660725456b7ce9e639a58557dec9e11546920bbc31b19f464d5f4e
- url: https://developers.telnyx.com/docs/voice/tts/providers/inworld
  content_hash: d5255967f509383759422b1889672e345e5df624a4cfa3b626c77b257cbf07c3
- url: https://developers.telnyx.com/docs/voice/tts/providers/minimax
  content_hash: b2a79b1c7d96a37478b64c29fe2726e9eb8d8fe7545ebae1b5493c75505f5378
- url: https://developers.telnyx.com/docs/voice/tts/providers/resemble
  content_hash: 18fa0871d70a11377bad2bad9c7e67270d840d55e971ce92cf5d7070489e1333
- url: https://developers.telnyx.com/docs/voice/tts/providers/rime
  content_hash: 644141bdaf60a8b3e08c6c42c4415d260c1a901cf7f547ede8b79dc965717164
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/grok
  content_hash: 74bae8c62d9b96f88cb6c4906a2f6f94e9c7648edd770d690680b0196052a423
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/index
  content_hash: c1e50146224fdc6777fcd587538087c7229ba397b8f444876e841e839b5dabdd
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/kokoro
  content_hash: 41f6e37a603b4f04f48249564d4849795a849a130d4d97709cb491f8451562a9
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/natural
  content_hash: 8af10e9cf2009f34fe647cf6d34d7927f3ab9b94ea37dea97034a1b4b2e54584
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/naturalhd
  content_hash: 6bb820b1ff640ca6c0a2f553514fa97505f0421cf49b3996098e1ec45794e426
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/qwen3
  content_hash: ba5954984204d13271e9c6acff63722223d58dbf02389747a912a211f10c78b6
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/ultra
  content_hash: 24123eae6b0b848336c53d08df750e3a3eae5004b5bdb84a2ab4a6d79218cf3f
- url: https://developers.telnyx.com/docs/voice/tts/providers/xai
  content_hash: f1bd1d14cb4623fd04fbdcffca4d08cc7bd93791776595d8ee3f1c7df111c142
updated_at: 2026-06-11T10:46:51Z
---

# TTS Providers

*Part 2 of 2 — see also: [Part 1](tts-providers--part-1.md)*

Telnyx supports multiple text-to-speech providers — both native models and third-party services — accessible via WebSocket and REST APIs. Each provider has a unique voice format, set of models, audio formats, and voice settings.

## Third-Party Providers

### AWS Polly

Voice format: `aws.Polly.<Engine>.<VoiceId>`. The engine can also be parsed from a hyphenated suffix on the voice ID (e.g., `Lucia-longform` resolves to engine `long-form`).

**WebSocket** — audio formats: `mp3`, `linear16`, `ogg_vorbis`. Sample rates: 8000, 16000, 22050, 24000. Supports `text_type` of `text` or `ssml`. Voice settings include `engine` (`standard`, `neural`, `generative`, `long-form`), `output_format`, `sample_rate`, `lexicon_names`, `language_code`, and `text_type`.

**REST** — same fields plus `output_type`. Supports `binary_output` (chunked audio), `base64_output` (JSON with base64 audio), or `audio_id` (JSON with `audio_url` for deferred retrieval).

### Azure Speech

Voice format: `azure.<VoiceId>` (flat identifiers, no model segment). Default voice: `en-US-AvaMultilingualNeural`.

**WebSocket** — audio formats: `mp3`, `wav`, `linear16`, `mulaw`, `alaw`. Default sample rate 24000; supports 8000, 16000, 24000, 48000. Supports SSML. Voice settings include `output_format` (Azure format string, default `audio-24khz-160kbitrate-mono-mp3`), `language_code`, `text_type`, `effect` (`eq_car`, `eq_telecomhp8k`), and `gender` (`Male`, `Female`).

**REST** — same fields plus `output_type`.

### ElevenLabs

Voice format: `elevenlabs.<Model>.<VoiceId>`. Requires your own API key configured in your Telnyx account. The `voice_id` references a voice from your own ElevenLabs account (pre-built, cloned, or designed). Preview voices at [elevenlabs.io/voice-library](https://elevenlabs.io/voice-library). Voice settings are relayed directly to the ElevenLabs API.

**WebSocket** — audio formats: `mp3`, `linear16`, `mulaw`. Sample rates: 8000–44100. Voice settings: `model_id`, `language_code`, `stability` (0.0–1.0), `similarity_boost` (0.0–1.0), `style` (0.0–1.0), `use_speaker_boost` (boolean).

**REST** — same voice settings fields plus `output_type`.

### Rime

Voice format: `Rime.<Model>.<VoiceId>`. Two models: **Coda** (flagship as of May 2026, LLM backbone, sub-100ms latency, 184 voices, supports en, es, fr, pt, de, ja) and **ArcanaV3** (previous flagship, expressive multilingual codeswitching, supports ar, en, fr, de, he, hi, ja, pt, es, ta). Coda is recommended for new integrations — it surpasses ArcanaV3 in naturalness, prosody, and artifact-free output.

**WebSocket** — audio formats: `mp3`, `linear16`. Default sample rate 24000; supports up to 96000. Voice settings: `voice_speed` (float, default `1.0`).

**REST** — same fields plus `output_type`.

### Minimax

Voice format: `minimax.<Model>.<VoiceId>`. The `voice_id` can be a system voice (pre-built) or a cloned voice from the Voice Design Lab (organization-scoped).

**WebSocket** — audio formats: `mp3`, `linear16`. Default sample rate 24000; supports 8000–44100. Voice settings: `speed` (float), `vol` (float), `pitch` (integer), `language_boost` (string).

**REST** — same fields plus `output_type`.

### Inworld

Voice format: `inworld.<Model>.<VoiceId>`. Models: `inworld-tts-1.5-mini` (alias `Mini`, faster) and `inworld-tts-1.5-max` (alias `Max`, higher quality). Defaults to `mini`.

**WebSocket** — audio formats: `mp3`, `linear16`. Default sample rate 24000; supports 8000–48000. Voice settings: `encoding` (`MP3` or `LINEAR16`), `sample_rate`, `language_code`.

**REST** — same fields plus `output_type`.

### Resemble

Voice format: `resemble.Turbo.<VoiceId>`. Default model: `Turbo`. The `voice_id` references a voice from your own Resemble account.

**WebSocket** — audio formats: `mp3`, `wav`. Default sample rate 48000; supports 8000–48000. Voice settings: `format` (`mp3` or `wav`), `precision` (`PCM_16`, `PCM_24`, `PCM_32`, `MULAW`), `sample_rate` (default `48000` for mp3, `16000` for wav).

**REST** — same fields plus `output_type`.

## Common REST Response Behavior

All providers share the same `output_type` response pattern:

- **`binary_output`** (default): chunked audio bytes. Content-Type varies by provider and format (e.g., `audio/mpeg`, `audio/wav`, `audio/pcm`).
- **`base64_output`**: JSON response with base64-encoded audio.
- **`audio_id`**: JSON response with an `audio_url` for deferred retrieval.

## Quick Reference: Provider Capabilities

| Provider | WebSocket | REST | SSML Support | Custom Voice Source | Key Differentiator |
|---|---|---|---|---|---|
| Telnyx Natural | Yes | Yes | No | Pre-built | Low-latency English |
| Telnyx NaturalHD | Yes | Yes | No | Pre-built | 9 languages, Rime Arcana |
| Telnyx KokoroTTS | Yes | Yes | No | Pre-built | Lowest latency, 5 languages |
| Telnyx Qwen3TTS | Yes | Yes | No | Cloned (Voice Design Lab) | Voice cloning, 11 languages |
| Telnyx Ultra | No | Yes | Emotion tags + `[laughter]` | Pre-built | Sub-100ms, 36 languages |
| xAI Grok | AI Assistants only | Yes | Speech tags | Pre-built | Expressive Mode, 20+ languages |
| AWS Polly | Yes | Yes | Yes | Pre-built | Engine selection, lexicons |
| Azure | Yes | Yes | Yes | Pre-built | Audio effects, gender filter |
| ElevenLabs | Yes | Yes | No | Your account | Stability/style controls, cloning |
| Rime | Yes | Yes | No | Pre-built | Coda model, 184 voices |
| Minimax | Yes | Yes | No | Pre-built + cloned | Speed/vol/pitch controls |
| Inworld | Yes | Yes | No | Pre-built | Mini/Max model choice |
| Resemble | Yes | Yes | No | Your account | Precision/sample rate control |
