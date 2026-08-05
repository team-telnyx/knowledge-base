---
title: Speech-to-Text WebSocket Streaming
summary: The Telnyx Speech-to-Text WebSocket streaming endpoint accepts real-time
  audio over a single WebSocket connection and returns transcription results as JSON
  text frames. All session configuration is passed as query parameters on the connection
  URL and locked at connect time; audio is sent as binary frames and control messages
  as JSON. The endpoint supports multiple transcription engines and models, a wide
  range of audio formats, language selection, interim results, endpointing, keyword
  boosting, redaction, and Deepgram Flux end-of-turn detection, with production guidance
  for connection recovery, buffering, keepalive, and graceful shutdown.
sources:
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/end-of-turn
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/endpointing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/engines-and-models
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/interim-results
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/keyword-boosting
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/language
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/redaction
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/pricing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/production-patterns
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/responses
updated_at: 2026-08-05T14:06:24Z
---

# Speech-to-Text WebSocket Streaming

*Part 2 of 4 — see also: [Part 1](speech-to-text-websocket-streaming--part-1.md), [Part 3](speech-to-text-websocket-streaming--part-3.md), [Part 4](speech-to-text-websocket-streaming--part-4.md)*

The Telnyx Speech-to-Text WebSocket streaming endpoint accepts real-time audio over a single WebSocket connection and returns transcription results as JSON text frames. All session configuration is passed as query parameters on the connection URL and locked at connect time; audio is sent as binary frames and control messages as JSON. The endpoint supports multiple transcription engines and models, a wide range of audio formats, language selection, interim results, endpointing, keyword boosting, redaction, and Deepgram Flux end-of-turn detection, with production guidance for connection recovery, buffering, keepalive, and graceful shutdown.

## Language

The `language` parameter accepts a BCP-47 language code. Default: `en-US`.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?language=es
```

Pass `multi` to enable automatic language detection. The aliases `auto` and `auto_detect` are silently mapped to `multi`.

```
?language=multi
?language=auto        # → multi
?language=auto_detect # → multi
```

### Engine Support

| Engine | Behavior |
| --- | --- |
| Deepgram | BCP-47 codes. `multi` for multi-language mode. |
| Telnyx | Whisper-based. `auto_detect` disables language hint entirely. |
| Google | BCP-47 codes. |
| Azure | BCP-47 codes. |
| xAI | Language codes such as `en`, `fr`, `de`, and `ja`. |
| AssemblyAI | Automatic multilingual detection and code switching across supported languages. |
| Speechmatics | Language codes such as `en`, `es`. Bilingual packs use Telnyx shorthand (e.g. `ar_en`) — mapped internally. Does not support `auto`; defaults to `en` if unrecognized. |
| Soniox | Automatic language detection. The `language` parameter is ignored — Soniox detects the language from the audio stream. |
| Parakeet | Automatic multilingual detection. The `language` parameter is ignored — Parakeet always auto-detects. |
| Reson8 | Supports 10 languages; can also accept `auto` (the default when omitted) for automatic language detection at the cost of transcription speed. |

### Supported Languages

For most engines, Telnyx passes the language code directly without validation. The supported set depends on which engine you use. Speechmatics is the exception — Telnyx accepts shorthand codes for bilingual/multilingual packs and maps them to the provider's `language` + `domain` configuration internally.

| Engine | Languages | Reference |
| --- | --- | --- |
| Deepgram | 40+ languages across Deepgram models. Nova-3 supports `multi` (10 languages in code-switching mode). Flux is English-only; Flux-multi supports English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch, plus `auto`. | [Deepgram languages](https://developers.deepgram.com/docs/models-languages-overview) |
| Telnyx | Whisper-based. 50+ languages. `auto_detect` to skip language hint. | — |
| Google | 125+ languages/locales. | [Google Cloud STT languages](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages) |
| Azure | 100+ languages/locales. | [Azure Speech languages](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=stt) |
| xAI | 25 languages, including Arabic, English, French, German, Hindi, Japanese, Korean, Portuguese, Spanish, and Vietnamese. | [xAI Voice API](https://docs.x.ai/developers/rest-api-reference/inference/voice) |
| AssemblyAI | 18 languages with native multilingual code switching: English, Spanish, German, French, Portuguese, Italian, Turkish, Dutch, Swedish, Norwegian, Danish, Finnish, Hindi, Vietnamese, Arabic, Hebrew, Japanese, and Mandarin (backed by Universal-3.5 Pro Realtime). | [AssemblyAI supported languages](https://www.assemblyai.com/docs/faq/language-support-for-real-time-transcription) |
| Speechmatics | 17+ languages. Standard codes (`en`, `es`, `cy`, `sw`, etc.) plus Telnyx shorthand for bilingual/multilingual packs (`ar_en`, `cmn_en`, `en_ms`, `en_ta`, `cmn_en_ms_ta`). Telnyx maps these internally to Speechmatics `language` + `domain` params — do not pass them raw to the provider. | [Speechmatics languages](https://docs.speechmatics.com/introduction/supported-languages) |
| Soniox | Automatic language detection — no language hint required. The `language` parameter is ignored. | [Soniox docs](https://soniox.com/docs) |
| Parakeet | Automatic multilingual detection — no language hint required. The `language` parameter is ignored. | — |
| Reson8 | 10 languages: `nl`, `en`, `fr`, `fy`, `de`, `it`, `pl`, `pt`, `es`, `sv`. Can also accept `auto` for automatic detection at the cost of transcription speed. | — |

### Common Codes

| Code | Language |
| --- | --- |
| `en` or `en-US` | English (US) |
| `en-GB` | English (UK) |
| `es` | Spanish |
| `fr` | French |
| `de` | German |
| `pt-BR` | Portuguese (Brazil) |
| `it` | Italian |
| `ja` | Japanese |
| `zh` | Chinese (Mandarin) |
| `hi` | Hindi |
| `ar` | Arabic |
| `ko` | Korean |
| `multi` | Multi-language / auto-detect (Deepgram) |

## Interim Results

Supported by Deepgram, Speechmatics, and Soniox. Other engines ignore this parameter. Controls whether the server sends partial (non-final) transcripts as speech is processed.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?interim_results=true
```

Default: `false`. Pass `"true"` as a string.

With `interim_results=false` (default), the server sends only final transcripts. Each message has `is_final: true`. Lower message volume, higher latency per result.

```
{"transcript": "Hello, how are you?", "is_final": true, "confidence": 0.98}
```

With `interim_results=true`, the server sends evolving partial transcripts as audio is processed, followed by a final. Partials have `is_final: false` and are replaced by the next message.

```
{"transcript": "Hello", "is_final": false, "confidence": 0.0}
{"transcript": "Hello, how", "is_final": false, "confidence": 0.0}
{"transcript": "Hello, how are you?", "is_final": true, "confidence": 0.98}
```

Partial transcripts have `confidence: 0.0` — confidence is only meaningful on final results.

## Endpointing

Supported by Deepgram, xAI, Google, Speechmatics, and Soniox. Other engines ignore this parameter. Controls how long the engine waits after silence before finalizing an utterance.

Soniox has a different valid range. When `transcription_engine=Soniox`, this parameter maps to `max_endpoint_delay_ms` and must be between **500 and 3000 ms**. Values outside that range are rejected. The default (100 ms) and the low-value examples below apply to Deepgram, xAI, Google, and Speechmatics only.

```
# Deepgram / xAI / Google / Speechmatics
wss://api.telnyx.com/v2/speech-to-text/transcription?endpointing=300

# Soniox (500–3000 ms)
wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Soniox&endpointing=1000
```

Default: `100` ms (not applicable to Soniox — Soniox endpointing is disabled unless a value in the 500–3000 ms range is provided).

| Value | Behavior |
| --- | --- |
| Integer (ms) | Finalize after this many ms of silence. Lower = faster but more splits. |
| `"false"` | Disable endpointing entirely. No automatic utterance boundaries. |

**Low values (50–100 ms)** — Fast response. Utterances may split mid-sentence on short pauses. *(Deepgram, xAI, Google, Speechmatics only — below Soniox minimum.)*

**High values (300–1000 ms)** — More complete sentences. Higher latency before finalization.

**Soniox range (500–3000 ms)** — Minimum 500 ms. Use 500–800 ms for responsive turn detection, 1000–3000 ms for longer utterances with natural pauses.

**Disabled (`"false"`)** — No automatic splits. Use `Finalize` control messages to manually trigger boundaries, or rely on `CloseStream` for a single final transcript.

When endpointing triggers, Deepgram sends the final transcript followed by an utterance end event (if `utterance_end_ms` is configured server-side — currently 1000 ms):

```
{"transcript": "Hello, how are you?", "is_final": true}
{"transcript": "", "is_final": true, "utterance_end": true}
```

The utterance end marker signals "this speaker turn is done."
