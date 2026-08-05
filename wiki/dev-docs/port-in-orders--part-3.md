---
title: Port-in orders
summary: Port-in orders transfer existing phone numbers from another carrier to Telnyx.
  This page covers the end-to-end port-in workflow via the V2 porting API, including
  creating and submitting orders, requesting FOC dates, on-demand activations, block
  and extension porting, bundle pre-configuration, messaging activation, cancellation,
  and webhook notifications and events.
sources:
- url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
updated_at: 2026-08-05T14:01:21Z
---

# Port-in orders

*Part 3 of 8 — see also: [Part 1](port-in-orders--part-1.md), [Part 2](port-in-orders--part-2.md), [Part 4](port-in-orders--part-4.md), [Part 5](port-in-orders--part-5.md), [Part 6](port-in-orders--part-6.md), [Part 7](port-in-orders--part-7.md), [Part 8](port-in-orders--part-8.md)*

Port-in orders transfer existing phone numbers from another carrier to Telnyx. This page covers the end-to-end port-in workflow via the V2 porting API, including creating and submitting orders, requesting FOC dates, on-demand activations, block and extension porting, bundle pre-configuration, messaging activation, cancellation, and webhook notifications and events.

## Port-in blocks

Block porting allows you to port consecutive groups of phone numbers (blocks) from another carrier to Telnyx. Unlike porting individual phone numbers, block porting handles entire ranges of numbers that are assigned together by carriers.

Phone number blocks are groups of consecutive phone numbers—typically 10, 100, or 1,000 numbers in sequence—assigned to a specific area or provider. Carriers manage these blocks as units, which means porting rules differ from individual numbers. Some countries require the entire block to be ported even if only some numbers are active.

By indicating that you are porting a block (rather than individual numbers), Telnyx can apply the correct processing rules and help you avoid rejections or exceptions during the porting process.

### Constraints

- Block porting is currently only available for **Germany (DE)** port orders.
- The maximum size for a single block is 1,000 phone numbers (`0` - `999`).
- Activation ranges must be equal to or a subset of the phone number range.
- Activation ranges cannot overlap with each other.
- When adding a block to an existing order, the block must match the order's country and phone number type.
- Blocks can only be added or deleted when the order is in `draft`, `in-process`, or `exception` status.

### Phone number range and activation ranges

When porting a block, you specify two key components:

- **Phone number range**: The complete block of consecutive numbers being ported. This defines the full range that will transfer to Telnyx and must be included in the Letter of Authorization (LOA). Block sizes are typically 10, 100, or 1,000 numbers.
- **Activation ranges**: The subset of numbers within the block that you want active immediately upon port completion. Numbers in the phone number range but not in any activation range will still port to your account but remain inactive.

This separation is useful when a country requires full-block porting but you only need certain numbers active. For example, if you own a 1,000-number block but only use 776 of them, you can port the entire block while activating only the numbers you need.

You can specify multiple activation ranges within a single block. For instance, if you need numbers `000`-`064` and number `087` active, you would define two separate activation ranges.

### How it works

**Step 1: Create a port order with blocks.** Use the [POST /v2/porting_orders endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-porting-order) to create an order. Include a `phone_number_blocks` array with:

- `phone_number_range`: The `start_at` and `end_at` values defining the complete block.
- `activation_ranges`: An array specifying which numbers to activate upon completion.

Both range values must be in E.164 format.

**Step 2: Add blocks to an existing order (if needed).** If you created an order for individual numbers that were rejected because they belong to a block, you can add the block to your existing order rather than starting over. Use the [POST /v2/porting_orders/{id}/phone_number_blocks endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-phone-number-block) to add a block. Any phone numbers already on the order that fall within the block range will be incorporated automatically.

**Step 3: View blocks on your order.** Use the [GET /v2/porting_orders/{id}/phone_number_blocks endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-phone-number-blocks) to view all blocks associated with your order. Each block has a unique `id`. When you query porting phone numbers using the [List porting phone numbers endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-phone-numbers), numbers that belong to a block include a `block_reference_id` field linking them to their block.

**Step 4: Remove a block (if needed).** Use the [DELETE /v2/porting_orders/{id}/phone_number_blocks/{block_id} endpoint](https://developers.telnyx.com/api-reference/porting-orders/delete-a-phone-number-block) to remove a block from an order. When you delete a block, the individual phone numbers remain on the order—only the block grouping is removed.
