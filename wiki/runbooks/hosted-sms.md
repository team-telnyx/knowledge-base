---
title: Hosted SMS
summary: Bring your own phone number onto the Telnyx platform for SMS and MMS while keeping it with your current voice provider.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
    content_hash: 9b68f689ac5f06cd468de75445b9d2c1e6185d96e18cadfe0db417b77b81246a
updated_at: 2026-04-10T00:00:00Z
---

# Hosted SMS

Bring your own phone number onto the Telnyx platform for SMS and MMS while keeping it with your current voice provider. Complete guide with eligibility checks, verification, and order management.

Hosted SMS lets you add messaging capabilities to phone numbers that stay with your current voice provider. Your existing voice service continues uninterrupted — Telnyx handles only the SMS and MMS routing.

This is ideal for:

* **Landline numbers** that need texting capabilities
* **Business numbers** where you want to keep your voice provider but add programmable messaging
* **Gradual migration** — test Telnyx messaging before a full port

  Hosting a number is **not** the same as porting. Your voice service stays with your current provider. Only SMS/MMS traffic routes through Telnyx.

## How it works

```mermaid theme={null}
flowchart LR
    A[Check Eligibility] --> B[Create Order]
    B --> C[Verify Ownership]
    C --> D[Upload LOA + Bill]
    D --> E[Telnyx Review]
    E --> F[Number Active]
```

| Step                     | What happens                             | Timeline          |
| ------------------------ | ---------------------------------------- | ----------------- |
| **1. Eligibility check** | Verify your numbers can be hosted        | Instant           |
| **2. Create order**      | Submit a hosted SMS order                | Instant           |
| **3. Verify ownership**  | Confirm you own the numbers via SMS code | 5 minutes         |
| **4. Upload documents**  | Submit LOA and recent provider bill      | Instant           |
| **5. Telnyx review**     | Our team reviews and activates           | 1-3 business days |

***

## Step 1: Check number eligibility

Not all numbers can be hosted. Check eligibility before creating an order.

### API

      ```bash
      curl -X POST https://api.telnyx.com/v2/messaging_hosted_number_orders/eligibility_numbers_check \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
          "phone_numbers": ["+13125550001", "+13125550002"]
        }'
      ```

      ```python
      import os
      import requests

      API_KEY = os.environ.get("TELNYX_API_KEY")
      headers = {
          "Authorization": f"Bearer {API_KEY}",
          "Content-Type": "application/json",
      }

      response = requests.post(
          "https://api.telnyx.com/v2/messaging_hosted_number_orders/eligibility_numbers_check",
          headers=headers,
          json={"phone_numbers": ["+13125550001", "+13125550002"]},
      )
      results = response.json()["phone_numbers"]
      for num in results:
          status = "✓" if num["eligible"] else "✗"
          print(f"{status} {num['phone_number']}: {num['detail']}")
      ```

      ```javascript
      const axios = require('axios');

      const headers = {
        Authorization: `Bearer ${process.env.TELNYX_API_KEY}`,
        'Content-Type': 'application/json',
      };

      const response = await axios.post(
        'https://api.telnyx.com/v2/messaging_hosted_number_orders/eligibility_numbers_check',
        { phone_numbers: ['+13125550001', '+13125550002'] },
        { headers }
      );

      response.data.phone_numbers.forEach((num) => {
        const status = num.eligible ? '✓' : '✗';
        console.log(`${status} ${num.phone_number}: ${num.detail}`);
      });
      ```

      ```ruby
      require "net/http"
      require "json"
      require "uri"

      uri = URI("https://api.telnyx.com/v2/messaging_hosted_number_orders/eligibility_numbers_check")
      http = Net::HTTP.new(uri.host, uri.port)
      http.use_ssl = true

      request = Net::HTTP::Post.new(uri)
      request["Authorization"] = "Bearer #{ENV['TELNYX_API_KEY']}"
      request["Content-Type"] = "application/json"
      request.body = { phone_numbers: ["+13125550001", "+13125550002"] }.to_json

      response = http.request(request)
      results = JSON.parse(response.body)["phone_numbers"]
      results.each do |num|
        status = num["eligible"] ? "✓" : "✗"
        puts "#{status} #{num['phone_number']}: #{num['detail']}"
      end
      ```

      ```go
      package main

      import (
      	"bytes"
      	"encoding/json"
      	"fmt"
      	"net/http"
      	"os"
      )

      func main() {
      	data := map[string][]string{
      		"phone_numbers": {"+13125550001", "+13125550002"},
      	}
      	body, _ := json.Marshal(data)
      	req, _ := http.NewRequest("POST",
      		"https://api.telnyx.com/v2/messaging_hosted_number_orders/eligibility_numbers_check",
      		bytes.NewBuffer(body))
      	req.Header.Set("Authorization", "Bearer "+os.Getenv("TELNYX_API_KEY"))
      	req.Header.Set("Content-Type", "application/json")

      	resp, _ := http.DefaultClient.Do(req)
      	defer resp.Body.Close()

      	var result map[string]interface{}
      	json.NewDecoder(resp.Body).Decode(&result)
      	numbers := result["phone_numbers"].([]interface{})
      	for _, n := range numbers {
      		num := n.(map[string]interface{})
      		eligible := num["eligible"].(bool)
      		symbol := "✗"
      		if eligible {
      			symbol = "✓"
      		}
      		fmt.Printf("%s %s: %s\n", symbol, num["phone_number"], num["detail"])
      	}
      }
      ```

      ```php
      <?php
      $apiKey = getenv('TELNYX_API_KEY');

      $data = ['phone_numbers' => ['+13125550001', '+13125550002']];

      $ch = curl_init('https://api.telnyx.com/v2/messaging_hosted_number_orders/eligibility_numbers_check');
      curl_setopt_array($ch, [
          CURLOPT_POST => true,
          CURLOPT_RETURNTRANSFER => true,
          CURLOPT_HTTPHEADER => [
              "Authorization: Bearer {$apiKey}",
              'Content-Type: application/json',
          ],
          CURLOPT_POSTFIELDS => json_encode($data),
      ]);

      $response = json_decode(curl_exec($ch), true);
      curl_close($ch);

      foreach ($response['phone_numbers'] as $num) {
          $status = $num['eligible'] ? '✓' : '✗';
          echo "{$status} {$num['phone_number']}: {$num['detail']}\n";
      }
      ```

      ```csharp .NET theme={null}
      using System.Net.Http.Headers;
      using System.Text;
      using System.Text.Json;

      var apiKey = Environment.GetEnvironmentVariable("TELNYX_API_KEY");
      var client = new HttpClient();
      client.DefaultRequestHeaders.Authorization =
          new AuthenticationHeaderValue("Bearer", apiKey);

      var data = new { phone_numbers = new[] { "+13125550001", "+13125550002" } };
      var json = JsonSerializer.Serialize(data);
      var content = new StringContent(json, Encoding.UTF8, "application/json");

      var response = await client.PostAsync(
          "https://api.telnyx.com/v2/messaging_hosted_number_orders/eligibility_numbers_check",
          content);
      var result = await response.Content.ReadAsStringAsync();

      using var doc = JsonDocument.Parse(result);
      foreach (var num in doc.RootElement.GetProperty("phone_numbers").EnumerateArray())
      {
          var eligible = num.GetProperty("eligible").GetBoolean();
          var symbol = eligible ? "✓" : "✗";
          Console.WriteLine($"{symbol} {num.GetProperty("phone_number")}: {num.GetProperty("detail")}");
      }
      ```

### Portal

    The Portal automatically checks eligibility when you enter numbers during order creation (Step 2).

### Eligibility statuses

| Status                                           | Description                           | Action                                   |
| ------------------------------------------------ | ------------------------------------- | ---------------------------------------- |
| `eligible`                                       | Number can be hosted                  | Proceed with order                       |
| `number_is_not_a_us_number`                      | Only US numbers supported             | Use a US number                          |
| `number_can_not_be_wireless`                     | Wireless numbers not supported        | Use a landline or VoIP number            |
| `number_can_not_be_in_telnyx`                    | Already on Telnyx platform            | No hosting needed — number already works |
| `number_can_not_hosted_with_a_telnyx_subscriber` | Already hosted by another Telnyx user | Contact support                          |
| `number_can_not_be_active_in_your_account`       | Active in your account already        | Check your number inventory              |
| `number_is_not_a_valid_routing_number`           | Invalid routing number                | Verify the number with your provider     |
| `number_is_not_in_e164_format`                   | Wrong format                          | Use E.164: `+1` followed by 10 digits    |
| `billing_account_check_failed`                   | Billing issue                         | Check your account billing status        |
| `billing_account_is_abolished`                   | Account closed                        | Contact support                          |

***

## Step 2: Create a hosted SMS order

### API

      ```bash
      curl -X POST https://api.telnyx.com/v2/messaging_hosted_number_orders \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
          "messaging_profile_id": "YOUR_MESSAGING_PROFILE_ID",
          "phone_numbers": ["+13125550001"]
        }'
      ```

      ```python
      response = requests.post(
          "https://api.telnyx.com/v2/messaging_hosted_number_orders",
          headers=headers,
          json={
              "messaging_profile_id": "YOUR_MESSAGING_PROFILE_ID",
              "phone_numbers": ["+13125550001"],
          },
      )
      order = response.json()
      print(f"Order ID: {order['id']}")
      print(f"Status: {order['status']}")
      for num in order["phone_numbers"]:
          print(f"  {num['phone_number']}: {num['status']}")
      ```

      ```javascript
      const response = await axios.post(
        'https://api.telnyx.com/v2/messaging_hosted_number_orders',
        {
          messaging_profile_id: 'YOUR_MESSAGING_PROFILE_ID',
          phone_numbers: ['+13125550001'],
        },
        { headers }
      );

      const order = response.data;
      console.log(`Order ID: ${order.id}`);
      console.log(`Status: ${order.status}`);
      order.phone_numbers.forEach((n) => {
        console.log(`  ${n.phone_number}: ${n.status}`);
      });
      ```

      ```ruby
      request = Net::HTTP::Post.new(URI("https://api.telnyx.com/v2/messaging_hosted_number_orders"))
      request["Authorization"] = "Bearer #{ENV['TELNYX_API_KEY']}"
      request["Content-Type"] = "application/json"
      request.body = {
        messaging_profile_id: "YOUR_MESSAGING_PROFILE_ID",
        phone_numbers: ["+13125550001"]
      }.to_json

      response = Net::HTTP.start("api.telnyx.com", 443, use_ssl: true) { |http| http.request(request) }
      order = JSON.parse(response.body)
      puts "Order ID: #{order['id']}"
      puts "Status: #{order['status']}"
      ```

    > **Note:** Numbers are created in `pending` status. They stay pending until you complete verification and document upload.

### Portal

1. **Navigate to Hosted SMS**

        Go to [Numbers → Hosted SMS](https://portal.telnyx.com/#/app/numbers/hosted-sms) in Mission Control.

2. **Create new order**

        Click [Add New Order](https://portal.telnyx.com/#/app/numbers/hosted-sms/new).

3. **Enter numbers**

        Enter the phone number(s) you want to host in E.164 format (e.g., `+13125550001`). The system automatically checks eligibility.

4. **Select messaging profile**

        Choose the [messaging profile](../concepts/messaging-profiles-overview.md) for these numbers.

5. **Create order**

        Click **Create Order** to proceed to document upload.

***

## Step 3: Verify phone number ownership

Prove you own the numbers by receiving and entering SMS verification codes.

### 3a. Request verification codes

  ```bash
  curl -X POST \
    "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/verification_codes" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "verification_method": "sms",
      "phone_numbers": ["+13125550001"]
    }'
  ```

  ```python
  response = requests.post(
      f"https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/verification_codes",
      headers=headers,
      json={
          "verification_method": "sms",
          "phone_numbers": ["+13125550001"],
      },
  )
  # 201 = codes sent successfully
  print(f"Codes sent: {response.status_code == 201}")
  ```

  ```javascript
  const response = await axios.post(
    `https://api.telnyx.com/v2/messaging_hosted_number_orders/${orderId}/verification_codes`,
    {
      verification_method: 'sms',
      phone_numbers: ['+13125550001'],
    },
    { headers }
  );
  console.log(`Codes sent: ${response.status === 201}`);
  ```

### 3b. Submit verification codes

  ```bash
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

  ```python
  response = requests.post(
      f"https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/validation_codes",
      headers=headers,
      json={
          "verification_codes": [
              {"phone_number": "+13125550001", "code": "87643"},
          ],
      },
  )
  result = response.json()
  for num in result["phone_numbers"]:
      print(f"{num['phone_number']}: {num['status']}")
  ```

  ```javascript
  const response = await axios.post(
    `https://api.telnyx.com/v2/messaging_hosted_number_orders/${orderId}/validation_codes`,
    {
      verification_codes: [
        { phone_number: '+13125550001', code: '87643' },
      ],
    },
    { headers }
  );

  response.data.phone_numbers.forEach((n) => {
    console.log(`${n.phone_number}: ${n.status}`);
  });
  ```

A successful verification returns `verified` status. The number status then changes to `ownership_successful`.

***

## Step 4: Upload authorization documents

After verification, upload two PDF documents:

1. **Letter of Authorization (LOA)** — signed authorization to host the number
2. **Recent bill** — from your current voice provider showing the number

  ```bash
  curl -X POST \
    "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/actions/file_upload" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    --form "loa=@/path/to/loa.pdf" \
    --form "bill=@/path/to/bill.pdf"
  ```

  ```python
  import requests

  with open("loa.pdf", "rb") as loa, open("bill.pdf", "rb") as bill:
      response = requests.post(
          f"https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}/actions/file_upload",
          headers={"Authorization": f"Bearer {API_KEY}"},
          files={"loa": loa, "bill": bill},
      )
  print(f"Upload status: {response.json()['status']}")
  ```

  ```javascript
  const FormData = require('form-data');
  const fs = require('fs');

  const form = new FormData();
  form.append('loa', fs.createReadStream('loa.pdf'));
  form.append('bill', fs.createReadStream('bill.pdf'));

  const response = await axios.post(
    `https://api.telnyx.com/v2/messaging_hosted_number_orders/${orderId}/actions/file_upload`,
    form,
    {
      headers: {
        ...form.getHeaders(),
        Authorization: `Bearer ${process.env.TELNYX_API_KEY}`,
      },
    }
  );
  console.log(`Upload status: ${response.data.status}`);
  ```

After upload, the Telnyx team reviews your order and activates the number(s). This typically takes **1-3 business days**.

***

## Check order status

  ```bash
  curl -s "https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}" \
    -H "Authorization: Bearer YOUR_API_KEY" | jq '{status, phone_numbers: [.phone_numbers[] | {phone_number, status}]}'
  ```

  ```python
  response = requests.get(
      f"https://api.telnyx.com/v2/messaging_hosted_number_orders/{order_id}",
      headers=headers,
  )
  order = response.json()
  print(f"Order status: {order['status']}")
  for num in order["phone_numbers"]:
      print(f"  {num['phone_number']}: {num['status']}")
  ```

### Order statuses

| Status                | Meaning                                                                    |
| --------------------- | -------------------------------------------------------------------------- |
| `pending`             | Order created, awaiting verification and documents                         |
| `loa_file_successful` | Documents uploaded successfully                                            |
| `successful`          | Order complete — numbers are active                                        |
| `failed`              | Activation failed (see [failure statuses](#troubleshooting-failed-orders)) |
| `deleted`             | Order was cancelled                                                        |

***

## Webhook notifications

Hosted SMS orders trigger webhooks to your [messaging profile's](https://portal.telnyx.com/#/programmable-messaging/profiles) configured webhook URL. Set up a handler to track order progress in real time.

  ```python
  from flask import Flask, request

  app = Flask(__name__)

  @app.route("/webhooks/hosted-sms", methods=["POST"])
  def hosted_sms_webhook():
      event = request.json["data"]
      event_type = event["event_type"]
      payload = event["payload"]

      order_id = payload["order_id"]
      order_status = payload["order_status"]

      print(f"Event: {event_type}")
      print(f"Order {order_id}: {order_status}")

      for num in payload.get("numbers", []):
          print(f"  {num['value']}: {num['status']}")

      # Handle specific events
      if order_status == "successful":
          print("Numbers are active! Ready to send messages.")
      elif order_status == "failed":
          print("Order failed. Check number statuses for details.")

      return "", 200
  ```

  ```javascript
  const express = require('express');
  const app = express();
  app.use(express.json());

  app.post('/webhooks/hosted-sms', (req, res) => {
    const event = req.body.data;
    const { event_type, payload } = event;

    console.log(`Event: ${event_type}`);
    console.log(`Order ${payload.order_id}: ${payload.order_status}`);

    for (const num of payload.numbers || []) {
      console.log(`  ${num.value}: ${num.status}`);
    }

    if (payload.order_status === 'successful') {
      console.log('Numbers are active! Ready to send messages.');
    } else if (payload.order_status === 'failed') {
      console.log('Order failed. Check number statuses for details.');
    }

    res.sendStatus(200);
  });
  ```

### Webhook event types

| Event                                     | Triggered when                                                 |
| ----------------------------------------- | -------------------------------------------------------------- |
| `messaging_hosted_numbers_orders.created` | Order is created                                               |
| `messaging_hosted_numbers_orders.updated` | Status changes (verification, LOA upload, activation, failure) |
| `messaging_hosted_numbers_orders.deleted` | Order is deleted                                               |

### Email and Portal notifications

You can also receive email notifications:

6. **Create notification profile**

    Go to [Advanced Features → Notifications](https://portal.telnyx.com/#/advanced-features/notifications) and click **New Profile**.

7. **Add email channel**

    Click **New Channel**, select your profile, choose **Email**, and enter your address.

8. **Configure settings**

    Click **New Settings**, select **Messaging Hosted SMS Activity**, and link to your profile.

***

## Troubleshooting failed orders

**Order status: carrier_rejected**

    **Cause:** The losing carrier (your current voice provider) rejected the hosting request.

    **Common reasons:**

    * Number is under contract with restrictions on SMS routing changes
    * Provider doesn't support hosted SMS arrangements
    * Account information mismatch between LOA and provider records

    **Fix:**

    * Contact your voice provider to understand the rejection
    * Verify your LOA matches the account holder name exactly
    * Some carriers require you to call and authorize the SMS routing change

---

**Order status: ineligible_carrier**

    **Cause:** The number's carrier does not support hosted SMS with Telnyx.

    **Fix:**

    * Consider porting the number fully to Telnyx instead
    * Contact Telnyx support to check if the carrier has been added since your last attempt

---

**Number status: failed_carrier_rejected**

    **Cause:** Specific number was rejected by the losing carrier while other numbers in the order may have succeeded.

    **Fix:**

    * Check if this specific number has different account ownership
    * Create a separate order for this number after resolving with your provider

---

**Number status: failed_number_already_hosted**

    **Cause:** The number is already hosted on Telnyx by another account.

    **Fix:**

    * If you own both accounts, remove the hosting from the other account first
    * If not, contact Telnyx support to resolve the conflict

---

**Number status: failed_timeout**

    **Cause:** The activation process timed out waiting for carrier response.

    **Fix:**

    * Create a new order for the same number
    * If it fails again, contact Telnyx support — the carrier may need manual intervention

---

**Verification code not received**

    **Cause:** The SMS verification code wasn't delivered to the phone number.

    **Fix:**

    * Ensure the number can receive SMS (landlines may need the current provider to enable it)
    * Check if the number has any SMS blocking enabled
    * Request the code again — you can retry multiple times
    * If the number truly cannot receive SMS, contact Telnyx support for alternative verification

---

**LOA rejected**

    **Cause:** The Letter of Authorization didn't meet requirements.

    **Common issues:**

    * LOA not signed
    * Name on LOA doesn't match the voice provider account
    * LOA template is outdated

    **Fix:**

    * Download the latest LOA template from Telnyx support
    * Ensure the authorized signer matches the account holder
    * Upload a new LOA via the API or Portal

---

**Hosted numbers not visible in Portal**

    **Known limitation:** Hosted numbers may not appear in the Portal number inventory. They are accessible via the API.

    ```bash theme={null}
    # List your hosted numbers
    curl -s "https://api.telnyx.com/v2/messaging_hosted_number_orders" \
      -H "Authorization: Bearer YOUR_API_KEY" | jq '.data[] | select(.status == "successful")'
    ```

---

***

## Failed order and number statuses reference

### Order statuses

| Status               | Description                                 |
| -------------------- | ------------------------------------------- |
| `carrier_rejected`   | Losing carrier rejected the porting request |
| `failed`             | Order closed — contact support              |
| `ineligible_carrier` | Number's carrier doesn't support hosted SMS |

### Number statuses

| Status                         | Description                                 |
| ------------------------------ | ------------------------------------------- |
| `failed`                       | Number closed — contact support             |
| `failed_carrier_rejected`      | Losing carrier rejected this number         |
| `failed_ineligible_carrier`    | Number's carrier doesn't support hosted SMS |
| `failed_number_already_hosted` | Already hosted by another Telnyx user       |
| `failed_number_not_found`      | Number not found in routing database        |
| `failed_timeout`               | Activation timed out                        |

***

## Next steps

  - [Internal Transfer](internal-hosted-sms-transfer.md) — Transfer hosted numbers between Telnyx accounts.

  - [Messaging Profiles](../concepts/messaging-profiles-overview.md) — Configure webhooks, opt-out settings, and number assignment.

  - [Send Your First Message](send-your-first-message.md) — Start sending SMS and MMS once your hosted numbers are active.

  - [Choosing Your Sender Type](../tutorial/choosing-a-sender-type.md) — Compare hosted SMS with other number types (10DLC, toll-free, short code).
