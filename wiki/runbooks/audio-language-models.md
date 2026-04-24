---
title: Audio Language Models
summary: In this tutorial, you'll learn how to.
sources:
  - url: https://developers.telnyx.com/docs/inference/audio-language-models/index
    content_hash: 8f0d8b52b9467f887aa2a3e91b07f83313d597a3d835d452b83ca47cc31b8b43
updated_at: 2026-04-10T00:00:00Z
---

# Audio Language Models

In this tutorial, you'll learn how to:

* Identify which Audio Language Models are available using our [models API](https://developers.telnyx.com/api-reference/chat/get-available-models#get-available-models)
* Chat with open source Audio Language Models using our [chat completions API](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion)

## Getting started

Audio Language Models are identified in our [models API](https://developers.telnyx.com/api-reference/chat/get-available-models#get-available-models) with a `task` type of `audio-text-to-text`.

Audio is made available to the model in two main ways:

* passing a link to the audio in a user message
* passing the base64 encoded audio directly in a user message

> **Note:** Make sure you have set the TELNYX\_API\_KEY environment variable

```python theme={null}
import base64
import os

from openai import OpenAI
import requests

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai"
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

This will output something like the following for this audio

<audio>
  <source type="audio/mpeg" />

  Your browser does not support the audio element.
</audio>

```
Transcribe link: That's one small step for man, one giant leap for mankind.
Transcribe base64: That's one small step for man, one giant leap for mankind.
Translate link: C'est un petit pas pour un homme, un grand pas pour l'humanité.
```


## Related Pages

- [Large Language Models (LLM)](../runbooks/large-language-models-llm.md)
- [Available Models](../runbooks/available-models.md)
