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

*Part 2 of 6 — see also: [Part 1](send-and-receive-messages-with-the-telnyx-messaging-api--part-1.md), [Part 3](send-and-receive-messages-with-the-telnyx-messaging-api--part-3.md), [Part 4](send-and-receive-messages-with-the-telnyx-messaging-api--part-4.md), [Part 5](send-and-receive-messages-with-the-telnyx-messaging-api--part-5.md), [Part 6](send-and-receive-messages-with-the-telnyx-messaging-api--part-6.md)*

Walks through sending your first SMS and MMS with the Telnyx Messaging API, including setup, code samples in multiple languages, error handling, rate limiting, webhook-based delivery tracking, and inbound MMS processing.

## Send an MMS

MMS messages support media attachments. Your number must be MMS-enabled. Include `media_urls` in your message request. You can send up to 10 media files per message.

### cURL

```
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "+15551234567",
    "to": "+15559876543",
    "text": "Check out this image!",
    "subject": "Picture",
    "media_urls": ["https://example.com/image.jpg"]
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
  text: 'Check out this image!',
  subject: 'Picture',
  media_urls: ['https://example.com/image.jpg']
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
    text="Check out this image!",
    subject="Picture",
    media_urls=["https://example.com/image.jpg"]
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
  text: "Check out this image!",
  subject: "Picture",
  media_urls: ["https://example.com/image.jpg"]
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
    From:      "+15551234567",
    To:        "+15559876543",
    Text:      "Check out this image!",
    Subject:   "Picture",
    MediaURLs: []string{"https://example.com/image.jpg"},
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
import java.util.List;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        MessageSendParams params = MessageSendParams.builder()
            .from("+15551234567")
            .to("+15559876543")
            .text("Check out this image!")
            .subject("Picture")
            .mediaUrls(List.of("https://example.com/image.jpg"))
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
    Text = "Check out this image!",
    Subject = "Picture",
    MediaUrls = new[] { "https://example.com/image.jpg" }
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
    'text' => 'Check out this image!',
    'subject' => 'Picture',
    'media_urls' => ['https://example.com/image.jpg']
]);

print_r($response);
```

### Send Multiple Media Files

Include multiple URLs in `media_urls`. Total payload must stay under carrier limits.

```
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "+18005550100",
    "to": "+18005550101",
    "text": "Product photos attached",
    "media_urls": [
      "https://example.com/photo1.jpg",
      "https://example.com/photo2.jpg",
      "https://example.com/photo3.jpg"
    ],
    "messaging_profile_id": "YOUR_MESSAGING_PROFILE_ID"
  }'
```

Media URLs must be publicly accessible. Telnyx downloads the media at send time — if the URL requires authentication or returns an error, the message will fail.

### Supported Media Types

| Type | Formats | Max Size |
| --- | --- | --- |
| **Images** | JPEG, PNG, GIF, BMP, WebP | 1 MB (carrier-dependent) |
| **Video** | MP4, 3GP | 600 KB (carrier-dependent) |
| **Audio** | MP3, AMR, WAV, OGG | 600 KB (carrier-dependent) |
| **Files** | vCard (.vcf), PDF | 600 KB |

Telnyx automatically transcodes oversized media when possible. For details on carrier-specific limits and transcoding behavior, see [MMS Media & Transcoding](mms-media-transcoding.md).
