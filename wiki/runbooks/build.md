---
title: Build
summary: Build a voice agent with Telnyx STT, TTS, and LLM and deploy it to the Telnyx platform.
sources:
  - url: https://developers.telnyx.com/docs/livekit/build/index
    content_hash: d0633d537fc9dfc4c4fe6131843fea3a55f13ae5300c141782129b4e5cff1db1
updated_at: 2026-04-10T00:00:00Z
---

# Build

Build a voice agent with Telnyx STT, TTS, and LLM and deploy it to the Telnyx platform.

> **Note:** **First time building?** Complete [Quickstart — Step 1](../tutorial/quick-start.md#step-1-configure-the-cli) to configure your CLI and register with the platform.

## 1. Install the plugin

```bash theme={null}
pip install "telnyx-livekit-plugin @ git+https://github.com/team-telnyx/telnyx-livekit-plugin.git#subdirectory=telnyx-livekit-plugin"
```

> **Note:** This is the Telnyx-maintained plugin, which includes the latest features and fixes ahead of the upstream `livekit-plugins-telnyx` PyPI package. We host our own release to iterate faster than the upstream cadence allows. Use the git install above for the current recommended version.

*[Plugin source on GitHub](https://github.com/team-telnyx/telnyx-livekit-plugin)*

## 2. Write your agent

Create `agent.py`:

```python theme={null}
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
        llm=openai.LLM.with_telnyx(model="moonshotai/Kimi-K2.5"),
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

## 3. Add a requirements file

Create `requirements.txt`:

```
livekit-agents
livekit-plugins-openai
livekit-plugins-silero
telnyx-livekit-plugin @ git+https://github.com/team-telnyx/telnyx-livekit-plugin.git#subdirectory=telnyx-livekit-plugin
```

## 4. Deploy

```bash theme={null}
lk agent deploy . --secrets TELNYX_API_KEY=$TELNYX_API_KEY
```

The platform builds your image in-cluster, deploys it, and starts the worker. Check the status:

```bash theme={null}
lk agent list
```

Tail logs once it's running:

```bash theme={null}
lk agent logs --id 
```

## Swap models

The example above uses Telnyx-hosted defaults. Swap any component independently:

* **STT** — Deepgram, Nova-3, Nova-2, Flux → [STT plugin](speech-to-text-stt.md)
* **TTS** — Telnyx Natural HD, MiniMax, Rime, ElevenLabs (BYOK), Azure → [TTS plugin](text-to-speech-tts.md)
* **LLM** — GPT-4o-mini, Kimi-K2.5, Qwen3, Claude (BYOK) → [LLM plugin](large-language-models-llm.md)

## Next steps

* [Telephony](telephony.md) — Connect your agent to a phone number
* [Deploy reference](deploy.md) — Secrets, rollbacks, multi-region
