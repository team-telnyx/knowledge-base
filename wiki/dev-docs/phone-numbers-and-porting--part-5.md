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

*Part 5 of 11 — see also: [Part 1](phone-numbers-and-porting--part-1.md), [Part 2](phone-numbers-and-porting--part-2.md), [Part 3](phone-numbers-and-porting--part-3.md), [Part 4](phone-numbers-and-porting--part-4.md), [Part 6](phone-numbers-and-porting--part-6.md), [Part 7](phone-numbers-and-porting--part-7.md), [Part 8](phone-numbers-and-porting--part-8.md), [Part 9](phone-numbers-and-porting--part-9.md), [Part 10](phone-numbers-and-porting--part-10.md), [Part 11](phone-numbers-and-porting--part-11.md)*

This page consolidates Telnyx developer documentation covering phone number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in and port-out workflows, and the notifications and events that track them. It provides an end-to-end reference for purchasing numbers, fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and monitoring the lifecycle of those operations via webhooks and events.

## Requirement Groups

Requirement groups allow you to view, manage, and fulfill regulatory requirements in advance for a particular order type. By creating a requirement group, you can pre-fill all necessary information and documentation just once, and then reuse this group across multiple orders. Each requirement group is specific to a combination of `country_code`, `phone_number_type`, and `action` (ordering or porting).

### Constraints

- Requirement groups are optional in most countries. You can fulfill requirements individually on each order or use requirement groups to pre-fill requirements.
- In the following countries, it is mandatory to use fulfilled requirement groups when placing a number order: CH (Switzerland), DK (Denmark), IT (Italy), NO (Norway), PT (Portugal), and SE (Sweden).
- A fulfilled requirement group means that every requirement in the group has an associated value. You cannot create an order with an empty requirement group in countries where requirement groups are mandatory.
- Requirement groups can only be associated with orders that match the group's `country_code`, `phone_number_type`, and `action` combination.
- Number orders do not automatically synchronize with requirement group changes. You must make another API request to apply updated requirement group values to existing orders.

### Requirement Group Statuses

| Status | Description |
| --- | --- |
| unapproved | Default status after creation. Has not been submitted for pre-approval. Orders using this group go through standard review. |
| pending-approval | Submitted and under review. Orders using this group go through standard review. |
| approved | Passed review. Orders using this group activate automatically within a few minutes. |
| declined | One or more requirements were rejected during pre-approval. Orders using this group go through standard review. |
| expired | Requirement(s) exceeded validity window. Orders using this group go through standard review. |
| no-longer-eligible | Regulatory requirements have changed. Cannot be used for orders. Create a new requirement group with current requirements. |

### Pre-approval

By default, orders using requirement groups go through standard review, where Number Ops manually reviews the requirements on each individual order after it is placed. Pre-approval is an optional feature that allows you to submit a requirement group for review before placing orders. Once a requirement group is pre-approved, orders using it can activate automatically within a few minutes, bypassing the standard review process.

Pre-approval makes sense when you will reuse the same requirement group for multiple orders AND you need quick number activation. If you're only using a requirement group for a few orders or don't need immediate activation, you can skip pre-approval entirely.

**Pre-approval limitations:**

- **Country coverage**: Requirement group pre-approval is supported in most countries, but not all. Some countries, such as Italy, do not support pre-approval.
- **Address validation**: If the requirement group has an address requirement, ensure that ordered phone numbers comply with that address requirement. For example, if the requirement specifies an address matching the DID area code and the approved address is in Munich, order a phone number in Munich. Ordering a number in a different area will cause the order to undergo standard review instead of immediate activation.

### How It Works

**Step 1: Create a requirement group.** Use the [POST /v2/requirement_groups endpoint](/api-reference/requirement-groups/create-a-new-requirement-group) to create a requirement group. Each group requires `country_code` (ISO Alpha-2 format), `phone_number_type` (`local`, `toll_free`, `national`, `mobile`, or `shared_cost`), and `action` (`ordering` or `porting`). Optionally include a `customer_reference` to label the requirement group for your own tracking purposes.

**Step 2: View the requirement group.** List all requirement groups using [GET /v2/requirement_groups](/api-reference/requirement-groups/list-requirement-groups), or retrieve a specific group by ID using [GET /v2/requirement_groups/:id](/api-reference/requirement-groups/get-a-single-requirement-group-by-id). The `regulatory_requirements` array lists each requirement that needs to be fulfilled.

**Step 3: Fulfill the requirement group.** Update the requirement group with values using [PATCH /v2/requirement_groups/:id](/api-reference/requirement-groups/update-requirement-values-in-requirement-group). In the request body, specify each `requirement_id` and its associated value.

**Step 4: Associate the requirement group with an order.**

- **For new number orders:** First, search for available phone numbers and identify the number(s) you would like to purchase. Then create a number order using [POST /v2/number_orders](/api-reference/phone-number-orders/create-a-number-order), including the `requirement_group_id` in each `phone_number` object.
- **For existing pending sub number orders:** Update a `pending` sub number order using [POST /v2/sub_number_orders/:id/requirement_group](https://developers.telnyx.com/api-reference/requirement-groups/update-requirement-group-for-a-sub-number-order). Include the `requirement_group_id` in the request body. The requirement group must be fulfilled. The request will only update non-approved requirements.
- **For porting orders:** Associate a requirement group with a porting order using [PATCH /v2/porting_orders/:id](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order), including the `requirement_group_id` in the request body. This request can be performed when the order is in `draft`, `in-process`, or `exception` status.

**Step 5 (Optional): Submit for pre-approval.** To submit a requirement group for pre-approval, use the [POST /v2/requirement_groups/:id/submit_for_approval endpoint](/api-reference/requirement-groups/submit-a-requirement-group-for-approval). The requirement group will transition to `pending-approval` status after submission. If all requirements are met, the group's `status` is set to `approved`. If requirements are rejected, the status will move to `declined`. If the requirement group is rejected, Number Ops will communicate feedback via comments on the requirement group.
