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

*Part 2 of 3 — see also: [Part 1](data-residency-processing-compliance-faq--part-1.md), [Part 3](data-residency-processing-compliance-faq--part-3.md)*

Answers common customer questions about where Telnyx AI data is processed and stored, which providers are used, retention behavior, and model training — covering both the Inference API and Voice AI Assistants.

## STT, TTS, and LLM providers (Voice AI)

For Voice AI Assistants, the STT, TTS, and LLM providers in use depend on the models and voices **you select**. Some are **self-hosted by Telnyx** (run on Telnyx-operated infrastructure); others are **third-party** services that Telnyx integrates with. This distinction matters for compliance: self-hosted models keep that processing step within Telnyx infrastructure, whereas third-party models route that step to the vendor.

Hosting (self-hosted vs. third-party) is about *which infrastructure* performs the step, not a guarantee of *region*. Processing region is not guaranteed for any provider — see the [processing vs. storage](#processing-vs-storage-the-key-distinction) note above.

### Speech-to-text (STT)

| Model | Provider | Hosting |
| --- | --- | --- |
| `deepgram/flux` | Deepgram | Self-hosted by Telnyx |
| `deepgram/nova-3` | Deepgram | Self-hosted by Telnyx |
| `deepgram/nova-2` | Deepgram | Self-hosted by Telnyx |
| `assemblyai/universal-streaming` | AssemblyAI | Self-hosted by Telnyx |
| `speechmatics/standard` | Speechmatics | Self-hosted by Telnyx |
| `distil-whisper/distil-large-v2` | Whisper (English-only) | Self-hosted by Telnyx |
| `azure/fast` | Azure | Third-party |
| `soniox/stt-rt-v4` | Soniox | Third-party |
| `xai/grok-stt` | xAI | Third-party |

### Text-to-speech (TTS)

TTS is delivered through Telnyx's TTS gateway, which integrates multiple providers. The provider depends on the voice you select:

| Provider | Hosting |
| --- | --- |
| Telnyx (in-house voices, including Telnyx Ultra) | Self-hosted by Telnyx |
| Rime | Self-hosted by Telnyx |
| Resemble | Self-hosted by Telnyx |
| ElevenLabs | Third-party |
| AWS | Third-party |
| Azure | Third-party |
| Minimax | Third-party |
| Inworld | Third-party |
| xAI | Third-party |

See [Text to Speech voices](text-to-speech-voices.md) for the current voice catalog.

### Large language model (LLM)

The assistant's model is served through Telnyx's inference platform. The model in use is the one you configure on the assistant.

**Self-hosted by Telnyx** (open models served on Telnyx infrastructure) include the **Qwen** and **Moonshot (Kimi)** model families — for example, `Qwen/Qwen3-235B-A22B`, `moonshotai/Kimi-K2.5`, and `moonshotai/Kimi-K2.6`.

**Third-party** models — including those from **Anthropic** (Claude), **OpenAI** (GPT), and **Google** (Gemini) — are **not self-hosted**. When you select one of these, the prompt is sent to that external provider to generate the response.

The available models evolve over time — for the current catalog and which models are recommended for assistants, see [Models](models.md).

If data residency or third-party data sharing is a concern, choose a self-hosted model (a Qwen or Moonshot/Kimi model) to keep prompt and response generation on Telnyx infrastructure. Region is not guaranteed even for self-hosted models.

### Can STT, TTS, or LLM processing be restricted to the EU?

There is **no hard guarantee** of processing region for any provider — Telnyx will endeavor to honor the configured region, but does not guarantee it. In addition:

- **Self-hosted** providers keep that processing step on Telnyx infrastructure, but region is not guaranteed.
- **Third-party** providers route that step to the vendor, whose own region behavior applies.

If you need STT, TTS, or LLM processing constrained to a specific region, [contact support](mailto:support@telnyx.com) so we can advise which self-hosted provider/model combinations best fit your requirement. Hard region guarantees are not offered for processing.

## Recordings

### Are call recordings disabled by default?

No — for Voice AI Assistants, **call recordings are enabled by default**, and you can turn them off. When recordings are enabled, the recording is stored as Media Storage, which is subject to your [Data Locality](data-locality.md) setting. Disable recording on the assistant (or per call) if you do not want recordings retained.

## Data retention and model training

### What does the data-retention setting control?

Voice AI Assistants expose a **data-retention** privacy setting (`privacy_settings.data_retention`). It is **enabled by default**. When you disable it, the assistant stops persisting conversation **content** while continuing the minimum processing needed to run and bill the call.

When `data_retention` is **disabled**, conversation content is **not retained**:

| Item | Behavior when retention is off |
| --- | --- |
| Conversation messages / transcripts | Not persisted to the conversations store |
| Insights | Not retained. An insight may be computed transiently in-memory to support live conversation behavior, but the conversation and its insights are not stored |
| Transcript and assistant answer in observability logs | Not retained; replaced with placeholders (for example, `[transcript not available]` / `[answer not available]`) |
| LLM request/response content logging | Disabled |
| TTS cache | Disabled, so synthesized audio is not cached |

A limited set of records is still **retained** even when conversation retention is off, because they are required to operate and bill the service:

| Item | Behavior when retention is off |
| --- | --- |
| Latency / timing metrics | Retained (timing only, no conversation content) |
| Billing, security, and fraud-prevention records | Retained as required for legitimate business and compliance purposes |

The data-retention flag governs retention of **conversation content** for Voice AI Assistants. Disabling it stops persistence of conversation content and insights; it does not change where data that *is* retained lives — storage region is controlled by [Data Locality](data-locality.md). Recordings are governed separately by the recording setting (see [Recordings](#recordings) above). For a guarantee tailored to your exact configuration (audio, tool inputs/outputs, memory, observability traces, and third-party provider logs), confirm in writing with your account team and DPA.

### Can a customer opt out of model improvement / training / evaluation?

Customer data handling for model training is governed by Telnyx's applicable terms and DPA. If you require an opt-out from model improvement, training, or evaluation — for both input and output data, and covering Telnyx and any third-party AI providers in your configuration — [contact your account team](mailto:support@telnyx.com) to confirm the governing terms and document the opt-out.

## Usage reporting and billing

### Can usage be broken down by assistant, phone number, or metadata/tag?

Usage and conversation data can be attributed using identifiers such as the assistant, the associated phone number, and metadata. For subscriber-level or per-tag billing breakdowns, [contact support](mailto:support@telnyx.com) to confirm which dimensions are available and how to structure metadata/tags for clean attribution. See [Agent Observability](agent-observability.md) and [Session Analysis](session-analysis.md).

## Related resources

- [Data Locality](data-locality.md)
- [Inference Regions & Availability](inference-regions-availability.md)
- [Models](models.md)
- [Transcription Settings](transcription-settings.md)
- [Text to Speech voices](text-to-speech-voices.md)
- [Agent Observability](agent-observability.md)
