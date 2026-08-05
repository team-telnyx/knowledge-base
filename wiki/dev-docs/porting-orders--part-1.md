---
title: Porting orders
summary: A consolidated guide to Telnyx porting workflows, covering port-in requirements
  and additional steps for inbound ports, plus port-out order management, notifications,
  and event tracking for numbers leaving your account.
sources:
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
- url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
updated_at: 2026-08-05T14:00:54Z
---

# Porting orders

*Part 1 of 4 — see also: [Part 2](porting-orders--part-2.md), [Part 3](porting-orders--part-3.md), [Part 4](porting-orders--part-4.md)*

A consolidated guide to Telnyx porting workflows, covering port-in requirements and additional steps for inbound ports, plus port-out order management, notifications, and event tracking for numbers leaving your account.

## Port-in requirements

All port-in orders have regulatory requirements that must be fulfilled before the port can be completed. These requirements vary based on the country and phone number type you are porting.

When you create a port order, the `requirements` array is automatically populated based on the country and phone number type being ported. Each requirement includes a `requirement_type_id` that identifies what information is needed. Use the `GET /v2/porting_orders/{id}/requirements` endpoint to view detailed information about all requirements on your port order, including descriptions and acceptance criteria.

To fulfill a requirement, submit the appropriate `field_value` for each `requirement_type_id` using the [PATCH /v2/porting_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order). The value you provide depends on the requirement type:

- **Document**: Provide a document ID from the [Documents API](https://developers.telnyx.com/api-reference/documents/upload-a-document).
- **Textual**: Provide a string value that meets the acceptance criteria.
- **Address**: Provide an address ID from the [Addresses API](https://developers.telnyx.com/api-reference/addresses/creates-an-address).

For detailed fulfillment instructions for each type, see the [regulatory requirements guide](https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements).

### Requirement statuses

Each requirement on a port order has a status that indicates its current state:

| Status | Description |
| --- | --- |
| `requirement-info-pending` | Awaiting user submission. You need to provide information to fulfill the requirement. |
| `requirement-info-under-review` | Information has been submitted and is awaiting review by Telnyx Porting Operations. |
| `requirement-info-exception` | The submitted information does not meet the acceptance criteria. You need to resubmit with corrected information. |
| `approved` | The requirement has been reviewed and validated by Telnyx Porting Operations. |

For a high-level view of whether all requirements have been fulfilled and approved, check the `requirements_status` field on the port order. A value of `true` means all requirements have been fulfilled and approved, while `false` indicates one or more requirements have not been fulfilled or approved yet. Use the [GET /v2/porting_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) to check this status.

## Porting additional steps

After you create and populate a porting order, Telnyx may require additional steps depending on the phone numbers being ported and the details provided. These steps must be completed before you can submit the order. Additional steps differ from [Port-in requirements](port-in-requirements.md), which cover documents and textual information needed for specific countries or number types. Additional steps involve actions or decisions that affect other phone numbers on your losing carrier's account.

The `additional_steps` array on a porting order indicates whether any additional steps are required:

| Value | Meaning |
| --- | --- |
| `[]` (empty array) | No additional steps required. You can proceed with submission. |
| `["associated_phone_numbers"]` | You must provide a list of phone numbers on your losing carrier's account that are not porting to Telnyx, and specify whether each should remain active or be deactivated after the port completes. |

Retrieve the porting order using the [GET /v2/porting_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) and check the `additional_steps` field in the response.

### Associated phone numbers

This additional step applies to partial ports of GB local phone numbers. When porting only some phone numbers from an account, you must specify what happens to the remaining phone numbers on the losing carrier's account.

The `associated_phone_numbers` step appears when both conditions are met:

- The porting order is for `GB` `local` phone numbers.
- The `port_type` is set to `partial_port`.

You must provide a list of phone numbers on your losing carrier's account that are not being ported to Telnyx. For each phone number or range, you must indicate one of two outcomes:

- **Keep**: The phone number remains active with the losing carrier after the port completes.
- **Disconnect**: The phone number is disconnected from the losing carrier after the port completes.

If the billing telephone number (BTN) is included in the port, all remaining number ranges can only be disconnected.

Use the [POST /v2/porting_orders/{id}/associated_phone_numbers endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-an-associated-phone-number) to specify ranges of phone numbers and their intended outcome (`keep` or `disconnect`). You can associate multiple number ranges by sending separate requests for each range. The phone numbers you specify in this step are not being ported to Telnyx; this endpoint communicates what should happen to other phone numbers on the losing carrier's account. Without this information, the losing carrier will reject the porting order.

You can manage the phone numbers associated with your porting order using these endpoints:

| Action | Endpoint |
| --- | --- |
| List associated phone numbers | [GET /v2/porting_orders/{id}/associated_phone_numbers](https://developers.telnyx.com/api-reference/porting-orders/list-all-associated-phone-numbers) |
| Remove an associated phone number | [DELETE /v2/porting_orders/{id}/associated_phone_numbers/{associated_phone_number_id}](https://developers.telnyx.com/api-reference/porting-orders/delete-an-associated-phone-number) |
