---
title: JSON Mode and Beyond
summary: Learn how to guarantee structured output from Telnyx chat completions using
  multiple choice, JSON Schema / Pydantic models, schemaless JSON mode, and regular
  expressions.
sources:
- url: https://developers.telnyx.com/docs/inference/json-mode
updated_at: 2026-08-05T13:46:21Z
---

# JSON Mode and Beyond

Learn how to guarantee structured output from Telnyx chat completions using multiple choice, JSON Schema / Pydantic models, schemaless JSON mode, and regular expressions.

## Overview

Telnyx's chat completions API supports several techniques for guaranteeing structured output from language models. These include:

- **Multiple choice** — restrict the model to one of a fixed set of string values.
- **JSON Schema / Pydantic models** — constrain the model to emit JSON matching a specific schema.
- **Schemaless JSON mode** — force the model to emit valid JSON without enforcing a particular shape.
- **Regular expressions** — constrain the model output to match a regex pattern.

All examples below use the OpenAI Python client pointed at Telnyx's OpenAI-compatible base URL, and assume the `TELNYX_API_KEY` environment variable is set.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai",
)
```

> **Note on reasoning models:** `zai-org/GLM-5.2` is a reasoning model. Structured output still arrives in `choices[0].message.content` — the model's chain-of-thought is returned separately in `choices[0].message.reasoning_content`, so it never pollutes the JSON you parse. To surface the reasoning, read it alongside `content`:
>
> ```python
> message = chat_completion.choices[0].message
> if getattr(message, "reasoning_content", None):
>     print("reasoning:", message.reasoning_content)
> print(message.content)  # the structured output
> ```

## Sentiment Analysis using Multiple Choice

The simplest form of structured output is multiple choice. By passing a `guided_choice` array in `extra_body`, the model is restricted to one of the listed values. In the example below, the only possible outputs are `positive` or `negative`.

```python
chat_completion = client.chat.completions.create(
    model="zai-org/GLM-5.2",
    messages=[
        {"role": "system", "content": "Classify the sentiment of this review as positive or negative."},
        {"role": "user", "content": "The staff went above and beyond! I had a great stay."}
    ],
    temperature=0.0,
    extra_body={
      "guided_choice": ["positive", "negative"]
    }
)
print(chat_completion.choices[0].message.content)
```

## Building on this with `guided_json`

To capture additional fields alongside the classification — for example, an explanation — use the `guided_json` field with a JSON Schema object.

```python
chat_completion = client.chat.completions.create(
    model="zai-org/GLM-5.2",
    messages=[
        {"role": "system", "content": "First describe the sentiment of the following review and then use that to classify the sentiment as positive or negative."},
        {"role": "user", "content": "The staff went above and beyond! I had a great stay."}
    ],
    temperature=0.0,
    extra_body={
      "guided_json": {
        "type": "object",
        "properties": {
          "sentiment": {
            "type": "string",
            "enum": ["positive", "negative"]
          },
          "explanation": {"type": "string"}
        },
        "required": ["sentiment", "explanation"]
      }
    }
)
print(chat_completion.choices[0].message.content)
```

This guarantees a JSON response matching the schema, for example:

```json
{
  "sentiment": "positive",
  "explanation": "The review mentions that the staff went above and beyond and the user had a great stay, which indicates a positive sentiment."
}
```

## Simplifying Schema Generation using Pydantic

Writing JSON Schema by hand is verbose. Pydantic models can generate the same schema automatically. The following is functionally equivalent to the previous example.

```python
import os
from enum import Enum
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai",
)

class Sentiment(str, Enum):
    positive = 'positive'
    negative = 'negative'

class SentimentAnalysis(BaseModel):
    explanation: str
    sentiment: Sentiment

chat_completion = client.chat.completions.create(
    model="zai-org/GLM-5.2",
    messages=[
        {"role": "system", "content": "First describe the sentiment of the following review and then use that to classify the sentiment as positive or negative."},
        {"role": "user", "content": "The staff went above and beyond! I had a great stay."}
    ],
    temperature=0.0,
    extra_body={
      "guided_json": SentimentAnalysis.model_json_schema()
    }
)
print(chat_completion.choices[0].message.content)
```

## Schema-Less JSON Mode

If you only need valid JSON without enforcing a particular shape, Telnyx supports the schemaless JSON mode provided by OpenAI via `response_format={"type": "json_object"}`.

```python
chat_completion = client.chat.completions.create(
    model="zai-org/GLM-5.2",
    messages=[
        {"role": "system", "content": "First describe the sentiment of the following review and then use that to classify the sentiment as positive or negative. Please respond using a JSON object."},
        {"role": "user", "content": "The staff went above and beyond! I had a great stay."}
    ],
    temperature=0.0,
    response_format={"type": "json_object"}
)
print(chat_completion.choices[0].message.content)
```

## Constraining Output with Regular Expressions

For finer-grained control, you can constrain the model output to match a regex pattern using `guided_regex`. This is especially useful in voice contexts where you may want to limit response length. The example below limits the response to a single sentence of 20 words or fewer.

```python
chat_completion = client.chat.completions.create(
    model="zai-org/GLM-5.2",
    messages=[
        {"role": "system", "content": "You are a concise and helpful AI assistant."},
        {"role": "user", "content": "Can you tell me about 10DLC?"}
    ],
    temperature=0.0,
    extra_body={
      "guided_regex": "(\\w+\\s*){1,20}[\.!?]"
    }
)
print(chat_completion.choices[0].message.content)
```

## Reference

- [Create a chat completion (OpenAI compatible)](https://developers.telnyx.com/api-reference/openai-chat/create-a-chat-completion-openai-compatible)
