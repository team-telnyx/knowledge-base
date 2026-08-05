---
title: Speech-to-Text
summary: 'Telnyx Speech-to-Text (STT) transcribes audio to text via three integration
  paths: WebSocket streaming for real-time partial and final transcripts, a REST API
  for synchronous file-based transcription, and in-call transcription for live voice
  calls. The platform supports multiple engines (Deepgram, Telnyx-hosted Whisper,
  Google, Azure, xAI, AssemblyAI, Speechmatics, Soniox, Parakeet, Reson8) selectable
  per request, with a single global endpoint and Bearer-token authentication.'
sources:
- url: https://developers.telnyx.com/docs/voice/stt/getting-started
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
- url: https://developers.telnyx.com/docs/voice/stt/migration
- url: https://developers.telnyx.com/docs/voice/stt/models
- url: https://developers.telnyx.com/docs/voice/stt/overview
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/index
updated_at: 2026-08-05T14:06:51Z
---

# Speech-to-Text

*Part 2 of 7 — see also: [Part 1](speech-to-text--part-1.md), [Part 3](speech-to-text--part-3.md), [Part 4](speech-to-text--part-4.md), [Part 5](speech-to-text--part-5.md), [Part 6](speech-to-text--part-6.md), [Part 7](speech-to-text--part-7.md)*

Telnyx Speech-to-Text (STT) transcribes audio to text via three integration paths: WebSocket streaming for real-time partial and final transcripts, a REST API for synchronous file-based transcription, and in-call transcription for live voice calls. The platform supports multiple engines (Deepgram, Telnyx-hosted Whisper, Google, Azure, xAI, AssemblyAI, Speechmatics, Soniox, Parakeet, Reson8) selectable per request, with a single global endpoint and Bearer-token authentication.

## Models and Engines

Telnyx STT supports multiple engines and models. Engine selection is specified as a parameter on the transcription command; the same engines are available across WebSocket streaming, REST, and in-call transcription.

| Engine | Model (WebSocket) | Model (REST) | Latency | Languages | Best for |
| --- | --- | --- | --- | --- | --- |
| **Deepgram** | `nova-3` | `deepgram/nova-3` | Low | 40+ ([reference](https://developers.deepgram.com/docs/models-languages-overview)) | **Recommended.** Highest English accuracy, diarization, word timestamps |
| **Deepgram** | `nova-2` | `deepgram/nova-2` | Low | 40+ | Legacy — use nova-3 unless you have a specific reason |
| **Deepgram** | `flux` | — | **Lowest** | English | Voice agents — built-in end-of-turn detection (WebSocket only) |
| **Deepgram** | `flux-multi` | — | **Lowest** | 10 languages | Multilingual voice agents — Flux with code-switching (WebSocket only) |
| **Telnyx** | `openai/whisper-large-v3-turbo` | `openai/whisper-large-v3-turbo` | Medium | 50+ ([reference](https://github.com/openai/whisper#available-models-and-languages)) | Multilingual transcription |
| **Telnyx** | `openai/whisper-tiny` | `openai/whisper-tiny` | Low | 50+ | Lightweight, on-network |
| **Google** | `latest_long` | — | Medium | 125+ ([reference](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)) | Long-form multilingual audio (WebSocket only) |
| **Azure** | `azure/fast` | — | Medium | 100+ ([reference](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=stt)) | Broad language and accent coverage (WebSocket only) |
| **xAI** | `xai/grok-stt` | — | Low | 25 languages | Grok STT for real-time transcription (WebSocket and Voice API only) |
| **AssemblyAI** | `assemblyai/universal-streaming` | — | Low | 18 languages | Universal-Streaming (backed by Universal-3.5 Pro Realtime) for voice agents with low latency and turn detection (WebSocket and Voice API only) |
| **Speechmatics** | `speechmatics/standard` | — | Low | 17+ languages | High-accuracy real-time transcription with bilingual and multilingual packs (WebSocket and Voice API only) |
| **Soniox** | `soniox/stt-rt-v4` | — | Low | Auto-detect | Real-time transcription with interim results and endpointing (WebSocket and Voice API only) |
| **Parakeet** | `nvidia/parakeet-v3` | — | — | Auto-detect | Self-hosted multilingual transcription, final transcripts only (WebSocket and Voice API only) |
| **Reson8** | `reson8/turns` | — | Low | 10 languages | Turn-based transcription with automatic language detection (WebSocket and Voice API only) |

### Engine Details

**Deepgram** is the default WebSocket engine. It offers the best English accuracy and the richest feature set. For REST, you must explicitly set `model="deepgram/nova-3"` — the REST default is `openai/whisper-large-v3-turbo`.

- **`nova-3`** — Latest and most accurate. Supports diarization, word-level timestamps, smart formatting, numerals, and punctuation via `model_config`. Use this unless you need the lowest possible latency.
- **`nova-2`** — Previous generation. Still supported but nova-3 is better in all benchmarks.
- **`flux`** — Purpose-built for voice agents. Lowest latency with built-in end-of-turn detection — tells you when the speaker has finished so your agent can respond. English only. WebSocket only.
- **`flux-multi`** — Multilingual Flux with code-switching. Same latency and end-of-turn detection as `flux`. WebSocket only.

Deepgram supports 40+ languages. Nova-3 supports `multi` mode (10 languages with code-switching). Flux-multi supports English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch, plus `auto`.

**Telnyx (Whisper)** runs Whisper models on-network.

- **`openai/whisper-large-v3-turbo`** — Multilingual (50+ languages, auto-detected). Returns text only — no timestamps regardless of response format.
- **`openai/whisper-tiny`** — Lightweight, lowest resource usage.

Use `auto_detect` to skip the language hint. Limitations: no diarization, no word-level timestamps.

**Google** Cloud Speech-to-Text integration. Model: `latest_long`. 125+ languages/locales.

**Azure** Speech Services integration. Model: `azure/fast`. 100+ languages/locales with strong accent and dialect coverage.

**xAI** Grok STT integration for real-time transcription. Model: `xai/grok-stt`. 25 languages, including Arabic, English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish, and Vietnamese.

**AssemblyAI** Universal-Streaming integration for real-time voice agent transcription, backed by AssemblyAI's [Universal-3.5 Pro Realtime](https://www.assemblyai.com/topic/universal-3-5-pro-realtime) model. Model: `assemblyai/universal-streaming`. 18 languages with native code-switching.

**Speechmatics** real-time transcription integration with high accuracy and multilingual support including bilingual packs. Model: `speechmatics/standard`. Supports interim results (partial transcripts) and graceful `CloseStream` shutdown.

**Soniox** real-time transcription integration with automatic language detection. Model: `soniox/stt-rt-v4`. Supports interim results, endpointing, and graceful `CloseStream` shutdown.

**Parakeet** is a self-hosted NVIDIA Parakeet integration for multilingual transcription with automatic language detection. Model: `nvidia/parakeet-v3`. Final transcripts only — no interim/partial results. Ignores endpointing. Accepts `linear16`/`linear32` (16 kHz) audio only.

**Reson8** turn-based transcription. Transcripts are delivered per turn of speech: interim frames carry the full transcript of the turn so far and supersede each other, and the final transcript for a turn arrives when the turn ends. Model: `reson8/turns`. Languages: Dutch, English, French, Frisian, German, Italian, Polish, Portuguese, Spanish, and Swedish. `auto` enables automatic language detection. Turn-based results — interim frames are cumulative (each carries the full turn transcript and supersedes the previous frame; there are no incremental word-by-word partials), and no `confidence` score on transcript frames. Ignores endpointing. Accepts `linear16`/`linear32`/`mulaw`/`alaw` audio at any sample rate.

### How to Choose

- **Need the highest accuracy for English?** → Deepgram `nova-3` — best WER (word error rate) across all English variants.
- **Building a voice agent that needs to know when the user stopped talking?** → Deepgram `flux` — lowest latency with built-in end-of-turn detection. Use `flux-multi` for multilingual agents.
- **Need to transcribe files in 50+ languages?** → Telnyx `openai/whisper-large-v3-turbo` via REST API.
- **Need diarization (who said what)?** → Deepgram `nova-3` with `model_config.diarize: true`.
- **Need broad accent/dialect support?** → Azure `azure/fast` — strong coverage across regional accents.
- **Need Grok STT for real-time calls?** → xAI `xai/grok-stt` via WebSocket or Voice API.
- **Need low-latency streaming for voice agents?** → AssemblyAI `assemblyai/universal-streaming` (backed by Universal-3.5 Pro Realtime) via WebSocket or Voice API.
- **Need high-accuracy multilingual with bilingual packs?** → Speechmatics `speechmatics/standard` via WebSocket or Voice API.
- **Need real-time transcription with automatic language detection?** → Soniox `soniox/stt-rt-v4` via WebSocket or Voice API.
- **Need self-hosted multilingual transcription with automatic language detection?** → Parakeet `nvidia/parakeet-v3` via WebSocket or Voice API.
- **Need turn-based transcription of European languages for voice agents?** → Reson8 `reson8/turns` via WebSocket or Voice API.

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
