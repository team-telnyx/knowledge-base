---
title: 'Telnyx AI Assistants and Inference: End-to-End Guide'
summary: 'A practical, end-to-end overview of Telnyx AI Assistants and the Inference
  platform: build a production voice/chat assistant, add tools and multi-agent handoff,
  integrate enterprise systems, personalize context, observe and test, connect custom
  LLMs, run outbound missions, and use the OpenAI-compatible API with popular frameworks.'
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
  content_hash: e0189c3115b2b0ec8739b1ba3b782ea483de7a1205ddf866eaa083720296cb8c
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
  content_hash: 2c912fe20139394c5ab264f87da4acbca62e09fddc4a85f5e6875085d54ae351
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools
  content_hash: 736401f329fc4cb4c746ff8fd5d756c00fd3a780410ce9084deeeeb5f6531aef
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
  content_hash: 6431659cfc1080b05fae3580b16b26fe3b6f7b5202645fba44f5e79be2cd854a
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
  content_hash: 54ced37ff96d25d884594291a9b2182447838e85369a8d510fbb3b23c14c4680
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing
  content_hash: c2cd727b5e21acc75cb8258b170d8409ca6cc11ac83c54f1e0ae8ddbb4c428f3
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
  content_hash: 736fc0db52d3ea5b769039b8e36da4a23ea55115063876b3255c1a94a0f87eb1
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
  content_hash: d95fae886becd4d35ad12b53c88e99212098bdbb49dc9b7d58794d25ec44d2da
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
  content_hash: 12dbefea69b6d1bf42a1127a6196161d990988bef7f3d2d9f76dbe17b9f37965
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant
  content_hash: e32a9adc892a0661d42b14ffb4ac44c8d27673ed44659a0ed8b4b0cde6a43a8b
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
  content_hash: 092e6a9c0e06ea66330623a246ed29bafe161aee37d5fe70ac30e438f59b0843
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
  content_hash: 64ef9736186a641ad56c46a2b877e3213acdd746097cc5b16a68f96cd948f852
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
  content_hash: fdb8a55e2ef84acf968b46cb1f3050a2a2f38f85a26cf00e2962197f656855a1
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
  content_hash: ca821eba88d1eac534203355be68363e22a3aebbd50b291e3dc76c00a3911401
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
  content_hash: f6ca453d878e12ba5456d3869fdccb68f6c8dbfd59cc90f645354a9fd3c0f56f
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
  content_hash: 7c4a61c73ea31848ed9fee51d634e781b570a94428b81ac911ec4bb571d43c31
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights
  content_hash: 5260dc0125514c7dbbb702677aee3d0287c72cf0a231f853362a09fff78cd3ca
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
  content_hash: faf7aa81b48b0b3f75d083453eab8fc8436d97733f61a4eeda2a35d8740d12c6
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
  content_hash: 9535f3261b50eba991879efe40251ef848b5813f54534f7a4e706f0ce0a5a256
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
  content_hash: 871874b88b14fe31dd5288d8d9619d2375add7c402b89982a308b5884ae14093
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
  content_hash: 26922965bafbb017a97563d2e1a29e806843dd384885c83bf663e86ef11136ec
- url: https://developers.telnyx.com/docs/inference/clusters
  content_hash: 471060e1d49ca97d8f6dd9a7002bbb67f598414e0f2d86761391f06e9a2bd016
- url: https://developers.telnyx.com/docs/inference/crewai
  content_hash: 3980d01d8139402ec6fc134c79f77b9b4bff2e8c78ed45f39abcc42d7dd113f5
- url: https://developers.telnyx.com/docs/inference/embeddings
  content_hash: 11c301c179a2606d02057f7a5c729f41ae782658cee670388d0562d6692df00f
- url: https://developers.telnyx.com/docs/inference/functions
  content_hash: f2f26dfdcf6d9f718ce6c4e5a6f347220f571debfd1ae17ef25c98c47836b4b7
- url: https://developers.telnyx.com/docs/inference/getting-started
  content_hash: a21c4e17aeb2257d25bc4e6e1ec5627664bab2e833c83a3fc8ce032d0f0f97a4
- url: https://developers.telnyx.com/docs/inference/integrations
  content_hash: 3b76ed618badbf413a98f1a78927b5d130f979213a282c38a4953403e6aa77c0
- url: https://developers.telnyx.com/docs/inference/langchain-integration
  content_hash: e8cdee2785afc4eee971e183b64550fbd6c414ef7209e4c9e53ebe42489782fd
- url: https://developers.telnyx.com/docs/inference/livekit
  content_hash: 5a7a732b11936e0945d5da04a4d6ac4a12e3d43d1ddeb71bc688cc70dc7ef773
- url: https://developers.telnyx.com/docs/inference/llama-index
  content_hash: 0b2fad61302e4bac48854a7b2038f91ca4d7c723a2095ba97c33bc69dcd78fba
- url: https://developers.telnyx.com/docs/inference/missions
  content_hash: cea50fbf7ed2aad52a771f47215f9db9b136504a6f571bfc0a35392185a5f71f
- url: https://developers.telnyx.com/docs/inference/models
  content_hash: 59252d732247472e4fcb65a955bfafc224353375c31b68729db6585c0a587496
- url: https://developers.telnyx.com/docs/inference/models/pricing
  content_hash: 6976462e6ab0f4ab6ec0190ce18f8ebfe7349d8805774ce9739ff79d6d25b75b
- url: https://developers.telnyx.com/docs/inference/models/regions
  content_hash: 4c6842a9c5f833c827036cbcbfa466c2cca13a251bcb004d308c0f871a955c1f
- url: https://developers.telnyx.com/docs/inference/openai
  content_hash: 9d6323e3d8756993136635f4d77fecb6c60635b20cec15b146be4a98652c1514
- url: https://developers.telnyx.com/docs/inference/pr-reviewer
  content_hash: 433282bf7e0b10587abc6e36bba25993962ca924e052f47a2ca480f4b210bbb3
- url: https://developers.telnyx.com/docs/inference/streaming-functions
  content_hash: fedd5e44b377b6a4b72bbce8832a1724f0035c7eba4ef8795f8309c1e15f5cde
updated_at: 2026-05-08T13:12:48Z
---

# Telnyx AI Assistants and Inference: End-to-End Guide

*Part 1 of 2 — see also: [Part 2](telnyx-ai-assistants-and-inference-end-to-end-guide--part-2.md)*

A practical, end-to-end overview of Telnyx AI Assistants and the Inference platform: build a production voice/chat assistant, add tools and multi-agent handoff, integrate enterprise systems, personalize context, observe and test, connect custom LLMs, run outbound missions, and use the OpenAI-compatible API with popular frameworks.

## What you can build with Telnyx AI
Telnyx lets you run real-time voice and chat assistants that talk, call tools and APIs, hand off to specialists, and integrate with your systems. Assistants are model-agnostic (OpenAI, Anthropic, Llama-family, Qwen, and hosted open-source models like moonshotai/Kimi). You can:

- Stand up a production-grade Voice AI assistant in minutes
- Route across specialized agents with unified or distinct voices
- Run long operations asynchronously and inject results mid-call
- Personalize with dynamic variables and persistent memory
- Connect CRMs/ITSMs (Salesforce, Zendesk, ServiceNow, Jira, HubSpot, Intercom, GitHub, Greenhouse)
- Observe LLM calls and tools in Langfuse; manage prompts there too
- Version, A/B, and canary traffic by end-user target
- Import agents from Vapi, ElevenLabs, Retell
- Bring your own LLM via any OpenAI-compatible endpoint
- Use OpenAI-compatible chat completions, embeddings, function-calling, streaming, and frameworks

## Quickstart: create a production Voice Assistant
1) In the Portal, go to AI Assistants and create a new assistant. Use system variables like {{telnyx_current_time}}, {{telnyx_conversation_channel}}, {{telnyx_agent_target}}, {{telnyx_end_user_target}}, {{call_control_id}} in instructions/greeting.  
2) Configure Voice (TTS/STT), optional background audio, Speaking Plan, and noise suppression (krisp or DeepFilterNet).  
3) Test inbound; optionally assign a number or place outbound test calls via API.  
4) Review Conversation History, transcripts, tools, and latency metrics.  
5) Optional: enable MMS during a live voice call with a vision-capable model (e.g., openai/gpt-4o, Groq/llama-4-maverick-17b-128e-instruct).

Outbound call example:
```
curl --request POST \
  --url https://api.telnyx.com/v2/texml/ai_calls/<texml_app_id> \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
      "From": "+13128675309",
      "To": "+15551234567",
      "AIAssistantId": "assistant-..."
  }'
```

## Core building blocks
- Assistants: name, model, instructions, voice/telephony, tools, insights, observability.
- Tools: Hang Up, Handoff, Transfer, SIP Refer, Send DTMF, Webhook; plus Invite/Skip Turn for multi-participant. Reuse shared tools via the Tools Library.
- Dynamic Variables: personalize prompts via API, SIP headers (X- headers), webhook (1s timeout), or defaults. Avoid the reserved telnyx_ prefix.
- Memory: grant assistants controlled access to prior conversations via a conversation_query and optional insight filters.
- Knowledge Bases: upload files or URLs and enable retrieval.
- Insights: run structured/unstructured post-call analysis; organize as Insight Groups with optional webhooks.

## Agent handoff between specialists
Handoff enables a triage agent to transfer to targeted specialist assistants with full context.

Lifecycle: detect → select agent → transfer context → transition → continue.  
Modes:
- Unified (default): same voice, seamless to the user, shared context.
- Distinct: each assistant keeps its own voice; explicit “transferring you to…”.

Best practices:
- Split agents when domains, tools, or patterns differ; keep one agent for narrow domains.
- Define clear triggers (intent/keywords/capability/sentiment) and boundaries; cap handoffs and add human failsafe.
- Pass full history, user/account, intent, collected data, actions tried, sentiment; use dynamic variables and consistent memory keys.
- Avoid loops: responsibility matrices, handoff history, max handoffs.

API (tool config excerpt):
```
{
  "type": "handoff",
  "handoff": {
    "voice_mode": "unified" | "distinct",
    "ai_assistants": [ {"name": "Billing", "id": "asst_billing_..."}, ... ]
  }
}
```

Industry templates: Triage→Specialist (Healthcare), Browse→Purchase→Support (E‑commerce), Auth→Account→Fraud (Financial), Tier1→Tier2→Tier3 (Support).

## Multi-participant voice calls
Assistants can invite another person mid-call (Invite tool), track speakers, and continue normal tool use. Add a Skip Turn tool so the assistant stays silent while humans speak to each other, and resume only when addressed.

Tip: Use Keyterm Boost on the Voice tab (supported by deepgram/flux and deepgram/nova-3) for participant names—supports dynamic variables (e.g., Telnyx,{{participant_names}}).

## Workflows and shared Tools
- Workflow tab: visualize the conversation flow—assistant and tool nodes, connections, and controls. Add/edit tools directly.
- Tools Library: define reusable tools once and assign to any assistant; centralize updates.

## Async tools and deferred context
For long-running webhooks, set async: true so the conversation continues while your backend works. When done, inject results into the live call with the Add Messages API.

Assistant webhook tool (async):
```
{
  "type": "webhook",
  "webhook": {
    "name": "lookup_order_status",
    "url": "https://your-backend.com/order-lookup",
    "method": "POST",
    "async": true,
    "body_parameters": { "type": "object", "properties": {"order_id": {"type": "string"}}, "required": ["order_id"] }
  }
}
```

Your backend receives x-telnyx-call-control-id, then injects results:
```
POST /v2/calls/{call_control_id}/actions/ai_assistant_add_messages
{
  "messages": [
    {"role": "system", "content": "Order ORD-12345 status: SHIPPED ..."}
  ]
}
```
Use clear, actionable system messages and handle edge cases (ended calls, multiple results) gracefully.

## Telephony features: transfers and outbound scheduling
- Voicemail detection on transfer: enable premium detection and choose action: stop_transfer or leave_message_and_stop_transfer (custom TTS or warm transfer instructions). The assistant remains with the caller the whole time.
- Scheduled Events: queue future outbound phone calls or SMS; for phone calls, configure retries on busy/no-answer/failed/canceled with max_retries_client_errors and retry_interval_secs (60–86400). Inspect attempt history via call_attempts; cancel pending events.

## Voice and transcription settings
Supported STT engines include deepgram/flux (English, optimized for live turn-taking), deepgram/nova-3 (multilingual), deepgram/nova-2, azure/fast (region selectable), assemblyai/universal-streaming, and xai/grok-stt. Deepgram settings include end-of-turn thresholds/timeouts, eager EOT, smart_format, numerals, and keyterm boosting. Adjust Speaking Plan timings for low latency. Enable noise suppression (krisp/DeepFilterNet) via voice settings or telephony_settings.noise_suppression.

## Observability and prompt ops (Langfuse)
Enable observability on an assistant to stream traces of LLM generations and tool calls to Langfuse, grouped deterministically per conversation. Store Langfuse keys as Integration Secrets. Optionally link to a Langfuse-managed prompt by name + version/label, or auto-publish instructions on save (prompt_sync). Tracing is async and low overhead.

## Testing, versions, and live traffic routing
Create tests with success criteria, then iterate and save changes as new versions. Use Traffic distribution to route by end user target (caller/destination) with ordered rules and percentage splits for canary rollouts; a default rule handles unmatched calls. Reorder, save, rollback; validate by test calls.

## Import assistants from other providers
Import Vapi, ElevenLabs, and Retell assistants via Portal or API. Instructions, greeting, tools (hangup/transfer/webhook), dynamic variables, voices (Vapi/EL) and many settings come over. Supply any placeholder secrets in Integration Secrets. Knowledge bases aren’t auto-imported—upload or crawl in the builder.
