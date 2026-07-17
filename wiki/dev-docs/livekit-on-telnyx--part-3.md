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

*Part 3 of 6 — see also: [Part 1](livekit-on-telnyx--part-1.md), [Part 2](livekit-on-telnyx--part-2.md), [Part 4](livekit-on-telnyx--part-4.md), [Part 5](livekit-on-telnyx--part-5.md), [Part 6](livekit-on-telnyx--part-6.md)*

Telnyx LiveKit is a managed platform for deploying voice AI agents at scale, combining LiveKit's agent framework with built-in telephony, colocated AI inference on Telnyx GPUs, and managed infrastructure across multiple regions. This page covers architecture, compatibility, regions, quickstart, build, deploy, models (STT/TTS/LLM), telephony, observability, limits, pricing, and migration from LiveKit Cloud or self-hosted.

## Build

### 1. Install the plugin

```
pip install "telnyx-livekit-plugin @ git+https://github.com/team-telnyx/telnyx-livekit-plugin.git#subdirectory=telnyx-livekit-plugin"
```

This is the Telnyx-maintained plugin, which includes the latest features and fixes ahead of the upstream `livekit-plugins-telnyx` PyPI package. We host our own release to iterate faster than the upstream cadence allows. Use the git install above for the current recommended version. [Plugin source on GitHub](https://github.com/team-telnyx/telnyx-livekit-plugin).

### 2. Write your agent

Create `agent.py`:

```
import asyncio
from livekit.agents import Agent, AgentSession, JobContext, RoomInputOptions
from livekit.plugins import openai, silero, telnyx

class MyAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a helpful voice assistant.")

    async def on_enter(self):
        self.session.generate_reply(
            instructions="Greet the caller and ask how you can help."
        )

async def entrypoint(ctx: JobContext):
    session = AgentSession(
        stt=telnyx.STT(
            transcription_engine="Deepgram",
            base_url="wss://api.telnyx.com/v2/speech-to-text/transcription",
        ),
        llm=openai.LLM.with_telnyx(model="zai-org/GLM-5.2"),
        tts=telnyx.TTS(
            voice="Telnyx.NaturalHD.astra",
            sample_rate=24000,
        ),
        vad=silero.VAD.load(),
    )

    await ctx.connect()
    await session.start(
        agent=MyAgent(),
        room=ctx.room,
        room_input_options=RoomInputOptions(),
    )

    disconnect_event = asyncio.Event()

    @ctx.room.on("disconnected")
    def on_disconnect(*args):
        disconnect_event.set()

    await disconnect_event.wait()
```

The only Telnyx-specific parts are the `stt`, `tts`, and `llm` — everything else is standard LiveKit.

### 3. Add a requirements file

Create `requirements.txt`:

```
livekit-agents
livekit-plugins-openai
livekit-plugins-silero
telnyx-livekit-plugin @ git+https://github.com/team-telnyx/telnyx-livekit-plugin.git#subdirectory=telnyx-livekit-plugin
```

### 4. Deploy

```
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
```

The platform builds your image in-cluster, deploys it, and starts the worker. Check the status:

```
lk agent list
```

Tail logs once it's running:

```
lk agent logs --id <AGENT_ID>
```

### Swap models

The example above uses Telnyx-hosted defaults. Swap any component independently:

- **STT** — Deepgram, Nova-3, Nova-2, Flux → [Speech-to-Text (STT)](speech-to-text-stt.md)
- **TTS** — Telnyx Natural HD, MiniMax, Rime, ElevenLabs (BYOK), Azure → [Text-to-Speech (TTS)](text-to-speech-tts.md)
- **LLM** — GPT-4o-mini, Kimi-K2.6, Claude (BYOK) → [Large Language Models (LLM)](large-language-models-llm.md)
