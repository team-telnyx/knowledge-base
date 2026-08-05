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

*Part 6 of 8 — see also: [Part 1](port-in-orders--part-1.md), [Part 2](port-in-orders--part-2.md), [Part 3](port-in-orders--part-3.md), [Part 4](port-in-orders--part-4.md), [Part 5](port-in-orders--part-5.md), [Part 7](port-in-orders--part-7.md), [Part 8](port-in-orders--part-8.md)*

Port-in orders transfer existing phone numbers from another carrier to Telnyx. This page covers the end-to-end port-in workflow via the V2 porting API, including creating and submitting orders, requesting FOC dates, on-demand activations, block and extension porting, bundle pre-configuration, messaging activation, cancellation, and webhook notifications and events.

## Cancel port order

Canceling a port order allows you to stop a port-in request before it completes. This is useful when business requirements change, the port was submitted in error, or you no longer need to transfer the phone numbers to Telnyx.

When you cancel a port order, it first transitions to a `cancel-pending` status while the Porting Operations team reviews and processes the cancellation request. Once processed, the order moves to `cancelled` status and the port-in will not proceed.

### Constraints

- You cannot cancel a port order via the API within **48 hours of the FOC (Firm Order Commitment) date/time**. If you need to cancel within this window, contact [Telnyx support](https://support.telnyx.com) directly.
- Cancellation requests require review by the Porting Operations team before taking effect.
- Once a port order reaches `cancelled` status, it cannot be reactivated. You would need to submit a new port order.

### Cancellation statuses

| Status | Description |
| --- | --- |
| `cancel-pending` | The cancellation request has been submitted and is awaiting review by the Porting Operations team. |
| `cancelled` | The port order has been successfully cancelled and will not proceed. |

### How it works

**Step 1: Cancel the port order.** Use the [POST /v2/porting_orders/{id}/actions/cancel endpoint](https://developers.telnyx.com/api-reference/porting-orders/cancel-a-porting-order) to request cancellation of a port order. Provide the port order ID in the request path. The port order will transition to `cancel-pending` status upon successful submission. If the port order's FOC date is within 48 hours, the API will return an error. In this case, contact [Telnyx support](https://support.telnyx.com) to request cancellation.

**Step 2: Monitor cancellation status.** You can check the status of the cancellation using the [GET /v2/porting_orders/{id} endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order). The port order will remain in `cancel-pending` status until the Porting Operations team processes the request. Once complete, the status will change to `cancelled`.

## Comments

Comments allow you to communicate directly with Telnyx Porting Operations during the porting process. Use the [Create comment endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-comment-for-a-porting-order) to send messages or respond to requests from the porting team.

Monitor your port orders for new comments using the [List comments endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-comments-of-a-porting-order). Porting Operations may add comments to request additional information or provide updates about your order. Subscribe to the `porting_order.new_comment` webhook event to receive notifications when new comments are added.
