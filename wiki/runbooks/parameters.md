---
title: Parameters
summary: All parameters are sent as `multipart/form-data`.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
    content_hash: 388628406221f89bc7242324bcb1f23ef406454383b8d83247ae16924c055083
updated_at: 2026-04-10T00:00:00Z
---

# Parameters

All parameters are sent as `multipart/form-data`.

<ParamField type="string">
  Model to use for transcription. See [Models](models.md) for details.

  **Values:** `distil-whisper/distil-large-v2` (default), `openai/whisper-large-v3-turbo`, `deepgram/nova-3`

<ParamField type="file">
  Audio file to transcribe. Mutually exclusive with `file_url`. See [Audio Formats](audio-formats.md) for supported formats, size limits, and per-model restrictions.

<ParamField type="string">
  Publicly accessible URL to an audio file. Mutually exclusive with `file`. See [Audio Formats](audio-formats.md) for details on how `file` and `file_url` differ.

<ParamField type="string">
  Language hint. Behavior varies by model — see [Language](https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/language).

<ParamField type="string">
  Output shape. See [Response Format](https://developers.telnyx.com/docs/voice/stt/rest-api/response).

  **Values:** `json` (default), `verbose_json`

<ParamField type="string">
  Timestamp detail level. Only valid with `response_format=verbose_json` — returns 400 otherwise.

  **Values:** `segment`

<ParamField type="object">
  Deepgram-specific options. Only valid with `deepgram/nova-3` — returns 400 for other models. See [Model Config](model-config.md).


## Related Pages

- [Parameters](../runbooks/parameters-2.md)
