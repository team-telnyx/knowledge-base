---
title: Group Messaging and Hosted SMS
summary: Telnyx messaging capabilities covering group MMS messaging for multi-party
  conversations and Hosted SMS for adding programmable messaging to numbers that remain
  with an existing voice provider, including internal transfers between Telnyx accounts.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/group-messaging
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer
updated_at: 2026-08-05T13:55:37Z
---

# Group Messaging and Hosted SMS

*Part 2 of 3 — see also: [Part 1](group-messaging-and-hosted-sms--part-1.md), [Part 3](group-messaging-and-hosted-sms--part-3.md)*

Telnyx messaging capabilities covering group MMS messaging for multi-party conversations and Hosted SMS for adding programmable messaging to numbers that remain with an existing voice provider, including internal transfers between Telnyx accounts.

## Hosted SMS

Hosted SMS adds messaging capabilities to phone numbers that stay with the current voice provider. The existing voice service continues uninterrupted — Telnyx handles only the SMS and MMS routing.

This is ideal for:

- **Landline numbers** that need texting capabilities
- **Business numbers** where the voice provider is kept but programmable messaging is added
- **Gradual migration** — test Telnyx messaging before a full port

Hosting a number is **not** the same as porting. Voice service stays with the current provider. Only SMS/MMS traffic routes through Telnyx.

### How it works

| Step | What happens | Timeline |
| --- | --- | --- |
| **1. Eligibility check** | Verify numbers can be hosted | Instant |
| **2. Create order** | Submit a hosted SMS order | Instant |
| **3. Verify ownership** | Confirm ownership via SMS code | 5 minutes |
| **4. Upload documents** | Submit LOA and recent provider bill | Instant |
| **5. Telnyx review** | Team reviews and activates | 1-3 business days |

### Check number eligibility

Not all numbers can be hosted. Check eligibility before creating an order.

```
curl -X POST https://api.telnyx.com/v2/messaging_hosted_number_orders/eligibility_numbers_check \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "phone_numbers": ["+13125550001", "+13125550002"]
  }'
```

The Portal automatically checks eligibility when numbers are entered during order creation.

**Eligibility statuses**

| Status | Description | Action |
| --- | --- | --- |
| `eligible` | Number can be hosted | Proceed with order |
| `number_is_not_a_us_number` | Only US numbers supported | Use a US number |
| `number_can_not_be_wireless` | Wireless numbers not supported | Use a landline or VoIP number |
| `number_can_not_be_in_telnyx` | Already on Telnyx platform | No hosting needed — number already works |
| `number_can_not_hosted_with_a_telnyx_subscriber` | Already hosted by another Telnyx user | Contact support |
| `number_can_not_be_active_in_your_account` | Active in the account already | Check number inventory |
| `number_is_not_a_valid_routing_number` | Invalid routing number | Verify the number with the provider |
| `number_is_not_in_e164_format` | Wrong format | Use E.164: `+1` followed by 10 digits |
| `billing_account_check_failed` | Billing issue | Check account billing status |
| `billing_account_is_abolished` | Account closed | Contact support |

### Create a hosted SMS order

```
curl -X POST https://api.telnyx.com/v2/messaging_hosted_number_orders \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "messaging_profile_id": "YOUR_MESSAGING_PROFILE_ID",
    "phone_numbers": ["+13125550001"]
  }'
```

Numbers are created in `pending` status. They stay pending until verification and document upload are complete.

In the Portal, navigate to [Numbers → Hosted SMS](https://portal.telnyx.com/#/app/numbers/hosted-sms), click [Add New Order](https://portal.telnyx.com/#/app/numbers/hosted-sms/new), enter the phone number(s) in E.164 format, select a [messaging profile](messaging-profiles--part-1.md), and click **Create Order**.

### Verify phone number ownership

Prove ownership of the numbers by receiving and entering SMS verification codes.

**Request verification codes:**

```
curl -X POST \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/verification_codes" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "verification_method": "sms",
    "phone_numbers": ["+13125550001"]
  }'
```

**Submit verification codes:**

```
curl -X POST \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/validation_codes" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "verification_codes": [
      {"phone_number": "+13125550001", "code": "87643"}
    ]
  }'
```

A successful verification returns `verified` status. The number status then changes to `ownership_successful`.

### Upload authorization documents

After verification, upload two PDF documents:

1. **Letter of Authorization (LOA)** — signed authorization to host the number
2. **Recent bill** — from the current voice provider showing the number

```
curl -X POST \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/actions/file_upload" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  --form "loa=@/path/to/loa.pdf" \
  --form "bill=@/path/to/bill.pdf"
```

After upload, the Telnyx team reviews the order and activates the number(s). This typically takes **1-3 business days**.

### Check order status

```
curl -s "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}" \
  -H "Authorization: Bearer YOUR_API_KEY" | jq '{status, phone_numbers: [.phone_numbers[] | {phone_number, status}]}'
```

**Order statuses**

| Status | Meaning |
| --- | --- |
| `pending` | Order created, awaiting verification and documents |
| `loa_file_successful` | Documents uploaded successfully |
| `successful` | Order complete — numbers are active |
| `failed` | Activation failed (see [troubleshooting](#troubleshooting-failed-orders)) |
| `deleted` | Order was cancelled |

### Webhook notifications

Hosted SMS orders trigger webhooks to the [messaging profile's](messaging-profiles--part-1.md) configured webhook URL. Set up a handler to track order progress in real time.

**Webhook event types**

| Event | Triggered when |
| --- | --- |
| `messaging_hosted_numbers_orders.created` | Order is created |
| `messaging_hosted_numbers_orders.updated` | Status changes (verification, LOA upload, activation, failure) |
| `messaging_hosted_numbers_orders.deleted` | Order is deleted |
| `messaging_hosted_numbers_orders.internal_transfer_detected` | Order is classified as an [Internal Hosted SMS Transfer](internal-hosted-sms-transfer.md) |
| `messaging_hosted_numbers_orders.internal_transfer_approval_requested` | Internal transfer approval requested from the losing account (72h window) |
| `messaging_hosted_numbers_orders.internal_transfer_approved` | Losing account approved the internal transfer |
| `messaging_hosted_numbers_orders.internal_transfer_rejected` | Losing account rejected the internal transfer, or the receiving account cancelled the order |
| `messaging_hosted_numbers_orders.internal_transfer_auto_approved` | Internal transfer auto-approved (72h window elapsed or bypass enabled) |

Email notifications can also be configured by creating a notification profile at [Advanced Features → Notifications](https://portal.telnyx.com/#/advanced-features/notifications), adding an email channel, and configuring **Messaging Hosted SMS Activity** settings.

### Troubleshooting failed orders

**Order status: `carrier_rejected`**

The losing carrier (the current voice provider) rejected the hosting request. Common reasons include the number being under contract with restrictions on SMS routing changes, the provider not supporting hosted SMS arrangements, or account information mismatch between the LOA and provider records. Contact the voice provider to understand the rejection, verify the LOA matches the account holder name exactly, and note that some carriers require a call to authorize the SMS routing change.

**Order status: `ineligible_carrier`**

The number's carrier does not support hosted SMS with Telnyx. Consider porting the number fully to Telnyx instead, or contact Telnyx support to check if the carrier has been added since the last attempt.

**Number status: `failed_carrier_rejected`**

A specific number was rejected by the losing carrier while other numbers in the order may have succeeded. Check if this specific number has different account ownership, and create a separate order for this number after resolving with the provider.

**Number status: `failed_number_already_hosted`**

The number is already hosted on Telnyx by another account. If both accounts are owned, remove the hosting from the other account first; otherwise, contact Telnyx support to resolve the conflict.

**Number status: `failed_timeout`**

The activation process timed out waiting for carrier response. Create a new order for the same number, and if it fails again, contact Telnyx support — the carrier may need manual intervention.

**Verification code not received**

Ensure the number can receive SMS (landlines may need the current provider to enable it), check if the number has any SMS blocking enabled, request the code again (retries are allowed), or contact Telnyx support for alternative verification if the number truly cannot receive SMS.

**LOA rejected**

The Letter of Authorization didn't meet requirements. Common issues include the LOA not being signed, the name on the LOA not matching the voice provider account, or an outdated LOA template. Download the latest LOA template from Telnyx support, ensure the authorized signer matches the account holder, and upload a new LOA via the API or Portal.

**Hosted numbers not visible in Portal**

Hosted numbers may not appear in the Portal number inventory. They are accessible via the API:

```
curl -s "https://api.telnyx.com/v2/messaging_hosted_number_orders" \
  -H "Authorization: Bearer YOUR_API_KEY" | jq '.data[] | select(.status == "successful")'
```

### Failed order and number statuses reference

**Order statuses**

| Status | Description |
| --- | --- |
| `carrier_rejected` | Losing carrier rejected the porting request |
| `failed` | Order closed — contact support |
| `ineligible_carrier` | Number's carrier doesn't support hosted SMS |

**Number statuses**

| Status | Description |
| --- | --- |
| `failed` | Number closed — contact support |
| `failed_carrier_rejected` | Losing carrier rejected this number |
| `failed_ineligible_carrier` | Number's carrier doesn't support hosted SMS |
| `failed_number_already_hosted` | Already hosted by another Telnyx user |
| `failed_number_not_found` | Number not found in routing database |
| `failed_timeout` | Activation timed out |
