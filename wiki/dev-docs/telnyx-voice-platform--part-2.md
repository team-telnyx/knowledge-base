---
title: Telnyx Voice Platform
summary: 'Covers two major Telnyx Voice capabilities: STIR/SHAKEN call authentication
  (attestation levels, certificate hosting, SIP header verification) and Speech-to-Text
  transcription (WebSocket streaming, REST file upload, in-call transcription, multi-engine
  model selection, and provider migration).'
sources:
- url: https://developers.telnyx.com/docs/voice/stir-shaken/attestation-behavior/index
  content_hash: e71721006805ece97317b6a2ce287bded0ee694d74cd96070f8efb6ec4546534
- url: https://developers.telnyx.com/docs/voice/stir-shaken/hosted-cert
  content_hash: 8a1cedc407a7eeed8a1f689a60c15c545dc6394a4ce0d4d664a31846b54b856b
- url: https://developers.telnyx.com/docs/voice/stir-shaken/sip-header-parameters
  content_hash: ddcbe69b5d283081160304794571d8ad56e52cca94e1f55ac224d31fe3f9ac5f
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
  content_hash: a17bf544d2f5411cb7a1e10bd8204fae4fb499a8debccef66cb9d596da2c280c
- url: https://developers.telnyx.com/docs/voice/stt/migration
  content_hash: 8273de02389d2c31f810a359f89523eeb2a64aa43286be196c610a805e479cdc
- url: https://developers.telnyx.com/docs/voice/stt/models
  content_hash: 637078dde1176884102bdc0e61dcc482b32bdee3552c24cbf5158b865a6a1426
- url: https://developers.telnyx.com/docs/voice/stt/overview/index
  content_hash: 3cd2887c1a24d01ca417a1e3a2f2e7e7db6cd92449fb5a77027b8cadb348015f
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
  content_hash: 277f6f5e42acfabb557c1b22f1293ce8235db0e343e8af493560f9071b12fa36
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
  content_hash: c75d57b2ceae2c7f6f780f4385e6a545f6dcc11d41a7cca25441d1add888572f
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
  content_hash: 3856e7e0bf451af19678e8ba5f19deb2fffe5ebab69aa15c93f0ee331521f964
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
  content_hash: afd719ffe51051e3855f74439d0eba8bde4e617f527163f25e99321d501562d6
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
  content_hash: 262aa6764992fbe5d612843b7bfe1044f0ddfb4a118cb7cb7038d64fb2ae28aa
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
  content_hash: 56bd4f643fc6734d46569c545513342da1a4a2e611b863a525edb13ea879d8dc
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
  content_hash: d6959b095ff36f9266a76bb3ba3f39c0cd75fd2f49e2b4bb7e1d3a7b480f23d6
updated_at: 2026-06-11T10:47:02Z
---

# Telnyx Voice Platform

*Part 2 of 4 — see also: [Part 1](telnyx-voice-platform--part-1.md), [Part 3](telnyx-voice-platform--part-3.md), [Part 4](telnyx-voice-platform--part-4.md)*

Covers two major Telnyx Voice capabilities: STIR/SHAKEN call authentication (attestation levels, certificate hosting, SIP header verification) and Speech-to-Text transcription (WebSocket streaming, REST file upload, in-call transcription, multi-engine model selection, and provider migration).

## STT Models and Engines

### Comparison

| Engine | Model (WebSocket) | Model (REST) | Latency | Languages | Best For |
|---|---|---|---|---|---|
| Deepgram | `nova-3` | `deepgram/nova-3` | Low | 40+ | **Recommended.** Highest English accuracy, diarization, word timestamps |
| Deepgram | `nova-2` | `deepgram/nova-2` | Low | 40+ | Legacy — use nova-3 unless you have a specific reason |
| Deepgram | `flux` | — | Lowest | 10 | Voice agents — built-in end-of-turn detection (WebSocket only) |
| Telnyx | `openai/whisper-large-v3-turbo` | `openai/whisper-large-v3-turbo` | Medium | 50+ | Multilingual transcription |
| Telnyx | `openai/whisper-tiny` | `openai/whisper-tiny` | Low | 50+ | Lightweight, on-network |
| Google | `latest_long` | — | Medium | 125+ | Long-form multilingual audio (WebSocket only) |
| Azure | `azure/fast` | — | Medium | 100+ | Broad language and accent coverage (WebSocket only) |
| xAI | `xai/grok-stt` | — | Low | 25 | Grok STT for real-time transcription (WebSocket and Voice API only) |
| AssemblyAI | `assemblyai/universal-streaming` | — | Low | 6 | Universal-Streaming for voice agents with low latency and turn detection (WebSocket and Voice API only) |
| Speechmatics | `speechmatics/standard` | — | Low | 17+ | High-accuracy real-time with bilingual/multilingual packs (WebSocket and Voice API only) |
| Soniox | `soniox/stt-rt-v4` | — | Low | Auto-detect | Real-time with automatic language detection (WebSocket and Voice API only) |

### Engine Details

**Deepgram** — The default WebSocket engine. Best English accuracy and richest feature set. For REST, you must explicitly set `model="deepgram/nova-3"`; the REST default is `openai/whisper-large-v3-turbo`.

- `nova-3` — Latest and most accurate. Supports diarization, word-level timestamps, smart formatting, numerals, and punctuation via `model_config`. Supports `multi` mode (10 languages with code-switching).
- `nova-2` — Previous generation. Still supported but nova-3 outperforms in all benchmarks.
- `flux` — Purpose-built for voice agents. Lowest latency with built-in end-of-turn detection. WebSocket only. Supports English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch.

**Telnyx (Whisper)** — Runs Whisper models on-network.

- `openai/whisper-large-v3-turbo` — Multilingual (50+ languages, auto-detected). Returns text only — no timestamps regardless of response format.
- `openai/whisper-tiny` — Lightweight, lowest resource usage. Returns text only.

Limitations: no diarization, no word-level timestamps.

**Google** — Model `latest_long`. 125+ languages/locales. Long-form multilingual audio. WebSocket only.

**Azure** — Model `azure/fast`. 100+ languages/locales with strong accent and dialect coverage. WebSocket only.

**xAI** — Model `xai/grok-stt`. 25 languages including Arabic, English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish, Vietnamese. WebSocket and Voice API only.

**AssemblyAI** — Model `assemblyai/universal-streaming`. 6 languages (English, Spanish, German, French, Portuguese, Italian). WebSocket and Voice API only.

**Speechmatics** — Model `speechmatics/standard`. 17+ languages including bilingual/multilingual packs (Arabic–English, Mandarin–English, English–Malay, English–Tamil, Tagalog, Spanish–English, etc.). Also supports Basque, Galician, Irish, Maltese, Mongolian, Swahili, Uyghur, Welsh. Supports interim results and graceful `CloseStream` shutdown. WebSocket and Voice API only.

**Soniox** — Model `soniox/stt-rt-v4`. Automatic language detection — no language hint required. Supports interim results, endpointing, and graceful `CloseStream` shutdown. WebSocket and Voice API only.

### How to Choose

- **Highest accuracy for English** → Deepgram `nova-3`
- **Voice agent that needs end-of-turn detection** → Deepgram `flux`
- **File transcription in 50+ languages** → `openai/whisper-large-v3-turbo` via REST
- **Diarization (who said what)** → Deepgram `nova-3` with `model_config.diarize: true`
- **Broad accent/dialect support** → Azure `azure/fast`
- **Grok STT for real-time calls** → xAI `xai/grok-stt`
- **Low-latency streaming for voice agents** → AssemblyAI `assemblyai/universal-streaming`
- **High-accuracy multilingual with bilingual packs** → Speechmatics `speechmatics/standard`
- **Automatic language detection** → Soniox `soniox/stt-rt-v4`

### Specifying the Engine and Model

**WebSocket** — set via query parameters:

```
wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3
```

**REST API** — set via the `model` body parameter:

```
curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
  -H "Authorization: Bearer YOUR_TELNYX_API_KEY" \
  -F model="deepgram/nova-3" \
  -F file=@audio.mp3
```
