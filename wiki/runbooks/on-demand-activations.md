---
title: On-demand activations
summary: Port your phone numbers at your convenience with flexible activation windows.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations/index
    content_hash: aff072ed723d7c0bda6428dcbea1647ffba3f4180dd27f22094d3781cd94e1e5
updated_at: 2026-04-10T00:00:00Z
---

# On-demand activations

Port your phone numbers at your convenience with flexible activation windows

## Overview

On-demand activations give you control over when your ported phone numbers activate. Rather than having numbers activate automatically at a carrier-assigned time, you can trigger the activation yourself within a designated window on the FOC (Firm Order Commitment) date.

This differs from scheduled activations where numbers automatically port at the exact FOC date and time assigned by the carrier. With on-demand activation, you choose the precise moment within the activation window that works best for your business operations.

If you don't initiate the activation during the window, the numbers will automatically port at the end of the window. This ensures your port order completes even if you miss the manual activation opportunity.

## Constraints

* On-demand activation is only available for orders where `fast_port_eligible` is `true`.
* Currently available for phone numbers in the **US** and **Canada** only.
* You can only initiate activation after the order reaches `foc-date-confirmed` status.
* Activation must occur within the designated activation window on the FOC date.

## Activation windows

Each country has a specific window during which you can initiate on-demand activation. The window defines the earliest and latest times you can trigger the port.

| Country | Window start | Window end | Duration |
| :------ | :----------- | :--------- | :------- |
| US      | 6:00 AM CT   | 8:00 PM CT | 14 hours |
| Canada  | 8:00 AM CT   | 3:00 PM CT | 7 hours  |

When your order reaches `foc-date-confirmed` status, an activation job is created. The `activation_windows` array in the activation job response shows the exact start and end times for your specific order.

The `activate_at` field indicates when the port will occur. By default, this is set to the end of the activation window. When you initiate on-demand activation, this field updates to reflect when you triggered the request.

## Activation job statuses

Each activation job has a status indicating its current state:

| Status       | Description                                                                 |
| :----------- | :-------------------------------------------------------------------------- |
| `created`    | The activation job exists and is waiting for the activation window to open. |
| `in-process` | The activation has been initiated and numbers are being ported.             |
| `completed`  | The activation finished successfully and numbers have been ported.          |

## How it works

### Step 1: Enable on-demand activation

By default, all porting orders use scheduled activation (`activation_type: scheduled`). To enable on-demand activation, update the order's activation settings using the [Edit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order).

Set `activation_settings.activation_type` to `on-demand`. The order must have `fast_port_eligible` set to `true` for this to succeed.

### Step 2: View the activation window

Once your order reaches `foc-date-confirmed` status, retrieve the activation job to see your activation window. Use the [List porting activation jobs endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-activation-jobs) to view the `activation_windows` array containing your window's `start_at` and `end_at` times.

### Step 3: Initiate activation

When the FOC date arrives and you're within the activation window, trigger the port using the [Activate porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/activate-every-number-in-a-porting-order-asynchronously).

The `activate_at` field updates to reflect the time you submitted the request, and the activation process begins.

### Step 4: Monitor activation progress

Track the activation job status to monitor progress. Use the [List porting activation jobs endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-activation-jobs) or [Retrieve a porting activation job endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-activation-job) to check the current `status`.

The job progresses from `created` to `in-process` to `completed`. Once the status reaches `completed`, your numbers have finished porting and are active on your Telnyx account.

For real-time updates, configure [porting notifications](https://developers.telnyx.com/docs/numbers/porting/port-in-notifications) to receive webhooks as the activation progresses.
