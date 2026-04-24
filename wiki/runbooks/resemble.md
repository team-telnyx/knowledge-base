---
title: Resemble
summary: Resemble TTS provider — bring your own Resemble API key.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/resemble
    content_hash: d512d23a6fb4cd8e826381d5b9691800f7831d33e28b4c2dd8e4f0c8085bb9f2
updated_at: 2026-04-10T00:00:00Z
---

# Resemble

Resemble TTS provider — bring your own Resemble API key.

**Voice format:** `resemble.Turbo.`

Default model: `Turbo`. `voice_id` is a voice from **your own Resemble account**.

## Voice Samples

| Voice                         | Language | Gender | Sample    |
| ----------------------------- | -------- | ------ | --------- |
| `Resemble.Turbo.Aaron_en-US`  | en-US    | Male   | <audio /> |
| `Resemble.Turbo.Amelia_en-US` | en-US    | Female | <audio /> |

***

## WebSocket

### Query Parameters

| Parameter      | Type    | Default | Description                              |
| -------------- | ------- | ------- | ---------------------------------------- |
| `audio_format` | string  | `mp3`   | `mp3`, `wav`.                            |
| `sample_rate`  | integer | `48000` | 8000, 16000, 22050, 32000, 44100, 48000. |

### Voice Settings

| Field         | Type   | Default                       | Description                                                                     |
| ------------- | ------ | ----------------------------- | ------------------------------------------------------------------------------- |
| `format`      | string | `mp3`                         | `mp3` or `wav`.                                                                 |
| `precision`   | string | `PCM_32`                      | `PCM_16`, `PCM_24`, `PCM_32`, `MULAW`.                                          |
| `sample_rate` | string | `48000` (mp3) / `16000` (wav) | `8000`, `16000`, `22050`, `32000`, `44100`, `48000`. Default depends on format. |

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "format": "wav",
    "precision": "PCM_16",
    "sample_rate": "22050"
  }
}
```

## REST API

### Fields

| Field         | Type   | Default           | Description                                      |
| ------------- | ------ | ----------------- | ------------------------------------------------ |
| `format`      | string | `mp3`             | `mp3` or `wav`.                                  |
| `precision`   | string | `PCM_32`          | `PCM_16`, `PCM_24`, `PCM_32`, `MULAW`.           |
| `sample_rate` | string | `48000` / `16000` | Sample rate. Default depends on format.          |
| `output_type` | string | `binary_output`   | `binary_output`, `base64_output`, or `audio_id`. |

### Response

Default (`binary_output`): chunked audio bytes.

With `output_type: "base64_output"`: JSON with base64-encoded audio.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
