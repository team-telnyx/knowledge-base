---
title: Telnyx Developer Documentation
summary: A comprehensive guide to Telnyx's Programmable Fax, Reporting & Analytics,
  and Speech & Voice APIs, covering setup, sending and receiving faxes, webhook handling,
  usage reporting, session analysis, and real-time speech-to-text and text-to-speech
  streaming.
sources:
- url: https://developers.telnyx.com/docs/programmable-fax/email-to-fax
- url: https://developers.telnyx.com/docs/programmable-fax/get-started/index
- url: https://developers.telnyx.com/docs/programmable-fax/quickstart
- url: https://developers.telnyx.com/docs/programmable-fax/receive-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/receiving-webhooks
- url: https://developers.telnyx.com/docs/programmable-fax/send-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/sending-commands
- url: https://developers.telnyx.com/docs/reporting/on-demand-reports/index
- url: https://developers.telnyx.com/docs/reporting/session-analysis
- url: https://developers.telnyx.com/docs/reporting/usage-reports/index
- url: https://developers.telnyx.com/docs/tts-stt/stt-websocket-streaming
- url: https://developers.telnyx.com/docs/tts-stt/telnyx-ultra-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-available-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-websocket-streaming
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
