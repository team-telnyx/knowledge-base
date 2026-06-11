---
title: Telnyx Text-to-Speech API
summary: Telnyx Text-to-Speech provides REST and WebSocket interfaces for synthesizing
  audio from text, supporting real-time streaming playback, multiple TTS providers,
  OpenAI SDK compatibility, and conversational barge-in patterns.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/api-reference
  content_hash: ea02fe06331e52e5066dff833c0598afde79b7bebeb61c1e3191cdc75f53b7e9
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/examples
  content_hash: 16ef22cb54e6ed6b1ae5c1fdb59b5b4bd5ea07be53581286541f1ced958f35b6
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/index
  content_hash: b6ca6f23cce45ad8ec4201e7fe0c703195a7e1f39626b10555d8fc30e0d53e73
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/pricing
  content_hash: d7275459734a88ed4e899a6ee9439929757b64aca9a7baf7ed22effb4953e6ba
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/request
  content_hash: 35370ca7212ed1f9de549b11f021a3387c2c8bec90e8f7ca815d2d8681de73d7
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/response
  content_hash: e8acfc6badb9c6f87283a243075f9300887d69b7673a625efae904345e9c6cca
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/configuration
  content_hash: 6b5a3bafecd321fcebf90e7e4ef069b88fb7a861a3562a4b1a651e72eff46d88
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/errors
  content_hash: ce2d0a0292324cec09128617bf277fcea51dc75bdc197b360a1a78af647bd877
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/examples
  content_hash: 926d8e69d30c20170b72e51895b5b8367f76cc845c132482dbf757c3540adf64
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/index
  content_hash: b4419a32235d92f689dd7f467814a442fe82985e7d406bfa5efd8e8d3c99d00f
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/messages
  content_hash: 87cdb6015b8d1abc8eebf5e73335cc22e6d5a756d03954e09aeef86c3b1bc52f
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/parameters/voice-settings
  content_hash: 804699ea5b600de602be28e823e2c21a2b0561ace23918e170f806af340b39a6
- url: https://developers.telnyx.com/docs/voice/uac-connections/index
  content_hash: fb4414be84cc9e9646e863d99b8f58a7a8ca9b2d4959833f3510ade01629b2d9
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
