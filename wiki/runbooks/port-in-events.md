---
title: Port-in events
summary: View events for your port-in orders and republish notifications for specific events.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/port-in-events/index
    content_hash: 78fc26eedb535e03057cb8d28252047aec08c00c71998c5c2d4e3bb5114e3042
updated_at: 2026-04-10T00:00:00Z
---

# Port-in events

View events for your port-in orders and republish notifications for specific events

## Overview

Port-in events provide a detailed record of everything that happens during the port-in process. Each time a status changes, a comment is added, or an order is split, the system creates an event that you can query and track.

This differs from [port-in notifications](https://developers.telnyx.com/docs/numbers/porting/port-in-notifications), which push updates to your webhook or email as they occur. The Events API gives you on-demand access to view your complete event history and republish notifications for specific events if needed.

With the Port-in Events API, you can:

* View all events across your port-in orders.
* Filter events by port-in order, event type, or date range.
* Republish notifications for specific events to your configured webhook or email.

## Event types

The following event types are generated during the port-in lifecycle:

| Event type                        | Description                                                    |
| :-------------------------------- | :------------------------------------------------------------- |
| `porting_order.status_changed`    | The port-in order transitioned to a new status.                |
| `porting_order.new_comment`       | A new comment was added to the port-in order.                  |
| `porting_order.split`             | One or more phone numbers were split into a separate order.    |
| `porting_order.messaging_changed` | The messaging activation status changed for the port-in order. |
| `porting_order.deleted`           | A draft port-in order was deleted.                             |

## How it works

### Step 1: List port-in events

Use the [GET /v2/porting/events endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-events) to retrieve a list of events for your port-in orders.

You can filter results by `porting_order_id` to view events for a specific order, or retrieve all events across your account with pagination support.

### Step 2: Republish event notifications

If you need to resend notifications for a specific event, use the [POST /v2/porting/events//republish endpoint](https://developers.telnyx.com/api-reference/porting-orders/republish-a-porting-event) where `{id}` is the event ID.

This endpoint republishes notifications only to channels you are currently subscribed to. To configure your notification settings, see [how to set up port-in notifications](https://developers.telnyx.com/docs/numbers/porting/port-in-notifications#how-to-setup-notifications-via-the-portal-for-all-port-orders-email-and-webhook).

Republishing an event resends the notifications but does not create a new event in the system. Email notifications may take a few minutes to be delivered.


## Related Pages

- [Port-out events](../runbooks/port-out-events.md)
- [Port-in requirements](../runbooks/port-in-requirements.md)
- [Port-in blocks](../runbooks/port-in-blocks.md)
- [Room and Events](../runbooks/room-and-events.md)
