---
title: Voice Cloning
summary: Create custom AI-generated voices using natural language prompts or clone voices from audio recordings, then use them across Telnyx TTS services.
sources:
  - url: https://developers.telnyx.com/docs/tts-stt/voice-cloning/index
    content_hash: a89795af3551239ae23d901919adcd805f1da745bf38e1189ec12b3c2200aab5
updated_at: 2026-04-10T00:00:00Z
---

# Voice Cloning

Create custom AI-generated voices using natural language prompts or clone voices from audio recordings, then use them across Telnyx TTS services.

The **[Voice Design Lab](https://portal.telnyx.com/#/app/ai/voice-design-lab)** lets you create unique, custom voices for text-to-speech without recording studio sessions or training datasets. There are two ways to create a custom voice:

* **Design a voice** — Describe the voice you want in natural language and the AI generates it.
* **Clone from audio** — Upload or record a short audio sample to capture a voice identity.

Both methods support two voice providers:

* **Telnyx** — Powered by Qwen3TTS, optimized for short reference audio (3–15 seconds).
* **Minimax** — Supports longer reference audio (10 seconds to 5 minutes) for richer voice capture.

Use the provider toggle at the top of the Design Studio or Upload panel to switch between them.

Once created, your custom voices are available anywhere Telnyx supports text-to-speech: AI Assistants, Call Control speak commands, and the TTS API.

## Design a voice from a prompt

Voice Design uses AI to generate voices from natural language descriptions. You describe characteristics like tone, age, pace, and texture — and the system creates audio samples you can preview before saving.

### How it works

1. **Choose a provider**

    Select **Telnyx** or **Minimax** using the provider toggle. Both generate voices from your description, but use different underlying models.

2. **Describe the voice**

    Write a natural language description of the voice you want. You can be as specific as you like — describe gender, age, tone, pace, texture, and personality.

    **Example prompts:**

    | Style      | Prompt                                                                                                              |
    | ---------- | ------------------------------------------------------------------------------------------------------------------- |
    | Friendly   | Female, mid-thirties. Warm and full, slightly husky. Moderate pace, sounds like someone who smiles while talking.   |
    | Precise    | Male, late thirties. Clean and dry, matter-of-fact. Deliberate pace, pauses before numbers and details.             |
    | Empathetic | Male, mid-thirties. Warm, slightly gravelly. Measured and unhurried. You can hear patience in the breathing rhythm. |

      Use the **Enhance** button in the portal to expand a short description into a detailed prompt. For example, "friendly dental receptionist" becomes a full voice specification.

3. **Generate samples**

    Click **Generate Samples** to create three audio previews. Each sample reads a different AI-generated script in your chosen language, so you can hear how the voice sounds in varied contexts.

4. **Preview and iterate**

    Listen to each sample. If none feel right, click **Regenerate All** to try again with the same prompt, or refine your description and generate new samples.

5. **Save as a voice clone**

    When you find a sample you like, click **Save This Voice**. Give it a name and gender tag — this creates a production-ready voice clone you can use immediately.

### Using the API

You can also design voices programmatically:

```bash theme={null}


## Related Pages

- [Voice Call Router](../runbooks/voice-call-router.md)
