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

*Part 8 of 11 — see also: [Part 1](phone-numbers-and-porting--part-1.md), [Part 2](phone-numbers-and-porting--part-2.md), [Part 3](phone-numbers-and-porting--part-3.md), [Part 4](phone-numbers-and-porting--part-4.md), [Part 5](phone-numbers-and-porting--part-5.md), [Part 6](phone-numbers-and-porting--part-6.md), [Part 7](phone-numbers-and-porting--part-7.md), [Part 9](phone-numbers-and-porting--part-9.md), [Part 10](phone-numbers-and-porting--part-10.md), [Part 11](phone-numbers-and-porting--part-11.md)*

This page consolidates Telnyx developer documentation covering phone number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in and port-out workflows, and the notifications and events that track them. It provides an end-to-end reference for purchasing numbers, fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and monitoring the lifecycle of those operations via webhooks and events.

## Port-in Extended Numbers

Phone number extensions allow multiple phone lines to branch off from a single direct inward dialing (DID) number or main line. The system has two components:

- **Route number**: The primary phone number (also called the "main" number) that serves as the gateway for incoming calls before they are directed to specific extensions.
- **Extended numbers**: Short digit sequences appended to the route number that connect callers directly to specific endpoints.

For example, if the route number is `+49 20 12345678`, extensions might include `+49 20 123456780` or `+49 20 1234567806`.

### Constraints

- Extended number porting is currently only available for German port orders.
- Extensions can only be added while the porting order is in `draft`, `in-process`, or `exception` status.
- The maximum extension range is `0` to `999`.
- Activation ranges must be equal to or a subset of the extension range.
- Activation ranges cannot overlap.

### Extension Range and Activation Ranges

Extensions are created in blocks defined by two parameters:

- **`extension_range`**: Represents the full range of extensions available for the route number. This typically covers 10 numbers (`0`-`9`), 100 numbers (`0`-`99`), or 1000 numbers (`0`-`999`).
- **`activation_ranges`**: Specifies which extensions within the `extension_range` should be active immediately upon port completion.

### How It Works

**Step 1: Create a porting order with the route number.** Create a porting order that includes the route number (the main DID). Do not include the extended numbers in the initial order.

**Step 2: Retrieve the porting phone number ID.** Use the [List all porting phone numbers](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-phone-numbers) endpoint to retrieve the `porting_phone_number_id` for your route number.

**Step 3: Add extensions to the porting order.** Use the [Create a phone number extension](https://developers.telnyx.com/api-reference/porting-orders/create-a-phone-number-extension) endpoint to attach extensions to your porting order. Provide the `porting_phone_number_id`, `extension_range`, and `activation_ranges` in your request.

**Step 4: Submit the porting order.** Once extensions are attached, submit your porting order through the standard porting workflow.

## Messaging and Porting

For local and toll-free phone numbers in the US and Canada, porting voice and porting messaging are two separate processes. A porting order transitioning to `ported` status indicates that voice has ported to Telnyx, but this status does not reflect the state of messaging.

Messaging routing is controlled by a NetNumber ID (NNID), which identifies the provider that owns SMS routing for a telephone number. At the FOC date and time, the losing carrier is expected to release the NNID so messaging routes through the winning carrier. In most cases, both voice and messaging port simultaneously. However, if the losing carrier fails to release the NNID, messaging continues to route through them even after voice has ported.

### Constraints

- Messaging porting tracking is only applicable to US and Canada local and toll-free phone numbers.
- The `messaging_capable` attribute must be `true` on the porting order to enable messaging tracking.
- A `messaging_profile_id` must be assigned to the porting order when enabling messaging activation.
- Phone numbers ported from other countries have messaging port simultaneously with voice.

### Messaging Port Statuses

The `messaging_port_status` field tracks messaging activation independently from the porting order's main `status` field:

| Status | Description |
| --- | --- |
| `pending` | Messaging activation is enabled but the porting order has not yet reached the FOC date and time. |
| `activating` | The porting order has ported and Telnyx is verifying messaging activation. |
| `ported` | Messaging has successfully ported to Telnyx. |
| `exception` | Messaging failed to port automatically and Telnyx is escalating with the losing carrier. |
| `not_applicable` | Messaging activation was not enabled for this porting order. |

### How It Works

**Step 1: Verify messaging capability.** Check the `messaging_capable` attribute on your porting order or portability check response.

**Step 2: Enable messaging activation.** Update the porting order using the [PATCH /v2/porting_orders/](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order) endpoint. Set `enable_messaging` to `true` in the `messaging` object. You must also assign a `messaging_profile_id` in the `phone_number_configuration` object.

**Step 3: Monitor messaging port status.** Prior to the FOC date and time, the order reflects `messaging_port_status: pending`. Once the porting order transitions to `ported` status, the messaging port status changes to `activating` while Telnyx verifies messaging activation.

**Step 4: Handle exceptions.** If the losing carrier fails to release messaging, the status changes to `exception`. When this occurs, the Telnyx Messaging Ops team is automatically notified and escalates with the losing carrier. Resolution typically occurs within 72 hours for local numbers and up to 5 business days for toll-free numbers.

### Partial Messaging Ports

When a porting order contains multiple phone numbers, it is possible for some numbers to port messaging successfully while others do not. If any phone number on the order fails to port messaging, the order-level `messaging_port_status` is `exception`. To check the messaging port status of individual phone numbers, use the [GET /v2/porting_orders//associated_phone_numbers](https://developers.telnyx.com/api-reference/porting-orders/list-all-associated-phone-numbers) endpoint.

### Hosted SMS Alternative

To avoid potential messaging downtime during porting, you can port SMS to Telnyx before porting voice by submitting a Hosted SMS request. This approach ensures messaging is active on Telnyx before the FOC date and time. The hosted SMS workflow involves:

- Submitting a Hosted SMS request for your phone numbers at least 4 business days before the scheduled FOC date.
- Creating a porting order with a FOC date at least 4 business days in the future.
- Once the Hosted SMS request completes, SMS routes through Telnyx while voice remains with the losing carrier.
- When the FOC date arrives, voice ports and both services route through Telnyx with no downtime.
