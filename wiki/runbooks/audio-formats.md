---
title: Audio Formats
summary: Applies to both `file` (multipart upload) and `file_url` (URL download).
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
    content_hash: 13912adda3af9525227383a5b03b2718be8bdf7c502a44de3643480747b44623
updated_at: 2026-04-10T00:00:00Z
---

# Audio Formats

Applies to both `file` (multipart upload) and `file_url` (URL download).

## Common

* **Max size:** 100 MB
* **Processing:** All audio is decoded, resampled to 16kHz, and mixed to mono via ffmpeg before transcription. Container format doesn't matter as long as ffmpeg can decode it — the validated extension list is the actual restriction.

## Supported Formats

| Format | `distil-whisper` | `whisper-turbo` | `deepgram/nova-3` |
| ------ | ---------------- | --------------- | ----------------- |
| flac   | Yes              | Yes             | No                |
| m4a    | Yes              | Yes             | No                |
| mp3    | Yes              | Yes             | **Yes**           |
| mp4    | Yes              | Yes             | No                |
| mpeg   | Yes              | Yes             | No                |
| mpga   | Yes              | Yes             | No                |
| oga    | Yes              | Yes             | No                |
| ogg    | Yes              | Yes             | No                |
| wav    | Yes              | Yes             | **Yes**           |
| webm   | Yes              | Yes             | No                |

## `file` vs `file_url`

|            | `file`                           | `file_url`                                                  |
| ---------- | -------------------------------- | ----------------------------------------------------------- |
| Delivery   | Multipart upload in request body | Server downloads from URL before transcription              |
| Timeout    | Request timeout                  | 15s download timeout                                        |
| Auth       | N/A                              | URL must be publicly accessible (no auth headers forwarded) |
| Validation | Same format and size checks      | Same format and size checks                                 |

One of `file` or `file_url` is required. Sending both returns 400.


## Related Pages

- [Audio Formats](../runbooks/audio-formats-2.md)
