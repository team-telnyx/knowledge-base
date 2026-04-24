---
title: Engines & Models
summary: Available transcription engines and models.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/engines-and-models
    content_hash: 37ff172a6a4f54204c4462120d4d274350844aa3c31284552b979cca4281b9f4
updated_at: 2026-04-10T00:00:00Z
---

# Engines & Models

Available transcription engines and models.

Set via `transcription_engine` and `model` query parameters.

## Engines

| Engine       | Default model         | Other models     | Notes                                    |
| ------------ | --------------------- | ---------------- | ---------------------------------------- |
| **Deepgram** | `nova-3`              | `nova-2`, `flux` | Default engine. Broadest format support. |
| **Telnyx**   | `openai/whisper-tiny` | —                | On-network, lightweight                  |
| **Google**   | `latest_long`         | —                | Multilingual, long-form                  |
| **Azure**    | `azure/fast`          | —                | Broad language/accent coverage           |

## Flux Model

Deepgram's lowest-latency model with built-in [end-of-turn detection](end-of-turn-detection.md). Designed for real-time voice agents. See [Audio Formats](audio-formats-2.md) for supported formats.
