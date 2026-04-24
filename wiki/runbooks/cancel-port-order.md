---
title: Cancel port order
summary: Cancel a port-in order that is no longer needed before it completes.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order/index
    content_hash: f87aa9c49a5c6bbb6ece1c75c9d5da8da0aa3c19995a468283dc6ab546e08034
updated_at: 2026-04-10T00:00:00Z
---

# Cancel port order

Cancel a port-in order that is no longer needed before it completes

## Overview

Canceling a port order allows you to stop a port-in request before it completes. This is useful when business requirements change, the port was submitted in error, or you no longer need to transfer the phone numbers to Telnyx.

When you cancel a port order, it first transitions to a `cancel-pending` status while the Porting Operations team reviews and processes the cancellation request. Once processed, the order moves to `cancelled` status and the port-in will not proceed.

## Constraints

* You cannot cancel a port order via the API within **48 hours of the FOC (Firm Order Commitment) date/time**. If you need to cancel within this window, contact [Telnyx support](https://support.telnyx.com) directly.
* Cancellation requests require review by the Porting Operations team before taking effect.
* Once a port order reaches `cancelled` status, it cannot be reactivated. You would need to submit a new port order.

## Cancellation statuses

When you cancel a port order, it progresses through the following statuses:

| Status           | Description                                                                                        |
| :--------------- | :------------------------------------------------------------------------------------------------- |
| `cancel-pending` | The cancellation request has been submitted and is awaiting review by the Porting Operations team. |
| `cancelled`      | The port order has been successfully cancelled and will not proceed.                               |

## How it works

### Step 1: Cancel the port order

Use the [POST /v2/porting\_orders//actions/cancel endpoint](https://developers.telnyx.com/api-reference/porting-orders/cancel-a-porting-order) to request cancellation of a port order. Provide the port order ID in the request path.

The port order will transition to `cancel-pending` status upon successful submission.

If the port order's FOC date is within 48 hours, the API will return an error. In this case, contact [Telnyx support](https://support.telnyx.com) to request cancellation.

### Step 2: Monitor cancellation status

You can check the status of the cancellation using the [GET /v2/porting\_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order).

The port order will remain in `cancel-pending` status until the Porting Operations team processes the request. Once complete, the status will change to `cancelled`.

## Notifications

You can receive webhook notifications when the port order status changes. Configure webhooks to receive `porting_order.status_changed` events when the order transitions to `cancel-pending` and `cancelled` statuses.

For more information about porting webhooks, see the [port-in events guide](https://developers.telnyx.com/docs/numbers/porting/port-in-events).
