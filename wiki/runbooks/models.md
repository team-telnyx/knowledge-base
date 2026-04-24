---
title: Models
summary: Your choice of `model` determines which audio formats are accepted, what `language` values are valid, and what response fields are available.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
    content_hash: 63006792e82110193c952b8162baf00e6f24b30cd9ff8a29bd495ecaa0809853
updated_at: 2026-04-10T00:00:00Z
---

# Models

Your choice of `model` determines which audio formats are accepted, what `language` values are valid, and what response fields are available.

|                      | `distil-whisper/distil-large-v2`           | `openai/whisper-large-v3-turbo` | `deepgram/nova-3`                                                         |
| -------------------- | ------------------------------------------ | ------------------------------- | ------------------------------------------------------------------------- |
| **Default**          | Yes                                        |                                 |                                                                           |
| **Audio formats**    | All 10                                     | All 10                          | mp3, wav only                                                             |
| **Language**         | English only (rejects `language` with 400) | 80+ languages, auto-detected    | English variants only (`en`, `en-US`, `en-GB`, `en-AU`, `en-NZ`, `en-IN`) |
| **Timestamps**       | Segment-level (`verbose_json`)             | No                              | Word-level (via `model_config`)                                           |
| **Diarization**      | No                                         | No                              | Yes (via `model_config`)                                                  |
| **Smart formatting** | No                                         | No                              | Yes (via `model_config`)                                                  |
| **`model_config`**   | Returns 400                                | Returns 400                     | [Deepgram pass-through](model-config.md) |

### `distil-whisper/distil-large-v2`

Lowest latency. Runs on-device. English only — setting `language` returns 400.

### `openai/whisper-large-v3-turbo`

Multilingual. Auto-detected if `language` omitted. See [Whisper docs](https://github.com/openai/whisper#available-models-and-languages) for the full language list. Returns text only — no timestamps regardless of `response_format`.

### `deepgram/nova-3`

Highest accuracy for English. Advanced features (diarization, word timestamps, smart formatting, numerals, punctuation) available via [`model_config`](model-config.md). Defaults `language` to `en` if omitted. Can also set `language` inside `model_config` — top-level field takes precedence. See [Deepgram language docs](https://developers.deepgram.com/docs/models-languages-overview) for details.
