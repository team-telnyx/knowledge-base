---
title: Inworld
summary: Inworld TTS provider — Mini (low-latency) and Max (high-quality) models.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/inworld
    content_hash: 584f480b9751baa4181592a030c7ea52fe4ce6ffb5f30a9a7fe5d7a117601258
updated_at: 2026-04-10T00:00:00Z
---

# Inworld

Inworld TTS provider — Mini (low-latency) and Max (high-quality) models.

**Voice format:** `inworld..`

**Models:** `inworld-tts-1.5-mini` (alias `Mini` — faster) and `inworld-tts-1.5-max` (alias `Max` — higher quality). Defaults to `mini`.

## Voice Samples

| Voice                  | Model | Gender | Sample    |
| ---------------------- | ----- | ------ | --------- |
| `Inworld.Max.Hank`     | Max   | Male   | <audio /> |
| `Inworld.Mini.Loretta` | Mini  | Female | <audio /> |

***

## WebSocket

### Query Parameters

| Parameter      | Type    | Default | Description                              |
| -------------- | ------- | ------- | ---------------------------------------- |
| `audio_format` | string  | `mp3`   | `mp3`, `linear16`.                       |
| `sample_rate`  | integer | `24000` | 8000, 16000, 22050, 24000, 44100, 48000. |
| `language`     | string  | —       | BCP-47 language code.                    |

### Voice Settings

| Field           | Type    | Default | Description                               |
| --------------- | ------- | ------- | ----------------------------------------- |
| `encoding`      | string  | `MP3`   | `MP3` or `LINEAR16`.                      |
| `sample_rate`   | integer | `24000` | Output sample rate in Hz.                 |
| `language_code` | string  | —       | BCP-47. Overrides `language` query param. |

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "encoding": "LINEAR16",
    "sample_rate": 16000
  }
}
```

## REST API

### Fields

| Field           | Type    | Default         | Description                                      |
| --------------- | ------- | --------------- | ------------------------------------------------ |
| `encoding`      | string  | `MP3`           | `MP3` or `LINEAR16`.                             |
| `sample_rate`   | integer | `24000`         | Output sample rate in Hz.                        |
| `language_code` | string  | —               | BCP-47 language code.                            |
| `output_type`   | string  | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

### Response

Default (`binary_output`): chunked audio bytes.

With `output_type: "base64_output"`: JSON with base64-encoded audio.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
