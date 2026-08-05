---
title: Audio Language Models
summary: Learn how to use Telnyx's Audio Language Models to transcribe, translate,
  and otherwise reason over audio inputs via the OpenAI-compatible chat completions
  API.
sources:
- url: https://developers.telnyx.com/docs/inference/audio-language-models
updated_at: 2026-08-05T13:45:40Z
---

# Audio Language Models

Learn how to use Telnyx's Audio Language Models to transcribe, translate, and otherwise reason over audio inputs via the OpenAI-compatible chat completions API.

## Overview

Audio Language Models on Telnyx let you send audio to a chat model and receive a text response. They are surfaced through the OpenAI-compatible chat completions API and identified in the [Models API](models-api.md) with a `task` type of `audio-text-to-text`.

You can supply audio to the model in two ways:

- Pass a URL pointing to the audio file in a user message.
- Pass the audio as a base64-encoded data URI directly in a user message.

## Getting started

Before running the examples below, make sure the `TELNYX_API_KEY` environment variable is set. The client is configured to point at Telnyx's OpenAI-compatible base URL.

```python
import base64
import os

from openai import OpenAI
import requests

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai"
)

def encode_audio_base64_from_url(audio_url: str) -> str:
    """Encode audio retrieved from a remote url to base64 format."""
    with requests.get(audio_url) as response:
        response.raise_for_status()
        result = base64.b64encode(response.content).decode('utf-8')

    return f"data:audio/ogg;base64,{result}"

def process_audio(audio_url, instructions):
    chat_completion = client.chat.completions.create(
        model="fixie-ai/ultravox-v0_4_1-llama-3_1-8b",
        messages=[
            {
                "role": "system",
                "content": instructions
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "audio_url",
                        "audio_url": {
                            "url": audio_url,
                        },
                    },
                ],
            }
        ],
    )
    return chat_completion.choices[0].message.content

audio_url = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Phrase_de_Neil_Armstrong.oga"
audio_base64 = encode_audio_base64_from_url(audio_url)

instructions = "Transcribe this verbatim. Do NOT respond with anything but the transcription."
print(f"Transcribe link: {process_audio(audio_url, instructions)}")
print(f"Transcribe base64: {process_audio(audio_base64, instructions)}")

instructions = "Translate this to French. Be faithful to the original while sounding like a native French speaker. Do NOT respond with anything but the translation."
print(f"Translate link: {process_audio(audio_url, instructions)}")
```

## Example output

Running the script above against the sample audio URL produces output similar to the following:

```
Transcribe link: That's one small step for man, one giant leap for mankind.
Transcribe base64: That's one small step for man, one giant leap for mankind.
Translate link: C'est un petit pas pour un homme, un grand pas pour l'humanité.
```

The same `process_audio` helper works for both the URL and base64-encoded forms of the audio, demonstrating that the model accepts either input format interchangeably.

## Reference

- [Get available models (OpenAI-compatible)](https://developers.telnyx.com/api-reference/openai-chat/get-available-models-openai-compatible)
- [Create a chat completion (OpenAI-compatible)](https://developers.telnyx.com/api-reference/openai-chat/create-a-chat-completion-openai-compatible)
