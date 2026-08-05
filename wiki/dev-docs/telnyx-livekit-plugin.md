---
title: Telnyx LiveKit Plugin
summary: Telnyx integrates with LiveKit's agent framework to power real-time, programmable
  voice agents. This page covers the voice assistant example, the native `livekit-plugins-telnyx`
  package for STT and TTS, and the OpenAI plugin path for LLM inference.
sources:
- url: https://developers.telnyx.com/docs/inference/livekit
updated_at: 2026-08-05T13:46:20Z
---

# Telnyx LiveKit Plugin

Telnyx integrates with LiveKit's agent framework to power real-time, programmable voice agents. This page covers the voice assistant example, the native `livekit-plugins-telnyx` package for STT and TTS, and the OpenAI plugin path for LLM inference.

## Overview

LiveKit's [agent framework](https://docs.livekit.io/agents/overview/) lets you build real-time, programmable voice agents. Telnyx integrates with LiveKit through the OpenAI plugin for LLM inference and through `livekit-plugins-telnyx` for native STT and TTS.

## Voice assistant example

This example is based on LiveKit's [agents examples repo](https://github.com/livekit/agents/tree/main/examples), modified to use Telnyx for LLM inference.

### Set up and activate a virtual env

```
python -m venv venv
source venv/bin/activate
```

### Install requirements

```
pip install -r requirements.txt
pip install livekit-plugins-telnyx
```

### Download files

This downloads model weights for voice-activity detection:

```
python agent.py download-files
```

### Agent code

The following code uses Telnyx for LLM inference via `openai.LLM.with_telnyx()`, with Telnyx STT and TTS.

```
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, voice, llm
from livekit.plugins import openai, silero, telnyx

load_dotenv()

async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a helpful voice assistant powered by Telnyx. "
            "Keep responses short and conversational."
        ),
    )

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    session = voice.AgentSession(
        llm=openai.LLM.with_telnyx(
            model="zai-org/GLM-5.2",
        ),
        vad=silero.VAD.load(),
        stt=telnyx.STT(),
        tts=telnyx.TTS(voice="Telnyx.NaturalHD.astra"),
        chat_ctx=initial_ctx,
    )
    session.start(ctx.room)

    await session.say("Hey, how can I help you today?", allow_interruptions=True)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
```

### Set environment variables

```
export TELNYX_API_KEY=<your Telnyx API key>
export LIVEKIT_URL=<your LiveKit server URL>
export LIVEKIT_API_KEY=<your LiveKit API key>
export LIVEKIT_API_SECRET=<your LiveKit API secret>
```

### Run the agent worker

```
python agent.py dev
```

### Test with a LiveKit frontend

Use the [LiveKit Agents Playground](https://agents-playground.livekit.io) to test your agent without building a frontend.

## Telnyx STT & TTS plugin

The `livekit-plugins-telnyx` package provides native Telnyx STT and TTS plugins for LiveKit agents.

```
pip install livekit-plugins-telnyx
```

### STT

Use `telnyx.STT()` for real-time speech-to-text via Telnyx's WebSocket streaming API:

```
from livekit.plugins import telnyx

session = voice.AgentSession(
    stt=telnyx.STT(),
    # ... other plugins
)
```

### TTS

Use `telnyx.TTS()` for real-time text-to-speech. Pass a `voice` parameter to select a specific voice:

```
from livekit.plugins import telnyx

session = voice.AgentSession(
    tts=telnyx.TTS(voice="Telnyx.NaturalHD.astra"),
    # ... other plugins
)
```

See [TTS Available Voices](tts-available-voices.md) for the full list of voice options.

## Related resources

- [LiveKit Telnyx LLM plugin docs](https://docs.livekit.io/agents/models/llm/plugins/telnyx/)
- [SIP Trunking LiveKit Configuration Guide](sip-trunking-livekit-configuration-guide.md)
- [Inference Getting Started](inference-getting-started.md)
