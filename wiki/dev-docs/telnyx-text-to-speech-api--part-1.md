---
title: Telnyx Text-to-Speech API
summary: Telnyx Text-to-Speech provides REST and WebSocket interfaces for synthesizing
  audio from text, supporting real-time streaming playback, multiple TTS providers,
  OpenAI SDK compatibility, and conversational barge-in patterns.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/api-reference
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/examples
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/index
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/pricing
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/request
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/response
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/configuration
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/index
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/messages
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/parameters/voice-settings
- url: https://developers.telnyx.com/docs/voice/uac-connections/index
updated_at: 2026-06-11T10:48:38Z
---

# Telnyx Text-to-Speech API

*Part 1 of 3 — see also: [Part 2](telnyx-text-to-speech-api--part-2.md), [Part 3](telnyx-text-to-speech-api--part-3.md)*

Telnyx Text-to-Speech provides REST and WebSocket interfaces for synthesizing audio from text, supporting real-time streaming playback, multiple TTS providers, OpenAI SDK compatibility, and conversational barge-in patterns.

## REST API

The REST API accepts text and streams audio back over the same HTTP connection using chunked transfer encoding. Audio chunks arrive as they are synthesized, so playback can begin immediately without waiting for the full file. The connection stays open until synthesis completes or 30 seconds pass with no new chunks. For multi-turn conversational flows, use [Telnyx Text-to-Speech API#WebSocket Streaming](telnyx-text-to-speech-api-websocket-streaming.md) instead.

### Endpoint

```
POST https://api.telnyx.com/v2/text-to-speech
```

### Request Body

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | string | Yes | — | Text to synthesize. Markdown is automatically stripped. |
| `voice` | string | Yes | — | Dot-separated voice identifier: `Provider.Model.VoiceId` (e.g., `Telnyx.NaturalHD.astra`) or `Provider.VoiceId` for single-model providers. |
| `output_type` | string | No | `binary_output` | Response format: `binary_output`, `base64_output`, or `audio_id`. |
| `language` | string | No | — | BCP-47 language code (e.g., `en-US`). Supported by AWS Polly, Azure, ElevenLabs, and Inworld. Ignored by other providers. |
| `text_type` | string | No | `text` | `text` or `ssml`. SSML is supported by AWS Polly and Azure. Telnyx Ultra has its own SSML emotion syntax. |
| `voice_settings` | object | No | — | Provider-specific tuning (speed, pitch, format, emotion). Fields vary by provider. |
| `pronunciation_dict_id` | string | No | — | UUID of a custom pronunciation dictionary. Word replacements are applied before synthesis. |
| `disable_cache` | boolean | No | `false` | Bypass the audio cache and always synthesize fresh. |

### Response Formats

The `output_type` field controls the response format.

**Streaming audio** (`binary_output`, default): Raw audio is returned over HTTP chunked transfer encoding with `Content-Type: audio/mpeg`. Start reading the body immediately — do not buffer the full response.

**Base64** (`base64_output`): The full audio is returned as a JSON payload after synthesis completes: `{"base64_audio": "<base64-encoded-audio>"}`. No streaming; the entire file must synthesize before the response is sent.

**Async** (`audio_id`): Synthesis runs in the background. The response returns immediately with `{"audio_url": "https://api.telnyx.com/v2/text-to-speech/speech/<id>"}`. Retrieve the audio later with `GET /v2/text-to-speech/speech/:audio_id`. If synthesis is still in progress, the GET response itself streams chunks as they become available.

### OpenAI SDK Compatibility

The REST endpoint is a drop-in replacement for the OpenAI Audio API:

```python
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

---
