---
title: Choosing a Sender Type
summary: Compare long codes, toll-free, short codes, RCS, and alphanumeric sender IDs to find the best messaging channel for your business.
sources:
  - url: https://developers.telnyx.com/docs/messaging/getting-started/choosing-your-sender-type/index
    content_hash: 3a210d12ce3009e21ef4196e1e5a8bcbaf57c4c403e02e7bd246d755eb5e3cfc
updated_at: 2026-04-10T00:00:00Z
---

# Choosing a Sender Type

Compare long codes, toll-free, short codes, RCS, and alphanumeric sender IDs to find the best messaging channel for your business.

## Interactive Product Selector

Answer a few quick questions to get a personalized recommendation:

This is a high-level recommendation. Contact [Telnyx Sales](https://telnyx.com/contact-us) for detailed guidance on complex use cases.

***

## Use Case Decision Tree

Not sure which sender type fits? Start with your primary use case:

**🔔 Transactional alerts (OTPs, order updates, appointment reminders)**

    **Best options:**

    * **Toll-free** — Fast provisioning (2–3 days), high throughput, handset-level delivery receipts. Ideal for US/CA transactional messaging.
    * **10DLC long code** — Good alternative if you want a local presence. Requires brand + campaign registration (2–3 business days).
    * **Short code** — Best for very high volume (200+ MPS). Longer provisioning (2–6 weeks) and higher cost.

    For OTP/2FA specifically, see our [Two-Factor Authentication guide](../runbooks/two-factor-authentication-2fa-via-sms.md).

---

**📢 Marketing & promotional campaigns**

    **Best options:**

    * **10DLC long code** — Required for A2P marketing in the US. Register your brand and campaign through [10DLC registration](getting-started-with-10dlc.md).
    * **Toll-free** — Good for mixed marketing + transactional. Requires [toll-free verification](../runbooks/toll-free-verification-with-business-registration-fields.md).
    * **Short code** — Premium option for brand recognition and highest throughput.
    * **RCS** — Rich media cards, carousels, and suggested actions for supported devices.

---

**💬 Conversational / two-way messaging**

    **Best options:**

    * **10DLC long code** — Local number feel, supports voice + SMS on the same number.
    * **Toll-free** — Works well for two-way if local presence isn't important.
    * **RCS** — Rich interactive experience with read receipts, typing indicators, and suggested replies.

    > **Warning:** Alphanumeric sender IDs are **one-way only** — recipients cannot reply.

---

**🌍 International messaging**

    **Best options:**

    * **Alphanumeric sender ID** — Supported in 100+ countries. No number procurement needed. Great for brand recognition internationally.
    * **Local long codes** — Required in some countries. Use the coverage checker below for availability.

    US toll-free and short code numbers only work for US/CA destinations. For international, use alphanumeric IDs or local numbers.

---

**📱 Rich media experiences (images, buttons, carousels)**

    **Best options:**

    * **RCS** — Full rich media support: images, video, carousels, suggested actions, branded sender profiles.
    * **MMS via long code/toll-free** — Image and video support for US/CA only.

    See our [RCS Getting Started guide](rcs-getting-started.md) for details.

---

***

## Sender Comparison

### Capabilities at a Glance

|                         | **10DLC Long Code**     | **Toll-Free**   | **Short Code** | **RCS**          | **Alphanumeric** |
| ----------------------- | ----------------------- | --------------- | -------------- | ---------------- | ---------------- |
| **Brand Recognition**   | Local number            | Brand           | Brand          | Brand (verified) | Brand name       |
| **Throughput**          | 3–75 MPS\*              | 3–150 MPS       | 200+ MPS       | 100+ MPS         | 100+ MPS         |
| **Daily Volume Limits** | 10K–200K (T-Mobile)\*\* | Unlimited       | Unlimited      | Unlimited        | Unlimited        |
| **Two-Way Messaging**   | ✅ Yes                   | ✅ Yes           | ✅ Yes          | ✅ Yes            | ❌ No             |
| **Voice Support**       | ✅ Yes                   | ✅ Yes           | ❌ No           | ❌ No             | ❌ No             |
| **Delivery Receipts**   | Carrier only            | Handset         | Handset        | Handset          | Handset          |
| **MMS Support**         | US/CA only              | US/CA only      | US/CA only     | Rich media       | ❌ No             |
| **Opt-Out Management**  | Telnyx managed          | Network managed | Telnyx managed | Telnyx managed   | N/A              |

<sub>\* Throughput varies based on TCR Trust Score. \*\* T-Mobile daily limits based on TCR brand score; can be increased upon request.</sub>

### Registration & Cost Comparison

Understanding the time and cost investment for each sender type helps you plan your launch:

|                             | **10DLC Long Code**    | **Toll-Free**          | **Short Code**         | **RCS**             | **Alphanumeric** |
| --------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------- | ---------------- |
| **Provisioning Time**       | 2–3 business days      | 2–3 business days      | 2–6 weeks              | 6–10 weeks          | Instant          |
| **Registration Required**   | Brand + Campaign (TCR) | Toll-free verification | Carrier approval       | Google verification | None             |
| **Number Procurement Cost** | Low (\~\$1/mo)         | Low (\~\$2/mo)         | High (\~\$500–1000/mo) | Agent setup fee     | Free             |
| **Per-Message Cost**        | Standard rates         | Standard rates         | Premium rates          | Standard rates      | Standard rates   |
| **Renewal/Ongoing**         | Annual brand vetting   | One-time verification  | Monthly lease          | Ongoing             | None             |

  - [10DLC Registration](getting-started-with-10dlc.md) — Register your brand and campaign for US A2P messaging.

  - [Toll-Free Verification](../runbooks/toll-free-verification-with-business-registration-fields.md) — Verify your toll-free number for higher throughput.

  - [Short Code Setup](../runbooks/short-codes.md) — Apply for a dedicated short code.

  - [RCS Getting Started](rcs-getting-started.md) — Set up RCS business messaging with rich media.

  - [Alphanumeric Sender ID](../runbooks/alphanumeric-sender-id.md) — Send branded one-way messages internationally.

  - [Hosted SMS](../runbooks/hosted-sms.md) — Bring your existing numbers to Telnyx messaging.

***

## Check Coverage by Country

Sender type availability varies by country. Use the tool below to check which options are available for your destination:

### Key Regional Considerations

### United States & Canada

    * **10DLC** is required for A2P messaging to US mobile numbers (enforced by carriers since 2023)
    * **Toll-free** numbers work for both US and CA
    * **Short codes** are country-specific (US short codes don't work in CA and vice versa)
    * **MMS** is supported on long code, toll-free, and short code
    * **RCS** is available for Android users

### Europe

    * **Alphanumeric sender IDs** are widely supported and commonly used
    * Some countries require pre-registration of alphanumeric IDs (e.g., UK, France)
    * **Local long codes** may be required for two-way messaging
    * Short codes are available in select markets
    * GDPR compliance required for all messaging

### Latin America

    * **Alphanumeric sender IDs** supported in most countries
    * **Local long codes** recommended for better deliverability
    * Some carriers require pre-approved sender IDs or templates
    * WhatsApp is dominant — consider RCS as an alternative rich channel

### Asia Pacific

    * Regulations vary significantly by country
    * **India** requires DLT registration and approved templates
    * **Australia** supports alphanumeric IDs and local numbers
    * Some countries require local entity for number procurement
    * Check coverage tool above for specific country details

***

## Quick Start: Send Your First Message

Once you've chosen your sender type, sending a message uses the same API regardless of sender:

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "from": "+15551234567",
      "to": "+15559876543",
      "text": "Hello from Telnyx!"
    }'
  ```

  ```python
  import telnyx

  telnyx.api_key = "YOUR_API_KEY"

  message = telnyx.Message.create(
      from_="+15551234567",
      to="+15559876543",
      text="Hello from Telnyx!"
  )
  print(message.id)
  ```

  ```javascript Node.js theme={null}
  const telnyx = require('telnyx')('YOUR_API_KEY');

  const message = await telnyx.messages.create({
    from: '+15551234567',
    to: '+15559876543',
    text: 'Hello from Telnyx!'
  });
  console.log(message.data.id);
  ```

  ```ruby
  require 'telnyx'

  Telnyx.api_key = 'YOUR_API_KEY'

  message = Telnyx::Message.create(
    from: '+15551234567',
    to: '+15559876543',
    text: 'Hello from Telnyx!'
  )
  puts message.id
  ```

  ```java
  import com.telnyx.sdk.*;
  import com.telnyx.sdk.api.MessagesApi;
  import com.telnyx.sdk.model.CreateMessageRequest;

  ApiClient client = Configuration.getDefaultApiClient();
  client.setApiKey("YOUR_API_KEY");

  MessagesApi api = new MessagesApi(client);
  CreateMessageRequest request = new CreateMessageRequest()
      .from("+15551234567")
      .to("+15559876543")
      .text("Hello from Telnyx!");

  api.createMessage(request);
  ```

  ```csharp .NET theme={null}
  using Telnyx;

  TelnyxConfiguration.SetApiKey("YOUR_API_KEY");

  var service = new MessagingSenderIdService();
  var message = service.CreateMessage(new NewMessage
  {
      From = "+15551234567",
      To = "+15559876543",
      Text = "Hello from Telnyx!"
  });
  Console.WriteLine(message.Id);
  ```

  ```php
  require 'vendor/autoload.php';

  $telnyx = new \Telnyx\TelnyxClient('YOUR_API_KEY');

  $message = $telnyx->messages->create([
      'from' => '+15551234567',
      'to' => '+15559876543',
      'text' => 'Hello from Telnyx!'
  ]);
  echo $message->id;
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

      message, err := client.Messages.Create(context.Background(),
          &telnyx.MessageParams{
              From: "+15551234567",
              To:   "+15559876543",
              Text: "Hello from Telnyx!",
          },
      )
      if err != nil {
          panic(err)
      }
      fmt.Println(message.ID)
  }
  ```

  The `from` field determines your sender type automatically:

  * **Phone number** (`+15551234567`) → Long code or toll-free
  * **Short code** (`12345`) → Short code
  * **Alphanumeric** (`"MyBrand"`) → Alphanumeric sender ID

  You can also use a [Messaging Profile](https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage) to let Telnyx select the best sender from your number pool.

***

## Next Steps

  - [Send a Message](../runbooks/send-your-first-message.md) — Complete guide to sending your first SMS/MMS.

  - [Messaging Profiles](https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage) — Configure number pools, webhooks, and features.

  - [10DLC Rate Limits](../runbooks/10dlc-rate-limits-throughput.md) — Understand throughput tiers and daily caps.
