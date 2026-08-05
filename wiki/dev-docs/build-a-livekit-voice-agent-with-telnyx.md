---
title: Build a LiveKit Voice Agent with Telnyx
summary: Step-by-step guide to installing the Telnyx LiveKit plugin, writing a voice
  agent that uses Telnyx STT, TTS, and LLM components, and deploying it to the LiveKit
  Agents platform.
sources:
- url: https://developers.telnyx.com/docs/livekit/build/index
updated_at: 2026-08-05T13:47:34Z
---

# Build a LiveKit Voice Agent with Telnyx

Step-by-step guide to installing the Telnyx LiveKit plugin, writing a voice agent that uses Telnyx STT, TTS, and LLM components, and deploying it to the LiveKit Agents platform.

## Overview

This page walks through building and deploying a LiveKit voice agent that uses Telnyx for speech-to-text, text-to-speech, and LLM inference. The Telnyx-maintained plugin is installed from GitHub and exposes `telnyx.STT`, `telnyx.TTS`, and an OpenAI-compatible LLM entry point that can be routed through Telnyx-hosted models.

Before starting, complete [Quickstart — Step 1](quickstart-step-1.md) to configure the LiveKit CLI and register with the platform.

## Install the plugin

Install the Telnyx-maintained LiveKit plugin from GitHub:

```
pip install "telnyx-livekit-plugin @ git+https://github.com/team-telnyx/telnyx-livekit-plugin.git#subdirectory=telnyx-livekit-plugin"
```

This package is hosted by Telnyx to ship features and fixes ahead of the upstream `livekit-plugins-telnyx` PyPI release. Use the git install above for the current recommended version.

- [Plugin source on GitHub](https://github.com/team-telnyx/telnyx-livekit-plugin)

## Write your agent

Create `agent.py` with a standard LiveKit `AgentSession` that wires Telnyx components into the STT, LLM, and TTS slots:

```python
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

The only Telnyx-specific parts of the agent are the `stt`, `tts`, and `llm` arguments — everything else is standard LiveKit.

## Add a requirements file

Create a `requirements.txt` so the deploy step can resolve all dependencies:

```
livekit-agents
livekit-plugins-openai
livekit-plugins-silero
telnyx-livekit-plugin @ git+https://github.com/team-telnyx/telnyx-livekit-plugin.git#subdirectory=telnyx-livekit-plugin
```

## Deploy

Deploy the agent to the LiveKit Agents platform, passing your Telnyx API key as a secret:

```
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
```

The platform builds the image in-cluster, deploys it, and starts the worker. Once deployed, you can manage it with the LiveKit CLI:

- List deployed agents:
  ```
  lk agent list
  ```
- Tail logs for a specific agent:
  ```
  lk agent logs --id <AGENT_ID>
  ```

## Swap models

The example above uses Telnyx-hosted defaults, but each component can be swapped independently:

- **STT** — Deepgram, Nova-3, Nova-2, Flux → see [STT plugin](stt-plugin.md)
- **TTS** — Telnyx Natural HD, MiniMax, Rime, ElevenLabs (BYOK), Azure → see [TTS plugin](tts-plugin.md)
- **LLM** — GPT-4o-mini, Kimi-K2.6, Claude (BYOK) → see [LLM plugin](llm-plugin.md)

## Next steps

- [Telephony](telephony.md) — Connect your agent to a phone number
- [Deploy reference](deploy-reference.md) — Secrets, rollbacks, multi-region
