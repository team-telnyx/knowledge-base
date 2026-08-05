---
title: Function Calling (Streaming + Parallel Calls)
summary: An advanced tutorial on using the Telnyx chat completions API to stream function
  calls and execute multiple tools in parallel, building on the basics covered in
  the introductory functions tutorial.
sources:
- url: https://developers.telnyx.com/docs/inference/streaming-functions
updated_at: 2026-08-05T13:46:43Z
---

# Function Calling (Streaming + Parallel Calls)

*Part 1 of 2 — see also: [Part 2](function-calling-streaming-parallel-calls--part-2.md)*

An advanced tutorial on using the Telnyx chat completions API to stream function calls and execute multiple tools in parallel, building on the basics covered in the introductory functions tutorial.

In the [Functions](functions.md) tutorial, we learned the basics for defining and executing functions using the chat completions API. This tutorial introduces more advanced use cases:

- Streaming function calls
- Passing multiple functions
- Executing function calls in parallel

For low-latency contexts, streaming and parallel calls are especially helpful.

## Defining our functions

First, we will define two functions we want to execute in parallel: `sleep` and `dream`. Our goal is to use the `dream` function to make an API call to the Telnyx chat completions endpoint while we `sleep`. We will also re-use the `func_to_tool` helper function we defined in the [Functions](functions.md) tutorial to easily convert between our Python functions and the JSON we need to pass to the `tools` field for our chat completions API.

Make sure you have set the `TELNYX_API_KEY` environment variable.

```python
import asyncio
import inspect
import json
import os
from openai import AsyncOpenAI
from pydantic import create_model

# Configuration
API_KEY = os.getenv("TELNYX_API_KEY")
BASE_URL = "https://api.telnyx.com/v2/ai/openai"
MODEL = "zai-org/GLM-5.2"

client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL)

async def sleep(seconds: int):
    """Sleep for a given number of seconds."""
    await asyncio.sleep(seconds)
    return f"I slept for {seconds} seconds!"

async def dream(subject: str):
    """Dream about a given subject."""
    chat_completion = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": f"BRIEFLY (one sentence max) describe a dream about {subject}"
            }
        ]
    )
    return chat_completion.choices[0].message.content

def func_to_tool(f):
    """Convert a function to a tool JSON schema."""
    kw = {
        n: (o.annotation, ... if o.default == inspect.Parameter.empty else o.default)
        for n, o in inspect.signature(f).parameters.items()
    }
    schema = create_model(f.__name__, **kw).model_json_schema()
    tool_json = {
        "type": "function",
        "function": {
            "name": schema["title"],
            "description": inspect.getdoc(f),
            "parameters": schema
        }
    }
    return tool_json
```

## Parsing Streaming Tools + Executing Tasks in Parallel

Next we will define a few functions to help us parse and execute tasks in parallel.

### handle_tool_calls

The `handle_tool_calls` function iterates over streamed chunks from the chat completions endpoint. The language model may invoke multiple tool calls to be executed in parallel and will differentiate them using the `index` attribute on the chunk. As we progress through the stream, we build our local copy of this list of function calls in the `tool_calls` list.

The first chunk of a new tool call contains the `name` of the function. This enables you to give early feedback to users that a function will be executed. In this example, we simply print the name of the function when it is detected.

As we build the arguments from the streamed chunks, we attempt to parse what we have built as JSON. Once we have a valid JSON object, we create an async task to be scheduled for execution (if we have not already done so).

**NB: Telnyx guarantees valid JSON is returned for tool calls, so you don't have to worry about lengthy retries or fuzzy matching.**

### execute_tasks

This function executes the tasks from the previous function and returns the results as they are completed, enabling users to receive feedback as soon as possible.

### func_wrapper

This is a trivial helper function that exposes the tool call ID and function name to `execute_tasks`.

```python
async def func_wrapper(func, tool_call_id, **kwargs):
    """Wrap a function to return its ID + name when executed."""
    result = await func(**kwargs)
    return tool_call_id, func.__name__, result

async def execute_tasks(tasks):
    """Execute asynchronous tasks and collect their results."""
    results = []
    for task in asyncio.as_completed(tasks):
        tool_call_id, func_name, result = await task
        print(f"Executed {func_name}, results: {result}")
        results.append(
            {
                "tool_call_id": tool_call_id,
                "role": "tool",
                "name": func_name,
                "content": result,
            }
        )
    return results

async def handle_tool_calls(chat_completion, function_map):
    """Handle streaming tool calls from chat completion."""
    tool_calls = []
    tasks = []
    tasked_tool_ids = set()

    async for chunk in chat_completion:
        delta = chunk.choices[0].delta
        if delta and delta.tool_calls:
            # We have detected tool calls from the LLM
            tcchunklist = delta.tool_calls
            for tcchunk in tcchunklist:
                index = tcchunk.index or 0
                if len(tool_calls) <= index:
                    # Based on the index, we have a new tool call
                    tool_calls.append(
                        {
                            "id": "",
                            "type": "function",
                            "function": {
                                "name": "",
                                "arguments": ""
                            }
                        }
                    )
                tc = tool_calls[index]

                if tcchunk.id:
                    tc["id"] += tcchunk.id
                if tcchunk.function.name:
                    tc["function"]["name"] += tcchunk.function.name
                    print(f"Detected function: {tcchunk.function.name}")
                if tcchunk.function.arguments:
                    tc["function"]["arguments"] += tcchunk.function.arguments
                    try:
                        kwargs = json.loads(tc["function"]["arguments"])
                    except json.JSONDecodeError:
                        # We don't have the full arguments JSON yet
                        continue
                    else:
                        if tc["id"] not in tasked_tool_ids:
                            func_name = tc["function"]["name"]
                            print(f"Executing {func_name} with {kwargs}")
                            wrapped_func = func_wrapper(function_map[func_name], tc["id"], **kwargs)
                            task = asyncio.create_task(wrapped_func)
                            tasks.append(task)
                            tasked_tool_ids.add(tc["id"])

    return tool_calls, tasks
```
