---
title: Minimax
summary: Minimax TTS provider — expressive voices with speed, volume, and pitch control.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/minimax
    content_hash: 392b77d3a5e5fbcd3f806db1014fa8c7b40d1e70deec2bc0ecccc9cd4486a00f
updated_at: 2026-04-10T00:00:00Z
---

# Minimax

Minimax TTS provider — expressive voices with speed, volume, and pitch control.

**Voice format:** `minimax..`

`voice_id` can be a **system voice** (pre-built) or a **cloned voice** from the [Voice Design Lab](https://portal.telnyx.com/#/app/ai/voice-design-lab) (organization-scoped).

## Voice Samples

| Voice                                                  | Gender | Sample    |
| ------------------------------------------------------ | ------ | --------- |
| `Minimax.speech-2.8-turbo.English_expressive_narrator` | Male   | <audio /> |
| `Minimax.speech-2.8-turbo.English_radiant_girl`        | Female | <audio /> |

***

## WebSocket

### Query Parameters

| Parameter      | Type    | Default | Description                              |
| -------------- | ------- | ------- | ---------------------------------------- |
| `audio_format` | string  | `mp3`   | `mp3`, `linear16`.                       |
| `sample_rate`  | integer | `24000` | 8000, 16000, 22050, 24000, 32000, 44100. |

### Voice Settings

| Field            | Type    | Default | Description                                   |
| ---------------- | ------- | ------- | --------------------------------------------- |
| `speed`          | float   | —       | Playback speed multiplier.                    |
| `vol`            | float   | —       | Volume level.                                 |
| `pitch`          | integer | —       | Pitch adjustment.                             |
| `language_boost` | string  | —       | Language emphasis for multilingual synthesis. |

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "speed": 1.1,
    "vol": 1.0,
    "pitch": 0
  }
}
```

## REST API

### Fields

| Field            | Type    | Default         | Description                                      |
| ---------------- | ------- | --------------- | ------------------------------------------------ |
| `speed`          | float   | —               | Playback speed multiplier.                       |
| `vol`            | float   | —               | Volume level.                                    |
| `pitch`          | integer | —               | Pitch adjustment.                                |
| `language_boost` | string  | —               | Language emphasis.                               |
| `output_type`    | string  | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

### Response

Default (`binary_output`): chunked audio bytes.

With `output_type: "base64_output"`: JSON with base64-encoded audio.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
