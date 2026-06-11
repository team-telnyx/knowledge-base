---
title: Telnyx Inference
summary: Telnyx Inference provides OpenAI-compatible API access to open-source LLMs
  hosted on Telnyx GPU infrastructure across four global regions. Swap your base URL
  and API key to integrate with frameworks like LangChain, LlamaIndex, CrewAI, and
  LiveKit, or route all OpenAI SDK calls through Telnyx with zero code changes via
  environment variables.
sources:
- url: https://developers.telnyx.com/docs/inference/integrations/index
- url: https://developers.telnyx.com/docs/inference/langchain-integration
- url: https://developers.telnyx.com/docs/inference/livekit
- url: https://developers.telnyx.com/docs/inference/llama-index
- url: https://developers.telnyx.com/docs/inference/missions/index
- url: https://developers.telnyx.com/docs/inference/models/index
- url: https://developers.telnyx.com/docs/inference/models/pricing
- url: https://developers.telnyx.com/docs/inference/models/regions
- url: https://developers.telnyx.com/docs/inference/openai
- url: https://developers.telnyx.com/docs/inference/pr-reviewer
- url: https://developers.telnyx.com/docs/inference/streaming-functions
updated_at: 2026-06-11T10:32:07Z
---

# Telnyx Inference

*Part 2 of 3 — see also: [Part 1](telnyx-inference-2--part-1.md), [Part 3](telnyx-inference-2--part-3.md)*

Telnyx Inference provides OpenAI-compatible API access to open-source LLMs hosted on Telnyx GPU infrastructure across four global regions. Swap your base URL and API key to integrate with frameworks like LangChain, LlamaIndex, CrewAI, and LiveKit, or route all OpenAI SDK calls through Telnyx with zero code changes via environment variables.

## Framework Integrations

### LangChain

Use `ChatOpenAI` with a `base_url` swap:

```bash
pip install langchain-openai
```

**Basic usage:**

```python
import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
    model="zai-org/GLM-5.1-FP8",
)

for chunk in llm.stream("Help me plan my vacation"):
    print(chunk.content, end="", flush=True)
```

**Function calling:**

```python
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a location."""
    return f"The weather in {location} is sunny and 72°F."

llm_with_tools = ChatOpenAI(
    base_url="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
    model="zai-org/GLM-5.1-FP8",
).bind_tools([get_weather])

result = llm_with_tools.invoke("What's the weather in Chicago?")
print(result.tool_calls)
```

### LlamaIndex

Use `OpenAILike` with an `api_base` swap:

```bash
pip install llama-index-core llama-index-llms-openai-like
```

```python
import os
from llama_index.llms.openai_like import OpenAILike
from llama_index.core.llms import ChatMessage

llm = OpenAILike(
    api_base="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
    model="zai-org/GLM-5.1-FP8",
    is_chat_model=True,
)

chat = llm.stream_chat([ChatMessage(role="user", content="Help me plan my vacation")])
for chunk in chat:
    print(chunk.delta, end="")
```

Combine with Telnyx Embeddings for retrieval-augmented generation.

### CrewAI

Set the `OPENAI_BASE_URL` environment variable or pass `base_url` in the LLM constructor to route CrewAI through Telnyx.

### LiveKit

LiveKit's [agent framework](https://docs.livekit.io/agents/overview/) integrates with Telnyx for LLM inference (via the OpenAI plugin), STT, and TTS:

```bash
pip install livekit-plugins-telnyx
```

**Voice assistant using Telnyx LLM, STT, and TTS:**

```python
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, voice, llm
from livekit.plugins import openai, silero, telnyx

async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text="You are a helpful voice assistant powered by Telnyx. Keep responses short and conversational.",
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    session = voice.AgentSession(
        llm=openai.LLM.with_telnyx(model="zai-org/GLM-5.1-FP8"),
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

**STT plugin** — `telnyx.STT()` provides real-time speech-to-text via Telnyx's WebSocket streaming API. **TTS plugin** — `telnyx.TTS()` provides real-time text-to-speech; pass a `voice` parameter to select a specific voice.

Required environment variables:

```bash
export TELNYX_API_KEY=<your Telnyx API key>
export LIVEKIT_URL=<your LiveKit server URL>
export LIVEKIT_API_KEY=<your LiveKit API key>
export LIVEKIT_API_SECRET=<your LiveKit API secret>
```

Test your agent with the [LiveKit Agents Playground](https://agents-playground.livekit.io).

## Function Calling

The Chat Completions API supports streaming function calls and parallel execution. Telnyx guarantees valid JSON is returned for tool calls.

### Streaming and Parallel Tool Calls

The model may invoke multiple tool calls differentiated by the `index` attribute on streamed chunks. The first chunk of a new tool call contains the function `name`, enabling early feedback. As streamed arguments build up, attempt JSON parsing; once valid, schedule an async task immediately.

```python
import asyncio, json, os
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai",
)

async def sleep(seconds: int):
    """Sleep for a given number of seconds."""
    await asyncio.sleep(seconds)
    return f"I slept for {seconds} seconds!"

async def dream(subject: str):
    """Dream about a given subject."""
    chat_completion = await client.chat.completions.create(
        model="zai-org/GLM-5.1-FP8",
        messages=[{"role": "user", "content": f"BRIEFLY describe a dream about {subject}"}],
    )
    return chat_completion.choices[0].message.content
```

Send both tools to the model with `tool_choice="required"` and `stream=True`, then parse the streamed chunks, schedule parallel `asyncio` tasks as arguments become parseable, and send results back for a final response.

## AI Missions

AI Missions let your agent execute multi-step workflows — research, phone calls, follow-ups, and summaries — using the Telnyx Missions API, Assistants API, and Numbers API together. An OpenClaw agent with the Telnyx Missions skill (installed from [ClawHub](https://clawhub.ai/dotcom-squad/telnyx-toolkit)) orchestrates the work.

### Prerequisites

- An OpenClaw agent
- A Telnyx account with an API key
- The Telnyx Missions skill installed and `TELNYX_API_KEY` configured as an environment variable
- At least one phone number in your Telnyx account for outbound calls

### How It Works

Your agent uses the **Missions API** to create a mission, plan steps, log events, and track status; the **Assistants API** to create a voice assistant with custom prompts and schedule calls; and the **Numbers API** to find and assign an available phone number. The Missions API tracks every step with statuses (`pending`, `in_progress`, `completed`, `failed`), providing a complete audit trail.

### Example Workflow

For a task like *"Find catering companies in Chicago and negotiate quotes for a corporate event"*, the agent will:

1. Create a mission and build an execution plan
2. Create a voice assistant with a tailored system prompt, greeting, and dynamic variables
3. Assign a phone number for outbound calling
4. Call the first target to establish a baseline
5. Call remaining targets using the best quote so far as leverage
6. Monitor call completions and capture conversation insights via the [AI Insights API](ai-insights-api.md)
7. Summarize results with recommendations

### Monitoring

The **AI Missions** section in the [Telnyx Portal](https://portal.telnyx.com) shows all missions, their status, and run details. Click **View Run** to see the structured result payload. The Portal also shows linked assistants, conversation history, and full transcripts with audio playback and latency metrics.

### Tips

- **Be specific** — detailed requests yield better results
- **Let the agent plan first** — ask it to create a plan before executing if you want to review
- **Check the Portal** — live progress is visible without chatting with the agent
- **Start small** — try 2–3 calls before scaling up
