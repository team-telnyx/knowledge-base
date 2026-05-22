---
title: 'Telnyx Integrations: Inference Frameworks and AI Assistant Platforms'
summary: Connect apps and workflows to Telnyx using OpenAI‑compatible SDKs (OpenAI,
  LangChain, LlamaIndex, CrewAI, LiveKit) and power AI assistants with enterprise
  integrations (Salesforce, Jira, Zendesk, and more). This guide covers environment
  routing, setup snippets, platform credentials, best practices, and troubleshooting.
sources:
- url: https://developers.telnyx.com/docs/inference/integrations/index
  content_hash: 4b60a5df66da0d5c77a1b9c245f8bf4785dfd729398acdac5e9eb06a6b2edff4
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
  content_hash: 736fc0db52d3ea5b769039b8e36da4a23ea55115063876b3255c1a94a0f87eb1
- url: https://developers.telnyx.com/docs/inference/langchain-integration
  content_hash: 2906e85c049c755f63f95efd8643fe75e55db1ef223d350952876823a0ef3f0a
- url: https://developers.telnyx.com/docs/inference/llama-index
  content_hash: 19becb528e62578a86c503e4791f919d3a803fbcca9dcd7e3fac40c40c4ec6c3
- url: https://developers.telnyx.com/docs/inference/openai
  content_hash: a64064b571f08a4dfc1aff6f37de63d1bc990e93c343836e6b3efdc9cada5690
- url: https://developers.telnyx.com/docs/inference/crewai
  content_hash: 9a8257cd80b4d1cfaae7972b7861a359a1af39880852f3a2a9db7342544e1442
- url: https://developers.telnyx.com/docs/inference/livekit
  content_hash: 5328c2500eaddcdd72e1e331e6f204077b88070e01e2001346a8d95be81ba43b
- url: https://developers.telnyx.com/docs/inference/streaming-functions
  content_hash: c3feeb248c728bbced5a3c4cee0ef581fd884d8a0b5c8aa45b1ffd65809fa3ca
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
  content_hash: 4ba75c47eee628f1855808bab33a188fdf86a1689a3ed3862ff37e245162ae8f
- url: https://developers.telnyx.com/docs/inference/pr-reviewer
  content_hash: b79e83243a6486f1635526f7e27456777c2a1a7c8a01eb5baea2a857178a81fc
updated_at: 2026-05-20T08:37:09Z
---

# Telnyx Integrations: Inference Frameworks and AI Assistant Platforms

*Part 2 of 2 — see also: [Part 1](telnyx-integrations-inference-frameworks-and-ai-assistant-platforms--part-1.md)*

Connect apps and workflows to Telnyx using OpenAI‑compatible SDKs (OpenAI, LangChain, LlamaIndex, CrewAI, LiveKit) and power AI assistants with enterprise integrations (Salesforce, Jira, Zendesk, and more). This guide covers environment routing, setup snippets, platform credentials, best practices, and troubleshooting.

## Coval testing and monitoring

Coval connects for assistant testing and QA (no end‑user tools are added).

### Prerequisites
- Coval account and a configured Telnyx assistant.

### Required credentials
- Coval API key from your Coval workspace.

### Capabilities
- Automated scenario simulation, CI/CD regression testing, production monitoring with alerts and replays, built‑in metrics (latency, accuracy, tool‑call effectiveness, instruction adherence).

## Managing connected integrations

- View: Open the assistant → Integrations → Connected Integrations to see what’s active.
- Disconnect: Click the unassign icon on a connected card; tools are disabled for that assistant and the integration moves to Available Integrations (can be reconnected). This only detaches from the current assistant; the integration remains in your account.
- Delete: From Available Integrations, click the trash icon to permanently remove the integration and stored credentials from your account.

## Security and configuration best practices

- Use dedicated service accounts with least‑privilege scopes.
- Rotate credentials regularly and monitor platform audit logs.
- Start with read‑only tools; add write actions gradually.
- Document when/how tools should be used and set sensible defaults (e.g., default project, priority).
- Handle errors gracefully with clear fallbacks.

## Performance considerations

- Minimize redundant API calls; cache frequently accessed values (e.g., via dynamic variables) per session.
- Set timeouts that balance responsiveness and reliability.
- Track rate limits and distribute load across service accounts if needed.

## Troubleshooting common issues

- Connection failures: Verify credentials, API access, token freshness; include Salesforce security token; ensure instance URLs exclude https:// and trailing slashes.
- Tools not appearing: Refresh, validate account permissions/subscription, disconnect/reconnect.
- Auth errors during calls: Regenerate tokens, update stored credentials, check account status/IP allowlists.
- Missing data: Confirm record existence and sharing/permissions; adjust search filters.
- Rate limiting: Reduce call frequency, cache data, request higher limits, or fan out across accounts.

## Advanced streaming tools and parallel function calls

Telnyx supports streaming tool calls and parallel execution with the OpenAI‑compatible chat completions API. You can:
- Provide multiple tools in tools=[...]
- Stream tool call deltas, detect functions early by index, and spawn tasks as soon as arguments parse
- Execute tasks concurrently and send tool results back for the final response
- Telnyx guarantees valid JSON for tool calls

See [Function Calling (Streaming + Parallel Calls)](function-calling-streaming-parallel-calls.md) for complete code.

## Example projects and tutorials

- AI SMS Outfit Recommender: Fetch weather from OpenMeteo, generate advice with Telnyx (e.g., Kimi‑K2.6), and send via Telnyx SMS. See [AI SMS Outfit Recs with OpenMeteo](ai-sms-outfit-recs-with-openmeteo.md).
- PR Reviewer GitHub Action: Review pull requests automatically using Telnyx‑hosted models; add TELNYX_API_KEY as a repo secret and configure model_name. See [PR Reviewer](pr-reviewer.md).

## Next steps and related resources

- Explore models, regions, and pricing: [Models](models.md), [Regions & Availability](regions-availability.md), [Pricing](pricing.md)
- Start building: [Inference API Quickstart](inference-api-quickstart.md), [OpenAI API Migration Guide](openai-api-migration-guide.md), [LangChain Integration](langchain-integration.md), [LlamaIndex Integration](llamaindex-integration.md), [CrewAI Integration](crewai-integration.md), [Telnyx LiveKit Plugin](telnyx-livekit-plugin.md)
- Retrieval: [Embeddings](embeddings.md)
- Securely store keys: Use Integration Secrets in the Telnyx Portal
- Full docs index: https://developers.telnyx.com/llms.txt
