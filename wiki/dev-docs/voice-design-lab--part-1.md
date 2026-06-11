---
title: Voice Design Lab
summary: The Telnyx Voice Design Lab lets you create custom text-to-speech voices
  either by describing what you want in natural language (voice design) or by uploading
  a recording of an existing speaker (voice cloning). Both paths produce a production-ready
  voice ID you can use across AI Assistants, Call Control, and the TTS WebSocket API.
sources:
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/concepts/index
  content_hash: c60b20a75a8bace3c2f04b5224c2ce2565c3e6cb725a52bdd479050ae845ef61
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/errors
  content_hash: cf23f295060c031a493711fbb6750713546320b99485c4252f123dcdbe402b26
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/parameters
  content_hash: 54abc1839297816e2c7922e25c897bb9a14cb88ab47ac03cffa7727531771307
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/quickstart
  content_hash: 073b498be8317ba0ec2e125b907bafa353cff565fcff00b9f0df0f67ae437db0
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/responses
  content_hash: 46560a2018645bb9c7cdbca09387618c9f7a6f06c2d8ae371c02044fbb1f2f29
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/api-details
  content_hash: 1725f44827794279807e7725e45b4128c8aca67b6092c874aeee33bf107d7feb
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/concepts/index
  content_hash: 75966e93a539e23aace590fbebab403367d144cf61ee640eb9b05297cc0a010a
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/prompting-guide
  content_hash: cd0e76231d0338c8669aa437f84fd799f1f6c85b14cece0f76fb8943c81b98e1
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/quickstart
  content_hash: 168c94cf0a921cd032a0d6447ee9b17de2077a4f88e1ad5827174092ccb8505a
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/index
  content_hash: 8787000e3f15133ef96752ff10e62e1c6fb200a0c66d6cd730df31fa50f8956f
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/using-custom-voices/index
  content_hash: b6f14a0eeb84a0123e99c58c1003a3d1ef2ef369de363345495e90cf7e94cdea
updated_at: 2026-06-11T10:49:14Z
---

# Voice Design Lab

*Part 1 of 3 — see also: [Part 2](voice-design-lab--part-2.md), [Part 3](voice-design-lab--part-3.md)*

The Telnyx Voice Design Lab lets you create custom text-to-speech voices either by describing what you want in natural language (voice design) or by uploading a recording of an existing speaker (voice cloning). Both paths produce a production-ready voice ID you can use across AI Assistants, Call Control, and the TTS WebSocket API.

## Design a Voice from a Prompt

Voice design generates a synthetic voice from a natural language description. You describe what you want — age, tone, accent, pacing — and the AI creates audio samples that match. There is no source audio; the voice is generated from scratch based on your text prompt.

The workflow has two steps:

1. **Voice Design** — an intermediate artifact (a draft). You can iterate on it up to 50 versions per design. It is **not** directly usable for TTS.
2. **Voice Clone** — a production-ready voice created from a design. This is what you pass to AI Assistants, Call Control, and the TTS API.

```
POST /v2/voice_designs → generates a sample → returns design id + version
POST /v2/voice_clones  → saves the design as a usable voice → returns voice clone id
```

The portal hides this two-step flow behind a single "Save This Voice" button.

### Portal walkthrough

1. Choose a provider (**Telnyx** or **Minimax**).
2. Describe the voice in natural language — gender, age, tone, pace, texture, personality.
3. Click **Generate Samples** to create three audio previews, each reading a different script in your chosen language.
4. Listen to each sample. Click **Regenerate All** to try again, or refine your description.
5. Click **Save This Voice**. Give it a name and gender tag — this creates a production-ready voice clone.

### API walkthrough

**1. Create a voice design:**

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

**2. Listen to the generated sample:**

```
GET /v2/voice_designs/{id}/sample
```

Returns `audio/wav`.

**3. Save as a usable voice clone:**

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

## Clone a Voice from Audio

Voice cloning captures a speaker's vocal characteristics — timbre, cadence, accent, pronunciation — from a short audio sample and applies them to new speech synthesis. The clone is a *representation* of the voice, not a recording. The system learns patterns from your audio and encodes them into parameters that guide TTS.

A clone is a statistical approximation — the model extracts patterns (formant frequencies, prosodic tendencies, spectral characteristics) and applies them during synthesis. Output passes through the TTS model, which has its own characteristics. A clone sounds *like* the speaker, but through the lens of the model. Quality has a ceiling set by your source audio, and the clone may not handle speech styles far from the original sample well (e.g., a voice cloned from calm narration may sound different when asked to express strong emotion).

### Two ways to create a clone

| Method | What it does | When to use |
| --- | --- | --- |
| **Upload audio** | Send an audio file directly | You have a recording ready |
| **From a voice design** | Save a previously generated design as a clone | You used Design a Voice to create it |

Both produce the same output: a voice clone with a voice ID you can use in production.

### Upload a file (portal)

1. Choose a provider (**Telnyx** or **Minimax**).
2. In the [Voice Design Lab](https://portal.telnyx.com/#/app/ai/voice-design-lab), click **Upload Audio** and choose your file or drag and drop it.
3. Enter a name for the voice and select the gender.
4. Click **Clone Voice**. The system processes the audio and creates a voice clone, typically in a few seconds.

### Record directly in the browser

1. Click **Upload Audio**, then select the **Record** tab.
2. Select the language you'll speak in. The system generates a reading script optimized for voice cloning.
3. Click **Start Recording** and read the script clearly.
4. Listen to your recording. Re-record if needed, then click **Clone Voice**.

### API: Clone with Telnyx (default — Qwen3TTS)

```
POST /v2/voice_clones/from_upload
Content-Type: multipart/form-data

audio_file: recording.wav
name: My Custom Voice
language: en
gender: female
```

### API: Clone with Minimax

Supports longer audio (up to 5 minutes):

```
POST /v2/voice_clones/from_upload
Content-Type: multipart/form-data

audio_file: recording.wav
name: My Custom Voice
language: en
gender: female
provider: minimax
```

### API: Clone with Ultra model

Ultra clones use the higher-quality `Ultra` model. The request returns `202 Accepted` — poll the clone's status until it becomes `active`.

```
POST /v2/voice_clones/from_upload
Content-Type: multipart/form-data

audio_file: recording.wav
name: My Ultra Voice
language: en
gender: female
provider: telnyx
model_id: Ultra
```

Response (`202 Accepted`):

```json
{
  "data": {
    "id": "uuid",
    "status": "pending"
  }
}
```

Poll with `GET /v2/voice_clones` until `status` is `active`.

## Models and Providers

Both voice design and voice cloning support two providers, selected via the `provider` body parameter.

| | Telnyx (Qwen3TTS) | Minimax |
| --- | --- | --- |
| **`provider` value** | `"telnyx"` (default) | `"minimax"` |
| **Generation parameters** | Respected | Not supported |
| **Prompt interpretation** | Follows prompts closely | May interpret differently |
| **When to use** | Fine control over generation, consistent results | Try a different model's interpretation of the same prompt |

Both providers support the same languages: Auto, Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian.

### Clone models

Set via `model_id` (body) on `POST /v2/voice_clones/from_upload`, or use `provider` to select Minimax.

| Model | Provider | Audio length | Max file | Sync/Async | Best for |
| --- | --- | --- | --- | --- | --- |
| **Qwen3TTS** | Telnyx (default) | 3–15s (auto-trimmed to 10s) | 5 MB | Sync (201) | Short, clean samples |
| **Ultra** | Telnyx | Up to 10s | 5 MB | Async (202) | Higher quality, more natural |
| **speech-2.8-turbo** | Minimax | 10s–5 min | 20 MB | Sync (201) | Longer recordings, more vocal range |

When `model_id` is `"Ultra"`, the API returns **202 Accepted** instead of 201. Poll `GET /v2/voice_clones/{id}` until `status` is `"active"`.

### Audio requirements for cloning

| | Qwen3TTS | Ultra | Minimax |
| --- | --- | --- | --- |
| **Audio length** | 3–15s (5–10s optimal) | Up to 10s | 10s–5 min |
| **Max file size** | 5 MB | 5 MB | 20 MB |
| **Formats** | WAV, MP3, FLAC, OGG, M4A | Same | Same |

- **Qwen3TTS:** aim for 5–10 seconds. Longer isn't better — auto-trims to 10s.
- **Minimax:** longer is better. 1–2 minutes of varied speech gives more vocal range.

### The `ref_text` parameter

Body parameter on `POST /v2/voice_clones/from_upload`. Optional. A transcript of what's being said in the audio. Improves clone quality by giving the model a text reference to align against.

### Voice design generation parameters

Body parameters on `POST /v2/voice_designs`. **Telnyx provider only** — ignored when `provider` is `"minimax"`.

| Body parameter | Default | Range | What it does |
| --- | --- | --- | --- |
| `temperature` | 0.9 | 0–2 | Higher = more varied/creative output. Lower = more predictable. |
| `top_k` | 50 | 1–1000 | Limits vocabulary at each generation step. Lower = more focused. |
| `top_p` | 1.0 | 0–1 | Nucleus sampling cutoff. Lower = fewer token choices. |
| `repetition_penalty` | 1.05 | 1–2 | Reduces repeated patterns in generated audio. |
| `max_new_tokens` | 2048 | 100–4096 | Maximum tokens to generate. Affects output length. |

The defaults are a good starting point — you can skip these parameters entirely and get good results.
