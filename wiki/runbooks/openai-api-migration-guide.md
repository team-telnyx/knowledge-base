---
title: OpenAI API Migration Guide
summary: OpenAI API Migration Guide.
sources:
  - url: https://developers.telnyx.com/docs/inference/openai/index
    content_hash: e00e155904f3d22c17a44f650f9ecdc737f4abb3726aeda01f50ee7e5bbc8129
updated_at: 2026-04-10T00:00:00Z
---

# OpenAI API Migration Guide

OpenAI API Migration Guide

We've worked to make migration from OpenAI to Telnyx as painless as possible.

You will only need to:

1. Set the `OPENAI_BASE_URL` and `OPENAI_API_KEY` environment variables
2. Use an open-source `model` supported by Telnyx

Set the environment variables...

* `export OPENAI_BASE_URL='https://api.telnyx.com/v2/ai'`
* `export OPENAI_API_KEY='KEY***'`

and this code will work!

## OpenAI example

```python theme={null}
from openai import OpenAI

client = OpenAI()
chat_completion = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=[
        {"role": "user", "content": "Tell me about Telnyx"}
    ],
    temperature=0.0,
    stream=True,
)
```

If you'd like to use different environment variables, you may also pass these fields in the client constructor

```python theme={null}
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url=os.getenv("TELNYX_BASE_URL")
)
chat_completion = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=[
        {"role": "user", "content": "Tell me about Telnyx"}
    ],
    temperature=0.0,
    stream=True,
)
```

Telnyx supports the vast majority of parameters for Chat and Audio (and a few helpful ones that OpenAI does not).

See the full compatibility matrix below.


## Related Pages

- [Twilio Migration Guide](../reference/twilio-migration-guide.md)
