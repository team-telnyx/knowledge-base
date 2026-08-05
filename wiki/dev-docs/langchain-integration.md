---
title: LangChain Integration
summary: Use Telnyx Inference with LangChain by pointing the OpenAI-compatible `ChatOpenAI`
  client at the Telnyx AI base URL. This page covers setup, basic usage, function
  calling, and streaming.
sources:
- url: https://developers.telnyx.com/docs/inference/langchain-integration
updated_at: 2026-08-05T13:46:12Z
---

# LangChain Integration

Use Telnyx Inference with LangChain by pointing the OpenAI-compatible `ChatOpenAI` client at the Telnyx AI base URL. This page covers setup, basic usage, function calling, and streaming.

## Setup

Install the LangChain OpenAI integration package:

```
pip install langchain-openai
```

## Usage

Telnyx Inference is OpenAI-compatible, so you can use `ChatOpenAI` from `langchain_openai` and swap the `base_url` to point at the Telnyx AI endpoint. Authenticate with your Telnyx API key and select a model such as `zai-org/GLM-5.2`.

```
import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
    model="zai-org/GLM-5.2",
)

for chunk in llm.stream("Help me plan my vacation"):
    print(chunk.content, end="", flush=True)
```

## Function Calling

Bind tools to the model using LangChain's standard `bind_tools` interface. The example below defines a `get_weather` tool and inspects the tool calls returned by the model.

```
import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a location."""
    return f"The weather in {location} is sunny and 72°F."

llm_with_tools = ChatOpenAI(
    base_url="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
    model="zai-org/GLM-5.2",
).bind_tools([get_weather])

result = llm_with_tools.invoke("What's the weather in Chicago?")
print(result.tool_calls)
```

## Streaming

Stream responses token-by-token by passing a list of `HumanMessage` objects to `llm.stream` and printing each chunk as it arrives.

```
from langchain_core.messages import HumanMessage

messages = [HumanMessage(content="Explain quantum computing in 3 sentences")]
for chunk in llm.stream(messages):
    print(chunk.content, end="", flush=True)
```
