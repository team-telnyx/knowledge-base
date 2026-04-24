---
title: Ultra
summary: Telnyx Ultra — sub-100ms latency, 44 languages, REST only.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/ultra
    content_hash: c152325cc25a88506bfe13400c74a11b4e25c80193f58c79e36e5567f6566fc7
updated_at: 2026-04-10T00:00:00Z
---

# Ultra

Telnyx Ultra — sub-100ms latency, 44 languages, REST only.

**Voice format:** `Telnyx.Ultra.<voice>`

Sub-100ms latency. 36 languages.

> **Warning:** **REST only** — Ultra is not available over public WebSocket.

## Voice Samples

| Voice                 | Language | Gender | Sample    |
| --------------------- | -------- | ------ | --------- |
| `Telnyx.Ultra.Asher`  | en       | Male   | <audio /> |
| `Telnyx.Ultra.Callie` | en       | Female | <audio /> |
| `Telnyx.Ultra.Clara`  | en-US    | Female | <audio /> |

***

## SSML Emotions

Ultra supports inline SSML emotion tags. Place the tag before the text:

```
<emotion value="excited" />Great news — your order shipped early!
```

**Primary emotions:** `angry`, `excited`, `content`, `sad`, `scared`.

**Additional:** `happy`, `enthusiastic`, `curious`, `calm`, `grateful`, `affectionate`, `sarcastic`, `surprised`, `confident`, `hesitant`, `apologetic`, `determined`, `frustrated`, `disappointed`.

Omitting the tag = neutral delivery. Use sparingly — Ultra interprets emotional subtext from the text itself.

## Nonverbal Cues

Insert `[laughter]` inline for natural laughing:

```
That's hilarious! [laughter] Anyway, let me check your account.
```

***

## Language Support

Set `language_boost` to improve pronunciation for the target language:

Arabic, Bengali, Bulgarian, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Gujarati, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Marathi, Māori, Norwegian, Polish, Portuguese, Punjabi, Romanian, Russian, Slovak, Spanish, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, Vietnamese.

***

## REST API

### Fields

| Field            | Type    | Default         | Description                                                              |
| ---------------- | ------- | --------------- | ------------------------------------------------------------------------ |
| `voice_speed`    | float   | `1.0`           | Speech rate multiplier.                                                  |
| `language_boost` | string  | —               | Target language hint.                                                    |
| `volume`         | float   | —               | Output volume.                                                           |
| `emotion`        | string  | —               | `neutral`, `happy`, `sad`, `angry`, `fearful`, `disgusted`, `surprised`. |
| `sampling_rate`  | integer | —               | Output sample rate in Hz.                                                |
| `output_type`    | string  | `binary_output` | `binary_output`, `base64_output`, or `audio_id`.                         |

### Response

Default (`binary_output`): chunked audio bytes with `Content-Type: audio/mpeg`.

With `output_type: "base64_output"`: JSON with base64-encoded audio.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
