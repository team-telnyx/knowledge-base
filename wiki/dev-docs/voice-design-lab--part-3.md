---
title: Voice Design Lab
summary: The Telnyx Voice Design Lab lets you create custom text-to-speech voices
  either by describing what you want in natural language (voice design) or by uploading
  a recording of an existing speaker (voice cloning). Both paths produce a production-ready
  voice ID you can use across AI Assistants, Call Control, and the TTS WebSocket API.
sources:
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/concepts/index
  content_hash: c60b20a75a8bace3c2f04b5224c2ce2565c3e6cb725a52bdd479050ae845ef61
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/errors
  content_hash: cf23f295060c031a493711fbb6750713546320b99485c4252f123dcdbe402b26
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/parameters
  content_hash: 54abc1839297816e2c7922e25c897bb9a14cb88ab47ac03cffa7727531771307
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/quickstart
  content_hash: 073b498be8317ba0ec2e125b907bafa353cff565fcff00b9f0df0f67ae437db0
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/responses
  content_hash: 46560a2018645bb9c7cdbca09387618c9f7a6f06c2d8ae371c02044fbb1f2f29
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/api-details
  content_hash: 1725f44827794279807e7725e45b4128c8aca67b6092c874aeee33bf107d7feb
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/concepts/index
  content_hash: 75966e93a539e23aace590fbebab403367d144cf61ee640eb9b05297cc0a010a
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/prompting-guide
  content_hash: cd0e76231d0338c8669aa437f84fd799f1f6c85b14cece0f76fb8943c81b98e1
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/quickstart
  content_hash: 168c94cf0a921cd032a0d6447ee9b17de2077a4f88e1ad5827174092ccb8505a
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/index
  content_hash: 8787000e3f15133ef96752ff10e62e1c6fb200a0c66d6cd730df31fa50f8956f
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/using-custom-voices/index
  content_hash: b6f14a0eeb84a0123e99c58c1003a3d1ef2ef369de363345495e90cf7e94cdea
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
