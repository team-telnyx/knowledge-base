---
title: Send and Receive Messages with the Telnyx Messaging API
summary: Walks through sending your first SMS and MMS with the Telnyx Messaging API,
  including setup, code samples in multiple languages, error handling, rate limiting,
  webhook-based delivery tracking, and inbound MMS processing.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/send-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-receive-mms/index
updated_at: 2026-08-05T13:58:28Z
---

# Send and Receive Messages with the Telnyx Messaging API

*Part 1 of 6 — see also: [Part 2](send-and-receive-messages-with-the-telnyx-messaging-api--part-2.md), [Part 3](send-and-receive-messages-with-the-telnyx-messaging-api--part-3.md), [Part 4](send-and-receive-messages-with-the-telnyx-messaging-api--part-4.md), [Part 5](send-and-receive-messages-with-the-telnyx-messaging-api--part-5.md), [Part 6](send-and-receive-messages-with-the-telnyx-messaging-api--part-6.md)*

Walks through sending your first SMS and MMS with the Telnyx Messaging API, including setup, code samples in multiple languages, error handling, rate limiting, webhook-based delivery tracking, and inbound MMS processing.

## Prerequisites

To get started with the Telnyx Messaging API you need:

- A [Telnyx account](https://telnyx.com/sign-up) (free to create)
- An [API key](https://portal.telnyx.com/#/app/api-keys)
- A [messaging profile](https://portal.telnyx.com/#/app/messaging) with a phone number enabled for SMS (and MMS, if you plan to send media)
- A webhook endpoint to receive inbound messages and delivery events (see [Webhooks and Delivery Tracking](webhooks-and-delivery-tracking.md) below and the [ngrok setup](/development/development-tools/ngrok-setup/index) guide for local development)

MMS is supported on US/Canada long codes, toll-free, and short codes. For media format details and carrier limits, see [MMS Media & Transcoding](mms-media-transcoding.md).

## Get Two Phone Numbers

Purchase two Telnyx numbers so you can test messaging between them without registration requirements.

1. Navigate to [Numbers > Search & Buy](https://portal.telnyx.com/#/app/numbers/search-numbers) in the portal.
2. Enter your preferred area code or region, check **SMS** under features, and click **Search**.
3. Click **Add to Cart** on two numbers, then **Place Order**.

Having two numbers lets you test on-net (Telnyx-to-Telnyx) messaging immediately, and also test receiving inbound messages.

## Create a Messaging Profile

1. Navigate to [Messaging](https://portal.telnyx.com/#/app/messaging) in the portal.
2. Click **Add new profile**, give it a name (e.g., "My App"), and click **Save**.
3. Go to [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers), and for each number, click the **Messaging Profile** dropdown, select your profile, and save.

## Send an SMS

Replace the placeholder values in the request below:

- `YOUR_API_KEY`: Your API key from the API Keys page
- `from`: Your first Telnyx number (the sender)
- `to`: Your second Telnyx number (the recipient)

**E.164 format is required.** Always include the `+` prefix, country code, and full number with no spaces or punctuation.

International number format examples:

| Country | Format | Example |
| --- | --- | --- |
| US/Canada | +1 + 10 digits | `+15551234567` |
| UK | +44 + 10-11 digits (drop leading 0) | `+447911123456` |
| Germany | +49 + 10-11 digits (drop leading 0) | `+4915123456789` |
| Australia | +61 + 9 digits (drop leading 0) | `+61412345678` |
| Brazil | +55 + 10-11 digits | `+5511987654321` |
| India | +91 + 10 digits | `+919876543210` |

Common mistakes:

- ❌ `15551234567` (missing `+`)
- ❌ `+1 (555) 123-4567` (contains spaces and punctuation)
- ❌ `+1-555-123-4567` (contains dashes)
- ✅ `+15551234567`

Sending to non-Telnyx numbers? Off-net messaging to external carriers typically requires sender registration (10DLC, toll-free verification, etc.). See [Next Steps](next-steps.md) for registration guides.

### cURL

```
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "+15551234567",
    "to": "+15559876543",
    "text": "Hello, world!"
  }'
```

### Node

```
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'],
});

const response = await client.messages.send({
  from: '+15551234567',
  to: '+15559876543',
  text: 'Hello, world!'
});

console.log(response.data);
```

### Python

```
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),
)

response = client.messages.send(
    from_="+15551234567",
    to="+15559876543",
    text="Hello, world!"
)

print(response.data)
```

### Ruby

```
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

response = client.messages.send_(
  from: "+15551234567",
  to: "+15559876543",
  text: "Hello, world!"
)

puts(response)
```

### Go

```
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
    To:   "+15559876543",
    Text: "Hello, world!",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.Data)
}
```

### Java

```
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
            .text("Hello, world!")
            .build();

        MessageSendResponse response = client.messages().send(params);
        System.out.println(response);
    }
}
```

### .NET

```
using Telnyx;

TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

var service = new MessageService();
var response = await service.SendAsync(new MessageSendOptions
{
    From = "+15551234567",
    To = "+15559876543",
    Text = "Hello, world!"
});

Console.WriteLine(response.Data);
```

### PHP

```
<?php
require_once 'vendor/autoload.php';

\Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

$response = \Telnyx\Message::Create([
    'from' => '+15551234567',
    'to' => '+15559876543',
    'text' => 'Hello, world!'
]);

print_r($response);
```

### Response

A successful response looks like this:

```
{
  "data": {
    "record_type": "message",
    "direction": "outbound",
    "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
    "type": "SMS",
    "messaging_profile_id": "16fd2706-8baf-433b-82eb-8c7fada847da",
    "from": {
      "phone_number": "+15551234567",
      "carrier": "Telnyx",
      "line_type": "Wireless"
    },
    "to": [
      {
        "phone_number": "+15559876543",
        "status": "queued",
        "carrier": "CARRIER",
        "line_type": "Wireless"
      }
    ],
    "text": "Hello, world!",
    "encoding": "GSM-7",
    "parts": 1,
    "cost": {
      "amount": 0.0051,
      "currency": "USD"
    }
  }
}
```

The `status: "queued"` means your message is on its way. Save the `id` to track delivery status.
