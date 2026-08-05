---
title: Embedding & RAG
summary: Embedding and retrieval-augmented generation (RAG) let applications search
  prior knowledge before asking a model to respond. This page covers the primitives
  that add memory or searchable context to an AI workflow, including embeddings and
  conversation history search.
sources:
- url: https://developers.telnyx.com/docs/inference/embedding-rag
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/feature-coverage
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/index
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/pricing
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/retention
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/searching
updated_at: 2026-08-05T13:45:57Z
---

# Embedding & RAG

Embedding and retrieval-augmented generation (RAG) let applications search prior knowledge before asking a model to respond. This page covers the primitives that add memory or searchable context to an AI workflow, including embeddings and conversation history search.

## Overview

Embedding and retrieval-augmented generation (RAG) let your applications search prior knowledge before asking a model to respond. These primitives add memory or searchable context to an AI workflow and can be used with AI Assistants, custom agent runtimes, or your own application code.

The available primitives are:

- [Embeddings](embeddings.md) — Generate embeddings from documents stored in Telnyx Storage and use them as retrieval context.
- [Conversation History](conversation-history.md) — Search persisted conversation transcripts and messages.

## Conversation History

Conversation History stores and indexes conversation records so your agents can search previous interactions and use them as memory or retrieval context.

### How It Works

1. Enable conversation persistence on a supported source.
2. Telnyx stores and indexes the conversation record.
3. Search the indexed history by text, record type, region, and filters.
4. Use search results as retrieval context for RAG.

### Feature Coverage

Conversation History coverage is organized by communication channel. Voice records are currently available from SIP connections.

#### Voice

Voice coverage currently includes call history from SIP connections. Enable `conversation_persistence` on a covered SIP connection resource to store and index voice conversation history.

Supported connection types:

- `ip_connections`
- `credential_connections`
- `fqdn_connections`

Enable:

```
PATCH /v2/credential_connections/{id}
```

```
{
  "conversation_persistence": true
}
```

Disable:

```
PATCH /v2/credential_connections/{id}
```

```
{
  "conversation_persistence": false
}
```

Verify:

```
GET /v2/credential_connections/{id}
```

The response includes `conversation_persistence` on the connection resource.

#### Messaging

Coming soon.

#### Email

Coming soon.

### Searching

Run a semantic search across persisted conversation records with `GET /v2/ai/conversation_histories`. Your query text is embedded into a vector and matched against indexed transcript chunks, so each result is a single chunk with a relevance `score` and its parent record's metadata — ready to use as retrieval context for RAG.

```
curl --globoff \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  "https://api.telnyx.com/v2/ai/conversation_histories?q=flight+refund&record_type=voice&top_k=10"
```

Pass a query (`q`) and a `record_type` (use `voice` for SIP call history). Narrow results with the `region`, `min_score`, and `filter[field][operator]` parameters. See the **Search conversation histories** API reference for the full set of parameters, filter operators, the response schema, and SDK code samples.

### Retention

Conversation History includes 30 days of indexed retention for persisted conversation records.

#### Default Retention

Conversation History stores and indexes covered conversation records for 30 days by default. During the included retention period, records can be returned by the Conversation Histories API when they match the search query and filters.

#### After 30 Days

After the included 30-day retention period, records are no longer retained for indexed Conversation History search unless extended retention is enabled.

#### Retention Scope

This retention behavior applies to Conversation History indexing and search. It does not describe retention for the source product that generated the record, such as call recordings, messaging records, or other product-specific storage.

### Pricing

Conversation History pricing has three parts: persisted text, extended storage, and search.

#### Rates

| Usage | Price | Notes |
| --- | --- | --- |
| Embed and persist | `$0.0015 / 1K characters` | Billed once on input transcript characters. Includes 30 days of retention. |
| Storage after 30 days | `$0.60 / GiB-month` | Applies only when extended retention is enabled. |
| Vector search | `$0.003 / search` | First 10,000 searches per month are free of charge. |

#### Example

A 10-minute call with about 10,000 transcript characters and one search within the free tier would be priced as:

| Line Item | Calculation | Price |
| --- | --- | --- |
| Embed and persist | `10K characters * $0.0015` | `$0.015` |
| Storage within 30 days | Included | `$0.00` |
| One vector search | Included in the first 10,000 searches per month | `$0.00` |
| Total |  | `~$0.015` |

## Next Steps

- [Review Conversation History feature coverage](conversation-history.md)
- [Search conversation history](conversation-history.md)
- [Review retention](conversation-history.md)
- [View pricing](conversation-history.md)
