---
title: Voice Design Lab
summary: 'The Voice Design Lab lets you create custom voices for text-to-speech in
  two ways: by describing a voice in natural language (Design a Voice) or by cloning
  from an audio sample (Clone from Audio). Both flows produce a production-ready voice
  clone that can be used across AI Assistants, Call Control, and the TTS API.'
sources:
- url: https://developers.telnyx.com/docs/voice/voice-design-lab
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/concepts/index
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/errors
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/parameters
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/quickstart
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/responses
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/api-details
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/concepts/index
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/prompting-guide
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/quickstart
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/using-custom-voices/index
updated_at: 2026-08-05T14:07:47Z
---

# Voice Design Lab

*Part 2 of 4 — see also: [Part 1](voice-design-lab--part-1.md), [Part 3](voice-design-lab--part-3.md), [Part 4](voice-design-lab--part-4.md)*

The Voice Design Lab lets you create custom voices for text-to-speech in two ways: by describing a voice in natural language (Design a Voice) or by cloning from an audio sample (Clone from Audio). Both flows produce a production-ready voice clone that can be used across AI Assistants, Call Control, and the TTS API.

## Design a Voice

### Concepts

Voice design generates a synthetic voice from a natural language description. You describe what you want — age, tone, accent, pacing — and the AI creates audio samples that match. This is **not** voice cloning: there is no source audio, and the voice is generated from scratch based on your text prompt.

The API has two separate resources:

1. **Voice Design** — an intermediate artifact (a draft). You can iterate on it (up to 50 versions per design). It is NOT usable for TTS directly.
2. **Voice Clone** — a production-ready voice created from a design. This is what you pass to AI Assistants, Call Control, and the TTS API.

```
POST /v2/voice_designs → generates a sample → returns design id + version
POST /v2/voice_clones  → saves the design as a usable voice → returns voice clone id
```

The portal hides this two-step flow behind a single "Save This Voice" button. When using the API directly, both steps are required.

### Portal walkthrough

1. **Choose a provider** — select **Telnyx** or **Minimax** using the provider toggle.
2. **Describe the voice** — write a natural language description of the voice you want (gender, age, tone, pace, texture, personality).
3. **Generate samples** — click **Generate Samples** to create three audio previews. Each reads a different script in your chosen language.
4. **Preview and iterate** — listen to each sample. Click **Regenerate All** to try again, or refine your description.
5. **Save as a voice clone** — click **Save This Voice**. Give it a name and gender tag — this creates a production-ready voice clone.

### API quickstart

**1. Create a voice design**

```
POST /v2/voice_designs

{
  "name": "Friendly Receptionist",
  "prompt": "Female, mid-thirties. Warm and full, slightly husky.",
  "text": "Hello, thank you for calling. How can I help you today?",
  "language": "en",
  "provider": "telnyx"
}
```

Set `"provider": "minimax"` to use the Minimax provider instead.

**2. Listen to the generated sample**

```
GET /v2/voice_designs/{id}/sample
```

Returns `audio/wav`.

**3. Save as a usable voice clone**

A voice design is a draft. To use it in production, save it as a clone:

```
POST /v2/voice_clones

{
  "name": "Friendly Receptionist",
  "voice_design_id": "DESIGN_ID",
  "version": 1,
  "language": "en",
  "gender": "female"
}
```

### Full example

Python

```python
import telnyx

client = telnyx.Telnyx(api_key="YOUR_TELNYX_API_KEY")

# 1. Create a voice design
design = client.voice_designs.create(
    name="Friendly Receptionist",
    prompt="Female, mid-thirties. Warm and full, slightly husky.",
    text="Hello, thank you for calling. How can I help you today?",
    language="en",
    provider="telnyx",
)
design_id = design.data.id
print(f"Voice design created: {design_id}")

# 2. Download the generated audio sample
sample = client.voice_designs.download_sample(design_id)
with open("sample.wav", "wb") as f:
    f.write(sample.content)
print("Sample saved to sample.wav")

# 3. Save the design as a usable voice clone
clone = client.voice_clones.create(
    params={
        "voice_design_id": design_id,
        "name": "Friendly Receptionist",
        "language": "en",
        "gender": "female",
    }
)
print(f"Voice clone ready: {clone.data.id}")
# Use this clone ID in TTS, Call Control, or AI Assistants
```

Node.js

```javascript
import Telnyx from 'telnyx';
import fs from 'fs';

const client = new Telnyx({ apiKey: 'YOUR_TELNYX_API_KEY' });

// 1. Create a voice design
const design = await client.voiceDesigns.create({
  name: 'Friendly Receptionist',
  prompt: 'Female, mid-thirties. Warm and full, slightly husky.',
  text: 'Hello, thank you for calling. How can I help you today?',
  language: 'en',
  provider: 'telnyx',
});
console.log(`Voice design created: ${design.data.id}`);

// 2. Download the generated audio sample
const sample = await client.voiceDesigns.downloadSample(design.data.id);
const buffer = Buffer.from(await sample.arrayBuffer());
fs.writeFileSync('sample.wav', buffer);
console.log('Sample saved to sample.wav');

// 3. Save the design as a usable voice clone
const clone = await client.voiceClones.create({
  params: {
    voice_design_id: design.data.id,
    name: 'Friendly Receptionist',
    language: 'en',
    gender: 'female',
  },
});
console.log(`Voice clone ready: ${clone.data.id}`);
// Use this clone ID in TTS, Call Control, or AI Assistants
```

### Prompting guide

**Recommended format**

Structure your prompt for consistent results:

```
<Gender>, <Age range>. <Quality/energy description>.
<1–2 sentences about timbre, pacing, delivery>
```

Example:

> Female, mid-thirties. Warm and full, slightly husky. Moderate pace, sounds like someone who smiles while talking.

**Dimensions to describe**

- **Age** — "young adult" / "in their 20s" (lighter, more energetic); "mid-thirties" / "early forties" (balanced, mature); "elderly" / "in his 80s" (deeper, weathered texture).
- **Tone / Timbre** — Deep / low-pitched (gravitas, authority); Smooth / rich (polished, professional); Gravelly / raspy (character, authenticity); Airy / breathy (intimate, soft); Warm / mellow (approachable, friendly).
- **Gender** — Male, female, or describe the sound directly: "a lower-pitched, husky female voice" or "a neutral, mid-pitched androgynous voice."
- **Pacing** — Measured / deliberate (careful, authoritative); Rapid-fire / quick (energetic, urgent); Relaxed / conversational (natural, approachable); Rhythmic (storytelling, narration).
- **Emotion / Energy** — Calm / serene (support, meditation); Enthusiastic / upbeat (marketing, announcements); Authoritative / matter-of-fact (IVR, instructions); Warm / empathetic (customer service, healthcare).
- **Accent / Regional** — be specific: "Slight British accent" rather than "British"; "Neutral American" rather than just "American"; "Soft Southern drawl" rather than "Southern".
- **Use case context** — adding context helps the model understand intent: "Customer service agent for a bank", "Podcast narrator for true crime", "Bedtime story reader for children".

**Example prompts**

| Use Case | Prompt | Recommended Engine |
| --- | --- | --- |
| Customer service | Female, mid-thirties. Warm and full, slightly husky. Moderate pace, sounds like someone who smiles while talking. | Minimax |
| IVR system | Male, late thirties. Clean and dry, matter-of-fact. Deliberate pace, pauses before numbers and details. | Telnyx |
| Voice agent | Female, late twenties. Clear and professional, slightly upbeat. Natural conversational pace with a helpful tone. |  |
| Podcast narrator | Male, early forties. Deep and smooth, with a rich baritone. Measured pacing, storytelling cadence. | Minimax |
| Empathetic support | Male, mid-thirties. Warm, slightly gravelly. Measured and unhurried. You can hear patience in the breathing rhythm. | Telnyx |
| Notification/alert | Female, mid-twenties. Bright and crisp. Quick pace, clear enunciation. No emotion — just information. | Minimax |
| Meditation guide | Female, mid-forties. Soft, airy, and serene. Extremely slow and deliberate pace. Soothing and deeply relaxing delivery. | Minimax |
| Energetic promo | Male, early twenties. Bright and enthusiastic, high energy. Rapid-fire pacing, sounds highly engaged and convincing. | Minimax |
| Audiobook (Fiction) | Male, in his 60s. Deep, weathered texture. Relaxed, storytelling cadence with a warm, nostalgic feel. | Telnyx |

**Common pitfalls**

- **Too vague** — "nice voice" or "good voice" produces generic output. Be specific about at least 3 dimensions.
- **Contradictory traits** — "whisper" + "booming" confuses the model. Pick a coherent set of characteristics.
- **Provider differences** — the same prompt may produce noticeably different results on Telnyx vs Minimax. Try both.
- **Ignoring the preview text** — the text you provide for synthesis should match the voice's intended use. Don't use a cheerful script for a somber voice.

**The Enhance button**

The portal's **Enhance** button uses AI to expand a short description into a detailed prompt. For example, "Empathetic tech support agent" becomes:

> *Empathetic tech support agent*  **Gender and age:** Female, late 20s to early 30s. **Where the voice sits:** Head and chest, with a balanced resonance. **Texture:** Silky smooth with a faint warmth, slightly airy. **Pace:** Moderate, with deliberate pauses for clarity and reassurance. **Distinctive quality:** A gentle, patient lilt that conveys calm and understanding.

This is a good starting point, but review the expanded prompt before generating — you may want to tweak specific dimensions.

### Design API parameters

**Providers** — set via the `provider` body parameter on `POST /v2/voice_designs`.

|  | Telnyx (Qwen3TTS) | Minimax |
| --- | --- | --- |
| `provider` value | `"telnyx"` (default) | `"minimax"` |
| Generation parameters | Respected | Not supported |
| Languages | Auto, Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian | Auto, Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian |
| Prompt interpretation | Follows prompts closely | May interpret differently |
| When to use | Fine control over generation, consistent results across iterations | Try a different model's interpretation of the same prompt |

**Generation parameters** — body parameters on `POST /v2/voice_designs`. **Telnyx provider only** — ignored when `provider` is `"minimax"`.

| Body parameter | Default | Range | What it does |
| --- | --- | --- | --- |
| `temperature` | 0.9 | 0–2 | Higher = more varied/creative output. Lower = more predictable. |
| `top_k` | 50 | 1–1000 | Limits vocabulary at each generation step. Lower = more focused. |
| `top_p` | 1.0 | 0–1 | Nucleus sampling cutoff. Lower = fewer token choices. |
| `repetition_penalty` | 1.05 | 1–2 | Reduces repeated patterns in generated audio. |
| `max_new_tokens` | 2048 | 100–4096 | Maximum tokens to generate. Affects output length. |

The defaults are a great starting point — you can skip these parameters entirely and get good results. Adjust them later if you want to fine-tune the output.
