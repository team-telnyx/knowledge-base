---
title: Telnyx Inference
summary: Telnyx Inference is a developer platform for building AI-powered applications,
  centered on an OpenAI-compatible chat completions API and a managed Voice AI Assistant
  product. It offers open-source LLMs hosted on Telnyx GPU infrastructure, embeddings
  and RAG, fine-tuning, audio language models, function calling, structured output,
  and integrations with enterprise platforms. The Voice AI Assistant product supports
  dynamic variables, memory, agent handoff, conversation workflows, multi-participant
  calls, scheduled events, observability via Langfuse, and AI Insights for conversation
  analysis.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/client-side-tools
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/telnyx-managed-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
- url: https://developers.telnyx.com/docs/inference/anthropic
- url: https://developers.telnyx.com/docs/inference/audio-language-models
- url: https://developers.telnyx.com/docs/inference/clusters
- url: https://developers.telnyx.com/docs/inference/crewai
- url: https://developers.telnyx.com/docs/inference/data-residency/index
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/feature-coverage
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/index
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/pricing
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/retention
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/searching
- url: https://developers.telnyx.com/docs/inference/embedding-rag/index
- url: https://developers.telnyx.com/docs/inference/embeddings/index
- url: https://developers.telnyx.com/docs/inference/fine-tuning
- url: https://developers.telnyx.com/docs/inference/functions
- url: https://developers.telnyx.com/docs/inference/getting-started/index
- url: https://developers.telnyx.com/docs/inference/integrations/index
- url: https://developers.telnyx.com/docs/inference/json-mode
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
updated_at: 2026-07-17T09:14:08Z
---

# Telnyx Inference

*Part 5 of 5 — see also: [Part 1](telnyx-inference--part-1.md), [Part 2](telnyx-inference--part-2.md), [Part 3](telnyx-inference--part-3.md), [Part 4](telnyx-inference--part-4.md)*

Telnyx Inference is a developer platform for building AI-powered applications, centered on an OpenAI-compatible chat completions API and a managed Voice AI Assistant product. It offers open-source LLMs hosted on Telnyx GPU infrastructure, embeddings and RAG, fine-tuning, audio language models, function calling, structured output, and integrations with enterprise platforms. The Voice AI Assistant product supports dynamic variables, memory, agent handoff, conversation workflows, multi-participant calls, scheduled events, observability via Langfuse, and AI Insights for conversation analysis.

## Regions and Availability

GPU infrastructure across four regions on three continents:

| Region | Location |
| --- | --- |
| US East | Atlanta |
| US West | Denver |
| EU | Paris |
| Asia-Pacific | Sydney |

Processing is latency-based, influenced by the ingress domain. Telnyx will endeavor to process in the preferred region but does not guarantee it. A region-selection API parameter is on the roadmap.

## Example: AI SMS Outfit Recommendations

A complete example combining OpenMeteo weather API, Telnyx Inference, and Telnyx SMS to send daily outfit recommendations based on weather. Uses `zai-org/GLM-5.2` for generating recommendations and the Telnyx Python SDK for sending SMS.

## Example: PR Reviewer

The Telnyx PR Reviewer is a GitHub Action that uses open-source language models on Telnyx GPUs to automatically review pull requests. Set up by adding `TELNYX_API_KEY` as a GitHub secret and creating a workflow file at `.github/workflows/review_pr.yml` using `team-telnyx/reviewpr@main`.
