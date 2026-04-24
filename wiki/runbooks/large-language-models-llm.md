---
title: Large Language Models (LLM)
summary: LLM inference available through Telnyx for LiveKit voice agents.
sources:
  - url: https://developers.telnyx.com/docs/livekit/models/llm
    content_hash: 5439ea66c6821c22c51d426aee6b74b76b22c166b85ce43aa9f329e7a70fbc1f
updated_at: 2026-04-10T00:00:00Z
---

# Large Language Models (LLM)

LLM inference available through Telnyx for LiveKit voice agents.

Telnyx hosts models with an OpenAI-compatible API. No concurrency limits. Use the standard OpenAI plugin with the `.with_telnyx()` helper:

```python theme={null}
from livekit.plugins import openai

llm = openai.LLM.with_telnyx(model="moonshotai/Kimi-K2.5")
```

## About `.with_telnyx()`

This is a built-in static method on `openai.LLM` in the official [`livekit-plugins-openai`](https://pypi.org/project/livekit-plugins-openai/) package, maintained by LiveKit — not a Telnyx package or fork. It works the same way as the other OpenAI-compatible helpers in that package (`.with_azure()`, `.with_fireworks()`, etc.): it sets `base_url` to Telnyx's inference endpoint (`https://api.telnyx.com/v2/ai`) and reads your `TELNYX_API_KEY` from the environment. You don't need any additional packages beyond `livekit-plugins-openai`.

## Hosted models

These run on Telnyx infrastructure — no external API key needed, just your `TELNYX_API_KEY`:

| Model                    | Description          |
| ------------------------ | -------------------- |
| `moonshotai/Kimi-K2.5`   | Moonshot AI's latest |
| `zai-org/GLM-5`          | Zhipu AI's latest    |
| `MiniMaxAI/MiniMax-M2.5` | MiniMax's latest     |

## Proprietary models (BYOK)

For models like GPT-4o or Claude, Telnyx proxies the request using your own API key. Add your provider key in the [Telnyx Portal](https://portal.telnyx.com) under Inference settings.

```python theme={null}


## Related Pages

- [Audio Language Models](../runbooks/audio-language-models.md)
