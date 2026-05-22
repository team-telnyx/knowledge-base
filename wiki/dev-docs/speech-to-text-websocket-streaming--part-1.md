---
title: Speech-to-Text WebSocket Streaming
summary: 'Real-time speech-to-text over a persistent WebSocket: send binary audio
  frames, receive interim and final transcripts. Configure engine, model, format,
  language, and options via query parameters at connect time. This page covers endpoints,
  lifecycle, parameters, audio formats, wire protocol, errors, production guidance,
  pricing, and an end-to-end example.'
sources:
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/index
  content_hash: 09b104a25721bd87168490feb07ae4fc9ddfd07304f76b90fbd3642920495125
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/index
  content_hash: fc286d165d2260a3fa064eeda887950dbbd0f8ad7f956b36a8545a00ca90c864
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/audio-formats
  content_hash: e0d34a29c46c6372a9356a8036cd49c34b29a8437595b5a7fccde6d8ad981856
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/end-of-turn
  content_hash: f0e5888926d16fed90a706a9f92bf9bbccb018631fff96bf57e2c057c7fd79f8
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/endpointing
  content_hash: a1f3a9060786a65476d177e467409af4772ac58717621e2ed6516afcbbfef7b2
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/engines-and-models
  content_hash: 362de89d372ea0d403ca92a7e0b81c0fa5467fc37ecffdc33d7e334373a9f229
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/interim-results
  content_hash: 2f41e386c19cbba310b0bbcae1164746c943aa7b110b77386a5fa9f0a0db3d28
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/keyword-boosting
  content_hash: f129015ff10e07db0d279486c1bb4ea5bb3838675f722a4602b00dfbce74aad6
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/language
  content_hash: b599a1715663f74d0fc9301d99cf7191bbe144fe3c10c8862f1fdb01582434da
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/redaction
  content_hash: 733da97cc355231be87e2593047db6221e4e11178a52f4c21e0854de68887075
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/pricing
  content_hash: 47996e9df70d41e1ad325e83c9168d97a744af63de2c58edee059c87323ca019
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/production-patterns
  content_hash: e163ee28e71bc85f54ec568e364ea3578a8b6226e9e1d8c16e479bdc441975ee
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/responses
  content_hash: 506aa628828daa09b9b21ba07591e34c344200416e0338bfd4b29a0008ae374a
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/errors
  content_hash: d163ced5de0e3ddcb430ba60abd04097868bf969469725ee1db40abee0641695
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/examples
  content_hash: c4973c5983c7fc8c1f3f27cd789b7ea1f523127d749ee5d1814beb2d40e72687
updated_at: 2026-05-20T10:05:31Z
---

# Speech-to-Text WebSocket Streaming

*Part 1 of 2 — see also: [Part 2](speech-to-text-websocket-streaming--part-2.md)*

Real-time speech-to-text over a persistent WebSocket: send binary audio frames, receive interim and final transcripts. Configure engine, model, format, language, and options via query parameters at connect time. This page covers endpoints, lifecycle, parameters, audio formats, wire protocol, errors, production guidance, pricing, and an end-to-end example.

## Endpoint and Session Configuration

- Primary WebSocket endpoint: wss://api.telnyx.com/v2/speech-to-text/transcription
- Direct WebSocket endpoint (no HTTP upgrade): wss://transcription.telnyx.com/public/speech-to-text/transcription
- Authenticate with Authorization: Bearer YOUR_API_KEY (HTTP header on the initial GET/upgrade)
- All configuration is set via query parameters at connect time and cannot change mid-session. Invalid parameters return a JSON error and the server closes the connection.
- Example URL: wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&input_format=wav&language=en-US&interim_results=true

## Connection Lifecycle and Flow

1) Handshake
- Client initiates an HTTP GET with Upgrade: websocket; server replies 101 Switching Protocols.
- You may also connect directly to the wss endpoint; the message protocol is identical.

2) Streaming
- Audio and transcripts flow concurrently (no request/response pairing).
- Client → Server frames:
  - Binary: raw audio bytes in small chunks (no base64 or JSON).
  - Text control messages:
    - {"type":"Finalize"} — flush buffer and force a final transcript (Deepgram only).
    - {"type":"CloseStream"} — flush any remaining transcription and end the stream gracefully (Deepgram, Speechmatics).
    - {"type":"KeepAlive"} — reset idle timeout during long silence (Deepgram only).
- Server → Client messages:
  - Transcription results with fields such as transcript, is_final, confidence; Deepgram may add speech_final and utterance_end markers.
  - Errors array; connection closes after an error.

3) Teardown
- Prefer a graceful close with {"type":"CloseStream"} (Deepgram, Speechmatics). The server sends remaining transcripts and then closes the socket.
- For other engines, close the WebSocket directly. Dropping the connection without CloseStream can lose buffered audio on Deepgram and Speechmatics.

## Audio Formats and Sample Rates

General rules
- Set the input_format query parameter. Audio is sent as binary WebSocket frames (chunked bytes).
- Container formats (e.g., mp3, wav, webm_opus) are self-describing; the server reads headers to detect encoding and sample rate.
- Raw encodings (e.g., linear16, mulaw, alaw, raw opus) carry no metadata — you must set sample_rate explicitly.
- If a sample rate is required but missing, you’ll receive an error (e.g., code 40003). Invalid or unsupported rates return errors (e.g., 40005).

Common capture scenarios
- Browser capture (MediaRecorder): input_format=webm_opus or ogg_opus; sample rate taken from headers (valid Opus rates typically 8–48 kHz).
- Telephony codecs: mulaw or alaw (commonly 8000 Hz), plus g729 (8000), amr_nb (8000), amr_wb (16000), speex (8/16/32 kHz; Google 16 kHz only).
- Raw PCM: linear16 (s16le), linear32 (f32le), raw opus frames; sample_rate is required (commonly 16000 for speech).
- Recorded files: mp3 (default for many engines), wav (uncompressed; default for Flux), flac (lossless).

Engine compatibility highlights
- Unsupported format/engine combinations return an error (40002). For Flux, unsupported formats return 40006.
- Universal formats across all engines/models: wav and linear16.
- Deepgram Flux is the most restrictive; compared to Nova it drops mp3, flac, webm_opus, amr_nb, amr_wb, g729, and speex.

## Engines and Models

Select via transcription_engine and model parameters.
- Deepgram: default model nova-3; also nova-2 and flux. Default engine with broadest format support.
- Telnyx: openai/whisper-tiny (on-network, lightweight).
- Google: latest_long (multilingual, long-form).
- Azure: azure/fast (broad language/accent coverage; region parameter required for Azure regions).
- xAI: xai/grok-stt (real-time transcription).
- AssemblyAI: assemblyai/universal-streaming (low-latency voice agents).
- Speechmatics: speechmatics/standard (high-accuracy real-time; supports multilingual and bilingual packs).

Flux model (Deepgram)
- Lowest-latency model with built-in end-of-turn detection for voice agents; see the End-of-Turn section for tuning.

## Parameters Reference

All parameters are query string values; they are locked once connected.
- transcription_engine (default Deepgram): Deepgram, Telnyx, Google, Azure, xAI, AssemblyAI
- model: per engine; see Engines and Models
- input_format (default mp3): see Audio Formats
- sample_rate (integer Hz; default 16000): required for raw encodings (linear16, mulaw, alaw, opus, etc.); ignored for container formats; invalid values return 40005
- language (default en-US): BCP-47 code or engine-specific behavior; see Language Selection
- interim_results ("true" | "false", default "false"): enable partial results on supported engines
- endpointing (Deepgram only; default 100 ms): integer ms or "false" to disable automatic utterance finalization
- redact (Deepgram only): comma-separated values (pci, ssn, numbers)
- keyterm (Deepgram Nova-3 and Flux): comma-separated boosted terms
- keywords (Deepgram Nova/Nova-2 legacy): keyword[:intensity] entries
- region (Azure only): Azure Speech Services region (e.g., eastus)
- eot_threshold (Flux only; default 0.7): confidence threshold 0.5–0.9 for EndOfTurn
- eot_timeout_ms (Flux only; default 5000): max silence 500–10000 ms before EndOfTurn
- eager_eot_threshold (Flux only; disabled by default): 0.3–0.9 threshold for speculative EagerEndOfTurn; must be ≤ eot_threshold

## Wire Protocol: Messages and Fields

Client → Server
- Audio data: binary frames containing raw audio bytes (no base64, no JSON). Recommended chunk size: 2048–8192 bytes.
- Control messages (JSON text frames with a type field):
  - Finalize — force a final transcript (Deepgram only)
  - CloseStream — gracefully end the session (Deepgram, Speechmatics)
  - KeepAlive — reset idle timeout (Deepgram only)
- Unknown text frames are ignored.

Server → Client
- Transcription result messages include:
  - transcript (string): transcribed text
  - is_final (boolean): true for finalized segments; false for interim (subject to change)
  - confidence (float 0.0–1.0): meaningful on final results; partials may report 0.0
  - speech_final (boolean, Deepgram): true if the speaker stopped
  - utterance_end (boolean, Deepgram): true for a silence-triggered boundary (empty transcript with is_final true)
- Error messages include an errors array with objects containing code, title, detail, and source.parameter. The server closes the connection shortly after sending an error.

## End-of-Turn Detection (Flux)

Flux uses confidence-based turn detection:
- eot_threshold: confidence required (higher = fewer false positives, slightly more latency)
- eot_timeout_ms: max silence before forcing EndOfTurn
- eager_eot_threshold: enables early speculative EagerEndOfTurn; if speech resumes, a TurnResumed event cancels it; lower values trigger earlier with more false starts

Event flow (without eager mode)
- Speech → silence → confidence ≥ eot_threshold → EndOfTurn
- Speech → silence → timeout (eot_timeout_ms) → EndOfTurn

Event flow (with eager mode)
- Speech → silence → confidence ≥ eager_eot_threshold → EagerEndOfTurn
  - If silence continues → confidence ≥ eot_threshold → EndOfTurn
  - If speech resumes → TurnResumed (cancel speculative work)

Profiles
- Default: eot_threshold=0.7, eot_timeout_ms=5000
- Low-latency: eager_eot_threshold=0.4, eot_threshold=0.7, eot_timeout_ms=6000
- High-reliability: eot_threshold=0.85, eot_timeout_ms=8000

## Interim Results

Support
- Deepgram and Speechmatics honor interim_results; other engines ignore it.

Behavior
- interim_results=false (default): only final messages; each has is_final true; lower message volume, higher per-result latency.
- interim_results=true: stream evolving partials (is_final false) followed by a final; partial confidence may be 0.0; only final results are stable.
