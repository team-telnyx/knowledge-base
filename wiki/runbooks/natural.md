---
title: Natural
summary: Telnyx Natural — low-latency English TTS backed by Rime Mist.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/natural
    content_hash: dd9aa41dc339f2c802f4a721f9f43a9e0afcfaed39b766fc5b4063db39587528
updated_at: 2026-04-10T00:00:00Z
---

# Natural

Telnyx Natural — low-latency English TTS backed by Rime Mist.

**Voice format:** `Telnyx.Natural.<voice>`

Pre-built English voices backed by Rime Mist.

## Voice Samples

| Voice                    | Gender | Sample    |
| ------------------------ | ------ | --------- |
| `Telnyx.Natural.allison` | Female | <audio /> |
| `Telnyx.Natural.brook`   | Female | <audio /> |

***

## WebSocket

### Query Parameters

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.Natural.allison&audio_format=mp3
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
    "voice_speed": 1.2
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
