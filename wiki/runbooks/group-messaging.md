---
title: Group Messaging
summary: Send and receive group MMS messages to multiple recipients using the Telnyx Messaging API.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/group-messaging/index
    content_hash: 61ab8fcf8bcde95d16776dfef943c7cbc8155c5eff37637cab6b6b2f8fa294e0
updated_at: 2026-04-10T00:00:00Z
---

# Group Messaging

Send and receive group MMS messages to multiple recipients using the Telnyx Messaging API. Supports up to 8 participants per conversation.

Send group MMS messages to multiple recipients in a single API call. Group messaging uses the MMS protocol to create multi-party conversations where all participants can see and reply to each other — just like a group text on your phone.

## Prerequisites

* A [Telnyx account](https://telnyx.com/sign-up)
* A [Messaging Profile](send-your-first-message.md#2-create-a-messaging-profile) with an MMS-enabled phone number
* An [API key](https://portal.telnyx.com/#/app/api-keys)

## How group messaging works

Group messaging builds on the MMS protocol to enable multi-party conversations:

1. You send a message to the **`/v2/messages/group_mms`** endpoint with multiple `to` numbers
2. Telnyx delivers the message to all recipients as a group MMS conversation
3. When any recipient replies, all participants (including your Telnyx number) receive the reply
4. You receive inbound group messages via [webhooks](receiving-webhooks-for-messaging.md) with a `cc` field listing all participants

<Callout type="info">
  **Group messaging constraints:**

  * Maximum of **8 recipients** per conversation (plus the sender)
  * **MMS protocol only** — all messages are billed at MMS rates
  * **US and Canada destinations only**
  * Requires a **v2 webhook version** on your messaging profile for inbound messages
  * Charged **per recipient** — standard MMS rates plus carrier passthrough fees apply

## Send a group message

1. **Set your API key**

    Export your API key as an environment variable:

    ```bash theme={null}
    export TELNYX_API_KEY="YOUR_API_KEY"
    ```

2. **Send the request**

    Send a group MMS to multiple recipients. You can include text, media, or both.

### Text + Media

          ```bash
          curl -X POST https://api.telnyx.com/v2/messages/group_mms \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $TELNYX_API_KEY" \
            -d '{
              "from": "+15551234567",
              "to": ["+15559876543", "+15558765432"],
              "text": "Hey team, check out this photo!",
              "media_urls": ["https://example.com/photo.jpg"]
            }'
          ```

          ```python
          import os
          from telnyx import Telnyx

          client = Telnyx(
              api_key=os.environ.get("TELNYX_API_KEY"),
          )

          response = client.messages.send(
              from_="+15551234567",
              to=["+15559876543", "+15558765432"],
              text="Hey team, check out this photo!",
              media_urls=["https://example.com/photo.jpg"]
          )

          print(response.data)
          ```

          ```javascript
          import Telnyx from 'telnyx';

          const client = new Telnyx({
            apiKey: process.env['TELNYX_API_KEY'],
          });

          const response = await client.messages.send({
            from: '+15551234567',
            to: ['+15559876543', '+15558765432'],
            text: 'Hey team, check out this photo!',
            media_urls: ['https://example.com/photo.jpg']
          });

          console.log(response.data);
          ```

          ```ruby
          require "telnyx"

          client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

          response = client.messages.send_(
            from: "+15551234567",
            to: ["+15559876543", "+15558765432"],
            text: "Hey team, check out this photo!",
            media_urls: ["https://example.com/photo.jpg"]
          )

          puts(response)
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
              From:      "+15551234567",
              To:        []string{"+15559876543", "+15558765432"},
              Text:      "Hey team, check out this photo!",
              MediaURLs: []string{"https://example.com/photo.jpg"},
            })
            if err != nil {
              panic(err.Error())
            }
            fmt.Printf("%+v\n", response.Data)
          }
          ```

          ```java
          package com.telnyx.example;

          import com.telnyx.sdk.client.TelnyxClient;
          import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
          import com.telnyx.sdk.models.messages.MessageSendParams;
          import com.telnyx.sdk.models.messages.MessageSendResponse;
          import java.util.List;

          public final class Main {
              public static void main(String[] args) {
                  TelnyxClient client = TelnyxOkHttpClient.fromEnv();

                  MessageSendParams params = MessageSendParams.builder()
                      .from("+15551234567")
                      .to(List.of("+15559876543", "+15558765432"))
                      .text("Hey team, check out this photo!")
                      .mediaUrls(List.of("https://example.com/photo.jpg"))
                      .build();

                  MessageSendResponse response = client.messages().send(params);
                  System.out.println(response);
              }
          }
          ```

          ```csharp .NET theme={null}
          using Telnyx;

          TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

          var service = new MessageService();
          var response = await service.SendAsync(new MessageSendOptions
          {
              From = "+15551234567",
              To = new[] { "+15559876543", "+15558765432" },
              Text = "Hey team, check out this photo!",
              MediaUrls = new[] { "https://example.com/photo.jpg" }
          });

          Console.WriteLine(response.Data);
          ```

          ```php
          <?php
          require_once 'vendor/autoload.php';

          \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

          $response = \Telnyx\Message::Create([
              'from' => '+15551234567',
              'to' => ['+15559876543', '+15558765432'],
              'text' => 'Hey team, check out this photo!',
              'media_urls' => ['https://example.com/photo.jpg']
          ]);

          print_r($response);
          ```

### Text only

          ```bash
          curl -X POST https://api.telnyx.com/v2/messages/group_mms \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $TELNYX_API_KEY" \
            -d '{
              "from": "+15551234567",
              "to": ["+15559876543", "+15558765432"],
              "text": "Hey team, lunch at noon?"
            }'
          ```

          ```python
          import os
          from telnyx import Telnyx

          client = Telnyx(
              api_key=os.environ.get("TELNYX_API_KEY"),
          )

          response = client.messages.send(
              from_="+15551234567",
              to=["+15559876543", "+15558765432"],
              text="Hey team, lunch at noon?"
          )

          print(response.data)
          ```

          ```javascript
          import Telnyx from 'telnyx';

          const client = new Telnyx({
            apiKey: process.env['TELNYX_API_KEY'],
          });

          const response = await client.messages.send({
            from: '+15551234567',
            to: ['+15559876543', '+15558765432'],
            text: 'Hey team, lunch at noon?'
          });

          console.log(response.data);
          ```

          ```ruby
          require "telnyx"

          client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

          response = client.messages.send_(
            from: "+15551234567",
            to: ["+15559876543", "+15558765432"],
            text: "Hey team, lunch at noon?"
          )

          puts(response)
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
              From: "+15551234567",
              To:   []string{"+15559876543", "+15558765432"},
              Text: "Hey team, lunch at noon?",
            })
            if err != nil {
              panic(err.Error())
            }
            fmt.Printf("%+v\n", response.Data)
          }
          ```

          ```java
          package com.telnyx.example;

          import com.telnyx.sdk.client.TelnyxClient;
          import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
          import com.telnyx.sdk.models.messages.MessageSendParams;
          import com.telnyx.sdk.models.messages.MessageSendResponse;
          import java.util.List;

          public final class Main {
              public static void main(String[] args) {
                  TelnyxClient client = TelnyxOkHttpClient.fromEnv();

                  MessageSendParams params = MessageSendParams.builder()
                      .from("+15551234567")
                      .to(List.of("+15559876543", "+15558765432"))
                      .text("Hey team, lunch at noon?")
                      .build();

                  MessageSendResponse response = client.messages().send(params);
                  System.out.println(response);
              }
          }
          ```

          ```csharp .NET theme={null}
          using Telnyx;

          TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

          var service = new MessageService();
          var response = await service.SendAsync(new MessageSendOptions
          {
              From = "+15551234567",
              To = new[] { "+15559876543", "+15558765432" },
              Text = "Hey team, lunch at noon?"
          });

          Console.WriteLine(response.Data);
          ```

          ```php
          <?php
          require_once 'vendor/autoload.php';

          \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

          $response = \Telnyx\Message::Create([
              'from' => '+15551234567',
              'to' => ['+15559876543', '+15558765432'],
              'text' => 'Hey team, lunch at noon?'
          ]);

          print_r($response);
          ```

### Response

A successful response includes per-recipient status:

```json theme={null}
{
  "data": {
    "record_type": "message",
    "direction": "outbound",
    "id": "403188fd-58c5-4557-a8de-1700a358d768",
    "type": "MMS",
    "messaging_profile_id": "1e0df9c5-8716-4bcf-8fb2-9f6d9527fd95",
    "from": "+15551234567",
    "to": [
      {
        "phone_number": "+15559876543",
        "status": "queued",
        "carrier": "T-MOBILE USA, INC.",
        "line_type": "Wireless"
      },
      {
        "phone_number": "+15558765432",
        "status": "queued",
        "carrier": "CELLCO PARTNERSHIP DBA VERIZON WIRELESS",
        "line_type": "Wireless"
      }
    ],
    "text": "Hey team, check out this photo!",
    "media": [
      {
        "url": "https://example.com/photo.jpg",
        "content_type": null,
        "sha256": null,
        "size": null
      }
    ],
    "encoding": "GSM-7",
    "parts": 1,
    "cost": {
      "amount": "0.0800",
      "currency": "USD"
    }
  }
}
```

Save the `id` to correlate delivery webhooks with your group message.

## Receive group messages

When someone replies to the group conversation, you receive a `message.received` webhook. The `cc` field lists all other participants in the conversation:

**Example inbound group message webhook**

  ```json theme={null}
  {
    "data": {
      "event_type": "message.received",
      "id": "0d7c4fbe-d075-435f-b71b-694391743967",
      "occurred_at": "2023-08-08T13:03:05.129+00:00",
      "payload": {
        "cc": [
          "+15558765432",
          "+15557654321",
          "+15551234567"
        ],
        "direction": "inbound",
        "encoding": "UCS-2",
        "from": {
          "carrier": "AT&T",
          "line_type": "Wireless",
          "phone_number": "+15559876543"
        },
        "id": "9d12c9d0-5172-429a-8fb9-cc9da297717f",
        "media": [],
        "messaging_profile_id": "1e0df9c5-8716-4bcf-8fb2-9f6d9527fd95",
        "record_type": "message",
        "text": "Sounds good, see you at noon!",
        "to": [
          {
            "carrier": "Telnyx",
            "line_type": "Wireless",
            "phone_number": "+15551234567",
            "status": "webhook_delivered"
          }
        ],
        "type": "MMS"
      },
      "record_type": "event"
    }
  }
  ```

---

**Key fields for inbound group messages:**

| Field               | Description                                      |
| ------------------- | ------------------------------------------------ |
| `from.phone_number` | The participant who sent the reply               |
| `to`                | Your Telnyx number(s) in the conversation        |
| `cc`                | All other participants in the group conversation |

## Webhooks and delivery tracking

Group messages generate individual webhook events and detail records for each recipient:

* **Per-recipient webhooks:** You receive a separate `message.finalized` event for each recipient with their individual delivery status
* **`group_message_id`:** A unique identifier returned in the API response, webhooks, and detail records that lets you correlate all individual records back to the original group message
* **Non-Telnyx recipient status:** Handset delivery confirmation is not available for non-Telnyx recipients — their status will show as `unknown`

**Example delivery webhook**

  ```json theme={null}
  {
    "data": {
      "event_type": "message.finalized",
      "id": "b40653f5-91cd-46b1-9542-0c092bd29795",
      "occurred_at": "2023-08-08T10:29:36.090+00:00",
      "payload": {
        "direction": "outbound",
        "from": {
          "phone_number": "+15551234567"
        },
        "group_message_id": "403189d4-b1d6-4993-b263-6470e5224430",
        "id": "403189d4-b1d6-4993-b263-6470e5224430",
        "to": [
          {
            "phone_number": "+15559876543",
            "status": "delivered"
          }
        ],
        "text": "Hey team, check out this photo!",
        "type": "MMS"
      },
      "record_type": "event"
    }
  }
  ```

---

## Comparison with other providers

| Feature                | Telnyx                     | Twilio                                             | Vonage                   |
| ---------------------- | -------------------------- | -------------------------------------------------- | ------------------------ |
| Group MMS support      | ✅ Native, single API call  | ⚠️ Requires Conversations API                      | ❌ Not natively supported |
| Max participants       | 8 + sender                 | 10 total                                           | N/A                      |
| Dedicated endpoint     | ✅ `/v2/messages/group_mms` | ❌ Requires Conversations setup                     | N/A                      |
| Setup complexity       | Single POST request        | Multi-step (create conversation, add participants) | N/A                      |
| Per-recipient tracking | ✅ Individual webhooks      | ✅ Via Conversations events                         | N/A                      |
| US/Canada support      | ✅                          | ✅                                                  | N/A                      |

## Troubleshooting

**Messages not delivered to all recipients**

  * Verify all `to` numbers are valid US or Canadian wireless numbers
  * Group MMS requires MMS-capable handsets — landlines and some VoIP numbers won't receive them
  * Check that you haven't exceeded the 8-recipient limit

---

**Not receiving inbound group messages**

  * Ensure your messaging profile uses **v2 webhook version** — go to [Messaging](https://portal.telnyx.com/#/app/messaging), edit your profile, and confirm the webhook version
  * Verify your webhook URL is accessible and returning `200 OK`

---

**Status shows 'unknown' for recipients**

  This is expected for non-Telnyx recipients. The MMS protocol does not reliably support delivery receipts across all carriers. Only Telnyx-to-Telnyx messages will show confirmed delivery status.

---

## Next steps

  - [Send Your First Message](send-your-first-message.md) — New to Telnyx messaging? Start here

  - [Receive Webhooks](receiving-webhooks-for-messaging.md) — Handle delivery confirmations and inbound messages

  - [Choose a Sender Type](../tutorial/choosing-a-sender-type.md) — Learn about long codes, toll-free, and short codes

  - [API Reference](https://developers.telnyx.com/api-reference/messages/send-a-short-code-message) — Full messaging API documentation
