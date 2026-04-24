---
title: Examples
summary: REST TTS code examples — OpenAI SDK compatibility, streaming playback, async retrieval.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/rest-api/examples
    content_hash: 21e8ef8e1c61b7d7a1841bd385a4671a06750beb154e870a427dfaf363beeda3
updated_at: 2026-04-10T00:00:00Z
---

# Examples

REST TTS code examples — OpenAI SDK compatibility, streaming playback, async retrieval.

## OpenAI SDK Compatibility

The REST endpoint is a drop-in replacement for the OpenAI Audio API:

```python theme={null}
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_TELNYX_API_KEY",
    base_url="https://api.telnyx.com/v2"
)

response = client.audio.speech.create(
    model="tts-1-hd",
    voice="astra",
    input="Hello from Telnyx."
)

response.stream_to_file("output.mp3")
```


## Related Pages

- [Examples](../runbooks/examples.md)
- [Examples](../runbooks/examples-2.md)
- [Examples](../runbooks/examples-4.md)
