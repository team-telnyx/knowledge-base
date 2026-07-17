---
title: Phone Numbers and Porting
summary: This page consolidates Telnyx developer documentation covering phone number
  search, ordering, reservations, bulk and advanced orders, regulatory requirements,
  requirement groups, documents, port-in and port-out workflows, and the notifications
  and events that track them. It provides an end-to-end reference for purchasing numbers,
  fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and
  monitoring the lifecycle of those operations via webhooks and events.
sources:
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/documents/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups
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
updated_at: 2026-07-17T09:16:33Z
---

# Phone Numbers and Porting

*Part 10 of 11 — see also: [Part 1](phone-numbers-and-porting--part-1.md), [Part 2](phone-numbers-and-porting--part-2.md), [Part 3](phone-numbers-and-porting--part-3.md), [Part 4](phone-numbers-and-porting--part-4.md), [Part 5](phone-numbers-and-porting--part-5.md), [Part 6](phone-numbers-and-porting--part-6.md), [Part 7](phone-numbers-and-porting--part-7.md), [Part 8](phone-numbers-and-porting--part-8.md), [Part 9](phone-numbers-and-porting--part-9.md), [Part 11](phone-numbers-and-porting--part-11.md)*

This page consolidates Telnyx developer documentation covering phone number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in and port-out workflows, and the notifications and events that track them. It provides an end-to-end reference for purchasing numbers, fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and monitoring the lifecycle of those operations via webhooks and events.

## Port-in Notifications

Port-in notifications provide real-time updates about your port orders. Notifications can be emitted to either email or webhook addresses for the following events:

1. Port order status changes
2. New comments
3. Split port orders
4. Messaging activation
5. Deleted "draft" porting orders

### Setup via Portal

1. Sign in to the [Telnyx Portal](https://portal.telnyx.com/).
2. Go to your `Account Settings` and click on the `Advanced Features` section. Then select [Notifications](https://portal.telnyx.com/#/app/advanced-features/notifications).
3. Click on the `New Profile` button to create a new `Notification Profile`.
4. Click on the `New Channel` button to specify which email or webhook URL to send notifications to.
5. Click on the `New Setting` button, select `Port In Notifications` and select the profile and channel.

### Setup on Specific Port Orders

If your use case requires each port order to have its own webhook URL, you can specify a unique URL as the value for the `webhook_url` parameter in the port order form:

```
curl --location --request PATCH 'https://api.telnyx.com/v2/porting_orders/{{id}}' \
--header 'Authorization: Bearer [REDACTED] \
--header 'Content-Type: application/json' \
--data-raw '{
    "webhook_url": "https://webhook.site/98e5e9e2-4921-4a64-b3c8-da0c6ce760f3"
}'
```

### Webhook Event Types

The following webhook events are emitted during the port-in lifecycle:

- `porting_order.status_changed`: The port-in order transitioned to a new status.
- `porting_order.new_comment`: A new comment was added to the port-in order.
- `porting_order.split`: One or more phone numbers were split into a separate order.
- `porting_order.messaging_changed`: The messaging activation status changed for the port-in order.
- `porting_order.deleted`: A draft port-in order was deleted.

## Port-in Events

Port-in events provide a detailed record of everything that happens during the port-in process. Each time a status changes, a comment is added, or an order is split, the system creates an event that you can query and track. This differs from port-in notifications, which push updates to your webhook or email as they occur. The Events API gives you on-demand access to view your complete event history and republish notifications for specific events if needed.

With the Port-in Events API, you can:

- View all events across your port-in orders.
- Filter events by port-in order, event type, or date range.
- Republish notifications for specific events to your configured webhook or email.

Use the [GET /v2/porting/events endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-events) to retrieve a list of events for your port-in orders. You can filter results by `porting_order_id` to view events for a specific order, or retrieve all events across your account with pagination support.

If you need to resend notifications for a specific event, use the [POST /v2/porting/events//republish endpoint](https://developers.telnyx.com/api-reference/porting-orders/republish-a-porting-event) where `{id}` is the event ID. This endpoint republishes notifications only to channels you are currently subscribed to. Republishing an event resends the notifications but does not create a new event in the system.

## Port-out Orders

A port-out order is created when another carrier requests to transfer phone numbers away from your Telnyx account. This occurs when an end-user authorizes a new carrier to port their number, and that carrier submits a port-in request to Telnyx. When Telnyx receives a port-out request, the system automatically creates a port-out order in your account. You can then review the order details and choose to authorize or reject the request based on the information provided.

Port-out orders require a response within 24–48 hours. If you do not respond within this window, the port-out is automatically authorized and will proceed on the requested FOC date.

### Port-out Order Statuses

| Status | Description |
| --- | --- |
| `pending` | The port-out request has been received and is awaiting your review. |
| `authorized` | You have approved the port-out request. The numbers will port on the FOC date. |
| `rejected-pending` | You have submitted a rejection. The Porting Ops team is reviewing the rejection reason. |
| `rejected` | The port-out request has been formally rejected and will not proceed. |
| `canceled` | The port-out request has been canceled by the gaining carrier or Telnyx. |
| `ported` | The phone numbers have successfully ported to the gaining carrier. |

### How It Works

**Step 1: Review incoming port-out orders.** Use the [GET /v2/portouts](https://developers.telnyx.com/api-reference/number-portout/list-portout-requests) endpoint to list all port-out orders on your account, or use the [GET /v2/portouts/:id](https://developers.telnyx.com/api-reference/number-portout/get-a-portout-request) endpoint to retrieve a specific order by ID. Review the order details including `phone_numbers`, `carrier_name`, `requested_foc_date`, and any subscriber information.

**Step 2: Authorize or reject the order.**

- **To authorize a port-out:** Use the [PATCH /v2/portouts/:id/authorized](https://developers.telnyx.com/api-reference/number-portout/update-status) endpoint where `:id` is the port-out order ID.
- **To reject a port-out:** First, retrieve the available rejection codes for your specific order using the [GET /v2/portouts/rejections/:portout_id](https://developers.telnyx.com/api-reference/number-portout/list-eligible-port-out-rejection-codes-for-a-specific-order) endpoint. Then, use the [PATCH /v2/portouts/:id/rejected-pending](https://developers.telnyx.com/api-reference/number-portout/update-status) endpoint with the appropriate `rejection_code` in the request body. If you use rejection code `1001` ("Other"), you must include a `reason` field explaining why you are rejecting the order.

## Port-out Notifications

Port-out notifications provide updates when port-out order statuses change or new comments are added. Notifications can be sent via email or webhook.

### Setup

1. Sign in to the [Telnyx Portal](https://portal.telnyx.com/).
2. Go to your `Account Settings` and click on the `Advanced Features` section. Then select [Notifications](https://portal.telnyx.com/#/app/advanced-features/notifications).
3. Click on the `New Profile` button to create a new `Notification Profile`.
4. Click on the `New Channel` button to specify which email or webhook URL to send notifications to.
5. Click on the `New Setting` button, select `Port Out Notifications` and select the profile and channel.

### Webhook Event Types

The following webhook events are emitted during the port-out lifecycle:

- `portout.status_changed`: The port-out order transitioned to a new status.
- `portout.new_comment`: A new comment was added to the port-out order.
- `portout.foc_date_changed`: The FOC date for the port-out was updated.

For port-out orders, the gaining carrier is allotted a grace period of 10 days, which means the gaining carrier can port the phone number at any point between the FOC date listed and the following 10 days.
