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

*Part 2 of 4 — see also: [Part 1](telnyx-text-to-speech--part-1.md), [Part 3](telnyx-text-to-speech--part-3.md), [Part 4](telnyx-text-to-speech--part-4.md)*

Telnyx Text-to-Speech (TTS) provides streaming speech synthesis over both REST and WebSocket transports, with multiple voice providers (Telnyx-branded models and xAI Grok), OpenAI SDK compatibility, and provider-specific tuning for speed, language, emotion, and voice cloning.

## WebSocket Streaming

### Configuration Surfaces

WebSocket TTS exposes two configuration surfaces, both one-shot and immutable for the session:

| Surface | When | What | Mutable? |
| --- | --- | --- | --- |
| Query parameters | WebSocket URL | Voice selection, audio format, sample rate, connection options | No — locked at connect |
| `voice_settings` | Init frame (`{"text": " "}`) | Provider-specific tuning (speed, pitch, format, etc.) | No — locked at init |

After the init frame, no configuration can change for the session. To change settings, open a new connection.

### Query Parameters

Set on the URL at connect time. Immutable for the session.

**Voice Selection**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `voice` | string | — | Voice identifier in `Provider.Model.VoiceId` format. |

The `voice_id` segment (third part of the `voice` string) refers to different things depending on the provider and model:

| Type | Example | How you get it |
| --- | --- | --- |
| **Pre-built voice** | `Telnyx.NaturalHD.astra` | Browse via the [Voices API](https://developers.telnyx.com/api-reference/text-to-speech-commands/list-available-voices) or [Voice Design](https://portal.telnyx.com/#/app/ai/voice-design-lab). Shipped by the provider — available to everyone. |
| **Your cloned voice** | `Telnyx.Qwen3TTS.my-ceo-clone` | Create in the [Voice Design](https://portal.telnyx.com/#/app/ai/voice-design-lab). Scoped to your organization — only your API key can use it. Available for Qwen3TTS and Minimax. |
| **BYOK provider voice** | `elevenlabs.v3.Adam` | A voice ID from your own ElevenLabs or Resemble account. You bring your own API key; Telnyx relays the request. |

The Voices API (`GET /v2/ai/tts/voices`) returns all voices available to your account — pre-built and cloned — with each voice's compound `id` ready to use as the `voice` parameter.

**Connection Options**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `language` | string | — | BCP-47 language code. Passed to the provider as `language_code`. Only used by providers that accept it (AWS Polly, Azure, ElevenLabs, Inworld). |
| `text_type` | string | `text` | Text type hint: `text` or `ssml`. Only AWS Polly and Azure use this. |
| `audio_format` | string | `mp3` | Output audio format: `mp3`, `linear16`, `wav`, `mulaw`, `alaw`, `ogg_vorbis`. Not all formats are supported by every provider — see providers' dedicated pages. |
| `sample_rate` | integer | provider default | Output sample rate in Hz. Accepted values vary by provider — see providers' dedicated pages. |
| `disable_cache` | boolean | `false` | Bypass the audio cache and always synthesize fresh. |

Example:

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra&audio_format=linear16&disable_cache=true
```

### Voice Settings

Provider-specific tuning (speed, pitch, format, emotion, etc.) is not set via query parameters. It is passed once in the `voice_settings` object on the initialization frame:

```
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 1.2,
    "emotion": "happy"
  }
}
```

Voice settings are applied when the synthesis worker starts and cannot be changed mid-session. **There are no common `voice_settings` fields.** Every field is provider-specific — the available fields, defaults, and accepted values are completely different per provider. Unrecognized fields are silently ignored. See your selected provider's page under [Providers](providers.md) for the exact fields.

### Errors

**HTTP Errors (Handshake)** — These occur during the WebSocket upgrade request, before the connection is established.

| Code | Cause |
| --- | --- |
| 400 | Invalid parameters — unsupported provider, missing required fields, or invalid voice format |
| 401 | Missing or invalid API key |
| 403 | Ultra model restricted on public WebSocket endpoint. Use [REST API](rest-api.md) for Ultra. |
| 403 | Cloned voice restricted — organization requires identity verification for cloned voices (Qwen3TTS, Minimax clones) |

**WebSocket Errors (Runtime)** — After the connection is established, errors arrive as JSON frames:

```
{
  "error": "Error in audio response"
}
```

The connection closes shortly after an error frame.

| Error | Cause |
| --- | --- |
| `"Error in audio response"` | The TTS provider returned an error during synthesis |
| `"Error in remaining audio response"` | Provider error while synthesizing buffered text during connection close |

**Troubleshooting**

| Symptom | Cause | Fix |
| --- | --- | --- |
| Connection rejected (400) | Invalid voice format | Use `Provider.Model.VoiceId` format (e.g., `Telnyx.NaturalHD.astra`) |
| Connection rejected (401) | Missing auth | Pass `Authorization: Bearer <key>` header during WebSocket upgrade |
| No audio after connecting | Missing handshake | Send `{"text": " "}` as first frame |
| `audio` field is `null` | Expected behavior | For streamed providers (Telnyx, Rime, Minimax, Resemble, Inworld), audio arrives in separate streamed frames |
| Text sent but no response | Sentence buffering | Text is buffered until a sentence boundary. Send more text, use `flush: true`, or end with punctuation |
| Ultra not working on WebSocket | Intentional restriction | Ultra is REST-only. Use `POST /v2/text-to-speech/speech` |
| Cloned voice rejected | Identity verification required | Complete L2 verification in the [Telnyx Portal](https://portal.telnyx.com) |
