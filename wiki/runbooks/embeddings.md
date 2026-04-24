---
title: Embeddings
summary: In this tutorial, you'll learn how to.
sources:
  - url: https://developers.telnyx.com/docs/inference/embeddings/index
    content_hash: 2d214e90da9bbe71e06b1adab3cef450a88acae5ff63b92f4ea9e99789f0163e
updated_at: 2026-04-10T00:00:00Z
---

# Embeddings

In this tutorial, you'll learn how to:

* Upload documents to [Telnyx Storage](https://telnyx.com/products/cloud-storage)
* Transform these documents into embeddings, enabling a language model to retrieve relevant sections of your documents
* Provide the storage bucket as context for the language model

## Upload your documents

You can upload objects to Telnyx's S3-Compatible storage API using our [quickstart](https://developers.telnyx.com/docs/cloud-storage/quick-start) or with our [drag-and-drop interface in the portal](https://portal.telnyx.com/#/storage/buckets).

## Embed your documents

Once you've uploaded your documents, you can [embed them via API](https://developers.telnyx.com/api-reference/embeddings/embed-url-content#embed-url-content) or by clicking the "Embed for AI Use" button in the portal while viewing your storage bucket's contents.

Behind the scenes, your documents will be processed into sections and each section will be "embedded" based on its contents. Later, when a user asks a language model a question, it will automatically be provided with the most relevant sections of documents from the bucket to help answer the question.

## Chat over your documents

Once your documents are embedded, you can try it out in the [AI Playground in the portal](https://portal.telnyx.com/#/ai/playground) by selecting your embedded bucket from the storage dropdown.

You can also use embeddings via our [chat completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion#create-a-chat-completion). Here is a Python example.

> **Note:** Make sure you have set the `TELNYX_API_KEY` environment variable. Also, update the `question` and `bucket` variables in the sample code.

```python theme={null}
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai",
)

question = "<ADD QUESTION HERE>"
bucket = "<ADD EMBEDDED BUCKET HERE>"
chat_completion = client.chat.completions.create(
  messages=[
    {
        "role": "user",
        "content": question
    }
  ],
  model="meta-llama/Meta-Llama-3.1-8B-Instruct",
  stream=True,
  tools=[
    {
        "type": "retrieval",
        "retrieval": {
            "bucket_ids": [bucket]
        }
    }
  ]
)

for chunk in chat_completion:
  if chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="", flush=True)
```
