---
title: Port-out orders
summary: Manage port-out requests when another carrier initiates a transfer for phone numbers on your Telnyx account.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
    content_hash: e9dfcf8e3d8ea773ae3e32f12dd6bfe9de13e93cb30a3f253a5e3d4671424bd7
updated_at: 2026-04-10T00:00:00Z
---

# Port-out orders

Manage port-out requests when another carrier initiates a transfer for phone numbers on your Telnyx account

## Overview

A port-out order is created when another carrier requests to transfer phone numbers away from your Telnyx account. This occurs when an end-user authorizes a new carrier to port their number, and that carrier submits a port-in request to Telnyx.

When Telnyx receives a port-out request, the system automatically creates a port-out order in your account. You can then review the order details and choose to authorize or reject the request based on the information provided.

Port-out orders require a response within 24–48 hours. If you do not respond within this window, the port-out is automatically authorized and will proceed on the requested FOC (Firm Order Commitment) date.

## Port-out order statuses

Each port-out order has a `status` field that indicates its current state in the porting process:

| Status             | Description                                                                                                   |
| :----------------- | :------------------------------------------------------------------------------------------------------------ |
| `pending`          | The port-out request has been received and is awaiting your review.                                           |
| `authorized`       | You have approved the port-out request. The numbers will port on the FOC date.                                |
| `rejected-pending` | You have submitted a rejection. The Porting Ops team is reviewing the rejection reason to ensure it is valid. |
| `rejected`         | The port-out request has been formally rejected and will not proceed.                                         |
| `canceled`         | The port-out request has been canceled by the gaining carrier or Telnyx.                                      |
| `ported`           | The phone numbers have successfully ported to the gaining carrier.                                            |

## How it works

### Step 1: Review incoming port-out orders

Use the [GET /v2/portouts](https://developers.telnyx.com/api-reference/number-portout/list-portout-requests) endpoint to list all port-out orders on your account, or use the [GET /v2/portouts/:id](https://developers.telnyx.com/api-reference/number-portout/get-a-portout-request) endpoint to retrieve a specific order by ID.

Review the order details including `phone_numbers`, `carrier_name`, `requested_foc_date`, and any subscriber information to verify the request is valid.

### Step 2: Authorize or reject the order

After reviewing the port-out order, you must either authorize or reject it.

**To authorize a port-out:**

Use the [PATCH /v2/portouts/:id/authorized](https://developers.telnyx.com/api-reference/number-portout/update-status) endpoint where `:id` is the port-out order ID. Once authorized, the phone numbers are cleared to port out on the FOC date.

**To reject a port-out:**

First, retrieve the available rejection codes for your specific order using the [GET /v2/portouts/rejections/:portout\_id](https://developers.telnyx.com/api-reference/number-portout/list-eligible-port-out-rejection-codes-for-a-specific-order) endpoint. The available rejection codes vary depending on the phone numbers in the order.

Then, use the [PATCH /v2/portouts/:id/rejected-pending](https://developers.telnyx.com/api-reference/number-portout/update-status) endpoint with the appropriate `rejection_code` in the request body.

If you use rejection code `1001` ("Other"), you must include a `reason` field explaining why you are rejecting the order. The Porting Ops team reviews the rejection reason to ensure it is valid. If the reason is not valid, the order is moved back to `pending` and you are notified to review it again.

## Notifications

To receive updates when port-out order statuses change or new comments are added, configure port-out notifications in your account. Notifications can be sent via email or webhook.

For setup instructions and webhook payload examples, see the [Port-out order notifications](https://developers.telnyx.com/docs/numbers/porting/port-out-notifications) guide.

To view and republish port-out events programmatically, see the [Port-out events API](https://developers.telnyx.com/docs/numbers/porting/port-out-events) guide.


## Related Pages

- [Port-out events](../runbooks/port-out-events.md)
- [Port-Out Order Notifications](../runbooks/port-out-order-notifications.md)
