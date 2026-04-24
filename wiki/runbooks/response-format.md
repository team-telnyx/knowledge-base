---
title: Response Format
summary: Controlled by the `response_format` parameter.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
    content_hash: 420b7f3698203325739da5a1f8fb654d121e44480e44e3bdc1dd45169ee9e103
updated_at: 2026-04-10T00:00:00Z
---

# Response Format

Controlled by the `response_format` parameter.

## `json` (Default)

Text only.

```json theme={null}
{
  "text": "The quick brown fox jumps over the lazy dog."
}
```

## `verbose_json`

Adds `duration` (seconds) and timestamped `segments`.

```json theme={null}
{
  "text": "The quick brown fox jumps over the lazy dog.",
  "duration": 3.42,
  "segments": [
    {
      "id": 0,
      "text": "The quick brown fox jumps over the lazy dog.",
      "start": 0.0,
      "end": 3.42
    }
  ]
}
```

Set `timestamp_granularities[]=segment` alongside `response_format=verbose_json`. Using `timestamp_granularities` without `verbose_json` returns 400.

## Segment Fields

| Field      | Type    | Description                                                                    |
| ---------- | ------- | ------------------------------------------------------------------------------ |
| `id`       | integer | Zero-indexed segment number                                                    |
| `text`     | string  | Segment transcript                                                             |
| `start`    | float   | Start time in seconds                                                          |
| `end`      | float   | End time in seconds                                                            |
| `words`    | array   | Word-level timestamps (present when the backend provides them — Deepgram only) |
| `speakers` | array   | Speaker labels (present when `diarize=true` in `model_config` — Deepgram only) |

## Timestamp Availability by Model

| Model                            | `verbose_json` timestamps                           |
| -------------------------------- | --------------------------------------------------- |
| `distil-whisper/distil-large-v2` | Segment-level start/end (from Bumblebee streaming)  |
| `openai/whisper-large-v3-turbo`  | **No timestamps** — backend returns text only       |
| `deepgram/nova-3`                | Segment-level + word-level (from Deepgram response) |

## Streaming Response (Undocumented)

Sending `Accept: application/stream+json` returns newline-delimited JSON chunks as segments are transcribed. Each line:

```json theme={null}
{"text": "segment text", "start": 0.0, "end": 3.42}
```

This is used internally but not in the public OAS spec.


## Related Pages

- [Response](../runbooks/response.md)
- [SIP Response Codes](../runbooks/sip-response-codes.md)
