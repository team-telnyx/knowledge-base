---
title: Email Webhooks & Events
summary: Telnyx email events flow through three consumption surfaces — recipient-scoped
  webhooks, the Events API for polling, and per-message lookups — covering the full
  lifecycle from queued through delivered, bounced, and engagement signals, plus domain
  lifecycle events. This page documents the event model, webhook payload envelope,
  signature verification, polling endpoints, and how to combine both surfaces in production.
sources:
- url: https://developers.telnyx.com/docs/messaging/email/webhooks-events/index
updated_at: 2026-08-05T13:53:18Z
---

# Email Webhooks & Events

*Part 4 of 5 — see also: [Part 1](email-webhooks-events--part-1.md), [Part 2](email-webhooks-events--part-2.md), [Part 3](email-webhooks-events--part-3.md), [Part 5](email-webhooks-events--part-5.md)*

Telnyx email events flow through three consumption surfaces — recipient-scoped webhooks, the Events API for polling, and per-message lookups — covering the full lifecycle from queued through delivered, bounced, and engagement signals, plus domain lifecycle events. This page documents the event model, webhook payload envelope, signature verification, polling endpoints, and how to combine both surfaces in production.

## Consume via polling

If you don’t have a public HTTPS endpoint — or you want to pull stored outbound message history on demand — use the Events API. Polling is built for agents, batch jobs, on-prem services, and reconciliation of outbound message events after a webhook outage.

The polling model accepts these 16 bare event types: `queued`, `deferred`, `scheduled`, `cancelled`, `sandbox`, `sending`, `sent`, `failed`, `delivered`, `bounced`, `complained`, `rejected`, `opened`, `clicked`, `unsubscribed`, and `daily_limit_exceeded`. Unlike webhook subscriptions, polling includes `sending`, `cancelled`, `rejected`, and `daily_limit_exceeded`, but excludes `received` and every `email_domain.*` event.

`daily_limit_exceeded` is a **scheduled-send admission failure**, not a webhook subscription event. It is persisted when a scheduled send fires and the account’s daily send limit no longer has room for it — the message is rejected at fire time rather than at submission time. It cannot be selected in a webhook `events` allowlist; poll for it or query it via `filter[event_type]=daily_limit_exceeded`.

### List account events

`GET /email_events` returns events for the authenticated account, oldest-first within a time window, with cursor pagination and server-side filtering.

```bash
curl "https://api.telnyx.com/v2/email_events?page_size=50&event_type=delivered,bounced&from=2026-07-01T00:00:00Z" \
  -H "Authorization: Bearer ***"
```

Response (`200`):

```json
{
  "data": [
    {
      "record_type": "email_event",
      "id": "a1b2c3d4-5678-9012-abcd-ef1234567890",
      "type": "delivered",
      "occurred_at": "2026-07-06T18:24:00.000Z",
      "email_id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
      "email": {
        "from": { "email": "sender@example.com", "name": "Telnyx" },
        "to": [{ "email": "recipient@example.com" }],
        "cc": [],
        "subject": "Welcome"
      },
      "payload": { "recipient": "recipient@example.com" }
    }
  ],
  "meta": {
    "page_size": 50,
    "time_range": {
      "from": "2026-07-01T00:00:00Z",
      "to": "2026-07-31T00:00:00Z"
    },
    "page_cursor": "eyJvY2N1cnJlZF9hdCI6IjIwMjYtMDctMDZUMTg6MjQ6MDBaIn0="
  }
}
```

#### Filters

| Parameter | Type | Description |
| --- | --- | --- |
| `page_size` | integer | Page size (default 25, clamped 1–100). |
| `page_cursor` | string | Opaque cursor returned in the previous page’s `meta.page_cursor`. Omit on the first request. |
| `event_type` | string or string[] | Comma-separated list **or** repeated query param. Filters to these event types. Unknown values return no matches. |
| `email_id` | UUID | Filter to events for a single email message. Invalid UUIDs are silently ignored. |
| `from` | ISO 8601 timestamp | Include events at or after this time. |
| `to` | ISO 8601 timestamp | Include events at or before this time. |

The `event_type` filter accepts the **bare event names** (e.g. `delivered`, `bounced`, `opened`) — not the `email.`-prefixed webhook event types. So `event_type=delivered,bounced` filters to delivery and bounce events.

**The message filter parameter is `email_id`, not `message_id`.** Filter a single message’s events with `?email_id=<email-id>`. For compatibility with the Telnyx v2 bracket convention, the service also accepts the legacy alias `filter[message_id]=<email-id>`, which normalizes to `email_id` — but note that `filter[email_id]` is **not** recognized. Unrecognized filter params are silently ignored and return unfiltered results, so a typo looks like a working query that returns everything.

#### Pagination and ordering

Events are ordered by `occurred_at` ascending, then by `id`. Pages are cursor-based: each response includes `meta.page_cursor` when more results are available, and **omits the field entirely** (rather than `null`) when you’ve reached the end of the result set. Pass that cursor as `page_cursor` on the next request.

The response `meta` always includes `time_range` — the resolved `{from, to}` query window, not the timestamps of the first and last returned events. With neither bound, `from` defaults to 30 days ago and `to` is `null`. With only `from`, `to` is capped at 30 days after `from`.

The `email` summary block (`{from, to, cc, subject}`) is present when the underlying message is available for preload, and **omitted** (not `null`) when it isn’t. Don’t rely on it always being present — guard for its absence.

### Per-message event history

To get the event timeline for a single message, use `GET /email_messages/{email_id}/events`. This is scoped to a message you own and returns its events in chronological order.

```bash
curl "https://api.telnyx.com/v2/email_messages/b0c7e8cb-6227-4c74-9f32-c7f80c30934b/events?page_size=50" \
  -H "Authorization: Bearer ***"
```

Response (`200`):

```json
{
  "data": [
    {
      "type": "queued",
      "occurred_at": "2026-07-06T18:20:00.000Z"
    },
    {
      "type": "sent",
      "occurred_at": "2026-07-06T18:20:02.000Z"
    },
    {
      "type": "delivered",
      "occurred_at": "2026-07-06T18:20:05.000Z",
      "payload": { "recipient": "recipient@example.com" }
    }
  ],
  "meta": {
    "page_size": 50
  }
}
```

Returns `404` if the email message doesn’t exist or belongs to another account. The per-message endpoint supports `page_size` and `page_cursor` but **not** the `event_type`/`from`/`to`/`email_id` filters (they don’t apply — you’re already scoped to one message).

### Event statistics

`GET /email_events/stats` returns aggregate counts and derived rates for the authenticated account over a time window.

```bash
curl "https://api.telnyx.com/v2/email_events/stats?from=2026-07-01T00:00:00Z&to=2026-07-07T00:00:00Z" \
  -H "Authorization: Bearer ***"
```

Response (`200`):

```json
{
  "data": {
    "record_type": "email_event_stats",
    "counts": {
      "queued": 12500,
      "sent": 12480,
      "delivered": 12310,
      "deferred": 42,
      "bounced": 128,
      "opened": 7800,
      "clicked": 2100,
      "complained": 4,
      "unsubscribed": 35,
      "failed": 2
    },
    "rates": {
      "delivery_rate": 98.48,
      "bounce_rate": 1.02,
      "deferred_rate": 0.34,
      "open_rate": 63.36,
      "click_rate": 26.92,
      "complaint_rate": 0.03
    },
    "time_range": {
      "from": "2026-07-01T00:00:00Z",
      "to": "2026-07-07T00:00:00Z"
    }
  }
}
```

Stats count **10 event types**: `queued`, `sent`, `delivered`, `deferred`, `bounced`, `opened`, `clicked`, `complained`, `unsubscribed`, and `failed`. Counts and rates are recipient-level: every address in `to`, `cc`, and `bcc` counts separately, while repeated events of the same type for the same message and recipient count once. Partial MTA injection results count successful recipients as `sent` and unsuccessful recipients as `failed`. The Email API rejects duplicate normalized recipient addresses across `to`, `cc`, and `bcc`. Other polling event types (such as `scheduled`, `cancelled`, `sandbox`, `sending`, `rejected`, and `daily_limit_exceeded`) are not included in stats. The rates are percentages:

| Rate | Formula |
| --- | --- |
| `delivery_rate` | `delivered / queued` |
| `bounce_rate` | `bounced / queued` |
| `deferred_rate` | `deferred / queued` |
| `open_rate` | `opened / delivered` |
| `click_rate` | `clicked / opened` |
| `complaint_rate` | `complained / delivered` |

`from` and `to` are optional ISO 8601 timestamps. With neither bound, `from` defaults to 30 days ago and `to` is `null`; the response reports those resolved query bounds.

### Polling patterns

#### Cursor loop (backfill or steady-state tail)

Poll `GET /email_events` with a `from` timestamp, then walk the cursor until `page_cursor` disappears. Because `from` is inclusive, persist the latest `occurred_at` and the event IDs seen at that timestamp. Start the next poll from the same timestamp and deduplicate the boundary events by `id`; using only the timestamp would reprocess them.

```python
import os
import requests

API = "https://api.telnyx.com/v2"
HEADERS = {"Authorization": f"Bearer {os.environ['TELNYX_API_KEY']}"}

def poll_events(
    since_iso,
    boundary_ids=(),
    event_types=("delivered", "bounced", "failed"),
):
    """Return new events and the next inclusive `(timestamp, IDs)` checkpoint."""
    params = {
        "page_size": 100,
        "from": since_iso,
        "event_type": ",".join(event_types),
    }
    boundary_ids = set(boundary_ids)
    events = []
    latest_at = since_iso
    latest_ids = set(boundary_ids)

    while True:
        r = requests.get(f"{API}/email_events", headers=HEADERS, params=params)
        r.raise_for_status()
        body = r.json()
        for event in body["data"]:
            occurred_at = event["occurred_at"]
            event_id = event["id"]

            # `from` is inclusive: skip events already processed at the boundary.
            if occurred_at == since_iso and event_id in boundary_ids:
                continue

            events.append(event)
            if occurred_at > latest_at:
                latest_at = occurred_at
                latest_ids = {event_id}
            elif occurred_at == latest_at:
                latest_ids.add(event_id)

        cursor = body.get("meta", {}).get("page_cursor")
        if not cursor:
            break
        params["page_cursor"] = cursor

    return events, latest_at, latest_ids

# Persist both checkpoint values after processing `events`, then pass them back
# on the next run:
# events, since_iso, boundary_ids = poll_events(since_iso, boundary_ids)
```

#### When to poll vs. webhook

| Use polling when… | Use webhooks when… |
| --- | --- |
| You have no public HTTPS endpoint (agents, on-prem, behind NAT). | You want real-time push with no polling latency. |
| You run a batch job that reconciles state on a schedule. | You need to react to events within seconds. |
| You’re reconciling stored outbound message events after a webhook endpoint was down. | Your endpoint is always reachable and can keep up with volume. |
| You want to inspect historical events without storing every webhook. | You want Telnyx to handle retries and delivery status. |

Use webhooks for real-time reactions and polling to reconcile the overlapping stored outbound message events. Polling does not backfill `email.received` or `email_domain.*` webhooks, and it additionally exposes `sending`, `cancelled`, `rejected`, and `daily_limit_exceeded` message events that cannot be selected in a webhook subscription.
