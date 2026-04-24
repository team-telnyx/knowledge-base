---
title: Telnyx
summary: Telnyx native TTS — 5 models across latency, quality, and language coverage.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/index
    content_hash: 653c2a57bfede0ae9787e89eee4edffb70bdc2ee0c9e1fa3f5a1a6623db9fa1b
updated_at: 2026-04-10T00:00:00Z
---

# Telnyx

Telnyx native TTS — 5 models across latency, quality, and language coverage.

## Selecting Telnyx

Telnyx is the **default provider**. If you don't specify a provider, you get Telnyx.

**WebSocket:**

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra
```

**REST:**

```bash theme={null}
curl --request POST \
  --url https://api.telnyx.com/v2/text-to-speech \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "text": "Hello.",
  "voice": "Telnyx.NaturalHD.astra"
}'
```

***

## Models

| Model                                                   | Latency | Quality | Languages    | Voice Source              | WebSocket | REST |
| ------------------------------------------------------- | ------- | ------- | ------------ | ------------------------- | --------- | ---- |
| [Natural](natural.md)     | Low     | Good    | English      | Pre-built (Rime Mist)     | Yes       | Yes  |
| [NaturalHD](naturalhd.md) | Low     | Better  | 9 languages  | Pre-built (Rime Arcana)   | Yes       | Yes  |
| [KokoroTTS](kokorotts.md)    | Lowest  | Good    | 5 languages  | Pre-built                 | Yes       | Yes  |
| [Qwen3TTS](qwen3tts.md)      | Medium  | High    | 11 languages | Cloned (Voice Design Lab) | Yes       | Yes  |
| [Ultra](ultra.md)         | Lowest  | Highest | 44 languages | Pre-built                 | **No**    | Yes  |

> **Warning:** **Ultra** is REST-only — not available over public WebSocket.

***

Browse all available voices via the [Voices API](https://developers.telnyx.com/api-reference/text-to-speech/list-voices) or the [Voice Design Lab](https://portal.telnyx.com/#/app/ai/voice-design-lab).


## Related Pages

- [Telnyx CLI](../reference/telnyx-cli.md)
