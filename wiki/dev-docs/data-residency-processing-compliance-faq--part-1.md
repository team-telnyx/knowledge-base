---
title: Data Residency, Processing & Compliance FAQ
summary: Answers common customer questions about where Telnyx AI data is processed
  and stored, which providers are used, retention behavior, and model training — covering
  both the Inference API and Voice AI Assistants.
sources:
- url: https://developers.telnyx.com/docs/inference/data-residency/index
updated_at: 2026-08-05T13:46:09Z
---

# Data Residency, Processing & Compliance FAQ

*Part 1 of 3 — see also: [Part 2](data-residency-processing-compliance-faq--part-2.md), [Part 3](data-residency-processing-compliance-faq--part-3.md)*

Answers common customer questions about where Telnyx AI data is processed and stored, which providers are used, retention behavior, and model training — covering both the Inference API and Voice AI Assistants.

## Processing vs. storage: the key distinction

Telnyx AI spans two products that handle **processing location** differently:

- **Inference API** — chat completions, the responses endpoint, and related model APIs.
- **Voice AI Assistants** — telephony-based conversational agents.

| | Processing in transit (not guaranteed) | Storage at rest (hard control) |
| --- | --- | --- |
| **Inference API** | Latency-based, influenced by the **ingress domain** you call (`api.telnyx.com`, `api.telnyx.eu`, `api.telnyx.com.au`). Not tied to data locality. Not guaranteed. | Chat completions: **not stored**. Responses endpoint (stores conversations): governed by your **data locality** setting (US, EU, APAC, or Middle East). |
| **Voice AI Assistants** | Influenced by the **anchorsite** on the assistant's TeXML application. Telnyx will endeavor to honor it, but it is not guaranteed. | Governed by your **data locality** flag, plus the **data-retention** setting for conversation content. |

[Data Locality](data-locality.md) governs **storage at rest** for covered data types (available regions: US, EU, APAC, and Middle East). Neither the data locality flag nor the anchorsite is a hard guarantee of where live **processing** happens.

## Inference API

### Where is Inference processing performed?

Inference **processing in transit is latency-based, influenced by the ingress domain you call**, not by your data locality setting. Telnyx will endeavor to process in the preferred region, but does not guarantee it:

| Ingress domain | Preferred region |
| --- | --- |
| `api.telnyx.com` | US |
| `api.telnyx.eu` | EU |
| `api.telnyx.com.au` | APAC |

Calling a regional ingress domain (for example, `api.telnyx.eu`) directs requests to the nearest GPU region for that domain. Telnyx will endeavor to route to that region, but does **not guarantee** the processing location: during failover or capacity events, requests are processed at the next-lowest-latency region rather than failing. See [Inference Regions & Availability](inference-regions-availability.md) for the underlying GPU regions.

### Does Inference store my data?

It depends on the endpoint:

- **Chat completions endpoint** — **does not store** request or response data.
- **Responses endpoint** — **stores conversations**. For stored data, your [Data Locality](data-locality.md) setting dictates the storage region.

### Can Inference traffic be pinned to a specific region?

Not as a hard guarantee. Routing is **latency-based**: calling a regional ingress domain (for example, `api.telnyx.eu`) directs requests to that region under normal conditions, and Telnyx will endeavor to keep them there, but Telnyx does **not guarantee** processing location. During failover or capacity events, requests are processed at the next-lowest-latency region rather than failing. If you have a strict compliance requirement for guaranteed processing location, [contact support](mailto:support@telnyx.com) to discuss what is possible for your account.

## Voice AI Assistants

### Where is Voice AI Assistant processing performed?

For Voice AI Assistants, processing location is **influenced by the anchorsite** configured on the assistant's **TeXML application** — not by the data locality flag. Setting the anchorsite (for example, Frankfurt for the EU) directs media/processing to that region under normal conditions.

The anchorsite is **not a hard control**. Telnyx will endeavor to honor it, but does not guarantee processing location: under failover or capacity events, processing can shift to another region rather than failing the call.

### Where is Voice AI Assistant data stored?

**Storage location at rest is a hard control, governed by your [Data Locality](data-locality.md) flag.** Retention of conversation content is further controlled by the **data-retention** setting (see [Data retention and model training](#data-retention-and-model-training)). Recording storage can also be directed to your own storage destination, which Telnyx respects.

### Are call audio, transcripts, prompts, responses, summaries, or recordings ever handled outside the configured region?

- **Processing** location is influenced by the assistant's anchorsite; Telnyx will endeavor to honor it, but it is **not guaranteed**.
- **Storage at rest** is a hard control, following your **data locality** flag. Recordings can be directed to a customer-controlled storage destination, which Telnyx respects.

Telnyx does **not** contractually guarantee blanket "EU-only processing." Telnyx will endeavor to honor processing controls but does not guarantee them, "processing" is defined very broadly, and some components — for example, third-party STT/TTS providers, or operational/security/fraud handling — may involve activity outside a single region. The specifics depend on the providers and features you enable. Confirm written data commitments with your account team and DPA before making representations to your own customers.

### Example: EU-focused Voice AI setup

A typical EU-oriented configuration combines:

- **Data locality:** EU (Germany) — a hard control over storage at rest
- **Anchorsite on the TeXML app:** an EU site (for example, Frankfurt) — Telnyx will endeavor to influence media/processing location, but it is not guaranteed
- **Voice API endpoint:** `api.telnyx.eu`
- **SIP endpoint:** `sip.telnyx.eu`

This keeps storage in the EU (a hard control via data locality) and steers processing toward the EU (via the anchorsite, which Telnyx will endeavor to honor but does not guarantee). STT/TTS provider choice also matters — some providers are self-hosted by Telnyx and some are third parties (see below).
