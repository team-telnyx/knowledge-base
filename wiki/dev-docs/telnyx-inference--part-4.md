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

*Part 4 of 5 — see also: [Part 1](telnyx-inference--part-1.md), [Part 2](telnyx-inference--part-2.md), [Part 3](telnyx-inference--part-3.md), [Part 5](telnyx-inference--part-5.md)*

Telnyx Inference is a developer platform for building AI-powered applications, centered on an OpenAI-compatible chat completions API and a managed Voice AI Assistant product. It offers open-source LLMs hosted on Telnyx GPU infrastructure, embeddings and RAG, fine-tuning, audio language models, function calling, structured output, and integrations with enterprise platforms. The Voice AI Assistant product supports dynamic variables, memory, agent handoff, conversation workflows, multi-participant calls, scheduled events, observability via Langfuse, and AI Insights for conversation analysis.

## Observability

Connect your AI assistant to [Langfuse](https://langfuse.com) for LLM observability. Every interaction is automatically traced and sent to your Langfuse project, including LLM generations (input messages, output response, model, token usage) and tool calls (tool name, input arguments, output result). Traces are grouped by conversation using a deterministic trace ID derived from `conversation_id`.

Store Langfuse credentials as Telnyx integration secrets, then enable via `observability_settings` with `status: "enabled"`, `secret_key_ref`, `public_key_ref`, and `host`. Optionally link to a Langfuse-managed prompt via `prompt_name` with `prompt_version` or `prompt_label` (mutually exclusive), and auto-publish instructions back to Langfuse with `prompt_sync: "enabled"`.

## AI Insights

### Creating Insights

Insights return free-form text responses based on your instructions. Create them in the [AI Insights](https://portal.telnyx.com/#/ai/insights) page. Use system variables like `{{telnyx_current_time}}`, `{{telnyx_conversation_channel}}`, `{{telnyx_agent_target}}`, and `{{telnyx_end_user_target}}` in instructions. Configure webhook delivery via Insight Groups or per-assistant override.

### Structured Insights

Structured insights extract data in a predefined JSON schema format. Enable **Collect as structured data** and define parameters with a name, type, required flag, and description. Supported types: `string`, `enum`, `number`, `integer`, `boolean`, `array`, `array (string)`, `array (number)`, `array (boolean)`, and `object`. Advanced mode adds custom validation rules, enum constraints, min/max constraints, pattern matching, and nested object definitions.

### Insight Groups

Insight Groups are named collections of insights with optional webhook configuration. Assign the same group to multiple assistants. Configure via `insight_settings.insight_group_id` in the API. Results are delivered via webhook with the `conversation.insights.completed` event type.

### Telnyx-Managed Insights

Built-in insights maintained by Telnyx with consistent scoring rubrics:

- **Agent Instruction Following**: Excellent, Good, Fair, Poor, N/A — measures how well the assistant followed its system prompt and tool-use instructions.
- **User Satisfaction**: Excellent, Good, Fair, Poor, N/A — estimates caller satisfaction based on responses, tone, and engagement signals.

View results per-conversation or as a 7-day stacked-bar trend chart. Toggle **Compare by assistant version** to split data into separate charts per version.

## Transcription Settings

Telnyx AI Assistants support multiple STT models:

| Model | Engine | Best For |
| --- | --- | --- |
| `deepgram/flux` | Deepgram | Conversational AI, optimized for turn-taking with multilingual support |
| `deepgram/nova-3` | Deepgram | Fast multilingual transcription |
| `deepgram/nova-2` | Deepgram | Fast multilingual transcription on previous-generation model |
| `azure/fast` | Azure | Fast multilingual transcription with optional region and API key |
| `assemblyai/universal-streaming` | AssemblyAI | Conversational, multilingual streaming with configurable turn detection |
| `xai/grok-stt` | xAI | Multilingual transcription using Grok STT |
| `nvidia/parakeet-v3` | Parakeet | Multilingual transcription with automatic language detection |

`deepgram/flux` supports end-of-turn detection with `eot_threshold` (0.5–0.9, default 0.8), `eot_timeout_ms` (500–10000, default 5000), and `eager_eot_threshold` (0.3–0.9, default 0.4). `eager_eot_threshold` must be less than or equal to `eot_threshold`. Both `deepgram/flux` and `deepgram/nova-3` support `keyterm` boosting, including dynamic variables.

## Testing and Traffic Distribution

Create tests in the [AI Tests page](https://portal.telnyx.com/#/ai/tests) to validate assistant behavior before deployment. Create assistant versions with **Save as New Version** to enable A/B testing.

Traffic routing uses ordered rules evaluated top to bottom. Each rule has **If** conditions (matching the end user target) and **Serve** behavior (send to one version or split by percentage). Target rules can match on end user target with operators `is one of`, `is not one of`, or `starts with`. For gradual rollouts, use **Split by percentage** with version slots. The default rule handles unmatched calls. Drag rules to reorder, click **Rollback** to clear all routing rules.

For automated evaluation at scale, integrate with [Coval](https://www.coval.dev/) for scenario simulation, CI/CD evaluations, production monitoring, and built-in metrics.

## Data Residency and Compliance

Telnyx AI spans two products with different processing location behavior:

- **Inference API**: Processing in transit is latency-based, influenced by the ingress domain (`api.telnyx.com` → US, `api.telnyx.eu` → EU, `api.telnyx.com.au` → APAC). Not guaranteed. Chat completions are not stored; the responses endpoint stores conversations governed by your data locality setting.
- **Voice AI Assistants**: Processing location is influenced by the anchorsite on the assistant's TeXML application. Storage at rest is governed by your data locality flag, plus the data-retention setting for conversation content.

Neither the data locality flag nor the anchorsite is a hard guarantee of where live processing happens. During failover or capacity events, requests are processed at the next-lowest-latency region rather than failing.

### STT, TTS, and LLM Providers

Some providers are self-hosted by Telnyx (run on Telnyx-operated infrastructure); others are third-party services. Self-hosted STT models include `deepgram/flux`, `deepgram/nova-3`, `deepgram/nova-2`, `assemblyai/universal-streaming`, `speechmatics/standard`, and `distil-whisper/distil-large-v2`. Third-party STT includes `azure/fast`, `soniox/stt-rt-v4`, and `xai/grok-stt`. Self-hosted TTS includes Telnyx in-house voices, Rime, and Resemble. Third-party TTS includes ElevenLabs, AWS, Azure, Minimax, Inworld, and xAI. Self-hosted LLMs include Qwen and Moonshot (Kimi) model families. Third-party LLMs include Anthropic (Claude), OpenAI (GPT), and Google (Gemini).

### Data Retention

Voice AI Assistants expose a `privacy_settings.data_retention` setting (enabled by default). When disabled, conversation content is not retained: messages/transcripts, insights, observability logs, LLM request/response content logging, and TTS cache are all stopped. Latency/timing metrics, billing, security, and fraud-prevention records are still retained.

Call recordings are enabled by default and stored as Media Storage subject to your data locality setting.

## AI Missions

AI Missions let your agent execute multi-step workflows like "Find catering companies in Chicago and call them to negotiate quotes." The Telnyx Missions skill integrates with OpenClaw agents and uses the Missions API, Assistants API, and Numbers API to orchestrate research, phone calls, follow-ups, and final summaries. Monitor progress in the [Telnyx Portal](https://portal.telnyx.com) under AI Missions, with full audit trails, conversation playback, and structured result payloads.

## Pricing

Pay-per-token with no minimums or commitments. For current per-model pricing, see [telnyx.com/pricing/inference-api](https://telnyx.com/pricing/inference-api).

| Category | Basis | Notes |
| --- | --- | --- |
| Text generation | Per 1M tokens (input + output) | Input and output priced separately; cached input tokens at a discount |
| Audio transcription | Per second of audio | Varies by model |
| Text-to-speech | Per 1M characters | Varies by voice/model |
| Embeddings | Per 1M tokens | Single rate |
