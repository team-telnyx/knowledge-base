---
title: Anthropic API Migration Guide
summary: Telnyx exposes an Anthropic-compatible Messages endpoint at POST /v2/ai/anthropic/v1/messages,
  accepting the same request body and returning the same response shape as the native
  Anthropic Messages API, including streaming via Anthropic SSE event types. This
  guide covers authentication, quickstart examples, streaming, tool calling, extended
  thinking, system prompts, available models, Telnyx-specific extensions, and a parameter
  compatibility matrix.
sources:
- url: https://developers.telnyx.com/docs/inference/anthropic
updated_at: 2026-08-05T13:45:44Z
---

# Anthropic API Migration Guide

*Part 1 of 2 — see also: [Part 2](anthropic-api-migration-guide--part-2.md)*

Telnyx exposes an Anthropic-compatible Messages endpoint at POST /v2/ai/anthropic/v1/messages, accepting the same request body and returning the same response shape as the native Anthropic Messages API, including streaming via Anthropic SSE event types. This guide covers authentication, quickstart examples, streaming, tool calling, extended thinking, system prompts, available models, Telnyx-specific extensions, and a parameter compatibility matrix.

## Overview

The Telnyx Inference API exposes an Anthropic-compatible Messages endpoint at `POST /v2/ai/anthropic/v1/messages`. It accepts the same request body as the [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) and returns the same response shape — including streaming via Anthropic SSE event types (`message_start`, `content_block_start`, `content_block_delta`, `content_block_stop`, `message_delta`, `message_stop`).

To migrate, swap the base URL and pass your Telnyx API key as a Bearer token.

## Authentication

The Anthropic SDK sends requests with an `x-api-key` header by default. Telnyx uses `Authorization: Bearer <TELNYX_API_KEY>` instead. Pass the Telnyx key as a `default_headers` override and set the SDK's own `api_key` to any placeholder value — the gateway ignores it.

```bash
export TELNYX_API_KEY='KEY***'
```

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key="unused",  # placeholder — the gateway uses the Bearer header below
    base_url="https://api.telnyx.com/v2/ai/anthropic",
    default_headers={
        "Authorization": f"Bearer {os.environ['TELNYX_API_KEY']}",
    },
)
```

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: "unused", // placeholder — the gateway uses the Bearer header below
  baseURL: "https://api.telnyx.com/v2/ai/anthropic",
  defaultHeaders: {
    Authorization: `Bearer ${process.env.TELNYX_API_KEY}`,
  },
});
```

The Anthropic SDK requires `api_key` to be set to a non-empty string, even when you override auth via `default_headers`. Use any placeholder — the Telnyx gateway only reads the `Authorization: Bearer` header.

## Quickstart

### Python

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key="unused",
    base_url="https://api.telnyx.com/v2/ai/anthropic",
    default_headers={
        "Authorization": f"Bearer {os.environ['TELNYX_API_KEY']}",
    },
)

# Non-streaming
message = client.messages.create(
    model="zai-org/GLM-5.2",
    max_tokens=1024,
    system="You are a friendly chatbot.",
    messages=[
        {"role": "user", "content": "Tell me about Telnyx"}
    ],
)
print(message.content[0].text)
```

### JavaScript / TypeScript

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: "unused",
  baseURL: "https://api.telnyx.com/v2/ai/anthropic",
  defaultHeaders: {
    Authorization: `Bearer ${process.env.TELNYX_API_KEY}`,
  },
});

// Non-streaming
const message = await client.messages.create({
  model: "zai-org/GLM-5.2",
  max_tokens: 1024,
  system: "You are a friendly chatbot.",
  messages: [{ role: "user", content: "Tell me about Telnyx" }],
});
console.log(message.content[0].text);
```

### curl

```bash
curl -sS -X POST "https://api.telnyx.com/v2/ai/anthropic/v1/messages" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "zai-org/GLM-5.2",
    "max_tokens": 1024,
    "system": "You are a friendly chatbot.",
    "messages": [{"role": "user", "content": "Tell me about Telnyx"}]
  }'
```

## Streaming

The endpoint streams Anthropic-format Server-Sent Events. Use the SDK's built-in streaming just as you would with the native Anthropic API:

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key="unused",
    base_url="https://api.telnyx.com/v2/ai/anthropic",
    default_headers={
        "Authorization": f"Bearer {os.environ['TELNYX_API_KEY']}",
    },
)

with client.messages.stream(
    model="zai-org/GLM-5.2",
    max_tokens=1024,
    system="You are a friendly chatbot.",
    messages=[{"role": "user", "content": "Tell me about Telnyx"}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

```javascript
const stream = await client.messages.stream({
  model: "zai-org/GLM-5.2",
  max_tokens: 1024,
  system: "You are a friendly chatbot.",
  messages: [{ role: "user", content: "Tell me about Telnyx" }],
});

for await (const event of stream) {
  if (event.type === "content_block_delta" && event.delta.type === "text_delta") {
    process.stdout.write(event.delta.text);
  }
}
```

## Tool Calling

Tool definitions and tool results follow the [Anthropic tool use format](https://docs.anthropic.com/en/docs/build-with-claude/tool-use):

```python
import os
import json
from anthropic import Anthropic

client = Anthropic(
    api_key="unused",
    base_url="https://api.telnyx.com/v2/ai/anthropic",
    default_headers={
        "Authorization": f"Bearer {os.environ['TELNYX_API_KEY']}",
    },
)

tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather in a given location.",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City and state, e.g. San Francisco, CA"},
            },
            "required": ["location"],
        },
    }
]

response = client.messages.create(
    model="zai-org/GLM-5.2",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Lisbon?"}],
)

# The model returns a tool_use content block
for block in response.content:
    if block.type == "tool_use":
        print(f"Tool: {block.name}")
        print(f"Input: {block.input}")
```

## Extended Thinking

For models that support extended thinking (e.g. Claude reasoning models), pass the `thinking` parameter. On older SDK versions that reject unknown kwargs, use `extra_body` to forward it into the request JSON:

```python
response = client.messages.create(
    model="zai-org/GLM-5.2",
    max_tokens=4096,
    messages=[{"role": "user", "content": "Exprove que 17 é primo."}],
    extra_body={
        "thinking": {"type": "enabled", "budget_tokens": 2048},
    },
)
```

## System Prompts

The `system` parameter can be a plain string or an array of content blocks, matching the [Anthropic API format](https://docs.anthropic.com/en/api/messages):

```python
# String system prompt
response = client.messages.create(
    model="zai-org/GLM-5.2",
    max_tokens=1024,
    system="You are a helpful assistant.",
    messages=[{"role": "user", "content": "Hello!"}],
)

# Array-style system prompt (cache_control, etc.)
response = client.messages.create(
    model="zai-org/GLM-5.2",
    max_tokens=1024,
    system=[
        {"type": "text", "text": "You are a helpful assistant.", "cache_control": {"type": "ephemeral"}},
    ],
    messages=[{"role": "user", "content": "Hello!"}],
)
```

## Models

Anthropic models are available under the `anthropic/` prefix. See [Available Models](available-models.md) for the full list. Open-source models hosted on Telnyx (e.g. `zai-org/GLM-5.2`, `moonshotai/Kimi-K2.6`) also work through this endpoint — the request is translated to the OpenAI-compatible format internally and the response is translated back to the Anthropic shape.
