---
title: Telnyx Text-to-Speech API
summary: Telnyx Text-to-Speech provides REST and WebSocket interfaces for synthesizing
  audio from text, supporting real-time streaming playback, multiple TTS providers,
  OpenAI SDK compatibility, and conversational barge-in patterns.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/api-reference
  content_hash: ea02fe06331e52e5066dff833c0598afde79b7bebeb61c1e3191cdc75f53b7e9
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/examples
  content_hash: 16ef22cb54e6ed6b1ae5c1fdb59b5b4bd5ea07be53581286541f1ced958f35b6
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/index
  content_hash: b6ca6f23cce45ad8ec4201e7fe0c703195a7e1f39626b10555d8fc30e0d53e73
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/pricing
  content_hash: d7275459734a88ed4e899a6ee9439929757b64aca9a7baf7ed22effb4953e6ba
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/request
  content_hash: 35370ca7212ed1f9de549b11f021a3387c2c8bec90e8f7ca815d2d8681de73d7
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/response
  content_hash: e8acfc6badb9c6f87283a243075f9300887d69b7673a625efae904345e9c6cca
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/configuration
  content_hash: 6b5a3bafecd321fcebf90e7e4ef069b88fb7a861a3562a4b1a651e72eff46d88
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/errors
  content_hash: ce2d0a0292324cec09128617bf277fcea51dc75bdc197b360a1a78af647bd877
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/examples
  content_hash: 926d8e69d30c20170b72e51895b5b8367f76cc845c132482dbf757c3540adf64
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/index
  content_hash: b4419a32235d92f689dd7f467814a442fe82985e7d406bfa5efd8e8d3c99d00f
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/messages
  content_hash: 87cdb6015b8d1abc8eebf5e73335cc22e6d5a756d03954e09aeef86c3b1bc52f
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/parameters/voice-settings
  content_hash: 804699ea5b600de602be28e823e2c21a2b0561ace23918e170f806af340b39a6
- url: https://developers.telnyx.com/docs/voice/uac-connections/index
  content_hash: fb4414be84cc9e9646e863d99b8f58a7a8ca9b2d4959833f3510ade01629b2d9
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
