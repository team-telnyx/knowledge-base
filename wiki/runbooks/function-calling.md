---
title: Function Calling
summary: In this tutorial, you'll learn how to connect large language models to external tools using our [chat completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion).
sources:
  - url: https://developers.telnyx.com/docs/inference/functions/index
    content_hash: 0e9fcffb6a70e5dac21c22a08b5ddb392970b0bbd5022eec169984864c94ee71
updated_at: 2026-04-10T00:00:00Z
---

# Function Calling

In this tutorial, you'll learn how to connect large language models to external tools using our [chat completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion). This includes:

* Defining a function
* Enabling the language model to choose the function
* Executing the function
* Sharing the results with the language model

## Introduction

Using the `tools` field, you can enable a language model to choose functions to call. The [chat completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion) does not call the function itself. It will return the arguments you need to execute the function yourself.

Of the open-source language models hosted on Telnyx, `Qwen/Qwen3-235B-A22B` is especially good at calling functions. While we recommend you start with this model, every model in our API supports the `tools` interface.

## Simple `get_current_weather` example

A popular toy example for function calls is the `get_current_weather` example.

The following code defines a function and passes it to the language model via the `tools` field.

> **Note:** Make sure you have set the `TELNYX_API_KEY` environment variable.

```python theme={null}
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The temperature unit to use",
                    },
                },
                "required": ["location", "unit"],
            },
        }
    }
]

messages = [
    {"role": "user", "content": "How is the weather in Chicago?"}
]

chat_completion = client.chat.completions.create(
    model="Qwen/Qwen3-235B-A22B",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)
print(chat_completion.choices[0].message)
```

A `tool_choice` of `auto` lets the language model decide to call a function (or not).

The options for `tool_choice` are:

* `required`: this forces the language model to choose a tool
* `none`: this forces the language model to NOT choose a tool
* `auto`: this lets the language model decide

If the language model chooses a function, the above will result in a response like this, with the `tool_calls` field populated.

```
ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_c31258d2-78a8-4566-b716-e3b2a774cbdb', function=Function(arguments='{"location": "Chicago", "unit": "fahrenheit"}', name='get_current_weather'), type='function')])
```

## Defining functions programmatically

In the next example, we will implement and execute `get_current_weather`. To do this cleanly, we are first going to define a helper function `func_to_tool` that extends the `schema` function from Jeremy Howard's [A Hacker's Guide to Language Models](https://github.com/fastai/lm-hackers/blob/main/lm-hackers.ipynb).

```python theme={null}
import inspect
import os
import json
from typing import Literal

from openai import OpenAI
from pydantic import create_model

def func_to_tool(f):
    kw = {
        n: (o.annotation, ... if o.default==inspect.Parameter.empty else o.default)
        for n, o in inspect.signature(f).parameters.items()
        }
    s = create_model(f.__name__, **kw).model_json_schema()
    tool_json = {
        "type": "function",
        "function": {
            "name": s["title"],
            "description": inspect.getdoc(f),
            "parameters": s
        }
    }
    return tool_json

TempUnit = Literal['celsius', 'fahrenheit']

def get_current_weather(location: str, unit: TempUnit = 'fahrenheit'):
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": unit})
    elif "chicago" in location.lower():
        return json.dumps({"location": "Chicago", "temperature": "22", "unit": unit})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai",
)
tools = [func_to_tool(get_current_weather)]
messages = [
    {"role": "user", "content": "How is the weather in Chicago?"}
]
chat_completion = client.chat.completions.create(
    model="Qwen/Qwen3-235B-A22B",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)
print(chat_completion.choices[0].message)
```

This is now functionally equivalent to the first example, but instead of writing and maintaining the verbose JSON definition ourselves, we can generate it programmatically from the executable Python function.

## Executing functions

Ok, it's nice that the language model wants to execute the `get_current_weather`, but how do we actually do that, and incorporate the results back into the interaction?

Continuing from the `chat_completion` response in the previous example

```python theme={null}
assistant_message = chat_completion.choices[0].message
tool_calls = assistant_message.tool_calls
content = assistant_message.content
if tool_calls:
    messages.append(assistant_message)
    available_functions = {"get_current_weather": get_current_weather}
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_response = function_to_call(**function_args)
        messages.append(
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            }
        )
    second_chat_completion = client.chat.completions.create(
        model="Qwen/Qwen3-235B-A22B",
        messages=messages,
    )
    print(second_chat_completion.choices[0].message.content)
else:
    print(content)
```

Now, we will get our answer from the language model, incorporating the output from the function call.

```
It's 22°F in Chicago.
```


## Related Pages

- [SIP URI Calling](../runbooks/sip-uri-calling.md)
