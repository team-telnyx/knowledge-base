---
title: NaturalHD
summary: Telnyx NaturalHD — multilingual TTS backed by Rime Arcana.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/naturalhd
    content_hash: f4a26b0ae946f043afb4b8e96c473243cd4049a238da4ac3a329370af17dbe47
updated_at: 2026-04-10T00:00:00Z
---

# NaturalHD

Telnyx NaturalHD — multilingual TTS backed by Rime Arcana.

**Voice format:** `Telnyx.NaturalHD.<voice>`

Pre-built voices backed by Rime Arcana. 9 languages: en, fr, de, es, ar, hi, ja, he, pt.

## Voice Samples

| Voice                       | Language | Gender | Sample    |
| --------------------------- | -------- | ------ | --------- |
| `Telnyx.NaturalHD.astra`    | en-US    | Female | <audio /> |
| `Telnyx.NaturalHD.albion`   | en-US    | Male   | <audio /> |
| `Telnyx.NaturalHD.amarante` | fr-FR    | Female | <audio /> |
| `Telnyx.NaturalHD.luna`     | en-US    | Female | <audio /> |

***

## WebSocket

### Query Parameters

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra&audio_format=mp3
```

| Parameter      | Type    | Default | Description                                     |
| -------------- | ------- | ------- | ----------------------------------------------- |
| `audio_format` | string  | `mp3`   | `mp3`, `linear16`.                              |
| `sample_rate`  | integer | `24000` | 8000, 16000, 22050, 24000, 44100, 48000, 96000. |

### Voice Settings

Send in the init frame (`{"text": " "}`):

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

Default (`binary_output`): chunked audio bytes with `Content-Type: audio/mpeg` (or `audio/wav`, `audio/pcm`).

With `output_type: "base64_output"`: JSON with base64-encoded audio.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
