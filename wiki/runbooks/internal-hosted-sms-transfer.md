---
title: Internal Hosted SMS Transfer
summary: Transfer hosted SMS numbers between Telnyx accounts.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer/index
    content_hash: 70d792558a040937b2ac1a4851d6cbb312248322186ee3cfbe90d2cabe6caa2f
updated_at: 2026-04-10T00:00:00Z
---

# Internal Hosted SMS Transfer

Transfer hosted SMS numbers between Telnyx accounts. Learn how internal transfers work when both accounts are on the Telnyx platform.

## Overview

Internal Hosted SMS Transfer allows you to move messaging-enabled numbers between two Telnyx accounts without going through the standard carrier porting process. This is useful when:

* You manage multiple Telnyx accounts (e.g., separate voice and messaging organizations)
* You need to consolidate numbers under a single account
* You're migrating messaging services from one Telnyx organization to another

<Callout type="info">
  Internal transfers are automatically detected when the number(s) in your hosted SMS order already belong to another Telnyx account. No additional configuration is needed — the system handles this automatically.

## How it works

Internal transfers follow a modified version of the standard [Hosted SMS](hosted-sms.md) flow with an additional approval step to protect the current number owner.

1. **Create the hosted SMS order**

    The receiving account creates a standard hosted SMS order with the number(s) to transfer. The system automatically detects that the number belongs to another Telnyx account and flags the order as an internal transfer.

2. **Current owner is notified**

    The account that currently owns the number receives an email and portal notification with the transfer request details, including an approval link.

3. **Approval window (72 hours)**

    The current owner has **72 hours** to approve or reject the transfer. If no action is taken, the transfer is **automatically approved** after the window expires.

4. **Verify ownership (2FA)**

    After approval, the receiving account must complete phone number ownership verification — the same [verification code process](hosted-sms.md#validate-phone-numbers) used in standard hosted SMS orders.

5. **Upload documents**

    Upload the Letter of Authorization (LOA) and the most recent bill, just like a standard hosted SMS order.

6. **Activation**

    Once approved, verified, and documents are submitted, the Telnyx team reviews and activates the transfer. The number's `user_id` is updated to the new account, and any existing 10DLC campaign associations on the number are removed.

<Callout type="warning">
  When a number is internally transferred, any **10DLC campaign registrations** associated with that number are automatically deleted. The receiving account must re-register the number with a campaign after the transfer completes.

## Create an internal transfer order

Create a hosted SMS order using the same endpoint as a standard order. The system automatically detects if the number belongs to another Telnyx account.

  ```bash
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

  ```python
  import telnyx

  telnyx.api_key = "YOUR_API_KEY"

  order = telnyx.MessagingHostedNumberOrder.create(
      messaging_profile_id="16fd2706-8baf-433b-82eb-8c7fada847da",
      phone_numbers=["+13125550001"]
  )
  print(order)
  ```

  ```javascript Node.js theme={null}
  const telnyx = require('telnyx')('YOUR_API_KEY');

  const order = await telnyx.messagingHostedNumberOrders.create({
    messaging_profile_id: '16fd2706-8baf-433b-82eb-8c7fada847da',
    phone_numbers: ['+13125550001']
  });
  console.log(order.data);
  ```

  ```ruby
  require 'telnyx'

  Telnyx.api_key = 'YOUR_API_KEY'

  order = Telnyx::MessagingHostedNumberOrder.create(
    messaging_profile_id: '16fd2706-8baf-433b-82eb-8c7fada847da',
    phone_numbers: ['+13125550001']
  )
  puts order
  ```

  ```java
  import com.telnyx.sdk.*;
  import com.telnyx.sdk.api.HostedNumbersApi;

  ApiClient client = new ApiClient();
  client.setApiKey("YOUR_API_KEY");

  HostedNumbersApi api = new HostedNumbersApi(client);
  CreateHostedNumberOrderRequest request = new CreateHostedNumberOrderRequest()
      .messagingProfileId("16fd2706-8baf-433b-82eb-8c7fada847da")
      .addPhoneNumbersItem("+13125550001");

  HostedNumberOrderResponse response = api.createHostedNumberOrder(request);
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Telnyx;

  TelnyxConfiguration.SetApiKey("YOUR_API_KEY");

  var service = new MessagingHostedNumberOrderService();
  var options = new NewMessagingHostedNumberOrder
  {
      MessagingProfileId = "16fd2706-8baf-433b-82eb-8c7fada847da",
      PhoneNumbers = new List<string> { "+13125550001" }
  };
  var order = await service.CreateAsync(options);
  Console.WriteLine(order);
  ```

  ```php
  require_once 'vendor/autoload.php';

  Telnyx\Telnyx::setApiKey('YOUR_API_KEY');

  $order = Telnyx\MessagingHostedNumberOrder::create([
      'messaging_profile_id' => '16fd2706-8baf-433b-82eb-8c7fada847da',
      'phone_numbers' => ['+13125550001']
  ]);
  echo $order;
  ```

  ```go
  package main

  import (
      "context"
      "fmt"
      telnyx "github.com/telnyx/telnyx-go"
  )

  func main() {
      client := telnyx.NewClient("YOUR_API_KEY")

      order, err := client.MessagingHostedNumberOrders.Create(
          context.Background(),
          &telnyx.MessagingHostedNumberOrderParams{
              MessagingProfileID: "16fd2706-8baf-433b-82eb-8c7fada847da",
              PhoneNumbers:       []string{"+13125550001"},
          },
      )
      if err != nil {
          panic(err)
      }
      fmt.Println(order)
  }
  ```

### Example response

```json theme={null}
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

<Callout type="info">
  The response looks identical to a standard hosted SMS order. The internal transfer detection happens server-side — the current owner of the number will receive a notification automatically.

## Approve or reject a transfer

The current number owner can approve or reject the transfer using the link in their notification email, or via the API.

### Approve

```bash theme={null}
curl -X POST \
  --header "Authorization: Bearer CURRENT_OWNER_API_KEY" \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/approve?token=APPROVAL_TOKEN"
```

### Reject

```bash theme={null}
curl -X POST \
  --header "Authorization: Bearer CURRENT_OWNER_API_KEY" \
  "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/reject?token=APPROVAL_TOKEN"
```

<Callout type="info">
  The `token` parameter is included in the notification sent to the current owner. It is a one-time use token that expires after **72 hours**. If the token expires without action, the transfer is **automatically approved**.

| Decision            | Result                                                                                   |
| ------------------- | ---------------------------------------------------------------------------------------- |
| **Approved**        | Transfer proceeds. Receiving account must complete 2FA verification and document upload. |
| **Rejected**        | Order is marked as `failed`. The receiving account is notified.                          |
| **No action (72h)** | Transfer is **auto-approved**. Receiving account must still complete verification.       |

## Complete the transfer

After the transfer is approved (either explicitly or via auto-approval), the receiving account must:

1. **Verify ownership** — Send and validate verification codes for the number(s), identical to the [standard verification process](hosted-sms.md#validate-phone-numbers).

2. **Upload documents** — Submit the LOA and bill via the [file upload endpoint](hosted-sms.md#uploading-authorization-documents).

3. **Wait for activation** — The Telnyx team reviews and activates the transfer.

## Webhook notifications

Internal transfers generate the same webhook events as standard hosted SMS orders, plus additional events for approval status changes.

### Approval pending (order created)

```json theme={null}
{
  "data": {
    "event_type": "messaging_hosted_numbers_orders.created",
    "payload": {
      "order_status": "pending",
      "numbers": [{"status": "pending", "value": "+13125550001"}]
    }
  }
}
```

### Transfer approved

```json theme={null}
{
  "data": {
    "event_type": "messaging_hosted_numbers_orders.updated",
    "payload": {
      "order_status": "pending",
      "approval_decision": "approved"
    }
  }
}
```

### Transfer rejected

```json theme={null}
{
  "data": {
    "event_type": "messaging_hosted_numbers_orders.updated",
    "payload": {
      "order_status": "failed",
      "approval_decision": "rejected"
    }
  }
}
```

### Transfer activated

```json theme={null}
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

## Key differences from standard Hosted SMS

| Aspect               | Standard Hosted SMS | Internal Transfer                               |
| -------------------- | ------------------- | ----------------------------------------------- |
| **Source**           | External carrier    | Another Telnyx account                          |
| **Detection**        | Manual              | Automatic (system detects Telnyx-owned numbers) |
| **Approval**         | Not required        | Required from current owner (72h window)        |
| **Auto-approval**    | N/A                 | Yes, after 72 hours with no response            |
| **Campaign cleanup** | N/A                 | 10DLC campaigns automatically removed           |
| **Carrier porting**  | Yes (NNID override) | No (direct `user_id` update)                    |
| **2FA verification** | Required            | Required (after approval)                       |
| **LOA + Bill**       | Required            | Required                                        |

## Troubleshooting

**Transfer was auto-approved but I didn't want it**

  If the 72-hour window passed without action, the transfer is automatically approved. Contact [Telnyx Support](https://support.telnyx.com) immediately — the transfer may be reversible if activation hasn't completed.

---

**Verification code not received**

  Ensure the number can receive SMS messages. For internal transfers, the verification code is sent to the number being transferred. If the number is a landline or doesn't have SMS capabilities on the current account, contact [Telnyx Support](https://support.telnyx.com) for assistance.

---

**Order failed after approval**

  Check the order status for specific error details. Common causes include:

  * The number was deleted or deactivated on the source account before activation
  * The number is already hosted with another Telnyx subscriber
  * Billing issues on the receiving account

  Use the [Get Order](https://developers.telnyx.com/api-reference/hosted-numbers/get-hosted-number-order) endpoint to check the current status.

---

**10DLC campaigns were removed**

  This is expected behavior. When a number transfers between accounts, existing campaign associations are automatically cleaned up. Register the number with a new campaign on the receiving account after the transfer completes. See [10DLC Campaign Registration](../tutorial/getting-started-with-10dlc.md) for details.

---
