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

*Part 2 of 6 — see also: [Part 1](phone-numbers-searching-ordering-and-regulatory-requirements--part-1.md), [Part 3](phone-numbers-searching-ordering-and-regulatory-requirements--part-3.md), [Part 4](phone-numbers-searching-ordering-and-regulatory-requirements--part-4.md), [Part 5](phone-numbers-searching-ordering-and-regulatory-requirements--part-5.md), [Part 6](phone-numbers-searching-ordering-and-regulatory-requirements--part-6.md)*

This page covers the end-to-end workflow for purchasing phone numbers on Telnyx, including searching inventory, reserving numbers, placing standard, bulk, and advanced orders, fulfilling regulatory requirements (textual, address, document, and action types), uploading supporting documents, and configuring webhook notifications.

## Buying a Phone Number

### Via Mission Control Portal

1. Navigate to **Real-Time Communication** > **Numbers** > **Buy Numbers** in the left sidebar.
2. Select your search criteria: Country (e.g., United States), Features (SMS, Voice, Fax, etc.), Number type (Local, Toll-Free, etc.), State/Region, and City/Area Code.
3. Click **Search**.
4. Choose a number from the results.
5. Click **Add to Cart** next to your chosen number.
6. Confirm the purchase by clicking **Place Order**.

### Via API

You can also purchase numbers programmatically:

```
# Search for available numbers
curl -X GET \
  --header "Authorization: Bearer your_api_key" \
  "https://api.telnyx.com/v2/available_phone_numbers?filter[country_code]=US&filter[locality]=Chicago"

# Purchase a specific number
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer your_api_key" \
  --data '{
    "phone_numbers": [{"phone_number": "+13125551234"}]
  }' \
  "https://api.telnyx.com/v2/number_orders"
```

### Next Steps

After purchasing your phone number, you will typically need to:

- **For Voice applications**: Assign it to a Voice API Application or SIP Connection.
- **For Messaging**: Configure it with a Messaging Profile.
- **For Fax**: Set up Fax Application settings.

## Number Orders

### Ordering Flow

1. **Search for phone numbers.** Use the [GET /available_phone_numbers](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) endpoint. Only phone numbers that were previously returned in a search request can be ordered.
2. **Create an order.** Use the [POST /number_orders endpoint](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order). In some countries, a requirement group must be included in the payload. See [Requirement Groups](requirement-groups--part-1.md) for more details.
3. **Regulatory Requirements.** If the order has no regulatory requirements, it should activate momentarily with no further user action. Otherwise, perform a [GET sub_number_orders/ request](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-sub-number-order) to see the regulatory requirements (in the `regulatory_requirements` array). Once you have collected the necessary information, perform a [PATCH /sub_number_orders/ request](https://developers.telnyx.com/api-reference/phone-number-orders/update-a-sub-number-orders-requirements) to associate that information to the number order.
4. **Handling Regulatory Requirement Rejections.** All regulatory requirements on an order are vetted individually. To check on the vetting status, perform a [GET /number_order_phone_numbers request](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-list-of-phone-numbers-associated-to-orders). If a rejection occurs:
   - Determine which regulatory requirement(s) was rejected.
   - [Review the comments](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-all-comments) on the order for a detailed explanation.
   - Update the order with corrections and resubmit for approval.

### Number Order vs Sub Number Order

Number Orders and Sub Number Orders share a parent-child relationship:

- **Number Order** = parent. Overarching order entity.
- **Sub Number Order** = child. Nested within the number order.

The `POST /number_orders` request always creates one number order, but it could be split into multiple sub number orders depending on the phone numbers being purchased. For example, an order containing 5 local numbers in Country A, 5 toll-free numbers in Country A, and 5 local numbers in Country B would result in 1 number order with 3 nested sub number orders. Sub number orders are processed independently.

### Order Statuses

Number orders / sub number orders have the following statuses:

| Status | Description |
| --- | --- |
| pending | Order was created and is being processed. Phone numbers are not yet active. |
| success | Order completed successfully. Phone numbers were activated. |
| failure | There was an issue with the order. |
| cancelled | The order was cancelled, either by the user or by the Telnyx team. |
| deleted | All phone numbers on the order have been deleted from the user account. |

When a number order / sub number order is in a `pending` status, the phone number status gives insight into the vetting process:

| Status | Description |
| --- | --- |
| requirement-info-pending | Order is missing values for one or more regulatory requirements. Customer needs to provide additional information before vetting can proceed. |
| requirement-info-under-review | Customer has provided values for all regulatory requirements. Order is awaiting vetting by Number Ops. |
| requirement-info-exception | One or more regulatory requirements have been rejected by Number Ops. Customer needs to review the rejections, make corrections, and resubmit. |
| approved | All requirements are approved. |
| deleted | All phone numbers on the order have been deleted from the user account. |

### Deadline and Auto Cancellation

Each order has a `deadline` attribute. Users are expected to have all regulatory requirements uploaded by the deadline, at which point the `deadline` is erased. Failure to provide all regulatory requirements by the deadline will result in auto-cancellation of the order. If one or more regulatory requirements are rejected, a new deadline will be set. Deadlines can be extended upon request via comment on the order.
