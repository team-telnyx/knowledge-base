---
title: Allowed FOC dates
summary: Request and set a specific date for your port order to complete.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates/index
    content_hash: c6b482975a08e242f9f7b2a692469963e299a13e618e40901fcb13e50595e4fa
updated_at: 2026-04-10T00:00:00Z
---

# Allowed FOC dates

Request and set a specific date for your port order to complete

## Overview

The firm order commitment (FOC) date is when the losing carrier agrees to release phone numbers to Telnyx. This is the date your port will actually complete and your numbers will become active on your Telnyx account.

When creating or updating a port order, you can request a specific FOC date using the `foc_datetime_requested` field. This gives you control over when your numbers port, allowing you to coordinate the transition with your business operations.

Once Telnyx receives FOC confirmation from the losing carrier, the order transitions to `foc-date-confirmed` status. The `foc_datetime_actual` field then reflects the confirmed date, which may differ from your requested date depending on carrier availability.

## Constraints

* Requested FOC dates are not guaranteed. The losing carrier ultimately determines the actual FOC date.
* The requested date and time must fall within one of the allowed FOC windows returned by the API.
* FOC windows vary based on the losing carrier and the phone numbers in your order.

## How it works

### Step 1: Retrieve allowed FOC windows

Use the [List allowed FOC dates endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-allowed-foc-dates) to view the available FOC windows for your port order.

The response contains an array of allowed windows, each with `start_time` and `end_time` fields indicating the valid date and time range. All times are in UTC format.

For example, a window with `start_time` of `2024-03-15T15:00:00Z` and `end_time` of `2024-03-15T23:00:00Z` means you can request any time between 15:00 and 23:00 UTC on March 15th.

### Step 2: Set your requested FOC date

Use the [Edit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order) to set your preferred FOC date.

Update the `activation_settings.foc_datetime_requested` field with a timestamp that falls within one of the allowed windows. The timestamp must be in ISO 8601 format (for example, `2024-03-15T15:00:00Z`).

### Step 3: Monitor FOC confirmation

After submitting your port order, Telnyx works with the losing carrier to confirm the FOC date. When confirmed, the order status changes to `foc-date-confirmed` and the `foc_datetime_actual` field updates with the confirmed date and time.

Monitor your order status through the [Retrieve porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) or configure webhooks to receive notifications when the status changes.

## Notifications

You can receive webhook notifications when the port order status changes. Configure webhooks to receive `porting_order.status_changed` events when the order transitions to `foc-date-confirmed` status.

For more information about porting webhooks, see the [port-in events guide](https://developers.telnyx.com/docs/numbers/porting/port-in-events).
