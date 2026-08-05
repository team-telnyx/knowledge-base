---
title: Telnyx Speech-to-Text and Text-to-Speech WebSocket Streaming
summary: Telnyx provides real-time WebSocket streaming APIs for both Speech-to-Text
  (STT) and Text-to-Speech (TTS), enabling low-latency audio transcription and synthesis
  for live voice applications. This page covers the STT and TTS WebSocket endpoints,
  authentication, supported engines and voices, frame formats, and complete Python
  examples for building bi-directional streaming clients.
sources:
- url: https://developers.telnyx.com/docs/tts-stt/stt-websocket-streaming
- url: https://developers.telnyx.com/docs/tts-stt/telnyx-ultra-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-available-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-websocket-streaming
updated_at: 2026-08-05T14:01:43Z
---

# Telnyx Speech-to-Text and Text-to-Speech WebSocket Streaming

*Part 3 of 3 — see also: [Part 1](telnyx-speech-to-text-and-text-to-speech-websocket-streaming--part-1.md), [Part 2](telnyx-speech-to-text-and-text-to-speech-websocket-streaming--part-2.md)*

Telnyx provides real-time WebSocket streaming APIs for both Speech-to-Text (STT) and Text-to-Speech (TTS), enabling low-latency audio transcription and synthesis for live voice applications. This page covers the STT and TTS WebSocket endpoints, authentication, supported engines and voices, frame formats, and complete Python examples for building bi-directional streaming clients.

## Telnyx Ultra voices

**Telnyx Ultra** is a premium text-to-speech model that delivers natural, emotionally expressive speech across 36 languages. With sub-100ms time to first byte and support for SSML emotion tags, Ultra is built for real-time AI assistants and customer-facing voice experiences where quality and responsiveness matter.

### What makes Ultra different

| Feature | Natural / NaturalHD | Ultra |
| --- | --- | --- |
| **Time to first byte** | ~200–300ms | **< 100ms** |
| **Expressive mode** | — | Automatic emotional interpretation with SSML emotion tags |
| **Nonverbal cues** | — | `[laughter]` and other natural vocalizations |
| **Languages** | Varies by voice | 36 languages |

### Voice format

Ultra voices use the format:

```
Telnyx.Ultra.<voice_id>
```

Browse available Ultra voices on the [Available Voices](available-voices.md) page and filter by the Ultra model.

### Expressive mode for AI Assistants

When using Ultra voices with [AI Assistants](ai-assistants.md), you can enable **expressive mode** — a toggle that lets the AI model dynamically control the emotional delivery of speech during a live conversation.

With expressive mode enabled, the assistant's system prompt is automatically augmented with instructions for using SSML emotion tags. The AI model then decides — in real time — when and how to apply emotional expression based on the conversation context. For example, the assistant might:

- Use an excited tone when delivering good news.
- Respond with empathy when a customer describes a problem.
- Insert `[laughter]` for natural, friendly moments.
- Speak neutrally for matter-of-fact information.

This "director-style" approach means you don't need to hard-code emotions into your prompt — the AI interprets the emotional subtext naturally, with optional explicit guidance for important moments.

![Conversation transcript showing an AI assistant using expressive mode — responding with angry, sad, and happy emotions plus laughter based on the user's requests](https://mintcdn.com/telnyx/6HnegDj7NgZUFT6I/img/ultra-expressive-mode-demo.png?fit=max&auto=format&n=6HnegDj7NgZUFT6I&q=85&s=48d326946aff58b2396b0eb1965e0f32)

#### Enable in the portal

1. Go to your assistant in the [Telnyx Portal](https://portal.telnyx.com/#/app/ai/assistants).
2. Under **Voice Settings**, select a **Telnyx Ultra** voice.
3. Toggle **Expressive Mode** on.
4. Save your assistant.

![AI Assistant voice settings in the Telnyx Portal showing a Telnyx Ultra voice selected and the Expressive Mode toggle enabled](https://mintcdn.com/telnyx/93EkNzE8M3fjEz_c/img/ultra-voice-settings-expressive-mode.png?fit=max&auto=format&n=93EkNzE8M3fjEz_c&q=85&s=e8a4d9333d29ddc394c47e28f1a07c3f)

#### Enable via API

Set `expressive_mode: true` in your assistant's `voice_settings`:

```bash
curl -X PATCH "https://api.telnyx.com/v2/ai/assistants/YOUR_ASSISTANT_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "voice_settings": {
      "voice": "Telnyx.Ultra.YOUR_VOICE_ID",
      "expressive_mode": true
    }
  }'
```

`expressive_mode` is only supported for Telnyx Ultra voices (voices starting with `Telnyx.Ultra.`). Enabling it with a non-Ultra voice will return a validation error.

### SSML emotion reference

When expressive mode is enabled, the assistant can use these SSML emotion tags in its responses. You can also use these tags with Ultra voices in [Call Control speak commands](call-control-speak-commands.md).

**Format:** Place an `<emotion>` tag before the text you want to affect:

```xml
<emotion value="EMOTION" />Your text here.
```

**Primary emotions (best quality):**

| Tag | Use for |
| --- | --- |
| `<emotion value="angry" />` | Firm, assertive delivery |
| `<emotion value="excited" />` | Energetic, enthusiastic responses |
| `<emotion value="content" />` | Calm, satisfied tone |
| `<emotion value="sad" />` | Empathetic, subdued delivery |
| `<emotion value="scared" />` | Anxious, worried tone |

**Additional emotions:** `happy`, `enthusiastic`, `curious`, `calm`, `grateful`, `affectionate`, `sarcastic`, `surprised`, `confident`, `hesitant`, `apologetic`, `determined`, `frustrated`, `disappointed`, and more.

**Nonverbalisms:** Insert `[laughter]` directly in the text for natural laughing:

```
That's a great joke! [laughter] Okay, let me help you with that.
```

**Pauses:** Use SSML `<break>` tags to add explicit pauses to Ultra speech. Set the pause length with the `time` attribute:

```xml
Hello, thank you for calling. <break time="0.2s"/> This is Alex. How can I help you today?
```

For natural conversational pacing, start with short pauses like `0.2s` or `0.3s`, then adjust based on how the voice sounds in your use case.

You don't need emotion tags or break tags for every sentence. Ultra naturally interprets emotional subtext and pacing from the text itself — use explicit tags sparingly for ambiguous readings, important moments, or places where you need a consistent pause. Omitting the tag is equivalent to neutral delivery and produces the most natural speech.

### Language support

Ultra supports 36 languages via the `language_boost` setting, which improves pronunciation accuracy for the target language: Arabic, Bengali, Bulgarian, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Gujarati, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Marathi, Māori, Norwegian, Polish, Portuguese, Punjabi, Romanian, Russian, Slovak, Spanish, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, and Vietnamese.

Set `language_boost` in your assistant's voice settings to improve pronunciation for the target language.

## Prerequisites

- **Python 3.8+**.
- A **Telnyx API key**.
- `websockets` library: `pip install websockets`.

## Additional resources

- [Telnyx STT documentation](telnyx-stt-documentation.md)
- [Telnyx Media Streaming Documentation](telnyx-media-streaming-documentation.md)
- [Telnyx Voice API](telnyx-voice-api.md)
- [Full STT demo project code](https://github.com/team-telnyx/demo-python-telnyx)
- [TTS demo implementation](https://github.com/team-telnyx/demo-python-telnyx/tree/master/asyncio-tts-standalone)
