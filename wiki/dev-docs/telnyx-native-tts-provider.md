---
title: Telnyx native TTS provider
summary: Telnyx is the default Text-to-Speech provider on the Telnyx platform, offering
  multiple voice models with different latency, quality, and language tradeoffs. Use
  WebSocket streaming or REST (Ultra is REST-only). Browse available voices via the
  Voices API or design and manage clones in the Voice Design Lab.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/index
  content_hash: 5dab36f4ce7f968e4769de9cf2f1ae65a5331f1ed5ed94ecc86c2e1f68fda130
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/ultra
  content_hash: 3957e72a9b195d184eef5c84223341906e4357ce022f545f3db60593656d8ea0
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/natural
  content_hash: ace36d725bf272ee4199bb982f58c27761db48d253388549567f258927fe04d9
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/naturalhd
  content_hash: cfbfa5e4cd6e003cddfdfc73200d98e2536cba54ba64a288e72a8ba41aa8b7cf
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/kokoro
  content_hash: ebd593ffb6015c6c229c5a9f9a893f842707ab4358419ffffde415135bea1425
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/qwen3
  content_hash: e8cb9655a34b19268facb3a09bb58301da8c477b57a4cd5a1e654ab202d58b97
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/grok
  content_hash: 4a1886651879403619493fa50f5d33667aa8a9d904cb752ce851db0071003632
updated_at: 2026-05-20T10:11:43Z
---

# Telnyx native TTS provider

Telnyx is the default Text-to-Speech provider on the Telnyx platform, offering multiple voice models with different latency, quality, and language tradeoffs. Use WebSocket streaming or REST (Ultra is REST-only). Browse available voices via the Voices API or design and manage clones in the Voice Design Lab.

## Selecting Telnyx
- Default provider: if you don’t specify a provider, Telnyx TTS is used.
- WebSocket endpoint example: wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra
- REST endpoint: POST https://api.telnyx.com/v2/text-to-speech (Authorization: Bearer <token>; JSON body includes at least text and voice)
- Browse voices: Voices API (https://developers.telnyx.com/api-reference/text-to-speech-commands/list-available-voices) and Voice Design Lab (https://portal.telnyx.com/#/app/ai/voice-design-lab)

## Models at a glance
- Natural — Low latency, good quality, English only. Pre-built voices (Rime Mist). WebSocket + REST.
- NaturalHD — Low latency, better quality, 9 languages (en, fr, de, es, ar, hi, ja, he, pt). Pre-built (Rime Arcana). WebSocket + REST.
- KokoroTTS — Lowest latency lightweight model, 5 languages (en, es, fr, it, pt). WebSocket + REST.
- Qwen3TTS — Medium latency, high quality, 11 languages (en, zh, fr, de, it, ja, ko, pt, ru, es, ar). Voice cloning; clones are created in your organization’s Voice Design Lab. WebSocket + REST.
- Ultra — Sub-100ms time-to-first-byte, highest quality, broad language coverage. REST only (not available over public WebSocket). Expressive SSML support.
- xAI Grok — Expressive voices for Voice AI Assistants and direct REST TTS. Higher latency than Ultra; supports rich speech tags in assistants.

See model details: [Natural](natural.md), [NaturalHD](naturalhd.md), [KokoroTTS](kokorotts.md), [Qwen3TTS](qwen3tts.md), [Ultra](ultra.md), [xAI Grok Voices](xai-grok-voices.md).

## Voice formats by model
- Natural: Telnyx.Natural.<voice>
- NaturalHD: Telnyx.NaturalHD.<voice>
- KokoroTTS: Telnyx.KokoroTTS.<voice>
- Qwen3TTS (clones): Telnyx.Qwen3TTS.<clone_name> (clone names come from the Voice Design Lab)
- Ultra: Telnyx.Ultra.<voice>
- xAI Grok (Assistants): xAI.<voice_id> (e.g., xAI.eve); direct REST uses provider "xai" with xAI-specific parameters

## WebSocket streaming options
- Availability: Natural, NaturalHD, KokoroTTS, Qwen3TTS support WebSocket. Ultra is REST-only.
- Common query parameters:
  - audio_format: mp3 (default) or linear16
  - sample_rate: default 24000. Natural/NaturalHD allow 8000, 16000, 22050, 24000, 44100, 48000, 96000. KokoroTTS and Qwen3TTS use 24000.
- Voice settings (send in the init frame along with a minimal text payload):
  - Natural, NaturalHD: voice_speed (float, default 1.0)
  - Qwen3TTS: language_boost (language hint; accepts names like English/Chinese/etc. or ISO codes), force_xvector (boolean, default false)
  - KokoroTTS: no tunable synthesis parameters (init frame needs only a placeholder text field)

For full streaming lifecycle, configuration, and message schema, see [WebSocket Streaming](websocket-streaming.md).

## REST API options and responses
- Output control (all models): output_type can be binary_output (default), base64_output, or audio_id (deferred retrieval via audio_url).
- Natural, NaturalHD:
  - Fields: voice_speed (default 1.0), output_type.
  - Default response uses audio/mpeg (MP3). WAV or PCM when requested by format.
- KokoroTTS:
  - No model-specific fields (audio is always MP3). Uses output_type for transport choice.
  - Default response Content-Type: audio/mpeg.
- Qwen3TTS:
  - Fields: language_boost, force_xvector, output_type.
  - Default response is raw PCM: 24 kHz, signed 16-bit, little-endian, mono (base64_output encodes this PCM).
- Ultra (REST only):
  - Fields: voice_speed, language_boost, volume, emotion (neutral, happy, sad, angry, fearful, disgusted, surprised), sampling_rate, output_type.
  - Default response: streamed audio bytes (audio/mpeg). Base64 or audio_id also supported.

See [REST API](rest-api.md) for request/response structure and examples.

## Ultra expressive controls
- SSML emotions: insert <emotion value="..." /> immediately before text. Primary: angry, excited, content, sad, scared. Additional: happy, enthusiastic, curious, calm, grateful, affectionate, sarcastic, surprised, confident, hesitant, apologetic, determined, frustrated, disappointed. Omitting the tag yields neutral delivery.
- Nonverbal cues: include [laughter] inline for natural laughing.
- Language hinting: set language_boost to improve target-language pronunciation (supports a wide set of languages including Arabic, Bengali, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Gujarati, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Marathi, Māori, Norwegian, Polish, Portuguese, Punjabi, Romanian, Russian, Slovak, Spanish, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, Vietnamese).

## xAI Grok voices and Expressive Mode
- What’s different from Ultra:
  - Expressiveness: Ultra uses SSML emotion tags plus simple cues like [laughter]; Grok supports rich xAI speech tags (pauses, breaths, laughs, whispering, emphasis, pitch, pace, intensity) during live Voice AI sessions.
  - Streaming: Ultra is REST-only; Grok streams with Voice AI Assistants (and supports direct REST TTS when using provider "xai").
  - Latency: Grok has higher latency; choose Ultra for sub-100ms needs.
- Voice format (Assistants): xAI.<voice_id> with available voices ara, eve, leo, rex, sal.
- Enable Expressive Mode for assistants: in the Portal under Voice Settings choose an xAI Grok voice and toggle Expressive Mode on, or set voice to xAI.<voice_id> and expressive_mode: true via the Assistants API.
- Tag examples the assistant can use when Expressive Mode is on (you can also include them in prompts):
  - Inline: [pause], [long-pause], [laugh], [chuckle], [breath]
  - Wrapping: <whisper>…</whisper>, <soft>…</soft>, <emphasis>…</emphasis>, <slow>…</slow>, <higher-pitch>…</higher-pitch>
- Direct REST TTS with xAI provider: set provider to xai and pass xAI params (voice_id one of ara/eve/leo/rex/sal; language code or auto; output_format mp3/wav/pcm/mulaw/alaw; sample_rate 8000–48000).

For details and full tag reference, see [xAI Grok Voices](xai-grok-voices.md).

## Language support summary
- Natural: English.
- NaturalHD: en, fr, de, es, ar, hi, ja, he, pt.
- KokoroTTS: en, es, fr, it, pt.
- Qwen3TTS: en, zh, fr, de, it, ja, ko, pt, ru, es, ar (use language_boost to hint).
- Ultra: broad coverage; use language_boost with supported languages (see list under Ultra expressive controls above).
- xAI Grok: auto language detection or explicit language code (for REST xAI requests).

## Choosing a model
- Need the fastest responses and REST-only integration: choose Ultra.
- Need low-latency WebSocket streaming with pre-built voices: choose Natural or NaturalHD (NaturalHD for multilingual, higher fidelity).
- Need the very lowest footprint/latency with fixed settings: choose KokoroTTS.
- Need cloned voices and multilingual synthesis: choose Qwen3TTS.
- Building Voice AI Assistants that benefit from richer paralinguistics: choose xAI Grok (accept higher latency).

## Tools and next steps
- Explore voices: Voices API (https://developers.telnyx.com/api-reference/text-to-speech-commands/list-available-voices) and Voice Design Lab (https://portal.telnyx.com/#/app/ai/voice-design-lab)
- Learn streaming details: [WebSocket Streaming](websocket-streaming.md)
- Build with REST: [REST API](rest-api.md)
- Improve pronunciations: [Pronunciation Dictionaries](pronunciation-dictionaries.md)
- Play audio into calls: [In-Call Playback](in-call-playback.md)
- Estimate costs: [Pricing](pricing.md)
