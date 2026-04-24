---
title: Inference API Quickstart
summary: Welcome to the Telnyx Inference API! This guide will teach you the basics of chatting with open-source language models running on Telnyx GPUs.
sources:
  - url: https://developers.telnyx.com/docs/inference/getting-started/index
    content_hash: ad610af5c569e08db7fc754f79e9f03e001baacf883084b9b99df8a85345ba6c
updated_at: 2026-04-10T00:00:00Z
---

# Inference API Quickstart

## Introduction

Welcome to the Telnyx Inference API! This guide will teach you the basics of chatting with open-source language models running on Telnyx GPUs.

## Prerequisites

* [Sign up for a free Telnyx account](https://telnyx.com/sign-up)
* [Create an API Key](https://portal.telnyx.com/#/app/auth/v2)
* \[Optional] OpenAI SDK
  * Our inference API is OpenAI-compatible
  * Try using one of their SDKs (`pip install openai` or `npm install openai`)

## Python Example

Let's complete your first chat. Here's some simple Python to interact with a language model.

> **Note:** *Make sure you have set the TELNYX\_API\_KEY environment variable*

```python theme={null}
import os
from openai import OpenAI

client = OpenAI(
  api_key=os.getenv("TELNYX_API_KEY"),
  base_url="https://api.telnyx.com/v2/ai",
)

chat_completion = client.chat.completions.create(
  messages=[
    {
        "role": "user",
        "content": "Tell me about Telnyx"
    }
  ],
  model="meta-llama/Meta-Llama-3.1-8B-Instruct",
  stream=True
)

for chunk in chat_completion:
  if chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="", flush=True)
```

## Core Concepts

### Messages

These refer to the history of messages in a chat.

### Roles

Every message has a role: **system**, **user**, **assistant**, or **tool**.

* **System** messages are sent once at the start of a chat, instructing the model how to behave for the duration of the chat. This is a good way to give the model a goal or a set of rules to follow.
* **User** messages refer to what the end-user has input
* **Assistant** messages refer to what the model has output
* **Tool** messages refer to the results of any tool calls. Tools are often referred to as function calls. See our [function calling tutorial](https://developers.telnyx.com/docs/inference/functions) for more information.

### Models

In the context of chat completions, we are talking about [large language models](https://en.wikipedia.org/wiki/Large_language_model) (LLMs). Your choice of LLM will affect the quality, speed, and price of your chat completions.

### Streaming

For real-time interactions, you will want the ability to stream partial responses back to a client as they are completed. To achieve this, we follow the same [Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) standard as OpenAI.

## Not sure how to get started?

| I want to...                                       | Relevant Tutorial                                                                                                                                                                                 |
| :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Build a voice assistant                            | [No-Code Voice Assistant](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index)                                                                               |
| Enforce structured JSON output                     | [JSON Mode and Beyond](https://developers.telnyx.com/docs/inference/json-mode)                                                                                                                    |
| Let a language model invoke my custom code         | [Function Calling](https://developers.telnyx.com/docs/inference/functions)<br />[Function Calling (Streaming + Parallel Calls)](https://developers.telnyx.com/docs/inference/streaming-functions) |
| Send audio to a language model                     | [Audio Language Models](https://developers.telnyx.com/docs/inference/audio-language-models)                                                                                                       |
| Send images to a language model                    | [Vision Language Models](https://developers.telnyx.com/docs/inference/vision)                                                                                                                     |
| Give a language model access to relevant documents | [Embeddings](https://developers.telnyx.com/docs/inference/embeddings)                                                                                                                             |
| Identify themes in my data                         | [Clusters](https://developers.telnyx.com/docs/inference/clusters)                                                                                                                                 |
| Teach a language model specific and complex tasks  | [Fine-tuning](https://developers.telnyx.com/docs/inference/fine-tuning)                                                                                                                           |

## Additional References

* Dive into our [tutorials](../runbooks/function-calling.md)
* Explore our our full [API reference](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion).
* Review our [OpenAI Compatibility Matrix](../runbooks/openai-api-migration-guide.md)
* Check out our [pricing page](https://telnyx.com/pricing/inference-api)

## Feedback

Have questions or need help troubleshooting? Our [support team](https://support.telnyx.com/) is here to assist you. Join our [Slack community](https://joinslack.telnyx.com/) to connect with other developers and the Telnyx team.


## Related Pages

- [React quickstart](../reference/react-quickstart.md)
- [Voice Assistant Quickstart](../runbooks/voice-assistant-quickstart.md)
- [Telnyx CLI Quickstart](../reference/telnyx-cli-quickstart.md)
- [Number Reputation Quickstart](../tutorial/number-reputation-quickstart.md)
