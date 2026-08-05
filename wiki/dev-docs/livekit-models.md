---
title: LiveKit Models
summary: Overview of the AI models available through the Telnyx LiveKit plugin, covering
  speech-to-text, text-to-speech, and large language model options hosted on Telnyx
  infrastructure.
sources:
- url: https://developers.telnyx.com/docs/livekit/models/index
- url: https://developers.telnyx.com/docs/livekit/models/llm
- url: https://developers.telnyx.com/docs/livekit/models/stt
- url: https://developers.telnyx.com/docs/livekit/models/tts
updated_at: 2026-08-05T13:47:47Z
---

# LiveKit Models

Overview of the AI models available through the Telnyx LiveKit plugin, covering speech-to-text, text-to-speech, and large language model options hosted on Telnyx infrastructure.

## Overview

All models are accessed through the [Telnyx plugin](telnyx-plugin.md). Models run on Telnyx GPUs, so whether you're using the plugin from LiveKit Cloud or deployed on the Telnyx platform, you get on-prem inference without managing infrastructure.

## Speech-to-Text

Telnyx hosts Deepgram models on dedicated GPUs. Access them through the Telnyx plugin:

```python
from livekit.plugins import telnyx

stt = telnyx.deepgram.STT(model="nova-3", language="en")
```

The plugin provides two STT classes:

- **`telnyx.deepgram.STT`** — Recommended. Connects to Deepgram models hosted on Telnyx GPUs. Takes a `model` parameter (`nova-3`, `nova-2`, `flux`).
- **`telnyx.STT`** — Connects to Telnyx's own transcription engine (default) or Deepgram via `transcription_engine="Deepgram"`. Takes a `transcription_engine` parameter instead of `model`.

For most use cases, `telnyx.deepgram.STT` is the simpler interface.

### Available models

#### Nova-3 (recommended)

Latest generation, best accuracy.

```python
stt = telnyx.deepgram.STT(
    model="nova-3",
    language="en",
    interim_results=True,
    keyterm=["YourBrand", "custom-term"],  # keyword boosting
)
```

#### Nova-2

Previous generation, stable and reliable. Uses weighted keyword boosting.

```python
stt = telnyx.deepgram.STT(
    model="nova-2",
    language="en",
    interim_results=True,
    keywords=["YourBrand:2.0", "custom-term:1.5"],
)
```

#### Flux

Experimental, with built-in end-of-turn detection. Designed for real-time voice agents.

```python
stt = telnyx.deepgram.STT(
    model="flux",
    language="en",
    interim_results=True,
    keyterm=["YourBrand", "custom-term"],
    eot_threshold=0.5,
    eot_timeout_ms=3000,
    eager_eot_threshold=0.3,
)
```

### Parameters

| Parameter | Default | Description |
| --- | --- | --- |
| `model` | `nova-3` | Model to use (`nova-3`, `nova-2`, `flux`) |
| `language` | `en` | Language code |
| `interim_results` | `True` | Stream partial transcriptions |
| `keyterm` | — | Keyword boosting (Nova-3, Flux) |
| `keywords` | — | Weighted keyword boosting (Nova-2) |
| `eot_threshold` | — | End-of-turn confidence threshold (Flux only) |
| `eot_timeout_ms` | — | End-of-turn timeout in ms (Flux only) |
| `eager_eot_threshold` | — | Eager end-of-turn threshold (Flux only) |

See the [plugin source on GitHub](https://github.com/team-telnyx/telnyx-livekit-plugin).

## Text-to-Speech

Telnyx offers an extensive library of voices across multiple providers and models, with broad language and accent support. Access them through the Telnyx plugin:

```python
from livekit.plugins import telnyx

tts = telnyx.TTS(voice="Telnyx.NaturalHD.astra")
```

### Voice ID format

Voice IDs follow the pattern `Provider.Model.voice_name`. To find a voice:

1. Browse the [voice library](https://developers.telnyx.com/docs/tts-stt/tts-available-voices/index)
2. Copy the voice ID (e.g. `Telnyx.NaturalHD.astra`)
3. Pass it to `telnyx.TTS(voice="...")`

### Examples

```python
# Telnyx Natural HD
tts = telnyx.TTS(voice="Telnyx.NaturalHD.astra")

# MiniMax Speech 2.8 Turbo
tts = telnyx.TTS(voice="MiniMax.speech-2.8-turbo.Narrator")

# Rime Arcana V3
tts = telnyx.TTS(voice="Rime.ArcanaV3.astra")
```

### Available providers and models

| Provider | Models |
| --- | --- |
| **Telnyx** | NaturalHD, Ultra |
| **MiniMax** | speech-02-turbo, speech-2.6-turbo, speech-2.8-turbo |
| **Rime** | ArcanaV3, KokoroTTS |
| **AWS** | Polly (Neural voices) |
| **Azure** | Neural voices |
| **Inworld** | Coming soon |
| **ResembleAI** | Coming soon |

Browse all voices and models in the [voice library](https://developers.telnyx.com/docs/tts-stt/tts-available-voices/index).

### Parameters

| Parameter | Default | Description |
| --- | --- | --- |
| `voice` | — | Voice ID (e.g. `Telnyx.NaturalHD.astra`) |
| `sample_rate` | `16000` | Audio sample rate in Hz |

## Large Language Models

Telnyx hosts models with an OpenAI-compatible API. No concurrency limits. Use the standard OpenAI plugin with the `.with_telnyx()` helper:

```python
from livekit.plugins import openai

llm = openai.LLM.with_telnyx(model="zai-org/GLM-5.2")
```

### About `.with_telnyx()`

This is a built-in static method on `openai.LLM` in the official [`livekit-plugins-openai`](https://pypi.org/project/livekit-plugins-openai/) package, maintained by LiveKit — not a Telnyx package or fork. It works the same way as the other OpenAI-compatible helpers in that package (`.with_azure()`, `.with_fireworks()`, etc.): it sets `base_url` to Telnyx's OpenAI-compatible inference endpoint (`https://api.telnyx.com/v2/ai/openai`) and reads your `TELNYX_API_KEY` from the environment. You don't need any additional packages beyond `livekit-plugins-openai`.

### Hosted models

These run on Telnyx infrastructure — no external API key needed, just your `TELNYX_API_KEY`:

| Model | Description |
| --- | --- |
| `moonshotai/Kimi-K3` | Moonshot AI — state-of-the-art open-weight intelligence, native vision, 1M context |
| `moonshotai/Kimi-K2.6` | Moonshot AI — voice AI, with thinking disabled **(Recommended)** |
| `zai-org/GLM-5.2` | Zhipu AI — most efficient reasoning, function calling |
| `MiniMaxAI/MiniMax-M3-MXFP8` | MiniMax — cheapest, high intelligence |

### Proprietary models (BYOK)

For models like GPT-4o or Claude, Telnyx proxies the request using your own API key. Add your provider key in the [Telnyx Portal](https://portal.telnyx.com) under Inference settings.

| Model | Provider | Description |
| --- | --- | --- |
| `openai/gpt-5.4-mini` | OpenAI | Compact high-efficiency model for production voice workflows |
| `openai/gpt-4o` | OpenAI | Multimodal flagship model |

```python
# Proprietary model via BYOK (bring your own key)
llm = openai.LLM.with_telnyx(model="openai/gpt-5.4-mini")
```

See the [full models list](https://developers.telnyx.com/docs/inference/models).
