---
title: Voice AI Assistants
summary: Telnyx Voice AI Assistants let you build, configure, and operate conversational
  voice agents entirely from the Mission Control Portal or via API. This page covers
  the no-code quickstart, supported language and transcription models, voice and noise-suppression
  settings, built-in and library tools, integrations, scheduled outbound events with
  retries, and programmatic voice control.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
updated_at: 2026-08-05T13:45:11Z
---

# Voice AI Assistants

*Part 5 of 6 — see also: [Part 1](voice-ai-assistants--part-1.md), [Part 2](voice-ai-assistants--part-2.md), [Part 3](voice-ai-assistants--part-3.md), [Part 4](voice-ai-assistants--part-4.md), [Part 6](voice-ai-assistants--part-6.md)*

Telnyx Voice AI Assistants let you build, configure, and operate conversational voice agents entirely from the Mission Control Portal or via API. This page covers the no-code quickstart, supported language and transcription models, voice and noise-suppression settings, built-in and library tools, integrations, scheduled outbound events with retries, and programmatic voice control.

## Scheduled Events

Scheduled events let an AI Assistant kick off an outbound interaction at a fixed point in the future — either a phone call or an SMS message to a specific recipient. The platform stores the event, dispatches it at the scheduled time, and reports the outcome through callbacks. For phone calls, you can also configure automatic retries when the recipient does not engage (busy, no-answer, failed, canceled), so the assistant keeps trying without you having to re-create the event.

Typical uses:

- Outbound appointment reminders, follow-ups, and renewal calls.
- After-hours callbacks scheduled by an inbound assistant.
- Automated SMS confirmations queued from a workflow.
- Re-attempting a missed call on a configurable interval until it connects.

### How it works

Each scheduled event flows through a small state machine:

1. **`pending`** — the event has been created and is waiting for its scheduled time.
2. **`in_progress`** — the executor has dispatched the call or SMS to Telnyx.
3. **`completed`** — the recipient was reached (call answered and ended normally, or SMS delivered).
4. **`failed`** — the event could not be completed and no further attempts will be made.

For phone calls, the terminal `CallStatus` returned by Telnyx decides whether the event is treated as a success or a retryable failure:

| `CallStatus` | Treated as |
| --- | --- |
| `completed` | Success |
| `busy` | Retryable client-side outcome |
| `no-answer` | Retryable client-side outcome |
| `failed` | Retryable client-side outcome |
| `canceled` | Retryable client-side outcome |

If retries are configured and budget remains, the event is re-queued with an updated `scheduled_at_fixed_datetime` and returned to `pending`. If the budget is exhausted, the event is marked `failed`.

### Configuring retries for external failures

Two fields on the create-event request control the retry policy for recipient-side outcomes (busy, no-answer, failed, canceled):

| Field | Type | Description |
| --- | --- | --- |
| `max_retries_client_errors` | integer, `0`–`10` | Number of additional dispatches allowed after the initial attempt. `0` (default) disables retries. |
| `retry_interval_secs` | integer, `60`–`86400` | Seconds to wait between attempts. Required whenever `max_retries_client_errors > 0`. |

Retries are **phone-call only**. Setting either field on an SMS event is rejected with a 400.

**Validation rules:**

- `retry_interval_secs` must be in the range `60`–`86400` (1 minute to 24 hours).
- `max_retries_client_errors` must be in the range `0`–`10`.
- If `max_retries_client_errors > 0`, `retry_interval_secs` must also be set.
- `retry_interval_secs` is only meaningful when `max_retries_client_errors > 0` — supplying one without the other returns a 400.
- Both fields must be omitted (or `0` / `null`) for `sms_chat` events.

**How retries are scheduled.** When a phone-call event finishes with a retryable `CallStatus` and budget remains:

- A new `CallAttempt` record is appended to the event's `call_attempts` array.
- `scheduled_at_fixed_datetime` is advanced to **now + `retry_interval_secs`** (not the original time + interval — the clock starts when the previous attempt's terminal status is received).
- `status` returns to `pending` and the executor will pick the event up again on its next sweep.

When the budget is exhausted, the final attempt is recorded, `status` becomes `failed`, and an `errors` entry explains that the client-error retry budget was exhausted.

**Total attempts.** `max_retries_client_errors` counts retries **on top of** the initial dispatch:

- `max_retries_client_errors: 0` → 1 total attempt (no retries).
- `max_retries_client_errors: 3` → up to 4 total attempts.
- `max_retries_client_errors: 10` → up to 11 total attempts.

### Inspecting attempt history

Each phone-call event exposes a `call_attempts` array containing one entry per terminal dispatch:

```
{
  "scheduled_event_id": "8f3c…",
  "telnyx_conversation_channel": "phone_call",
  "status": "pending",
  "max_retries_client_errors": 3,
  "retry_interval_secs": 300,
  "call_attempts": [
    {
      "attempt_number": 1,
      "attempted_at": "2026-05-07T14:30:02.812Z",
      "call_status": "no-answer",
      "call_duration": null,
      "telnyx_call_control_id": "v3:abc…"
    },
    {
      "attempt_number": 2,
      "attempted_at": "2026-05-07T14:35:08.114Z",
      "call_status": "busy",
      "call_duration": null,
      "telnyx_call_control_id": "v3:def…"
    }
  ]
}
```

The audit trail stays on a single row across the entire retry sequence — you do not need to query multiple events to reconstruct what happened.

### API reference

All endpoints are scoped to a specific assistant.

| Method | Path | Purpose |
| --- | --- | --- |
| `POST` | `/v2/ai/assistants/{assistant_id}/scheduled_events` | Create a scheduled event |
| `GET` | `/v2/ai/assistants/{assistant_id}/scheduled_events` | List scheduled events (paginated, filterable) |
| `GET` | `/v2/ai/assistants/{assistant_id}/scheduled_events/{event_id}` | Fetch a single event |
| `DELETE` | `/v2/ai/assistants/{assistant_id}/scheduled_events/{event_id}` | Cancel a scheduled event |

**Create-event fields:**

| Field | Required | Channels | Description |
| --- | --- | --- | --- |
| `telnyx_conversation_channel` | Yes | both | `phone_call` or `sms_chat`. |
| `telnyx_end_user_target` | Yes | both | The recipient (phone number, E.164 or SIP URI). |
| `telnyx_agent_target` | Yes | both | The number the assistant calls or sends from. |
| `scheduled_at_fixed_datetime` | Yes | both | ISO-8601 timestamp; must be in the future. |
| `text` | Yes for SMS | `sms_chat` | The message body. |
| `conversation_metadata` | No | both | Free-form key/value metadata attached to the resulting conversation. |
| `dynamic_variables` | No | both | Variables passed to the assistant for prompt interpolation. |
| `max_retries_client_errors` | No | `phone_call` | Retry budget for recipient-side outcomes. |
| `retry_interval_secs` | No | `phone_call` | Seconds between retries. |

### Examples

**Schedule a phone call with retries on busy / no-answer.** This event will be tried up to four times total (initial + 3 retries), with a five-minute gap between attempts:

```
curl -L 'https://api.telnyx.com/v2/ai/assistants/{assistant_id}/scheduled_events' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer <TOKEN>' \
  --data-raw '{
    "telnyx_conversation_channel": "phone_call",
    "telnyx_end_user_target": "+15551234567",
    "telnyx_agent_target": "+15553456789",
    "scheduled_at_fixed_datetime": "2026-05-08T15:00:00Z",
    "max_retries_client_errors": 3,
    "retry_interval_secs": 300,
    "conversation_metadata": {
      "campaign": "renewal-q2",
      "customer_id": "cust_42"
    }
  }'
```

**Schedule a phone call without retries.** Omit the retry fields (or set `max_retries_client_errors` to `0`) for a single-attempt call:

```
curl -L 'https://api.telnyx.com/v2/ai/assistants/{assistant_id}/scheduled_events' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer <TOKEN>' \
  --data-raw '{
    "telnyx_conversation_channel": "phone_call",
    "telnyx_end_user_target": "+15551234567",
    "telnyx_agent_target": "+15553456789",
    "scheduled_at_fixed_datetime": "2026-05-08T15:00:00Z"
  }'
```

**Schedule an SMS.** Retry fields do not apply to SMS events:

```
curl -L 'https://api.telnyx.com/v2/ai/assistants/{assistant_id}/scheduled_events' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer <TOKEN>' \
  --data-raw '{
    "telnyx_conversation_channel": "sms_chat",
    "telnyx_end_user_target": "+15551234567",
    "telnyx_agent_target": "+15553456789",
    "scheduled_at_fixed_datetime": "2026-05-08T15:00:00Z",
    "text": "Hi! This is a reminder about your appointment tomorrow at 10 AM."
  }'
```

**Inspect retry history:**

```
curl -L 'https://api.telnyx.com/v2/ai/assistants/{assistant_id}/scheduled_events/{event_id}' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer <TOKEN>'
```

The response includes `status`, `call_attempts`, and (once retries finish) the final `call_status` and `errors` array.

**Cancel a pending event.** Deleting a `pending` event prevents any further dispatches. Deletion has no effect on attempts that have already completed:

```
curl -X DELETE 'https://api.telnyx.com/v2/ai/assistants/{assistant_id}/scheduled_events/{event_id}' \
  -H 'Authorization: Bearer <TOKEN>'
```

### Choosing a retry policy

A few rules of thumb when picking values:

- **Short intervals (60–300s)** suit time-sensitive flows where the recipient is likely to be near their phone — verification calls, urgent reminders. They burn the retry budget quickly, which is sometimes what you want.
- **Medium intervals (5–30 minutes)** are a good default for outreach campaigns. Long enough that a busy recipient may finish their previous call; short enough that the event still completes within an hour.
- **Long intervals (1–24 hours)** match daily-cadence flows: missed bill reminders, callback queues, abandoned-cart nudges.
- **Total reach time** = `max_retries_client_errors × retry_interval_secs`. Make sure that span fits inside the time window when calling is acceptable for your use case (and your jurisdiction's calling-hour rules).
- **Higher `max_retries_client_errors` is not always better** — at some point the recipient is unlikely to answer regardless of how many times you try. Three to five retries is usually plenty.
