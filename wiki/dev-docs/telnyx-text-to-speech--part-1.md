---
title: Telnyx Text-to-Speech
summary: Telnyx Text-to-Speech (TTS) provides streaming speech synthesis over both
  REST and WebSocket transports, with multiple voice providers (Telnyx-branded models
  and xAI Grok), OpenAI SDK compatibility, and provider-specific tuning for speed,
  language, emotion, and voice cloning.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/kokoro
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/natural
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/naturalhd
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/qwen3
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/sukhan
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/ultra
- url: https://developers.telnyx.com/docs/voice/tts/providers/xai
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/api-reference
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/examples
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/index
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/pricing
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/request
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/response
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/configuration
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/errors
updated_at: 2026-08-05T14:06:54Z
---

# Telnyx Text-to-Speech

*Part 1 of 4 — see also: [Part 2](telnyx-text-to-speech--part-2.md), [Part 3](telnyx-text-to-speech--part-3.md), [Part 4](telnyx-text-to-speech--part-4.md)*

Telnyx Text-to-Speech (TTS) provides streaming speech synthesis over both REST and WebSocket transports, with multiple voice providers (Telnyx-branded models and xAI Grok), OpenAI SDK compatibility, and provider-specific tuning for speed, language, emotion, and voice cloning.

## Overview

Telnyx Text-to-Speech streams synthesized audio back to the client over HTTP chunked transfer encoding (REST) or a persistent WebSocket connection. Audio chunks arrive as they are generated, so clients can begin playback immediately without waiting for the full file. The REST connection stays open until synthesis completes or 30 seconds pass with no new chunks. For multi-turn conversational use cases where text is continuously fed in, use [WebSocket Streaming](websocket-streaming.md) instead.

The full OpenAPI spec is available in the [API Reference](api-reference.md). Note: the OAS is currently being cleaned up — some fields and provider-specific schemas may be incomplete.

## REST API

### Endpoint

```
POST https://api.telnyx.com/v2/text-to-speech/speech
```

### Example

```
curl --request POST \
  --url https://api.telnyx.com/v2/text-to-speech/speech \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "text": "Hello from Telnyx text-to-speech.",
  "voice": "Telnyx.NaturalHD.astra"
}'
```

### Request Body

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `text` | string | Yes | — | Text to synthesize. Markdown is automatically stripped. |
| `voice` | string | Yes | — | Dot-separated voice identifier. Format: `Provider.Model.VoiceId` (e.g., `Telnyx.NaturalHD.astra`) or `Provider.VoiceId` when the provider has a single model. |
| `output_type` | string | No | `binary_output` | Response format: `binary_output`, `base64_output`, or `audio_id`. |
| `language` | string | No | — | BCP-47 language code (e.g., `en-US`). Supported by AWS Polly, Azure, ElevenLabs, and Inworld. Ignored by other providers. |
| `text_type` | string | No | `text` | `text` or `ssml`. SSML is supported by AWS Polly and Azure. Ultra has its own [SSML emotion syntax](/docs/voice/tts/providers/telnyx/ultra#ssml-emotions). |
| `voice_settings` | object | No | — | Provider-specific tuning (speed, pitch, format, emotion). Fields vary by provider — see individual [provider pages](/docs/voice/tts/providers/telnyx). |
| `pronunciation_dict_id` | string | No | — | UUID of a custom pronunciation dictionary. Word replacements are applied before synthesis. |
| `disable_cache` | boolean | No | `false` | Bypass the audio cache and always synthesize fresh. |

### Text Preprocessing

Before synthesis, text passes through two stages:

1. **Markdown stripping** — headers, bold, italics, code blocks, links, lists, emoji are converted to plain text.
2. **Pronunciation dictionary** — if `pronunciation_dict_id` is set, custom word replacements are applied.

### Response

The `output_type` request field controls what comes back.

**Streaming Audio (default)** — With `output_type: "binary_output"` (or omitted), the response is raw audio over HTTP chunked transfer encoding:

```
HTTP/1.1 200 OK
Content-Type: audio/mpeg
Transfer-Encoding: chunked

<audio chunk 1>
<audio chunk 2>
...
```

Start reading the body immediately — don't buffer the full response.

**Base64** — With `output_type: "base64_output"`, the full audio is returned as a JSON payload after synthesis completes:

```
{"base64_audio": "<base64-encoded-audio>"}
```

No streaming — the entire file must synthesize before the response is sent.

**Async (audio_id)** — With `output_type: "audio_id"`, synthesis runs in the background. You get a URL back immediately:

```
{"audio_url": "https://api.telnyx.com/v2/text-to-speech/speech/<id>"}
```

Retrieve the audio later with `GET /v2/text-to-speech/speech/:audio_id`. If the audio is still synthesizing, the GET response itself streams chunks as they become available.

### OpenAI SDK Compatibility

The REST endpoint is a drop-in replacement for the OpenAI Audio API:

```
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_TELNYX_API_KEY",
    base_url="https://api.telnyx.com/v2"
)

response = client.audio.speech.create(
    model="tts-1-hd",
    voice="astra",
    input="Hello from Telnyx."
)

response.stream_to_file("output.mp3")
```
