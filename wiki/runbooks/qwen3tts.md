---
title: Qwen3TTS
summary: Telnyx Qwen3TTS — voice cloning with 11-language support.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/qwen3
    content_hash: 25f57897884f51ffb0dd5889cc98662b5a5839babe4d7eb6d286281f5993688b
updated_at: 2026-04-10T00:00:00Z
---

# Qwen3TTS

Telnyx Qwen3TTS — voice cloning with 11-language support.

**Voice format:** `Telnyx.Qwen3TTS.<clone_name>`

Voice cloning model. 11 languages: en, zh, fr, de, it, ja, ko, pt, ru, es, ar.

The `voice_id` is the name of a clone you created in the [Voice Design Lab](https://portal.telnyx.com/#/app/ai/voice-design-lab). Clones are scoped to your organization.

## Voice Samples

| Voice                     | Gender | Sample    |
| ------------------------- | ------ | --------- |
| `Telnyx.Qwen3TTS.Delta`   | Female | <audio /> |
| `Telnyx.Qwen3TTS.Whiskey` | Male   | <audio /> |

***

## WebSocket

### Query Parameters

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.Qwen3TTS.Delta
```

| Parameter      | Type    | Default | Description        |
| -------------- | ------- | ------- | ------------------ |
| `audio_format` | string  | `mp3`   | `mp3`, `linear16`. |
| `sample_rate`  | integer | `24000` | 24000.             |

### Voice Settings

Send in the init frame (`{"text": " "}`):

| Field            | Type    | Default | Description                                                                                                                                                |
| ---------------- | ------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `language_boost` | string  | —       | Target language hint: `Auto`, `English`, `Chinese`, `French`, `German`, `Italian`, `Japanese`, `Korean`, `Portuguese`, `Russian`, `Spanish`, or ISO codes. |
| `force_xvector`  | boolean | `false` | Force x-vector voice embedding.                                                                                                                            |

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "language_boost": "English"
  }
}
```

## REST API

### Fields

| Field            | Type    | Default         | Description                                      |
| ---------------- | ------- | --------------- | ------------------------------------------------ |
| `language_boost` | string  | —               | Target language hint.                            |
| `force_xvector`  | boolean | `false`         | Force x-vector voice embedding.                  |
| `output_type`    | string  | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

### Response

Default (`binary_output`): chunked PCM audio bytes. Always 24kHz signed 16-bit LE mono.

With `output_type: "base64_output"`: JSON with base64-encoded PCM.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
