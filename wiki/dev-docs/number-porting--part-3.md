---
title: Number Porting
summary: Number porting at Telnyx covers both port-in orders (transferring phone numbers
  to Telnyx from another carrier) and port-out orders (when another carrier requests
  numbers away from your Telnyx account). The port-in process involves checking portability,
  creating and fulfilling orders, managing FOC dates, and optionally configuring messaging,
  bundles, extensions, and blocks. Port-out orders are initiated externally and require
  you to authorize or reject them. Both flows support webhook notifications and a
  queryable event history.
sources:
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
updated_at: 2026-06-11T10:40:42Z
---

# Number Porting

*Part 3 of 4 — see also: [Part 1](number-porting--part-1.md), [Part 2](number-porting--part-2.md), [Part 4](number-porting--part-4.md)*

Number porting at Telnyx covers both port-in orders (transferring phone numbers to Telnyx from another carrier) and port-out orders (when another carrier requests numbers away from your Telnyx account). The port-in process involves checking portability, creating and fulfilling orders, managing FOC dates, and optionally configuring messaging, bundles, extensions, and blocks. Port-out orders are initiated externally and require you to authorize or reject them. Both flows support webhook notifications and a queryable event history.

## Phone Number Extensions

Phone number extensions allow multiple lines to branch off a single DID (route number). This is common in offices or call centers.

- **Route number**: the primary/main number that serves as the gateway.
- **Extended numbers**: short digit sequences appended to the route number.

When porting extended numbers, you first create a porting order with the route number, then attach extensions before submission.

### Constraints

- Extended number porting is currently only available for German port orders.
- Extensions can only be added while the order is in `draft`, `in-process`, or `exception` status.
- Maximum extension range is `0` to `999`.
- Activation ranges must be equal to or a subset of the extension range.
- Activation ranges cannot overlap.

### Extension range and activation ranges

- **`extension_range`**: the full range of extensions available for the route number (e.g., `0`–`9` for 10 numbers, `0`–`99` for 100, `0`–`999` for 1,000). All extensions within this range port with the route number.
- **`activation_ranges`**: which extensions should be **active** immediately upon port completion. Extensions not in any activation range port but remain inactive.

For example, with route number `+49 20 12345678`, to activate only extension `+49 20 123456784`: set `extension_range` to `0`–`9` and `activation_ranges` to `4`–`4`. For non-contiguous extensions like `04`, `19`, `20`, and `42`: set `extension_range` to `0`–`99` and `activation_ranges` to `4`–`4`, `19`–`20`, `42`–`42`.

### Steps

1. Create a porting order with the route number only (not extended numbers).
2. Retrieve the route number's `porting_phone_number_id` via `GET /v2/porting_phone_numbers`.
3. Attach extensions using `POST /v2/porting_orders/{id}/phone_number_extensions` with `porting_phone_number_id`, `extension_range`, and `activation_ranges`.
4. Submit the porting order through the standard workflow.

### Managing extensions

- **View** – Extended numbers don't appear in the porting phone numbers list. Use `GET /v2/porting_orders/{id}/phone_number_extensions` to view them.
- **Delete** – Use `DELETE /v2/porting_orders/{id}/phone_number_extensions/{extension_id}`. The order must be in `draft`, `in-process`, or `exception` status.

## Block Porting

Block porting handles consecutive groups of phone numbers (blocks) from another carrier. Phone number blocks are typically 10, 100, or 1,000 consecutive numbers. By indicating you are porting a block, Telnyx applies the correct processing rules and helps avoid rejections.

### Constraints

- Currently only available for **Germany (DE)** port orders.
- Maximum single block size: 1,000 numbers (`0`–`999`).
- Activation ranges must be equal to or a subset of the phone number range.
- Activation ranges cannot overlap.
- When adding a block to an existing order, it must match the order's country and phone number type.
- Blocks can only be added or deleted when the order is in `draft`, `in-process`, or `exception` status.

### Phone number range and activation ranges

- **Phone number range**: the complete block being ported (defined by `start_at` and `end_at` in E.164 format). This full range must be included in the LOA.
- **Activation ranges**: the subset of numbers to activate immediately upon port completion. Numbers in the range but not in any activation range still port but remain inactive.

You can specify multiple activation ranges within a single block (e.g., `000`–`064` and `087`).

### Steps

1. **Create a port order with blocks** – Use `POST /v2/porting_orders` with a `phone_number_blocks` array containing `phone_number_range` (`start_at`, `end_at`) and `activation_ranges`.
2. **Add blocks to an existing order** – Use `POST /v2/porting_orders/{id}/phone_number_blocks`. Numbers already on the order that fall within the block range are incorporated automatically.
3. **View blocks** – Use `GET /v2/porting_orders/{id}/phone_number_blocks`. Numbers belonging to a block include a `block_reference_id` in the porting phone numbers list.
4. **Remove a block** – Use `DELETE /v2/porting_orders/{id}/phone_number_blocks/{block_id}`. Individual phone numbers remain on the order—only the block grouping is removed.

## Canceling Port-In Orders

Canceling stops a port-in request before it completes. The order first transitions to `cancel-pending` while the Porting Operations team reviews the request, then to `cancelled` once processed. A cancelled order cannot be reactivated; you must submit a new one.

### Constraints

- You **cannot** cancel via the API within **48 hours of the FOC date/time**. Contact [Telnyx support](https://support.telnyx.com) directly within that window.
- Cancellation requires review by the Porting Operations team.

### Steps

1. Use `POST /v2/porting_orders/{id}/actions/cancel` to request cancellation. If the FOC date is within 48 hours, the API returns an error—contact support instead.
2. Monitor the order status. It remains `cancel-pending` until processed, then changes to `cancelled`.

### Cancellation webhook events

Configure webhooks to receive `porting_order.status_changed` events for `cancel-pending` and `cancelled` transitions.

## Port-In Notifications and Events

### Setting up notifications

Port-in notifications can be sent via email or webhook and cover: status changes, new comments, split orders, messaging activation, and deleted draft orders.

**Portal-wide setup** (applies to all port orders):

1. Sign in to the [Telnyx Portal](https://portal.telnyx.com/).
2. Go to **Account Settings → Advanced Features → [Notifications](https://portal.telnyx.com/#/app/advanced-features/notifications)**.
3. Create a **New Profile** (Notification Profile).
4. Add **New Channel(s)** for email or webhook URLs.
5. Add a **New Setting**, select **Port In Notifications**, and choose the profile and channel.

**Per-order webhook** (webhook only):

Set the `webhook_url` parameter when creating or updating a port order via `PATCH /v2/porting_orders/{id}`. This allows each order to have its own webhook URL.

### Port-in event types

The Events API provides on-demand access to event history (distinct from push notifications). Event types include:

| Event type | Description |
|---|---|
| `porting_order.status_changed` | Order transitioned to a new status. |
| `porting_order.new_comment` | A new comment was added. |
| `porting_order.split` | Numbers were split into a separate order. |
| `porting_order.messaging_changed` | Messaging activation status changed. |
| `porting_order.deleted` | A draft order was deleted (via API or auto-deletion after 30 days). |

### Querying and republishing events

- **List events** – `GET /v2/porting/events` with optional filters by `porting_order_id`, event type, or date range.
- **Republish** – `POST /v2/porting/events/{id}/republish` resends notifications to currently subscribed channels. It does not create a new event. Email delivery may take a few minutes.
