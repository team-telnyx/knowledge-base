---
title: Messaging + Porting
summary: Track and manage messaging activation when porting US and Canada phone numbers.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting/index
    content_hash: cfe2833346cc0d0770431c8e54ffcaeef2c8ca6b372fa0f7bd46a9c39dacd04c
updated_at: 2026-04-10T00:00:00Z
---

# Messaging + Porting

Track and manage messaging activation when porting US and Canada phone numbers

## Overview

For local and toll-free phone numbers in the US and Canada, porting voice and porting messaging are two separate processes. A porting order transitioning to `ported` status indicates that voice has ported to Telnyx, but this status does not reflect the state of messaging.

Messaging routing is controlled by a NetNumber ID (NNID), which identifies the provider that owns SMS routing for a telephone number. At the FOC date and time, the losing carrier is expected to release the NNID so messaging routes through the winning carrier. In most cases, both voice and messaging port simultaneously.

However, if the losing carrier fails to release the NNID, messaging continues to route through them even after voice has ported. This can occur due to:

* Internal system errors or delays at the losing carrier.
* Carrier block policies that retain messaging temporarily after a port.
* Intentional hosting of messaging with another carrier.

Telnyx provides visibility into messaging port status and automatically escalates issues when messaging fails to activate at the FOC date and time.

## Constraints

* Messaging porting tracking is only applicable to US and Canada local and toll-free phone numbers.
* The `messaging_capable` attribute must be `true` on the porting order to enable messaging tracking.
* A `messaging_profile_id` must be assigned to the porting order when enabling messaging activation.
* Phone numbers ported from other countries have messaging port simultaneously with voice.

## Messaging port statuses

The `messaging_port_status` field tracks messaging activation independently from the porting order's main `status` field. A porting order can have a `status` of `ported` (voice has ported) while the `messaging_port_status` is still `activating` or `exception`.

| Status           | Description                                                                                      |
| :--------------- | :----------------------------------------------------------------------------------------------- |
| `pending`        | Messaging activation is enabled but the porting order has not yet reached the FOC date and time. |
| `activating`     | The porting order has ported and Telnyx is verifying messaging activation.                       |
| `ported`         | Messaging has successfully ported to Telnyx.                                                     |
| `exception`      | Messaging failed to port automatically and Telnyx is escalating with the losing carrier.         |
| `not_applicable` | Messaging activation was not enabled for this porting order.                                     |

## How it works

### Step 1: Verify messaging capability

Check the `messaging_capable` attribute on your porting order or portability check response. Use the [POST /v2/portability\_checks](https://developers.telnyx.com/api-reference/phone-number-porting/run-a-portability-check) endpoint to verify capability before creating a porting order, or check the `messaging` object on an existing porting order using the [GET /v2/porting\_orders/](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) endpoint.

* If `messaging_capable` is `true`, Telnyx can support messaging for the phone numbers on the order.
* If `messaging_capable` is `false`, Telnyx cannot support messaging for those phone numbers.

### Step 2: Enable messaging activation

To enable messaging tracking and activation, update the porting order using the [PATCH /v2/porting\_orders/](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order) endpoint. Set `enable_messaging` to `true` in the `messaging` object.

You must also assign a `messaging_profile_id` in the `phone_number_configuration` object. This messaging profile is applied to all phone numbers on the order upon porting.

The porting order must be in `draft`, `in-process`, or `exception` status to enable this feature.

### Step 3: Monitor messaging port status

Prior to the FOC date and time, the order reflects `messaging_port_status: pending`. Once the porting order transitions to `ported` status, the messaging port status changes to `activating` while Telnyx verifies messaging activation.

In most cases, the losing carrier releases the NNID at the FOC date and time, and the status updates to `ported`.

### Step 4: Handle exceptions

If the losing carrier fails to release messaging, the status changes to `exception`. When this occurs, the Telnyx Messaging Ops team is automatically notified and escalates with the losing carrier. Resolution typically occurs within 72 hours for local numbers and up to 5 business days for toll-free numbers.

Once resolved, the `messaging_port_status` updates to `ported`.

## Webhook notifications

[Follow this support article](https://support.telnyx.com/en/articles/4277896-notification-settings) to set up webhook notifications for messaging port status changes.

Select the Notification Setting "Port In Notifications" to receive `porting_order.messaging_changed` events.

## Partial messaging ports

When a porting order contains multiple phone numbers, it is possible for some numbers to port messaging successfully while others do not. If any phone number on the order fails to port messaging, the order-level `messaging_port_status` is `exception`.

To check the messaging port status of individual phone numbers, use the [GET /v2/porting\_orders//associated\_phone\_numbers](https://developers.telnyx.com/api-reference/porting-orders/list-all-associated-phone-numbers) endpoint. Each phone number has its own `messaging_port_status` attribute indicating whether that specific number ported messaging successfully.

## Hosted SMS alternative

To avoid potential messaging downtime during porting, you can port SMS to Telnyx before porting voice by submitting a Hosted SMS request. This approach ensures messaging is active on Telnyx before the FOC date and time.

The hosted SMS workflow involves:

* Submitting a Hosted SMS request for your phone numbers at least 4 business days before the scheduled FOC date.
* Creating a porting order with a FOC date at least 4 business days in the future.
* Once the Hosted SMS request completes, SMS routes through Telnyx while voice remains with the losing carrier.
* When the FOC date arrives, voice ports and both services route through Telnyx with no downtime.

For more information, see the [Hosted SMS messaging process](https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process) support article.

## Troubleshooting

### Porting voice only without messaging

To port only voice to Telnyx while hosting messaging elsewhere, do not enable messaging activation on the porting order. Leave `enable_messaging` as `null` and do not assign a `messaging_profile_id`. The `messaging_port_status` remains `not_applicable` and Telnyx does not attempt to override the NNID.

If you later decide to activate messaging with Telnyx, see the [Send a message](https://developers.telnyx.com/docs/messaging/messages/send-message) guide.

### Porting non-US and non-Canada phone numbers

For phone numbers outside of the US and Canada, voice and messaging port simultaneously when the order transitions to `ported` status. Messaging porting tracking is available but not required for these numbers. You can optionally enable messaging activation to receive status updates and webhook notifications.

### Messaging port status shows exception

An `exception` status indicates one or more phone numbers on the order are still routing SMS through the losing carrier. Telnyx is automatically escalating with the losing carrier. Continue routing messaging through the losing carrier until you receive notification that messaging has ported.

### Expected messaging port timing

For US and Canada local phone numbers, approximately 90% of orders have messaging activated within 10 minutes of porting. The remaining orders typically complete within 1-2 business days.

For US and Canada toll-free phone numbers, messaging usually ports within 10 minutes. If activation does not occur within that window, resolution may take 4-5 business days.

For all other phone numbers, messaging ports simultaneously with voice.

### Messaging shows ported but messages fail to deliver

Verify that the phone number has a valid `messaging_profile_id` assigned. If a messaging profile is assigned and messages still fail, contact support for investigation.

### Unable to enable messaging activation

Verify that the porting order shows `messaging_capable: true` and the order status is `draft`, `in-process`, or `exception`. If these conditions are met and you cannot enable messaging activation, contact support for assistance.


## Related Pages

- [Messaging Profiles Overview](../concepts/messaging-profiles-overview.md)
