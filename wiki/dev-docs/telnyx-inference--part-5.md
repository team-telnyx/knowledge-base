---
title: Telnyx Inference
summary: Telnyx Inference provides an OpenAI-compatible API for large language model
  chat completions, function calling, embeddings, and clustering, alongside AI Insights
  for conversation analysis and Voice AI Assistants for telephony-based conversational
  agents. This page covers the core API, integrations, data residency, and practical
  tutorials.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
- url: https://developers.telnyx.com/docs/inference/clusters
- url: https://developers.telnyx.com/docs/inference/crewai
- url: https://developers.telnyx.com/docs/inference/data-residency
- url: https://developers.telnyx.com/docs/inference/embeddings
- url: https://developers.telnyx.com/docs/inference/functions
- url: https://developers.telnyx.com/docs/inference/getting-started/index
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
