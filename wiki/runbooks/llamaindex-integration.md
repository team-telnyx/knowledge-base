---
title: LlamaIndex Integration
summary: 'LlamaIndex integration for connecting custom data sources to LLMs.'
sources:
  - url: https://developers.telnyx.com/docs/inference/llama-index/index
    content_hash: e6084e3cb890219feabeb2c2278d363707a4015d551424c8fd0253755969b524
updated_at: 2026-04-10T00:00:00Z
---

# LlamaIndex Integration

*LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models (LLMs)*

To use LlamaIndex with Telnyx's OpenAI compatible API run:

* `pip install llama-index-core`

* `pip install llama-index-llms-openai-like`

Here's some sample code to get you started

## Sample Llama Index code

> **Note:** Make sure you have set the `TELNYX_API_KEY` environment variable

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


## Related Pages

- [Langchain Integration](../runbooks/langchain-integration.md)
- [Zapier Integration](../runbooks/zapier-integration.md)
