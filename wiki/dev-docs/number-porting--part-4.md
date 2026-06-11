---
title: Number Porting
summary: Number porting at Telnyx covers both port-in orders (transferring phone numbers
  to Telnyx from another carrier) and port-out orders (when another carrier requests
  numbers away from your Telnyx account). The port-in process involves checking portability,
  creating and fulfilling orders, managing FOC dates, and optionally configuring messaging,
  bundles, extensions, and blocks. Port-out orders are initiated externally and require
  you to authorize or reject them. Both flows support webhook notifications and a
  queryable event history.
sources:
- url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started/index
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
- url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
updated_at: 2026-06-11T10:40:42Z
---

# Number Porting

*Part 4 of 4 — see also: [Part 1](number-porting--part-1.md), [Part 2](number-porting--part-2.md), [Part 3](number-porting--part-3.md)*

Number porting at Telnyx covers both port-in orders (transferring phone numbers to Telnyx from another carrier) and port-out orders (when another carrier requests numbers away from your Telnyx account). The port-in process involves checking portability, creating and fulfilling orders, managing FOC dates, and optionally configuring messaging, bundles, extensions, and blocks. Port-out orders are initiated externally and require you to authorize or reject them. Both flows support webhook notifications and a queryable event history.

## Port-Out Orders

A port-out order is created when another carrier requests to transfer phone numbers away from your Telnyx account. Telnyx automatically creates the order in your account, and you can authorize or reject it.

Port-out orders require a response within 24–48 hours. If you do not respond, the port-out is automatically authorized and proceeds on the FOC date.

### Port-out order statuses

| Status | Description |
|---|---|
| `pending` | Request received; awaiting your review. |
| `authorized` | You approved the request; numbers will port on the FOC date. |
| `rejected-pending` | You submitted a rejection; Porting Ops is reviewing the reason. |
| `rejected` | Request formally rejected; will not proceed. |
| `canceled` | Request canceled by the gaining carrier or Telnyx. |
| `ported` | Numbers successfully ported to the gaining carrier. |

### Reviewing and responding

1. **Review** – Use `GET /v2/portouts` to list orders, or `GET /v2/portouts/{id}` for a specific order. Check `phone_numbers`, `carrier_name`, `requested_foc_date`, and subscriber information.
2. **Authorize** – Use `PATCH /v2/portouts/{id}/authorized` to approve the port-out.
3. **Reject** – First, retrieve eligible rejection codes with `GET /v2/portouts/rejections/{portout_id}`. Then use `PATCH /v2/portouts/{id}/rejected-pending` with the appropriate `rejection_code`. If using code `1001` ("Other"), you must include a `reason` field. The Porting Ops team validates the reason; if invalid, the order returns to `pending`.

### FOC date changes for port-outs

The gaining carrier is allotted a 10-day grace period, meaning they can port the number at any point between the listed FOC date and the following 10 days. Most port-outs occur on the listed FOC date, but there is no guarantee.

## Port-Out Notifications and Events

Port-out notifications can be sent via email or webhook for status changes and new comments.

### Setting up port-out notifications

1. Sign in to the [Telnyx Portal](https://portal.telnyx.com/).
2. Go to **Account Settings → Advanced Features → [Notifications](https://portal.telnyx.com/#/app/advanced-features/notifications)**.
3. Create a **New Profile**.
4. Add **New Channel(s)** for email or webhook URLs.
5. Add a **New Setting**, select **Port Out Notifications**, and choose the profile and channel.

### Port-out event types

| Event type | Description |
|---|---|
| `portout.status_changed` | The port-out order transitioned to a new status. |
| `portout.new_comment` | A new comment was added to the port-out order. |
| `portout.foc_date_changed` | The FOC date for the port-out was updated. |

### Querying and republishing port-out events

- **List events** – `GET /v2/portout/events` with optional filters by `portout_id`, event type, or date range.
- **Republish** – `POST /v2/portout/events/{id}/republish` resends notifications to currently subscribed channels without creating a new event.
