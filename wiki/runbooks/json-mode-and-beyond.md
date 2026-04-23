---
title: JSON Mode and Beyond
summary: 'Tutorial on using JSON mode with Telnyx Inference API.'
sources:
  - url: https://developers.telnyx.com/docs/inference/json-mode/index
    content_hash: 9598fd4e65f7c528ee277398cdee5cf1ef520adff8308a2330060d86d17ea26d
updated_at: 2026-04-10T00:00:00Z
---

# JSON Mode and Beyond

In this tutorial, you'll learn how to: Start building on Telnyx today.

In this tutorial, you'll learn how to:

* Guarantee structured output using our [chat completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion)
* This can be done using JSON Schema / Pydantic models, (schemaless) JSON Mode, regular expressions, and multiple choice.

## Sentiment Analysis using Multiple Choice

One of the simplest forms of structured output is multiple choice.

The only possible outputs of the following code snippet are `positive` or `negative`.

> **Note:** Make sure you have set the `TELNYX_API_KEY` environment variable

```python theme={null}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai",
)

chat_completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
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

Now let's say we want to capture an explanation for the classification as well. We can leverage the `guided_json` field for this.

```python theme={null}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai",
)

chat_completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
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

This will ensure a JSON response with the same schema as the following

```
{
  "sentiment": "positive",
  "explanation": "The review mentions that the staff went above and beyond and the user had a great stay, which indicates a positive sentiment."
}
```

## Simplifying Schema Generation using Pydantic

The above is helpful to see the raw JSON Schema specification being sent via API. However, for practical purposes, using Pydantic models can help simplify generating the specs. The following is functionally equivalent to the previous example.

```python theme={null}
import os
from enum import Enum
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai",
)

class Sentiment(str, Enum):
    positive = 'positive'
    negative = 'negative'

class SentimentAnalysis(BaseModel):
    explanation: str
    sentiment: Sentiment

chat_completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
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

## Schema-less JSON Mode

We also support the schema-less JSON mode provided by OpenAI

```python theme={null}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai",
)

chat_completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=[
        {"role": "system", "content": "First describe the sentiment of the following review and then use that to classify the sentiment as positive or negative. Please respond using a JSON object."},
        {"role": "user", "content": "The staff went above and beyond! I had a great stay."}
    ],
    temperature=0.0,
    response_format={"type": "json_object"}
)
print(chat_completion.choices[0].message.content)
```

## And now for something completely different (regular expressions)

You can do a lot with regular expressions, and now you can ensure language model outputs follow a regex. Something we see a lot, especially in a voice context, is wanting to limit the length of a response. Below is a toy example limiting a response to a sentence with 20 words or fewer.

```python theme={null}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai",
)

chat_completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
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
