---
title: Telnyx Speech-to-Text (STT)
summary: Telnyx STT converts audio to text via real-time WebSocket streaming, file-based
  REST transcription, and in-call transcription. It supports multiple engines (Deepgram,
  Whisper, Google, Azure, xAI, AssemblyAI, Speechmatics), is OpenAI SDK compatible
  for REST, and makes migrations from other providers straightforward.
sources:
- url: https://developers.telnyx.com/docs/voice/stt/overview/index
  content_hash: 70e59d39740d3a725c30bac4ed53fde656003acdc2980789bea34268c89bf169
- url: https://developers.telnyx.com/docs/voice/stt/getting-started
  content_hash: aab423d90e8142cd0d36339e8f44195c90fbfa0c3343f1541bc41a4984c11ea4
- url: https://developers.telnyx.com/docs/voice/stt/migration
  content_hash: ff5b9c5386452a8199ce8a36019560d0631211500ee1a4d034fb238d29957f38
- url: https://developers.telnyx.com/docs/voice/stt/models
  content_hash: 1a8e70d1f994345fcd55e088029447f0ea655c7716a1a16788f7e84458c71317
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
  content_hash: 8c62c138c18b9d124f4d7795c5cb924f66e8e99ff74534ed5c9a14f33fb9ec78
updated_at: 2026-05-20T09:52:13Z
---

# Telnyx Speech-to-Text (STT)

*Part 1 of 2 — see also: [Part 2](telnyx-speech-to-text-stt--part-2.md)*

Telnyx STT converts audio to text via real-time WebSocket streaming, file-based REST transcription, and in-call transcription. It supports multiple engines (Deepgram, Whisper, Google, Azure, xAI, AssemblyAI, Speechmatics), is OpenAI SDK compatible for REST, and makes migrations from other providers straightforward.

## What Telnyx STT offers
- WebSocket Streaming: send audio over a persistent WebSocket and receive low-latency partial and final transcripts.
- File-Based Transcription (REST): upload a file or provide a URL and get a complete transcript; OpenAI SDK compatible.
- In-Call Transcription: enable live-call STT via the Voice API or TeXML with engine selection per call.

## Quickstart and prerequisites
- Requirements: a Telnyx account and an API key.
- Get started quickly in Python or Node.js with end-to-end examples for both WebSocket and REST in [Speech-to-Text quickstart](speech-to-text-quickstart.md).

## WebSocket streaming overview
- Connect to a single global endpoint and stream binary audio frames; receive JSON messages with fields like `transcript` and `is_final` (partial vs final).
- URL pattern (example):
  wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&input_format=linear16&sample_rate=16000&language=en-US&interim_results=true
- Key query parameters:
  - transcription_engine (e.g., Deepgram, Google, Azure, xAI, AssemblyAI, Speechmatics)
  - model (e.g., nova-3, flux, azure/fast, latest_long)
  - input_format and sample_rate (e.g., linear16 at 16000 Hz), language, interim_results
- Advanced features are configured via parameters (e.g., keyword boosting, redaction, endpointing/turn detection). See [WebSocket Parameters](websocket-parameters.md).
- For flow and message patterns, see [Speech-to-Text WebSocket lifecycle](speech-to-text-websocket-lifecycle.md).

## File-based transcription (REST)
- Endpoint: https://api.telnyx.com/v2/ai/audio/transcriptions (multipart/form-data).
- Use either a file upload or a file_url; returns a simple {"text": "..."} payload by default.
- OpenAI SDK compatible: switch base_url to https://api.telnyx.com/v2 and use your Telnyx API key; existing client.audio.transcriptions.create(...) code works.
- Timestamps and diarization: use model="deepgram/nova-3" and response_format=verbose_json with model_config (e.g., diarize, smart_format). Whisper models (openai/whisper-large-v3-turbo, openai/whisper-tiny) return text only.
- Example (cURL):
  curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
    -H "Authorization: Bearer YOUR_TELNYX_API_KEY" \
    -F model="openai/whisper-large-v3-turbo" \
    -F file=@audio.mp3
  
  Or provide a URL:
  curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
    -H "Authorization: Bearer YOUR_TELNYX_API_KEY" \
    -F model="openai/whisper-large-v3-turbo" \
    -F file_url="https://example.com/audio.mp3"

## In-call transcription
- Add real-time transcription to live calls; Telnyx handles codecs and media formats.
- Integrations:
  - Voice API: send transcription_start/transcription_stop on active calls.
  - TeXML: include transcription directives in XML call flows.
- Choose engines per call (same set as WebSocket). See [In-Call Transcription](in-call-transcription.md).

## Engines and models
- Deepgram (default for WebSocket):
  - nova-3: best English accuracy; supports diarization, word timestamps, smart formatting via model_config; 40+ languages (see Deepgram languages reference: https://developers.deepgram.com/docs/models-languages-overview)
  - nova-2: previous gen; use nova-3 unless you have a specific need
  - flux: ultra-low latency with built-in end-of-turn detection (WebSocket only; English)
- Telnyx Whisper (runs on-network):
  - openai/whisper-large-v3-turbo (REST default): multilingual (50+; https://github.com/openai/whisper#available-models-and-languages); returns text only
  - openai/whisper-tiny: lightweight option; text only
- Google: latest_long (WebSocket only), 125+ languages (https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)
- Azure: azure/fast (WebSocket only), ~100+ languages (https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=stt)
- xAI: xai/grok-stt for real-time (WebSocket and Voice API)
- AssemblyAI: assemblyai/universal-streaming for voice agents with low latency and turn detection (WebSocket and Voice API)
- Speechmatics: speechmatics/standard for high-accuracy multilingual and bilingual packs (WebSocket and Voice API); supports interim results and graceful CloseStream

How to specify the engine and model:
- WebSocket: via query string, e.g. wss://.../transcription?transcription_engine=Deepgram&model=nova-3
- REST: via the model field, e.g. -F model="deepgram/nova-3"

See details and comparisons in [Models & Engines](models-engines.md).

## Migration from other providers
- Deepgram → Telnyx (WebSocket/REST):
  - Auth: Token → Authorization: Bearer
  - WebSocket adds transcription_engine=Deepgram; model names carry over (nova-2, nova-3, flux)
  - Wire protocol: same (binary audio in, JSON transcripts out)
  - Field mapping: Deepgram transcript fields map to transcript; is_final/speech_final → is_final
- ElevenLabs → Telnyx:
  - WebSocket: xi-api-key → Authorization: Bearer; model_id maps to transcription_engine+model; language_code → language; keywords → keyterm (for nova-3/flux)
  - REST: file field audio → file; model_id → model; response shape remains {"text": "..."}
- OpenAI Whisper (REST) → Telnyx:
  - Just change api_key and base_url; method and response stay the same
  - Note: Whisper at Telnyx returns text only; for segments/timestamps use deepgram/nova-3 with verbose_json
- Google Cloud → Telnyx (WebSocket):
  - Drop protobuf/gRPC and service accounts; switch to WebSocket with JSON
  - language_code → language; encoding → input_format; sample_rate_hertz → sample_rate; interim_results → interim_results
  - results[0].alternatives[0].transcript → transcript; results[0].is_final → is_final
- AWS Transcribe → Telnyx (WebSocket):
  - Replace HTTP/2 event stream and SigV4 with plain WebSocket and Bearer auth
  - language_code → language; media_encoding → input_format; media_sample_rate_hz → sample_rate; enable_partial_results_stabilization → interim_results; vocabulary_name → keyterm
  - transcript.results[].alternatives[].transcript → transcript; is_partial inversely maps to is_final
- Azure Speech → Telnyx (WebSocket/REST):
  - WebSocket: remove SDK/region; speech_recognition_language → language; recognizing → is_final:false; recognized → is_final:true
  - REST: region-specific URL and Ocp-Apim-Subscription-Key become global endpoint + Authorization: Bearer; body becomes multipart/form-data; response text maps to text

For side-by-side examples, see [Migrate to Telnyx STT](migrate-to-telnyx-stt.md).

## Choosing the right model
- Highest English accuracy and rich features (timestamps, diarization): Deepgram nova-3
- Lowest latency and built-in end-of-turn detection for voice agents: Deepgram flux (WebSocket)
- Multilingual file transcription (50+ languages) with simple integration: Whisper large-v3-turbo (REST)
- Broad accent/dialect coverage: Azure azure/fast (WebSocket)
- Real-time Grok STT: xai/grok-stt (WebSocket/Voice API)
- Low-latency streaming for voice agents: assemblyai/universal-streaming (WebSocket/Voice API)
- High-accuracy multilingual with bilingual packs: speechmatics/standard (WebSocket/Voice API)

## Capabilities and limitations
- Partial vs final results: enable interim_results to receive low-latency partial transcripts; final results have is_final:true
- Timestamps and diarization: available with Deepgram nova-3 (via model_config and verbose_json in REST); Whisper models return text only (no segments/timestamps/diarization)
- End-of-turn detection: built into Deepgram flux (WebSocket)
- Language coverage: varies by engine (Deepgram 40+, Whisper 50+, Google 125+, Azure 100+; see external language lists linked above)
- Defaults: WebSocket commonly uses Deepgram; REST defaults to openai/whisper-large-v3-turbo unless you set model explicitly
