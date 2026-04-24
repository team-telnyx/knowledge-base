---
title: Rime
summary: Rime TTS provider — ArcanaV3 model with speed and format control.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/rime
    content_hash: e76bb777d54f0275ac7c96cd72504724c2bf57303c74deb03fb3c34632f0ac6d
updated_at: 2026-04-10T00:00:00Z
---

# Rime

Rime TTS provider — ArcanaV3 model with speed and format control.

**Voice format:** `rime.ArcanaV3.`

## Voice Samples

| Voice                  | Language | Gender | Sample    |
| ---------------------- | -------- | ------ | --------- |
| `Rime.ArcanaV3.albion` | en-US    | Male   | <audio /> |
| `Rime.ArcanaV3.arcade` | en-US    | Male   | <audio /> |

***

## WebSocket

### Query Parameters

| Parameter      | Type    | Default | Description                                     |
| -------------- | ------- | ------- | ----------------------------------------------- |
| `audio_format` | string  | `mp3`   | `mp3`, `linear16`.                              |
| `sample_rate`  | integer | `24000` | 8000, 16000, 22050, 24000, 44100, 48000, 96000. |

### Voice Settings

| Field         | Type  | Default | Description             |
| ------------- | ----- | ------- | ----------------------- |
| `voice_speed` | float | `1.0`   | Speech rate multiplier. |

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 0.9
  }
}
```

## REST API

### Fields

| Field         | Type   | Default         | Description                                      |
| ------------- | ------ | --------------- | ------------------------------------------------ |
| `voice_speed` | float  | `1.0`           | Speech rate multiplier.                          |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

### Response

Default (`binary_output`): chunked audio bytes.

With `output_type: "base64_output"`: JSON with base64-encoded audio.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
