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

*Part 1 of 8 — see also: [Part 2](port-in-orders--part-2.md), [Part 3](port-in-orders--part-3.md), [Part 4](port-in-orders--part-4.md), [Part 5](port-in-orders--part-5.md), [Part 6](port-in-orders--part-6.md), [Part 7](port-in-orders--part-7.md), [Part 8](port-in-orders--part-8.md)*

Port-in orders transfer existing phone numbers from another carrier to Telnyx. This page covers the end-to-end port-in workflow via the V2 porting API, including creating and submitting orders, requesting FOC dates, on-demand activations, block and extension porting, bundle pre-configuration, messaging activation, cancellation, and webhook notifications and events.

## Overview

Port-in orders allow you to transfer existing phone numbers from another carrier to Telnyx. The porting process involves creating a draft order, providing required information and documents, and submitting the order for processing with the losing carrier. Port orders are processed asynchronously through coordination between Telnyx and the losing carrier. Processing times vary based on carrier, country, and phone number type—ranging from same-day for FastPort-eligible numbers to several weeks for international ports.

For general information about the porting process, timelines, and international requirements, see the [porting support articles](https://support.telnyx.com/en/collections/133126-porting-articles-and-guides).

## Constraints

- Phone numbers must pass a portability check before creating a port order. Non-portable numbers will result in API errors.
- Port orders may be automatically split into multiple orders based on country, number type, SPID (for US/CA), and FastPort eligibility.
- Each split order must be updated and submitted independently.
- A Letter of Authorization (LOA) and recent invoice are required for most port orders.
- Requested FOC dates are not guaranteed—the losing carrier determines the actual activation date.

## Order splitting

When you create a port order with multiple phone numbers, the API may split them into separate orders. Numbers are grouped based on:

- **Country**: Numbers from different countries are split into separate orders.
- **Number type**: Local, toll-free, and mobile numbers are processed separately.
- **SPID**: For US and CA numbers, numbers with different Service Provider IDs are split.
- **FastPort eligibility**: FastPort-eligible numbers are separated from standard port orders.

If your order is split, the API returns multiple port order IDs. You must complete and submit each order individually.

## How it works

### Step 1: Check portability

Use the [Portability check endpoint](https://developers.telnyx.com/api-reference/phone-number-porting/run-a-portability-check) to verify your numbers can be ported to Telnyx before creating an order. Phone numbers must be submitted in E.164 format.

The response indicates whether each number is `portable` and includes additional details like `fast_portable` eligibility and `messaging_capable` status. If a number is not portable, the `not_portable_reason` field explains why.

### Step 2: Create a draft port order

Use the [Create porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-porting-order) to create a draft order with your phone numbers.

The API validates the numbers and may split them into multiple orders. Each order is created in `draft` status, allowing you to add required information before submission.

### Step 3: Fulfill the porting order

Use the [Edit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order) to provide the required information:

- **End user information**: The name and account details of the current account holder with the losing carrier.
- **Service address**: The address associated with the phone numbers being ported.
- **Regulatory requirements**: Documents and information required for the port, such as a Letter of Authorization (LOA) and recent invoice. See the [Port-in requirements](port-in-requirements.md) guide for details.
- **Phone number configuration**: Optionally assign a `connection_id`, `messaging_profile_id`, or `emergency_address_id` to apply settings to all ported numbers.
- **FOC date**: Select your requested firm order commitment (FOC) date—the date your numbers will port to Telnyx. See [Allowed FOC dates](allowed-foc-dates.md) for details on retrieving available windows and setting your preferred date.

### Step 4: Submit the port order

Use the [Submit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/submit-a-porting-order) to submit your order.

The order transitions from `draft` to `in-process` status. Telnyx validates the submission and coordinates with the losing carrier to complete the port.

### Step 5: Monitor order progress

Track your order status using the [Retrieve porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) or configure webhooks to receive status change notifications.

If the order enters `exception` status, check the order comments for details about the rejection. Update the required information and resubmit.

## Allowed FOC dates

The firm order commitment (FOC) date is when the losing carrier agrees to release phone numbers to Telnyx. This is the date your port will actually complete and your numbers will become active on your Telnyx account.

When creating or updating a port order, you can request a specific FOC date using the `foc_datetime_requested` field. This gives you control over when your numbers port, allowing you to coordinate the transition with your business operations.

Once Telnyx receives FOC confirmation from the losing carrier, the order transitions to `foc-date-confirmed` status. The `foc_datetime_actual` field then reflects the confirmed date, which may differ from your requested date depending on carrier availability.

### Constraints

- Requested FOC dates are not guaranteed. The losing carrier ultimately determines the actual FOC date.
- The requested date and time must fall within one of the allowed FOC windows returned by the API.
- FOC windows vary based on the losing carrier and the phone numbers in your order.

### How it works

**Step 1: Retrieve allowed FOC windows.** Use the [List allowed FOC dates endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-allowed-foc-dates) to view the available FOC windows for your port order. The response contains an array of allowed windows, each with `start_time` and `end_time` fields indicating the valid date and time range. All times are in UTC format. For example, a window with `start_time` of `2024-03-15T15:00:00Z` and `end_time` of `2024-03-15T23:00:00Z` means you can request any time between 15:00 and 23:00 UTC on March 15th.

**Step 2: Set your requested FOC date.** Use the [Edit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order) to set your preferred FOC date. Update the `activation_settings.foc_datetime_requested` field with a timestamp that falls within one of the allowed windows. The timestamp must be in ISO 8601 format (for example, `2024-03-15T15:00:00Z`).

**Step 3: Monitor FOC confirmation.** After submitting your port order, Telnyx works with the losing carrier to confirm the FOC date. When confirmed, the order status changes to `foc-date-confirmed` and the `foc_datetime_actual` field updates with the confirmed date and time. Monitor your order status through the [Retrieve porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) or configure webhooks to receive notifications when the status changes.
