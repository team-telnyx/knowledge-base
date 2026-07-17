---
title: Telnyx Reporting
summary: Telnyx reporting combines the v2 Usage Reports API for aggregated usage data,
  the Session Analysis API for tree-based per-session cost and event inspection, and
  On-Demand Reports for natural-language queries against the same usage data.
sources:
- url: https://developers.telnyx.com/docs/reporting/on-demand-reports/index
- url: https://developers.telnyx.com/docs/reporting/session-analysis/index
- url: https://developers.telnyx.com/docs/reporting/usage-reports/index
updated_at: 2026-07-17T09:16:44Z
---

# Telnyx Reporting

*Part 3 of 4 — see also: [Part 1](telnyx-reporting--part-1.md), [Part 2](telnyx-reporting--part-2.md), [Part 4](telnyx-reporting--part-4.md)*

Telnyx reporting combines the v2 Usage Reports API for aggregated usage data, the Session Analysis API for tree-based per-session cost and event inspection, and On-Demand Reports for natural-language queries against the same usage data.

## Session Analysis API

Session Analysis gives you a complete view of costs and events for any usage session on the Telnyx platform:

- **Full event tree** — parent events, child events, and their relationships
- **Rollup costs** — per-event costs plus cumulative totals across the session
- **Product linkages** — how different Telnyx products interacted in a single session

This is especially valuable for AI-powered sessions, where a single call can involve multiple Telnyx products — AI Voice Assistant, inference, speech-to-text, text-to-speech, call control, SIP trunking, and more — all layered into one conversation.

### When to Use It

| Use Case | Why Session Analysis Helps |
| --- | --- |
| AI session cost breakdown | See the full cost tree for an AI assistant call, broken down by inference turns, STT/TTS, and infrastructure costs |
| Troubleshooting | Trace the complete event chain to debug unexpected call flow or billing issues |
| Usage auditing | Verify which products and services were consumed during a session |
| Cost optimization | Identify which components of an AI session drive the most cost and optimize accordingly |

### Core Concepts

#### Record Types

A **record type** identifies the category of usage event for a Telnyx product. Each record type maps to a specific product and has defined relationships to other record types. For example, `ai-voice-assistant` is the record type for AI Voice Assistant sessions, which have `inference` events as children.

#### Sessions

A **session** is a tree of related usage events. The **root event** is the primary event you are analyzing. **Child events** are related usage that occurred as part of that session. For example, an AI Voice Assistant call involves a `call-session` root with a `call-control` child, which in turn has an `ai-voice-assistant` child with `inference` events underneath — each representing one LLM turn in the conversation.

#### Relationships

Events are connected via relationships:

| Relationship | Direction | Example |
| --- | --- | --- |
| `child_of` | Parent → Child | An `ai-voice-assistant` event has `inference` children (one per LLM turn) |
| `parent_of` | Child → Parent | An `inference` event has a parent `ai-voice-assistant` session |

Relationships are defined via **field mappings** — the child's `local_field` matches the parent's `parent_field`. For example, `inference` events link to their `ai-voice-assistant` parent via the `conversation_id` field.

#### Cost Rollup

Each event node includes:

- **`event_cost`** — cost of this individual event
- **`cumulative_cost`** — this event's cost plus all descendant costs

The root event's `cumulative_cost` equals the total session cost. For AI sessions, this means the `call-session` cumulative cost includes everything — the AI assistant, each inference turn, STT, TTS, call control, and SIP trunking — rolled up into one number.

### Endpoints

#### 1. List All Record Types

```
GET /v2/session_analysis/metadata
```

Returns all available record types, their relationships, and query parameter options. The response includes:

- `record_types[]` — array of all record types with their parent/child relationships
- `query_parameters` — valid parameters for session analysis queries
- `meta` — total count and last updated timestamp

```
curl "https://api.telnyx.com/v2/session_analysis/metadata" \
 -H "Authorization: Bearer YOUR_API_KEY"
```

#### 2. Get Record Type Details

```
GET /v2/session_analysis/metadata/{record_type}
```

Returns metadata for a specific record type with additional details:

- Valid child and parent relationships
- Example query URLs
- Recommended max depth for traversal

```
curl "https://api.telnyx.com/v2/session_analysis/metadata/ai-voice-assistant" \
 -H "Authorization: Bearer YOUR_API_KEY"
```

#### 3. Get Session Analysis

```
GET /v2/session_analysis/{record_type}/{event_id}
```

Retrieves the full session analysis tree for a specific event.

**Path Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| `record_type` | string | The record type identifier (see the Record Types Reference below) |
| `event_id` | UUID | The event's unique identifier |

You can find event IDs in the individual webhooks or detail records for the applicable event.

**Which record type should I use?** If you are analyzing a call made with your AI assistant, start with `call-session`. This gives you the full picture — AI assistant sessions, inference events, call control, SIP trunking, and all other products in one tree. Use the metadata endpoint to explore other starting points for different products.

**Query Parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `include_children` | boolean | `true` | Include child events in the response |
| `max_depth` | integer | `2` | Maximum traversal depth (1–5) |
| `expand` | string | `record` | Only `record` (include full record data) or `none` (omit record data) |
| `date_time` | ISO 8601 | — | Timestamp to narrow index selection (improves performance) |

```
curl "https://api.telnyx.com/v2/session_analysis/call-session/a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d?include_children=true&max_depth=3&date_time=2026-03-17" \
 -H "Authorization: Bearer YOUR_API_KEY"
```

### Response Structure

#### Top-Level Fields

```
{
 "session_id": "4c9d22b0-1e4b-11f1-83a0-02420aef51a1",
 "cost": {
 "total": "0.009800",
 "currency": "USD"
 },
 "root": { /* EventNode */ },
 "meta": {
 "event_count": 3,
 "products": ["ai-voice-assistant", "inference", "callcontrol-cdrs"]
 }
}
```

| Field | Description |
| --- | --- |
| `session_id` | Identifier for the analyzed session |
| `cost.total` | Total session cost (sum of all events) |
| `cost.currency` | ISO 4217 currency code |
| `root` | Root event node (tree structure) |
| `meta.event_count` | Total events in the tree |
| `meta.products` | Unique products involved in the session |

#### Event Node Structure

Each event in the tree follows this structure:

```
{
 "id": "4c9d22b0-1e4b-11f1-83a0-02420aef51a1",
 "product": "callcontrol-cdrs",
 "event_name": "callcontrol-cdrs",
 "relationship": null,
 "cost": {
 "event_cost": "0.000000",
 "cumulative_cost": "0.009800",
 "currency": "USD"
 },
 "links": {
 "self": "/v2/session_analysis/call-control/4c9d22b0-...",
 "records": "/v2/detail_records?record_type=call-control&id=4c9d22b0-..."
 },
 "record": { /* Full detail record */ },
 "children": [ /* Array of child EventNodes */ ]
}
```

| Field | Description |
| --- | --- |
| `id` | Event identifier |
| `product` | Internal product identifier |
| `event_name` | Event type name |
| `relationship` | How this event relates to its parent (null for root) |
| `cost.event_cost` | Cost of this individual event |
| `cost.cumulative_cost` | This event + all descendants |
| `links.self` | Link to this analysis node |
| `links.records` | Link to underlying detail records |
| `record` | Full detail record data (varies by record type) |
| `children` | Child event nodes |

#### Relationship Object

For child events, the `relationship` field explains the connection:

```
{
 "type": "child_of",
 "via": {
 "local_field": "conversation_id",
 "parent_field": "conversation_id"
 },
 "parent_id": "4c9063e0-1e4b-11f1-b789-02420aef51a1"
}
```

| Field | Description |
| --- | --- |
| `type` | Relationship type (`child_of` or `parent_of`) |
| `via.local_field` | Field on this record that links to parent |
| `via.parent_field` | Field on the parent record that is matched |
| `parent_id` | Identifier of the parent event |

The `via` fields vary by relationship. AI-related linkages often use `conversation_id`, while voice/telephony relationships typically use `telnyx_session_id` or `call_session_id`.

### Example: AI Voice Assistant Session

A customer makes an inbound call to an AI Voice Assistant using the Telnyx Web Dialer. The assistant handles a multi-turn conversation over ~152 seconds.

**Query:**

```
curl "https://api.telnyx.com/v2/session_analysis/call-session/a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d?max_depth=5&include_children=true&date_time=2026-03-17" \
 -H "Authorization: Bearer YOUR_API_KEY"
```

**Session tree:**

```
call-session (SIP Trunking) event: $0.0000 cumulative: $0.2128
├── recording event: $0.0051 cumulative: $0.0051
├── webrtc event: $0.0052 cumulative: $0.0052
├── sip-trunking event: $0.0052 cumulative: $0.0052
└── call-control event: $0.0052 cumulative: $0.1973
    └── ai-voice-assistant event: $0.1800 cumulative: $0.1921
        ├── inference event: $0.0010
        ├── inference event: $0.0015
        ├── inference event: $0.0029
        ├── inference event: $0.0033
        └── inference event: $0.0034
```

**Summary:**

| Field | Value |
| --- | --- |
| Total session cost | $0.2128 |
| Event count | 11 |
| Duration | ~152 seconds |
| Products involved | siptrunking-cdrs, recording-cdrs, webrtc-cdrs, callcontrol-cdrs, ai-voice-assistant, inference |

**Key observations:**

- The **call-session** root has $0.00 event cost — it is a container for the session, not a billable event itself.
- **ai-voice-assistant** is the dominant cost at $0.18 (billed at $0.06/min for 3 billed minutes). Its cumulative cost of $0.1921 includes 5 inference events underneath.
- Each **inference** event represents a single LLM call during the conversation — one per assistant turn. The cost per turn varies based on the model and token count.
- **call-control** has a $0.0052 event cost but a $0.1973 cumulative cost — the difference is the ai-voice-assistant subtree rolling up underneath it.
- **recording**, **webrtc**, and **sip-trunking** are leaf nodes with no children, so their event cost equals their cumulative cost.

#### Understanding the AI Cost Structure

In an AI-powered call, costs come from multiple layers:

| Layer | Record Type | What You Are Billed For |
| --- | --- | --- |
| AI Assistant | `ai-voice-assistant` | Time-based (per minute of assistant usage) |
| LLM Inference | `inference` | Per-turn (each LLM call is a separate event) |
| Call Control | `call-control` | Time-based (per minute of call control usage) |
| Transport | `sip-trunking`, `webrtc` | Time-based (per minute for the voice leg) |
| Add-ons | `recording`, `speech-to-text`, `text-to-speech` | Per-use or per-minute depending on the product |

Session Analysis rolls all of these into one tree, so you can see exactly where cost accumulates — whether it is the AI assistant minute rate, the number of inference turns, or the underlying voice transport.

### Common Use Cases

#### Debugging High-Cost AI Sessions

1. Query the session with `max_depth=5` to get the full tree.
2. Look at `meta.products` to see which products were involved.
3. Compare `event_cost` across children — if `ai-voice-assistant` is the driver, check how many inference turns occurred underneath.
4. Check `record` fields for rate information (`rate`, `rate_measured_in`) and duration.

#### Finding Related Events

1. Start from any event in the tree.
2. Use `relationship.via` to understand the field linkage.
3. Query the parent or children directly using their `id`.

#### Exporting for Analysis

1. Use `expand=none` to get just the tree structure without full records.
2. Flatten the tree programmatically for spreadsheet import.
3. Or keep full records and parse specific fields (for example, `rate`, `duration_sec`).

### Best Practices

#### Performance

- **Provide `date_time`** when you know it — this narrows the index search and improves response time.
- **Use appropriate `max_depth`** — start with `2`, increase only if needed. AI sessions with inference events typically need `max_depth=4` or `5` to reach the leaf level.
- **Use `expand=none`** if you only need cost rollups, not full records.

#### Querying

- **Start from the root event** — the most complete picture comes from the top-level event.
- **Check metadata first** — `/metadata/{record_type}` shows expected children and recommended depth.
- **Use `links.records`** to get the underlying detail records for deeper analysis.

#### Error Handling

| Status Code | Meaning | Action |
| --- | --- | --- |
| 400 | Invalid parameters | Check `record_type` spelling, `event_id` format |
| 403 | Forbidden | Verify API key has access to this user's data |
| 404 | Event not found | Event may not exist, or `date_time` is incorrect |
| 500 | Internal error | Retry with exponential backoff |

### Record Types Reference

#### AI & Voice Intelligence

| Record Type | Product | Description | Common Children |
| --- | --- | --- | --- |
| `ai-voice-assistant` | AI Voice Assistant | AI assistant sessions | `inference` |
| `inference` | Inference | AI inference events (one per LLM turn) | — |
| `inference-speech-to-text` | Inference | STT-specific inference | — |
| `inference-text-to-speech` | Inference | TTS-specific inference | — |
| `summarization` | Inference | Text summarization | — |
| `embedding` | Inference | Vector embeddings | — |
| `speech-to-text` | Speech-to-Text | STT transcription records | — |
| `text-to-speech` | Text-to-Speech | TTS synthesis records | — |
| `amd` | Answering Machine Detection | AMD invocations | — |
| `noise-suppression` | Noise Suppression | Audio enhancement records | — |

#### Voice & Telephony

| Record Type | Product | Description | Common Children |
| --- | --- | --- | --- |
| `call-session` | N/A | Root-level record for grouping related voice product usage records | `call-control`, `sip-trunking`, `recording`, `webrtc`, `siprec-client`, `fax-api`, `conference-participant` |
| `call-control` | Call Control (Programmable Voice) | Voice API call records | `ai-voice-assistant`, `amd`, `media-streaming`, `speech-to-text`, `text-to-speech`, `noise-suppression` |
| `sip-trunking` | SIP Trunking | SIP trunking detail records | — |
| `webrtc` | WebRTC | WebRTC call records | — |

#### Media & Storage

| Record Type | Product | Description | Common Children |
| --- | --- | --- | --- |
| `recording` | Call Recording | Call recording CDRs | — |
| `media_storage` | Media Storage | Stored media files | — |
| `media-streaming` | Media Streaming | Real-time audio streams | — |
| `forking` | Media Forking | Forked media records | — |

#### Conferencing

| Record Type | Product | Description | Common Children |
| --- | --- | --- | --- |
| `conference` | Conference | Conference sessions | `conference-participant` |
| `conference-participant` | Conference | Individual participant records | — |

#### Messaging

| Record Type | Product | Description | Common Children |
| --- | --- | --- | --- |
| `message` | Messaging | SMS/MMS message records | `ai-messaging-assistant` |

#### Video

| Record Type | Product | Description | Common Children |
| --- | --- | --- | --- |
| `room-session-event` | Programmable Video | Video room sessions | — |
| `room-session-participant-event` | Programmable Video | Video participants | — |
| `room-session-recording-event` | Programmable Video | Video recordings | — |
| `room-session-composition-event` | Programmable Video | Video compositions | — |

#### Other Products

| Record Type | Product | Description | Common Children |
| --- | --- | --- | --- |
| `verify` | Verify (2FA) | Verification attempts | — |
| `fax-api` | Fax API | Fax transmission records | — |
| `branded-calling` | Branded Calling | Caller ID branding | — |
| `siprec-client` | SIPREC | SIPREC recording sessions | — |
| `sim_card_usage` | Wireless | SIM card data usage | — |
| `customer-service-record` | CSR | Customer service records | — |
