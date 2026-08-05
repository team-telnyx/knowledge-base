---
title: Schedule SMS and MMS Messages
summary: Schedule SMS and MMS messages to send at a specific time in the future using
  the Telnyx messaging API. Use scheduled messaging for appointment reminders, marketing
  campaigns, time-zone-aware notifications, and any scenario where precise delivery
  timing matters.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/schedule-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-an-rcs-message/index
updated_at: 2026-08-05T13:56:55Z
---

# Schedule SMS and MMS Messages

*Part 2 of 3 — see also: [Part 1](schedule-sms-and-mms-messages--part-1.md), [Part 3](schedule-sms-and-mms-messages--part-3.md)*

Schedule SMS and MMS messages to send at a specific time in the future using the Telnyx messaging API. Use scheduled messaging for appointment reminders, marketing campaigns, time-zone-aware notifications, and any scenario where precise delivery timing matters.

## Schedule a message

You can schedule messages using either endpoint:

- **`POST /v2/messages`** — The standard send endpoint, with the `send_at` parameter added
- **`POST /v2/messages/schedule`** — A dedicated scheduling endpoint with the same parameters

Both endpoints accept identical parameters. The examples below use `/v2/messages` with `send_at`.

### Set your API key

Export your API key as an environment variable:

```
export TELNYX_API_KEY="YOUR_API_KEY"
```

### Choose your send time

The `send_at` field requires an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) formatted datetime string in UTC. For example:

- `2026-02-15T14:30:00Z` — February 15, 2026 at 2:30 PM UTC
- `2026-02-14T09:00:00-08:00` — February 14, 2026 at 9:00 AM PST

**Time zone tip:** Always convert your desired delivery time to UTC, or include the UTC offset. Messages are delivered based on the UTC time you specify, not the recipient's local time zone.

### Send the request

#### SMS

```
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

```csharp
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

#### MMS

```
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

```csharp
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

```json
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
