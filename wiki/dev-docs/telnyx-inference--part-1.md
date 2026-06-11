---
title: Telnyx Inference
summary: Telnyx Inference provides an OpenAI-compatible API for large language model
  chat completions, function calling, embeddings, and clustering, alongside AI Insights
  for conversation analysis and Voice AI Assistants for telephony-based conversational
  agents. This page covers the core API, integrations, data residency, and practical
  tutorials.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
  content_hash: ff522f2e6bd1723aaae77aa0136c8445286d925413287656782da4be07d09f11
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
  content_hash: 7b522bb1ea6820875819e42eeb02ef42c22beea5981ac6d32e5415b96292655b
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
  content_hash: 50e16a3392164849e8db62587e0a7d5fdc2f38c5f7bf22efbf8816070480878f
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
  content_hash: 0bf1cdff1a2e68b76975f93b097d45c41337877c1dbbba2397ea493699f9fd35
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
  content_hash: 35e09b760fc2688800b0cbec4812a2b908b2893f4c2b014c4c85e4b020cfe572
- url: https://developers.telnyx.com/docs/inference/clusters
  content_hash: 2168a5dbf3b8c93576ac5ca7eb6daef42850a48d2787e29743f161a668bc6b0d
- url: https://developers.telnyx.com/docs/inference/crewai
  content_hash: bb1baccf1e6687a03af6f732aaceb0e310beb83d0b6ce6aa7f9cb934418a351b
- url: https://developers.telnyx.com/docs/inference/data-residency
  content_hash: 5ec98630f8132d215237b19167267f10bf0a0afc3879a204570c1e18258b6c5b
- url: https://developers.telnyx.com/docs/inference/embeddings
  content_hash: da55ec529bd85eaa5fbcc3baac0d1b3d0c01b0d70cc62a03854a507fe8accdf0
- url: https://developers.telnyx.com/docs/inference/functions
  content_hash: d8787dd1d761b9535b4b844287b039a25c7cc0a895592a3309b5da4b3f1ceb15
- url: https://developers.telnyx.com/docs/inference/getting-started/index
  content_hash: 91d21b775b382bcbd90ae079c0b93ca3854a5cfea589b985c25e9a151ea79b45
updated_at: 2026-06-11T10:33:19Z
---

# Telnyx Inference

*Part 1 of 6 — see also: [Part 2](telnyx-inference--part-2.md), [Part 3](telnyx-inference--part-3.md), [Part 4](telnyx-inference--part-4.md), [Part 5](telnyx-inference--part-5.md), [Part 6](telnyx-inference--part-6.md)*

Telnyx Inference provides an OpenAI-compatible API for large language model chat completions, function calling, embeddings, and clustering, alongside AI Insights for conversation analysis and Voice AI Assistants for telephony-based conversational agents. This page covers the core API, integrations, data residency, and practical tutorials.

## Getting Started

### Prerequisites

- A [Telnyx account](https://telnyx.com/sign-up)
- An [API Key](https://portal.telnyx.com/#/app/auth/v2)
- Python 3.8+

Install the OpenAI SDK (the Telnyx Inference API is OpenAI-compatible — any OpenAI SDK works with a `base_url` swap):

```bash
pip install openai
```

### Quick Start

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
  model="zai-org/GLM-5.1-FP8",
  stream=True
)

# GLM-5.1 is a reasoning model: it streams its thinking in `reasoning_content`
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

Reasoning models such as `zai-org/GLM-5.1-FP8` return their chain-of-thought in a separate `reasoning_content` field (on `message` for non-streaming responses, or `delta` when streaming). Models without reasoning simply omit it, so the `getattr(..., "reasoning_content", None)` guard works for every model.

### Core Concepts

| Concept | Description |
|---|---|
| **Messages** | Chat history passed to the model |
| **Roles** | Every message has a role: `system` (model behavior instructions), `user` (end-user input), `assistant` (model output), or `tool` (function call results) |
| **Models** | See [Available Models](https://developers.telnyx.com/docs/inference/models) for all hosted LLMs with context lengths and capabilities |
| **Streaming** | Server-sent events, same as OpenAI |

## Function Calling

Using the `tools` field, you can enable a language model to choose functions to call. The chat completions API does not call the function itself — it returns the arguments you need to execute the function yourself. Of the open-source language models hosted on Telnyx, `zai-org/GLM-5.1-FP8` is especially good at calling functions.

### Defining and Calling Functions

```python
import os, json
from openai import OpenAI

client = OpenAI(
  api_key=os.getenv("TELNYX_API_KEY"),
  base_url="https://api.telnyx.com/v2/ai/openai",
)

tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "description": "The temperature unit to use"},
        },
        "required": ["location", "unit"],
      },
    }
  }
]

messages = [{"role": "user", "content": "How is the weather in Chicago?"}]
chat_completion = client.chat.completions.create(
  model="zai-org/GLM-5.1-FP8",
  messages=messages,
  tools=tools,
  tool_choice="auto"
)
```

The `tool_choice` options are:

- `required` — forces the model to choose a tool
- `none` — forces the model not to choose a tool
- `auto` — lets the model decide

### Executing Functions and Returning Results

If the model chooses a function, the response includes a `tool_calls` field. You then execute the function and append the result back as a `tool`-role message:

```python
assistant_message = chat_completion.choices[0].message
tool_calls = assistant_message.tool_calls
if tool_calls:
    messages.append(assistant_message)
    available_functions = {"get_current_weather": get_current_weather}
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_response = function_to_call(**function_args)
        messages.append({
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": function_name,
            "content": function_response,
        })
    second_chat_completion = client.chat.completions.create(
        model="zai-org/GLM-5.1-FP8",
        messages=messages,
    )
    print(second_chat_completion.choices[0].message.content)
```

### Defining Functions Programmatically

You can generate the JSON tool definition from a Python function signature using Pydantic's `create_model`:

```python
import inspect
from pydantic import create_model
from typing import Literal

def func_to_tool(f):
    kw = {
        n: (o.annotation, ... if o.default == inspect.Parameter.empty else o.default)
        for n, o in inspect.signature(f).parameters.items()
    }
    s = create_model(f.__name__, **kw).model_json_schema()
    return {
        "type": "function",
        "function": {
            "name": s["title"],
            "description": inspect.getdoc(f),
            "parameters": s
        }
    }
```

## Embeddings & Document Retrieval

Embeddings are numerical representations of concepts within text, image, or audio data. They encode meaning so that semantically similar content is closer in vector space. This enables semantic search and retrieval-augmented generation (RAG).

### Upload Documents

Upload objects to Telnyx's S3-Compatible storage using the [Cloud Storage quickstart](https://developers.telnyx.com/docs/cloud-storage/quick-start) or the [drag-and-drop interface in the portal](https://portal.telnyx.com/#/storage/buckets).

### Embed Documents

Embed documents via the [embed API](https://developers.telnyx.com/api-reference/embeddings/embed-url-content) or by clicking "Embed for AI Use" in the portal while viewing your storage bucket's contents. Behind the scenes, documents are processed into sections and each section is embedded.

### Chat Over Your Documents

Once documents are embedded, you can use them in the [AI Playground](https://portal.telnyx.com/#/ai/playground) by selecting the bucket from the storage dropdown, or via the chat completions API:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai",
)

question = "<ADD QUESTION HERE>"
bucket = "<ADD EMBEDDED BUCKET HERE>"
chat_completion = client.chat.completions.create(
  messages=[{"role": "user", "content": question}],
  model="zai-org/GLM-5.1-FP8",
  stream=True,
  tools=[{
    "type": "retrieval",
    "retrieval": {"bucket_ids": [bucket]}
  }]
)

for chunk in chat_completion:
  if chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="", flush=True)
```
