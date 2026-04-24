---
title: Language
summary: Language parameter behavior and engine differences.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/language
    content_hash: 33a03a8b1226c7f4e91e0ec77575295d4a437577ebe30838214ec2d7d8dfd421
updated_at: 2026-04-10T00:00:00Z
---

# Language

Language parameter behavior and engine differences.

BCP-47 language code. Default: `en-US`.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?language=es
```

## Auto-Detection

Pass `multi` to enable automatic language detection. The aliases `auto` and `auto_detect` are silently mapped to `multi`.

```
?language=multi
?language=auto        # → multi
?language=auto_detect # → multi
```

## Engine Support

| Engine   | Behavior                                                      |
| -------- | ------------------------------------------------------------- |
| Deepgram | BCP-47 codes. `multi` for multi-language mode.                |
| Telnyx   | Whisper-based. `auto_detect` disables language hint entirely. |
| Google   | BCP-47 codes.                                                 |
| Azure    | BCP-47 codes.                                                 |

## Supported Languages

Telnyx passes the language code directly to the engine — no validation or mapping. The supported set depends entirely on which engine you use.

| Engine   | Languages                                                                                         | Reference                                                                                                              |
| -------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Deepgram | 40+ languages. Nova-3 supports `multi` (10 languages in code-switching mode). Flux: English only. | [Deepgram languages](https://developers.deepgram.com/docs/models-languages-overview)                                   |
| Telnyx   | Whisper-based. 50+ languages. `auto_detect` to skip language hint.                                | —                                                                                                                      |
| Google   | 125+ languages/locales.                                                                           | [Google Cloud STT languages](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)          |
| Azure    | 100+ languages/locales.                                                                           | [Azure Speech languages](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=stt) |

## Common Codes

| Code            | Language                                |
| --------------- | --------------------------------------- |
| `en` or `en-US` | English (US)                            |
| `en-GB`         | English (UK)                            |
| `es`            | Spanish                                 |
| `fr`            | French                                  |
| `de`            | German                                  |
| `pt-BR`         | Portuguese (Brazil)                     |
| `ja`            | Japanese                                |
| `zh`            | Chinese (Mandarin)                      |
| `hi`            | Hindi                                   |
| `ar`            | Arabic                                  |
| `ko`            | Korean                                  |
| `multi`         | Multi-language / auto-detect (Deepgram) |
