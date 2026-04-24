---
title: Telnyx LiveKit Plugin
summary: Integrate Telnyx STT, TTS, and LLM services into LiveKit agents using the Telnyx LiveKit Plugin.
sources:
  - url: https://developers.telnyx.com/docs/inference/livekit/index
    content_hash: b17e55b1b64e049ccabd0fe389ae4c76b16a589a645f0e9e98ab4b49cb084e13
updated_at: 2026-04-10T00:00:00Z
---

# Telnyx LiveKit Plugin

Integrate Telnyx STT, TTS, and LLM services into LiveKit agents using the Telnyx LiveKit Plugin.

LiveKit's [agent framework](https://docs.livekit.io/agents/overview/) lets you build real-time, programmable voice agents. Telnyx integrates with LiveKit through the OpenAI plugin for LLM inference and through `livekit-plugins-telnyx` for native STT and TTS.

## Voice assistant example

This example is based on LiveKit's [agents examples repo](https://github.com/livekit/agents/tree/main/examples), modified to use Telnyx for LLM inference.

### Set up and activate a virtual env

```bash theme={null}
python -m venv venv
source venv/bin/activate
```

### Install requirements

```bash theme={null}
pip install -r requirements.txt
pip install livekit-plugins-telnyx
```

### Download files

This downloads model weights for voice-activity detection:

```bash theme={null}
python agent.py download-files
```

### Agent code

The following code uses Telnyx for LLM inference via `openai.LLM.with_telnyx()`, with Telnyx STT and TTS.

```python theme={null}
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
            model="meta-llama/Meta-Llama-3.1-70B-Instruct",
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

```bash theme={null}
export TELNYX_API_KEY=<your Telnyx API key>
export LIVEKIT_URL=<your LiveKit server URL>
export LIVEKIT_API_KEY=<your LiveKit API key>
export LIVEKIT_API_SECRET=<your LiveKit API secret>
```

### Run the agent worker

```bash theme={null}
python agent.py dev
```

### Test with a LiveKit frontend

Use the [LiveKit Agents Playground](https://agents-playground.livekit.io) to test your agent without building a frontend.

## Telnyx STT & TTS plugin

The `livekit-plugins-telnyx` package provides native Telnyx STT and TTS plugins for LiveKit agents.

```bash theme={null}
pip install livekit-plugins-telnyx
```

### STT

Use `telnyx.STT()` for real-time speech-to-text via Telnyx's WebSocket streaming API:

```python theme={null}
from livekit.plugins import telnyx

session = voice.AgentSession(
    stt=telnyx.STT(),
    # ... other plugins
)
```

### TTS

Use `telnyx.TTS()` for real-time text-to-speech. Pass a `voice` parameter to select a specific voice:

```python theme={null}
from livekit.plugins import telnyx

session = voice.AgentSession(
    tts=telnyx.TTS(voice="Telnyx.NaturalHD.astra"),
    # ... other plugins
)
```

See [TTS available voices](https://developers.telnyx.com/docs/tts-stt/tts-available-voices) for the full list of voice options.

## Related resources

* [LiveKit Telnyx LLM plugin docs](https://docs.livekit.io/agents/models/llm/plugins/telnyx/)
* [SIP trunk configuration for LiveKit](telnyx-livekit-sip-trunk-configuration.md)
* [Inference getting started](https://developers.telnyx.com/docs/inference)


## Related Pages

- [Telnyx & LiveKit: SIP Trunk Configuration](../runbooks/telnyx-livekit-sip-trunk-configuration.md)
