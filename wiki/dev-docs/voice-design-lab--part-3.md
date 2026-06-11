---
title: Voice Design Lab
summary: The Telnyx Voice Design Lab lets you create custom text-to-speech voices
  either by describing what you want in natural language (voice design) or by uploading
  a recording of an existing speaker (voice cloning). Both paths produce a production-ready
  voice ID you can use across AI Assistants, Call Control, and the TTS WebSocket API.
sources:
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/concepts/index
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/errors
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/parameters
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/quickstart
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/responses
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/api-details
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/concepts/index
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/prompting-guide
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/quickstart
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/index
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/using-custom-voices/index
updated_at: 2026-06-11T10:49:14Z
---

# Voice Design Lab

*Part 3 of 3 — see also: [Part 1](voice-design-lab--part-1.md), [Part 2](voice-design-lab--part-2.md)*

The Telnyx Voice Design Lab lets you create custom text-to-speech voices either by describing what you want in natural language (voice design) or by uploading a recording of an existing speaker (voice cloning). Both paths produce a production-ready voice ID you can use across AI Assistants, Call Control, and the TTS WebSocket API.

## Errors

### General errors

These errors apply to all providers.

| Endpoint | Status | Code | Detail |
| --- | --- | --- | --- |
| `show` | 404 | 10005 | Clone not found or invalid UUID |
| `create` | 404 | 10005 | Voice design not found / no version |
| `create` | 409 | 10012 | Duplicate `provider_voice_id` |
| `create` | 422 | 10027 | Changeset validation |
| `create_from_upload` | 422 | 10027 | `audio_file is required` |
| `create_from_upload` | 422 | 10027 | File too large. Maximum allowed size is 5MB (20MB for Minimax) |
| `create_from_upload` | 400 | 10015 | Failed to process audio file: \<reason\> (FFmpeg failure) |
| `create_from_upload` | 422 | 10027 | Invalid `provider`+`model_id` combination |
| `update` | 404 | 10005 | Clone not found |
| `update` | 422 | 10027 | Changeset validation errors |
| `delete` | 404 | 10005 | Clone not found |
| `sample` | 404 | 10005 | Clone or sample not found |

### Telnyx / Cartesia errors

| Status | Code | Detail | Provider |
| --- | --- | --- | --- |
| 422 | 10027 | Pattern-matched messages (voice not found, audio too short/long, bad quality, unsupported format, unsupported language, invalid params, text length invalid) | Telnyx/Cartesia |
| 429 | 10011 | `Provider rate limit exceeded` | All providers |

### Minimax errors

| Status | Code | Detail | Provider |
| --- | --- | --- | --- |
| 422 | 10038 | Audio is too short (min 10s) | Minimax (code 2037) |
| 422 | 10038 | Audio is too long | Minimax (code 2038) |
| 422 | 10038 | Audio quality too low | Minimax (code 2039) |
| 422 | 10038 | Audio contains too much noise | Minimax (code 2048) |
| 422 | 10038 | Voice cloning provider error: \<msg\> | Minimax (other codes) |
| 500 | 10037 | Voice clone service configuration error | Auth misconfiguration detected |
| 502 | 10037 | Voice clone service unavailable | Upstream error or connection failure |
