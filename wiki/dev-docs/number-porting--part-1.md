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

*Part 1 of 4 — see also: [Part 2](number-porting--part-2.md), [Part 3](number-porting--part-3.md), [Part 4](number-porting--part-4.md)*

Number porting at Telnyx covers both port-in orders (transferring phone numbers to Telnyx from another carrier) and port-out orders (when another carrier requests numbers away from your Telnyx account). The port-in process involves checking portability, creating and fulfilling orders, managing FOC dates, and optionally configuring messaging, bundles, extensions, and blocks. Port-out orders are initiated externally and require you to authorize or reject them. Both flows support webhook notifications and a queryable event history.

## Port-In Workflow

Port-in orders transfer existing phone numbers from another carrier to Telnyx. The process is asynchronous—Telnyx coordinates with the losing carrier—and timelines range from same-day (for FastPort-eligible numbers) to several weeks for international ports.

Phone numbers must pass a portability check before creating an order. Orders may be automatically split into multiple orders based on country, number type, SPID (for US/CA), and FastPort eligibility; each split order must be updated and submitted independently. A Letter of Authorization (LOA) and recent invoice are required for most port orders.

### Order splitting

When you create a port order with multiple phone numbers, the API may split them into separate orders grouped by:

- **Country** – numbers from different countries are separated.
- **Number type** – local, toll-free, and mobile are processed separately.
- **SPID** – for US and CA, numbers with different Service Provider IDs are split.
- **FastPort eligibility** – FastPort-eligible numbers are separated from standard orders.

If your order is split, the API returns multiple port order IDs, and each must be completed and submitted individually.

### Step-by-step process

1. **Check portability** – Use the [Portability check endpoint](https://developers.telnyx.com/api-reference/phone-number-porting/run-a-portability-check) with numbers in E.164 format. The response indicates `portable`, `fast_portable`, `messaging_capable`, and—if not portable—`not_portable_reason`.
2. **Create a draft port order** – Use the [Create porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-porting-order). The API validates and may split numbers into multiple orders, each in `draft` status.
3. **Fulfill the porting order** – Use the [Edit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order) to provide end-user information, service address, regulatory documents (see [Number Porting#Port-In Requirements](number-porting-port-in-requirements.md)), optional phone number configuration (`connection_id`, `messaging_profile_id`, `emergency_address_id`), and your requested FOC date (see [Number Porting#FOC Dates and Scheduling](number-porting-foc-dates-and-scheduling.md)).
4. **Submit the port order** – Use the [Submit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/submit-a-porting-order). The order transitions from `draft` to `in-process`.
5. **Monitor order progress** – Use the [Retrieve porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) or webhooks. If the order enters `exception` status, check comments, update information, and resubmit.

### Comments

Comments let you communicate with Telnyx Porting Operations during the porting process. Use the [Create comment endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-comment-for-a-porting-order) to send messages, and the [List comments endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-comments-of-a-porting-order) to view them. Subscribe to the `porting_order.new_comment` webhook event for real-time notifications.

## Port-In Requirements

All port-in orders have regulatory requirements that must be fulfilled before the port completes. Requirements vary by country and phone number type.

When you create a port order, the `requirements` array is automatically populated. Use `GET /v2/porting_orders/{id}/requirements` to view all requirements, including descriptions and acceptance criteria.

### Fulfilling requirements

Submit the appropriate `field_value` for each `requirement_type_id` using `PATCH /v2/porting_orders/{id}`:

- **Document** – Provide a document ID from the [Documents API](https://developers.telnyx.com/api-reference/documents/upload-a-document).
- **Textual** – Provide a string that meets the acceptance criteria.
- **Address** – Provide an address ID from the [Addresses API](https://developers.telnyx.com/api-reference/addresses/creates-an-address).

### Requirement statuses

| Status | Description |
|---|---|
| `requirement-info-pending` | Awaiting user submission. |
| `requirement-info-under-review` | Submitted and awaiting review by Telnyx Porting Operations. |
| `requirement-info-exception` | Submitted information does not meet acceptance criteria; resubmit with corrections. |
| `approved` | Reviewed and validated by Telnyx Porting Operations. |

The `requirements_status` field on the port order provides a high-level view: `true` means all requirements are fulfilled and approved; `false` means one or more are still pending or not yet approved.

## Additional Steps for Port-In

After populating a porting order, Telnyx may require additional steps that involve actions affecting other phone numbers on the losing carrier's account. These differ from supplemental regulatory requirements.

Check the `additional_steps` array on the porting order:

- `[]` (empty) – no additional steps; proceed with submission.
- `["associated_phone_numbers"]` – you must specify what happens to remaining numbers on the losing carrier's account.

### Associated phone numbers

This step applies to partial ports of GB local phone numbers (when `port_type` is `partial_port`). You must provide a list of phone numbers on the losing carrier's account that are **not** porting to Telnyx and specify one of two outcomes for each:

- **Keep** – the number remains active with the losing carrier.
- **Disconnect** – the number is disconnected after the port completes.

If the billing telephone number (BTN) is included in the port, all remaining number ranges can only be disconnected.

Use `POST /v2/porting_orders/{id}/associated_phone_numbers` to specify ranges and their intended outcome. You can manage associated numbers with:

- **List** – `GET /v2/porting_orders/{id}/associated_phone_numbers`
- **Remove** – `DELETE /v2/porting_orders/{id}/associated_phone_numbers/{associated_phone_number_id}`

## FOC Dates and Scheduling

The Firm Order Commitment (FOC) date is when the losing carrier agrees to release phone numbers to Telnyx—the date the port actually completes and numbers become active on your account.

### Requesting a FOC date

Use the `foc_datetime_requested` field when creating or updating a port order. The requested date and time must fall within one of the allowed FOC windows returned by the [List allowed FOC dates endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-allowed-foc-dates). Each window has `start_time` and `end_time` in UTC. Requested dates are **not guaranteed**; the losing carrier ultimately determines the actual FOC date.

### Confirmation

Once Telnyx receives FOC confirmation from the losing carrier, the order transitions to `foc-date-confirmed` status. The `foc_datetime_actual` field then reflects the confirmed date, which may differ from your requested date. Monitor via the [Retrieve porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) or configure webhooks for `porting_order.status_changed` events.
