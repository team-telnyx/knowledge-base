---
title: Telnyx Inference
summary: Telnyx Inference provides OpenAI-compatible API access to open-source LLMs
  hosted on Telnyx GPU infrastructure across four global regions. Swap your base URL
  and API key to integrate with frameworks like LangChain, LlamaIndex, CrewAI, and
  LiveKit, or route all OpenAI SDK calls through Telnyx with zero code changes via
  environment variables.
sources:
- url: https://developers.telnyx.com/docs/inference/integrations/index
  content_hash: c917ca415534ceced4543645dc0ee6a5e62aefde9764fe870bb3201efdda4557
- url: https://developers.telnyx.com/docs/inference/langchain-integration
  content_hash: 4bd1dbec9065b530d85fbe2c489b5cd808a6b40b81d5c701953855be74c83e14
- url: https://developers.telnyx.com/docs/inference/livekit
  content_hash: 1f0ffde23788f831e1cb82fe236a0a961bfcb81d24a7c18c3c77a80db28fd888
- url: https://developers.telnyx.com/docs/inference/llama-index
  content_hash: 0baed96eb2cfcbeda95bf1035cd59bf22c36a8fbc123a55208e95ec2ccc38cb3
- url: https://developers.telnyx.com/docs/inference/missions/index
  content_hash: 5a0a8ecfe1e2bc89d7401e6fc5a1fa9314f410011748e0c31e1c385d84301a0d
- url: https://developers.telnyx.com/docs/inference/models/index
  content_hash: 0c0e28e4c8992811c63c195fdee840417580b576a80525c5abf55debb2059fab
- url: https://developers.telnyx.com/docs/inference/models/pricing
  content_hash: d89500d3b013a59f00ee7771443639e5e1b065e81fcbd940f22ac18c4b972bf0
- url: https://developers.telnyx.com/docs/inference/models/regions
  content_hash: 229946cf9f354592c53a9aae56ff9f9550e07bcbd93adf09781cd8803934cd3a
- url: https://developers.telnyx.com/docs/inference/openai
  content_hash: 4d4c6e277b6f7aaded30c491784c883491fe8cb0de7fe2656b5b6fd6afcae210
- url: https://developers.telnyx.com/docs/inference/pr-reviewer
  content_hash: 3630170587e0109e1756789451f296c0805234dc629fec14f6dd05c0ba66ab01
- url: https://developers.telnyx.com/docs/inference/streaming-functions
  content_hash: 00f147864dd739761a9aa134e33a411d72322eecdf5fc1ef36b6f309c885fe61
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
