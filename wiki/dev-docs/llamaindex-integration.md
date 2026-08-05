---
title: LlamaIndex Integration
summary: Use LlamaIndex with Telnyx Inference through the OpenAI-compatible API by
  pointing the `OpenAILike` client at the Telnyx AI endpoint. This page covers setup,
  streaming chat usage, and combining the integration with Telnyx Embeddings for retrieval-augmented
  generation.
sources:
- url: https://developers.telnyx.com/docs/inference/llama-index
updated_at: 2026-08-05T13:46:17Z
---

# LlamaIndex Integration

Use LlamaIndex with Telnyx Inference through the OpenAI-compatible API by pointing the `OpenAILike` client at the Telnyx AI endpoint. This page covers setup, streaming chat usage, and combining the integration with Telnyx Embeddings for retrieval-augmented generation.

## Setup

Install the LlamaIndex core package and the OpenAI-like LLM adapter:

```
pip install llama-index-core llama-index-llms-openai-like
```

The Telnyx Inference API is OpenAI-compatible, so you can use LlamaIndex's `OpenAILike` client by swapping the `api_base` to the Telnyx endpoint.

## Usage

Instantiate the `OpenAILike` client pointed at the Telnyx AI endpoint and stream a chat completion:

```python
import os
from llama_index.llms.openai_like import OpenAILike
from llama_index.core.lls import ChatMessage

llm = OpenAILike(
    api_base="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
    model="zai-org/GLM-5.2",
    is_chat_model=True,
)

chat = llm.stream_chat([ChatMessage(role="user", content="Help me plan my vacation")])
for chunk in chat:
    print(chunk.delta, end="")
```

The `api_key` should be set to your Telnyx API key, typically loaded from an environment variable. Set `is_chat_model=True` so the client uses the chat completions interface, and pass any supported Telnyx model identifier in the `model` field.

## RAG with Embeddings

Combine the LlamaIndex integration with [Embeddings](embeddings.md) to build retrieval-augmented generation (RAG) pipelines. The Telnyx Embeddings service handles document upload and indexing, while the LlamaIndex chat model retrieves relevant context and generates responses. See the [Embeddings](embeddings.md) guide for details on uploading and indexing documents.
