---
title: Telnyx Developer Documentation
summary: A comprehensive guide to Telnyx's Programmable Fax, Reporting & Analytics,
  and Speech & Voice APIs, covering setup, sending and receiving faxes, webhook handling,
  usage reporting, session analysis, and real-time speech-to-text and text-to-speech
  streaming.
sources:
- url: https://developers.telnyx.com/docs/programmable-fax/email-to-fax
  content_hash: ae956e35cbe778faa550865d178aa512a687347422967b41e7a73b0c9364af92
- url: https://developers.telnyx.com/docs/programmable-fax/get-started/index
  content_hash: a575ae8f265f3ea2e617b542b7d6487bd8d9e4fcdd3734795432d746dbe75d8e
- url: https://developers.telnyx.com/docs/programmable-fax/quickstart
  content_hash: 162c427173df6aab8cad1d63cf53c10a31f6363d5d1fbebeacca092f99fc7373
- url: https://developers.telnyx.com/docs/programmable-fax/receive-a-fax-api
  content_hash: 1d8b685093cd16efa0df2c2b2e385296e0f3d36e3b4882cb3fcdf6ff32f1e650
- url: https://developers.telnyx.com/docs/programmable-fax/receiving-webhooks
  content_hash: b65b3f5a519156817aea525848b57f52f9bd40558645bc87356a2db202636f5d
- url: https://developers.telnyx.com/docs/programmable-fax/send-a-fax-api
  content_hash: 702c037dc0af510343f0f7d960dbfe368fd785fcd4614ce295bdbead03eb7ffa
- url: https://developers.telnyx.com/docs/programmable-fax/sending-commands
  content_hash: 8d55fb8cfe9dbe0694a68e6c21128c0e3663ee3e7309b8ce11dbd8a3a826a0f0
- url: https://developers.telnyx.com/docs/reporting/on-demand-reports/index
  content_hash: be2475e7633ad6e93e0105757b0ba6bcbeb2aecd6ab7127b68b72e7c712e033c
- url: https://developers.telnyx.com/docs/reporting/session-analysis
  content_hash: 9b537f31fe03cdc4d041a4cefb01f6e0303673dce26f78e980f1db54968ecbc3
- url: https://developers.telnyx.com/docs/reporting/usage-reports/index
  content_hash: 619f12548c152b55f58f96ad18d8e5acb022679092f6c18fdafce89186634ec5
- url: https://developers.telnyx.com/docs/tts-stt/stt-websocket-streaming
  content_hash: 851082b5bb21f1fe0454bd5c236783faacdf44d9c11ef0acf1480ca44031b23d
- url: https://developers.telnyx.com/docs/tts-stt/telnyx-ultra-voices
  content_hash: fc89baa71369839911ad9530a0315313e420d08b9a7e755a10b769c9f3476f83
- url: https://developers.telnyx.com/docs/tts-stt/tts-available-voices
  content_hash: 1380d4c10aa72181d69b6705a81bac26fa1fc424afec460b7874613db55feeff
- url: https://developers.telnyx.com/docs/tts-stt/tts-websocket-streaming
  content_hash: a3493cabf711a0cf0d546df8a0b3c75ecee91a0755f3869d522a1e0e217c6586
updated_at: 2026-06-11T10:41:11Z
---

# Telnyx Developer Documentation

*Part 2 of 3 — see also: [Part 1](telnyx-developer-documentation--part-1.md), [Part 3](telnyx-developer-documentation--part-3.md)*

A comprehensive guide to Telnyx's Programmable Fax, Reporting & Analytics, and Speech & Voice APIs, covering setup, sending and receiving faxes, webhook handling, usage reporting, session analysis, and real-time speech-to-text and text-to-speech streaming.

## Reporting and Analytics

### Usage Reports API

The v2 Usage Reports API provides a single endpoint for aggregated usage data across all Telnyx products. It supports JSON (default) and CSV (`format=csv`) output.

#### Supported Products

sip-trunking, messaging, call-control, wireless, cloud-storage, inference, verify-2fa, fax-api, webrtc, cps, conference, programmable-video, call-control-features, customer-service-record, media-streaming, noise-suppression, text-to-speech, speech-to-text, recording, forking, media-storage, amd

#### Query Requirements

- **Product** (required): One product per query; you cannot query multiple products at once.
- **Dates**: Format as `YYYY-MM-DDThh:mm:ssTZD` (e.g. `2022-12-24T19:20:30-05:00`). `start_date` is inclusive; `end_date` is exclusive. Maximum range is 31 days. Alternatively, use `date_range` with date literals (e.g. `date_range=last_1_weeks`, `date_range=today`).
- **Dimensions**: How to break out data (e.g. `direction`, `country_code`, `connection_id`). Include any field you filter on as a dimension.
- **Metrics**: Values to report (e.g. `cost`, `connected`, `attempted`, `count`, `parts`).

#### Discovering Dimensions and Metrics

Query the options endpoint to see available dimensions and metrics per product:

```bash
curl "https://api.telnyx.com/v2/usage_reports/options?product=sip-trunking" \
  --header "Authorization: Bearer YOUR_API_KEY"
```

#### Example Queries

**SIP Trunking — outbound calls by country:**

```bash
curl -g "https://api.telnyx.com/v2/usage_reports?product=sip-trunking&start_date=2024-01-23T00:00:00-00:00&end_date=2024-01-29T00:00:00-00:00&metrics=connected,attempted,cost&dimensions=direction,country_code&filter[direction]=outbound" \
  --header "Authorization: Bearer YOUR_API_KEY"
```

**Messaging — today's outbound messages by carrier:**

```bash
curl -g "https://api.telnyx.com/v2/usage_reports?product=messaging&dimensions=direction,normalized_carrier&metrics=cost,parts,count&date_range=today&filter[direction]=outbound" \
  --header "Authorization: Bearer YOUR_API_KEY"
```

**Short-duration call analysis** (relevant for Telnyx's automatic surcharge on accounts where ≤6-second calls exceed 15% of outbound traffic):

```bash
curl -g "https://api.telnyx.com/v2/usage_reports?product=sip-trunking&start_date=2024-01-01T00:00:00-00:00&end_date=2024-02-01T00:00:00-00:00&metrics=completed&dimensions=direction,short_duration_call&filter[direction]=outbound" \
  --header "Authorization: Bearer YOUR_API_KEY"
```

### On-Demand Reports

On-Demand Reports lets you query your Telnyx usage data using natural language instead of building filters manually. The system translates your description into structured queries against your Usage Report data.

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Navigate to **Reporting → [On-Demand Reports](https://portal.telnyx.com/#/reporting/on-demand-reports)**.
3. Type a query describing the report you need.

**Example queries:**

- "Daily wireless spend for the last 10 days"
- "Number of messages by direction for last week as a pie chart"
- "Weekly total calls last quarter"
- "Average SIP cost for last 2 weeks as line graph"

You can specify chart types (bar, pie, line, table), date ranges (relative or absolute), and groupings (direction, product, day, week, etc.). On-Demand Reports queries run against v2 Usage Report data only and is not a general knowledge assistant.

### Session Analysis

Session Analysis provides a complete view of costs and events for any usage session on the Telnyx platform — especially valuable for AI-powered sessions where a single call can involve multiple products (AI Voice Assistant, inference, speech-to-text, text-to-speech, call control, SIP trunking, etc.).

#### Core Concepts

- **Record Type**: Identifies the category of usage event for a product (e.g. `ai-voice-assistant`, `call-control`, `inference`).
- **Session**: A tree of related usage events. The **root event** is the primary event; **child events** are related usage underneath.
- **Relationships**: Events connect via `child_of` or `parent_of` relationships, defined by field mappings (e.g. `conversation_id`, `telnyx_session_id`).
- **Cost Rollup**: Each node has `event_cost` (individual) and `cumulative_cost` (this event + all descendants). The root's `cumulative_cost` equals the total session cost.

#### Endpoints

**List all record types:**

```
GET /v2/session_analysis/metadata
```

**Get record type details:**

```
GET /v2/session_analysis/metadata/{record_type}
```

**Get session analysis:**

```
GET /v2/session_analysis/{record_type}/{event_id}
```

Query parameters for the analysis endpoint:

| Parameter | Type | Default | Description |
|---|---|---|---|
| `include_children` | boolean | `true` | Include child events |
| `max_depth` | integer | `2` | Maximum traversal depth (1–5) |
| `expand` | string | `record` | `record` (full data) or `none` (structure only) |
| `date_time` | ISO 8601 | — | Timestamp to narrow index selection (improves performance) |

For AI sessions, use `call-session` as the starting record type with `max_depth=4` or `5` to reach leaf-level inference events.

#### Response Structure

Top-level:

| Field | Description |
|---|---|
| `session_id` | Session identifier |
| `cost.total` | Total session cost |
| `cost.currency` | ISO 4217 currency code |
| `root` | Root event node (tree structure) |
| `meta.event_count` | Total events in the tree |
| `meta.products` | Unique products involved |

Each event node includes:

| Field | Description |
|---|---|
| `id` | Event identifier |
| `product` | Internal product identifier |
| `event_name` | Event type name |
| `relationship` | How this event relates to its parent (null for root) |
| `cost.event_cost` | Individual event cost |
| `cost.cumulative_cost` | This event + all descendants |
| `links.self` | Link to this analysis node |
| `links.records` | Link to underlying detail records |
| `record` | Full detail record data |
| `children` | Child event nodes |

#### Example AI Session Tree

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

#### Best Practices

- Provide `date_time` to narrow the index and improve response time.
- Start with `max_depth=2`; increase to 4–5 for AI sessions with inference events.
- Use `expand=none` if you only need cost rollups.
- Start from the root event for the most complete picture.
- Check metadata first to understand expected children and recommended depth.

#### Key Record Types

| Category | Record Types |
|---|---|
| **AI & Voice Intelligence** | `ai-voice-assistant`, `inference`, `inference-speech-to-text`, `inference-text-to-speech`, `summarization`, `embedding`, `speech-to-text`, `text-to-speech`, `amd`, `noise-suppression` |
| **Voice & Telephony** | `call-session`, `call-control`, `sip-trunking`, `webrtc` |
| **Media & Storage** | `recording`, `media_storage`, `media-streaming`, `forking` |
| **Conferencing** | `conference`, `conference-participant` |
| **Messaging** | `message` (child: `ai-messaging-assistant`) |
| **Video** | `room-session-event`, `room-session-participant-event`, `room-session-recording-event`, `room-session-composition-event` |
| **Other** | `verify`, `fax-api`, `branded-calling`, `siprec-client`, `sim_card_usage`, `customer-service-record` |

---
