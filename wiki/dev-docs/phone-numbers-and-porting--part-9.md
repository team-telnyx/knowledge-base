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

*Part 9 of 11 — see also: [Part 1](phone-numbers-and-porting--part-1.md), [Part 2](phone-numbers-and-porting--part-2.md), [Part 3](phone-numbers-and-porting--part-3.md), [Part 4](phone-numbers-and-porting--part-4.md), [Part 5](phone-numbers-and-porting--part-5.md), [Part 6](phone-numbers-and-porting--part-6.md), [Part 7](phone-numbers-and-porting--part-7.md), [Part 8](phone-numbers-and-porting--part-8.md), [Part 10](phone-numbers-and-porting--part-10.md), [Part 11](phone-numbers-and-porting--part-11.md)*

This page consolidates Telnyx developer documentation covering phone number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in and port-out workflows, and the notifications and events that track them. It provides an end-to-end reference for purchasing numbers, fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and monitoring the lifecycle of those operations via webhooks and events.

## Bundles with Porting Orders

Bundle pre-configuration allows you to associate bundles with phone numbers on a porting order before those numbers are active at Telnyx. When the port completes and the phone numbers become active, the pre-configured bundles are automatically applied.

### Constraints

- Bundle pre-configuration is only available via API.
- Bundles can be pre-configured or updated at any point before the porting order reaches `ported` or `cancelled` status.
- Each bundle can only be associated with one phone number.
- You can pre-configure up to 20 phone numbers per API request.
- The bundle must be valid for the specific phone number type and characteristics.
- Pre-configuring bundles is optional.

### How It Works

**Step 1: Verify available bundles.** Use the [GET /v2/bundle-pricing/user_bundles endpoint](https://developers.telnyx.com/api-reference/user-bundles/get-user-bundles) to list your bundles. A bundle is available for pre-configuration if its `resources` array is empty.

**Step 2: Get porting phone number IDs.** Each phone number on a porting order has a unique `porting_phone_number_id`. Use the [GET /v2/porting_phone_numbers endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-phone-numbers) with a filter for your porting order ID to retrieve the list of phone numbers and their associated IDs.

**Step 3: Pre-configure bundles.** Use the [POST /v2/porting_orders/phone_number_configurations endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-list-of-phone-number-configurations) to associate bundles with porting phone numbers. Each configuration requires a `porting_phone_number_id` and a `user_bundle_id`.

**Step 4: Verify configurations.** Use the `GET /v2/porting_orders/phone_number_configurations` endpoint with your porting order ID to view which bundles are pre-configured with which phone numbers.

## Port-in Blocks

Block porting allows you to port consecutive groups of phone numbers (blocks) from another carrier to Telnyx. Phone number blocks are groups of consecutive phone numbers—typically 10, 100, or 1,000 numbers in sequence—assigned to a specific area or provider. Some countries require the entire block to be ported even if only some numbers are active.

### Constraints

- Block porting is currently only available for Germany (DE) port orders.
- The maximum size for a single block is 1,000 phone numbers (`0` - `999`).
- Activation ranges must be equal to or a subset of the phone number range.
- Activation ranges cannot overlap with each other.
- When adding a block to an existing order, the block must match the order's country and phone number type.
- Blocks can only be added or deleted when the order is in `draft`, `in-process`, or `exception` status.

### Phone Number Range and Activation Ranges

When porting a block, you specify two key components:

- **Phone number range**: The complete block of consecutive numbers being ported. This defines the full range that will transfer to Telnyx and must be included in the Letter of Authorization (LOA).
- **Activation ranges**: The subset of numbers within the block that you want active immediately upon port completion.

### How It Works

**Step 1: Create a port order with blocks.** Use the [POST /v2/porting_orders endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-porting-order) to create an order. Include a `phone_number_blocks` array with `phone_number_range` (the `start_at` and `end_at` values defining the complete block) and `activation_ranges` (an array specifying which numbers to activate upon completion). Both range values must be in E.164 format.

**Step 2: Add blocks to an existing order (if needed).** If you created an order for individual numbers that were rejected because they belong to a block, you can add the block to your existing order using the [POST /v2/porting_orders//phone_number_blocks endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-phone-number-block).

**Step 3: View blocks on your order.** Use the [GET /v2/porting_orders//phone_number_blocks endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-phone-number-blocks) to view all blocks associated with your order.

**Step 4: Remove a block (if needed).** Use the [DELETE /v2/porting_orders//phone_number_blocks/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/delete-a-phone-number-block) to remove a block from an order.

## Porting Additional Steps

After you create and populate a porting order, Telnyx may require additional steps depending on the phone numbers being ported and the details provided. These steps must be completed before you can submit the order. Additional steps differ from supplemental port order requirements, which cover documents and textual information needed for specific countries or number types. Additional steps involve actions or decisions that affect other phone numbers on your losing carrier's account.

### Checking for Additional Steps

The `additional_steps` array on a porting order indicates whether any additional steps are required:

- `[]` (empty array): No additional steps required. You can proceed with submission.
- `["associated_phone_numbers"]`: You must provide a list of phone numbers on your losing carrier's account that are not porting to Telnyx, and specify whether each should remain active or be deactivated after the port completes.

Retrieve the porting order using the [GET /v2/porting_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) and check the `additional_steps` field in the response.

### Associated Phone Numbers

This additional step applies to partial ports of GB local phone numbers. When porting only some phone numbers from an account, you must specify what happens to the remaining phone numbers on the losing carrier's account.

**When this step is required:** The `associated_phone_numbers` step appears when both conditions are met: the porting order is for GB local phone numbers, and the `port_type` is set to `partial_port`.

You must provide a list of phone numbers on your losing carrier's account that are not being ported to Telnyx. For each phone number or range, you must indicate one of two outcomes:

- **Keep**: The phone number remains active with the losing carrier after the port completes.
- **Disconnect**: The phone number is disconnected from the losing carrier after the port completes.

If the billing telephone number (BTN) is included in the port, all remaining number ranges can only be disconnected.

Use the [POST /v2/porting_orders//associated_phone_numbers endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-an-associated-phone-number) to specify ranges of phone numbers and their intended outcome. You can associate multiple number ranges by sending separate requests for each range.
