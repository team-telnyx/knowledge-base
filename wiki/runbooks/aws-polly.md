---
title: AWS Polly
summary: AWS Polly TTS provider — neural, generative, and long-form synthesis engines.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/aws
    content_hash: cff9a280dd5b55be3e1af608b8445a84e7fa875266fcabe72d033d2011f4ed9f
updated_at: 2026-04-10T00:00:00Z
---

# AWS Polly

AWS Polly TTS provider — neural, generative, and long-form synthesis engines.

**Voice format:** `aws.Polly..`

Example: `aws.Polly.Generative.Lucia`

The engine can also be parsed from a hyphenated suffix on the voice ID — e.g., `Lucia-longform` resolves to engine `long-form`.

## Voice Samples

| Voice                        | Language | Gender | Sample    |
| ---------------------------- | -------- | ------ | --------- |
| `aws.Polly.Danielle-Neural`  | en-US    | Female | <audio /> |
| `aws.Polly.Gregory-Neural`   | en-US    | Male   | <audio /> |
| `aws.Polly.Lucia-Generative` | es-ES    | Female | <audio /> |

***

## WebSocket

### Query Parameters

| Parameter      | Type    | Default | Description                                                             |
| -------------- | ------- | ------- | ----------------------------------------------------------------------- |
| `audio_format` | string  | `mp3`   | `mp3`, `linear16`, `ogg_vorbis`.                                        |
| `sample_rate`  | integer | —       | 8000, 16000, 22050, 24000.                                              |
| `language`     | string  | —       | BCP-47 language code. Passed as `language_code` to Polly.               |
| `text_type`    | string  | `text`  | `text` or `ssml`. Polly supports SSML for fine-grained prosody control. |

### Voice Settings

| Field           | Type   | Default    | Description                                                                                                                                   |
| --------------- | ------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `engine`        | string | `standard` | `standard`, `neural`, `generative`, `long-form`.                                                                                              |
| `output_format` | string | —          | Any [Polly output format](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-OutputFormat). |
| `sample_rate`   | string | —          | e.g. `"8000"`, `"16000"`, `"22050"`, `"24000"`. Valid values depend on engine and format.                                                     |
| `lexicon_names` | array  | —          | Pronunciation lexicon names to apply.                                                                                                         |
| `language_code` | string | —          | BCP-47. Overrides `language` query param.                                                                                                     |
| `text_type`     | string | `text`     | `text` or `ssml`. Overrides query param.                                                                                                      |

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "engine": "generative",
    "output_format": "mp3",
    "sample_rate": "24000"
  }
}
```

## REST API

### Fields

| Field           | Type   | Default         | Description                                      |
| --------------- | ------ | --------------- | ------------------------------------------------ |
| `engine`        | string | `standard`      | `standard`, `neural`, `generative`, `long-form`. |
| `output_format` | string | —               | Polly output format.                             |
| `sample_rate`   | string | —               | Sample rate in Hz.                               |
| `lexicon_names` | array  | —               | Pronunciation lexicon names.                     |
| `language_code` | string | —               | BCP-47 language code.                            |
| `text_type`     | string | `text`          | `text` or `ssml`.                                |
| `output_type`   | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

### Response

Default (`binary_output`): chunked audio bytes. Format depends on `output_format`.

With `output_type: "base64_output"`: JSON with base64-encoded audio.

With `output_type: "audio_id"`: JSON with an `audio_url` for deferred retrieval.
