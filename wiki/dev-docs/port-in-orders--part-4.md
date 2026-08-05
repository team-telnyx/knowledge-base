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

*Part 4 of 8 — see also: [Part 1](port-in-orders--part-1.md), [Part 2](port-in-orders--part-2.md), [Part 3](port-in-orders--part-3.md), [Part 5](port-in-orders--part-5.md), [Part 6](port-in-orders--part-6.md), [Part 7](port-in-orders--part-7.md), [Part 8](port-in-orders--part-8.md)*

Port-in orders transfer existing phone numbers from another carrier to Telnyx. This page covers the end-to-end port-in workflow via the V2 porting API, including creating and submitting orders, requesting FOC dates, on-demand activations, block and extension porting, bundle pre-configuration, messaging activation, cancellation, and webhook notifications and events.

## Port in extended numbers

Phone number extensions allow multiple phone lines to branch off from a single direct inward dialing (DID) number or main line. This setup is common in offices or call centers where individual desks or employees need unique extensions.

The system has two components:

- **Route number**: The primary phone number (also called the "main" number) that serves as the gateway for incoming calls before they are directed to specific extensions.
- **Extended numbers**: Short digit sequences appended to the route number that connect callers directly to specific endpoints like departments or individuals.

For example, if the route number is `+49 20 12345678`, extensions might include `+49 20 123456780` or `+49 20 1234567806`.

When porting extended numbers, you first create a porting order with the route number, then attach the extensions to that order before submission.

### Constraints

- Extended number porting is currently only available for German port orders.
- Extensions can only be added while the porting order is in `draft`, `in-process`, or `exception` status.
- The maximum extension range is `0` to `999`.
- Activation ranges must be equal to or a subset of the extension range.
- Activation ranges cannot overlap.

### Extension range and activation ranges

Extensions are created in blocks defined by two parameters:

- **`extension_range`**: Represents the full range of extensions available for the route number. This typically covers 10 numbers (`0`-`9`), 100 numbers (`0`-`99`), or 1000 numbers (`0`-`999`). All extensions within this range will port with the route number.
- **`activation_ranges`**: Specifies which extensions within the `extension_range` should be active immediately upon port completion. Extensions not included in `activation_ranges` will port but remain inactive on your account.

For example, if your route number is `+49 20 12345678` and you want to activate only extension `+49 20 123456784`:

- Set `extension_range` to `0`-`9` (covering `+49 20 123456780` through `+49 20 123456789`).
- Set `activation_ranges` to `4`-`4` (activating only `+49 20 123456784`).

For multiple non-contiguous extensions like `+49 20 1234567804`, `+49 20 1234567819`, `+49 20 1234567820`, and `+49 20 1234567842`:

- Set `extension_range` to `0`-`99`.
- Set `activation_ranges` to include `4`-`4`, `19`-`20`, and `42`-`42`.

### How it works

**Step 1: Create a porting order with the route number.** Create a porting order that includes the route number (the main DID). Do not include the extended numbers in the initial order.

**Step 2: Retrieve the porting phone number ID.** Use the [List all porting phone numbers](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-phone-numbers) endpoint to retrieve the `porting_phone_number_id` for your route number. You will need this ID to attach extensions.

**Step 3: Add extensions to the porting order.** Use the [Create a phone number extension](https://developers.telnyx.com/api-reference/porting-orders/create-a-phone-number-extension) endpoint to attach extensions to your porting order. Provide the `porting_phone_number_id`, `extension_range`, and `activation_ranges` in your request.

**Step 4: Submit the porting order.** Once extensions are attached, submit your porting order through the standard porting workflow. The route number and all extensions within the `extension_range` will port together.

### Manage extensions

**View extensions.** The route number appears in the [List all porting phone numbers](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-phone-numbers) response, but extended numbers do not. To view extensions attached to a porting order, use the [List all phone number extensions](https://developers.telnyx.com/api-reference/porting-orders/list-all-phone-number-extensions) endpoint.

**Delete extensions.** To remove extensions from a porting order before submission, use the [Delete a phone number extension](https://developers.telnyx.com/api-reference/porting-orders/delete-a-phone-number-extension) endpoint. The order must be in `draft`, `in-process`, or `exception` status.

## Bundles with porting orders

Bundle pre-configuration allows you to associate [bundles](https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing) with phone numbers on a porting order before those numbers are active at Telnyx. When the port completes and the phone numbers become active, the pre-configured bundles are automatically applied.

The term "pre-configure" is used because bundles are not actually applied to phone numbers until after the numbers port in and become active at Telnyx. During the porting process, the bundle association exists as a pending configuration that takes effect upon port completion.

### Constraints

- Bundle pre-configuration is only available via API.
- Bundles can be pre-configured or updated at any point before the porting order reaches `ported` or `cancelled` status, including shortly before the FOC date.
- Each bundle can only be associated with one phone number. If a pre-configured bundle is used elsewhere before the port completes, the assignment will fail.
- You can pre-configure up to 20 phone numbers per API request.
- The bundle must be valid for the specific phone number type and characteristics. Invalid bundle-number combinations will return an error.
- Pre-configuring bundles is optional. You can pre-configure bundles for some, all, or none of the phone numbers on a porting order.

### How it works

**Step 1: Verify available bundles.** Use the [GET /v2/bundle-pricing/user_bundles endpoint](https://developers.telnyx.com/api-reference/user-bundles/get-user-bundles) to list your bundles, or view them on the [Bundles page](https://portal.telnyx.com/#/app/bundles) in Mission Control Portal. A bundle is available for pre-configuration if its `resources` array is empty. Each bundle has eligibility criteria for which phone numbers it can be assigned to. To purchase additional bundles, visit the [Bundle Orders page](https://portal.telnyx.com/#/app/bundles/order).

**Step 2: Get porting phone number IDs.** Each phone number on a porting order has a unique `porting_phone_number_id` that you need for pre-configuration. Use the [GET /v2/porting_phone_numbers endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-phone-numbers) with a filter for your porting order ID to retrieve the list of phone numbers and their associated IDs.

**Step 3: Pre-configure bundles.** Use the [POST /v2/porting_orders/phone_number_configurations endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-list-of-phone-number-configurations) to associate bundles with porting phone numbers. Each configuration requires:

- `porting_phone_number_id`: The ID of the phone number on your porting order.
- `user_bundle_id`: The ID of the bundle to pre-configure.

**Step 4: Verify configurations.** Use the `GET /v2/porting_orders/phone_number_configurations` endpoint with your porting order ID to view which bundles are pre-configured with which phone numbers. When the port completes and phone numbers become active at Telnyx, the pre-configured bundles are automatically applied to the corresponding phone numbers.
