---
title: Short Codes
summary: Request and configure short codes for high-volume A2P messaging.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/short-code/index
    content_hash: 1d59788119a144498ea24868797d4b9f76cd3eaf9ffa2e6f54e7fcf71a6a8139
updated_at: 2026-04-10T00:00:00Z
---

# Short Codes

Request and configure short codes for high-volume A2P messaging. Understand provisioning timelines, carrier certification, and use cases.

Short codes are 5- or 6-digit phone numbers designed for high-volume, application-to-person (A2P) messaging. They offer the highest throughput of any sender type — up to **1,000 messages per second** — and are recognized by consumers as legitimate business numbers.

## When to use short codes

### Good fit

    * **High-volume alerts:** Time-sensitive notifications to large audiences
    * **Two-factor authentication:** OTP delivery at scale with high deliverability
    * **Marketing campaigns:** Promotional messages with keyword opt-in (e.g., "Text JOIN to 12345")
    * **Voting and polling:** Interactive SMS campaigns
    * **Emergency notifications:** Critical alerts requiring maximum throughput

### Consider alternatives

    | Need                            | Better option                                                                   |
    | ------------------------------- | ------------------------------------------------------------------------------- |
    | Low volume (\< 1,000 msgs/day)  | [10DLC Long Code](../tutorial/getting-started-with-10dlc.md)                       |
    | Quick setup (no 8-12 week wait) | [Toll-Free](toll-free-verification-with-business-registration-fields.md)                       |
    | Two-way conversations           | Long Code with [Sticky Sender](sticky-sender.md)    |
    | International messaging         | [Alphanumeric Sender ID](alphanumeric-sender-id.md) |
    | Budget-conscious                | 10DLC (lower per-message cost)                                                  |

***

## Short code vs. other sender types

| Feature               | Short Code                           | Toll-Free | 10DLC Long Code         |
| --------------------- | ------------------------------------ | --------- | ----------------------- |
| **Throughput**        | Up to 1,000 MPS                      | 20 MPS    | Varies by campaign      |
| **Setup time**        | 8-12 weeks                           | 1-2 weeks | Days                    |
| **Cost**              | Higher (monthly lease + per-message) | Moderate  | Lowest                  |
| **Carrier trust**     | Highest                              | High      | Varies by vetting score |
| **MMS support**       | Yes                                  | Yes       | Yes                     |
| **Two-way messaging** | Yes (keyword-based)                  | Yes       | Yes                     |
| **Vanity numbers**    | Available                            | No        | No                      |

***

## Provisioning process

1. **Request a short code**

    Navigate to [Short Code](https://portal.telnyx.com/#/messaging-short-code) in Mission Control and submit your request.

    **Choose your type:**

    | Type       | Description                                         | Timeline    |
    | ---------- | --------------------------------------------------- | ----------- |
    | **Random** | Carrier-assigned number                             | 8-10 weeks  |
    | **Vanity** | Memorable number you choose (e.g., 46835 = "GOULD") | 10-12 weeks |

    > **Note:** Vanity codes are subject to availability. Request early — popular combinations may already be taken.

2. **Complete your application**

    Provide details about your messaging program:

    * **Company information** — Legal name, address, contact
    * **Use case description** — What messages you'll send
    * **Message content samples** — Representative examples
    * **Volume estimates** — Expected daily/monthly message volume
    * **Opt-in flow** — How users subscribe (web form, keyword, etc.)
    * **Opt-out handling** — STOP keyword support
    * **Help response** — HELP keyword response content

3. **Carrier certification**

    Your application is submitted to each major US carrier for review and approval:

    | Carrier     | Review process                               |
    | ----------- | -------------------------------------------- |
    | AT\&T       | Reviews content, opt-in flow, and compliance |
    | T-Mobile    | Reviews content and message flow             |
    | Verizon     | Reviews content and use case                 |
    | US Cellular | Reviews content                              |

    > **Warning:** **This is the longest step.** Carrier certification typically takes **8-12 weeks**. Each carrier reviews independently — you may get approved by some carriers before others. Plan your launch timeline accordingly.

4. **Start messaging**

    Once approved by all target carriers, your short code appears under your messaging profile. Send messages using the same [Messaging API](send-your-first-message.md) as any other number type.

***

## Sending messages from a short code

Once provisioned, send messages the same way as any other sender type:

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "from": "12345",
      "to": "+15559876543",
      "text": "Your verification code is 847291. It expires in 5 minutes."
    }'
  ```

  ```python
  import os
  from telnyx import Telnyx

  client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

  response = client.messages.send(
      from_="12345",
      to="+15559876543",
      text="Your verification code is 847291. It expires in 5 minutes.",
  )

  print(f"Message sent: {response.data.id}")
  ```

  ```javascript
  import Telnyx from 'telnyx';

  const client = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

  const response = await client.messages.send({
    from: '12345',
    to: '+15559876543',
    text: 'Your verification code is 847291. It expires in 5 minutes.',
  });

  console.log(`Message sent: ${response.data.id}`);
  ```

  ```ruby
  require "telnyx"

  client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

  response = client.messages.send_(
    from: "12345",
    to: "+15559876543",
    text: "Your verification code is 847291. It expires in 5 minutes."
  )

  puts "Message sent: #{response.id}"
  ```

  ```go
  package main

  import (
    "context"
    "fmt"
    "os"

    "github.com/team-telnyx/telnyx-go"
    "github.com/team-telnyx/telnyx-go/option"
  )

  func main() {
    client := telnyx.NewClient(
      option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
    )
    response, err := client.Messages.Send(context.TODO(), telnyx.MessageSendParams{
      From: "12345",
      To:   "+15559876543",
      Text: "Your verification code is 847291. It expires in 5 minutes.",
    })
    if err != nil {
      panic(err.Error())
    }
    fmt.Printf("Message sent: %s\n", response.Data.ID)
  }
  ```

  ```java
  package com.telnyx.example;

  import com.telnyx.sdk.client.TelnyxClient;
  import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
  import com.telnyx.sdk.models.messages.MessageSendParams;

  public final class Main {
      public static void main(String[] args) {
          TelnyxClient client = TelnyxOkHttpClient.fromEnv();

          var params = MessageSendParams.builder()
              .from("12345")
              .to("+15559876543")
              .text("Your verification code is 847291. It expires in 5 minutes.")
              .build();

          var response = client.messages().send(params);
          System.out.println("Message sent: " + response.data().id());
      }
  }
  ```

  ```csharp .NET theme={null}
  using Telnyx;

  TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

  var service = new MessageService();
  var response = await service.SendAsync(new MessageSendOptions
  {
      From = "12345",
      To = "+15559876543",
      Text = "Your verification code is 847291. It expires in 5 minutes."
  });

  Console.WriteLine($"Message sent: {response.Data.Id}");
  ```

  ```php
  <?php
  require_once 'vendor/autoload.php';

  \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

  $response = \Telnyx\Message::Create([
      'from' => '12345',
      'to' => '+15559876543',
      'text' => 'Your verification code is 847291. It expires in 5 minutes.',
  ]);

  echo "Message sent: {$response->id}\n";
  ```

> **Note:** Short codes use **ASCII 7-bit** encoding by default (same character limits as GSM-7). See [Message Encoding](message-encoding.md) for details.

***

## Automated responses

Short codes must handle standard keywords to pass carrier certification. Telnyx manages these automatically.

### Required keywords

| Keyword                                       | Purpose           | Telnyx handling                                     |
| --------------------------------------------- | ----------------- | --------------------------------------------------- |
| **STOP** (and UNSUBSCRIBE, END, QUIT, CANCEL) | Opt-out           | Automatic — user is blocked from receiving messages |
| **HELP** (and INFO)                           | Help/support info | Automatic — sends your configured help message      |
| **Campaign keyword**                          | Campaign opt-in   | Automatic — sends your configured keyword response  |

### Customizing responses

After carrier certification, you can customize the HELP and campaign keyword responses:

**Custom HELP response**

    Configure a custom help message that includes:

    * Your business name
    * What messages the user is subscribed to
    * How to get support (phone number or email)
    * How to opt out

    **Example:**

    ```
    Acme Corp: You're subscribed to order updates. For help, call 1-800-555-0123 
    or email support@acme.com. Reply STOP to unsubscribe. Msg&data rates may apply.
    ```

---

**Custom keyword response**

    When a user texts your campaign keyword (e.g., "JOIN"), they receive a confirmation message.

    **Example:**

    ```
    Welcome to Acme Corp alerts! You'll receive order updates and promotions. 
    Reply HELP for help, STOP to cancel. Msg&data rates may apply. ~4 msgs/month.
    ```

---

**Disabling automatic responses**

    After certification, you can disable automatic responses for HELP and campaign keywords to handle them yourself via webhook. Contact [support@telnyx.com](mailto:support@telnyx.com) to request this change.

    > **Warning:** **STOP responses cannot be disabled.** Opt-out handling is managed at the carrier level. Once a user opts out, they are blocked from receiving messages — you cannot send a custom opt-out confirmation.

---

***

## Use case examples

**Two-factor authentication (2FA)**

    **Keyword:** N/A (API-triggered)
    **Flow:** User initiates login → your app sends OTP via short code → user enters code

    ```
    Your Acme verification code is 847291. It expires in 5 minutes. 
    If you didn't request this, ignore this message.
    ```

    **Why short code:** Highest deliverability, fastest delivery, trusted by carriers.

---

**Marketing opt-in campaign**

    **Keyword:** JOIN
    **Flow:** User texts JOIN to 12345 → receives welcome message → gets promotional messages

    ```
    Welcome msg: Acme Corp: Thanks for joining! Get exclusive deals and updates. 
    Reply HELP for help, STOP to cancel. Msg&data rates may apply. ~4 msgs/month.

    Promo msg: Acme Flash Sale! 30% off all items today only. Shop now: https://acme.com/sale
    Reply STOP to opt out.
    ```

---

**Emergency / mass notifications**

    **Keyword:** ALERT
    **Flow:** User opts in → receives critical alerts (weather, school closings, etc.)

    ```
    ALERT: Severe thunderstorm warning for Springfield County until 8 PM. 
    Seek shelter immediately. Updates at https://acme.com/alerts
    ```

    **Why short code:** Maximum throughput (1,000 MPS) for time-critical mass notifications.

---

***

## Carrier certification requirements

> **Warning:** Failing to meet these requirements will delay or prevent certification. Prepare these items before submitting your application.

| Requirement            | Details                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| **Opt-in mechanism**   | Clear, documented method for users to subscribe (web form, keyword, paper form)          |
| **Opt-in disclosure**  | Users must know what they're subscribing to, message frequency, and that rates may apply |
| **Opt-out support**    | Must honor STOP and similar keywords immediately                                         |
| **Help support**       | Must respond to HELP with business name, support contact, and opt-out instructions       |
| **Message frequency**  | Must disclose expected message frequency at opt-in                                       |
| **Content compliance** | Message content must match the registered use case                                       |
| **Privacy policy**     | Published privacy policy covering SMS data collection                                    |
| **Terms of service**   | Published terms covering messaging program                                               |

***

## Related resources

  - [Choosing Your Sender Type](../tutorial/choosing-a-sender-type.md) — Compare short codes, toll-free, long codes, and alphanumeric sender IDs.

  - [Rate Limiting](rate-limiting.md) — Short code throughput limits and queuing behavior.

  - [Advanced Opt-In/Out](advanced-opt-in-out-management.md) — Customize opt-in and opt-out behavior.

  - [Message Encoding](message-encoding.md) — Understand ASCII 7-bit encoding used by short codes.


## Related Pages

- [API error codes](../reference/api-error-codes.md)
