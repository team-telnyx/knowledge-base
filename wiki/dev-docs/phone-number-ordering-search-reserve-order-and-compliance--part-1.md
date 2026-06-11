---
title: 'Phone Number Ordering: Search, Reserve, Order, and Compliance'
summary: A consolidated guide to finding, reserving, and purchasing Telnyx phone numbers,
  including regulatory requirements, requirement groups, action-based verifications,
  documents, advanced orders, bulk ordering, statuses, deadlines, notifications, and
  post-activation steps.
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
updated_at: 2026-05-20T09:21:49Z
---

# Phone Number Ordering: Search, Reserve, Order, and Compliance

*Part 1 of 2 — see also: [Part 2](phone-number-ordering-search-reserve-order-and-compliance--part-2.md)*

A consolidated guide to finding, reserving, and purchasing Telnyx phone numbers, including regulatory requirements, requirement groups, action-based verifications, documents, advanced orders, bulk ordering, statuses, deadlines, notifications, and post-activation steps.

## End-to-End Ordering Workflow

- Search inventory using GET v2/available_phone_numbers. Only numbers returned in a recent search can be ordered.
- Optionally reserve numbers for 30 minutes to hold them while you order.
- Create a number order with POST v2/number_orders. In some countries, include a fulfilled requirement group.
- Fulfill any regulatory requirements (text, address, document, or action). Orders without requirements typically activate quickly.
- Monitor order and phone number statuses, handle any rejections, and meet deadlines to avoid auto-cancellation.

## Searching for Numbers

Use GET v2/available_phone_numbers to discover purchasable numbers.

Constraints
- A country code (ISO 3166-1 alpha-2) is required.
- Numbers must have appeared in a recent search to be orderable.
- Wildcards are not supported in filters.
- Results may be limited by your account verification level.

Best practices and filters
- Use the Inventory Coverage API to preview feasible filter values (e.g., area codes, cities) and estimate availability.
- Filter by features (e.g., sms, emergency) to match capabilities to your use case.
- For US toll-free, filter[quickship]=true returns pre-provisioned numbers ready for immediate use (non-quickship may take up to 2 business days to activate).
- Review the cost_information object in search results before ordering.
- Helpful filters include: phone_number_type (local, toll_free, etc.), national_destination_code (area code), locality (city/region), administrative_area (US/CA state/province), starts_with, ends_with, contains, consecutive, limit.
- Discovery and holding filters: reservable (only reservable numbers), exclude_held_numbers, only_reserved_numbers (numbers on hold/reserved for you).

References
- Search guide: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search
- API: https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers
- Inventory coverage: https://developers.telnyx.com/api-reference/inventory-level/create-an-inventory-coverage-request

## Reserving Numbers

Reservations hold numbers exclusively for you for 30 minutes.

Flow
- Search with filter[reservable]=true and filter[exclude_held_numbers]=true to find reservable numbers.
- Reserve using POST v2/number_reservations. The response includes overall status, per-number status, and expired_at per number. Partial successes are possible.
- List reservations: GET v2/number_reservations.
- Extend a reservation by 30 minutes: POST v2/number_reservations/{id}/actions/extend.

References
- Guide: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations
- API: https://developers.telnyx.com/api-reference/phone-number-reservations/create-a-number-reservation

## Placing Number Orders (API)

- Create: POST v2/number_orders (include numbers found via search). In certain countries, include requirement_group_id per phone number.
- View and manage regulatory requirements per sub order:
  - Retrieve a sub order and its regulatory_requirements: GET v2/sub_number_orders/{id}.
  - Provide values: PATCH v2/sub_number_orders/{id}.
- Parent/child model:
  - Number Order (parent) may contain multiple Sub Number Orders (children), split by attributes such as country and number type. Sub orders process independently.

References
- Guide: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders
- Create order API: https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order
- Sub orders API: https://developers.telnyx.com/api-reference/phone-number-orders/list-sub-number-orders

## Regulatory Requirements and Fulfillment

Regulatory requirements vary by country, phone number type, and action (ordering vs porting). Use GET /requirements to discover what’s needed for a given combination.

Requirement types
- textual: Provide a string value that meets acceptance_criteria if present.
- address: Provide an address_id created via POST v2/addresses (not a free-form string address).
- document: Provide a document_id uploaded via POST /documents.
- action: An external step (e.g., third-party verification). See Action Requirements below.

Notes
- Requirements evolve over time; always re-check current requirements.
- You can fulfill on each order directly or reuse a [Requirement groups](requirement-groups.md).

References
- Overview: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements
- Requirements API: https://developers.telnyx.com/api-reference/requirements/list-all-requirements
- Requirement types API: https://developers.telnyx.com/api-reference/requirement-types/retrieve-a-requirement-types
- Addresses API: https://developers.telnyx.com/api-reference/addresses/creates-an-address

## Requirement Groups (Pre-filling and Pre-Approval)

Requirement groups let you pre-fill and reuse regulatory data for a specific country_code, phone_number_type, and action.

Key points and constraints
- Optional in most countries; mandatory for orders in CH, DK, IT, NO, PT, SE.
- A "fulfilled" group has values for every required field. Mandatory countries require fulfilled groups at order time.
- Groups only apply to matching orders (country/type/action). Updates do not auto-sync to existing orders; re-apply via API to update an order.

Statuses
- unapproved, pending-approval, approved, declined, expired, no-longer-eligible (cannot be used).

Pre-approval (optional)
- Submit groups for pre-approval so orders using them can auto-activate within minutes.
- Not supported in all countries (e.g., Italy). Address validations must align with ordered numbers (e.g., area-code match where required; national address must be in-country). If misaligned, standard review occurs.

How to use
- Create: POST v2/requirement_groups.
- Inspect requirements: GET v2/requirement_groups or GET v2/requirement_groups/{id}.
- Fulfill: PATCH v2/requirement_groups/{id} (supply requirement_id -> value pairs).
- Associate with orders:
  - New number orders: include requirement_group_id per phone number in POST v2/number_orders.
  - Existing pending sub orders: POST v2/sub_number_orders/{id}/requirement_group (fulfilled groups only; approved fields on the order are not overwritten).
  - Porting orders: PATCH v2/porting_orders/{id} with requirement_group_id (overwrites existing values).
- Submit for pre-approval: POST v2/requirement_groups/{id}/submit_for_approval.
- Discuss via comments (comment_record_type=requirement_group).

References
- Guide: https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups

## Action Requirements (External Verification)

Some orders require external actions instead of documents/text. These are fulfilled via specialized flows.

Australia mobile ID verification (Onfido)
- Requirement ID: b7c72fb8-fa08-4529-aaf6-b9117d3f3698.
- Flow:
  1) Generate a unique verification link via the external requirements endpoint for sub number orders (include first_name, last_name).
  2) Share the returned URL (requirement_action.value) with the end user to complete Onfido verification.
  3) Upon approval, the requirement auto-completes; the order’s requirements_met becomes true, allowing it to proceed.

References
- Overview: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement
- Onfido: https://onfido.com/
