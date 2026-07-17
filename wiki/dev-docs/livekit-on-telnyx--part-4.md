---
title: LiveKit on Telnyx
summary: Telnyx LiveKit is a managed platform for deploying voice AI agents at scale,
  combining LiveKit's agent framework with built-in telephony, colocated AI inference
  on Telnyx GPUs, and managed infrastructure across multiple regions. This page covers
  architecture, compatibility, regions, quickstart, build, deploy, models (STT/TTS/LLM),
  telephony, observability, limits, pricing, and migration from LiveKit Cloud or self-hosted.
sources:
- url: https://developers.telnyx.com/docs/livekit/architecture
- url: https://developers.telnyx.com/docs/livekit/build/index
- url: https://developers.telnyx.com/docs/livekit/compatibility
- url: https://developers.telnyx.com/docs/livekit/connect
- url: https://developers.telnyx.com/docs/livekit/deploy/configuration
- url: https://developers.telnyx.com/docs/livekit/deploy/index
- url: https://developers.telnyx.com/docs/livekit/deploy/management
- url: https://developers.telnyx.com/docs/livekit/deploy/secrets
- url: https://developers.telnyx.com/docs/livekit/index
- url: https://developers.telnyx.com/docs/livekit/limits
- url: https://developers.telnyx.com/docs/livekit/migration/from-livekit-cloud
- url: https://developers.telnyx.com/docs/livekit/migration/from-self-hosted
- url: https://developers.telnyx.com/docs/livekit/models/index
- url: https://developers.telnyx.com/docs/livekit/models/llm
- url: https://developers.telnyx.com/docs/livekit/models/stt
- url: https://developers.telnyx.com/docs/livekit/models/tts
- url: https://developers.telnyx.com/docs/livekit/observability/index
- url: https://developers.telnyx.com/docs/livekit/pricing
- url: https://developers.telnyx.com/docs/livekit/quickstart
- url: https://developers.telnyx.com/docs/livekit/regions
- url: https://developers.telnyx.com/docs/livekit/telephony
updated_at: 2026-07-17T09:14:35Z
---

# LiveKit on Telnyx

*Part 4 of 6 — see also: [Part 1](livekit-on-telnyx--part-1.md), [Part 2](livekit-on-telnyx--part-2.md), [Part 3](livekit-on-telnyx--part-3.md), [Part 5](livekit-on-telnyx--part-5.md), [Part 6](livekit-on-telnyx--part-6.md)*

Telnyx LiveKit is a managed platform for deploying voice AI agents at scale, combining LiveKit's agent framework with built-in telephony, colocated AI inference on Telnyx GPUs, and managed infrastructure across multiple regions. This page covers architecture, compatibility, regions, quickstart, build, deploy, models (STT/TTS/LLM), telephony, observability, limits, pricing, and migration from LiveKit Cloud or self-hosted.

## Models

All models are accessed through the Telnyx plugin. Models run on Telnyx GPUs, so whether you're using the plugin from LiveKit Cloud or deployed on the Telnyx platform, you get on-prem inference without managing infrastructure.

### Speech-to-Text (STT)

Telnyx hosts Deepgram models on dedicated GPUs. Access them through the Telnyx plugin:

```
from livekit.plugins import telnyx

stt = telnyx.deepgram.STT(model="nova-3", language="en")
```

The plugin provides two STT classes:

- **`telnyx.deepgram.STT`** — Recommended. Connects to Deepgram models hosted on Telnyx GPUs. Takes a `model` parameter (`nova-3`, `nova-2`, `flux`).
- **`telnyx.STT`** — Connects to Telnyx's own transcription engine (default) or Deepgram via `transcription_engine="Deepgram"`. Takes a `transcription_engine` parameter instead of `model`.

For most use cases, `telnyx.deepgram.STT` is the simpler interface. [Plugin source on GitHub](https://github.com/team-telnyx/telnyx-livekit-plugin).

**Nova-3 (recommended).** Latest generation, best accuracy.

```
stt = telnyx.deepgram.STT(
    model="nova-3",
    language="en",
    interim_results=True,
    keyterm=["YourBrand", "custom-term"],  # keyword boosting
)
```

**Nova-2.** Previous generation, stable and reliable. Uses weighted keyword boosting.

```
stt = telnyx.deepgram.STT(
    model="nova-2",
    language="en",
    interim_results=True,
    keywords=["YourBrand:2.0", "custom-term:1.5"],
)
```

**Flux.** Experimental, with built-in end-of-turn detection. Designed for real-time voice agents.

```
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

Parameters:

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

### Text-to-Speech (TTS)

Telnyx offers an extensive library of voices across multiple providers and models, with broad language and accent support. Access them through the Telnyx plugin:

```
from livekit.plugins import telnyx

tts = telnyx.TTS(voice="Telnyx.NaturalHD.astra")
```

Voice IDs follow the pattern `Provider.Model.voice_name`. To find a voice:

1. Browse the [voice library](https://developers.telnyx.com/docs/tts-stt/tts-available-voices/index)
2. Copy the voice ID (e.g. `Telnyx.NaturalHD.astra`)
3. Pass it to `telnyx.TTS(voice="...")`

Examples:

```
# Telnyx Natural HD
tts = telnyx.TTS(voice="Telnyx.NaturalHD.astra")

# MiniMax Speech 2.8 Turbo
tts = telnyx.TTS(voice="MiniMax.speech-2.8-turbo.Narrator")

# Rime Arcana V3
tts = telnyx.TTS(voice="Rime.ArcanaV3.astra")
```

Available providers and models:

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

Parameters:

| Parameter | Default | Description |
| --- | --- | --- |
| `voice` | — | Voice ID (e.g. `Telnyx.NaturalHD.astra`) |
| `sample_rate` | `16000` | Audio sample rate in Hz |

### Large Language Models (LLM)

Telnyx hosts models with an OpenAI-compatible API. No concurrency limits. Use the standard OpenAI plugin with the `.with_telnyx()` helper:

```
from livekit.plugins import openai

llm = openai.LLM.with_telnyx(model="zai-org/GLM-5.2")
```

`.with_telnyx()` is a built-in static method on `openai.LLM` in the official [`livekit-plugins-openai`](https://pypi.org/project/livekit-plugins-openai/) package, maintained by LiveKit — not a Telnyx package or fork. It works the same way as the other OpenAI-compatible helpers in that package (`.with_azure()`, `.with_fireworks()`, etc.): it sets `base_url` to Telnyx's OpenAI-compatible inference endpoint (`https://api.telnyx.com/v2/ai/openai`) and reads your `TELNYX_API_KEY` from the environment. You don't need any additional packages beyond `livekit-plugins-openai`.

Hosted models — these run on Telnyx infrastructure, no external API key needed, just your `TELNYX_API_KEY`:

| Model | Description |
| --- | --- |
| `moonshotai/Kimi-K2.6` | Moonshot AI — voice AI, with thinking disabled **(Recommended)** |
| `zai-org/GLM-5.2` | Zhipu AI — most efficient reasoning, function calling |
| `MiniMaxAI/MiniMax-M3-MXFP8` | MiniMax — cheapest, high intelligence |

Proprietary models (BYOK) — for models like GPT-4o or Claude, Telnyx proxies the request using your own API key. Add your provider key in the [Telnyx Portal](https://portal.telnyx.com) under Inference settings.

```
# Proprietary model via BYOK (bring your own key)
llm = openai.LLM.with_telnyx(model="openai/gpt-4o-mini")
```

See the [full models list](https://developers.telnyx.com/docs/inference/models).

## Deploy

Same commands as LiveKit Cloud. `lk agent deploy` uploads your code, builds a container image on Telnyx's build service, and deploys the worker.

### 1. Create your agent

```
lk agent create .
```

Registers the agent and writes the agent ID to `livekit.toml`. Skip this if you've already created the agent.

### 2. Deploy

```
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
```

Subsequent deploys roll out a new version.

### 3. Check status

```
lk agent list
```

### 4. Tail logs

```
lk agent logs --id <AGENT_ID>
```

For build logs:

```
lk agent logs --id <AGENT_ID> --log-type build
```

### 5. Update secrets

Add or update secrets on a running agent:

```
lk agent update-secrets <AGENT_ID> --secrets "OPENAI_API_KEY=<your-key>"
```

### 6. Rollback

```
lk agent rollback <AGENT_ID>
```

### What gets auto-injected

The platform injects these into your agent's environment at runtime — you don't need to set them manually:

- `LIVEKIT_URL`
- `LIVEKIT_API_KEY` — your Telnyx API key
- `LIVEKIT_API_SECRET`

## Deploy configuration

### Regions

Deploy to the region closest to your users. See [Regions](regions.md) for all available endpoints.

### Environment variables and livekit.toml

Set `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET` as environment variables. You also need a `livekit.toml` in your project directory that defines the subdomain and agent ID:

```
[project]
subdomain = "nyc1"

[agent]
id = "<agent-id>"
```

`lk agent create` writes the agent ID to `livekit.toml`. Don't edit the `[agent]` section manually. If you clone an example repo, remove the `[agent]` section before running `lk agent create` so a fresh ID is generated.

For multi-agent projects, use the `--config` flag to point at different TOML files:

```
lk agent deploy . --config agent-a.toml
lk agent deploy . --config agent-b.toml
```

### Multiple environments

Use separate API keys for dev, staging, and production environments. Each key operates independently.

### Log access

Stream logs from your running agent:

```
lk agent logs <agent-id>
```

Log forwarding to third-party services (Datadog, Sentry, CloudWatch) is coming soon.
