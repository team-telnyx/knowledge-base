---
title: OpenAI API Migration Guide
summary: Migrate from the OpenAI API to Telnyx by swapping two environment variables
  and updating the model name. The Telnyx inference endpoint is OpenAI-compatible,
  exposing chat completions and transcriptions endpoints with a superset of supported
  parameters, plus a `reasoning_content` field for reasoning models.
sources:
- url: https://developers.telnyx.com/docs/inference/openai
updated_at: 2026-08-05T13:46:31Z
---

# OpenAI API Migration Guide

Migrate from the OpenAI API to Telnyx by swapping two environment variables and updating the model name. The Telnyx inference endpoint is OpenAI-compatible, exposing chat completions and transcriptions endpoints with a superset of supported parameters, plus a `reasoning_content` field for reasoning models.

## Overview

Migrating from the OpenAI API to Telnyx requires only two changes: swap the base URL and API key environment variables, and update the model name. The Telnyx inference endpoint at `https://api.telnyx.com/v2/ai/openai` is fully compatible with the OpenAI Python SDK.

## Quick Start

Set the environment variables and instantiate the OpenAI client as usual:

```
export OPENAI_BASE_URL='https://api.telnyx.com/v2/ai/openai'
export OPENAI_API_KEY='KEY***'
```

```python
from openai import OpenAI

client = OpenAI()  # picks up env vars
chat_completion = client.chat.completions.create(
    model="zai-org/GLM-5.2",
    messages=[{"role": "user", "content": "Tell about Telnyx"}],
    temperature=0.0,
    stream=True,
)
```

Alternatively, pass the credentials and base URL explicitly:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai",
)
chat_completion = client.chat.completions.create(
    model="zai-org/GLM-5.2",
    messages=[{"role": "user", "content": "Tell about Telnyx"}],
    temperature=0.0,
    stream=True,
)
```

## Reasoning Models

Reasoning models such as `zai-org/GLM-5.2` expose a `reasoning_content` field alongside the standard `content` field. It contains the model's chain-of-thought and appears on `message` for non-streaming responses or `delta` for streaming responses. Read it the same way you read `content`:

```python
chat_completion = client.chat.completions.create(
    model="zai-org/GLM-5.2",
    messages=[{"role": "user", "content": "Tell about Telnyx"}],
)
message = chat_completion.choices[0].message

# Reasoning models populate reasoning_content; other models leave it None.
if getattr(message, "reasoning_content", None):
    print("reasoning:", message.reasoning_content)
print("answer:", message.content)
```

## Chat Completions Compatibility

Telnyx supports a superset of OpenAI's chat completions parameters. The following table compares parameter support:

| Parameter | Telnyx | OpenAI |
| --- | --- | --- |
| `messages` | ✅ | ✅ |
| `model` | ✅ | ✅ |
| `stream` | ✅ | ✅ |
| `max_tokens` | ✅ | ✅ |
| `temperature` | ✅ | ✅ |
| `top_p` | ✅ | ✅ |
| `frequency_penalty` | ✅ | ✅ |
| `presence_penalty` | ✅ | ✅ |
| `n` | ✅ | ✅ |
| `stop` | ✅ | ✅ |
| `logit_bias` | ✅ | ✅ |
| `logprobs` | ✅ | ✅ |
| `top_logprobs` | ✅ | ✅ |
| `seed` | ✅ | ✅ |
| `response_format` | ✅ | ✅ |
| `tool_choice` | ✅ | ✅ |
| `tools` | ✅ | ✅ |
| `function` | ✅ | ✅ |
| `retrieval` | ✅ | ❌ |
| `guided_json` | ✅ | ❌ |
| `guided_regex` | ✅ | ❌ |
| `guided_choice` | ✅ | ❌ |
| `min_p` | ✅ | ❌ |
| `use_beam_search` | ✅ | ❌ |
| `best_of` | ✅ | ❌ |
| `length_penalty` | ✅ | ❌ |
| `early_stopping` | ✅ | ❌ |
| `user` | ❌ | ✅ |

Telnyx-exclusive parameters include `retrieval`, `guided_json`, `guided_regex`, `guided_choice`, `min_p`, `use_beam_search`, `best_of`, `length_penalty`, and `early_stopping`. The `user` parameter is not supported on Telnyx.

## Transcriptions Compatibility

The transcriptions endpoint also mirrors OpenAI's interface, with a few differences:

| Parameter | Telnyx | OpenAI |
| --- | --- | --- |
| `file` | ✅ | ✅ |
| `model` | ✅ | ✅ |
| `response_format` | ✅ | ✅ |
| `timestamp_granularities[]` → `segment` | ✅ | ✅ |
| `timestamp_granularities[]` → `word` | ❌ | ✅ |
| `language` | ❌ | ✅ |
| `prompt` | ❌ | ✅ |
| `temperature` | ❌ | ✅ |

Telnyx supports `segment`-level timestamp granularities but not `word`-level. The `language`, `prompt`, and `temperature` parameters are not currently supported on the Telnyx transcriptions endpoint.
