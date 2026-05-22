---
title: Third‑party TTS providers
summary: How to select and configure third‑party text‑to‑speech voices on Telnyx,
  including voice naming formats, WebSocket and REST options, audio formats, provider‑specific
  settings, and special capabilities for AWS Polly, Azure, ElevenLabs, Inworld, Minimax,
  Resemble, Rime, and xAI.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/providers/aws
- url: https://developers.telnyx.com/docs/voice/tts/providers/azure
- url: https://developers.telnyx.com/docs/voice/tts/providers/elevenlabs
- url: https://developers.telnyx.com/docs/voice/tts/providers/inworld
- url: https://developers.telnyx.com/docs/voice/tts/providers/minimax
- url: https://developers.telnyx.com/docs/voice/tts/providers/resemble
- url: https://developers.telnyx.com/docs/voice/tts/providers/rime
- url: https://developers.telnyx.com/docs/voice/tts/providers/xai
updated_at: 2026-05-20T10:15:20Z
---

# Third‑party TTS providers

How to select and configure third‑party text‑to‑speech voices on Telnyx, including voice naming formats, WebSocket and REST options, audio formats, provider‑specific settings, and special capabilities for AWS Polly, Azure, ElevenLabs, Inworld, Minimax, Resemble, Rime, and xAI.

## Voice naming and selection
- AWS Polly: `aws.Polly.<Engine>.<VoiceId>` (engines: `standard`, `neural`, `generative`, `long-form`). A hyphenated suffix on the voice ID can imply engine (e.g., `Lucia-longform` → `long-form`). Example: `aws.Polly.Generative.Lucia`.
- Azure: `azure.<VoiceId>` (flat identifiers). Default: `azure.en-US-AvaMultilingualNeural`. Example: `azure.en-US-AvaMultilingualNeural`.
- ElevenLabs: `elevenlabs.<Model>.<VoiceId>`; `voice_id` must be a voice from your ElevenLabs account (prebuilt, cloned, or designed). Example: `elevenlabs.v3.Adam`. Requires your own ElevenLabs API key configured in Telnyx.
- Inworld: `inworld.<Model>.<VoiceId>`; models: `inworld-tts-1.5-mini` (alias `Mini`, default) and `inworld-tts-1.5-max` (alias `Max`). Examples: `inworld.Mini.Loretta`, `inworld.Max.Hank`.
- Minimax: `minimax.<Model>.<VoiceId>`; `voice_id` may be a system voice or a cloned voice from the Telnyx Voice Design Lab (org‑scoped). Example: `minimax.speech-2.8-turbo.English_expressive_narrator`.
- Resemble: `resemble.Turbo.<VoiceId>` (default model `Turbo`); `voice_id` comes from your Resemble account. Example: `resemble.Turbo.Amelia_en-US`.
- Rime: `rime.ArcanaV3.<VoiceId>`. Example: `rime.ArcanaV3.albion`.
- xAI Grok voices: `xAI.<VoiceId>`; options include `xAI.ara`, `xAI.eve`, `xAI.leo`, `xAI.rex`, `xAI.sal`.

## WebSocket interoperability and query parameters
Use [TTS WebSocket Streaming](tts-websocket-streaming.md) for low‑latency synthesis where supported.
- AWS Polly
  - `audio_format`: `mp3`, `linear16`, `ogg_vorbis`
  - `sample_rate`: 8000, 16000, 22050, 24000
  - `language`: BCP‑47 (passed as `language_code` to Polly)
  - `text_type`: `text` (default) or `ssml`
- Azure
  - `audio_format`: `mp3`, `wav`, `linear16`, `mulaw`, `alaw`
  - `sample_rate`: 8000, 16000, 24000, 48000 (default 24000)
  - `language`: BCP‑47 (default `en-US`)
  - `text_type`: `text` or `ssml`
- ElevenLabs
  - `audio_format`: `mp3`, `linear16`, `mulaw`
  - `sample_rate`: 8000, 16000, 22050, 24000, 44100
  - `language`: BCP‑47
- Inworld
  - `audio_format`: `mp3`, `linear16`
  - `sample_rate`: 8000, 16000, 22050, 24000, 44100, 48000 (default 24000)
- Minimax
  - `audio_format`: `mp3`, `linear16`
  - `sample_rate`: 8000, 16000, 22050, 24000, 32000, 44100 (default 24000)
- Resemble
  - `audio_format`: `mp3`, `wav`
  - `sample_rate`: 8000, 16000, 22050, 32000, 44100, 48000 (default 48000)
- Rime
  - `audio_format`: `mp3`, `linear16`
  - `sample_rate`: 8000, 16000, 22050, 24000, 44100, 48000, 96000 (default 24000)
- xAI Grok voices
  - Not available on the public WebSocket API. Use [TTS REST API](tts-rest-api.md) or Telnyx AI Assistants.

## Provider voice settings reference
Settings can be supplied in `voice_settings` via WebSocket or REST (fields are equivalent unless noted).
- AWS Polly
  - `engine`: `standard`, `neural`, `generative`, `long-form` (default `standard`)
  - `output_format`: any AWS Polly output format (see https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-OutputFormat)
  - `sample_rate`: string Hz value (e.g., `"24000"`; valid combos depend on engine/format)
  - `lexicon_names`: array of pronunciation lexicons
  - `language_code`: BCP‑47 (overrides `language`)
  - `text_type`: `text` or `ssml` (overrides query param)
- Azure
  - `output_format`: Azure audio format string (default `audio-24khz-160kbitrate-mono-mp3`)
  - `language_code`: BCP‑47 (default `en-US`)
  - `text_type`: `text` or `ssml`
  - `effect`: `eq_car`, `eq_telecomhp8k`
  - `gender`: `Male`, `Female`
- ElevenLabs (pass‑through to ElevenLabs API)
  - Common fields: `model_id`, `language_code`, `stability`, `similarity_boost`, `style`, `use_speaker_boost`
- Inworld
  - `encoding`: `MP3` or `LINEAR16` (default `MP3`)
  - `sample_rate`: integer Hz (default 24000)
  - `language_code`: BCP‑47
- Minimax
  - `speed`: float (playback speed multiplier)
  - `vol`: float (volume)
  - `pitch`: integer (pitch adjustment)
  - `language_boost`: string (emphasize a language in multilingual synthesis)
- Resemble
  - `format`: `mp3` or `wav` (default `mp3`)
  - `precision`: `PCM_16`, `PCM_24`, `PCM_32`, `MULAW` (default `PCM_32`)
  - `sample_rate`: string Hz (mp3 default `48000`; wav default `16000`)
- Rime
  - `voice_speed`: float (default `1.0`)
- xAI Grok voices (REST only)
  - `language`: language code or `auto` (default `auto`)
  - `output_format`: `mp3`, `wav`, `pcm`, `mulaw`, `alaw` (default `mp3`)
  - `sample_rate`: 8000, 16000, 22050, 24000, 44100, 48000 (default 24000)

## REST outputs and retrieval
Across providers, `output_type` controls how audio is returned:
- `binary_output` (default): chunked audio bytes in the chosen output/format.
- `base64_output`: JSON payload with base64‑encoded audio.
- `audio_id`: JSON containing an `audio_url` you can fetch later.

## SSML, lexicons, and expressive control
- SSML
  - AWS Polly and Azure both accept SSML when `text_type` is `ssml` for fine‑grained prosody/pronunciation.
- Pronunciation resources
  - AWS Polly can apply `lexicon_names` for custom pronunciations. For cross‑provider options, see [Pronunciation Dictionaries](pronunciation-dictionaries.md).
- Expressive tags (xAI Grok voices)
  - Inline tags for natural delivery: `[pause]`, `[long-pause]`, `[laugh]`, `[chuckle]`, `[giggle]`, `[sigh]`, `[breath]`, `[inhale]`, `[exhale]`.
  - Style tags: `<whisper>`, `<soft>`, `<loud>`, `<emphasis>`, `<slow>`, `<fast>`, `<higher-pitch>`, `<lower-pitch>`.
  - Use tags sparingly for naturalness; see xAI fields above for format and rates.

## Account and voice ownership notes
- ElevenLabs: requires your own ElevenLabs API key in Telnyx; `voice_id` must exist in your ElevenLabs account.
- Resemble: `voice_id` must be a voice from your Resemble account.
- Minimax: `voice_id` can be a system voice or a cloned voice created in the Telnyx Voice Design Lab (org‑scoped).

## Availability and latency notes
- WebSocket availability: AWS, Azure, ElevenLabs, Inworld, Minimax, Resemble, and Rime support the public WebSocket API. xAI Grok voices do not — use [TTS REST API](tts-rest-api.md) or Telnyx AI Assistants.
- Latency: xAI Grok voices are higher‑latency than Telnyx Ultra; for sub‑100 ms TTFB, consider Telnyx Ultra voices.

## Quick voice string examples
- AWS Polly: `aws.Polly.Generative.Lucia`
- Azure: `azure.en-US-AvaMultilingualNeural`
- ElevenLabs: `elevenlabs.v3.Adam`
- Inworld: `inworld.Mini.Loretta`
- Minimax: `minimax.speech-2.8-turbo.English_expressive_narrator`
- Resemble: `resemble.Turbo.Amelia_en-US`
- Rime: `rime.ArcanaV3.albion`
- xAI: `xAI.eve`
