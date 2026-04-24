---
title: Port in extended numbers
summary: Port phone number extensions (extended numbers) alongside a route number for German porting orders.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/extensions/index
    content_hash: a85c669e829b9148665666baddb5e55529204407363907b659f08395a6768408
updated_at: 2026-04-10T00:00:00Z
---

# Port in extended numbers

Port phone number extensions (extended numbers) alongside a route number for German porting orders

## Overview

Phone number extensions allow multiple phone lines to branch off from a single direct inward dialing (DID) number or main line. This setup is common in offices or call centers where individual desks or employees need unique extensions.

The system has two components:

* **Route number**: The primary phone number (also called the "main" number) that serves as the gateway for incoming calls before they are directed to specific extensions.
* **Extended numbers**: Short digit sequences appended to the route number that connect callers directly to specific endpoints like departments or individuals.

For example, if the route number is `+49 20 12345678`, extensions might include `+49 20 123456780` or `+49 20 1234567806`.

When porting extended numbers, you first create a porting order with the route number, then attach the extensions to that order before submission.

## Constraints

* Extended number porting is currently only available for German port orders.
* Extensions can only be added while the porting order is in `draft`, `in-process`, or `exception` status.
* The maximum extension range is `0` to `999`.
* Activation ranges must be equal to or a subset of the extension range.
* Activation ranges cannot overlap.

## Extension range and activation ranges

Extensions are created in blocks defined by two parameters:

* **`extension_range`**: Represents the full range of extensions available for the route number. This typically covers 10 numbers (`0`-`9`), 100 numbers (`0`-`99`), or 1000 numbers (`0`-`999`). All extensions within this range will port with the route number.
* **`activation_ranges`**: Specifies which extensions within the `extension_range` should be active immediately upon port completion. Extensions not included in `activation_ranges` will port but remain inactive on your account.

For example, if your route number is `+49 20 12345678` and you want to activate only extension `+49 20 123456784`:

* Set `extension_range` to `0`-`9` (covering `+49 20 123456780` through `+49 20 123456789`).
* Set `activation_ranges` to `4`-`4` (activating only `+49 20 123456784`).

For multiple non-contiguous extensions like `+49 20 1234567804`, `+49 20 1234567819`, `+49 20 1234567820`, and `+49 20 1234567842`:

* Set `extension_range` to `0`-`99`.
* Set `activation_ranges` to include `4`-`4`, `19`-`20`, and `42`-`42`.

## How it works

### Step 1: Create a porting order with the route number

Create a porting order that includes the route number (the main DID). Do not include the extended numbers in the initial order.

### Step 2: Retrieve the porting phone number ID

Use the [List all porting phone numbers](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-phone-numbers) endpoint to retrieve the `porting_phone_number_id` for your route number. You will need this ID to attach extensions.

### Step 3: Add extensions to the porting order

Use the [Create a phone number extension](https://developers.telnyx.com/api-reference/porting-orders/create-a-phone-number-extension) endpoint to attach extensions to your porting order. Provide the `porting_phone_number_id`, `extension_range`, and `activation_ranges` in your request.

### Step 4: Submit the porting order

Once extensions are attached, submit your porting order through the standard porting workflow. The route number and all extensions within the `extension_range` will port together.

## Manage extensions

### View extensions

The route number appears in the [List all porting phone numbers](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-phone-numbers) response, but extended numbers do not. To view extensions attached to a porting order, use the [List all phone number extensions](https://developers.telnyx.com/api-reference/porting-orders/list-all-phone-number-extensions) endpoint.

### Delete extensions

To remove extensions from a porting order before submission, use the [Delete a phone number extension](https://developers.telnyx.com/api-reference/porting-orders/delete-a-phone-number-extension) endpoint. The order must be in `draft`, `in-process`, or `exception` status.
