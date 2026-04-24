---
title: Overview
summary: File-based speech-to-text via REST.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
    content_hash: 5057a86b25abc6d5ac26d2418752decd7a7166bcd694b7607d7ee20f2def67a0
updated_at: 2026-04-10T00:00:00Z
---

# Overview

File-based speech-to-text via REST.

`POST /v2/ai/audio/transcriptions`

Synchronous file transcription. Upload audio or pass a URL, get text back.

## Feature Support

If you're coming from alternative providers:

| Feature                  | Status                                                                                                   |
| ------------------------ | -------------------------------------------------------------------------------------------------------- |
| OpenAI SDK compatible    | **Yes** — swap `base_url` and `api_key`, existing code works                                             |
| Multi-engine selection   | **Yes** — 3 models behind one endpoint                                                                   |
| File upload              | **Yes**                                                                                                  |
| URL transcription        | **Yes** (`file_url`)                                                                                     |
| Timestamps (segment)     | **Yes** (`verbose_json`)                                                                                 |
| Timestamps (word-level)  | **Deepgram only** (via `model_config`)                                                                   |
| Diarization              | **Deepgram only** (via `model_config`)                                                                   |
| Smart formatting         | **Deepgram only** (via `model_config`)                                                                   |
| Multilingual             | **Model-dependent** — distil-whisper: English only, whisper-turbo: 80+ languages, Deepgram: English only |
| Async / webhooks         | No                                                                                                       |
| Multichannel             | No (forced mono)                                                                                         |
| Export formats (SRT/VTT) | No                                                                                                       |
| Audio event tagging      | No                                                                                                       |
| YouTube/TikTok URL       | No                                                                                                       |
| Transcript retrieval     | No                                                                                                       |
| File size limit          | 100 MB                                                                                                   |

## Quick Start

  ```python
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_TELNYX_API_KEY",
      base_url="https://api.telnyx.com/v2",
  )

  result = client.audio.transcriptions.create(
      model="distil-whisper/distil-large-v2",
      file=open("audio.mp3", "rb"),
  )
  ```

  ```javascript
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: "YOUR_TELNYX_API_KEY",
    baseURL: "https://api.telnyx.com/v2",
  });

  const result = await client.audio.transcriptions.create({
    model: "distil-whisper/distil-large-v2",
    file: fs.createReadStream("audio.mp3"),
  });
  ```


## Related Pages

- [Overview](../runbooks/overview.md)
