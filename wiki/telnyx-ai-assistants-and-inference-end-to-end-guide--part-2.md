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

*Part 2 of 2 — see also: [Part 1](telnyx-ai-assistants-and-inference-end-to-end-guide--part-1.md)*

A practical, end-to-end overview of Telnyx AI Assistants and the Inference platform: build a production voice/chat assistant, add tools and multi-agent handoff, integrate enterprise systems, personalize context, observe and test, connect custom LLMs, run outbound missions, and use the OpenAI-compatible API with popular frameworks.

## Bring your own LLM (OpenAI-compatible endpoints)
Point an assistant to any publicly accessible OpenAI-compatible chat completions base_url (Azure OpenAI, Bedrock, Baseten, vLLM/SGLang, etc.). Store the API key as an Integration Secret. Optionally set external_llm.forward_metadata: true to forward dynamic variables as extra_metadata for routing/personalization at your gateway.

## Models, regions, and pricing
Hosted chat models include moonshotai/Kimi-K2.6 (recommended), zai-org/GLM-5.1-FP8, MiniMaxAI/MiniMax-M2.7. Embeddings: thenlper/gte-large. Regions: US East (Atlanta), US West (Denver), EU (Paris), APAC (Sydney); routing is automatic; EU processing stays in-region. Pricing is pay-per-token/character/second by product—see the Inference pricing page for current rates.

## OpenAI-compatible API and frameworks
Use Telnyx by swapping base_url=https://api.telnyx.com/v2/ai/openai and your API key in any OpenAI SDK.

- Function Calling: define tools, let the model pick (tool_choice auto/required/none), execute functions server-side, and send results back as tool messages.
- Streaming + parallel tools: parse streamed tool_calls by index and dispatch async tasks; return results incrementally and finalize with a second model response.
- Frameworks: LangChain (ChatOpenAI), LlamaIndex (OpenAILike), CrewAI (LLM base_url), LiveKit (LLM + native Telnyx STT/TTS plugins). Environment variables can globally route OpenAI clients through Telnyx.

## Embeddings, retrieval, and clusters
Embed documents in Telnyx Storage via API or Portal and ground chat completions with retrieval tools. Compute semantic clusters over embedded content to identify themes/subtopics; tune min_cluster_size and min_subcluster_size; fetch JSON cluster structures and graphs via API.

## AI Insights: analysis at scale
Create insights (text or structured JSON) with clear instructions and optional variables; organize them into Insight Groups with per-group webhooks; assign groups to assistants. Structured insights support string/enum/number/integer/boolean/arrays/objects with optional constraints; use enums for categorical accuracy. Industry templates cover Healthcare, Support, Sales, E‑commerce, and Financial Services with webhook handling examples.

## Missions: autonomous, multi-call voice outreach
With AI Missions and the Telnyx Missions skill (OpenClaw), describe a multi-step task (e.g., find caterers, call and negotiate), and the agent plans steps, creates a purpose-built voice assistant, assigns a number, schedules calls, monitors completion, extracts insights, and returns a structured recommendation. Review mission plans, runs, linked assistants, conversations, and audio in the Portal.

## Security, secrets, data residency
Store all third-party and Langfuse credentials as Integration Secrets (write-once). Use least-privilege service accounts, rotate keys, and test in sandbox environments. EU accounts process and keep inference traffic in-region; contact support to pin region routing.

## Troubleshooting and tuning
- Dynamic variables: ensure names match, respect precedence (API > SIP headers > webhook > defaults), and keep webhook under 1s; verify webhook signing and logs in Portal.
- Handoff loops: tighten domains, add boundaries, cap handoffs, and add a human fallback.
- Context loss: configure each assistant’s dynamic variables webhook/memory consistently; use shared memory keys and metadata.
- Integrations: validate credentials, scopes, and instance domains; reconnect if tools don’t appear; handle rate limits and timeouts; cache frequent reads.
- Observability: status enabled, correct secret refs, and Langfuse host; rotate keys in Integration Secrets.
- STT tuning: set appropriate end-of-turn thresholds; boost key terms; align Speaking Plan with your turn-taking needs.
- Load and canaries: use Tests and Traffic distribution to validate new versions before promotion.

## Handy API links
- Create/update Assistant: https://developers.telnyx.com/api-reference/assistants/create-an-assistant  
- Start Voice Assistant (call control): https://developers.telnyx.com/api-reference/call-commands/start-ai-assistant  
- Add Messages to active call: https://developers.telnyx.com/api-reference/call-commands/add-messages-to-ai-assistant  
- Transfer Call: https://developers.telnyx.com/api-reference/call-commands/transfer-call  
- Scheduled Events: /v2/ai/assistants/{assistant_id}/scheduled_events  
- OpenAI-compatible Chat Completions: https://api.telnyx.com/v2/ai/openai  
- Embeddings & Clusters APIs: see Embeddings and Clusters references in docs
