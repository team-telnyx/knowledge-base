---
title: Telnyx Inference
summary: Telnyx Inference provides an OpenAI-compatible API for large language model
  chat completions, function calling, embeddings, and clustering, alongside AI Insights
  for conversation analysis and Voice AI Assistants for telephony-based conversational
  agents. This page covers the core API, integrations, data residency, and practical
  tutorials.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
  content_hash: ff522f2e6bd1723aaae77aa0136c8445286d925413287656782da4be07d09f11
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
  content_hash: 7b522bb1ea6820875819e42eeb02ef42c22beea5981ac6d32e5415b96292655b
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
  content_hash: 50e16a3392164849e8db62587e0a7d5fdc2f38c5f7bf22efbf8816070480878f
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
  content_hash: 0bf1cdff1a2e68b76975f93b097d45c41337877c1dbbba2397ea493699f9fd35
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
  content_hash: 35e09b760fc2688800b0cbec4812a2b908b2893f4c2b014c4c85e4b020cfe572
- url: https://developers.telnyx.com/docs/inference/clusters
  content_hash: 2168a5dbf3b8c93576ac5ca7eb6daef42850a48d2787e29743f161a668bc6b0d
- url: https://developers.telnyx.com/docs/inference/crewai
  content_hash: bb1baccf1e6687a03af6f732aaceb0e310beb83d0b6ce6aa7f9cb934418a351b
- url: https://developers.telnyx.com/docs/inference/data-residency
  content_hash: 5ec98630f8132d215237b19167267f10bf0a0afc3879a204570c1e18258b6c5b
- url: https://developers.telnyx.com/docs/inference/embeddings
  content_hash: da55ec529bd85eaa5fbcc3baac0d1b3d0c01b0d70cc62a03854a507fe8accdf0
- url: https://developers.telnyx.com/docs/inference/functions
  content_hash: d8787dd1d761b9535b4b844287b039a25c7cc0a895592a3309b5da4b3f1ceb15
- url: https://developers.telnyx.com/docs/inference/getting-started/index
  content_hash: 91d21b775b382bcbd90ae079c0b93ca3854a5cfea589b985c25e9a151ea79b45
updated_at: 2026-06-11T10:33:19Z
---

# Telnyx Inference

*Part 5 of 6 — see also: [Part 1](telnyx-inference--part-1.md), [Part 2](telnyx-inference--part-2.md), [Part 3](telnyx-inference--part-3.md), [Part 4](telnyx-inference--part-4.md), [Part 6](telnyx-inference--part-6.md)*

Telnyx Inference provides an OpenAI-compatible API for large language model chat completions, function calling, embeddings, and clustering, alongside AI Insights for conversation analysis and Voice AI Assistants for telephony-based conversational agents. This page covers the core API, integrations, data residency, and practical tutorials.

## Data Residency

Telnyx AI spans two products that handle processing location differently:

- **Inference API** — chat completions, responses endpoint, and related model APIs.
- **Voice AI Assistants** — telephony-based conversational agents.

### Processing vs. Storage

Telnyx offers **hard controls for data at rest** (storage location and retention) but **does not offer hard controls for processing location**. Where a request is *processed* is **latency-based and best-effort** — influenced, not guaranteed. Under failover or capacity events, processing shifts to the next-best region rather than failing.

| | Processing (best-effort) | Storage at rest (hard control) |
|---|---|---|
| **Inference API** | Influenced by ingress domain (`api.telnyx.com` → US, `api.telnyx.eu` → EU, `api.telnyx.com.au` → APAC). Not guaranteed. | Chat completions: not stored. Responses endpoint: governed by data locality. |
| **Voice AI Assistants** | Influenced by the anchorsite on the TeXML application. Not guaranteed. | Governed by data locality flag + data-retention setting. |

### Inference API Details

- **Chat completions endpoint** does not store request or response data.
- **Responses endpoint** stores conversations; storage region is governed by your [Data Locality](https://developers.telnyx.com/docs/account-setup/data-locality) setting.
- Traffic **cannot be pinned** to a specific region as a hard guarantee.

### Voice AI Assistant Details

- Processing location is influenced by the **anchorsite** on the assistant's TeXML application (best-effort, not guaranteed).
- Storage at rest is a **hard control** governed by your data locality flag.
- Recordings are **enabled by default** but can be disabled; when enabled, they are stored as Media Storage subject to data locality.

### Data Retention

Voice AI Assistants expose a `privacy_settings.data_retention` setting (enabled by default). When **disabled**, the assistant stops persisting conversation **content** while continuing minimum processing to run and bill the call:

| Item | Retention Off |
|---|---|
| Conversation messages / transcripts | Not persisted |
| Insights | Not retained (may be computed transiently in-memory) |
| Transcript/answer in observability logs | Replaced with placeholders |
| LLM request/response content logging | Disabled |
| TTS cache | Disabled |

A limited set of records is still retained even when retention is off (latency/timing metrics, billing/security/fraud-prevention records).

### STT, TTS, and LLM Providers

Some providers are **self-hosted by Telnyx** (processing stays on Telnyx infrastructure); others are **third-party** (processing routes to the vendor). Region remains best-effort for all providers.

**Self-hosted STT**: `deepgram/flux`, `deepgram/nova-3`, `deepgram/nova-2`, `assemblyai/universal-streaming`, `speechmatics/standard`, `distil-whisper/distil-large-v2`.

**Third-party STT**: `azure/fast`, `soniox/stt-rt-v4`, `xai/grok-stt`.

**Self-hosted TTS**: Telnyx in-house voices (including Telnyx Ultra), Rime, Resemble.

**Third-party TTS**: ElevenLabs, AWS, Azure, Minimax, Inworld, xAI.

**Self-hosted LLM**: Qwen and Moonshot (Kimi) model families (e.g., `Qwen/Qwen3-235B-A22B`, `moonshotai/Kimi-K2.5`, `moonshotai/Kimi-K2.6`).

**Third-party LLM**: Anthropic (Claude), OpenAI (GPT), Google (Gemini) — prompts are sent to the external provider.

If data residency or third-party data sharing is a concern, choose a self-hosted model to keep prompt and response generation on Telnyx infrastructure.

### Example: EU-Focused Voice AI Setup

A typical EU-oriented configuration:

- **Data locality:** EU (Germany) — hard control over storage at rest
- **Anchorsite on TeXML app:** an EU site (e.g., Frankfurt) — best-effort influence over processing
- **Voice API endpoint:** `api.telnyx.eu`
- **SIP endpoint:** `sip.telnyx.eu`

For contractual data commitments, [contact support](mailto:support@telnyx.com) or your Telnyx account team.

## Framework Integrations

### CrewAI

Use Telnyx as the LLM backend for CrewAI agents:

```bash
pip install crewai
```

Set environment variables for global routing:

```bash
export TELNYX_API_KEY=your_telnyx_api_key
export OPENAI_BASE_URL=https://api.telnyx.com/v2/ai/openai
```

Or configure per-agent:

```python
import os
from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="zai-org/GLM-5.1-FP8",
    base_url="https://api.telnyx.com/v2/ai/openai",
    api_key=os.getenv("TELNYX_API_KEY"),
)

researcher = Agent(
    role="Research Analyst",
    goal="Find and analyze information",
    backstory="You are an experienced research analyst.",
    llm=llm,
)

writer = Agent(
    role="Technical Writer",
    goal="Write clear, accurate reports",
    backstory="You are a skilled technical writer.",
    llm=llm,
)

research_task = Task(description="Research the latest trends in AI infrastructure", agent=researcher)
write_task = Task(description="Write a summary report based on the research findings", agent=writer)

crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()
print(result)
```

Tool calling is also supported:

```python
from crewai.tools import tool

@tool("Search the web")
def search_web(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"

researcher = Agent(
    role="Research Analyst",
    goal="Find and analyze information",
    backstory="You are an experienced research analyst.",
    llm=llm,
    tools=[search_web],
)
```
