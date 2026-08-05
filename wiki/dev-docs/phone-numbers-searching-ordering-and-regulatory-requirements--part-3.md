---
title: 'Phone Numbers: Searching, Ordering, and Regulatory Requirements'
summary: This page covers the end-to-end workflow for purchasing phone numbers on
  Telnyx, including searching inventory, reserving numbers, placing standard, bulk,
  and advanced orders, fulfilling regulatory requirements (textual, address, document,
  and action types), uploading supporting documents, and configuring webhook notifications.
sources:
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/documents/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements
updated_at: 2026-08-05T14:00:16Z
---

# Phone Numbers: Searching, Ordering, and Regulatory Requirements

*Part 3 of 6 — see also: [Part 1](phone-numbers-searching-ordering-and-regulatory-requirements--part-1.md), [Part 2](phone-numbers-searching-ordering-and-regulatory-requirements--part-2.md), [Part 4](phone-numbers-searching-ordering-and-regulatory-requirements--part-4.md), [Part 5](phone-numbers-searching-ordering-and-regulatory-requirements--part-5.md), [Part 6](phone-numbers-searching-ordering-and-regulatory-requirements--part-6.md)*

This page covers the end-to-end workflow for purchasing phone numbers on Telnyx, including searching inventory, reserving numbers, placing standard, bulk, and advanced orders, fulfilling regulatory requirements (textual, address, document, and action types), uploading supporting documents, and configuring webhook notifications.

## Bulk Number Orders

Bulk number orders (inexplicit orders) allow you to purchase phone numbers by specifying search criteria and quantity, without needing to identify and select specific phone numbers beforehand. The API automatically searches for available numbers matching your criteria, reserves them, and creates number orders on your account. This differs from the standard ordering workflow where you first search, review results, and then create orders for specific phone numbers.

### Constraints

- Bulk orders are only available for phone numbers in the **US and CA**.
- Maximum of 10,000 phone numbers per bulk order.
- The API will only order numbers that are available at the time of processing. Availability is not guaranteed and depends on current inventory levels. Use the [inventory coverage API](https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started#coverage) to check inventory levels prior to ordering.

### Ordering Groups

You can include multiple ordering groups in a single bulk order request. Each ordering group is processed independently and can have different search criteria and strategies. For example, a single bulk order could include:

- 5 local phone numbers in California, US with voice features.
- 3 toll-free phone numbers in US with SMS features.
- 10 local phone numbers in area code 212, New York, US.

Each ordering group tracks its own `count_requested`, `count_allocated`, and `status` fields independently.

### Order Statuses

| Status | Description |
| --- | --- |
| pending | The bulk order is queued and awaiting processing. |
| processing | The order is actively being processed. |
| success | The order was fully processed without errors. All requested phone numbers were ordered. |
| partial_success | The order was processed, but only partially completed. Some numbers could not be purchased due to insufficient inventory or errors. |
| failed | The order could not be processed successfully. |

### How It Works

1. **Create a bulk order.** Use the [POST /v2/inexplicit_number_orders endpoint](https://developers.telnyx.com/api-reference/inexplicit-number-orders/create-an-inexplicit-number-order). Each `ordering_group` requires `country_iso` (US or CA), `count_requested`, and `phone_number_type`. Optionally include [search filters](https://developers.telnyx.com/docs/numbers/phone-numbers/number-search) to narrow down results. Specify a `strategy` that controls behavior when inventory is insufficient: `always` (default) orders whatever quantity is available, while `never` only places the order if the full quantity can be fulfilled. You can also configure `connection_id`, `messaging_profile_id`, `billing_group_id`, or `customer_reference` to automatically apply settings to all ordered phone numbers.
2. **Monitor order status.** Use [GET /v2/inexplicit_number_orders](https://developers.telnyx.com/api-reference/inexplicit-number-orders/list-inexplicit-number-orders) to list all bulk orders, or [GET /v2/inexplicit_number_orders/](https://developers.telnyx.com/api-reference/inexplicit-number-orders/retrieve-an-inexplicit-number-order) to retrieve a specific bulk order by ID. Monitor the `status` field and compare `count_allocated` to `count_requested`.
3. **Access the created number orders.** When the bulk order completes processing, the `orders` array in the API response shows the number orders that were created. Each entry includes:
   - **number_order_id**: The ID of the parent number order.
   - **sub_number_order_ids**: An array of sub number order IDs associated with the parent order.

   Retrieve details using the standard number ordering APIs: [GET /v2/number_orders/](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-number-order) for the parent number order, and [GET /v2/sub_number_orders](https://developers.telnyx.com/api-reference/phone-number-orders/list-sub-number-orders) for sub number orders. From this point, follow the standard [Number Orders](number-orders.md) workflow to complete any remaining steps.
