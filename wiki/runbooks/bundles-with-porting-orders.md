---
title: Bundles with porting orders
summary: Associate bundles with porting phone numbers so bundle pricing is automatically applied when the port completes.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting/index
    content_hash: a47f82e0c3ab9b7563037d98980e83be21cf26b7a0a9b2fa06def895f240bc69
updated_at: 2026-04-10T00:00:00Z
---

# Bundles with porting orders

Associate bundles with porting phone numbers so bundle pricing is automatically applied when the port completes

## Overview

Bundle pre-configuration allows you to associate [bundles](https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing) with phone numbers on a porting order before those numbers are active at Telnyx. When the port completes and the phone numbers become active, the pre-configured bundles are automatically applied.

The term "pre-configure" is used because bundles are not actually applied to phone numbers until after the numbers port in and become active at Telnyx. During the porting process, the bundle association exists as a pending configuration that takes effect upon port completion.

## Constraints

* Bundle pre-configuration is only available via API.
* Bundles can be pre-configured or updated at any point before the porting order reaches `ported` or `cancelled` status, including shortly before the FOC date.
* Each bundle can only be associated with one phone number. If a pre-configured bundle is used elsewhere before the port completes, the assignment will fail.
* You can pre-configure up to 20 phone numbers per API request.
* The bundle must be valid for the specific phone number type and characteristics. Invalid bundle-number combinations will return an error.
* Pre-configuring bundles is optional. You can pre-configure bundles for some, all, or none of the phone numbers on a porting order.

## How it works

### Step 1: Verify available bundles

Use the [GET /v2/bundle-pricing/user\_bundles endpoint](https://developers.telnyx.com/api-reference/user-bundles/get-user-bundles) to list your bundles, or view them on the [Bundles page](https://portal.telnyx.com/#/app/bundles) in Mission Control Portal.

A bundle is available for pre-configuration if its `resources` array is empty. Each bundle has eligibility criteria for which phone numbers it can be assigned to. To purchase additional bundles, visit the [Bundle Orders page](https://portal.telnyx.com/#/app/bundles/order).

### Step 2: Get porting phone number IDs

Each phone number on a porting order has a unique `porting_phone_number_id` that you need for pre-configuration.

Use the [GET /v2/porting\_phone\_numbers endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-phone-numbers) with a filter for your porting order ID to retrieve the list of phone numbers and their associated IDs.

### Step 3: Pre-configure bundles

Use the [POST /v2/porting\_orders/phone\_number\_configurations endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-a-list-of-phone-number-configurations) to associate bundles with porting phone numbers. Each configuration requires:

* `porting_phone_number_id`: The ID of the phone number on your porting order.
* `user_bundle_id`: The ID of the bundle to pre-configure.

### Step 4: Verify configurations

Use the `GET /v2/porting_orders/phone_number_configurations` endpoint with your porting order ID to view which bundles are pre-configured with which phone numbers.

When the port completes and phone numbers become active at Telnyx, the pre-configured bundles are automatically applied to the corresponding phone numbers.


## Related Pages

- [Getting started with port-in orders](../tutorial/getting-started-with-port-in-orders.md)
