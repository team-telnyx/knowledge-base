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

*Part 3 of 4 — see also: [Part 1](voice-design-lab--part-1.md), [Part 2](voice-design-lab--part-2.md), [Part 4](voice-design-lab--part-4.md)*

The Voice Design Lab lets you create custom voices for text-to-speech in two ways: by describing a voice in natural language (Design a Voice) or by cloning from an audio sample (Clone from Audio). Both flows produce a production-ready voice clone that can be used across AI Assistants, Call Control, and the TTS API.

## Clone from Audio

### Concepts

Voice cloning captures a speaker's vocal characteristics — timbre, cadence, accent, pronunciation — from a short audio sample and applies them to new speech synthesis. The clone is a *representation* of the voice, not a recording of it. The system learns patterns from your audio and encodes them into parameters that guide TTS. This means:

- The cloned voice can say things the original speaker never said.
- Clone quality is bounded by what the model can learn from your sample.
- Poor recordings, background noise, or inconsistent delivery degrade the clone.

A clone is not a recording. It's a statistical approximation of a voice — the model extracts patterns (formant frequencies, prosodic tendencies, spectral characteristics) and applies them during synthesis. This means:

- Output passes through the TTS model, which has its own characteristics. A clone sounds *like* the speaker, but through the lens of the model.
- Quality has a ceiling set by your source audio. No amount of API parameters will fix a noisy or inconsistent recording.
- The clone may not handle speech styles far from the original sample well. A voice cloned from calm narration may sound different when asked to express strong emotion.

**Two ways to create a clone**

| Method | What it does | When to use |
| --- | --- | --- |
| Upload audio | Send an audio file directly | You have a recording ready |
| From a voice design | Save a previously generated design as a clone | You used Design a Voice to create it |

Both produce the same output: a voice clone with a voice ID you can use in production.

### Recording best practices

1. **Match your recording to your use case.** Don't read a monotone script if you want an expressive clone. The AI replicates what it hears — including energy, emotion, and pacing.
2. **Speak clearly, avoid background noise.** Use a decent microphone in a quiet space. Background noise gets cloned too. A $100–$300 USB condenser in a quiet room is sufficient.
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

### Portal walkthrough

**Upload a file**

1. **Choose a provider** — select **Telnyx** or **Minimax** using the provider toggle.
2. **Upload audio** — in the [Voice Design](https://portal.telnyx.com/#/app/ai/voice-design-lab), click **Upload Audio** and choose your file or drag and drop it.
3. **Set voice details** — enter a name for the voice and select the gender.
4. **Clone** — click **Clone Voice**. The system processes the audio and creates a voice clone, typically in a few seconds.

**Record directly in the browser**

1. **Switch to Record mode** — click **Upload Audio**, then select the **Record** tab.
2. **Choose a language** — select the language you'll speak in. The system generates a reading script optimized for voice cloning.
3. **Read the script** — click **Start Recording** and read the script clearly. It's designed to capture the full range of phonemes.
4. **Review and submit** — listen to your recording. Re-record if needed, then click **Clone Voice**.

### Clone API quickstart

**Clone with Telnyx (default)**

```
POST /v2/voice_clones/from_upload
Content-Type: multipart/form-data

audio_file: recording.wav
name: My Custom Voice
language: en
gender: female
```

**Clone with Minimax**

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

**Clone with Ultra model**

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
    "status": "pending",
    ...
  }
}
```

Poll with `GET /v2/voice_clones` until `status` is `active`.

### SDK examples

**Clone with Telnyx (default)**

Python

```python
import telnyx

client = telnyx.Telnyx(api_key="YOUR_TELNYX_API_KEY")

clone = client.voice_clones.create_from_upload(
    params={
        "audio_file": open("recording.wav", "rb"),
        "name": "My Custom Voice",
        "language": "en",
        "gender": "female",
        "provider": "telnyx",
    }
)

print("Voice Clone Created:", clone.data)
```

Node.js

```javascript
import Telnyx from 'telnyx';
import fs from 'fs';

const client = new Telnyx({ apiKey: 'YOUR_TELNYX_API_KEY' });

const clone = await client.voiceClones.createFromUpload({
  params: {
    audio_file: fs.createReadStream('recording.wav'),
    name: 'My Custom Voice',
    language: 'en',
    gender: 'female',
    provider: 'telnyx',
  },
});

console.log('Voice Clone Created:', clone.data);
```

**Clone with Minimax**

Minimax supports longer audio (up to 20MB) and uses the `speech-2.8-turbo` model.

Python

```python
import telnyx

client = telnyx.Telnyx(api_key="YOUR_TELNYX_API_KEY")

clone = client.voice_clones.create_from_upload(
    params={
        "audio_file": open("recording.wav", "rb"),
        "name": "My Custom Voice",
        "language": "en",
        "gender": "female",
        "provider": "minimax",
    }
)

print("Voice Clone Created:", clone.data)
```

Node.js

```javascript
import Telnyx from 'telnyx';
import fs from 'fs';

const client = new Telnyx({ apiKey: 'YOUR_TELNYX_API_KEY' });

const clone = await client.voiceClones.createFromUpload({
  params: {
    audio_file: fs.createReadStream('recording.wav'),
    name: 'My Custom Voice',
    language: 'en',
    gender: 'female',
    provider: 'minimax',
  },
});

console.log('Voice Clone Created:', clone.data);
```

**Clone with Ultra model**

Ultra clones return `202 Accepted` and require polling until the status is `active`.

Python

```python
import telnyx
import time

client = telnyx.Telnyx(api_key="YOUR_TELNYX_API_KEY")

# Create the clone (returns 202 Accepted)
clone = client.voice_clones.create_from_upload(
    params={
        "audio_file": open("recording.wav", "rb"),
        "name": "My Ultra Voice",
        "language": "en",
        "gender": "female",
        "provider": "telnyx",
        "model_id": "Ultra",
    }
)

print("Clone submitted:", clone.data.id, "— status:", clone.data.status)

# Poll until active
while True:
    clones = client.voice_clones.list()
    for c in clones:
        if c.id == clone.data.id:
            if c.status == "active":
                print("Clone ready!")
                break
    else:
        time.sleep(5)
        continue
    break
```

Node.js

```javascript
import Telnyx from 'telnyx';
import fs from 'fs';

const client = new Telnyx({ apiKey: 'YOUR_TELNYX_API_KEY' });

// Create the clone (returns 202 Accepted)
const clone = await client.voiceClones.createFromUpload({
  params: {
    audio_file: fs.createReadStream('recording.wav'),
    name: 'My Ultra Voice',
    language: 'en',
    gender: 'female',
    provider: 'telnyx',
    model_id: 'Ultra',
  },
});

console.log('Clone submitted:', clone.data.id, '— status:', clone.data.status);

// Poll until active
while (true) {
  const clones = await client.voiceClones.list();
  const found = clones.data.find((c) => c.id === clone.data.id);
  if (found?.status === 'active') {
    console.log('Clone ready!');
    break;
  }
  await new Promise((r) => setTimeout(r, 5000));
}
```

### Clone API parameters

**Models** — set via `model_id` (body) on `POST /v2/voice_clones/from_upload`, or use `provider` (body) to select Minimax.

| Model | Provider | Audio length | Max file | Sync/Async | Best for |
| --- | --- | --- | --- | --- | --- |
| Qwen3TTS | Telnyx (default) | 3–15s (auto-trimmed to 10s) | 5 MB | Sync (201) | Short, clean samples |
| Ultra | Telnyx | Up to 10s | 5 MB | **Async (202)** | Higher quality, more natural |
| speech-2.8-turbo | Minimax | 10s–5 min | 20 MB | Sync (201) | Longer recordings, more vocal range |

**Audio requirements** — body parameter `audio_file` (multipart) on `POST /v2/voice_clones/from_upload`.

|  | Qwen3TTS | Ultra | Minimax |
| --- | --- | --- | --- |
| Audio length | 3–15s (5–10s optimal) | Up to 10s | 10s–5 min |
| Max file size | 5 MB | 5 MB | 20 MB |
| Formats | WAV, MP3, FLAC, OGG, M4A | Same | Same |

- **Qwen3TTS:** aim for 5–10 seconds. Longer isn't better — auto-trims to 10s.
- **Minimax:** longer is better. 1–2 minutes of varied speech gives more vocal range.

**The `ref_text` parameter** — body parameter on `POST /v2/voice_clones/from_upload`. Optional. A transcript of what's being said in the audio. Improves clone quality by giving the model a text reference to align against.

**Ultra async flow** — when `model_id` is `"Ultra"`, the API returns **202 Accepted** instead of 201:

```
POST /v2/voice_clones/from_upload → 202 { "data": { "status": "pending" } }
```

Poll until ready:

```
GET /v2/voice_clones/{id} → 200 { "data": { "status": "active" } }
```

### Responses

**Voice ID format** — every clone response includes fields to construct the voice ID: `{Provider}.{Model}.{provider_voice_id}`

| Provider | `provider_voice_id` value |
| --- | --- |
| Telnyx Qwen3TTS | Equals the clone's UUID (`id` field) |
| Telnyx Ultra | Cartesia-assigned voice ID |
| Minimax | Minimax-assigned ID (encoded format) |

**Clone status**

| Status | Meaning |
| --- | --- |
| `active` | Ready to use |
| `pending` | Being processed (Ultra only — poll until active) |
| `failed` | Processing failed |
| `expired` | Voice was not kept alive |

Qwen3TTS and Minimax clones are always `active` on creation.

### Errors

**General errors** — these errors apply to all providers.

| Endpoint | Status | Code | Detail |
| --- | --- | --- | --- |
| `show` | **404** | `10005` | Clone not found or invalid UUID |
| `create` | **404** | `10005` | Voice design not found / no version |
| `create` | **409** | `10012` | Duplicate `provider_voice_id` |
| `create` | **422** | `10027` | Changeset validation (see below) |
| `create_from_upload` | **422** | `10027` | `audio_file is required` |
| `create_from_upload` | **422** | `10027` | `File too large. Maximum allowed size is 5MB` (20MB for Minimax) |
| `create_from_upload` | **400** | `10015` | `Failed to process audio file: <reason>` (FFmpeg failure) |
| `create_from_upload` | **422** | `10027` | Invalid `provider`+`model_id` combination |
| `update` | **404** | `10005` | Clone not found |
| `update` | **422** | `10027` | Changeset validation errors |
| `delete` | **404** | `10005` | Clone not found |
| `sample` | **404** | `10005` | Clone or sample not found |

**Telnyx / Cartesia errors**

| Status | Code | Detail | Provider |
| --- | --- | --- | --- |
| **422** | `10027` | Pattern-matched messages (voice not found, audio too short/long, bad quality, unsupported format, unsupported language, invalid params, text length invalid) | Telnyx/Cartesia |
| **429** | `10011` | `Provider rate limit exceeded` | All providers |

**Minimax errors**

| Status | Code | Detail | Provider |
| --- | --- | --- | --- |
| **422** | `10038` | `Audio is too short (min 10s)` | Minimax (code 2037) |
| **422** | `10038` | `Audio is too long` | Minimax (code 2038) |
| **422** | `10038` | `Audio quality too low` | Minimax (code 2039) |
| **422** | `10038` | `Audio contains too much noise` | Minimax (code 2048) |
| **422** | `10038` | `Voice cloning provider error: <msg>` | Minimax (other codes) |
| **500** | `10037` | `Voice clone service configuration error` | Auth misconfiguration detected |
| **502** | `10037` | `Voice clone service unavailable` | Upstream error or connection failure |
