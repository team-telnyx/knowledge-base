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

*Part 2 of 3 — see also: [Part 1](phone-number-ordering--part-1.md), [Part 3](phone-number-ordering--part-3.md)*

Covers the full lifecycle of purchasing phone numbers on Telnyx: searching available inventory, reserving numbers, placing standard and bulk orders, submitting advanced orders for unavailable inventory, and fulfilling regulatory requirements including document uploads, address verification, and action-based requirements.

## Bulk Orders

Bulk number orders (inexplicit orders) let you purchase numbers by specifying search criteria and quantity without selecting specific numbers. The API automatically searches, reserves, and orders matching numbers in a single request.

### Bulk Order Constraints

- Only available for US and CA phone numbers.
- Maximum 10,000 numbers per bulk order.
- Availability is not guaranteed; depends on current inventory.
- Use the inventory coverage API to check levels before ordering.

### Ordering Groups

A single bulk order can include multiple ordering groups, each with different search criteria and strategies. Each group tracks its own `count_requested`, `count_allocated`, and `status` independently.

### Bulk Order Statuses

| Status | Description |
|---|---|
| pending | Queued and awaiting processing. |
| processing | Actively being processed. |
| success | Fully processed; all requested numbers ordered. |
| partial_success | Partially completed; some numbers unavailable. |
| failed | Could not be processed successfully. |

### Bulk Order Flow

1. **Create a bulk order**: `POST /v2/inexplicit_number_orders`. Each ordering group requires `country_iso` (US or CA), `count_requested`, and `phone_number_type`. Optionally include search filters. Specify a `strategy` — `always` (default, orders whatever is available) or `never` (only orders if full quantity can be fulfilled). You can also set `connection_id`, `messaging_profile_id`, `billing_group_id`, or `customer_reference`.
2. **Monitor order status**: Use `GET /v2/inexplicit_number_orders` (list) or `GET /v2/inexplicit_number_orders/:id` (retrieve). Compare `count_allocated` to `count_requested`.
3. **Access created number orders**: The `orders` array in the response lists `number_order_id` and `sub_number_order_ids`. Retrieve details using the standard number ordering APIs, then follow the standard workflow to complete any remaining steps.

## Advanced Orders

When Telnyx has coverage but no available numbers match your search, you can submit an Advanced Order. Telnyx's Number Operations team will attempt to acquire the numbers. This process is asynchronous and best-effort.

### Advanced Order Constraints

- Not eligible for US or CA toll-free numbers (the search API reflects all possible inventory).
- Not eligible for unique/specific phone numbers.
- Best effort only; fulfillment is not guaranteed.

### Advanced Order Statuses

| Status | Description |
|---|---|
| pending | Created but not yet being processed. |
| processing | Currently being processed by Telnyx. |
| exception | Issue with the order; review and resolve. |
| hold | Telnyx needs to replenish inventory; no action needed. |
| ordered | Successfully placed and fulfilled. |
| failed | Could not be completed. |

### Advanced Order Flow

1. **Search for phone numbers** using `GET /v2/available_phone_numbers`. If no results are returned, try adjusting filters.
2. **Create an Advanced Order**: `POST /v2/advanced_orders` with the same search parameters.
3. **Add regulatory requirements**: Create a [requirement group](phone-number-ordering-requirement-groups.md) matching the country and phone number type, then `PATCH /v2/advanced_orders/:order_id/requirement_group` with the `requirement_group_id`. Edit requirements on the requirement group first, then re-PATCH the order.
4. **Finish the process**: When the order transitions to `ordered`, check the `orders` array for Number Order IDs. Retrieve those orders with `GET /v2/number_orders/:number_order_id` and treat them as standard number orders.

### Advanced Order Comments

Communicate with the Number Operations team via the Comments API. Use `filter[comment_record_type]=advanced_number_order` and set the `comment_record_id` to the advanced order ID.

### Advanced Order Webhook Events

Advanced orders emit `advanced_order.status_update` events for status transitions and `advanced_order.new_comment` events for new comments. Configure notifications via the [notification settings guide](https://support.telnyx.com/en/articles/4277896-notification-settings).

## Regulatory Requirements

Some phone numbers require additional information before activation. Requirements are defined per country, phone number type, and action (ordering or porting). Use the `GET /v2/requirements` endpoint with filters to discover what is needed.

The API response contains two record types:
- `"record_type": "requirement"` — the parent record indicating the country/type/action combination.
- `"record_type": "requirement_type"` — the specific requirement to fulfill (e.g., proof of address).

### Requirement Type Classifications

Each requirement type has one of four classifications:

- **Textual**: Any string value (subject to acceptance criteria).
- **Address**: Must provide an address ID. Create an address via `POST /v2/addresses`, then pass the returned ID as the field value. You cannot write out the address as a string.
- **Document**: Must provide a document ID. Upload via `POST /v2/documents`, then pass the returned ID as the field value.
- **Action**: Requires the end user to complete an external action (e.g., identity verification). See the [Action Requirements](phone-number-ordering-action-requirements.md) section below.

To view detailed information about a requirement type (description, examples, acceptance criteria), use `GET /v2/requirement_types/:id`.
