---
title: Number Orders
summary: Tutorial for ordering phone numbers.
sources:
  - url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders/index
    content_hash: 0acb794957482d23ee87e77d2543acebfce079c8789063d9dcc9f57081b60a21
updated_at: 2026-04-10T00:00:00Z
---

# Number Orders

Tutorial for ordering phone numbers

This guide will walk you through how to order phone numbers.

## Ordering Flow

### Step 1: Search for phone numbers.

Use the [GET /available\_phone\_numbers](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) endpoint to search for phone numbers to purchase. [See this guide](https://developers.telnyx.com/docs/numbers/phone-numbers/number-search) for more details.

Only phone numbers that were previously returned in a search request can be ordered.

### Step 2: Create an order

Use the [POST /number\_orders endpoint](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order) to create an order. 

Note: in some countries, a "requirement group" needs to be included in the payload for the `POST /number_orders` API request. For more details, [check out this guide](https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups).

### Step 3: Regulatory Requirements

If the order does not have regulatory requirements, then it should activate momentarily with no further user action. The rest of the flow outlined (Step 3 and Step 4) is irrelevant in this case.

However, phone numbers in most countries have regulatory requirements. 

Perform a [GET sub\_number\_orders/ request](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-sub-number-order) to see the regulatory requirements for that order (in the `regulatory_requirements` array).

Once you have collected the necessary information, perform a [PATCH /sub\_number\_orders/ request](https://developers.telnyx.com/api-reference/phone-number-orders/update-a-sub-number-orders-requirements) to associate that information to the number order.

For more information on regulatory requirements, check out this guide.

### Step 4: Handling Regulatory Requirement Rejections

All regulatory requirements on an order are vetted individually. Once all regulatory requirements are vetted and approved, the order will complete.

To check on the regulatory requirement vetting status, perform a [GET /number\_order\_phone\_numbers request](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-list-of-phone-numbers-associated-to-orders). It is possible that some (or all) of the information provided is rejected. If a rejection occurs:

* Determine which regulatory requirement(s) was rejected
* [Review the comments](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-all-comments) on the order to see a more detailed explanation why the regulatory requirement(s) was rejected
* Update the order with any corrections, and resubmit for approval

## “Number Order” vs “Sub Number Order”

“Number Orders” and “Sub Number Orders” share a parent - child relationship:

* “Number Order” = “parent”. Overarching order entity. 
* “Sub Number Order” = “child”. Nested within the “number order”.

The `POST /number_orders` request will always create one (1) “number order”. However, it could be split into multiple “sub number orders” depending on the phone numbers you are purchasing. For example, if you created a number order that included the following:

* 5 `local` phone numbers in Country A
* 5 `toll_free` phone numbers in Country A
* 5 `local` phone numbers in Country B

Then the request would be 1 number order with 3 nested sub number orders.

Sub number orders are processed independently, even if they are a part of the same number order.

## Order Statuses

Number orders / sub number orders have a few possible statuses:

| Status    | Description                                                                                                                                                      |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pending   | Order was created and is being processed. Phone numbers are not yet active.                                                                                      |
| success   | Order completed successfully. Phone numbers were activated.                                                                                                      |
| failure   | There was an issue with the order.                                                                                                                               |
| cancelled | The order was cancelled. [Either by the user](https://developers.telnyx.com/api-reference/phone-number-orders/cancel-a-sub-number-order), or by the Telnyx team. |
| deleted   | All phone numbers on the order have been deleted from the user account.                                                                                          |

When a number order / sub number order is in a `pending` status, [the phone number status](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-list-of-phone-numbers-associated-to-orders) will give insight into the vetting process. Phone numbers can have the following statuses while an order is `pending`:

| Status                        | Description                                                                                                                                                               |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| requirement-info-pending      | Order is missing values for one or more regulatory requirements. Customer needs to provide additional information to fulfill all requirements before vetting can proceed. |
| requirement-info-under-review | Customer has provided values for all regulatory requirements. Order is awaiting vetting by Number Ops                                                                     |
| requirement-info-exception    | One or more of the regulatory requirements have been rejected by Number Ops. Customer needs to review the rejections, make corrections, and resubmit                      |
| approved                      | All requirements are approved.                                                                                                                                            |
| deleted                       | All phone numbers on the order have been deleted from the user account.                                                                                                   |

## Deadline + Auto Cancellation

Each order has a `deadline` attribute. Users are expected to have all regulatory requirements uploaded by the deadline, at which point the `deadline` is erased.

Failure to provide all regulatory requirements by the deadline will result in auto-cancellation of the order.

If one or more regulatory requirements are rejected, a new deadline will be set. The user will have until the new deadline to make corrections to avoid auto-cancellation.

Deadlines can be extended upon request via comment on the order.

## Webhook notifications

[Follow this support article](https://support.telnyx.com/en/articles/4277896-notification-settings) to set up webhook notifications for order events. 

Select the Notification Setting “Number Order Notifications: for all number order notifications”.


## Related Pages

- [Bulk number orders](../runbooks/bulk-number-orders.md)
- [Number Reservations](../runbooks/number-reservations.md)
- [Number Pool](../runbooks/number-pool.md)
- [Advanced Orders](../runbooks/advanced-orders.md)
- [Number Search](../runbooks/number-search.md)
