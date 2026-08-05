---
title: Embeddings
summary: Learn how to upload documents to Telnyx Storage, transform them into embeddings,
  and use those embeddings as context for a language model to answer questions over
  your data.
sources:
- url: https://developers.telnyx.com/docs/inference/embeddings/index
updated_at: 2026-08-05T13:45:54Z
---

# Embeddings

Learn how to upload documents to Telnyx Storage, transform them into embeddings, and use those embeddings as context for a language model to answer questions over your data.

## Overview

This tutorial walks through the end-to-end workflow for using embeddings on Telnyx:

- Upload documents to [Telnyx Storage](telnyx-storage.md)
- Transform those documents into embeddings so a language model can retrieve relevant sections
- Provide the storage bucket as context for the language model

## Upload your documents

You can upload objects to Telnyx's S3-Compatible storage API using the [Cloud Storage Quickstart](cloud-storage-quickstart.md) or with the drag-and-drop interface in the [portal](https://portal.telnyx.com/#/storage/buckets).

## Embed your documents

Once your documents are uploaded, you can embed them via the [Embed URL Content API](https://developers.telnyx.com/api-reference/embeddings/embed-url-content#embed-url-content) or by clicking the **Embed for AI Use** button in the portal while viewing your storage bucket's contents.

Behind the scenes, your documents are processed into sections, and each section is embedded based on its contents. Later, when a user asks a language model a question, the most relevant sections of documents from the bucket are automatically provided to help answer the question.

## Chat over your documents

Once your documents are embedded, you can try it out in the [AI Playground in the portal](https://portal.telnyx.com/#/ai/playground) by selecting your embedded bucket from the storage dropdown.

You can also use embeddings via the [Chat Completions API](https://developers.telnyx.com/api-reference/openai-chat/create-a-chat-completion-openai-compatible). The following Python example shows how to stream a chat completion that retrieves context from an embedded bucket.

Make sure the `TELNYX_API_KEY` environment variable is set, and update the `question` and `bucket` variables in the sample code.

```python
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai",
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
  model="zai-org/GLM-5.2",
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

The `retrieval` tool with `bucket_ids` is what tells the model to pull relevant embedded sections from the specified bucket and use them as context for the response.
