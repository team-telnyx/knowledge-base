---
title: Telnyx Text-to-Speech
summary: Telnyx Text-to-Speech (TTS) provides streaming speech synthesis over both
  REST and WebSocket transports, with multiple voice providers (Telnyx-branded models
  and xAI Grok), OpenAI SDK compatibility, and provider-specific tuning for speed,
  language, emotion, and voice cloning.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/kokoro
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/natural
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/naturalhd
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/qwen3
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/sukhan
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/ultra
- url: https://developers.telnyx.com/docs/voice/tts/providers/xai
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/api-reference
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/examples
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/index
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/pricing
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/request
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/response
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/configuration
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/errors
updated_at: 2026-08-05T14:06:54Z
---

# Telnyx Text-to-Speech

*Part 3 of 4 — see also: [Part 1](telnyx-text-to-speech--part-1.md), [Part 2](telnyx-text-to-speech--part-2.md), [Part 4](telnyx-text-to-speech--part-4.md)*

Telnyx Text-to-Speech (TTS) provides streaming speech synthesis over both REST and WebSocket transports, with multiple voice providers (Telnyx-branded models and xAI Grok), OpenAI SDK compatibility, and provider-specific tuning for speed, language, emotion, and voice cloning.

## Providers

### KokoroTTS

**Voice format:** `Telnyx.KokoroTTS.<voice>`

Lightweight, lowest-latency model. 5 languages: en, es, fr, it, pt.

| Voice | Language | Gender |
| --- | --- | --- |
| `Telnyx.KokoroTTS.af_heart` | en-US | Female |
| `Telnyx.KokoroTTS.am_adam` | en-US | Male |
| `Telnyx.KokoroTTS.bf_emma` | en-UK | Female |

**WebSocket**

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.KokoroTTS.af_heart
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`. |
| `sample_rate` | integer | `24000` | 24000. |

**Voice Settings** — None. All synthesis parameters are fixed. The init frame only needs `{"text": " "}`.

**REST API** — No model-specific fields. Audio format is always MP3.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default (`binary_output`): chunked audio bytes with `Content-Type: audio/mpeg`. With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

### Natural

**Voice format:** `Telnyx.Natural.<voice>`

Pre-built English voices backed by Rime Mist.

| Voice | Gender |
| --- | --- |
| `Telnyx.Natural.allison` | Female |
| `Telnyx.Natural.brook` | Female |

**WebSocket**

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.Natural.allison&audio_format=mp3
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`. |
| `sample_rate` | integer | `24000` | 8000, 16000, 22050, 24000, 44100, 48000, 96000. |

**Voice Settings** — Send in the init frame (`{"text": " "}`):

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | `1.0` | Speech rate multiplier. |

```
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 1.2
  }
}
```

**REST API**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | `1.0` | Speech rate multiplier. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default (`binary_output`): chunked audio bytes with `Content-Type: audio/mpeg` (or `audio/wav`, `audio/pcm`). With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

### NaturalHD

**Voice format:** `Telnyx.NaturalHD.<voice>`

Pre-built voices backed by Rime Arcana. 9 languages: en, fr, de, es, ar, hi, ja, he, pt.

| Voice | Language | Gender |
| --- | --- | --- |
| `Telnyx.NaturalHD.astra` | en-US | Female |
| `Telnyx.NaturalHD.albion` | en-US | Male |
| `Telnyx.NaturalHD.amarante` | fr-FR | Female |
| `Telnyx.NaturalHD.luna` | en-US | Female |

**WebSocket**

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra&audio_format=mp3
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`. |
| `sample_rate` | integer | `24000` | 8000, 16000, 22050, 24000, 44100, 48000, 96000. |

**Voice Settings** — Send in the init frame (`{"text": " "}`):

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | `1.0` | Speech rate multiplier. |

```
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 0.9
  }
}
```

**REST API**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | `1.0` | Speech rate multiplier. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default (`binary_output`): chunked audio bytes with `Content-Type: audio/mpeg` (or `audio/wav`, `audio/pcm`). With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

### Qwen3TTS

**Voice format:** `Telnyx.Qwen3TTS.<clone_name>`

Voice cloning model. 11 languages: en, zh, fr, de, it, ja, ko, pt, ru, es, ar. The `voice_id` is the name of a clone you created in the [Voice Design](https://portal.telnyx.com/#/app/ai/voice-design-lab). Clones are scoped to your organization.

| Voice | Gender |
| --- | --- |
| `Telnyx.Qwen3TTS.Delta` | Female |
| `Telnyx.Qwen3TTS.Whiskey` | Male |

**WebSocket**

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.Qwen3TTS.Delta
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`. |
| `sample_rate` | integer | `24000` | 24000. |

**Voice Settings** — Send in the init frame (`{"text": " "}`):

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `language_boost` | string | — | Target language hint: `Auto`, `English`, `Chinese`, `French`, `German`, `Italian`, `Japanese`, `Korean`, `Portuguese`, `Russian`, `Spanish`, or ISO codes. |
| `force_xvector` | boolean | `false` | Force x-vector voice embedding. |

```
{
  "text": " ",
  "voice_settings": {
    "language_boost": "English"
  }
}
```

**REST API**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `language_boost` | string | — | Target language hint. |
| `force_xvector` | boolean | `false` | Force x-vector voice embedding. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default (`binary_output`): chunked PCM audio bytes. Always 24kHz signed 16-bit LE mono. With `output_type: "base64_output"`: JSON with base64-encoded PCM. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

### Sukhan

**Voice format:** `Telnyx.Sukhan.<voice_id>`

Urdu-only voice model, 14 curated voices. No prosody controls (speed/pitch) or language selection — each voice speaks Urdu only. Native audio is 22050Hz.

| Voice | Gender | Accent |
| --- | --- | --- |
| `Telnyx.Sukhan.urdu-professor` | Male | Standard |
| `Telnyx.Sukhan.news-reader` | Female | Standard |
| `Telnyx.Sukhan.sindhi-networker` | Male | Sindhi |
| `Telnyx.Sukhan.podcast-host` | Male | Standard |

Browse the full 14-voice catalogue via the [Voices API](https://developers.telnyx.com/api-reference/text-to-speech-commands/list-available-voices).

**WebSocket**

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.Sukhan.urdu-professor
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`. `wav` is **not** supported. |
| `sample_rate` | integer | `22050` | Only `22050` (native) is supported. |

**Voice Settings** — None. No prosody controls are exposed — `voice_speed` and other settings have no effect if sent. The init frame only needs `{"text": " "}`.

**REST API**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `response_format` | string | native | `pcm`, `mp3`. `wav` is **not** supported. |
| `sampling_rate` | integer | `22050` | Only `22050` (native) is supported. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default (`binary_output`): chunked audio bytes, 22050Hz signed 16-bit LE mono (native PCM, transcoded to MP3 on request). With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

`sampling_rate`/`sample_rate` values other than `22050` are rejected with a `400` error. Unsupported format values are also rejected — REST `response_format` accepts only `pcm`/`mp3`; WebSocket `audio_format` accepts only `mp3`/`linear16` (its PCM equivalent). Neither accepts `wav`.

### Ultra

**Voice format:** `Telnyx.Ultra.<voice>`

Sub-100ms latency. 36 languages. **REST only** — Ultra is not available over public WebSocket.

| Voice | Language | Gender |
| --- | --- | --- |
| `Telnyx.Ultra.Asher` | en | Male |
| `Telnyx.Ultra.Callie` | en | Female |
| `Telnyx.Ultra.Clara` | en-US | Female |

**SSML Emotions** — Ultra supports inline SSML emotion tags. Place the tag before the text:

```
<emotion value="excited" />Great news — your order shipped early!
```

**Primary emotions:** `angry`, `excited`, `content`, `sad`, `scared`. **Additional:** `happy`, `enthusiastic`, `curious`, `calm`, `grateful`, `affectionate`, `sarcastic`, `surprised`, `confident`, `hesitant`, `apologetic`, `determined`, `frustrated`, `disappointed`. Omitting the tag = neutral delivery. Use sparingly — Ultra interprets emotional subtext from the text itself.

**Nonverbal Cues** — Insert `[laughter]` inline for natural laughing:

```
That's hilarious! [laughter] Anyway, let me check your account.
```

**Language Support** — Set `language_boost` to improve pronunciation for the target language: Arabic, Bengali, Bulgarian, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Gujarati, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Marathi, Māori, Norwegian, Polish, Portuguese, Punjabi, Romanian, Russian, Slovak, Spanish, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, Vietnamese.

**REST API**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | `1.0` | Speech rate multiplier. |
| `language_boost` | string | — | Target language hint. |
| `volume` | float | — | Output volume. |
| `emotion` | string | — | `neutral`, `happy`, `sad`, `angry`, `fearful`, `disgusted`, `surprised`. |
| `sampling_rate` | integer | — | Output sample rate in Hz. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

Default (`binary_output`): chunked audio bytes with `Content-Type: audio/mpeg`. With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

xAI Grok is the second TTS provider supporting Expressive Mode. For Grok voice options, see [Grok Voices](grok-voices.md). Note: Grok voices have higher latency than Ultra.

### xAI Grok

**Voice format:** `xAI.<VoiceId>`

xAI Grok voices are expressive, multilingual text-to-speech voices. They support inline speech tags for pauses, vocal sounds, emphasis, pitch, pace, and intensity. xAI Grok voices are higher-latency than [Ultra](ultra.md). For latency-sensitive applications that need sub-100ms time to first byte, use Ultra.

| Voice | Voice ID | Use for |
| --- | --- | --- |
| Ara | `xAI.ara` | Warm, conversational assistant experiences |
| Eve | `xAI.eve` | General-purpose voice assistant experiences |
| Leo | `xAI.leo` | Confident, direct interactions |
| Rex | `xAI.rex` | Characterful or energetic interactions |
| Sal | `xAI.sal` | Distinctive conversational tone |

**WebSocket** — xAI Grok voices are not available on the public TTS WebSocket API. Use the [REST API](rest-api.md) for direct text-to-speech generation, or use xAI Grok voices with [AI Assistants](/docs/inference/ai-assistants/no-code-voice-assistant).

**REST API**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `language` | string | `auto` | Language code, or `auto` to detect automatically. |
| `output_format` | string | `mp3` | `mp3`, `wav`, `pcm`, `mulaw`, or `alaw`. |
| `sample_rate` | integer | `24000` | 8000, 16000, 22050, 24000, 44100, or 48000. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

```
{
  "text": "Let me check that for you. [pause] I found your appointment.",
  "voice": "xAI.eve",
  "voice_settings": {
    "language": "auto",
    "output_format": "mp3",
    "sample_rate": 24000
  }
}
```

Default (`binary_output`): chunked audio bytes. With `output_type: "base64_output"`: JSON with base64-encoded audio. With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.

**Expressive Speech Tags** — Use speech tags inline in `text` when you want more expressive delivery.

| Tag | Use for |
| --- | --- |
| `[pause]` | A short natural pause |
| `[long-pause]` | A longer pause for topic transitions or important moments |
| `[laugh]`, `[chuckle]`, `[giggle]` | Natural laughter or amused reactions |
| `[sigh]`, `[breath]`, `[inhale]`, `[exhale]` | Breath and sigh sounds |
| `<whisper>` | Whispered delivery |
| `<soft>` | Softer delivery |
| `<loud>` | Louder delivery |
| `<emphasis>` | Emphasized delivery |
| `<slow>`, `<fast>` | Slower or faster pace |
| `<higher-pitch>`, `<lower-pitch>` | Higher or lower pitch |

```
So I walked in and [pause] there it was. [laugh] I honestly could not believe it!
```

```
<emphasis>Your appointment is confirmed for tomorrow at 3 PM.</emphasis>
```

Use expressive tags sparingly. The goal is natural delivery, not tagging every sentence.

**AI Assistants** — For AI Assistants, choose an xAI Grok voice such as `xAI.eve` and enable **Expressive Mode** to let the assistant decide when speech tags improve the caller experience.
