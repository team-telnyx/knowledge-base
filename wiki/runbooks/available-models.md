---
title: Available Models
summary: Models available through the Telnyx Inference API for chat completions, AI Assistants, and more.
sources:
  - url: https://developers.telnyx.com/docs/inference/models/index
    content_hash: e6ea37dafd84e2ee1d52fe835238ed27a8c6b388bb692d7559d2177ff9ccf0f8
updated_at: 2026-04-10T00:00:00Z
---

# Available Models

Models available through the Telnyx Inference API for chat completions, AI Assistants, and more.

Telnyx provides access to a variety of open-source and proprietary large language models (LLMs) through the Inference API. All models are accessible via the [Chat Completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion) and are OpenAI-compatible.

## Chat Completions models

These models are verified for use with the [Chat Completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion).

> **Note:** Currently available in the US only. Additional regions coming soon.

| Model ID                 | Description                                                            |
| ------------------------ | ---------------------------------------------------------------------- |
| `moonshotai/Kimi-K2.5`   | Balance of intelligence and cost, real-time voice AI **(Recommended)** |
| `zai-org/GLM-5`          | Highest intelligence open-source LLM                                   |
| `MiniMaxAI/MiniMax-M2.5` | High intelligence at lower cost                                        |

## Other models

The following models are also available on the Telnyx platform.

| Model ID                                  | Description                                             |
| ----------------------------------------- | ------------------------------------------------------- |
| `Qwen/Qwen3-235B-A22B`                    | Strong function calling and reasoning                   |
| `Groq/kimi-k2-instruct`                   | Open-source instruction-tuned model                     |
| `Groq/llama-4-maverick-17b-128e-instruct` | Open-source instruction-tuned model                     |
| `anthropic/claude-haiku-4-5`              | Fast, lightweight Anthropic model for voice AI and chat |
| `google/gemini-2.5-flash`                 | Google proprietary model                                |
| `openai/gpt-4.1`                          | OpenAI proprietary model                                |
| `openai/gpt-4o`                           | OpenAI proprietary model                                |
| `openai/gpt-5`                            | OpenAI proprietary model                                |
| `openai/gpt-5.1`                          | OpenAI proprietary model                                |
| `openai/gpt-5.2`                          | OpenAI proprietary model                                |
| `fixie-ai/ultravox-v0_4_1-llama-3_1-8b`   | Audio language model for voice input                    |

## Choosing a model

* **General use**: `moonshotai/Kimi-K2.5` offers the best balance of intelligence and cost.
* **Highest quality**: `zai-org/GLM-5` for tasks requiring maximum intelligence.
* **Cost-sensitive**: `MiniMaxAI/MiniMax-M2.5` provides high intelligence at lower cost.
* **Function calling**: `Qwen/Qwen3-235B-A22B` is recommended for [function calling](function-calling.md) workflows.
* **Anthropic**: `anthropic/claude-haiku-4-5` for fast, lightweight responses in [Voice AI Assistants](voice-assistant-quickstart.md).
* **Audio input**: `fixie-ai/ultravox-v0_4_1-llama-3_1-8b` for [audio language models](audio-language-models.md).

## Using a model

Pass the model ID in the `model` parameter of your API request:

```python theme={null}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai",
)

chat_completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2.5",
    messages=[{"role": "user", "content": "Hello!"}],
)
```


## Related Pages

- [Audio Language Models](../runbooks/audio-language-models.md)
