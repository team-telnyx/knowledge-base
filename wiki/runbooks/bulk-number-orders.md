---
title: Bulk number orders
summary: Order phone numbers in bulk by specifying quantity and search criteria without selecting specific numbers upfront.
sources:
  - url: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering/index
    content_hash: 35df02204670c42a19a3bdcb76638cf43188e3014f3c1a465200ef8f9c6b57cc
updated_at: 2026-04-10T00:00:00Z
---

# Bulk number orders

Order phone numbers in bulk by specifying quantity and search criteria without selecting specific numbers upfront

## Overview

Bulk number orders (inexplicit orders) allow you to purchase phone numbers by specifying search criteria and quantity, without needing to identify and select specific phone numbers beforehand. The API automatically searches for available numbers matching your criteria, reserves them, and creates number orders on your account.

This differs from the standard ordering workflow where you first [search for available numbers](https://developers.telnyx.com/docs/numbers/phone-numbers/number-search), review the results, and then [create orders](https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders) for specific phone numbers.

The bulk ordering process handles the search, reservation, and ordering steps automatically in a single API request. Orders are processed asynchronously, with processing time varying based on your search criteria, quantity requested, and current inventory availability.

## Constraints

* Bulk orders are only available for phone numbers in the **US and CA**.
* Maximum of 10,000 phone numbers per bulk order.
* The API will only order numbers that are available at the time of processing. Availability is not guaranteed and depends on current inventory levels. You can use the [inventory coverage API](https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started#coverage) to check inventory levels prior to ordering.

## Ordering Groups

You can include multiple ordering groups in a single bulk order request. Each ordering group is processed independently and can have different search criteria and strategies.

For example, you could create one bulk order that includes:

* 5 local phone numbers in California, US with voice features.
* 3 toll-free phone numbers in US with SMS features.
* 10 local phone numbers in area code 212, New York, US.

Each ordering group tracks its own `count_requested`, `count_allocated`, and `status` fields independently.

## Order Statuses

Each ordering group within a bulk order has a status that indicates its current progress:

| Status           | Description                                                                                                                                                            |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pending          | The bulk order is queued and awaiting processing.                                                                                                                      |
| processing       | The order is actively being processed.                                                                                                                                 |
| success          | The order was fully processed without errors. All requested phone numbers were ordered.                                                                                |
| partial\_success | The order was processed, but only partially completed. Some numbers could not be purchased due to insufficient inventory or errors encountered during number ordering. |
| failed           | The order could not be processed successfully.                                                                                                                         |

## How It Works

### Step 1: Create a bulk order

Use the [POST /v2/inexplicit\_number\_orders endpoint](https://developers.telnyx.com/api-reference/inexplicit-number-orders/create-an-inexplicit-number-order) to create an order. Each `ordering_group` requires `country_iso` (US or CA), `count_requested`, and `phone_number_type`.

Optionally include [search filters](https://developers.telnyx.com/docs/numbers/phone-numbers/number-search) to narrow down results.

You can specify a `strategy` that controls behavior when inventory is insufficient: `always` (default) orders whatever quantity is available, while `never` only places the order if the full quantity can be fulfilled.

You can also configure `connection_id`, `messaging_profile_id`, `billing_group_id`, or `customer_reference` to automatically apply settings to all ordered phone numbers.

### Step 2: Monitor order status

You can check the status of your bulk orders using the following endpoints:

* [GET /v2/inexplicit\_number\_orders](https://developers.telnyx.com/api-reference/inexplicit-number-orders/list-inexplicit-number-orders): List all bulk orders with pagination support.
* [GET /v2/inexplicit\_number\_orders/](https://developers.telnyx.com/api-reference/inexplicit-number-orders/retrieve-an-inexplicit-number-order): Retrieve a specific bulk order by ID.

Monitor the `status` field to track progress, and compare `count_allocated` to `count_requested` to see how many numbers were successfully ordered in each ordering group.

### Step 3: Access the created number orders

When the bulk order completes processing, the `orders` array in the API response shows the number orders that were created to fulfill your request. Each entry includes:

* **number\_order\_id**: The ID of the parent number order.
* **sub\_number\_order\_ids**: An array of sub number order IDs associated with the parent order.

You can retrieve details about these orders using the standard number ordering APIs:

* [GET /v2/number\_orders/](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-number-order): Retrieve the parent number order.
* [GET /v2/sub\_number\_orders](https://developers.telnyx.com/api-reference/phone-number-orders/list-sub-number-orders): List sub number orders.

From this point, follow the standard [number ordering workflow](https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders) to complete any remaining steps.

## Webhook Notifications

You can configure webhook notifications to receive updates about your orders. [Follow this support article](https://support.telnyx.com/en/articles/4277896-notification-settings) to set up webhook notifications.

Select the "Number Order Notifications" notification setting to receive webhooks for all number order events. Note that webhook events are generated by the underlying number orders created by the bulk order, not by the bulk order itself.


## Related Pages

- [Number Orders](../runbooks/number-orders.md)
