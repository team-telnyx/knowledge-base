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

*Part 3 of 3 — see also: [Part 1](group-messaging-and-hosted-sms--part-1.md), [Part 2](group-messaging-and-hosted-sms--part-2.md)*

Telnyx messaging capabilities covering group MMS messaging for multi-party conversations and Hosted SMS for adding programmable messaging to numbers that remain with an existing voice provider, including internal transfers between Telnyx accounts.

## Internal Hosted SMS Transfer

Internal Hosted SMS Transfer moves messaging-enabled numbers between two Telnyx accounts without going through the standard carrier porting process. This is useful when:

- Multiple Telnyx accounts are managed (e.g., separate voice and messaging organizations)
- Numbers need to be consolidated under a single account
- Messaging services are being migrated from one Telnyx organization to another

Internal transfers are automatically detected when the number(s) in a hosted SMS order already belong to another Telnyx account. No additional configuration is needed — the system handles this automatically.

When a number is internally transferred, any **10DLC campaign registrations** associated with that number are automatically deleted. The receiving account must re-register the number with a campaign after the transfer completes.

### How it works

Internal transfers follow a modified version of the standard [Hosted SMS](hosted-sms.md) flow with an additional approval step to protect the current number owner.

1. **Create the hosted SMS order** — The receiving account creates a standard hosted SMS order with the number(s) to transfer. The system automatically detects that the number belongs to another Telnyx account and flags the order as an internal transfer.
2. **Current owner is notified** — The account that currently owns the number receives an email and portal notification with the transfer request details, including an approval link.
3. **Approval window (72 hours)** — The current owner has **72 hours** to approve or reject the transfer. If no action is taken, the transfer is **automatically approved** after the window expires.
4. **Verify ownership (2FA)** — After approval, the receiving account must complete phone number ownership verification — the same verification code process used in standard hosted SMS orders.
5. **Upload documents** — Upload the Letter of Authorization (LOA) and the most recent bill, just like a standard hosted SMS order.
6. **Activation** — Once approved, verified, and documents are submitted, the Telnyx team reviews and activates the transfer. The number's `user_id` is updated to the new account, and any existing 10DLC campaign associations on the number are removed.

### Create an internal transfer order

Create a hosted SMS order using the same endpoint as a standard order. The system automatically detects if the number belongs to another Telnyx account.

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "messaging_profile_id": "16fd2706-8baf-433b-82eb-8c7fada847da",
    "phone_numbers": ["+13125550001"]
  }' \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders"
```

Example response:

```
{
  "record_type": "messaging_hosted_number_order",
  "id": "7d9b9fdc-d073-4c3d-9c74-bf0622b3830c",
  "messaging_profile_id": "16fd2706-8baf-433b-82eb-8c7fada847da",
  "status": "pending",
  "phone_numbers": [
    {
      "record_type": "messaging_hosted_number",
      "id": "bda67701-2c08-47ba-8242-f6e6b235cca8",
      "phone_number": "+13125550001",
      "status": "pending"
    }
  ]
}
```

The response looks identical to a standard hosted SMS order. The internal transfer detection happens server-side — the current owner of the number will receive a notification automatically.

### Approve or reject a transfer

The current number owner can approve or reject the transfer using the link in their notification email, or via the API.

**Approve:**

```
curl -X POST \
  --header "Authorization: Bearer CURRENT_OWNER_API_KEY" \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/approve?token=APPROVAL_TOKEN"
```

**Reject:**

```
curl -X POST \
  --header "Authorization: Bearer CURRENT_OWNER_API_KEY" \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/reject?token=APPROVAL_TOKEN"
```

The `token` parameter is included in the notification sent to the current owner. It is a one-time use token that expires after **72 hours**. If the token expires without action, the transfer is **automatically approved**.

| Decision | Result |
| --- | --- |
| **Approved** | Transfer proceeds. Receiving account must complete 2FA verification and document upload. |
| **Rejected** | Order is marked as `failed`. The receiving account is notified. |
| **No action (72h)** | Transfer is **auto-approved**. Receiving account must still complete verification. |

### Complete the transfer

After the transfer is approved (either explicitly or via auto-approval), the receiving account must:

1. **Verify ownership** — Send and validate verification codes for the number(s), identical to the standard verification process.
2. **Upload documents** — Submit the LOA and bill via the file upload endpoint.
3. **Wait for activation** — The Telnyx team reviews and activates the transfer.

### Webhook notifications

Internal transfers generate the same webhook events as standard hosted SMS orders (`.created`, `.updated`, `.deleted`), plus five lifecycle-specific events that let you track classification, approval, and auto-approval separately from generic order updates.

**Lifecycle event reference**

| Event | Fired when |
| --- | --- |
| `messaging_hosted_numbers_orders.internal_transfer_detected` | Order is classified as an internal transfer (fires on order creation, immediately after `.created`) |
| `messaging_hosted_numbers_orders.internal_transfer_approval_requested` | Approval was requested from the losing account and the 72h window has started. Includes `approval_deadline` |
| `messaging_hosted_numbers_orders.internal_transfer_approved` | Losing account clicked **Approve** |
| `messaging_hosted_numbers_orders.internal_transfer_rejected` | Losing account clicked **Reject**, or the receiving account cancelled/deleted the order |
| `messaging_hosted_numbers_orders.internal_transfer_auto_approved` | 72h window elapsed with no response (background auto-approval), or the receiving account was on the bypass-approval allowlist |

**Detected (fires after `.created`):**

```
{
  "data": {
    "event_type": "messaging_hosted_numbers_orders.internal_transfer_detected",
    "payload": {
      "order_status": "pending",
      "numbers": [{"status": "pending", "value": "+13125550001"}]
    }
  }
}
```

**Approval requested:**

```
{
  "data": {
    "event_type": "messaging_hosted_numbers_orders.internal_transfer_approval_requested",
    "payload": {
      "order_status": "pending",
      "numbers": [{"status": "pending", "value": "+13125550001"}],
      "decision": "pending",
      "approval_deadline": 1714521600
    }
  }
}
```

**Approved:**

```
{
  "data": {
    "event_type": "messaging_hosted_numbers_orders.internal_transfer_approved",
    "payload": {
      "order_status": "pending",
      "decision": "approved"
    }
  }
}
```

**Rejected:**

```
{
  "data": {
    "event_type": "messaging_hosted_numbers_orders.internal_transfer_rejected",
    "payload": {
      "order_status": "failed",
      "decision": "rejected"
    }
  }
}
```

**Auto-approved:**

```
{
  "data": {
    "event_type": "messaging_hosted_numbers_orders.internal_transfer_auto_approved",
    "payload": {
      "order_status": "pending",
      "decision": "approved"
    }
  }
}
```

**Transfer activated:**

Once approved, activation emits the standard `.updated` event when numbers become successful:

```
{
  "data": {
    "event_type": "messaging_hosted_numbers_orders.updated",
    "payload": {
      "order_status": "successful",
      "numbers": [{"status": "successful", "value": "+13125550001"}]
    }
  }
}
```

### Key differences from standard Hosted SMS

| Aspect | Standard Hosted SMS | Internal Transfer |
| --- | --- | --- |
| **Source** | External carrier | Another Telnyx account |
| **Detection** | Manual | Automatic (system detects Telnyx-owned numbers) |
| **Approval** | Not required | Required from current owner (72h window) |
| **Auto-approval** | N/A | Yes, after 72 hours with no response |
| **Campaign cleanup** | N/A | 10DLC campaigns automatically removed |
| **Carrier porting** | Yes (NNID override) | No (direct `user_id` update) |
| **2FA verification** | Required | Required (after approval) |
| **LOA + Bill** | Required | Required |

### Troubleshooting

**Transfer was auto-approved but not wanted**

If the 72-hour window passed without action, the transfer is automatically approved. Contact [Telnyx Support](https://support.telnyx.com) immediately — the transfer may be reversible if activation hasn't completed.

**Verification code not received**

Ensure the number can receive SMS messages. For internal transfers, the verification code is sent to the number being transferred. If the number is a landline or doesn't have SMS capabilities on the current account, contact [Telnyx Support](https://support.telnyx.com) for assistance.

**Order failed after approval**

Check the order status for specific error details. Common causes include the number being deleted or deactivated on the source account before activation, the number already being hosted with another Telnyx subscriber, or billing issues on the receiving account. Use the [Get Order](https://developers.telnyx.com/api-reference/hosted-numbers/retrieve-a-messaging-hosted-number-order) endpoint to check the current status.

**10DLC campaigns were removed**

This is expected behavior. When a number transfers between accounts, existing campaign associations are automatically cleaned up. Register the number with a new campaign on the receiving account after the transfer completes. See [10DLC Campaign Registration](https://developers.telnyx.com/docs/messaging/10dlc/quickstart) for details.
