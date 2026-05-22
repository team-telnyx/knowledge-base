---
title: LiveKit models overview
summary: Access STT, TTS, and LLMs for real-time voice agents through the Telnyx plugin
  and an OpenAI-compatible endpoint. Models run on Telnyx GPUs for on-prem inference
  whether you deploy on Telnyx or use LiveKit Cloud, with single-invoice billing across
  compute, models, and telephony.
sources:
- url: https://developers.telnyx.com/docs/livekit/models/index
  content_hash: 837c3552237dfed439c540a7a0f1691a463c5990d99f2e07d7fbd19cad025a54
- url: https://developers.telnyx.com/docs/livekit/models/llm
  content_hash: 19f40b74c03a3cfd98fd4e06105858dcea0a89ef070f567b263ec8c00a2576e0
- url: https://developers.telnyx.com/docs/livekit/models/stt
  content_hash: 66c3f00fdbb726fadc15b70898ff803d3ea37c7c7754e109904fc9c6812e507c
- url: https://developers.telnyx.com/docs/livekit/models/tts
  content_hash: 91d71bc860439178ef397be4faff35ebf393cb184011ec3c198a0458166c2ab9
- url: https://developers.telnyx.com/docs/livekit/telephony
  content_hash: 2031d644a628f9c2281b2ac595fb2220a4eddf8a65e481b974160cf34fc96480
- url: https://developers.telnyx.com/docs/livekit/pricing
  content_hash: a1347ef53af38228e0e522215600ae969a4472364954425bef6b1475596cf6cd
updated_at: 2026-05-20T08:54:34Z
---

# LiveKit models overview

Access STT, TTS, and LLMs for real-time voice agents through the Telnyx plugin and an OpenAI-compatible endpoint. Models run on Telnyx GPUs for on-prem inference whether you deploy on Telnyx or use LiveKit Cloud, with single-invoice billing across compute, models, and telephony.

## How to access models

- All models are available via the Telnyx plugin for LiveKit. You get GPU-hosted inference on Telnyx without running your own infrastructure.
- Works from both LiveKit Cloud and LiveKit on Telnyx deployments.
- LLMs are exposed via an OpenAI-compatible API with no concurrency limits. Use the official LiveKit OpenAI plugin helper and your TELNYX_API_KEY.

Examples:

```python
# STT / TTS via Telnyx plugin
from livekit.plugins import telnyx

# STT (Deepgram models hosted on Telnyx GPUs)
stt = telnyx.deepgram.STT(model="nova-3", language="en")

# TTS (choose any supported voice)
tts = telnyx.TTS(voice="Telnyx.NaturalHD.astra")
```

```python
# LLM via OpenAI-compatible helper (maintained by LiveKit)
from livekit.plugins import openai

llm = openai.LLM.with_telnyx(model="moonshotai/Kimi-K2.6")
```

Notes:
- `.with_telnyx()` sets base_url to Telnyx’s OpenAI-compatible endpoint (https://api.telnyx.com/v2/ai/openai) and reads TELNYX_API_KEY from the environment. No extra packages beyond `livekit-plugins-openai` are required.

## Speech-to-Text (STT)

Telnyx hosts Deepgram models (Nova-3, Nova-2, Flux) on dedicated GPUs. Use the Telnyx plugin:

```python
from livekit.plugins import telnyx

# Recommended: direct Deepgram models hosted on Telnyx GPUs
a = telnyx.deepgram.STT(model="nova-3", language="en")

# Alternative: Telnyx STT wrapper (or Deepgram via transcription_engine)
b = telnyx.STT(transcription_engine="Deepgram")
```

- telnyx.deepgram.STT — Recommended. Parameters include `model` (nova-3, nova-2, flux), `language`, `interim_results`, `keyterm`/`keywords`, and Flux-specific end-of-turn (EOT) controls.
- telnyx.STT — Uses Telnyx’s engine by default or Deepgram via `transcription_engine="Deepgram"`.

Available models and examples:
- Nova-3 (recommended): best accuracy
```python
stt = telnyx.deepgram.STT(
    model="nova-3", language="en", interim_results=True,
    keyterm=["YourBrand", "custom-term"],  # keyword boosting
)
```
- Nova-2: stable, weighted keyword boosting
```python
stt = telnyx.deepgram.STT(
    model="nova-2", language="en", interim_results=True,
    keywords=["YourBrand:2.0", "custom-term:1.5"],
)
```
- Flux: experimental, built-in EOT for real-time agents
```python
stt = telnyx.deepgram.STT(
    model="flux", language="en", interim_results=True,
    keyterm=["YourBrand", "custom-term"],
    eot_threshold=0.5, eot_timeout_ms=3000, eager_eot_threshold=0.3,
)
```

Key parameters:
- model (default nova-3): nova-3 | nova-2 | flux
- language (default en)
- interim_results (default True)
- keyterm (Nova-3, Flux) | keywords (Nova-2)
- Flux-only: eot_threshold, eot_timeout_ms, eager_eot_threshold

See also: [Speech-to-Text (STT)](speech-to-text-stt.md)

## Text-to-Speech (TTS)

A wide voice library across multiple providers and models with broad language and accent support:

```python
from livekit.plugins import telnyx

tts = telnyx.TTS(voice="Telnyx.NaturalHD.astra")
```

Voice ID format: `Provider.Model.voice_name`.
- Browse voices: https://developers.telnyx.com/docs/tts-stt/tts-available-voices/index
- Copy a voice ID (e.g., `Telnyx.NaturalHD.astra`) and pass to `telnyx.TTS(voice=...)`.

Examples:
```python
# Telnyx Natural HD
tts = telnyx.TTS(voice="Telnyx.NaturalHD.astra")
# MiniMax Speech 2.8 Turbo
tts = telnyx.TTS(voice="MiniMax.speech-2.8-turbo.Narrator")
# Rime Arcana V3
tts = telnyx.TTS(voice="Rime.ArcanaV3.astra")
```

Supported providers and models (highlights):
- Telnyx: NaturalHD, Ultra
- MiniMax: speech-02-turbo, speech-2.6-turbo, speech-2.8-turbo
- Rime: ArcanaV3, KokoroTTS
- AWS: Polly (Neural)
- Azure: Neural
- Inworld: coming soon
- ResembleAI: coming soon

Parameters:
- voice (required): e.g., Telnyx.NaturalHD.astra
- sample_rate (default 16000 Hz)

Platform-exclusive: Telnyx Ultra voices are available only for agents deployed on LiveKit on Telnyx (not via the plugin alone). See the voice library for options.

See also: [Text-to-Speech (TTS)](text-to-speech-tts.md)

## Large Language Models (LLM)

Use the OpenAI-compatible helper from `livekit-plugins-openai`:

```python
from livekit.plugins import openai

# Hosted model (no external key needed)
llm = openai.LLM.with_telnyx(model="moonshotai/Kimi-K2.6")
```

About `.with_telnyx()`:
- Static method provided by the official LiveKit `livekit-plugins-openai` package (not a Telnyx fork).
- Configures `base_url=https://api.telnyx.com/v2/ai/openai` and reads TELNYX_API_KEY from the environment.

Hosted models (run on Telnyx; only TELNYX_API_KEY required):
- moonshotai/Kimi-K2.6 — voice AI, thinking disabled (recommended)
- zai-org/GLM-5.1-FP8 — efficient reasoning, function calling
- MiniMaxAI/MiniMax-M2.7 — lowest cost, high intelligence

Proprietary models via BYOK:
- Add your provider key in the Telnyx Portal (Inference settings): https://portal.telnyx.com
```python
llm = openai.LLM.with_telnyx(model="openai/gpt-4o-mini")
```

Full model list: https://developers.telnyx.com/docs/inference/models

See also: [Large Language Models (LLM)](large-language-models-llm.md)

## Telephony integration highlights

Telnyx is the carrier — buy a number and connect it to your agent with no third-party SIP setup. Calls route on-net from Telnyx SIP directly to your agent.

Supported:
- Inbound calls via SIP dispatch rules (DID → LiveKit SIP → your agent)
- Outbound calls using the `lk` CLI:
```bash
lk sip participant create \
  --room "my-room" \
  --trunk "<SIP_TRUNK_ID>" \
  --call "+15551234567" \
  --identity "outbound-caller"
```
- DTMF via RFC 2833/4733 (delivered to your agent as events)
- SIP headers to participant attributes via `headers_to_attributes`
- HD voice codecs: G.722 (16 kHz, default) and Opus (48 kHz; requires SRTP and enabling Opus on your Telnyx SIP connection; set `media_encryption: ALLOW` on the LiveKit inbound trunk). Opus is preferred when available.

Not yet supported (roadmap; requires Enterprise SIP):
- Call transfers (REFER / warm transfer)

See also: [LiveKit on Telnyx telephony](livekit-on-telnyx-telephony.md) and [LiveKit on Telnyx Quick Start](livekit-on-telnyx-quick-start.md)

## Pricing and billing

- Single Telnyx invoice for compute, models, and telephony (no third‑party SIP fees on top).
- STT pricing: https://telnyx.com/pricing/speech-to-text
- TTS pricing: https://telnyx.com/pricing/text-to-speech
- LLM pricing: https://telnyx.com/pricing/conversational-ai
- Telnyx Ultra voices are platform-exclusive for LiveKit on Telnyx deployments.

See also: [LiveKit on Telnyx pricing](livekit-on-telnyx-pricing.md)

## See also

- [Build with the Telnyx plugin](build-with-the-telnyx-plugin.md)
- [LiveKit on Telnyx observability](livekit-on-telnyx-observability.md)
- [LiveKit on Telnyx architecture](livekit-on-telnyx-architecture.md)
- [LiveKit on Telnyx regions](livekit-on-telnyx-regions.md)
- [LiveKit on Telnyx limits and quotas](livekit-on-telnyx-limits-and-quotas.md)
