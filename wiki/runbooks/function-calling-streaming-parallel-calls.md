---
title: Function Calling (Streaming + Parallel Calls)
summary: In the [previous tutorial](function-calling.md), we learned the basics for defining and executing functions using our [chat completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion).
sources:
  - url: https://developers.telnyx.com/docs/inference/streaming-functions/index
    content_hash: 8855afd7e87560438774d2075b0a667767bc84bdebd55437f7003e434841b883
updated_at: 2026-04-10T00:00:00Z
---

# Function Calling (Streaming + Parallel Calls)

In the [previous tutorial](function-calling.md), we learned the basics for defining and executing functions using our [chat completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion).

In this tutorial, we will introduce more advanced use cases:

* Streaming function calls
* Passing multiple functions
* Executing function calls in parallel

For low-latency contexts, streaming and parallel calls are especially helpful.

## Defining our functions

First, we will define two functions we want to execute in parallel: `sleep` and `dream`.

Our goal is to use the `dream` function to make an API call to the Telnyx chat completions endpoint while we `sleep`.

We will also re-use the `func_to_tool` helped function we defined in the [previous tutorial](function-calling.md) to easily convert between our Python functions and the JSON we need to pass to the `tools` field for our chat completions API.

> **Note:** Make sure you have set the `TELNYX_API_KEY` environment variable

```python theme={null}
import asyncio
import inspect
import json
import os
from openai import AsyncOpenAI
from pydantic import create_model
