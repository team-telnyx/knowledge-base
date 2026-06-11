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

*Part 1 of 3 — see also: [Part 2](telnyx-inference-2--part-2.md), [Part 3](telnyx-inference-2--part-3.md)*

Telnyx Inference provides OpenAI-compatible API access to open-source LLMs hosted on Telnyx GPU infrastructure across four global regions. Swap your base URL and API key to integrate with frameworks like LangChain, LlamaIndex, CrewAI, and LiveKit, or route all OpenAI SDK calls through Telnyx with zero code changes via environment variables.

## OpenAI-Compatible API

Telnyx exposes an OpenAI-compatible endpoint at `https://api.telnyx.com/v2/ai/openai`. To migrate, swap `base_url` and `api_key` in any framework that supports OpenAI:

```python
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai",
)
chat_completion = client.chat.completions.create(
    model="zai-org/GLM-5.1-FP8",
    messages=[{"role": "user", "content": "Tell me about Telnyx"}],
    temperature=0.0,
    stream=True,
)
```

### Reasoning Models

Reasoning models such as `zai-org/GLM-5.1-FP8` add a `reasoning_content` field alongside the usual `content`. It holds the model's chain-of-thought and appears on `message` (non-streaming) or `delta` (streaming):

```python
chat_completion = client.chat.completions.create(
    model="zai-org/GLM-5.1-FP8",
    messages=[{"role": "user", "content": "Tell me about Telnyx"}],
)
message = chat_completion.choices[0].message
if getattr(message, "reasoning_content", None):
    print("reasoning:", message.reasoning_content)
print("answer:", message.content)
```

### Chat Completions Compatibility

The following parameters are supported in the Telnyx Chat Completions API. Parameters marked as Telnyx-only go beyond the OpenAI spec:

| Parameter | Telnyx | OpenAI |
|---|---|---|
| `messages`, `model`, `stream`, `max_tokens`, `temperature`, `top_p` | ✅ | ✅ |
| `frequency_penalty`, `presence_penalty`, `n`, `stop`, `logit_bias` | ✅ | ✅ |
| `logprobs`, `top_logprobs`, `seed`, `response_format` | ✅ | ✅ |
| `tool_choice`, `tools`, `function` | ✅ | ✅ |
| `retrieval` | ✅ | ❌ |
| `guided_json`, `guided_regex`, `guided_choice` | ✅ | ❌ |
| `min_p`, `use_beam_search`, `best_of` | ✅ | ❌ |
| `length_penalty`, `early_stopping` | ✅ | ❌ |
| `user` | ❌ | ✅ |

### Transcriptions Compatibility

| Parameter | Telnyx | OpenAI |
|---|---|---|
| `file`, `model`, `response_format` | ✅ | ✅ |
| `timestamp_granularities[]` → `segment` | ✅ | ✅ |
| `timestamp_granularities[]` → `word` | ❌ | ✅ |
| `language`, `prompt`, `temperature` | ❌ | ✅ |

## Available Models

All models are accessible via the OpenAI-compatible Chat Completions API.

### Chat Models

| Model ID | Parameters | Context Length | Best For |
|---|---|---|---|
| `moonshotai/Kimi-K2.6` | 1.0T | 256K | Highest intelligence, voice AI (with thinking disabled) **(Recommended)** |
| `zai-org/GLM-5.1-FP8` | 753.9B | 202K | Most efficient reasoning, function calling |
| `MiniMaxAI/MiniMax-M2.7` | — | 2M | Cheapest while maintaining high intelligence |

### Embedding Models

| Model ID | Dimensions | Best For |
|---|---|---|
| `thenlper/gte-large` | 1024 | Text embeddings |

## Regions and Routing

Telnyx runs GPU infrastructure across four regions on three continents:

| Region | Location |
|---|---|
| US East | Atlanta |
| US West | Denver |
| EU | Paris |
| Asia-Pacific | Sydney |

Inference processing is latency-based and best-effort, influenced by the ingress domain you call — not by your account's data locality setting:

| Ingress domain | Preferred region |
|---|---|
| `api.telnyx.com` | US |
| `api.telnyx.eu` | EU |
| `api.telnyx.com.au` | APAC |

Calling a regional ingress domain directs requests to the nearest GPU region under normal conditions. Telnyx does **not guarantee** processing location: during failover or capacity events, requests are processed at the next-lowest-latency region rather than failing.

Processing location and storage location are controlled separately. The **chat completions** endpoint does not store request or response data. The **responses** endpoint stores conversations, and that storage is governed by your Data Locality setting. For a full cross-product breakdown, see the [Data Residency & Compliance FAQ](data-residency-compliance-faq.md).

## Pricing

Pay-per-token with no minimums or commitments. For current per-model pricing, see [telnyx.com/pricing/inference-api](https://telnyx.com/pricing/inference-api).

| Category | Basis | Notes |
|---|---|---|
| Text generation | Per 1M tokens (input + output) | Input and output priced separately; cached input tokens at a discount |
| Audio transcription | Per second of audio | Varies by model |
| Text-to-speech | Per 1M characters | Varies by voice/model |
| Embeddings | Per 1M tokens | Single rate |

## Environment Variables

Route all OpenAI SDK calls through Telnyx with no code changes by setting two environment variables:

```bash
export OPENAI_API_KEY=your_telnyx_api_key
export OPENAI_BASE_URL=https://api.telnyx.com/v2/ai/openai
```

The OpenAI SDK picks these up automatically when you instantiate `OpenAI()` with no arguments.
