---
title: KokoroTTS
summary: Telnyx KokoroTTS — lowest-latency lightweight TTS.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/kokoro
    content_hash: a1b9a3ed562d948d72f1e0a3ecc3a666a5a8fb9440813f51e8cdd039e7c49e65
updated_at: 2026-04-10T00:00:00Z
---

# KokoroTTS

Telnyx KokoroTTS — lowest-latency lightweight TTS.

**Voice format:** `Telnyx.KokoroTTS.<voice>`

Lightweight, lowest-latency model. 5 languages: en, es, fr, it, pt.

## Voice Samples

| Voice                       | Language | Gender | Sample    |
| --------------------------- | -------- | ------ | --------- |
| `Telnyx.KokoroTTS.af_heart` | en-US    | Female | <audio /> |
| `Telnyx.KokoroTTS.am_adam`  | en-US    | Male   | <audio /> |
| `Telnyx.KokoroTTS.bf_emma`  | en-UK    | Female | <audio /> |

***

## WebSocket

### Query Parameters

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.KokoroTTS.af_heart
```

| Parameter      | Type    | Default | Description        |
| -------------- | ------- | ------- | ------------------ |
| `audio_format` | string  | `mp3`   | `mp3`, `linear16`. |
| `sample_rate`  | integer | `24000` | 24000.             |

### Voice Settings

None. All synthesis parameters are fixed. The init frame only needs `{"text": " "}`.

## REST API

### Fields

No model-specific fields. Audio format is always MP3.

| Field         | Type   | Default         | Description                                      |
| ------------- | ------ | --------------- | ------------------------------------------------ |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

### Response

Default (`binary_output`): chunked audio bytes with `Content-Type: audio/mpeg`.

With `output_type: "base64_output"`: JSON with base64-encoded audio.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
