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

*Part 4 of 6 — see also: [Part 1](phone-numbers-searching-ordering-and-regulatory-requirements--part-1.md), [Part 2](phone-numbers-searching-ordering-and-regulatory-requirements--part-2.md), [Part 3](phone-numbers-searching-ordering-and-regulatory-requirements--part-3.md), [Part 5](phone-numbers-searching-ordering-and-regulatory-requirements--part-5.md), [Part 6](phone-numbers-searching-ordering-and-regulatory-requirements--part-6.md)*

This page covers the end-to-end workflow for purchasing phone numbers on Telnyx, including searching inventory, reserving numbers, placing standard, bulk, and advanced orders, fulfilling regulatory requirements (textual, address, document, and action types), uploading supporting documents, and configuring webhook notifications.

## Advanced Orders

When you search for numbers, four outcomes are possible:

1. The search returns available phone numbers that you can purchase.
2. The search targets a region where Telnyx has no coverage, resulting in a `4xx` response.
3. The request errors out due to a server issue (`5xx`) or a timeout.
4. Telnyx has coverage but no available numbers matching the given search criteria.

In case (4), you can submit an Advanced Order request. Telnyx's Number Operations team will attempt to acquire the phone numbers that are currently unavailable. If successful, the team will order and activate the numbers on your account. This process is asynchronous.

### Constraints

- Not eligible for US or CA toll-free phone numbers. The search API reflects all possible inventory.
- Not eligible for unique phone numbers (e.g., a specific phone number like 123-456-7890, or numbers ending in 0000).
- Advanced orders are best effort. Telnyx cannot guarantee that the requested phone numbers can be procured.

### Advanced Order Statuses

- **pending**: The Advanced Order has been created but is not yet being processed by Telnyx.
- **processing**: The Advanced Order is currently being processed by Telnyx.
- **exception**: There is an issue with the advanced order. Please review it and take the appropriate actions to resolve the issue.
- **hold**: Telnyx needs to replenish inventory to fulfill your request. This process can take some time. No further action is needed on your end; the order will remain in this status until Telnyx is able to replenish those phone numbers.
- **ordered**: The Advanced Order has been successfully placed and fulfilled.
- **failed**: The Advanced Order could not be completed.

### How It Works

1. **Search for phone numbers to purchase.** Use the `GET v2/available_phone_numbers` endpoint ([API reference](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers)). If no results are returned, try adjusting your search filters to find similar phone numbers that are immediately available.
2. **If no results are returned, create an Advanced Order.** Use the `POST /v2/advanced_orders` endpoint ([API reference](https://developers.telnyx.com/api-reference/advanced-number-orders/create-advanced-order)). Include the same values that you were using as search parameters previously.
3. **Add regulatory requirements to an Advanced Order.** In most countries, Number Ops can only procure phone numbers if you provide the necessary regulatory requirements. Number Ops will reach out and ask you to provide the applicable regulatory requirements.
   1. Create a [requirement group](requirement-groups--part-1.md) that matches the country and phone number type of your Advanced Order.
   2. Make a `PATCH https://api.telnyx.com/v2/advanced_orders/:order_id/requirement_group` request ([API reference](https://developers.telnyx.com/api-reference/advanced-number-orders/update-advanced-order)). Use the requirement group `id` as the `requirement_group_id` value in the request body.
   3. To edit the requirements associated with the Advanced Order, edit them on the requirement group first, then `PATCH v2/advanced_orders/:order_id/requirement_group` again. The updated requirements will override the original ones.

   After you PATCH the order with a fulfilled requirement group, the `advanced_order_requirements` array will contain the values from your requirement group.

4. **Finish the number ordering process.** When an Advanced Order transitions to `ordered` status, Number Ops has placed number order(s) on your account for the requested phone numbers. Check the `orders` array in the Advanced Order API response to see which number orders were placed. The `orders` array lists the Number Order IDs for the orders that were placed. Use the `GET v2/number_orders/:number_order_id` request ([API reference](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-number-order)) to view details about the actual number order, which phone numbers were ordered, the status of the order, and any regulatory requirements to be fulfilled. Treat these new number orders like any other number order.

### Comments

You can communicate with the Number Operations team about your request through the Comments API. Use `filter[comment_record_type]=advanced_number_order` and specify the advanced order ID as the `comment_record_id` in the API requests.

- [View comments](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-all-comments)
- [Create a comment](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-comment)

### Notifications

You can set up email and/or webhook notifications for your Advanced Orders. [Follow this guide](https://support.telnyx.com/en/articles/4277896-notification-settings) to learn more about configuring notifications.
