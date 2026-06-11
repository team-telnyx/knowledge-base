---
title: Telnyx Text-to-Speech API
summary: Telnyx Text-to-Speech provides REST and WebSocket interfaces for synthesizing
  audio from text, supporting real-time streaming playback, multiple TTS providers,
  OpenAI SDK compatibility, and conversational barge-in patterns.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/api-reference
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/examples
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/index
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/pricing
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/request
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/response
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/configuration
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/index
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/messages
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/parameters/voice-settings
- url: https://developers.telnyx.com/docs/voice/uac-connections/index
updated_at: 2026-06-11T10:48:38Z
---

# Telnyx Text-to-Speech API

*Part 3 of 3 — see also: [Part 1](telnyx-text-to-speech-api--part-1.md), [Part 2](telnyx-text-to-speech-api--part-2.md)*

Telnyx Text-to-Speech provides REST and WebSocket interfaces for synthesizing audio from text, supporting real-time streaming playback, multiple TTS providers, OpenAI SDK compatibility, and conversational barge-in patterns.

## Voice Selection

The `voice` parameter uses the format `Provider.Model.VoiceId`. The `VoiceId` segment refers to different things depending on the provider and model:

| Type | Example | How to get it |
|---|---|---|
| **Pre-built voice** | `Telnyx.NaturalHD.astra` | Browse via the Voices API (`GET /v2/ai/tts/voices`) or Voice Design Lab |
| **Your cloned voice** | `Telnyx.Qwen3TTS.my-ceo-clone` | Create in the Voice Design Lab. Scoped to your organization. Available for Qwen3TTS and Minimax. |
| **BYOK provider voice** | `elevenlabs.v3.Adam` | A voice ID from your own ElevenLabs or Resemble account. You bring your own API key. |

The Voices API returns all voices available to your account — pre-built and cloned — with each voice's compound `id` ready to use as the `voice` parameter.

---

## Voice Settings by Provider

Voice settings are provider-specific. There are no common fields. Unrecognized fields are silently ignored.

### Telnyx Natural / NaturalHD

| Parameter | Type | Default | Description |
|---|---|---|---|
| `voice_speed` | float | 1.0 | Speech rate. Values > 1 are faster. |

### Telnyx Ultra (REST only)

| Parameter | Type | Default | Description |
|---|---|---|---|
| `voice_speed` | float | 1.0 | Speech rate. Values > 1 are faster. |
| `language_boost` | string | — | Target language |
| `volume` | float | — | Volume level |
| `emotion` | string | — | `neutral`, `happy`, `sad`, `angry`, `fearful`, `disgusted`, `surprised` |

### Telnyx Qwen3TTS

| Parameter | Type | Default | Description |
|---|---|---|---|
| `language_boost` | string | `"Auto"` | Target language: `Auto`, `English`, `Chinese`, `French`, `German`, `Italian`, `Japanese`, `Korean`, `Portuguese`, `Russian`, `Spanish`, or ISO codes (`en`, `zh`, etc.) |

### Azure Speech

| Parameter | Type | Default | Description |
|---|---|---|---|
| `language_code` | string | `"en-US"` | Language code |
| `text_type` | string | `"text"` | `text` or `ssml` |
| `effect` | string | — | `eq_car` or `eq_telecomhp8k` |
| `gender` | string | — | `Male` or `Female` |

### AWS Polly

| Parameter | Type | Default | Description |
|---|---|---|---|
| `language_code` | string | — | BCP-47 language code |
| `output_format` | string | — | Audio format override |
| `engine` | string | `"standard"` | `standard`, `neural`, `generative`, or `long-form` |
| `text_type` | string | `"text"` | `text` or `ssml` |
| `lexicon_names` | array | — | Pronunciation lexicon names |

### Minimax

| Parameter | Type | Default | Description |
|---|---|---|---|
| `speed` | float | — | Speech rate |
| `vol` | float | — | Volume |
| `pitch` | integer | — | Pitch adjustment |
| `language_boost` | string | — | Language emphasis |

### Rime

| Parameter | Type | Default | Description |
|---|---|---|---|
| `voice_speed` | float | 1.0 | Speech rate. Above 1.0 = faster, below 1.0 = slower. |
| `sampling_rate` | integer | 24000 | Output sample rate in Hz. |
| `response_format` | string | `"mp3"` | `mp3`, `pcm`, or `wav`. |

### Inworld

| Parameter | Type | Default | Description |
|---|---|---|---|
| `language_code` | string | — | Language code |

---

## Text Preprocessing

Before synthesis, text passes through two stages in both REST and WebSocket:

1. **Markdown stripping** — Headers, bold, italics, code blocks, links, lists, and emoji are converted to plain text. This is useful when synthesizing LLM output.
2. **Pronunciation dictionary** — If `pronunciation_dict_id` is set, custom word replacements are applied.

---

## Pricing

Pricing varies by engine and model. Contact [sales](https://telnyx.com/contact-us) or check the [pricing page](https://telnyx.com/pricing/text-to-speech) for current rates.
