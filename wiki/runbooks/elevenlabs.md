---
title: ElevenLabs
summary: ElevenLabs TTS provider — bring your own ElevenLabs API key.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/elevenlabs
    content_hash: c20686fc28823838284a44a0fc448b6eb8791bbea7da233e384c2e4d2ac3e7fc
updated_at: 2026-04-10T00:00:00Z
---

# ElevenLabs

ElevenLabs TTS provider — bring your own ElevenLabs API key.

> **Warning:** ElevenLabs requires your own API key configured in your Telnyx account. Telnyx relays requests to the ElevenLabs API — voice settings are passed through directly.

**Voice format:** `elevenlabs..`

Example: `elevenlabs.v3.Adam`

`voice_id` is a voice from **your own ElevenLabs account** — pre-built, cloned, or designed. Preview voices at [elevenlabs.io/voice-library](https://elevenlabs.io/voice-library).

***

## WebSocket

### Query Parameters

| Parameter      | Type    | Default | Description                       |
| -------------- | ------- | ------- | --------------------------------- |
| `audio_format` | string  | `mp3`   | `mp3`, `linear16`, `mulaw`.       |
| `sample_rate`  | integer | —       | 8000, 16000, 22050, 24000, 44100. |
| `language`     | string  | —       | BCP-47 language code.             |

### Voice Settings

Relayed directly to the [ElevenLabs API](https://elevenlabs.io/docs/api-reference/text-to-speech). Any field ElevenLabs accepts can be passed here.

| Field               | Type    | Default | Description                                                |
| ------------------- | ------- | ------- | ---------------------------------------------------------- |
| `model_id`          | string  | —       | ElevenLabs model override (e.g. `eleven_multilingual_v2`). |
| `language_code`     | string  | —       | BCP-47. Overrides `language` query param.                  |
| `stability`         | float   | —       | 0.0–1.0. Voice consistency.                                |
| `similarity_boost`  | float   | —       | 0.0–1.0. Clarity and similarity to original voice.         |
| `style`             | float   | —       | 0.0–1.0. Style exaggeration.                               |
| `use_speaker_boost` | boolean | —       | Speaker boost toggle for clarity.                          |

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.75,
    "style": 0.3
  }
}
```

## REST API

### Fields

| Field               | Type    | Default         | Description                                      |
| ------------------- | ------- | --------------- | ------------------------------------------------ |
| `model_id`          | string  | —               | ElevenLabs model override.                       |
| `stability`         | float   | —               | 0.0–1.0. Voice consistency.                      |
| `similarity_boost`  | float   | —               | 0.0–1.0. Clarity and similarity.                 |
| `style`             | float   | —               | 0.0–1.0. Style exaggeration.                     |
| `use_speaker_boost` | boolean | —               | Speaker boost toggle.                            |
| `output_type`       | string  | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

### Response

Default (`binary_output`): chunked audio bytes. Format determined by ElevenLabs.

With `output_type: "base64_output"`: JSON with base64-encoded audio.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
