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

*Part 2 of 2 — see also: [Part 1](function-calling-streaming-parallel-calls--part-1.md)*

An advanced tutorial on using the Telnyx chat completions API to stream function calls and execute multiple tools in parallel, building on the basics covered in the introductory functions tutorial.

## Putting it all together

With our helper functions defined, we are ready to stream and execute multiple function calls in parallel. In this code, we:

- Ask the language model to `sleep` and `dream` at the same time
- Execute the returned tool calls in parallel
- Provide the results back to the language model and get a final response

```python
async def main():
    prompt = "Take a quick 10 second power nap and dream about Telnyx. Then write a haiku about it!"
    messages = [{"role": "user", "content": prompt}]
    print(f"Prompt: {prompt}")
    
    functions = [sleep, dream]
    function_map = {f.__name__: f for f in functions}
    tools = [func_to_tool(func) for func in functions]

    chat_completion = await client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="required",
        stream=True
    )

    tool_calls, tasks = await handle_tool_calls(chat_completion, function_map)

    messages.append(
        {
            "role": "assistant",
            "tool_calls": tool_calls,
        }
    )

    task_results = await execute_tasks(tasks)
    messages.extend(task_results)

    print("Sending results back to LLM...")
    print()
    second_chat_completion = await client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True,
    )

    # GLM-5.2 is a reasoning model: stream reasoning_content (its thinking) and
    # content (the final answer) separately. Non-reasoning models omit the former.
    async for chunk in second_chat_completion:
        delta = chunk.choices[0].delta
        if getattr(delta, "reasoning_content", None):
            print(delta.reasoning_content, end="", flush=True)
        if delta.content:
            print(delta.content, end="", flush=True)
    print()

if __name__ == "__main__":
    asyncio.run(main())
```

The output of the print statements in this script will look something like this. Notice that `sleep` was detected and executed first, but `dream` still returned results first.

```
Prompt: Take a quick 10 second power nap and dream about Telnyx. Then write a haiku about it!
Detected function: sleep
Executing sleep with {'seconds': 10}
Detected function: dream
Executing dream with {'subject': 'Telnyx'}
Executed dream, results: In my dream, I was walking through a futuristic cityscape where Telnyx's logo was emblazoned on skyscrapers, and I could hear the hum of millions of concurrent voice calls and messages being transmitted seamlessly through their network.
Executed sleep, results: I slept for 10 seconds!
Sending results back to LLM...

Here is a haiku about Telnyx:

Telnyx city glows
Voices whisper through the air
Connected we stand
```
