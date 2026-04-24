---
title: Port-out events
summary: View events for your port-out orders and republish notifications for specific events.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/port-out-events/index
    content_hash: 4d938676fcdec349984a4515a2af04d9e5d9155d38c997783f8fc2ac314a0621
updated_at: 2026-04-10T00:00:00Z
---

# Port-out events

View events for your port-out orders and republish notifications for specific events

## Overview

Port-out events provide a detailed record of everything that happens during the port-out process. Each time a status changes, a comment is added, or a FOC date is updated, the system creates an event that you can query and track.

This differs from [port-out notifications](https://developers.telnyx.com/docs/numbers/porting/port-out-notifications), which push updates to your webhook or email as they occur. The Events API gives you on-demand access to view your complete event history and republish notifications for specific events if needed.

With the Port-out Events API, you can:

* View all events across your port-out orders.
* Filter events by port-out order, event type, or date range.
* Republish notifications for specific events to your configured webhook or email.

## Event types

The following event types are generated during the port-out lifecycle:

| Event type                 | Description                                                        |
| :------------------------- | :----------------------------------------------------------------- |
| `portout.status_changed`   | The port-out order transitioned to a new status.                   |
| `portout.new_comment`      | A new comment was added to the port-out order.                     |
| `portout.foc_date_changed` | The FOC (Firm Order Commitment) date for the port-out was updated. |

## How it works

### Step 1: List port-out events

Use the [GET /v2/portout/events endpoint](https://developers.telnyx.com/api-reference/number-portout/list-all-port-out-events) to retrieve a list of events for your port-out orders.

You can filter results by `portout_id` to view events for a specific order, or retrieve all events across your account with pagination support.

### Step 2: Republish event notifications

If you need to resend notifications for a specific event, use the [POST /v2/portout/events//republish endpoint](https://developers.telnyx.com/api-reference/number-portout/republish-a-port-out-event) where `{id}` is the event ID.

This endpoint republishes notifications only to channels you are currently subscribed to. To configure your notification settings, see [how to set up port-out notifications](https://developers.telnyx.com/docs/numbers/porting/port-out-notifications#how-to-set-up-port-out-notifications).

Republishing an event resends the notifications but does not create a new event in the system. Email notifications may take a few minutes to be delivered.


## Related Pages

- [Port-in events](../runbooks/port-in-events.md)
- [Port-out orders](../tutorial/port-out-orders.md)
- [Port-Out Order Notifications](../runbooks/port-out-order-notifications.md)
- [Room and Events](../runbooks/room-and-events.md)
