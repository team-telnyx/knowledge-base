---
title: Inference API Quickstart
summary: Get started with the Telnyx Inference API using the OpenAI SDK. The API is
  OpenAI-compatible, supports streaming, and exposes reasoning content from reasoning
  models such as zai-org/GLM-5.2.
sources:
- url: https://developers.telnyx.com/docs/inference/getting-started/index
updated_at: 2026-08-05T13:46:06Z
---

# Inference API Quickstart

Get started with the Telnyx Inference API using the OpenAI SDK. The API is OpenAI-compatible, supports streaming, and exposes reasoning content from reasoning models such as zai-org/GLM-5.2.

## Prerequisites

Before you begin, make sure you have:

- A [Telnyx account](https://telnyx.com/sign-up)
- An [API Key](https://portal.telnyx.com/#/app/auth/v2)
- Python 3.8+

Install the OpenAI SDK:

```
pip install openai
```

The Inference API is OpenAI-compatible. Any OpenAI SDK works with a `base_url` swap.

## Python

```python
import os
from openai import OpenAI

client = OpenAI(
  api_key=os.getenv("TELNYX_API_KEY"),
  base_url="https://api.telnyx.com/v2/ai/openai",
)

chat_completion = client.chat.completions.create(
  messages=[
    {"role": "user", "content": "Tell me about Telnyx"}
  ],
  model="zai-org/GLM-5.2",
  stream=True
)

# GLM-5.2 is a reasoning model: it streams its thinking in `reasoning_content`
# before the final answer in `content`. Print both so you can see the reasoning.
reasoning_started = False
content_started = False
for chunk in chat_completion:
  delta = chunk.choices[0].delta
  if getattr(delta, "reasoning_content", None):
    if not reasoning_started:
      print("--- reasoning ---")
      reasoning_started = True
    print(delta.reasoning_content, end="", flush=True)
  if delta.content:
    if not content_started:
      print("\n--- answer ---")
      content_started = True
    print(delta.content, end="", flush=True)
```

Reasoning models such as `zai-org/GLM-5.2` return their chain-of-thought in a separate `reasoning_content` field (on `message` for non-streaming responses, or `delta` when streaming). Models without reasoning simply omit it, so the `getattr(..., "reasoning_content", None)` guard works for every model.

## Core Concepts

### Messages

Chat history passed to the model.

### Roles

Every message has a role: **system**, **user**, **assistant**, or **tool**.

- **system** — model behavior instructions
- **user** — end-user input
- **assistant** — model output
- **tool** — function call results. See [Function Calling](function-calling.md).

### Models

[Available Models](available-models.md) lists all hosted LLMs with context lengths and capabilities.

### Streaming

Server-sent events, same as OpenAI.

## What Next?

| I want to… | Go to |
| --- | --- |
| Build a voice assistant | [No-Code Voice Assistant](no-code-voice-assistant.md) |
| Call custom code from the model | [Function Calling](function-calling.md) / [Streaming Functions](streaming-functions.md) |
| Ground responses in documents | [Embeddings](embeddings.md) |
| Identify themes in data | [Clusters](clusters.md) |
| Migrate from OpenAI | [OpenAI Migration](openai-migration.md) |
| Browse all models | [Available Models](available-models.md) |
