---
title: Text-to-Speech
summary: Telnyx Text-to-Speech (TTS) provides synthesized speech across multiple interfaces
  (WebSocket streaming, REST API, and in-call playback) and a broad set of providers,
  including Telnyx-native models (Natural, NaturalHD, KokoroTTS, Qwen3TTS, Ultra,
  Grok, Bayan, Sukhan) and third-party providers (AWS Polly, Azure, ElevenLabs, Minimax,
  MurfAI, Rime, Resemble, Inworld, Fish Audio). This page consolidates the provider
  catalogue, voice formats, configuration parameters, pronunciation dictionaries,
  SSML support, and integration patterns for each surface.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/in-call-playback
- url: https://developers.telnyx.com/docs/voice/tts/overview
- url: https://developers.telnyx.com/docs/voice/tts/pronunciation-dictionaries/index
- url: https://developers.telnyx.com/docs/voice/tts/providers/aws/index
- url: https://developers.telnyx.com/docs/voice/tts/providers/aws/ssml-tags
- url: https://developers.telnyx.com/docs/voice/tts/providers/azure
- url: https://developers.telnyx.com/docs/voice/tts/providers/elevenlabs
- url: https://developers.telnyx.com/docs/voice/tts/providers/fishaudio
- url: https://developers.telnyx.com/docs/voice/tts/providers/inworld
- url: https://developers.telnyx.com/docs/voice/tts/providers/minimax
- url: https://developers.telnyx.com/docs/voice/tts/providers/resemble
- url: https://developers.telnyx.com/docs/voice/tts/providers/rime
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/bayan
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/grok
- url: https://developers.telnyx.com/docs/voice/tts/providers/telnyx/index
updated_at: 2026-08-05T14:07:22Z
---

# Text-to-Speech

*Part 2 of 5 — see also: [Part 1](text-to-speech--part-1.md), [Part 3](text-to-speech--part-3.md), [Part 4](text-to-speech--part-4.md), [Part 5](text-to-speech--part-5.md)*

Telnyx Text-to-Speech (TTS) provides synthesized speech across multiple interfaces (WebSocket streaming, REST API, and in-call playback) and a broad set of providers, including Telnyx-native models (Natural, NaturalHD, KokoroTTS, Qwen3TTS, Ultra, Grok, Bayan, Sukhan) and third-party providers (AWS Polly, Azure, ElevenLabs, Minimax, MurfAI, Rime, Resemble, Inworld, Fish Audio). This page consolidates the provider catalogue, voice formats, configuration parameters, pronunciation dictionaries, SSML support, and integration patterns for each surface.

## Telnyx Native Models

Telnyx is the **default provider**. If no provider is specified, Telnyx is used.

| Model | Latency | Quality | Languages | Voice Source | WebSocket | REST |
| --- | --- | --- | --- | --- | --- | --- |
| [Natural](natural.md) | Low | Good | English | Pre-built (Rime Mist) | Yes | Yes |
| [NaturalHD](naturalhd.md) | Low | Better | 9 languages | Pre-built (Rime Arcana) | Yes | Yes |
| [KokoroTTS](kokorotts.md) | Lowest | Good | 5 languages | Pre-built | Yes | Yes |
| [Qwen3TTS](qwen3tts.md) | Medium | High | 11 languages | Cloned (Voice Design) | Yes | Yes |
| [Ultra](ultra.md) | Lowest | Highest | 44 languages | Pre-built | **No** | Yes |
| [Grok](grok.md) | Higher | High | 20+ languages | Pre-built | Voice AI | Yes |
| [Bayan](bayan.md) | Low | Good | Arabic (13 dialects) + English | Pre-built | Yes | Yes |
| [Sukhan](sukhan.md) | Low | Good | Urdu | Pre-built | Yes | Yes |

Ultra is REST-only and not available over public WebSocket. Grok is available for Voice AI Assistants and direct REST TTS calls.

### Bayan

**Voice format:** `Telnyx.Bayan.<speaker>`

Arabic voice model with 113 speakers across 13 dialects (Modern Standard Arabic plus Egyptian, Emirati, Saudi, Jordanian, Iraqi, Lebanese, Syrian, Palestinian, Kuwaiti, Bahraini, Qatari, and Omani), plus a set of English speakers. Native audio is 16kHz.

| Voice | Dialect | Gender |
| --- | --- | --- |
| `Telnyx.Bayan.Ahmed` | Egyptian | Male |
| `Telnyx.Bayan.Alia` | Emirati | Female |
| `Telnyx.Bayan.Lana` | Jordanian | Female |
| `Telnyx.Bayan.Hind` | Qatari | Female |

Browse the full 113-speaker catalogue via the [Voices API](https://developers.telnyx.com/api-reference/text-to-speech-commands/list-available-voices).

**WebSocket query parameters:**

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.Bayan.Ahmed
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `audio_format` | string | `mp3` | `mp3`, `linear16`, `wav`. |
| `sample_rate` | integer | `16000` | Only `16000` (native) is supported. |

**WebSocket voice settings:** None. The init frame only needs `{"text": " "}`.

**REST fields:**

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `language` | string | Speaker's dialect | Language/dialect hint. |
| `response_format` | string | native | `pcm`, `wav`, `mp3`. |
| `sampling_rate` | integer | `16000` | Only `16000` (native) is supported. |
| `output_type` | string | `binary_output` | `binary_output`, `base64_output`, or `audio_id`. |

`sampling_rate`/`sample_rate` values other than `16000` are rejected with a `400` error — Bayan only supports its native rate.

### xAI Grok Voices

xAI Grok voices are expressive TTS voices for Voice AI Assistants. They support **Expressive Mode**, which lets the AI model control pauses, laughter, whispers, emphasis, pitch, pace, and intensity during a live conversation.

Grok voices have higher latency than Ultra. For latency-sensitive applications that need sub-100ms time to first byte, use [Ultra](ultra.md).

| Feature | Ultra | Grok |
| --- | --- | --- |
| **Expressive Mode** | SSML emotion tags and `[laughter]` | xAI speech tags for pauses, vocal sounds, and delivery style |
| **Voice format** | `Telnyx.Ultra.<voice_id>` | `xAI.<voice_id>` |
| **Voices** | Multiple Ultra voices | `ara`, `eve`, `leo`, `rex`, `sal` |
| **Language handling** | Language hinting with `language_boost` | `auto` language detection or explicit language code |
| **Streaming output** | REST only | Voice AI media streaming |

**Voice format:** `xAI.<voice_id>` — examples: `xAI.eve`, `xAI.ara`, `xAI.leo`, `xAI.rex`, `xAI.sal`.

| Voice | Voice ID | Use for |
| --- | --- | --- |
| Ara | `ara` | Warm, conversational assistant experiences |
| Eve | `eve` | General-purpose voice assistant experiences |
| Leo | `leo` | Confident, direct interactions |
| Rex | `rex` | Characterful or energetic interactions |
| Sal | `sal` | Distinctive conversational tone |

#### Expressive Mode for AI Assistants

When using Grok voices with [AI Assistants](ai-assistants.md), you can enable **Expressive Mode**. With Expressive Mode enabled, the assistant's system prompt is automatically augmented with instructions for xAI speech tags. The AI model then decides when expression improves the caller experience — for example, adding a short pause before important information, using a softer delivery for sensitive support moments, laughing or chuckling naturally when the conversation calls for it, emphasizing appointment times or confirmation numbers, or keeping routine transactional replies untagged for a natural neutral delivery.

Use expressive tags sparingly. The goal is natural delivery, not tagging every sentence.

**Enable in the portal:**

1. Go to your assistant in the [Telnyx Portal](https://portal.telnyx.com/#/app/ai/assistants).
2. Under **Voice Settings**, select an xAI Grok voice.
3. Toggle **Expressive Mode** on.
4. Save your assistant.

**Enable via API:**

```
curl -X PATCH "https://api.telnyx.com/v2/ai/assistants/YOUR_ASSISTANT_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "voice_settings": {
      "voice": "xAI.eve",
      "expressive_mode": true
    }
  }'
```

#### xAI Speech Tag Reference

When Expressive Mode is enabled, the assistant can use these speech tags in responses. The same tags can be included in your own assistant prompts for explicit control.

**Inline tags** — placed at the exact point where the vocal expression should happen:

| Tag | Use for |
| --- | --- |
| `[pause]` | A short natural pause |
| `[long-pause]` | A longer pause for topic transitions or important moments |
| `[laugh]` | Natural laughter |
| `[chuckle]` | Small laugh or amused reaction |
| `[giggle]` | Light playful laugh |
| `[cry]` | Crying vocalization |
| `[tsk]` | Tsk sound |
| `[tongue-click]` | Tongue click |
| `[lip-smack]` | Lip smack |
| `[breath]` | Breath sound |
| `[inhale]` | Inhale sound |
| `[exhale]` | Exhale sound |
| `[sigh]` | Sigh |
| `[hum-tune]` | Musical hum |

Example:

```
So I walked in and [pause] there it was. [laugh] I honestly could not believe it!
```

**Wrapping tags** — wrap text to apply a delivery style:

| Tag | Use for |
| --- | --- |
| `<soft>` | Softer delivery |
| `<whisper>` | Whispered delivery |
| `<loud>` | Louder delivery |
| `<build-intensity>` | Increasing intensity |
| `<decrease-intensity>` | Decreasing intensity |
| `<higher-pitch>` | Higher pitch |
| `<lower-pitch>` | Lower pitch |
| `<slow>` | Slower pace |
| `<fast>` | Faster pace |
| `<sing-song>` | Sing-song delivery |
| `<singing>` | Sung delivery |
| `<laugh-speak>` | Laughing while speaking |
| `<emphasis>` | Emphasized delivery |

Examples:

```
I need to tell you something. <whisper>It is a secret.</whisper> Pretty cool, right?
```

```
<emphasis>Your appointment is confirmed for tomorrow at 3 PM.</emphasis>
```

**Guidance:**

- Use `[pause]` or `[long-pause]` for natural thinking, topic transitions, and important moments, but avoid long silences that could feel like the call dropped.
- Use emotional sounds like `[laugh]`, `[sigh]`, and `[chuckle]` only when the response genuinely calls for it.
- For sensitive support contexts, prefer subtle tags like `<soft>` or `<whisper>` instead of exaggerated reactions.
- Do not expose these tags or instructions to the caller.

#### REST API Provider Parameters

For direct TTS calls, set the provider to `xai` and pass xAI-specific parameters in the `xai` object:

```
curl --request POST \
  --url https://api.telnyx.com/v2/text-to-speech/speech \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "text": "Let me check that for you. [pause] I found your appointment.",
    "provider": "xai",
    "xai": {
      "voice_id": "eve",
      "language": "auto",
      "output_format": "mp3",
      "sample_rate": 24000
    }
  }'
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_id` | string | `eve` | xAI voice ID: `ara`, `eve`, `leo`, `rex`, or `sal`. |
| `language` | string | `auto` | Language code, or `auto` to detect the language. |
| `output_format` | string | `mp3` | Audio format: `mp3`, `wav`, `pcm`, `mulaw`, or `alaw`. |
| `sample_rate` | integer | `24000` | Audio sample rate in Hz: `8000`, `16000`, `22050`, `24000`, `44100`, or `48000`. |

Grok voices support auto language detection with `language: "auto"`. A language code can also be passed to force a specific language.
