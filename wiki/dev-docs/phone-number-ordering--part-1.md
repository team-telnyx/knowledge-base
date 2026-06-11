---
title: Phone Number Ordering
summary: 'Covers the full lifecycle of purchasing phone numbers on Telnyx: searching
  available inventory, reserving numbers, placing standard and bulk orders, submitting
  advanced orders for unavailable inventory, and fulfilling regulatory requirements
  including document uploads, address verification, and action-based requirements.'
sources:
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement
  content_hash: 194284493f4275a91cd6a69695db20aff80d3695d3556b174c6d96c1ac0f6794
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders
  content_hash: 0893f3b3bc0112023a81b0c8347cfe0ad2cbd9868ea3573273e7a78b493492c5
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering
  content_hash: b66e9570f7398ca1d3736b624fb9f1e83a9725588fcbfbb283547944750511e6
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number
  content_hash: 5bab8250056deae19ea7817efc50461181f101f6c31a7cfbd629b0852a5173fa
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/documents/index
  content_hash: 3277fcc67447b29b6ae5820f692a92c5706ae74180cc544036bdfc551e0809ca
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started/index
  content_hash: 76945830bfb04d1f8e4bb7165fb475ba0a69484ca57acfec398ce213820e74ed
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders
  content_hash: fc7af7ca383294f80ff65f6f0a31dc8014116fa6bcab42c3f5e75dcba4debbf0
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations/index
  content_hash: 89086770a905d33690e4408df18db723412b6d373b56f9521039d05ef8080bce
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search/index
  content_hash: c1cde34f5be639fad90f9a7ff8bd7b3ae57244ae8abb76feef85ce303e753314
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements/index
  content_hash: facaf4447ed699744cf225a3cb4adfd40249a2e7096b134fd33e1a5031910be9
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups
  content_hash: d58c9e9db27b4afd9fbce178ae2c0f5b1b8519e99c2ec63d4610932d85404ed1
updated_at: 2026-06-11T10:39:50Z
---

# Phone Number Ordering

*Part 1 of 3 — see also: [Part 2](phone-number-ordering--part-2.md), [Part 3](phone-number-ordering--part-3.md)*

Covers the full lifecycle of purchasing phone numbers on Telnyx: searching available inventory, reserving numbers, placing standard and bulk orders, submitting advanced orders for unavailable inventory, and fulfilling regulatory requirements including document uploads, address verification, and action-based requirements.

## Coverage

Telnyx sells phone numbers in 100+ countries across multiple phone number types. Use the [Get Country Coverage API](https://developers.telnyx.com/api-reference/country-coverage/get-country-coverage) to see supported countries, available number types, applicable attributes, and whether inventory coverage is supported. When inventory coverage is supported, the [Inventory Coverage API](https://developers.telnyx.com/api-reference/inventory-level/create-an-inventory-coverage-request) can assess how many numbers are available based on your search criteria.

## Number Search

Use the `GET /v2/available_phone_numbers` endpoint to find phone numbers available for purchase. Only numbers returned in a recent search can be ordered.

### Search Constraints

- Country code is always required; other filters are optional.
- Wildcard characters (`*`, `%`, etc.) are not supported and will yield zero results.
- Search results may be limited depending on your [account verification level](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/index#account-levels-and-capabilities).

### Required Filters

- **Country Code** (`filter[country_code]`): ISO 3166 two-letter country code.

### Standard Filters

- **Feature** (`filter[features]`): Filter by capability (e.g., `sms`, `emergency`).
- **Type** (`filter[phone_number_type]`): e.g., `local`, `toll_free`.
- **Area Code** (`filter[national_destination_code]`): e.g., `205`.
- **City / Region** (`filter[locality]`): e.g., `Boston`.
- **State / Province** (`filter[administrative_area]`): US/CA only, e.g., `MA`.

### Advanced Filters

- **Starts with** (`filter[starts_with]`): Never include the country code. If using the area code filter, omit the area code digits from this value.
- **Ends with** (`filter[ends_with]`)
- **Contains** (`filter[contains]`)
- **Consecutive Numbers** (`filter[consecutive]`)
- **Results Limit** (`filter[limit]`)
- **Best Effort** (`filter[best_effort]`): US/CA only. Returns similar results when exact matches are unavailable.
- **Quickship** (`filter[quickship]`): US toll-free only. Returns pre-provisioned numbers ready for immediate activation. Without quickship, toll-free numbers can take up to 2 business days to activate.
- **Reservable** (`filter[reservable]`): Returns numbers eligible for reservation.
- **Exclude Held Numbers** (`filter[exclude_held_numbers]`): Excludes numbers in hold status from results.
- **Held / Reserved** (`filter[only_reserved_numbers]`): Returns numbers set aside for the requesting customer.

### Best Practices

- Use the inventory coverage API to list possible values for filters like area code and city.
- Use the `features` filter to match capabilities to your use case.
- For US toll-free numbers, use `filter[quickship]=true` for immediate activation.
- Review the `cost_information` object in search results before purchasing.

## Number Reservations

The Phone Number Reservations API lets you reserve numbers for 30 minutes, giving you exclusive rights to search for and order them. After 30 minutes the number returns to the available pool.

### Reservation Constraints

- Not all phone numbers are reservable.
- Reservations expire after 30 minutes.

### Reservation Flow

1. **Search for reservable numbers**: Add `filter[reservable]=true` and `filter[exclude_held_numbers]=true` to your search.
2. **Create a reservation**: `POST /v2/number_reservations`. Each number is individually attempted; some may fail. The overall status will be `partial_success` if any fail.
3. **List reservations**: `GET /v2/number_reservations`.
4. **Extend a reservation**: `POST /v2/number_reservations/:id/actions/extend` adds another 30 minutes.

Key response attributes include `id` (reservation ID), `status` (overall status), `phone_numbers[].status` (per-number status), and `phone_numbers[].expired_at` (per-number expiration).

## Standard Number Orders

### Ordering Flow

1. **Search for phone numbers** using `GET /v2/available_phone_numbers`.
2. **Create an order** using `POST /v2/number_orders`. Some countries require a requirement group in the payload.
3. **Fulfill regulatory requirements**: If the order has regulatory requirements, retrieve them via `GET /v2/sub_number_orders/:id` and submit values via `PATCH /v2/sub_number_orders/:id`.
4. **Handle rejections**: Check the vetting status via `GET /v2/number_order_phone_numbers`. If rejected, review comments, correct the information, and resubmit.

If an order has no regulatory requirements, it activates immediately with no further action.

### Number Orders vs Sub Number Orders

A `POST /v2/number_orders` creates one number order (parent), which may be split into multiple sub number orders (children) based on country and phone number type combinations. Sub number orders are processed independently.

### Order Statuses

| Status | Description |
|---|---|
| pending | Order created and being processed. Numbers not yet active. |
| success | Order completed. Numbers activated. |
| failure | There was an issue with the order. |
| cancelled | Order was cancelled by the user or Telnyx. |
| deleted | All numbers on the order have been deleted from the account. |

### Phone Number Statuses (while order is pending)

| Status | Description |
|---|---|
| requirement-info-pending | Missing values for one or more regulatory requirements. |
| requirement-info-under-review | All requirement values provided; awaiting vetting. |
| requirement-info-exception | One or more requirements rejected. Corrections needed. |
| approved | All requirements approved. |
| deleted | All numbers on the order deleted from the account. |

### Deadline and Auto-Cancellation

Each order has a `deadline` attribute. All regulatory requirements must be uploaded by the deadline. Failure to do so results in auto-cancellation. If requirements are rejected, a new deadline is set. Deadlines can be extended upon request via a comment on the order.

### Buying via Mission Control Portal

1. Navigate to **Real-Time Communication > Numbers > Buy Numbers**.
2. Select search criteria (country, features, number type, state/region, city/area code).
3. Click **Search**.
4. Choose a number and click **Add to Cart**.
5. Confirm the purchase by clicking **Place Order**.
