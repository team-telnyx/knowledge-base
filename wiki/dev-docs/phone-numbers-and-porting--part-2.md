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

*Part 2 of 11 — see also: [Part 1](phone-numbers-and-porting--part-1.md), [Part 3](phone-numbers-and-porting--part-3.md), [Part 4](phone-numbers-and-porting--part-4.md), [Part 5](phone-numbers-and-porting--part-5.md), [Part 6](phone-numbers-and-porting--part-6.md), [Part 7](phone-numbers-and-porting--part-7.md), [Part 8](phone-numbers-and-porting--part-8.md), [Part 9](phone-numbers-and-porting--part-9.md), [Part 10](phone-numbers-and-porting--part-10.md), [Part 11](phone-numbers-and-porting--part-11.md)*

This page consolidates Telnyx developer documentation covering phone number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in and port-out workflows, and the notifications and events that track them. It provides an end-to-end reference for purchasing numbers, fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and monitoring the lifecycle of those operations via webhooks and events.

## Number Orders

### Ordering Flow

**Step 1: Search for phone numbers.** Use the [GET /available_phone_numbers](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) endpoint to search for phone numbers to purchase. Only phone numbers that were previously returned in a search request can be ordered.

**Step 2: Create an order.** Use the [POST /number_orders endpoint](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order) to create an order. In some countries, a requirement group needs to be included in the payload for the `POST /number_orders` API request.

**Step 3: Regulatory Requirements.** If the order does not have regulatory requirements, it should activate momentarily with no further user action. However, phone numbers in most countries have regulatory requirements. Perform a [GET sub_number_orders/ request](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-sub-number-order) to see the regulatory requirements for that order (in the `regulatory_requirements` array). Once you have collected the necessary information, perform a [PATCH /sub_number_orders/ request](https://developers.telnyx.com/api-reference/phone-number-orders/update-a-sub-number-orders-requirements) to associate that information to the number order.

**Step 4: Handling Regulatory Requirement Rejections.** All regulatory requirements on an order are vetted individually. Once all regulatory requirements are vetted and approved, the order will complete. To check on the regulatory requirement vetting status, perform a [GET /number_order_phone_numbers request](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-list-of-phone-numbers-associated-to-orders). If a rejection occurs:

- Determine which regulatory requirement(s) was rejected.
- Review the comments on the order to see a more detailed explanation.
- Update the order with any corrections, and resubmit for approval.

### Number Order vs Sub Number Order

"Number Orders" and "Sub Number Orders" share a parent-child relationship:

- **Number Order** = parent. Overarching order entity.
- **Sub Number Order** = child. Nested within the number order.

The `POST /number_orders` request will always create one number order, but it could be split into multiple sub number orders depending on the phone numbers you are purchasing. For example, a number order that includes 5 local phone numbers in Country A, 5 toll-free phone numbers in Country A, and 5 local phone numbers in Country B would result in 1 number order with 3 nested sub number orders. Sub number orders are processed independently, even if they are part of the same number order.

### Order Statuses

Number orders and sub number orders have the following statuses:

| Status | Description |
| --- | --- |
| pending | Order was created and is being processed. Phone numbers are not yet active. |
| success | Order completed successfully. Phone numbers were activated. |
| failure | There was an issue with the order. |
| cancelled | The order was cancelled, either by the user or by the Telnyx team. |
| deleted | All phone numbers on the order have been deleted from the user account. |

When a number order or sub number order is in a `pending` status, the phone number status will give insight into the vetting process:

| Status | Description |
| --- | --- |
| requirement-info-pending | Order is missing values for one or more regulatory requirements. |
| requirement-info-under-review | Customer has provided values for all regulatory requirements. Order is awaiting vetting by Number Ops. |
| requirement-info-exception | One or more regulatory requirements have been rejected by Number Ops. |
| approved | All requirements are approved. |
| deleted | All phone numbers on the order have been deleted from the user account. |

### Deadline and Auto Cancellation

Each order has a `deadline` attribute. Users are expected to have all regulatory requirements uploaded by the deadline, at which point the `deadline` is erased. Failure to provide all regulatory requirements by the deadline will result in auto-cancellation of the order. If one or more regulatory requirements are rejected, a new deadline will be set. Deadlines can be extended upon request via comment on the order.
