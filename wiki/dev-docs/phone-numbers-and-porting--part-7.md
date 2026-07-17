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

*Part 7 of 11 — see also: [Part 1](phone-numbers-and-porting--part-1.md), [Part 2](phone-numbers-and-porting--part-2.md), [Part 3](phone-numbers-and-porting--part-3.md), [Part 4](phone-numbers-and-porting--part-4.md), [Part 5](phone-numbers-and-porting--part-5.md), [Part 6](phone-numbers-and-porting--part-6.md), [Part 8](phone-numbers-and-porting--part-8.md), [Part 9](phone-numbers-and-porting--part-9.md), [Part 10](phone-numbers-and-porting--part-10.md), [Part 11](phone-numbers-and-porting--part-11.md)*

This page consolidates Telnyx developer documentation covering phone number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in and port-out workflows, and the notifications and events that track them. It provides an end-to-end reference for purchasing numbers, fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and monitoring the lifecycle of those operations via webhooks and events.

## Port-in Requirements

All port-in orders have regulatory requirements that must be fulfilled before the port can be completed. These requirements vary based on the country and phone number type you are porting.

When you create a port order, the `requirements` array is automatically populated based on the country and phone number type being ported. Each requirement includes a `requirement_type_id` that identifies what information is needed. Use the `GET /v2/porting_orders/{id}/requirements` endpoint to view detailed information about all requirements on your port order.

To fulfill a requirement, submit the appropriate `field_value` for each `requirement_type_id` using the [PATCH /v2/porting_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order). The value you provide depends on the requirement type:

- **Document**: Provide a document ID from the Documents API.
- **Textual**: Provide a string value that meets the acceptance criteria.
- **Address**: Provide an address ID from the Addresses API.

### Requirement Statuses

| Status | Description |
| --- | --- |
| `requirement-info-pending` | Awaiting user submission. |
| `requirement-info-under-review` | Information has been submitted and is awaiting review by Telnyx Porting Operations. |
| `requirement-info-exception` | The submitted information does not meet the acceptance criteria. |
| `approved` | The requirement has been reviewed and validated by Telnyx Porting Operations. |

For a high-level view of whether all requirements have been fulfilled and approved, check the `requirements_status` field on the port order. Use the [GET /v2/porting_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) to check this status.

## Allowed FOC Dates

The firm order commitment (FOC) date is when the losing carrier agrees to release phone numbers to Telnyx. This is the date your port will actually complete and your numbers will become active on your Telnyx account. When creating or updating a port order, you can request a specific FOC date using the `foc_datetime_requested` field.

### Constraints

- Requested FOC dates are not guaranteed. The losing carrier ultimately determines the actual FOC date.
- The requested date and time must fall within one of the allowed FOC windows returned by the API.
- FOC windows vary based on the losing carrier and the phone numbers in your order.

### How It Works

**Step 1: Retrieve allowed FOC windows.** Use the [List allowed FOC dates endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-allowed-foc-dates) to view the available FOC windows for your port order. The response contains an array of allowed windows, each with `start_time` and `end_time` fields indicating the valid date and time range. All times are in UTC format.

**Step 2: Set your requested FOC date.** Use the [Edit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order) to set your preferred FOC date. Update the `activation_settings.foc_datetime_requested` field with a timestamp that falls within one of the allowed windows. The timestamp must be in ISO 8601 format.

**Step 3: Monitor FOC confirmation.** After submitting your port order, Telnyx works with the losing carrier to confirm the FOC date. When confirmed, the order status changes to `foc-date-confirmed` and the `foc_datetime_actual` field updates with the confirmed date and time.

## On-demand Activations

On-demand activations give you control over when your ported phone numbers activate. Rather than having numbers activate automatically at a carrier-assigned time, you can trigger the activation yourself within a designated window on the FOC date. If you don't initiate the activation during the window, the numbers will automatically port at the end of the window.

### Constraints

- On-demand activation is only available for orders where `fast_port_eligible` is `true`.
- Currently available for phone numbers in the US and Canada only.
- You can only initiate activation after the order reaches `foc-date-confirmed` status.
- Activation must occur within the designated activation window on the FOC date.

### Activation Windows

| Country | Window start | Window end | Duration |
| --- | --- | --- | --- |
| US | 6:00 AM CT | 8:00 PM CT | 14 hours |
| Canada | 8:00 AM CT | 3:00 PM CT | 7 hours |

When your order reaches `foc-date-confirmed` status, an activation job is created. The `activation_windows` array in the activation job response shows the exact start and end times for your specific order. The `activate_at` field indicates when the port will occur. By default, this is set to the end of the activation window.

### Activation Job Statuses

| Status | Description |
| --- | --- |
| `created` | The activation job exists and is waiting for the activation window to open. |
| `in-process` | The activation has been initiated and numbers are being ported. |
| `completed` | The activation finished successfully and numbers have been ported. |

### How It Works

**Step 1: Enable on-demand activation.** By default, all porting orders use scheduled activation (`activation_type: scheduled`). To enable on-demand activation, update the order's activation settings using the [Edit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order). Set `activation_settings.activation_type` to `on-demand`.

**Step 2: View the activation window.** Once your order reaches `foc-date-confirmed` status, retrieve the activation job to see your activation window using the [List porting activation jobs endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-activation-jobs).

**Step 3: Initiate activation.** When the FOC date arrives and you're within the activation window, trigger the port using the [Activate porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/activate-every-number-in-a-porting-order-asynchronously).

**Step 4: Monitor activation progress.** Track the activation job status using the [List porting activation jobs endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-activation-jobs) or [Retrieve a porting activation job endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-activation-job).

## Cancel Port Order

Canceling a port order allows you to stop a port-in request before it completes. When you cancel a port order, it first transitions to a `cancel-pending` status while the Porting Operations team reviews and processes the cancellation request. Once processed, the order moves to `cancelled` status.

### Constraints

- You cannot cancel a port order via the API within 48 hours of the FOC date/time. If you need to cancel within this window, contact Telnyx support directly.
- Cancellation requests require review by the Porting Operations team before taking effect.
- Once a port order reaches `cancelled` status, it cannot be reactivated.

### Cancellation Statuses

| Status | Description |
| --- | --- |
| `cancel-pending` | The cancellation request has been submitted and is awaiting review. |
| `cancelled` | The port order has been successfully cancelled and will not proceed. |

### How It Works

**Step 1: Cancel the port order.** Use the [POST /v2/porting_orders//actions/cancel endpoint](https://developers.telnyx.com/api-reference/porting-orders/cancel-a-porting-order) to request cancellation. If the port order's FOC date is within 48 hours, the API will return an error.

**Step 2: Monitor cancellation status.** Check the status of the cancellation using the [GET /v2/porting_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order).
