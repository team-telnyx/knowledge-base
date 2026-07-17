---
title: Telnyx Inference
summary: Telnyx Inference is a developer platform for building AI-powered applications,
  centered on an OpenAI-compatible chat completions API and a managed Voice AI Assistant
  product. It offers open-source LLMs hosted on Telnyx GPU infrastructure, embeddings
  and RAG, fine-tuning, audio language models, function calling, structured output,
  and integrations with enterprise platforms. The Voice AI Assistant product supports
  dynamic variables, memory, agent handoff, conversation workflows, multi-participant
  calls, scheduled events, observability via Langfuse, and AI Insights for conversation
  analysis.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/client-side-tools
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/telnyx-managed-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
- url: https://developers.telnyx.com/docs/inference/anthropic
- url: https://developers.telnyx.com/docs/inference/audio-language-models
- url: https://developers.telnyx.com/docs/inference/clusters
- url: https://developers.telnyx.com/docs/inference/crewai
- url: https://developers.telnyx.com/docs/inference/data-residency/index
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/feature-coverage
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/index
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/pricing
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/retention
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/searching
- url: https://developers.telnyx.com/docs/inference/embedding-rag/index
- url: https://developers.telnyx.com/docs/inference/embeddings/index
- url: https://developers.telnyx.com/docs/inference/fine-tuning
- url: https://developers.telnyx.com/docs/inference/functions
- url: https://developers.telnyx.com/docs/inference/getting-started/index
- url: https://developers.telnyx.com/docs/inference/integrations/index
- url: https://developers.telnyx.com/docs/inference/json-mode
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
updated_at: 2026-07-17T09:14:08Z
---

# Telnyx Inference

*Part 1 of 5 — see also: [Part 2](telnyx-inference--part-2.md), [Part 3](telnyx-inference--part-3.md), [Part 4](telnyx-inference--part-4.md), [Part 5](telnyx-inference--part-5.md)*

Telnyx Inference is a developer platform for building AI-powered applications, centered on an OpenAI-compatible chat completions API and a managed Voice AI Assistant product. It offers open-source LLMs hosted on Telnyx GPU infrastructure, embeddings and RAG, fine-tuning, audio language models, function calling, structured output, and integrations with enterprise platforms. The Voice AI Assistant product supports dynamic variables, memory, agent handoff, conversation workflows, multi-participant calls, scheduled events, observability via Langfuse, and AI Insights for conversation analysis.

## Overview

Telnyx Inference is a developer platform for building AI-powered applications, with a particular focus on real-time voice agents. The platform exposes an OpenAI-compatible chat completions API, an Anthropic-compatible Messages endpoint, audio language models, embeddings, retrieval-augmented generation (RAG), fine-tuning, and a managed Voice AI Assistant product. All chat models are open-source LLMs hosted on Telnyx GPU infrastructure across four regions (Atlanta, Denver, Paris, Sydney), with routing influenced by the ingress domain you call (`api.telnyx.com`, `api.telnyx.eu`, `api.telnyx.com.au`).

## Available Models

Open-source LLMs hosted on Telnyx GPU infrastructure, all accessible via the [Chat Completions API](https://developers.telnyx.com/api-reference/openai-chat/create-a-chat-completion-openai-compatible).

| Model ID | Parameters | Context Length | Best For |
| --- | --- | --- | --- |
| `moonshotai/Kimi-K2.6` | 1.0T | 256K | Highest intelligence, voice AI (with thinking disabled) **(Recommended)** |
| `zai-org/GLM-5.2` | 753.9B | 1M | Coding, reasoning, 1M context window |
| `MiniMaxAI/MiniMax-M3-MXFP8` | 428B | 1M | Cheapest while maintaining high intelligence |

For embeddings, `thenlper/gte-large` (1024 dimensions) is available.

Reasoning models such as `zai-org/GLM-5.2` return their chain-of-thought in a separate `reasoning_content` field on `message` (non-streaming) or `delta` (streaming). Non-reasoning models omit it, so a `getattr(..., "reasoning_content", None)` guard works for every model.

## Inference API Quickstart

The Inference API is OpenAI-compatible. Any OpenAI SDK works with a `base_url` swap.

```
pip install openai
```

```
import os
from openai import OpenAI

client = OpenAI(
  api_key=os.getenv("TELNYX_API_KEY"),
  base_url="https://api.telnyx.com/v2/ai/openai",
)

chat_completion = client.chat.completions.create(
  messages=[{"role": "user", "content": "Tell me about Telnyx"}],
  model="zai-org/GLM-5.2",
  stream=True
)
```

Every message has a role: **system** (model behavior instructions), **user** (end-user input), **assistant** (model output), or **tool** (function call results). Streaming uses server-sent events, same as OpenAI.

## OpenAI and Anthropic Compatibility

### OpenAI Migration

Swap two environment variables and change the model name:

```
export OPENAI_BASE_URL='https://api.telnyx.com/v2/ai/openai'
export OPENAI_API_KEY='KEY***'
```

Telnyx supports the standard OpenAI parameters (`messages`, `model`, `stream`, `max_tokens`, `temperature`, `top_p`, `frequency_penalty`, `presence_penalty`, `n`, `stop`, `logit_bias`, `logprobs`, `top_logprobs`, `seed`, `response_format`, `tool_choice`, `tools`, `function`) plus Telnyx-specific extensions: `retrieval`, `guided_json`, `guided_regex`, `guided_choice`, `min_p`, `use_beam_search`, `best_of`, `length_penalty`, and `early_stopping`. The `user` parameter is not supported.

### Anthropic Migration

The Telnyx Inference API exposes an Anthropic-compatible Messages endpoint at `POST /v2/ai/anthropic/v1/messages`. It accepts the same request body as the [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) and returns the same response shape, including streaming via Anthropic SSE event types (`message_start`, `content_block_start`, `content_block_delta`, `content_block_stop`, `message_delta`, `message_stop`).

The Anthropic SDK sends requests with an `x-api-key` header by default. Telnyx uses `Authorization: Bearer <TELNYX_API_KEY>` instead. Pass the Telnyx key as a `default_headers` override and set the SDK's own `api_key` to any placeholder value — the gateway ignores it.

```
import os
from anthropic import Anthropic

client = Anthropic(
    api_key="unused",
    base_url="https://api.telnyx.com/v2/ai/anthropic",
    default_headers={
        "Authorization": f"Bearer {os.environ['TELNYX_API_KEY']}",
    },
)
```

Telnyx-specific fields accepted alongside the standard Anthropic body include `api_key_ref`, `mcp_servers`, `fallback_config`, `billing_group_id`, `timeout`, `max_retries`, and `service_tier`.

## Framework Integrations

OpenAI-compatible API. Swap `base_url` and `api_key` in any framework that supports OpenAI.

| Framework | Swap Method | Guide |
| --- | --- | --- |
| OpenAI SDK | `base_url` in client constructor | [OpenAI Migration](openai-migration.md) |
| LangChain | `base_url` in `ChatOpenAI` | [LangChain Integration](langchain-integration.md) |
| LlamaIndex | `api_base` in `OpenAILike` | [LlamaIndex Integration](llamaindex-integration.md) |
| CrewAI | `OPENAI_BASE_URL` env var or `base_url` in LLM | [CrewAI Integration](crewai-integration.md) |
| LiveKit | Telnyx as LLM provider | [Telnyx LiveKit Plugin](telnyx-livekit-plugin.md) |

Route all OpenAI SDK calls through Telnyx with no code changes:

```
export OPENAI_API_KEY=your_telnyx_api_key
export OPENAI_BASE_URL=https://api.telnyx.com/v2/ai/openai
```

### LangChain

```
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
    model="zai-org/GLM-5.2",
)
```

### LlamaIndex

```
from llama_index.llms.openai_like import OpenAILike

llm = OpenAILike(
    api_base="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
    model="zai-org/GLM-5.2",
    is_chat_model=True,
)
```

### CrewAI

```
from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="zai-org/GLM-5.2",
    base_url="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
)
```

### LiveKit

The `livekit-plugins-telnyx` package provides native Telnyx STT and TTS plugins for LiveKit agents. Use `openai.LLM.with_telnyx(model="zai-org/GLM-5.2")` for LLM inference, `telnyx.STT()` for speech-to-text, and `telnyx.TTS(voice="Telnyx.NaturalHD.astra")` for text-to-speech.

## Function Calling

Using the `tools` field, you can enable a language model to choose functions to call. The chat completions API does not call the function itself — it returns the arguments you need to execute the function yourself. Of the open-source models hosted on Telnyx, `zai-org/GLM-5.2` is especially good at calling functions.

`tool_choice` options are `required` (force the model to choose a tool), `none` (force the model to NOT choose a tool), or `auto` (let the model decide).

### Streaming and Parallel Calls

For low-latency contexts, streaming and parallel calls are especially helpful. The `handle_tool_calls` pattern iterates over streamed chunks, building a local copy of function calls in a `tool_calls` list. The first chunk of a new tool call contains the function `name`, enabling early feedback. As arguments are built from streamed chunks, the code attempts to parse them as JSON; once valid, an async task is scheduled for execution. Telnyx guarantees valid JSON is returned for tool calls.

## Structured Output

Telnyx supports several structured output modes via `extra_body`:

- **`guided_choice`** — restrict output to a list of allowed strings (e.g., `["positive", "negative"]`).
- **`guided_json`** — enforce a JSON Schema (or Pydantic model) on the response.
- **`response_format: {"type": "json_object"}`** — schema-less JSON mode.
- **`guided_regex`** — constrain output to match a regular expression (useful for limiting response length).

## Audio Language Models

Audio Language Models are identified in the models API with a `task` type of `audio-text-to-text`. Audio is made available to the model either by passing a link to the audio in a user message or by passing base64-encoded audio directly. Example model: `fixie-ai/ultravox-v0_4_1-llama-3_1-8b`.
