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

*Part 3 of 11 — see also: [Part 1](phone-numbers-and-porting--part-1.md), [Part 2](phone-numbers-and-porting--part-2.md), [Part 4](phone-numbers-and-porting--part-4.md), [Part 5](phone-numbers-and-porting--part-5.md), [Part 6](phone-numbers-and-porting--part-6.md), [Part 7](phone-numbers-and-porting--part-7.md), [Part 8](phone-numbers-and-porting--part-8.md), [Part 9](phone-numbers-and-porting--part-9.md), [Part 10](phone-numbers-and-porting--part-10.md), [Part 11](phone-numbers-and-porting--part-11.md)*

This page consolidates Telnyx developer documentation covering phone number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in and port-out workflows, and the notifications and events that track them. It provides an end-to-end reference for purchasing numbers, fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and monitoring the lifecycle of those operations via webhooks and events.

## Advanced Orders

When you search for numbers, four outcomes are possible:

1. The search returns available phone numbers that you can purchase.
2. The search targets a region where Telnyx has no coverage, resulting in a `4xx` response.
3. The request errors out due to a server issue (`5xx`) or a timeout.
4. Telnyx has coverage but no available numbers matching the given search criteria. This is when the Advanced Order Request API is useful.

In case (4), you can submit an Advanced Order request. Telnyx's Number Operations team will attempt to acquire the phone numbers that are currently unavailable. If successful, the team will order and activate the numbers on your account. This process is asynchronous.

### Constraints

- Not eligible for US or CA toll-free phone numbers. The search API reflects all possible inventory.
- Not eligible for unique phone numbers (e.g., a specific phone number like 123-456-7890, or a number ending in 0000).
- Advanced orders are best effort. Telnyx cannot guarantee that the requested phone numbers can be procured.

### Advanced Order Statuses

- **pending**: The Advanced Order has been created but is not yet being processed by Telnyx.
- **processing**: The Advanced Order is currently being processed by Telnyx.
- **exception**: There is an issue with the advanced order. Please review it and take the appropriate actions to resolve the issue.
- **hold**: Telnyx needs to replenish inventory to fulfill the request. This process can take some time. No further action is needed on your end.
- **ordered**: The Advanced Order has been successfully placed and fulfilled.
- **failed**: The Advanced Order could not be completed.

### How It Works

**1. Search for phone numbers to purchase.** First, search for your phone numbers using the `GET v2/available_phone_numbers` endpoint. If no results are returned, try to adjust your search filters to find similar phone numbers that are immediately available.

**2. If no results are returned, create an Advanced Order.** Create an Advanced Order using the `POST /v2/advanced_orders` endpoint. In the body of the request, include the same values that you were using as search parameters previously.

**3. Add regulatory requirements to an Advanced Order.** In most countries, the Number Ops team can only procure phone numbers if you provide the necessary regulatory requirements. Create a requirement group that matches the country and phone number type of your Advanced Order, then make a `PATCH https://api.telnyx.com/v2/advanced_orders/:order_id/requirement_group` request using the requirement group `id` as the `requirement_group_id` value. If you need to edit the requirements, edit them on the requirement group first, then PATCH the Advanced Order again.

**4. Finish the number ordering process.** When an Advanced Order transitions to `ordered` status, Number Ops has placed number order(s) on your account for the requested phone numbers. Check the `orders` array in the Advanced Order API response to see which number orders were placed. Use the `GET v2/number_orders/:number_order_id` request to view details about the actual number order, which phone numbers were ordered, the status of the order, and any regulatory requirements to be fulfilled.

### Comments and Notifications

You can communicate with the Number Operations team about your request through the Comments API. Use `filter[comment_record_type]=advanced_number_order` and specify the advanced order ID as the `comment_record_id` in the API requests.

You can set up email and/or webhook notifications for your Advanced Orders. Webhook events include `advanced_order.status_update` (for transitions between statuses) and `advanced_order.new_comment`.

## Bulk Number Orders

Bulk number orders (inexplicit orders) allow you to purchase phone numbers by specifying search criteria and quantity, without needing to identify and select specific phone numbers beforehand. The API automatically searches for available numbers matching your criteria, reserves them, and creates number orders on your account. This differs from the standard ordering workflow where you first search for available numbers, review the results, and then create orders for specific phone numbers.

### Constraints

- Bulk orders are only available for phone numbers in the US and CA.
- Maximum of 10,000 phone numbers per bulk order.
- The API will only order numbers that are available at the time of processing. Availability is not guaranteed and depends on current inventory levels.

### Ordering Groups

You can include multiple ordering groups in a single bulk order request. Each ordering group is processed independently and can have different search criteria and strategies. For example, you could create one bulk order that includes 5 local phone numbers in California, US with voice features; 3 toll-free phone numbers in US with SMS features; and 10 local phone numbers in area code 212, New York, US. Each ordering group tracks its own `count_requested`, `count_allocated`, and `status` fields independently.

### Order Statuses

Each ordering group within a bulk order has a status that indicates its current progress:

| Status | Description |
| --- | --- |
| pending | The bulk order is queued and awaiting processing. |
| processing | The order is actively being processed. |
| success | The order was fully processed without errors. All requested phone numbers were ordered. |
| partial_success | The order was processed, but only partially completed. Some numbers could not be purchased. |
| failed | The order could not be processed successfully. |

### How It Works

**Step 1: Create a bulk order.** Use the [POST /v2/inexplicit_number_orders endpoint](https://developers.telnyx.com/api-reference/inexplicit-number-orders/create-an-inexplicit-number-order) to create an order. Each `ordering_group` requires `country_iso` (US or CA), `count_requested`, and `phone_number_type`. Optionally include search filters to narrow down results. You can specify a `strategy` that controls behavior when inventory is insufficient: `always` (default) orders whatever quantity is available, while `never` only places the order if the full quantity can be fulfilled. You can also configure `connection_id`, `messaging_profile_id`, `billing_group_id`, or `customer_reference` to automatically apply settings to all ordered phone numbers.

**Step 2: Monitor order status.** Check the status of your bulk orders using the [GET /v2/inexplicit_number_orders](https://developers.telnyx.com/api-reference/inexplicit-number-orders/list-inexplicit-number-orders) and [GET /v2/inexplicit_number_orders/](https://developers.telnyx.com/api-reference/inexplicit-number-orders/retrieve-an-inexplicit-number-order) endpoints. Monitor the `status` field to track progress, and compare `count_allocated` to `count_requested` to see how many numbers were successfully ordered.

**Step 3: Access the created number orders.** When the bulk order completes processing, the `orders` array in the API response shows the number orders that were created. Each entry includes a `number_order_id` and `sub_number_order_ids`. From this point, follow the standard number ordering workflow to complete any remaining steps.

Webhook notifications are generated by the underlying number orders created by the bulk order, not by the bulk order itself. Select the "Number Order Notifications" notification setting to receive webhooks for all number order events.
