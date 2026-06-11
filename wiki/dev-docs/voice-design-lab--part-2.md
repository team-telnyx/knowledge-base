---
title: Voice Design Lab
summary: The Telnyx Voice Design Lab lets you create custom text-to-speech voices
  either by describing what you want in natural language (voice design) or by uploading
  a recording of an existing speaker (voice cloning). Both paths produce a production-ready
  voice ID you can use across AI Assistants, Call Control, and the TTS WebSocket API.
sources:
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/concepts/index
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/errors
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/parameters
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/quickstart
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/responses
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/api-details
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/concepts/index
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/prompting-guide
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/quickstart
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/index
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/using-custom-voices/index
updated_at: 2026-06-11T10:49:14Z
---

# Voice Design Lab

*Part 2 of 3 — see also: [Part 1](voice-design-lab--part-1.md), [Part 3](voice-design-lab--part-3.md)*

The Telnyx Voice Design Lab lets you create custom text-to-speech voices either by describing what you want in natural language (voice design) or by uploading a recording of an existing speaker (voice cloning). Both paths produce a production-ready voice ID you can use across AI Assistants, Call Control, and the TTS WebSocket API.

## Prompting Guide for Voice Design

### Recommended format

Structure your prompt for consistent results:

```
<Gender>, <Age range>. <Quality/energy description>.
<1–2 sentences about timbre, pacing, delivery>
```

**Example:** Female, mid-thirties. Warm and full, slightly husky. Moderate pace, sounds like someone who smiles while talking.

### Dimensions to describe

**Age:**

- "Young adult", "in their 20s" → lighter, more energetic
- "Mid-thirties", "early forties" → balanced, mature
- "Elderly", "in his 80s" → deeper, weathered texture

**Tone / Timbre:**

- **Deep / low-pitched** — gravitas, authority
- **Smooth / rich** — polished, professional
- **Gravelly / raspy** — character, authenticity
- **Airy / breathy** — intimate, soft
- **Warm / mellow** — approachable, friendly

**Gender:** Male, female, or describe the sound directly (e.g., "a lower-pitched, husky female voice" or "a neutral, mid-pitched androgynous voice").

**Pacing:**

- **Measured / deliberate** — careful, authoritative
- **Rapid-fire / quick** — energetic, urgent
- **Relaxed / conversational** — natural, approachable
- **Rhythmic** — storytelling, narration

**Emotion / Energy:**

- **Calm / serene** — support, meditation
- **Enthusiastic / upbeat** — marketing, announcements
- **Authoritative / matter-of-fact** — IVR, instructions
- **Warm / empathetic** — customer service, healthcare

**Accent / Regional:** Be specific — "slight British accent" rather than "British", "neutral American" rather than "American", "soft Southern drawl" rather than "Southern".

**Use case context:** Adding context helps the model understand intent (e.g., "customer service agent for a bank", "podcast narrator for true crime", "bedtime story reader for children").

### Example prompts

| Use Case | Prompt | Recommended Engine |
| --- | --- | --- |
| Customer service | Female, mid-thirties. Warm and full, slightly husky. Moderate pace, sounds like someone who smiles while talking. | Minimax |
| IVR system | Male, late thirties. Clean and dry, matter-of-fact. Deliberate pace, pauses before numbers and details. | Telnyx |
| Voice agent | Female, late twenties. Clear and professional, slightly upbeat. Natural conversational pace with a helpful tone. | — |
| Podcast narrator | Male, early forties. Deep and smooth, with a rich baritone. Measured pacing, storytelling cadence. | Minimax |
| Empathetic support | Male, mid-thirties. Warm, slightly gravelly. Measured and unhurried. You can hear patience in the breathing rhythm. | Telnyx |
| Notification/alert | Female, mid-twenties. Bright and crisp. Quick pace, clear enunciation. No emotion — just information. | Minimax |
| Meditation guide | Female, mid-forties. Soft, airy, and serene. Extremely slow and deliberate pace. Soothing and deeply relaxing delivery. | Minimax |
| Energetic promo | Male, early twenties. Bright and enthusiastic, high energy. Rapid-fire pacing, sounds highly engaged and convincing. | Minimax |
| Audiobook (Fiction) | Male, in his 60s. Deep, weathered texture. Relaxed, storytelling cadence with a warm, nostalgic feel. | Telnyx |

### Common pitfalls

- **Too vague** — "nice voice" or "good voice" produces generic output. Be specific about at least 3 dimensions.
- **Contradictory traits** — "whisper" + "booming" confuses the model. Pick a coherent set of characteristics.
- **Provider differences** — the same prompt may produce noticeably different results on Telnyx vs Minimax. Try both.
- **Ignoring the preview text** — the text you provide for synthesis should match the voice's intended use. Don't use a cheerful script for a somber voice.

### The Enhance button

The portal's **Enhance** button uses AI to expand a short description into a detailed prompt covering gender/age, resonance placement, texture, pace, and distinctive quality. This is a good starting point, but review the expanded prompt before generating — you may want to tweak specific dimensions.

## Recording Best Practices for Voice Cloning

1. **Match your recording to your use case.** Don't read a monotone script if you want an expressive clone. The AI replicates what it hears — including energy, emotion, and pacing.
2. **Speak clearly, avoid background noise.** Use a decent microphone in a quiet space. Background noise gets cloned too. A $100–300 USB condenser in a quiet room is sufficient.
3. **Avoid long pauses.** The cloned voice will mimic pauses between sentences. Keep speech flowing naturally.
4. **Trim your recording.** Speech from start to finish, no dead air at the beginning or end.
5. **Speak in the target language.** If you want the clone to speak Spanish, record in Spanish.
6. **Keep it consistent.** Same tone, accent, and energy throughout. Wide fluctuations confuse the model. The AI clones everything — including stutters, "uhms", and inconsistencies.
7. **Aim for the right volume.** Target -23 to -18 dB RMS with peaks no higher than -3 dB. Too quiet = noise floor issues. Too loud = clipping.
8. **Audio codec doesn't matter much.** MP3 at 128 kbps or above is fine. WAV is ideal but higher bitrate MP3 won't noticeably hurt quality.
9. **Optimal duration by model:**
   - **Qwen3TTS:** 5–10 seconds. Auto-trims to 10s. More isn't better.
   - **Ultra:** Up to 10 seconds.
   - **Minimax:** 1–2 minutes is the sweet spot. Longer recordings capture more vocal range, but beyond 3 minutes yields diminishing returns.

## Voice ID Format and Clone Status

Every clone response includes fields to construct the voice ID: `{Provider}.{Model}.{provider_voice_id}`

| Provider | `provider_voice_id` value |
| --- | --- |
| **Telnyx Qwen3TTS** | Equals the clone's UUID (`id` field) |
| **Telnyx Ultra** | Cartesia-assigned voice ID |
| **Minimax** | Minimax-assigned ID (encoded format) |

Examples:

- **Telnyx:** `Telnyx.Qwen3TTS.33226e69-3abd-429b-b64a-86775c9b5850`
- **Minimax:** `Minimax.speech-2.8-turbo.TB4ZMVKanThGeldiw8rLBEg21v4ifjUTRgLpkodJxpMYV`

Find the voice ID in the Voice Design Lab by clicking on any saved voice, or build it from the clone response's `provider`, `provider_supported_models`, and `provider_voice_id` fields.

### Clone status

| Status | Meaning |
| --- | --- |
| `active` | Ready to use |
| `pending` | Being processed (Ultra only — poll until active) |
| `failed` | Processing failed |
| `expired` | Voice was not kept alive |

Qwen3TTS and Minimax clones are always `active` on creation.

## Using Custom Voices

Once you have a voice ID, you can use it across Telnyx products:

- **AI Assistants:** Select your custom voice in the assistant's voice settings. Telnyx clones appear under **Telnyx / Qwen3TTS**, Minimax clones under **Minimax**.
- **Call Control:** Pass the voice ID in the `voice` field of the `speak` command.
- **TTS WebSocket:** Pass the voice ID as the `voice` query parameter on the WebSocket URL. See the [TTS streaming guide](https://developers.telnyx.com/docs/tts-stt/tts-websocket-streaming) for the full connection flow.
