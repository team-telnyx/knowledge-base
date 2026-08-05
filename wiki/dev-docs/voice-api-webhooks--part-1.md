---
title: Voice API Webhooks
summary: Voice API webhooks are HTTP callbacks that notify your application in real
  time when events occur during a call. Each event delivers a JSON payload to a configured
  URL, and your application can respond with call control commands to drive the call
  flow.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks
updated_at: 2026-08-05T14:04:53Z
---

# Voice API Webhooks

*Part 1 of 2 — see also: [Part 2](voice-api-webhooks--part-2.md)*

Voice API webhooks are HTTP callbacks that notify your application in real time when events occur during a call. Each event delivers a JSON payload to a configured URL, and your application can respond with call control commands to drive the call flow.

## Overview

Voice API webhooks are HTTP callbacks that notify your application in real time when events occur during a call — a call is initiated, audio playback finishes, a recording is saved, and so on. Your application receives a JSON payload for each event and can respond with call control commands to drive the call flow.

## Webhook delivery

When an event occurs on a call, Telnyx delivers the webhook to your configured URL. If the primary URL fails, the webhook is sent to the failover URL (if configured).

For details on retry logic, signature verification, and general webhook behavior, see [Webhook Fundamentals](webhook-fundamentals.md).

## Configuration

Webhooks can be configured at three levels:

1. **Connection webhook config** — default webhook URL and settings tied to a [Voice API connection](https://portal.telnyx.com/#/app/connections) in Mission Control.
2. **Custom webhook config** — per-command overrides. Pass `webhook_url` and `webhook_url_method` in any call control command to route that command's webhooks to a different endpoint.
3. **Events webhook config** — advanced configuration that routes specific event types to different URLs.

You can also manage webhook settings programmatically via the [Call Control Applications API](call-control-applications-api.md). Use [Create](https://developers.telnyx.com/api-reference/call-control-applications/create-a-call-control-application) or [Update](https://developers.telnyx.com/api-reference/call-control-applications/update-a-call-control-application) to set webhook URLs, failover URLs, API version, and timeout values on a connection.

### Configuration parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `webhook_event_url` | String | Primary destination for webhook delivery |
| `webhook_event_failover_url` | String | Secondary URL used when the primary fails |
| `webhook_api_version` | String | Webhook format version (`"1"` or `"2"`) |
| `webhook_timeout_secs` | Integer | Seconds to wait before timing out (0–30, default: null) |

## HTTP methods and headers

### Methods

Webhooks use the `POST` method by default. Pass `webhook_url_method` as `GET` in a call control command to receive that command's webhook payloads as URL query parameters instead of a JSON body.

### Headers

Every webhook request includes:

| Header | Description |
| --- | --- |
| `Content-Type` | `application/json` (POST requests) |
| `User-Agent` | `telnyx-webhooks` |
| `Telnyx-Signature-Ed25519` | ED25519 signature for [verification](https://developers.telnyx.com/development/api-fundamentals/webhooks/receiving-webhooks#webhook-signing) |
| `Telnyx-Timestamp` | Unix timestamp when the webhook was generated |

## Webhook payload structure

All Voice API webhooks share a common envelope. Below is an example `call.initiated` payload:

```json
{
  "data": {
    "record_type": "event",
    "event_type": "call.initiated",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "occurred_at": "2018-02-02T22:25:27.521992Z",
    "payload": {
      "call_control_id": "d14dbcee-880b-11eb-8204-02420a0f7568",
      "connection_id": "7267xxxxxxxxxxxxxx",
      "call_leg_id": "d14dbcee-880b-11eb-8204-02420a0f7568",
      "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
      "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
      "from": "+12025550133",
      "to": "+12025550131",
      "direction": "incoming",
      "state": "parked"
    }
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

### Common fields

| Field | Location | Description |
| --- | --- | --- |
| `record_type` | `data` | Always `"event"` |
| `event_type` | `data` | Event name (see Event types below) |
| `id` | `data` | Unique identifier for this webhook event |
| `occurred_at` | `data` | ISO 8601 timestamp of when the event occurred |
| `call_control_id` | `data.payload` | ID used to issue call control commands for this call leg |
| `call_leg_id` | `data.payload` | Unique ID for this call leg — use to correlate webhooks |
| `call_session_id` | `data.payload` | Shared ID across related call legs (e.g., both sides of a transfer) |
| `connection_id` | `data.payload` | Voice API connection used for the call |
| `client_state` | `data.payload` | Base64-encoded state passed through from a previous command |
| `from` | `data.payload` | Calling party number or SIP URI |
| `to` | `data.payload` | Called party number or SIP URI |
| `attempt` | `meta` | Delivery attempt number (increments on retries) |
| `delivered_to` | `meta` | URL the webhook was sent to |
