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
  content_hash: c57d04ef8e55bf70f85d691716151e30f2269f5617cc5b890a08a3b02d8b97f7
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
  content_hash: 42415df5ca6fab87fb39deb17ad1095c7b17bcff8eb34205cb4cb045bdda5129
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
  content_hash: f78fb88a5a55f83b02c1a393d324e00db0fa1d5ef7574f724a1fa95d151c72d3
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
  content_hash: 5ccdea42739f096fff42a94c477bb735791253ef005b501201a62590f6527c6c
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started/index
  content_hash: ba6cc1f079d5d8b5bf6edf528e15cb7966f54d483cf4355d45cef759c1dfb961
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
  content_hash: db74f412411b32614ca0191df8f2a8da628f2964cc6d4c27f6a2a649dd40f2ff
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
  content_hash: 3e790c6cb3ba41b7580d5f87af025906ec71d6ab399bbd1dfca753fe9394ea91
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
  content_hash: 35b440b6af71ff23b789929d8cfb955fae9e530fa73a9dc434d20a39ecda061c
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
  content_hash: f3e4b2c3940588fc3b2266a2a9ca69b01a962f4ca5e1b6d87cf0ec33265003d8
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
  content_hash: 4122729cf6748c535219fb6949b2794fa0383dd3e58160f098448159f24c06e5
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements
  content_hash: 12c93a7143e8dab1d4250af66007af051eb7dd70e83bc1ffafe2a7577f3abeac
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-events
  content_hash: b52f2d40d95f86a5ea703fdd249fa76d568eb7f3da0ba05066aec6f9185bb35f
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications
  content_hash: c5a9cd86d7f047458f86c67ebebf504529c162d4685c3ffcb42754a629908460
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
  content_hash: cd0410d6fe502cc0e334002c3d91a0736a01d729700ece288fcb0fd238cdc7ce
- url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
  content_hash: 939ebc3a4092308abcc1b152f2d66a799afea7aa9c634ed3b51b3e0e3751913d
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
