---
title: TTS Providers
summary: Telnyx supports multiple text-to-speech providers — both native models and
  third-party services — accessible via WebSocket and REST APIs. Each provider has
  a unique voice format, set of models, audio formats, and voice settings.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/providers/aws
- url: https://developers.telnyx.com/docs/voice/tts/providers/azure
- url: https://developers.telnyx.com/docs/voice/tts/providers/elevenlabs
- url: https://developers.telnyx.com/docs/voice/tts/providers/inworld
- url: https://developers.telnyx.com/docs/voice/tts/providers/minimax
- url: https://developers.telnyx.com/docs/voice/tts/providers/resemble
- url: https://developers.telnyx.com/docs/voice/tts/providers/rime
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/grok
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/index
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/kokoro
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/natural
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/naturalhd
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/qwen3
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/ultra
- url: https://developers.telnyx.com/docs/voice/tts/providers/xai
updated_at: 2026-06-11T10:46:51Z
---

# TTS Providers

*Part 1 of 2 — see also: [Part 2](tts-providers--part-2.md)*

Telnyx supports multiple text-to-speech providers — both native models and third-party services — accessible via WebSocket and REST APIs. Each provider has a unique voice format, set of models, audio formats, and voice settings.

## Voice Format Convention

Every TTS voice is identified by a dot-delimited string: `<provider>.<Model>.<VoiceId>`. Some providers omit the model segment (e.g., Azure uses `azure.<VoiceId>`, xAI uses `xAI.<VoiceId>`). The voice string is passed as the `voice` query parameter on WebSocket connections or the `voice` field in REST requests.

## Telnyx Native Models

Telnyx is the default provider — if no provider is specified, you get Telnyx. Browse all available voices via the [Voices API](https://developers.telnyx.com/api-reference/text-to-speech-commands/list-available-voices) or the [Voice Design Lab](https://portal.telnyx.com/#/app/ai/voice-design-lab).

| Model | Voice Format | Latency | Quality | Languages | Voice Source | WebSocket | REST |
|---|---|---|---|---|---|---|---|
| Natural | `Telnyx.Natural.<voice>` | Low | Good | English | Pre-built (Rime Mist) | Yes | Yes |
| NaturalHD | `Telnyx.NaturalHD.<voice>` | Low | Better | 9 (en, fr, de, es, ar, hi, ja, he, pt) | Pre-built (Rime Arcana) | Yes | Yes |
| KokoroTTS | `Telnyx.KokoroTTS.<voice>` | Lowest | Good | 5 (en, es, fr, it, pt) | Pre-built | Yes | Yes |
| Qwen3TTS | `Telnyx.Qwen3TTS.<clone_name>` | Medium | High | 11 (en, zh, fr, de, it, ja, ko, pt, ru, es, ar) | Cloned (Voice Design Lab) | Yes | Yes |
| Ultra | `Telnyx.Ultra.<voice>` | Lowest | Highest | 36 | Pre-built | **No** | Yes |
| Grok | `xAI.<voice_id>` | Higher | High | 20+ | Pre-built | Voice AI only | Yes |

### Natural

Pre-built English voices backed by Rime Mist. Supports `mp3` and `linear16` audio formats. Sample rates: 8000, 16000, 22050, 24000, 44100, 48000, 96000 (default 24000). Voice settings: `voice_speed` (float, default `1.0`).

### NaturalHD

Pre-built voices backed by Rime Arcana across 9 languages. Supports `mp3` and `linear16` audio formats. Same sample rate range and `voice_speed` setting as Natural.

### KokoroTTS

Lightweight, lowest-latency model across 5 languages. Supports `mp3` and `linear16` at 24000 Hz only. No configurable voice settings — the init frame only needs `{"text": " "}`. REST audio format is always MP3.

### Qwen3TTS

Voice cloning model. The `voice_id` is the name of a clone created in the Voice Design Lab, scoped to your organization. Supports `mp3` and `linear16` at 24000 Hz. Voice settings include `language_boost` (target language hint such as `Auto`, `English`, `Chinese`, etc.) and `force_xvector` (boolean, default `false`). REST output is always 24kHz signed 16-bit LE mono PCM when using `binary_output`.

### Ultra

Sub-100ms latency, 36 languages, REST-only (not available over public WebSocket). Supports SSML emotion tags and nonverbal cues.

**SSML Emotions** — place before the text: `<emotion value="excited" />Great news!`. Primary emotions: `angry`, `excited`, `content`, `sad`, `scared`. Additional: `happy`, `enthusiastic`, `curious`, `calm`, `grateful`, `affectionate`, `sarcastic`, `surprised`, `confident`, `hesitant`, `apologetic`, `determined`, `frustrated`, `disappointed`. Omitting the tag yields neutral delivery.

**Nonverbal Cues** — insert `[laughter]` inline for natural laughing.

REST fields: `voice_speed` (float), `language_boost` (string), `volume` (float), `emotion` (string — `neutral`, `happy`, `sad`, `angry`, `fearful`, `disgusted`, `surprised`), `sampling_rate` (integer), `output_type`.

### xAI Grok Voices

Expressive, multilingual voices with higher latency than Ultra. Five voices: `ara` (warm/conversational), `eve` (general-purpose), `leo` (confident/direct), `rex` (characterful/energetic), `sal` (distinctive tone). Not available on the public TTS WebSocket — use REST or [AI Assistants](ai-assistants--part-1.md).

**Expressive Mode** — when enabled on an AI Assistant, the system prompt is augmented so the model decides when speech tags improve the experience. Enable via the Portal (toggle under Voice Settings) or via API with `expressive_mode: true` in `voice_settings`.

**Inline speech tags:** `[pause]`, `[long-pause]`, `[laugh]`, `[chuckle]`, `[giggle]`, `[cry]`, `[tsk]`, `[tongue-click]`, `[lip-smack]`, `[breath]`, `[inhale]`, `[exhale]`, `[sigh]`, `[hum-tune]`.

**Wrapping tags:** `<soft>`, `<whisper>`, `<loud>`, `<build-intensity>`, `<decrease-intensity>`, `<higher-pitch>`, `<lower-pitch>`, `<slow>`, `<fast>`, `<sing-song>`, `<singing>`, `<laugh-speak>`, `<emphasis>`.

Use tags sparingly for natural delivery. For sensitive contexts, prefer subtle tags like `<soft>` or `<whisper>`.

REST fields: `language` (default `auto` for detection), `output_format` (`mp3`, `wav`, `pcm`, `mulaw`, `alaw`), `sample_rate` (8000–48000), `output_type`.
