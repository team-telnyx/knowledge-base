---
title: Phone Number Ordering
summary: 'Covers the full lifecycle of purchasing phone numbers on Telnyx: searching
  available inventory, reserving numbers, placing standard and bulk orders, submitting
  advanced orders for unavailable inventory, and fulfilling regulatory requirements
  including document uploads, address verification, and action-based requirements.'
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
