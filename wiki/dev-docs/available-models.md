---
title: Available Models
summary: Overview of open-weight LLMs and embedding models hosted on Telnyx GPU infrastructure,
  including chat model specifications, pricing structure, regional availability, and
  data residency considerations.
sources:
- url: https://developers.telnyx.com/docs/inference/models
- url: https://developers.telnyx.com/docs/inference/models/pricing
- url: https://developers.telnyx.com/docs/inference/models/regions
updated_at: 2026-08-05T13:46:25Z
---

# Available Models

Overview of open-weight LLMs and embedding models hosted on Telnyx GPU infrastructure, including chat model specifications, pricing structure, regional availability, and data residency considerations.

Open-weight LLMs hosted on Telnyx GPU infrastructure. All models are accessible via the [Chat Completions API](chat-completions-api.md) (OpenAI-compatible).

## Chat Models

| Model ID | Parameters | Context Length | Best For |
| --- | --- | --- | --- |
| `moonshotai/Kimi-K3` | 2.8T | 1M | State-of-the-art open-weight intelligence for coding, reasoning, and multimodal work **(Recommended)** |
| `moonshotai/Kimi-K2.6` | 1.0T | 256K | Voice AI (with thinking disabled) |
| `zai-org/GLM-5.2` | 753.9B | 1M | Coding, reasoning, 1M context window |
| `MiniMaxAI/MiniMax-M3-MXFP8` | 428B | 1M | Cheapest while maintaining high intelligence |

## Embedding Models

| Model ID | Dimensions | Best For |
| --- | --- | --- |
| `thenlper/gte-large` | 1024 | Text embeddings |

## Pricing

Pay-per-token with no minimums and no commitments. For current per-model pricing, see [telnyx.com/pricing/inference-api](https://telnyx.com/pricing/inference-api).

| Category | Basis | Notes |
| --- | --- | --- |
| Text generation | Per 1M tokens (input + output) | Input and output priced separately; cached input tokens at a discount |
| Audio transcription | Per second of audio | Varies by model |
| Text-to-speech | Per 1M characters | Varies by voice/model |
| Embeddings | Per 1M tokens | Single rate |

## Regions & Availability

GPU infrastructure is deployed across five regions on four continents. Telnyx will endeavor to process requests in the region nearest the ingress domain you call, but this is not guaranteed.

### Current Regions

| Region | Location |
| --- | --- |
| US East | Atlanta |
| US West | Denver |
| EU | Paris |
| Asia-Pacific | Sydney |
| Middle East | UAE |

### Routing

Inference processing is latency-based, influenced by the ingress domain you call, not by your account's data locality setting. Telnyx will endeavor to process in the preferred region, but does not guarantee it:

| Ingress domain | Preferred region |
| --- | --- |
| `api.telnyx.com` | US |
| `api.telnyx.eu` | EU |
| `api.telnyx.com.au` | APAC |

Calling a regional ingress domain (for example, `api.telnyx.eu`) directs requests to the nearest GPU region for that domain under normal conditions. Telnyx does **not guarantee** processing location: during failover or capacity events, requests are processed at the next-lowest-latency region rather than failing. A region-selection API parameter is on the roadmap.

### Data Residency

Processing location and storage location are controlled separately:

- **Processing in transit** is latency-based, influenced by the ingress domain you call (see Routing above). Telnyx will endeavor to process in the preferred region, but it is not a guaranteed processing location.
- **Storage at rest** depends on the endpoint. The **chat completions** endpoint does not store request or response data. The **responses** endpoint stores conversations, and that storage is governed by your [Data Locality](data-locality.md) setting (US, EU, APAC, or Middle East).

For a full cross-product breakdown (including Voice AI Assistants), see the [Data Residency & Compliance FAQ](data-residency-compliance-faq.md).

### Roadmap

- Region selection API parameter
- Per-region model status and latency metrics
- Edge inference for sub-50ms response times
