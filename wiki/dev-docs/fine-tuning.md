---
title: Fine Tuning
summary: Learn how to upload documents to Telnyx Storage, fine-tune a language model
  on those documents, and chat with the resulting custom model via the portal or API.
sources:
- url: https://developers.telnyx.com/docs/inference/fine-tuning
updated_at: 2026-08-05T13:46:02Z
---

# Fine Tuning

Learn how to upload documents to Telnyx Storage, fine-tune a language model on those documents, and chat with the resulting custom model via the portal or API.

## Overview

This tutorial walks through the end-to-end fine-tuning workflow on Telnyx:

- Upload documents to [Cloud Storage](cloud-storage.md)
- Customize a language model for your unique needs, using those documents
- Chat with the fine-tuned language model in the portal or via API

Like most fine-tuning providers, Telnyx supports the standard `.jsonl` training file as input. Unlike most providers, Telnyx can also use AI to generate a training file from your raw documents automatically. This tutorial covers that automated workflow.

## Upload your documents

Upload objects to Telnyx's S3-compatible storage API using the [Cloud Storage](cloud-storage.md) quickstart, or use the drag-and-drop interface in the [portal storage buckets view](https://portal.telnyx.com/#/storage/buckets).

![AI Storage Portal](https://mintcdn.com/telnyx/4tBNWGoUCO9azKQ0/img/fine-tuning-storage.png?fit=max&auto=format&n=4tBNWGoUCO9azKQ0&q=85&s=15516f75b2367c77bb6a4b22da45bc74)

## Fine-tune a language model on your documents

Once documents are uploaded, kick off a fine-tuning job via the [Create a fine-tuning job API endpoint](https://developers.telnyx.com/api-reference/fine-tuning/create-a-fine-tuning-job#create-a-fine-tuning-job) or by navigating to the [fine-tuning tab in the portal](https://portal.telnyx.com/#/ai/fine-tuning). From there, select a base model to train and the bucket containing your training documents.

![AI Fine Tune Creation](https://mintcdn.com/telnyx/4tBNWGoUCO9azKQ0/img/fine-tuning-create.png?fit=max&auto=format&n=4tBNWGoUCO9azKQ0&q=85&s=0e97c5107ddabb480018cf1cf4991085)

Behind the scenes, your documents are automatically converted with AI into a `.jsonl` training file, and fine-tuning begins immediately using that file. The whole process may take several minutes to complete. Monitor the status of your fine-tuning job in the fine-tuning tab.

![AI Fine Tune List](https://mintcdn.com/telnyx/4tBNWGoUCO9azKQ0/img/fine-tuning-list.png?fit=max&auto=format&n=4tBNWGoUCO9azKQ0&q=85&s=27e1e4df4d0f279d63ff0588e1016682)

## Chat with your new model

Once the model is fine-tuned, try it out in the [AI Playground in the portal](https://portal.telnyx.com/#/ai/playground) by selecting the model from the dropdown.

The fine-tuned model can also be used via the [chat completions API](https://developers.telnyx.com/api-reference/openai-chat/create-a-chat-completion-openai-compatible). The following Python example uses the OpenAI-compatible client. Make sure the `TELNYX_API_KEY` environment variable is set, and update the `question` and `model` variables in the sample code.

```python
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai",
)

question = "<ADD QUESTION HERE>"
model = "<ADD FINE TUNED MODEL NAME HERE>"
chat_completion = client.chat.completions.create(
  messages=[
    {
        "role": "user",
        "content": question
    }
  ],
  model=model,
  stream=True
)

for chunk in chat_completion:
  if chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="", flush=True)
```
