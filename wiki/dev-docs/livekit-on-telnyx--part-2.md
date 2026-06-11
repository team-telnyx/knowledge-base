---
title: LiveKit on Telnyx
summary: LiveKit on Telnyx is a platform for deploying real-time voice AI agents with
  integrated telephony, AI models (STT, TTS, LLM), and observability — all billed
  on a single Telnyx invoice with no third-party SIP fees.
sources:
- url: https://developers.telnyx.com/docs/livekit/models/index
- url: https://developers.telnyx.com/docs/livekit/models/llm
- url: https://developers.telnyx.com/docs/livekit/models/stt
- url: https://developers.telnyx.com/docs/livekit/models/tts
- url: https://developers.telnyx.com/docs/livekit/observability/index
- url: https://developers.telnyx.com/docs/livekit/pricing
- url: https://developers.telnyx.com/docs/livekit/quickstart
- url: https://developers.telnyx.com/docs/livekit/regions
- url: https://developers.telnyx.com/docs/livekit/telephony
updated_at: 2026-06-11T10:34:33Z
---

# LiveKit on Telnyx

*Part 2 of 2 — see also: [Part 1](livekit-on-telnyx--part-1.md)*

LiveKit on Telnyx is a platform for deploying real-time voice AI agents with integrated telephony, AI models (STT, TTS, LLM), and observability — all billed on a single Telnyx invoice with no third-party SIP fees.

## AI Models

All models are accessed through the [Telnyx plugin](https://github.com/team-telnyx/telnyx-livekit-plugin) and run on Telnyx GPUs, giving you on-prem inference without managing infrastructure — whether you're using the plugin from LiveKit Cloud or deployed on the Telnyx platform.

### Speech-to-Text (STT)

Telnyx hosts Deepgram models on dedicated GPUs. Access them through the Telnyx plugin:

```python
from livekit.plugins import telnyx

stt = telnyx.deepgram.STT(model="nova-3", language="en")
```

The plugin provides two STT classes:

- **`telnyx.deepgram.STT`** — Recommended. Connects to Deepgram models hosted on Telnyx GPUs. Takes a `model` parameter.
- **`telnyx.STT`** — Connects to Telnyx's own transcription engine (default) or Deepgram via `transcription_engine="Deepgram"`. Takes a `transcription_engine` parameter instead of `model`.

**Available models:**

- **Nova-3 (recommended)** — Latest generation, best accuracy. Supports `keyterm` for keyword boosting.
- **Nova-2** — Previous generation, stable and reliable. Uses weighted keyword boosting via `keywords`.
- **Flux** — Experimental, with built-in end-of-turn detection designed for real-time voice agents. Supports `keyterm`, `eot_threshold`, `eot_timeout_ms`, and `eager_eot_threshold`.

**Parameters:**

| Parameter | Default | Description |
|---|---|---|
| `model` | `nova-3` | Model to use (`nova-3`, `nova-2`, `flux`) |
| `language` | `en` | Language code |
| `interim_results` | `True` | Stream partial transcriptions |
| `keyterm` | — | Keyword boosting (Nova-3, Flux) |
| `keywords` | — | Weighted keyword boosting (Nova-2) |
| `eot_threshold` | — | End-of-turn confidence threshold (Flux only) |
| `eot_timeout_ms` | — | End-of-turn timeout in ms (Flux only) |
| `eager_eot_threshold` | — | Eager end-of-turn threshold (Flux only) |

### Text-to-Speech (TTS)

Telnyx offers an extensive library of voices across multiple providers and models with broad language and accent support:

```python
from livekit.plugins import telnyx

tts = telnyx.TTS(voice="Telnyx.NaturalHD.astra")
```

Voice IDs follow the pattern `Provider.Model.voice_name`. Browse the [voice library](https://developers.telnyx.com/docs/tts-stt/tts-available-voices/index) to find a voice, copy its ID, and pass it to `telnyx.TTS(voice="...")`.

**Available providers and models:**

| Provider | Models |
|---|---|
| **Telnyx** | NaturalHD, Ultra |
| **MiniMax** | speech-02-turbo, speech-2.6-turbo, speech-2.8-turbo |
| **Rime** | ArcanaV3, KokoroTTS |
| **AWS** | Polly (Neural voices) |
| **Azure** | Neural voices |
| **Inworld** | Coming soon |
| **ResembleAI** | Coming soon |

**Telnyx Ultra** is the highest-fidelity voice, available exclusively for agents deployed on LiveKit on Telnyx (not through the plugin alone).

**Parameters:**

| Parameter | Default | Description |
|---|---|---|
| `voice` | — | Voice ID (e.g. `Telnyx.NaturalHD.astra`) |
| `sample_rate` | `16000` | Audio sample rate in Hz |

### Large Language Models (LLM)

Telnyx hosts models with an OpenAI-compatible API — no concurrency limits. Use the standard OpenAI plugin with the `.with_telnyx()` helper:

```python
from livekit.plugins import openai

llm = openai.LLM.with_telnyx(model="zai-org/GLM-5.1-FP8")
```

`.with_telnyx()` is a built-in static method on `openai.LLM` in the official [`livekit-plugins-openai`](https://pypi.org/project/livekit-plugins-openai/) package, maintained by LiveKit. It works the same as other OpenAI-compatible helpers (`.with_azure()`, `.with_fireworks()`, etc.): it sets `base_url` to `https://api.telnyx.com/v2/ai/openai` and reads your `TELNYX_API_KEY` from the environment. No additional packages beyond `livekit-plugins-openai` are needed.

**Hosted models** (no external API key needed, just `TELNYX_API_KEY`):

| Model | Description |
|---|---|
| `moonshotai/Kimi-K2.6` | Moonshot AI — voice AI, with thinking disabled (Recommended) |
| `zai-org/GLM-5.1-FP8` | Zhipu AI — most efficient reasoning, function calling |
| `MiniMaxAI/MiniMax-M2.7` | MiniMax — cheapest, high intelligence |

**Proprietary models (BYOK)** — For models like GPT-4o or Claude, Telnyx proxies the request using your own API key. Add your provider key in the [Telnyx Portal](https://portal.telnyx.com) under Inference settings:

```python
llm = openai.LLM.with_telnyx(model="openai/gpt-4o-mini")
```

See the [full models list](https://developers.telnyx.com/docs/inference/models) for all available options.

## Observability

### Agent logs

Stream logs from your running agent via the CLI:

```bash
lk agent logs <agent-id>
```

This gives you stdout/stderr from your agent in real time — same as LiveKit Cloud's log access.

### Coming soon

Traces, metrics, and session debugging are on the roadmap.

## Pricing

All services — compute, models, and telephony — are billed on a single Telnyx invoice. On other platforms you pay third-party SIP fees on top of usage; on Telnyx those are gone entirely.

- **STT**: See [telnyx.com/pricing/speech-to-text](https://telnyx.com/pricing/speech-to-text)
- **TTS**: See [telnyx.com/pricing/text-to-speech](https://telnyx.com/pricing/text-to-speech)
- **LLM**: See [telnyx.com/pricing/conversational-ai](https://telnyx.com/pricing/conversational-ai)
