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

*Part 2 of 5 — see also: [Part 1](telnyx-inference--part-1.md), [Part 3](telnyx-inference--part-3.md), [Part 4](telnyx-inference--part-4.md), [Part 5](telnyx-inference--part-5.md)*

Telnyx Inference is a developer platform for building AI-powered applications, centered on an OpenAI-compatible chat completions API and a managed Voice AI Assistant product. It offers open-source LLMs hosted on Telnyx GPU infrastructure, embeddings and RAG, fine-tuning, audio language models, function calling, structured output, and integrations with enterprise platforms. The Voice AI Assistant product supports dynamic variables, memory, agent handoff, conversation workflows, multi-participant calls, scheduled events, observability via Langfuse, and AI Insights for conversation analysis.

## Embeddings and RAG

### Embeddings

Upload documents to [Telnyx Storage](https://telnyx.com/products/cloud-storage), then embed them via API or by clicking "Embed for AI Use" in the portal. Documents are processed into sections and each section is embedded based on its contents. Once embedded, you can chat over them in the [AI Playground](https://portal.telnyx.com/#/ai/playground) or via the chat completions API using a `retrieval` tool with `bucket_ids`.

### Clusters

After embedding documents, you can [compute clusters](https://developers.telnyx.com/api-reference/clusters/compute-new-clusters#compute-new-clusters) to identify common themes. The `min_cluster_size` and `min_subcluster_size` parameters control how clusters are identified. Top-level clusters identify broad themes; sub-clusters identify more specific topics within a broader theme. Inspect results as JSON via the `task_id` endpoint, or render a graph via the `/graph` endpoint.

### Conversation History

Conversation History stores and indexes conversation records so agents can search previous interactions. Enable `conversation_persistence` on a covered SIP connection resource (`ip_connections`, `credential_connections`, `fqdn_connections`) to store and index voice conversation history. Search via `GET /v2/ai/conversation_histories` with a query (`q`) and `record_type` (use `voice` for SIP call history). Narrow results with `region`, `min_score`, and `filter[field][operator]` parameters.

Pricing has three parts: embed and persist at `$0.0015 / 1K characters` (includes 30 days of retention), storage after 30 days at `$0.60 / GiB-month`, and vector search at `$0.003 / search` (first 10,000 searches per month are free). Default retention is 30 days.

## Fine-Tuning

Upload documents to Telnyx Storage, then fine-tune a language model on them via API or the [fine-tuning tab in the portal](https://portal.telnyx.com/#/ai/fine-tuning). Telnyx supports the standard `.jsonl` training file as input, and will also use AI to generate a training file from your raw documents automatically. Once fine-tuned, use the model in the AI Playground or via the chat completions API.

## Voice AI Assistants

### Quickstart

In the [AI Assistants tab](https://portal.telnyx.com/#/ai/assistants), create a new assistant from a blank template. Configure instructions and greeting (which can use `{{variable}}` placeholders), then configure voice settings (TTS and STT providers, background audio, speaking plan, noise suppression). Assign a phone number and test the assistant.

Telnyx provides system variables for use in instructions and greetings:

| Variable | Description | Example |
| --- | --- | --- |
| `{{telnyx_current_time}}` | Current date and time in UTC | `Monday, February 24 2025 04:04:15 PM UTC` |
| `{{telnyx_conversation_channel}}` | `phone_call`, `web_call`, or `sms_chat` | `phone_call` |
| `{{telnyx_agent_target}}` | Phone number, SIP URI, or identifier for the agent | `+13128675309` |
| `{{telnyx_end_user_target}}` | Phone number, SIP URI, or identifier for the end user | `+15551234567` |
| `{{telnyx_sip_header_user_to_user}}` | User to User SIP header for the call | `cmlkPTM0Nzg1O3A9dQ==;encoding=base64;purpose=call` |
| `{{telnyx_sip_header_diversion}}` | Diversion SIP header for the call | `<sip:bob@example.com>;reason=user-busy` |
| `{{call_control_id}}` | Call control ID for the call | `v3:u5OAKGEPT3Dx8SZSSDRWEMdNH2OripQhO` |
| `{{telnyx_shaken_stir_attestation}}` | SHAKEN/STIR attestation level for inbound calls | `a` |

Telnyx also supports timezone-aware date/time variants (e.g., `{{telnyx_current_time_America/New_York}}`), shorthands (`{{telnyx_current_date}}`, `{{telnyx_current_weekday}}`), and a custom `date` format filter using `strftime` codes.

### Voice Settings

- **TTS providers**: Telnyx, AWS, Azure, ElevenLabs, Inworld. Ultra and xAI Grok voices support Expressive Mode with inline SSML emotion tags and nonverbal cues like `[laughter]`.
- **STT providers**: Telnyx (whisper), Deepgram, Azure. See [Transcription Settings](transcription-settings.md) for model details.
- **Background Audio**: Play predefined or custom background audio during calls.
- **Speaking Plan**: Four pause types — wait seconds (baseline), on punctuation seconds, on no punctuation seconds, on number seconds.
- **Noise Suppression**: Krisp or DeepFilterNet engines. Enable via `telephony_settings.noise_suppression` in the API.

### Outbound Calls

```
curl --request POST \
  --url https://api.telnyx.com/v2/texml/ai_calls/<texml_app_id> \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
      "From": "+13128675309",
      "To": "+15551234567",
      "AIAssistantId": "assistant-6207ab25-b185-478f-b2ef-85159e226727"
  }'
```

### MMS Integration During Voice Calls

When a user sends an MMS message during an ongoing voice call, the agent can detect it, analyze attached images using vision-capable models, and provide real-time responses. Supported vision models: `Groq/llama-4-maverick-17b-128e-instruct` and `OpenAI/gpt-4o`.

### Multi-Participant Calls

Multi-participant Voice AI calls let an assistant bring another person into an active call, follow who is speaking, and continue using the same tools and instructions. Add an **Invite** tool so the assistant can invite another participant, and a **Skip Turn** tool so the assistant can stay silent while people talk to each other. Use **Keyterm Boost** on the Voice tab to improve transcription accuracy on participant names.

### Scheduled Events

Scheduled events let an AI Assistant kick off an outbound interaction at a fixed point in the future — either a phone call or an SMS message. For phone calls, configure automatic retries with `max_retries_client_errors` (0–10) and `retry_interval_secs` (60–86400). Retryable outcomes are `busy`, `no-answer`, `failed`, and `canceled`. Each phone-call event exposes a `call_attempts` array with one entry per terminal dispatch.

### Voicemail Detection on Transfer

When a Voice AI Assistant transfers a call, the destination may go to voicemail. Set `detection_mode` to `premium` for ML-based detection. When voicemail is detected, choose `stop_transfer` (cancel and return to caller) or `leave_message_and_stop_transfer` (deliver a TTS message, then cancel). The voicemail message can be custom text or the warm transfer audio instructions.

## Dynamic Variables

Dynamic variables let you configure a template for your agent's behavior. Use `{{variable_name}}` syntax in instructions, greeting, or tools. The lifecycle: **Define** placeholders → **Inject** values via API, webhooks, SIP headers, or defaults → **Resolve** at conversation start → **Use** throughout the conversation.

Resolution precedence (highest to lowest):

1. **Outbound API call** — pass via `AIAssistantDynamicVariables` parameter.
2. **Custom SIP Headers** — `X-` prefix headers map to dynamic variables (e.g., `X-Full-Name` → `{{full_name}}`). Telnyx reserves the `X-Telnyx` namespace.
3. **Dynamic Variables Webhook** — POST to `dynamic_variables_webhook_url` at conversation start. Response can include `dynamic_variables`, `memory`, and `conversation` fields. Default timeout is 1.5 seconds, up to 10 seconds via `dynamic_variables_webhook_timeout_ms`.
4. **Default values** in the Assistant builder.
5. **Unset** — variables remain as raw `{{variable_name}}`.
