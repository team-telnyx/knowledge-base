---
title: Telnyx Text-to-Speech WebSocket Streaming
summary: 'Real-time text-to-speech over a persistent WebSocket: open a connection,
  send text frames, and receive base64-encoded audio chunks as they’re synthesized.
  Configure voices and output via URL query parameters and provider-specific voice_settings
  in the init frame, then stream text with optional flushing and barge-in controls.
  Includes message schema, examples, errors, and provider notes.'
sources:
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/index
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/configuration
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/messages
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/parameters/voice-settings
updated_at: 2026-05-20T10:22:43Z
---

# Telnyx Text-to-Speech WebSocket Streaming

*Part 2 of 2 — see also: [Part 1](telnyx-text-to-speech-websocket-streaming--part-1.md)*

Real-time text-to-speech over a persistent WebSocket: open a connection, send text frames, and receive base64-encoded audio chunks as they’re synthesized. Configure voices and output via URL query parameters and provider-specific voice_settings in the init frame, then stream text with optional flushing and barge-in controls. Includes message schema, examples, errors, and provider notes.

## Errors, restrictions, and troubleshooting
HTTP (handshake) errors:
- 400: invalid parameters (unsupported provider, missing fields, bad voice format). Use Provider.Model.VoiceId, e.g., Telnyx.NaturalHD.astra.
- 401: missing/invalid API key. Include Authorization: Bearer <key> on upgrade.
- 403: Ultra model is restricted on the public WebSocket; use [Text-to-Speech REST API](text-to-speech-rest-api.md).
- 403: cloned voice restricted until organization completes identity verification (applies to Qwen3TTS and Minimax clones).

WebSocket (runtime) errors:
- Error frame: {"error":"Error in audio response"} or {"error":"Error in remaining audio response"}. The connection closes shortly after.

Troubleshooting tips:
- No audio after connecting: ensure you sent the handshake frame with a single space first.
- audio is null: expected for streamed providers — collect audio from streamed chunks where text is null.
- Text sent but no response: sentence buffering may be waiting — send more text, include punctuation, or use flush:true.
- Ultra not working on WebSocket: it’s REST-only; use POST /v2/text-to-speech/speech.
- Cloned voice rejected: complete L2 verification in the Telnyx Portal.

## Provider-specific voice_settings reference
Note: there are no global voice_settings fields; each provider defines its own. Supply these once in the handshake frame.
- Telnyx Natural / NaturalHD
  - voice_speed (float, default 1.0): speech rate; >1 is faster.
- Telnyx Ultra (REST-only; not available over WebSocket)
  - voice_speed (float), language_boost (string), volume (float), emotion (string: neutral, happy, sad, angry, fearful, disgusted, surprised).
- Telnyx Qwen3TTS
  - language_boost (string, default "Auto"): accepted values include Auto, English, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish, or ISO codes (en, zh, ...).
- Azure Speech
  - language_code (string, default "en-US"), text_type (text|ssml), effect (eq_car|eq_telecomhp8k), gender (Male|Female).
- AWS Polly
  - language_code (BCP‑47), output_format (string), engine (standard|neural|generative|long-form; default standard), text_type (text|ssml), lexicon_names (array).
- Minimax
  - speed (float), vol (float), pitch (integer), language_boost (string).
- Inworld
  - language_code (string).

## Best practices and gotchas
- Always send the init frame first ("text": " ") and include any voice_settings there.
- Add punctuation or use flush:true to reduce latency from sentence buffering.
- Choose audio_format and sample_rate supported by your target provider and playback path.
- Use disable_cache=true when you must force fresh synthesis; otherwise leverage caching for repeat text.
- Collect audio correctly for your provider: streamed vs concatenated delivery differs by provider.
- Close cleanly with an empty text frame to ensure all buffered audio is returned.
- Ultra voices are not supported over WebSocket; use the REST API instead.
- For phone-call use cases, see [In-Call Playback](in-call-playback.md).
