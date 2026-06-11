---
title: 'Telnyx Integrations: Inference Frameworks and AI Assistant Platforms'
summary: Connect apps and workflows to Telnyx using OpenAI‑compatible SDKs (OpenAI,
  LangChain, LlamaIndex, CrewAI, LiveKit) and power AI assistants with enterprise
  integrations (Salesforce, Jira, Zendesk, and more). This guide covers environment
  routing, setup snippets, platform credentials, best practices, and troubleshooting.
sources:
- url: https://developers.telnyx.com/docs/inference/integrations/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/langchain-integration
- url: https://developers.telnyx.com/docs/inference/llama-index
- url: https://developers.telnyx.com/docs/inference/openai
- url: https://developers.telnyx.com/docs/inference/crewai
- url: https://developers.telnyx.com/docs/inference/livekit
- url: https://developers.telnyx.com/docs/inference/streaming-functions
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
- url: https://developers.telnyx.com/docs/inference/pr-reviewer
updated_at: 2026-05-20T08:37:09Z
---

# Telnyx Integrations: Inference Frameworks and AI Assistant Platforms

*Part 1 of 2 — see also: [Part 2](telnyx-integrations-inference-frameworks-and-ai-assistant-platforms--part-2.md)*

Connect apps and workflows to Telnyx using OpenAI‑compatible SDKs (OpenAI, LangChain, LlamaIndex, CrewAI, LiveKit) and power AI assistants with enterprise integrations (Salesforce, Jira, Zendesk, and more). This guide covers environment routing, setup snippets, platform credentials, best practices, and troubleshooting.

## Integration categories

- Framework integrations: Use Telnyx as an OpenAI‑compatible LLM backend in OpenAI SDKs, LangChain, LlamaIndex, CrewAI, and LiveKit.
- AI assistant platform integrations: Let Telnyx Voice/Chat assistants create tickets, update records, and fetch context from tools like Salesforce, ServiceNow, Jira, HubSpot, Zendesk, Intercom, GitHub, and Greenhouse. Coval adds testing/monitoring for agents.

## OpenAI compatibility and environment routing

Telnyx offers an OpenAI‑compatible API. Most frameworks work by swapping the base URL and API key.

- Global routing (no code changes in OpenAI SDKs):
  - export OPENAI_API_KEY=your_telnyx_api_key
  - export OPENAI_BASE_URL=https://api.telnyx.com/v2/ai/openai
- Explicit configuration (Python OpenAI SDK):
  - Base URL: https://api.telnyx.com/v2/ai/openai
  - Model example: moonshotai/Kimi-K2.6

See [OpenAI API Migration Guide](openai-api-migration-guide.md) for compatibility details (chat parameters, extra Telnyx features like retrieval and guided_json, and transcription notes).

## Framework quick-starts

- OpenAI SDK: Swap OPENAI_BASE_URL and OPENAI_API_KEY, or pass base_url and api_key to the client. See [OpenAI API Migration Guide](openai-api-migration-guide.md).
- LangChain: Use ChatOpenAI with base_url set to Telnyx. See [LangChain Integration](langchain-integration.md).
- LlamaIndex: Use OpenAILike with api_base set to Telnyx. See [LlamaIndex Integration](llamaindex-integration.md).
- CrewAI: Set OPENAI_BASE_URL (and your Telnyx API key) or pass base_url/api_key in LLM(). See [CrewAI Integration](crewai-integration.md).
- LiveKit: Use Telnyx for LLM inference via the OpenAI plugin and native Telnyx STT/TTS with livekit-plugins-telnyx. See [Telnyx LiveKit Plugin](telnyx-livekit-plugin.md).

## LangChain setup and function calling

- Install: pip install langchain-openai
- Minimal usage:
  - from langchain_openai import ChatOpenAI
  - ChatOpenAI(base_url="https://api.telnyx.com/v2/ai/openai", api_key=os.getenv("TELNYX_API_KEY"), model="moonshotai/Kimi-K2.6")
- Tools/function calling: bind_tools([...]) to enable structured tool calls with Telnyx’s OpenAI‑compatible tools API. See [LangChain Integration](langchain-integration.md).

## LlamaIndex setup and streaming chat

- Install: pip install llama-index-core llama-index-llms-openai-like
- Minimal usage:
  - OpenAILike(api_base="https://api.telnyx.com/v2/ai/openai", api_key=os.getenv("TELNYX_API_KEY"), model="moonshotai/Kimi-K2.6", is_chat_model=True)
  - Use stream_chat([...]) for token streaming.
- For RAG, combine with [Embeddings](embeddings.md). See [LlamaIndex Integration](llamaindex-integration.md).

## CrewAI agents and tools

- Global routing (recommended):
  - export TELNYX_API_KEY=your_telnyx_api_key
  - export OPENAI_BASE_URL=https://api.telnyx.com/v2/ai/openai
- Per‑agent config: LLM(model="moonshotai/Kimi-K2.6", base_url="https://api.telnyx.com/v2/ai/openai", api_key=os.getenv("TELNYX_API_KEY"))
- Add @tool functions to agents for tool calling. See [CrewAI Integration](crewai-integration.md).

## LiveKit voice agents with Telnyx STT/TTS

- Install: pip install livekit-plugins-telnyx
- Use OpenAI plugin with Telnyx LLM: openai.LLM.with_telnyx(model="moonshotai/Kimi-K2.6")
- Telnyx STT/TTS: stt=telnyx.STT(), tts=telnyx.TTS(voice="Telnyx.NaturalHD.astra")
- Env vars: TELNYX_API_KEY plus LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET
- Test quickly with the LiveKit Agents Playground.
- See available voices in [TTS available voices](tts-available-voices.md). More in [Telnyx LiveKit Plugin](telnyx-livekit-plugin.md).

## AI assistant enterprise integrations

To connect a platform to an AI assistant:

1) Open your assistant in the Mission Control Portal (AI Assistants) or create one.
2) Go to the Integrations tab.
3) Add Integration, choose a provider, and enter required credentials.
4) Enable tools, set sensible defaults, and save the assistant.

Common uses: lead/case management (Salesforce, HubSpot, Zendesk), incident/ticket workflows (ServiceNow, Jira), customer context (Intercom), dev workflows (GitHub), recruiting (Greenhouse). Coval adds simulation, regression testing, and production monitoring for assistants.

## GitHub integration details

### Prerequisites
- GitHub account with repo access and permission to create Personal Access Tokens.

### Required credentials
- Personal Access Token (classic) with scopes such as repo, read:user, read:org.

### Available tools
- Create issues, manage PRs, search repos, access code/files, manage labels.

### Example use
- “Create an issue for a Safari login bug and tag priority:high.”

## Greenhouse integration details

### Prerequisites
- Greenhouse account with Harvest API access and permissions.

### Required credentials
- Harvest API key from Dev Center → API Credential Management.

### Available tools
- Candidate lookup, interview scheduling, application management, job posting access, scorecard review.

### Example use
- “What’s the status of the candidate who interviewed yesterday?” → Assistant returns stage and details.

## HubSpot integration details

### Prerequisites
- HubSpot account with API access.

### Required credentials
- Private app access token (Settings → Integrations → Private Apps → Auth tab).

### Available tools
- Manage contacts, deals, tickets, company records, and log engagements.

### Example use
- Capture a lead, create a deal, and schedule a demo from a single conversation.

## Intercom integration details

### Prerequisites
- Intercom account, permission to create private apps.

### Required credentials
- Access token from Developer Hub app authentication.

### Available tools
- Access conversation history, create notes, update attributes, search users, manage tags.

### Example use
- Fetch a customer by email, review history, update company name, and note the change.

## Jira integration details

### Prerequisites
- Jira Cloud/Server account, project access.

### Required credentials
- Account email, API token (id.atlassian.com), and site URL (e.g., yourcompany.atlassian.net without https://).

### Available tools
- Create/update/search issues, add comments, and transition workflow states.

### Example use
- “Create a bug in PROJ with High priority and assign on‑call.”

## Salesforce integration details

### Prerequisites
- Salesforce account with API access, username/password, security token, organization ID.

### Required credentials
- Instance domain (acme.my.salesforce.com or sandbox variant), username, password, security token, org ID.

### Available tools
- Search/create/update records (cases, leads, opportunities, tasks) and run SOQL queries.

### Example use
- “Create a high‑priority case for outage” or “Qualify this enterprise lead.”

## ServiceNow integration details

### Prerequisites
- ServiceNow instance with API access and appropriate roles (e.g., itil, admin).

### Required credentials
- Instance URL (e.g., acme.service-now.com), username, password.

### Available tools
- Create/update incidents and tickets, search KB, query records (CMDB, users, catalog).

### Example use
- “Log a Wi‑Fi incident and route appropriately,” or “Request access to the marketing drive.”

## Zendesk integration details

### Prerequisites
- Zendesk account with API access and admin token generation.

### Required credentials
- Subdomain (company for company.zendesk.com), email, API token.

### Available tools
- Create tickets, search customer history, update ticket status/assignee/priority, access KB.

### Example use
- “Open a login issue ticket and confirm last week’s ticket status.”
