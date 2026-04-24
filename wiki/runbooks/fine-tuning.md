---
title: Fine Tuning
summary: In this tutorial, you'll learn how to.
sources:
  - url: https://developers.telnyx.com/docs/inference/fine-tuning/index
    content_hash: af64aac05cc154e2b75a5676903936fc8e3979241ec11f7cb87efbbbf6a85deb
updated_at: 2026-04-10T00:00:00Z
---

# Fine Tuning

In this tutorial, you'll learn how to:

* Upload documents to [Telnyx Storage](https://telnyx.com/products/cloud-storage)
* Customize a language model for your unique needs, using those documents
* Chat with this fine-tuned language model in the portal or via API

Like most fine-tuning providers, Telnyx supports the standard `.jsonl` training file as input.

Unlike most fine-tuning providers, Telnyx will also use AI to generate a training file from your raw documents automatically. This is the workflow covered in this tutorial.

## Upload your documents

You can upload objects to Telnyx's S3-Compatible storage API using our [quickstart](https://developers.telnyx.com/docs/cloud-storage/quick-start) or with our [drag-and-drop interface in the portal](https://portal.telnyx.com/#/storage/buckets).

<img alt="AI Storage Portal" />

## Fine-tune a language model on your documents

Once you've uploaded your documents, you can [fine tune on them via API](https://developers.telnyx.com/api-reference/fine-tuning/create-a-fine-tuning-job#create-a-fine-tuning-job) or by navigating to the [fine-tuning tab in the portal](https://portal.telnyx.com/#/ai/fine-tuning). Once there you can select a base model to train and the bucket with your training documents.

<img alt="AI Fine Tune Creation" />

Behind the scenes, your documents will be automatically converted with AI into a `.jsonl` training file. Immediately after, we will begin fine-tuning your model using this training file.

This whole process may take several minutes to complete. You can monitor the status of your fine-tuning job in the fine-tuning tab.

<img alt="AI Fine Tune List" />

## Chat with your new model

Once your model is fine-tuned, you can try it out in the [AI Playground in the portal](https://portal.telnyx.com/#/ai/playground) by selecting your model in the dropdown.

You can also use your fine-tuned model via our [chat completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion#create-a-chat-completion). Here is a Python example.

> **Note:** Make sure you have set the `TELNYX_API_KEY` environment variable. Also, update the `question` and `model` variables in the sample code.

```python theme={null}
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai",
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
