---
title: Schedule SMS and MMS Messages
summary: Schedule SMS and MMS messages for future delivery using the Telnyx Messaging API.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/schedule-message/index
    content_hash: c7b098a30433b1985cd99401b8cd6e3b9b84a3d0362dda35467af0ace87dd704
updated_at: 2026-04-10T00:00:00Z
---

# Schedule SMS and MMS Messages

Schedule SMS and MMS messages for future delivery using the Telnyx Messaging API. Send time-sensitive campaigns, reminders, and notifications at the perfect moment.

Schedule SMS and MMS messages to send at a specific time in the future. Use scheduled messaging for appointment reminders, marketing campaigns, time-zone-aware notifications, and any scenario where precise delivery timing matters.

## Prerequisites

* A [Telnyx account](https://telnyx.com/sign-up)
* A [Messaging Profile](send-your-first-message.md#2-create-a-messaging-profile) with an assigned phone number
* An [API key](https://portal.telnyx.com/#/app/api-keys)

## How scheduled messaging works

When you schedule a message, Telnyx stores it and delivers it at the specified time. Here's how it works:

1. You send a request with a `send_at` timestamp set in the future
2. Telnyx validates the request and returns a message resource with `status: "scheduled"`
3. At the scheduled time (accurate to the minute), Telnyx sends the message
4. Standard [webhooks](receiving-webhooks-for-messaging.md) fire as the message is processed and delivered

<Callout type="info">
  **Scheduling constraints:**

  * `send_at` must be at least **5 minutes** in the future
  * `send_at` must be no more than **5 days** in the future
  * Scheduling accuracy is up to **1 minute**
  * Maximum of **1 million** scheduled messages at any given time

## Schedule a message

You can schedule messages using either endpoint:

* **`POST /v2/messages`** — The standard send endpoint, with the `send_at` parameter added
* **`POST /v2/messages/schedule`** — A dedicated scheduling endpoint with the same parameters

Both endpoints accept identical parameters. The examples below use `/v2/messages` with `send_at`.

1. **Set your API key**

    Export your API key as an environment variable:

    ```bash theme={null}
    export TELNYX_API_KEY="YOUR_API_KEY"
    ```

2. **Choose your send time**

    The `send_at` field requires an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) formatted datetime string in UTC. For example:

    * `2026-02-15T14:30:00Z` — February 15, 2026 at 2:30 PM UTC
    * `2026-02-14T09:00:00-08:00` — February 14, 2026 at 9:00 AM PST

    <Callout type="tip">
      **Time zone tip:** Always convert your desired delivery time to UTC, or include the UTC offset. Messages are delivered based on the UTC time you specify, not the recipient's local time zone.

3. **Send the request**

### SMS

          ```bash
          curl -X POST https://api.telnyx.com/v2/messages \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $TELNYX_API_KEY" \
            -d '{
              "from": "+15551234567",
              "to": "+15559876543",
              "text": "Reminder: Your appointment is tomorrow at 10 AM.",
              "send_at": "2026-02-15T14:30:00Z"
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
              to="+15559876543",
              text="Reminder: Your appointment is tomorrow at 10 AM.",
              send_at="2026-02-15T14:30:00Z"
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
            to: '+15559876543',
            text: 'Reminder: Your appointment is tomorrow at 10 AM.',
            send_at: '2026-02-15T14:30:00Z'
          });

          console.log(response.data);
          ```

          ```ruby
          require "telnyx"

          client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

          response = client.messages.send_(
            from: "+15551234567",
            to: "+15559876543",
            text: "Reminder: Your appointment is tomorrow at 10 AM.",
            send_at: "2026-02-15T14:30:00Z"
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
              From:   "+15551234567",
              To:     "+15559876543",
              Text:   "Reminder: Your appointment is tomorrow at 10 AM.",
              SendAt: "2026-02-15T14:30:00Z",
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

          public final class Main {
              public static void main(String[] args) {
                  TelnyxClient client = TelnyxOkHttpClient.fromEnv();

                  MessageSendParams params = MessageSendParams.builder()
                      .from("+15551234567")
                      .to("+15559876543")
                      .text("Reminder: Your appointment is tomorrow at 10 AM.")
                      .sendAt("2026-02-15T14:30:00Z")
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
              To = "+15559876543",
              Text = "Reminder: Your appointment is tomorrow at 10 AM.",
              SendAt = "2026-02-15T14:30:00Z"
          });

          Console.WriteLine(response.Data);
          ```

          ```php
          <?php
          require_once 'vendor/autoload.php';

          \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

          $response = \Telnyx\Message::Create([
              'from' => '+15551234567',
              'to' => '+15559876543',
              'text' => 'Reminder: Your appointment is tomorrow at 10 AM.',
              'send_at' => '2026-02-15T14:30:00Z'
          ]);

          print_r($response);
          ```

### MMS

          ```bash
          curl -X POST https://api.telnyx.com/v2/messages \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $TELNYX_API_KEY" \
            -d '{
              "from": "+15551234567",
              "to": "+15559876543",
              "text": "Check out our weekend sale!",
              "subject": "Weekend Sale",
              "media_urls": ["https://example.com/sale-banner.jpg"],
              "send_at": "2026-02-15T14:30:00Z"
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
              to="+15559876543",
              text="Check out our weekend sale!",
              subject="Weekend Sale",
              media_urls=["https://example.com/sale-banner.jpg"],
              send_at="2026-02-15T14:30:00Z"
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
            to: '+15559876543',
            text: 'Check out our weekend sale!',
            subject: 'Weekend Sale',
            media_urls: ['https://example.com/sale-banner.jpg'],
            send_at: '2026-02-15T14:30:00Z'
          });

          console.log(response.data);
          ```

          ```ruby
          require "telnyx"

          client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

          response = client.messages.send_(
            from: "+15551234567",
            to: "+15559876543",
            text: "Check out our weekend sale!",
            subject: "Weekend Sale",
            media_urls: ["https://example.com/sale-banner.jpg"],
            send_at: "2026-02-15T14:30:00Z"
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
              To:        "+15559876543",
              Text:      "Check out our weekend sale!",
              Subject:   "Weekend Sale",
              MediaURLs: []string{"https://example.com/sale-banner.jpg"},
              SendAt:    "2026-02-15T14:30:00Z",
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
                      .to("+15559876543")
                      .text("Check out our weekend sale!")
                      .subject("Weekend Sale")
                      .mediaUrls(List.of("https://example.com/sale-banner.jpg"))
                      .sendAt("2026-02-15T14:30:00Z")
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
              To = "+15559876543",
              Text = "Check out our weekend sale!",
              Subject = "Weekend Sale",
              MediaUrls = new[] { "https://example.com/sale-banner.jpg" },
              SendAt = "2026-02-15T14:30:00Z"
          });

          Console.WriteLine(response.Data);
          ```

          ```php
          <?php
          require_once 'vendor/autoload.php';

          \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

          $response = \Telnyx\Message::Create([
              'from' => '+15551234567',
              'to' => '+15559876543',
              'text' => 'Check out our weekend sale!',
              'subject' => 'Weekend Sale',
              'media_urls' => ['https://example.com/sale-banner.jpg'],
              'send_at' => '2026-02-15T14:30:00Z'
          ]);

          print_r($response);
          ```

### Response

A successful response returns the message with `status: "scheduled"`:

```json theme={null}
{
  "data": {
    "record_type": "message",
    "direction": "outbound",
    "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
    "type": "SMS",
    "messaging_profile_id": "16fd2706-8baf-433b-82eb-8c7fada847da",
    "from": {
      "phone_number": "+15551234567"
    },
    "to": [
      {
        "phone_number": "+15559876543",
        "status": "scheduled"
      }
    ],
    "text": "Reminder: Your appointment is tomorrow at 10 AM.",
    "send_at": "2026-02-15T14:30:00Z"
  }
}
```

Save the `id` — you'll need it to retrieve or cancel the scheduled message.

## Retrieve a scheduled message

Check the status of a scheduled message with `GET /v2/messages/{id}`:

  ```bash
  curl -X GET https://api.telnyx.com/v2/messages/b0c7e8cb-6227-4c74-9f32-c7f80c30934b \
    -H "Authorization: Bearer $TELNYX_API_KEY"
  ```

  ```python
  import os
  from telnyx import Telnyx

  client = Telnyx(
      api_key=os.environ.get("TELNYX_API_KEY"),
  )

  response = client.messages.retrieve("b0c7e8cb-6227-4c74-9f32-c7f80c30934b")

  print(response.data)
  ```

  ```javascript
  import Telnyx from 'telnyx';

  const client = new Telnyx({
    apiKey: process.env['TELNYX_API_KEY'],
  });

  const response = await client.messages.retrieve(
    'b0c7e8cb-6227-4c74-9f32-c7f80c30934b'
  );

  console.log(response.data);
  ```

<Callout type="warning">
  The retrieve endpoint can only access messages created within the last **10 days**. For older messages, generate an [MDR report](https://portal.telnyx.com/#/app/reporting/mdr).

## Cancel a scheduled message

Cancel a message that hasn't been sent yet with `DELETE /v2/messages/{id}`:

  ```bash
  curl -X DELETE https://api.telnyx.com/v2/messages/b0c7e8cb-6227-4c74-9f32-c7f80c30934b \
    -H "Authorization: Bearer $TELNYX_API_KEY"
  ```

  ```python
  import os
  from telnyx import Telnyx

  client = Telnyx(
      api_key=os.environ.get("TELNYX_API_KEY"),
  )

  response = client.messages.delete("b0c7e8cb-6227-4c74-9f32-c7f80c30934b")

  print(response.data)
  ```

  ```javascript
  import Telnyx from 'telnyx';

  const client = new Telnyx({
    apiKey: process.env['TELNYX_API_KEY'],
  });

  const response = await client.messages.del(
    'b0c7e8cb-6227-4c74-9f32-c7f80c30934b'
  );

  console.log(response.data);
  ```

<Callout type="info">
  **Cancellation rules:**

  * The message must have `status: "scheduled"`
  * The `send_at` time must be more than **1 minute** in the future
  * Once a message begins sending, it cannot be cancelled

## Webhooks

Scheduled messages trigger the same [messaging webhooks](receiving-webhooks-for-messaging.md) as immediate messages. The webhook sequence is:

1. **`message.sent`** — Fires when the message is sent at the scheduled time
2. **`message.finalized`** — Fires when delivery is confirmed or fails

**Example webhook payload for a scheduled message**

  ```json theme={null}
  {
    "data": {
      "event_type": "message.sent",
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "occurred_at": "2026-02-15T14:30:01Z",
      "payload": {
        "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
        "direction": "outbound",
        "type": "SMS",
        "from": {
          "phone_number": "+15551234567"
        },
        "to": [
          {
            "phone_number": "+15559876543",
            "status": "sent"
          }
        ],
        "text": "Reminder: Your appointment is tomorrow at 10 AM."
      }
    }
  }
  ```

---

## Use cases

**Appointment reminders**

  Schedule reminders 24 hours before an appointment:

  ```python
  from datetime import datetime, timedelta, timezone
  import os
  from telnyx import Telnyx

  client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

  appointment_time = datetime(2026, 2, 16, 10, 0, tzinfo=timezone.utc)
  reminder_time = appointment_time - timedelta(hours=24)

  response = client.messages.send(
      from_="+15551234567",
      to="+15559876543",
      text=f"Reminder: Your appointment is tomorrow at {appointment_time.strftime('%I:%M %p')} UTC.",
      send_at=reminder_time.isoformat()
  )

  print(f"Reminder scheduled for {reminder_time.isoformat()}, message ID: {response.data.id}")
  ```

---

**Time-zone-aware campaigns**

  Send marketing messages during business hours in each recipient's time zone:

  ```python
  from datetime import datetime, timezone, timedelta
  import os
  from telnyx import Telnyx

  client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

  recipients = [
      {"number": "+15551234567", "tz_offset": -5},  # EST
      {"number": "+15559876543", "tz_offset": -8},  # PST
      {"number": "+15557654321", "tz_offset": -6},  # CST
  ]

  for recipient in recipients:
      # Send at 10:00 AM in each recipient's local time
      local_10am = datetime(2026, 2, 16, 10, 0, tzinfo=timezone(timedelta(hours=recipient["tz_offset"])))
      utc_time = local_10am.astimezone(timezone.utc)

      response = client.messages.send(
          from_="+15550001111",
          to=recipient["number"],
          text="Weekend flash sale! 20% off with code WEEKEND20.",
          send_at=utc_time.isoformat()
      )
      print(f"Scheduled for {recipient['number']} at {utc_time.isoformat()}")
  ```

---

## Limits and rate limiting

* **Scheduling window:** 5 minutes to 5 days in the future
* **Maximum scheduled messages:** 1 million at any given time
* **Accuracy:** Messages are sent within 1 minute of the scheduled time
* **Rate limits:** The same [rate limits](rate-limiting.md) apply to scheduled messages as to immediate messages — both when creating the scheduled message and when it's sent

## Comparison with other providers

| Feature                    | Telnyx                         | Twilio                          | Vonage                 |
| -------------------------- | ------------------------------ | ------------------------------- | ---------------------- |
| Scheduling window          | 5 min – 5 days                 | 15 min – 35 days                | Not natively supported |
| Cancellation               | ✅ Up to 1 min before send time | ✅ Up to 1 hour before send time | N/A                    |
| Dedicated endpoint         | ✅ `/v2/messages/schedule`      | ❌ Same endpoint only            | N/A                    |
| Requires Messaging Service | ❌ Optional                     | ✅ Required                      | N/A                    |
| Additional cost            | ❌ Free                         | ❌ Free                          | N/A                    |
| Accuracy                   | \~1 minute                     | \~15 minutes                    | N/A                    |

## Next steps

  - [Send Your First Message](send-your-first-message.md) — New to Telnyx messaging? Start here

  - [Receive Webhooks](receiving-webhooks-for-messaging.md) — Handle delivery confirmations and inbound messages

  - [Rate Limiting](rate-limiting.md) — Understand messaging throughput limits

  - [API Reference](https://developers.telnyx.com/api-reference/messages/send-a-message) — Full API parameter documentation


## Related Pages

- [Receive SMS and MMS Messages](../runbooks/receive-sms-and-mms-messages.md)
- [Send RCS Messages](../runbooks/send-rcs-messages.md)
