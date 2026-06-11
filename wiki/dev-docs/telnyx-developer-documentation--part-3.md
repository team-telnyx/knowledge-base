---
title: Telnyx Developer Documentation
summary: A comprehensive guide to Telnyx's Programmable Fax, Reporting & Analytics,
  and Speech & Voice APIs, covering setup, sending and receiving faxes, webhook handling,
  usage reporting, session analysis, and real-time speech-to-text and text-to-speech
  streaming.
sources:
- url: https://developers.telnyx.com/docs/programmable-fax/email-to-fax
  content_hash: ae956e35cbe778faa550865d178aa512a687347422967b41e7a73b0c9364af92
- url: https://developers.telnyx.com/docs/programmable-fax/get-started/index
  content_hash: a575ae8f265f3ea2e617b542b7d6487bd8d9e4fcdd3734795432d746dbe75d8e
- url: https://developers.telnyx.com/docs/programmable-fax/quickstart
  content_hash: 162c427173df6aab8cad1d63cf53c10a31f6363d5d1fbebeacca092f99fc7373
- url: https://developers.telnyx.com/docs/programmable-fax/receive-a-fax-api
  content_hash: 1d8b685093cd16efa0df2c2b2e385296e0f3d36e3b4882cb3fcdf6ff32f1e650
- url: https://developers.telnyx.com/docs/programmable-fax/receiving-webhooks
  content_hash: b65b3f5a519156817aea525848b57f52f9bd40558645bc87356a2db202636f5d
- url: https://developers.telnyx.com/docs/programmable-fax/send-a-fax-api
  content_hash: 702c037dc0af510343f0f7d960dbfe368fd785fcd4614ce295bdbead03eb7ffa
- url: https://developers.telnyx.com/docs/programmable-fax/sending-commands
  content_hash: 8d55fb8cfe9dbe0694a68e6c21128c0e3663ee3e7309b8ce11dbd8a3a826a0f0
- url: https://developers.telnyx.com/docs/reporting/on-demand-reports/index
  content_hash: be2475e7633ad6e93e0105757b0ba6bcbeb2aecd6ab7127b68b72e7c712e033c
- url: https://developers.telnyx.com/docs/reporting/session-analysis
  content_hash: 9b537f31fe03cdc4d041a4cefb01f6e0303673dce26f78e980f1db54968ecbc3
- url: https://developers.telnyx.com/docs/reporting/usage-reports/index
  content_hash: 619f12548c152b55f58f96ad18d8e5acb022679092f6c18fdafce89186634ec5
- url: https://developers.telnyx.com/docs/tts-stt/stt-websocket-streaming
  content_hash: 851082b5bb21f1fe0454bd5c236783faacdf44d9c11ef0acf1480ca44031b23d
- url: https://developers.telnyx.com/docs/tts-stt/telnyx-ultra-voices
  content_hash: fc89baa71369839911ad9530a0315313e420d08b9a7e755a10b769c9f3476f83
- url: https://developers.telnyx.com/docs/tts-stt/tts-available-voices
  content_hash: 1380d4c10aa72181d69b6705a81bac26fa1fc424afec460b7874613db55feeff
- url: https://developers.telnyx.com/docs/tts-stt/tts-websocket-streaming
  content_hash: a3493cabf711a0cf0d546df8a0b3c75ecee91a0755f3869d522a1e0e217c6586
updated_at: 2026-06-11T10:41:11Z
---

# Telnyx Developer Documentation

*Part 3 of 3 — see also: [Part 1](telnyx-developer-documentation--part-1.md), [Part 2](telnyx-developer-documentation--part-2.md)*

A comprehensive guide to Telnyx's Programmable Fax, Reporting & Analytics, and Speech & Voice APIs, covering setup, sending and receiving faxes, webhook handling, usage reporting, session analysis, and real-time speech-to-text and text-to-speech streaming.

## Speech and Voice

### Available Text-to-Speech Voices

Telnyx provides access to voices from multiple providers through a single API:

- **Telnyx voices**: Natural, NaturalHD, and [Ultra](https://developers.telnyx.com/docs/tts-stt/telnyx-ultra-voices) tiers
- **Third-party providers**: xAI Grok, AWS Polly, Azure, ElevenLabs, Inworld, MiniMax, ResembleAI, Rime

You can also create custom voices using the Voice Design Lab. Browse and filter voices by provider, model, and language on the Available Voices page.

### Telnyx Ultra Voices

Telnyx Ultra is a premium TTS model with sub-100ms time to first byte, support for 36 languages, and expressive mode for AI assistants.

| Feature | Natural / NaturalHD | Ultra |
|---|---|---|
| Time to first byte | ~200–300ms | **< 100ms** |
| Expressive mode | — | Automatic emotional interpretation with SSML emotion tags |
| Nonverbal cues | — | `[laughter]` and other natural vocalizations |
| Languages | Varies by voice | 36 languages |

Ultra voices use the format `Telnyx.Ultra.<voice_id>`.

#### Expressive Mode

When enabled on an AI Assistant, the model dynamically controls emotional delivery using SSML emotion tags. The AI decides in real time when to apply emotional expression based on conversation context — you don't need to hard-code emotions into your prompt.

**Enable in the portal:** Go to your assistant → Voice Settings → select a Telnyx Ultra voice → toggle Expressive Mode on.

**Enable via API:**

```bash
curl -X PATCH "https://api.telnyx.com/v2/ai/assistants/YOUR_ASSISTANT_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"voice_settings": {"voice": "Telnyx.Ultra.VOICE_ID", "expressive_mode": true}}'
```

`expressive_mode` is only supported for Ultra voices; enabling it with a non-Ultra voice returns a validation error.

#### SSML Emotion Reference

Format: `<emotion value="EMOTION" />Your text here.`

**Primary emotions (best quality):**

| Tag | Use for |
|---|---|
| `<emotion value="angry" />` | Firm, assertive delivery |
| `<emotion value="excited" />` | Energetic, enthusiastic responses |
| `<emotion value="content" />` | Calm, satisfied tone |
| `<emotion value="sad" />` | Empathetic, subdued delivery |
| `<emotion value="scared" />` | Anxious, worried tone |

**Additional emotions:** `happy`, `enthusiastic`, `curious`, `calm`, `grateful`, `affectionate`, `sarcastic`, `surprised`, `confident`, `hesitant`, `apologetic`, `determined`, `frustrated`, `disappointed`, and more.

**Nonverbalisms:** Insert `[laughter]` directly in text.

**Pauses:** Use `<break time="0.2s" />` for explicit pauses. Start with short pauses (0.2s–0.3s) and adjust.

Omitting tags produces neutral, natural delivery — use explicit tags sparingly for ambiguous readings or important moments.

#### Language Support

Ultra supports 36 languages via the `language_boost` setting, which improves pronunciation accuracy: Arabic, Bengali, Bulgarian, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Gujarati, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Marathi, Māori, Norwegian, Polish, Portuguese, Punjabi, Romanian, Russian, Slovak, Spanish, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, and Vietnamese.

### TTS WebSocket Streaming

The Telnyx TTS WebSocket API provides real-time audio synthesis from text input, enabling low-latency voice generation.

#### Endpoint

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice={voice_id}
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `voice` | string | Yes | Voice identifier (e.g. `Telnyx.NaturalHD.astra`) |
| `inactivity_timeout` | integer | No | Seconds without message before closing (default: 20) |

Authenticate with an `Authorization: Bearer YOUR_API_KEY` header.

#### Connection Flow

1. **Connect** — Open WebSocket with authentication.
2. **Initialize** — Send `{
