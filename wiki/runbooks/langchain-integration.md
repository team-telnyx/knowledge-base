---
title: Langchain Integration
summary: 'LangChain framework integration for developing applications powered by LLMs.'
sources:
  - url: https://developers.telnyx.com/docs/inference/langchain-integration/index
    content_hash: e11f6fff35038cfb2a1189e57d82ed2b9e7b151ff86c8777654c1a061b99468d
updated_at: 2026-04-10T00:00:00Z
---

# Langchain Integration

## Langchain

*LangChain is a framework for developing applications powered by large language models (LLMs)*

To use Langchain with Telnyx's OpenAI compatible API run:

`pip install langchain-openai`

Here's some sample code to get you started

## Langchain Sample Code

```python theme={null}
import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.telnyx.com/v2/ai",
    api_key=os.getenv("TELNYX_API_KEY"),
    model="meta-llama/Meta-Llama-3.1-8B-Instruct"
)

for chunk in llm.stream("Help me plan my vacation"):
    print(chunk.content, end="", flush=True)
```

*Note: Make sure you have set the TELNYX\_API\_KEY environment variable*

## LlamaIndex

*LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models (LLMs)*

To use LlamaIndex with Telnyx's OpenAI compatible API run:

```shell theme={null}
pip install llama-index-core
pip install llama-index-llms-openai-like
```

Here's some sample code to get you started

```python theme={null}
import os
from llama_index.llms.openai_like import OpenAILike
from llama_index.core.llms import ChatMessage

llm = OpenAILike(
    api_base="https://api.telnyx.com/v2/ai",
    api_key=os.getenv("TELNYX_API_KEY"),
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    is_chat_model=True,
)

chat = llm.stream_chat(
    [
        ChatMessage(role="user", content="help me plan my vacation"),
    ]
)
for chunk in chat:
    print(chunk.delta, end="")
```

*Note: Make sure you have set the TELNYX\_API\_KEY environment variable*


## Related Pages

- [LlamaIndex Integration](../runbooks/llamaindex-integration.md)
- [Zapier Integration](../runbooks/zapier-integration.md)
