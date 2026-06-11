---
title: Telnyx Inference API Overview
summary: 'A concise guide to getting started with Telnyx’s OpenAI-compatible Inference
  API: available models, regions and pricing, function calling, embeddings and retrieval,
  clustering analytics, and voice-outreach automation with AI Missions.'
sources:
- url: https://developers.telnyx.com/docs/inference/getting-started/index
- url: https://developers.telnyx.com/docs/inference/models/index
- url: https://developers.telnyx.com/docs/inference/models/pricing
- url: https://developers.telnyx.com/docs/inference/models/regions
- url: https://developers.telnyx.com/docs/inference/missions/index
- url: https://developers.telnyx.com/docs/inference/functions
- url: https://developers.telnyx.com/docs/inference/embeddings
- url: https://developers.telnyx.com/docs/inference/clusters
updated_at: 2026-05-20T08:36:12Z
---

# Telnyx Inference API Overview

*Part 1 of 2 — see also: [Part 2](telnyx-inference-api-overview--part-2.md)*

A concise guide to getting started with Telnyx’s OpenAI-compatible Inference API: available models, regions and pricing, function calling, embeddings and retrieval, clustering analytics, and voice-outreach automation with AI Missions.

## Quickstart

Prerequisites
- Telnyx account and API key
- Python 3.8+
- Any OpenAI-compatible SDK (set base_url)

Install the OpenAI SDK:

```
pip install openai
```

Python example (streaming chat):

```
import os
from openai import OpenAI

client = OpenAI(
  api_key=os.getenv("TELNYX_API_KEY"),
  base_url="https://api.telnyx.com/v2/ai/openai",
)

chat_completion = client.chat.completions.create(
  messages=[{"role": "user", "content": "Tell me about Telnyx"}],
  model="moonshotai/Kimi-K2.6",
  stream=True,
)

for chunk in chat_completion:
  if chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="", flush=True)
```

## Core concepts

### Messages
A chat is a list of messages forming conversation history.

### Roles
- system: instructions for model behavior
- user: end-user input
- assistant: model output
- tool: results from function/tool calls (see [Function Calling](function-calling.md))

### Models
All models are accessible via the OpenAI-compatible Chat Completions API. Browse the catalog in [Available Models](available-models.md).

Recommended highlights
- moonshotai/Kimi-K2.6 — 1.0T params, 256K context; highest intelligence; great at function calling and voice AI (with “thinking” disabled)
- zai-org/GLM-5.1-FP8 — 753.9B params, 202K context; efficient reasoning, strong for tools
- MiniMaxAI/MiniMax-M2.7 — 2M context; lowest cost while maintaining high intelligence

Embeddings
- thenlper/gte-large — 1024-dim text embeddings

### Streaming
Server-Sent Events, same behavior as OpenAI streaming.

## Regions and data residency
- Regions: US East (Atlanta), US West (Denver), EU (Paris), Asia-Pacific (Sydney)
- Routing: automatic to the nearest region based on your account’s data locality; no region parameter required
- Residency: inference runs in-region; EU accounts keep traffic in the EU. To pin traffic to a specific region for compliance, contact support

## Pricing
Pay-as-you-go with no commitments. See current rates at https://telnyx.com/pricing/inference-api
- Text generation: per 1M tokens (input and output metered separately); cached input tokens discounted
- Audio transcription: per second of audio
- Text-to-speech: per 1M characters
- Embeddings: per 1M tokens

## Function calling
Use the tools interface of the Chat Completions API to let models propose function calls; you execute them and feed results back as tool messages. All hosted models support tools; moonshotai/Kimi-K2.6 is a strong default.

Tool choice
- auto: model decides whether to call a tool
- required: force a tool call
- none: disallow tool calls

Minimal Python example:

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["location", "unit"],
            },
        },
    }
]

messages = [{"role": "user", "content": "How is the weather in Chicago?"}]
resp = client.chat.completions.create(
    model="moonshotai/Kimi-K2.6",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)
assistant_msg = resp.choices[0].message

# If tool_calls present: parse args, execute your function, then send results back as a tool message
```

For end-to-end patterns (including programmatic schemas and execution), see [Function Calling](function-calling.md).

## Embeddings and retrieval
Use Telnyx Storage + embeddings to ground model answers in your documents. See details in [Embeddings](embeddings.md).

Workflow
1) Upload documents to Telnyx S3-compatible Storage (portal or API)
2) Embed your bucket via API or the “Embed for AI Use” button in the portal
3) At query time, use the retrieval tool to supply relevant chunks to the model

Python example (chat over a bucket):

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TELNYX_API_KEY"),
    base_url="https://api.telnyx.com/v2/ai/openai",
)

question = "<ADD QUESTION HERE>"
bucket = "<ADD EMBEDDED BUCKET HERE>"
chat = client.chat.completions.create(
  messages=[{"role": "user", "content": question}],
  model="moonshotai/Kimi-K2.6",
  stream=True,
  tools=[{"type": "retrieval", "retrieval": {"bucket_ids": [bucket]}}],
)

for chunk in chat:
  if chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="", flush=True)
```

## Clusters (identify themes in your data)
After embedding a bucket, compute clusters to discover themes and subtopics. See [Identifying themes in your data with Clusters](identifying-themes-in-your-data-with-clusters.md).

Key parameters
- prefix/files: restrict clustering to a subset
- min_cluster_size: minimum points for broad themes
- min_subcluster_size: minimum points for niche subtopics

Create clusters:

```
curl --request POST \
  --url https://api.telnyx.com/v2/ai/clusters \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "bucket": "cluster-gatsby",
    "min_cluster_size": 50,
    "min_subcluster_size": 10
  }'
```

Response includes a task_id (e.g., {"data":{"task_id":"04dd624f-c9b3-4fc8-8cec-492c8696e9ea"}}).

Inspect results and graphs:

```
curl --request GET \
  --url "https://api.telnyx.com/v2/ai/clusters/04dd624f-c9b3-4fc8-8cec-492c8696e9ea?show_subclusters=true" \
  --header "Authorization: Bearer $TELNYX_API_KEY"

curl --request GET \
  --url "https://api.telnyx.com/v2/ai/clusters/04dd624f-c9b3-4fc8-8cec-492c8696e9ea/graph" \
  --header "Authorization: Bearer $TELNYX_API_KEY" --output clusters.png
```

Tips
- Increase min_cluster_size for broader, fewer clusters
- Use top_n_nodes to sample representative items per cluster
- Use cluster_id to explore a specific cluster’s subclusters

## AI Missions (voice outreach automation)
With AI Missions and the Telnyx Missions skill, agents can plan and execute multi-step outreach (research, phone calls, follow-ups) and deliver structured summaries. See [Voice Outreach with AI Missions](voice-outreach-with-ai-missions.md).

What you’ll need
- An OpenClaw agent
- Telnyx account and API key
- Telnyx Missions skill (configure TELNYX_API_KEY); the skill selects/assigns a number automatically

How it works (at a glance)
- Missions API: create mission, plan steps, log progress and results
- Assistants API: create a voice assistant (prompt, greeting, dynamic variables) and place calls
- Numbers API: pick and assign an outbound caller ID from your account

Typical flow
1) Create a mission and execution plan
2) Create/configure a purpose-built voice assistant
3) Assign a phone number and schedule calls (business hours, timezone-aware)
4) Place calls, monitor status (completed/failed/no answer/busy), capture transcripts and insights
5) Summarize results and store result_summary and result_payload

Portal views
- AI Missions dashboard: mission statuses, last updates, and run summaries
- Run detail: inputs, timing, final structured results (e.g., quotes, recommendations, conversation IDs)
- Conversations: transcripts with audio playback and per-turn latency (STT, LLM, TTS)

Insights
- Use AI Insights to extract structured data (e.g., pricing, availability, terms) from conversations
