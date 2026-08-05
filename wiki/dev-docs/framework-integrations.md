---
title: Framework Integrations
summary: Telnyx's inference API is OpenAI-compatible, allowing you to swap the `base_url`
  and `api_key` in any framework that supports OpenAI. This page provides a quick
  reference for supported frameworks and the environment variables needed to route
  calls through Telnyx.
sources:
- url: https://developers.telnyx.com/docs/inference/integrations/index
updated_at: 2026-08-05T13:46:05Z
---

# Framework Integrations

Telnyx's inference API is OpenAI-compatible, allowing you to swap the `base_url` and `api_key` in any framework that supports OpenAI. This page provides a quick reference for supported frameworks and the environment variables needed to route calls through Telnyx.

## Quick Reference

Telnyx's inference API is OpenAI-compatible. You can swap `base_url` and `api_key` in any framework that supports OpenAI to route requests through Telnyx.

| Framework | Swap Method | Guide |
| --- | --- | --- |
| OpenAI SDK | `base_url` in client constructor | [OpenAI Migration](openai-migration.md) |
| LangChain | `base_url` in `ChatOpenAI` | [LangChain](langchain.md) |
| LlamaIndex | `api_base` in `OpenAILike` | [LlamaIndex](llamaindex.md) |
| CrewAI | `OPENAI_BASE_URL` env var or `base_url` in LLM | [CrewAI](crewai.md) |
| LiveKit | Telnyx as LLM provider | [LiveKit](livekit.md) |

## Environment Variables

Route all OpenAI SDK calls through Telnyx with no code changes by setting the following environment variables:

```
export OPENAI_API_KEY=your_telnyx_api_key
export OPENAI_BASE_URL=https://api.telnyx.com/v2/ai/openai
```
