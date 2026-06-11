---
title: Telnyx Inference
summary: Telnyx Inference provides OpenAI-compatible API access to open-source LLMs
  hosted on Telnyx GPU infrastructure across four global regions. Swap your base URL
  and API key to integrate with frameworks like LangChain, LlamaIndex, CrewAI, and
  LiveKit, or route all OpenAI SDK calls through Telnyx with zero code changes via
  environment variables.
sources:
- url: https://developers.telnyx.com/docs/inference/integrations/index
- url: https://developers.telnyx.com/docs/inference/langchain-integration
- url: https://developers.telnyx.com/docs/inference/livekit
- url: https://developers.telnyx.com/docs/inference/llama-index
- url: https://developers.telnyx.com/docs/inference/missions/index
- url: https://developers.telnyx.com/docs/inference/models/index
- url: https://developers.telnyx.com/docs/inference/models/pricing
- url: https://developers.telnyx.com/docs/inference/models/regions
- url: https://developers.telnyx.com/docs/inference/openai
- url: https://developers.telnyx.com/docs/inference/pr-reviewer
- url: https://developers.telnyx.com/docs/inference/streaming-functions
updated_at: 2026-06-11T10:32:07Z
---

# Telnyx Inference

*Part 3 of 3 — see also: [Part 1](telnyx-inference-2--part-1.md), [Part 2](telnyx-inference-2--part-2.md)*

Telnyx Inference provides OpenAI-compatible API access to open-source LLMs hosted on Telnyx GPU infrastructure across four global regions. Swap your base URL and API key to integrate with frameworks like LangChain, LlamaIndex, CrewAI, and LiveKit, or route all OpenAI SDK calls through Telnyx with zero code changes via environment variables.

## PR Reviewer GitHub Action

The PR Reviewer by Telnyx is a GitHub Action that uses open-source LLMs on Telnyx GPUs to automatically review pull requests.

### Setup

1. **Get a Telnyx API key** from the [Telnyx Portal](https://portal.telnyx.com/) under **API Keys**
2. **Add it as a GitHub secret** named `TELNYX_API_KEY` under **Settings → Secrets and variables → Actions**
3. **Create the workflow file** at `.github/workflows/review_pr.yml`:

```yaml
name: PR Review

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  pull-requests: write

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - name: PR Review
        uses: team-telnyx/reviewpr@main
        with:
          telnyx_api_key: ${{ secrets.TELNYX_API_KEY }}
          model_name: "zai-org/GLM-5.1-FP8"
```

The `model_name` parameter is optional; if omitted a default model is used. You can experiment with different models from the [Telnyx LLM Library](https://telnyx.com/products/llm-library).
