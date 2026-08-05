---
title: Porting orders
summary: A consolidated guide to Telnyx porting workflows, covering port-in requirements
  and additional steps for inbound ports, plus port-out order management, notifications,
  and event tracking for numbers leaving your account.
sources:
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
- url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
updated_at: 2026-08-05T14:00:54Z
---

# Porting orders

*Part 4 of 4 — see also: [Part 1](porting-orders--part-1.md), [Part 2](porting-orders--part-2.md), [Part 3](porting-orders--part-3.md)*

A consolidated guide to Telnyx porting workflows, covering port-in requirements and additional steps for inbound ports, plus port-out order management, notifications, and event tracking for numbers leaving your account.

## Port-out events

Port-out events provide a detailed record of everything that happens during the port-out process. Each time a status changes, a comment is added, or a FOC date is updated, the system creates an event that you can query and track. This differs from [Port-out notifications](port-out-notifications.md), which push updates to your webhook or email as they occur. The Events API gives you on-demand access to view your complete event history and republish notifications for specific events if needed.

With the Port-out Events API, you can:

- View all events across your port-out orders.
- Filter events by port-out order, event type, or date range.
- Republish notifications for specific events to your configured webhook or email.

### Event types

The following event types are generated during the port-out lifecycle:

| Event type | Description |
| --- | --- |
| `portout.status_changed` | The port-out order transitioned to a new status. |
| `portout.new_comment` | A new comment was added to the port-out order. |
| `portout.foc_date_changed` | The FOC (Firm Order Commitment) date for the port-out was updated. |

### Listing and republishing events

Use the [GET /v2/portout/events endpoint](https://developers.telnyx.com/api-reference/number-portout/list-all-port-out-events) to retrieve a list of events for your port-out orders. You can filter results by `portout_id` to view events for a specific order, or retrieve all events across your account with pagination support.

If you need to resend notifications for a specific event, use the [POST /v2/portout/events/{id}/republish endpoint](https://developers.telnyx.com/api-reference/number-portout/republish-a-port-out-event) where `{id}` is the event ID. This endpoint republishes notifications only to channels you are currently subscribed to. To configure your notification settings, see [Port-out notifications](port-out-notifications.md). Republishing an event resends the notifications but does not create a new event in the system. Email notifications may take a few minutes to be delivered.
