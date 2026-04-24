---
title: Azure Speech
summary: Azure Speech TTS provider — multilingual neural voices with SSML support.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/azure
    content_hash: 5b1ad5de02ff5f7b121e335013550c429561d10ed1207fb38170a740a49f15c2
updated_at: 2026-04-10T00:00:00Z
---

# Azure Speech

Azure Speech TTS provider — multilingual neural voices with SSML support.

**Voice format:** `azure.`

Example: `azure.en-US-AvaMultilingualNeural`

No model ID segment — Azure voices are flat identifiers. Default voice: `en-US-AvaMultilingualNeural`.

## Voice Samples

| Voice                                  | Language | Gender | Sample    |
| -------------------------------------- | -------- | ------ | --------- |
| `azure.en-US-AvaMultilingualNeural`    | en-US    | Female | <audio /> |
| `azure.en-US-AndrewMultilingualNeural` | en-US    | Male   | <audio /> |

***

## WebSocket

### Query Parameters

| Parameter      | Type    | Default | Description                                                                  |
| -------------- | ------- | ------- | ---------------------------------------------------------------------------- |
| `audio_format` | string  | `mp3`   | `mp3`, `wav`, `linear16`, `mulaw`, `alaw`.                                   |
| `sample_rate`  | integer | `24000` | 8000, 16000, 24000, 48000.                                                   |
| `language`     | string  | `en-US` | BCP-47 language code.                                                        |
| `text_type`    | string  | `text`  | `text` or `ssml`. Azure supports SSML for pronunciation and prosody control. |

### Voice Settings

| Field           | Type   | Default                            | Description                                                                                                                      |
| --------------- | ------ | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `output_format` | string | `audio-24khz-160kbitrate-mono-mp3` | See [Azure audio formats](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs). |
| `language_code` | string | `en-US`                            | BCP-47. Overrides `language` query param.                                                                                        |
| `text_type`     | string | `text`                             | `text` or `ssml`. Overrides query param.                                                                                         |
| `effect`        | string | —                                  | `eq_car`, `eq_telecomhp8k`. Audio equalization.                                                                                  |
| `gender`        | string | —                                  | `Male`, `Female`. Voice gender filter.                                                                                           |

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "output_format": "audio-48khz-192kbitrate-mono-mp3",
    "effect": "eq_car"
  }
}
```

## REST API

### Fields

| Field           | Type   | Default                            | Description                                      |
| --------------- | ------ | ---------------------------------- | ------------------------------------------------ |
| `output_format` | string | `audio-24khz-160kbitrate-mono-mp3` | Azure audio format string.                       |
| `language_code` | string | `en-US`                            | BCP-47 language code.                            |
| `text_type`     | string | `text`                             | `text` or `ssml`.                                |
| `effect`        | string | —                                  | `eq_car`, `eq_telecomhp8k`.                      |
| `gender`        | string | —                                  | `Male`, `Female`.                                |
| `output_type`   | string | `binary_output`                    | `binary_output`, `base64_output`, or `audio_id`. |

### Response

Default (`binary_output`): chunked audio bytes.

With `output_type: "base64_output"`: JSON with base64-encoded audio.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
