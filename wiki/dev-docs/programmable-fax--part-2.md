---
title: Programmable Fax
summary: Telnyx Programmable Fax provides HTTP API endpoints for sending, receiving,
  and managing faxes. This page covers account setup, sending and receiving faxes
  via the API, webhook handling, and an email-to-fax tutorial.
sources:
- url: https://developers.telnyx.com/docs/programmable-fax/email-to-fax
- url: https://developers.telnyx.com/docs/programmable-fax/get-started/index
- url: https://developers.telnyx.com/docs/programmable-fax/quickstart
- url: https://developers.telnyx.com/docs/programmable-fax/receive-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/receiving-webhooks
- url: https://developers.telnyx.com/docs/programmable-fax/send-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/sending-commands
updated_at: 2026-08-05T14:01:02Z
---

# Programmable Fax

*Part 2 of 3 — see also: [Part 1](programmable-fax--part-1.md), [Part 3](programmable-fax--part-3.md)*

Telnyx Programmable Fax provides HTTP API endpoints for sending, receiving, and managing faxes. This page covers account setup, sending and receiving faxes via the API, webhook handling, and an email-to-fax tutorial.

## Webhooks

When you send a Programmable Fax command and receive a successful response (HTTP 200 OK), you can expect to receive a webhook. The webhook is delivered to the primary URL specified on the Application associated with the call. If that URL does not resolve, or your application returns a non-200 OK response, the webhook is delivered to the failover URL, if one is specified.

To minimize webhook delivery time, Telnyx:

- does not enforce the order in which webhooks are delivered
- retries webhook delivery if your application does not respond within a certain time threshold

As a result, you may encounter out-of-order, simultaneous, or duplicate webhooks. Duplicate webhooks may cause your application to issue duplicate commands. You can instruct Telnyx to ignore duplicate commands by sending a `command_id` parameter as part of your commands. Commands with duplicate `command_ids` within 60 seconds will be ignored.

### Outbound fax webhooks

| Command | Associated webhooks |
| --- | --- |
| Send a fax | `fax.queued`, `fax.media.processed`, `fax.sending.started`, `fax.delivered`, `fax.failed` |

### Webhook payload fields

| Field | Description |
| --- | --- |
| `record_type` | Description of the record. |
| `id` | Unique id for the webhook. |
| `event_type` | The type of event. |
| `occurred_at` | ISO-8601 datetime of when the event occurred. |
| `to` | Destination number or SIP URI of the call. |
| `from` | Number or SIP URI placing the call. |
| `fax_id` | Unique ID for the Programmable Fax. |
| `client_state` | Configurable state to track commands. |
| `status` | Can be one of `queued`, `media.processed`, `sending.started`, `delivered`, `failed`. |

### Example: fax queued

```json
{
  "data": {
    "event_type": "fax.queued",
    "id": "3691d047-d22a-424d-80ed-fe871981aa6d",
    "occurred_at": "2020-04-22T19:32:12.538002Z",
    "record_type": "event",
    "payload": {
      "call_duration_secs": 50,
      "connection_id": "7267xxxxxxxxxxxxxx",
      "direction": "outbound",
      "fax_id": "b679398e-8b4c-46bd-8630-6797f1ab5228",
      "from": "+35319605860",
      "original_media_url": "https://www.telnyx.com/telnyx-fax/1.pdf",
      "partial_content": true,
      "status": "queued",
      "to": "+13129457420",
      "user_id": "a5b1dfa3-fd2e-4e02-8ea4-xxxxxxxxxxxx"
    }
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "http://example.com/webhooks"
  }
}
```

### Example: fax delivered

```json
{
  "event_type": "fax.delivered",
  "id": "3320554f-6b74-4138-a74b-a1e2ec7eaf8b",
  "occurred_at": "2022-01-07T10:01:43.677850Z",
  "payload": {
    "call_duration_secs": 79,
    "connection_id": "1232154810234",
    "direction": "outbound",
    "fax_id": "c62be5bc-9b13-4b6c-abda-34dd8b541287",
    "from": "+19459457421",
    "original_media_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    "page_count": 1,
    "status": "delivered",
    "to": "+13129457420",
    "user_id": "bdaa1f9f-1018-4156-867d-6c4ac9f556eb"
  }
}
```

### Example: fax failed

```json
{
  "event_type": "fax.failed",
  "id": "d906ecda-db21-428e-9ca0-74dae7e7c144",
  "occurred_at": "2022-01-05T22:23:46.888808Z",
  "payload": {
    "connection_id": "1232154810234",
    "direction": "outbound",
    "failure_reason": "user_busy",
    "fax_id": "f7b303ed-674c-4962-951b-848380510893",
    "from": "+19459457421",
    "original_media_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    "status": "failed",
    "to": "+13129457420",
    "user_id": "417b0cc2-39e0-4ab9-b116-e56543649aa9"
  }
}
```

### Possible failure reasons

Inspect the `failure_reason` field in the webhook payload to debug failed deliveries. Possible values include:

- `account_disabled`
- `connection_channel_limit_exceeded`
- `destination_invalid`
- `destination_not_in_countries_whitelist`
- `destination_not_in_service_plan`
- `destination_unreachable`
- `fax_initial_communication_timeout`
- `fax_signaling_error`
- `invalid_ecm_response_from_receiver`
- `no_outbound_profile`
- `outbound_profile_channel_limit_exceeded`
- `outbound_profile_daily_spend_limit_exceeded`
- `receiver_call_dropped`
- `receiver_communication_error`
- `receiver_decline`
- `receiver_incompatible_destination`
- `receiver_invalid_number_format`
- `receiver_no_answer`
- `receiver_no_response`
- `receiver_recovery_on_timer_expire`
- `receiver_unallocated_number`
- `service_unavailable`
- `unverified_destination_not_allowed`
- `unverified_origination_number`
- `user_busy`
- `user_channel_limit_exceeded`
