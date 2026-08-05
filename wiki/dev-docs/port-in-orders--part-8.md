---
title: Port-in orders
summary: Port-in orders transfer existing phone numbers from another carrier to Telnyx.
  This page covers the end-to-end port-in workflow via the V2 porting API, including
  creating and submitting orders, requesting FOC dates, on-demand activations, block
  and extension porting, bundle pre-configuration, messaging activation, cancellation,
  and webhook notifications and events.
sources:
- url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
updated_at: 2026-08-05T14:01:21Z
---

# Port-in orders

*Part 8 of 8 — see also: [Part 1](port-in-orders--part-1.md), [Part 2](port-in-orders--part-2.md), [Part 3](port-in-orders--part-3.md), [Part 4](port-in-orders--part-4.md), [Part 5](port-in-orders--part-5.md), [Part 6](port-in-orders--part-6.md), [Part 7](port-in-orders--part-7.md)*

Port-in orders transfer existing phone numbers from another carrier to Telnyx. This page covers the end-to-end port-in workflow via the V2 porting API, including creating and submitting orders, requesting FOC dates, on-demand activations, block and extension porting, bundle pre-configuration, messaging activation, cancellation, and webhook notifications and events.

## Port-in events

Port-in events provide a detailed record of everything that happens during the port-in process. Each time a status changes, a comment is added, or an order is split, the system creates an event that you can query and track.

This differs from [Port-in order notifications](port-in-order-notifications.md), which push updates to your webhook or email as they occur. The Events API gives you on-demand access to view your complete event history and republish notifications for specific events if needed.

With the Port-in Events API, you can:

- View all events across your port-in orders.
- Filter events by port-in order, event type, or date range.
- Republish notifications for specific events to your configured webhook or email.

### Event types

| Event type | Description |
| --- | --- |
| `porting_order.status_changed` | The port-in order transitioned to a new status. |
| `porting_order.new_comment` | A new comment was added to the port-in order. |
| `porting_order.split` | One or more phone numbers were split into a separate order. |
| `porting_order.messaging_changed` | The messaging activation status changed for the port-in order. |
| `porting_order.deleted` | A draft port-in order was deleted. |

### How it works

**Step 1: List port-in events.** Use the [GET /v2/porting/events endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-events) to retrieve a list of events for your port-in orders. You can filter results by `porting_order_id` to view events for a specific order, or retrieve all events across your account with pagination support.

**Step 2: Republish event notifications.** If you need to resend notifications for a specific event, use the [POST /v2/porting/events/{id}/republish endpoint](https://developers.telnyx.com/api-reference/porting-orders/republish-a-porting-event) where `{id}` is the event ID. This endpoint republishes notifications only to channels you are currently subscribed to. To configure your notification settings, see [how to set up port-in notifications](https://developers.telnyx.com/docs/numbers/porting/port-in-notifications#how-to-setup-notifications-via-the-portal-for-all-port-orders-email-and-webhook). Republishing an event resends the notifications but does not create a new event in the system. Email notifications may take a few minutes to be delivered.

## Additional resources

- [Port-in requirements](port-in-requirements.md) - View and fulfill regulatory requirements on your port orders.
- [Allowed FOC dates](allowed-foc-dates.md) - Request and set a specific date for your port order to complete.
- [On-demand activations](on-demand-activations.md) - Take control of your port order with FastPort on-demand activations.
- [Cancel port order](cancel-port-order.md) - Cancel a port order before it completes.
