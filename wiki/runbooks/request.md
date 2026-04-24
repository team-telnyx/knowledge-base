---
title: Request
summary: REST TTS request body fields — text, voice, output type, and provider-specific settings.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/rest-api/request
    content_hash: 80243179bc40e9cc7391819eb3b40adea314cdd255316978b07a8d1443ba1476
updated_at: 2026-04-10T00:00:00Z
---

# Request

REST TTS request body fields — text, voice, output type, and provider-specific settings.

## Endpoint

```
POST https://api.telnyx.com/v2/text-to-speech
```

## Example

```bash theme={null}
curl --request POST \
  --url https://api.telnyx.com/v2/text-to-speech \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "text": "Hello from Telnyx text-to-speech.",
  "voice": "Telnyx.NaturalHD.astra"
}'
```

## Request Body

| Field                   | Type    | Required | Default         | Description                                                                                                                                                   |
| ----------------------- | ------- | -------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `text`                  | string  | Yes      | —               | Text to synthesize. Markdown is automatically stripped.                                                                                                       |
| `voice`                 | string  | Yes      | —               | Dot-separated voice identifier. Format: `Provider.Model.VoiceId` (e.g., `Telnyx.NaturalHD.astra`) or `Provider.VoiceId` when the provider has a single model. |
| `output_type`           | string  | No       | `binary_output` | Response format: `binary_output`, `base64_output`, or `audio_id`.                                                                                             |
| `language`              | string  | No       | —               | BCP-47 language code (e.g., `en-US`). Supported by AWS Polly, Azure, ElevenLabs, and Inworld. Ignored by other providers.                                     |
| `text_type`             | string  | No       | `text`          | `text` or `ssml`. SSML is supported by AWS Polly and Azure. Ultra has its own [SSML emotion syntax](ultra.md#ssml-emotions).    |
| `voice_settings`        | object  | No       | —               | Provider-specific tuning (speed, pitch, format, emotion). Fields vary by provider — see individual [provider pages](telnyx.md).        |
| `pronunciation_dict_id` | string  | No       | —               | UUID of a custom pronunciation dictionary. Word replacements are applied before synthesis.                                                                    |
| `disable_cache`         | boolean | No       | `false`         | Bypass the audio cache and always synthesize fresh.                                                                                                           |
