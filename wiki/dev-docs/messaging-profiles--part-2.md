---
title: Messaging Profiles
summary: A messaging profile is the central configuration object for Telnyx messaging.
  It groups phone numbers, defines webhook URLs, and controls features such as number
  pooling, smart encoding, MMS transcoding, MMS-to-SMS fallback, spend limits, and
  URL shortening. Every phone number used for messaging must be assigned to a messaging
  profile.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration/index
updated_at: 2026-08-05T13:56:37Z
---

# Messaging Profiles

*Part 2 of 6 — see also: [Part 1](messaging-profiles--part-1.md), [Part 3](messaging-profiles--part-3.md), [Part 4](messaging-profiles--part-4.md), [Part 5](messaging-profiles--part-5.md), [Part 6](messaging-profiles--part-6.md)*

A messaging profile is the central configuration object for Telnyx messaging. It groups phone numbers, defines webhook URLs, and controls features such as number pooling, smart encoding, MMS transcoding, MMS-to-SMS fallback, spend limits, and URL shortening. Every phone number used for messaging must be assigned to a messaging profile.

## Number Pool

When enabled, messages sent from the profile automatically distribute across all assigned numbers. This increases throughput and helps avoid carrier filtering.

| Setting | Description |
| --- | --- |
| `geomatch` | Select sender number closest to recipient's area code |
| `sticky_sender` | Reuse the same sender number for each recipient |
| `skip_unhealthy` | Skip numbers with delivery issues |
| `long_code_weight` | Weight for long code selection (default: 1) |
| `toll_free_weight` | Weight for toll-free selection (default: 1) |

Weights are ratios, not percentages. With `long_code_weight: 5` and `toll_free_weight: 1`, approximately 5 out of every 6 messages use a long code. Setting a weight to `0` removes that number type from the pool.

### Configure Number Pool

Enable Number Pool on your messaging profile by setting `number_pool_settings`:

```bash
curl -X PATCH "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "number_pool_settings": {
      "long_code_weight": 5,
      "toll_free_weight": 1,
      "skip_unhealthy": true
    }
  }'
```

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

const response = await client.messagingProfiles.update(
  'YOUR_PROFILE_ID',
  {
    number_pool_settings: {
      long_code_weight: 5,
      toll_free_weight: 1,
      skip_unhealthy: true
    }
  }
);

console.log(response.data);
```

```python
import os
from telnyx import Telnyx

client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

response = client.messaging_profiles.update(
    "YOUR_PROFILE_ID",
    number_pool_settings={
        "long_code_weight": 5,
        "toll_free_weight": 1,
        "skip_unhealthy": True
    }
)

print(response.data)
```

```ruby
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

response = client.messaging_profiles.update(
  "YOUR_PROFILE_ID",
  number_pool_settings: {
    long_code_weight: 5,
    toll_free_weight: 1,
    skip_unhealthy: true
  }
)

puts response
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
  
  response, err := client.MessagingProfiles.Update(
    context.TODO(),
    "YOUR_PROFILE_ID",
    telnyx.MessagingProfileUpdateParams{
      NumberPoolSettings: &telnyx.NumberPoolSettingsParam{
        LongCodeWeight:  telnyx.Int(5),
        TollFreeWeight:  telnyx.Int(1),
        SkipUnhealthy:   telnyx.Bool(true),
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response)
}
```

```java
package com.telnyx.example;

import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
import com.telnyx.sdk.models.messagingprofiles.*;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        NumberPoolSettings poolSettings = NumberPoolSettings.builder()
            .longCodeWeight(5)
            .tollFreeWeight(1)
            .skipUnhealthy(true)
            .build();

        MessagingProfileUpdateParams params = MessagingProfileUpdateParams.builder()
            .numberPoolSettings(poolSettings)
            .build();

        MessagingProfileUpdateResponse response = client.messagingProfiles()
            .update("YOUR_PROFILE_ID", params);
        System.out.println(response);
    }
}
```

```csharp
using System;
using Telnyx;

TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

var service = new MessagingProfileService();
var options = new MessagingProfileUpdateOptions
{
    NumberPoolSettings = new NumberPoolSettings
    {
        LongCodeWeight = 5,
        TollFreeWeight = 1,
        SkipUnhealthy = true
    }
};

var profile = service.Update("YOUR_PROFILE_ID", options);
Console.WriteLine(profile);
```

```php
<?php
require_once 'vendor/autoload.php';

\Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

$profile = \Telnyx\MessagingProfile::update("YOUR_PROFILE_ID", [
    "number_pool_settings" => [
        "long_code_weight" => 5,
        "toll_free_weight" => 1,
        "skip_unhealthy" => true
    ]
]);

print_r($profile);
```

In the [Telnyx Portal](https://portal.telnyx.com/#/app/messaging), edit a messaging profile, toggle on **Number Pool** under **Outbound**, configure the weights, optionally enable **Skip Unhealthy Numbers**, and save.

### Send messages with Number Pool

When sending with Number Pool, omit the `from` field and specify your `messaging_profile_id` instead. Telnyx automatically selects the optimal sender.

```bash
curl -X POST "https://api.telnyx.com/v2/messages/number_pool" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "messaging_profile_id": "YOUR_PROFILE_ID",
    "to": "+15559876543",
    "text": "Hello from Number Pool!"
  }'
```

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

const response = await client.messages.sendWithNumberPool({
  messaging_profile_id: 'YOUR_PROFILE_ID',
  to: '+15559876543',
  text: 'Hello from Number Pool!'
});

console.log(`Sent from: ${response.data.from.phone_number}`);
```

```python
import os
from telnyx import Telnyx

client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

response = client.messages.send_with_number_pool(
    messaging_profile_id="YOUR_PROFILE_ID",
    to="+15559876543",
    text="Hello from Number Pool!"
)

print(f"Sent from: {response.data.from_.phone_number}")
```

```ruby
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

response = client.messages.send_with_number_pool(
  messaging_profile_id: "YOUR_PROFILE_ID",
  to: "+15559876543",
  text: "Hello from Number Pool!"
)

puts "Sent from: #{response.from.phone_number}"
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
  
  response, err := client.Messages.SendWithNumberPool(
    context.TODO(),
    telnyx.MessageSendWithNumberPoolParams{
      MessagingProfileID: "YOUR_PROFILE_ID",
      To:                 "+15559876543",
      Text:               "Hello from Number Pool!",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("Sent from: %s\n", response.Data.From.PhoneNumber)
}
```

```java
package com.telnyx.example;

import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
import com.telnyx.sdk.models.messages.*;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        MessageSendWithNumberPoolParams params = MessageSendWithNumberPoolParams.builder()
            .messagingProfileId("YOUR_PROFILE_ID")
            .to("+15559876543")
            .text("Hello from Number Pool!")
            .build();

        MessageSendResponse response = client.messages().sendWithNumberPool(params);
        System.out.println("Sent from: " + response.data().from().phoneNumber());
    }
}
```

```csharp
using System;
using Telnyx;

TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

var service = new MessagingService();
var options = new MessageSendWithNumberPoolOptions
{
    MessagingProfileId = "YOUR_PROFILE_ID",
    To = "+15559876543",
    Text = "Hello from Number Pool!"
};

var message = service.SendWithNumberPool(options);
Console.WriteLine($"Sent from: {message.From.PhoneNumber}");
```

```php
<?php
require_once 'vendor/autoload.php';

\Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

$message = \Telnyx\Message::create([
    "messaging_profile_id" => "YOUR_PROFILE_ID",
    "to" => "+15559876543",
    "text" => "Hello from Number Pool!"
], null, "/v2/messages/number_pool");

echo "Sent from: " . $message->from->phone_number . "\n";
```

The response includes the actual `from` number that was selected:

```json
{
  "data": {
    "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
    "type": "SMS",
    "from": {
      "phone_number": "+15551234567",
      "carrier": "Telnyx",
      "line_type": "long_code"
    },
    "to": [
      {
        "phone_number": "+15559876543",
        "status": "queued"
      }
    ],
    "text": "Hello from Number Pool!"
  }
}
```

### Disable Number Pool

To disable Number Pool, set `number_pool_settings` to an empty object:

```bash
curl -X PATCH "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"number_pool_settings": {}}'
```

```javascript
await client.messagingProfiles.update('YOUR_PROFILE_ID', {
  number_pool_settings: {}
});
```

```python
client.messaging_profiles.update(
    "YOUR_PROFILE_ID",
    number_pool_settings={}
)
```

### Related Number Pool features

- **Sticky Sender** — Maintains consistency by using the same number for a recipient across messages. When enabled, if you've previously messaged a recipient, the same number is reused when available. Enable with `{"number_pool_settings": {"long_code_weight": 1, "sticky_sender": true}}`. See [Sticky Sender](sticky-sender.md) for details.
- **Geomatch** — Selects a sender number matching the recipient's geographic area, improving deliverability and user trust by showing a local number. Enable with `{"number_pool_settings": {"long_code_weight": 1, "geomatch": true}}`. See [Geomatch](geomatch.md) for details.
- **Skip Unhealthy Numbers** — Monitors delivery success rates and automatically excludes numbers performing poorly. If all numbers in the pool are unhealthy, message sending will fail rather than use an unhealthy number.

### Number Pool troubleshooting

- **Message rejected: No healthy numbers in pool** — All numbers are flagged as unhealthy and `skip_unhealthy` is enabled. Temporarily disable `skip_unhealthy`, add more numbers to your messaging profile, or investigate delivery issues on existing numbers.
- **Messages always sent from same number type** — Weight of one type set to 0, or only one number type assigned. Verify weights are non-zero for both types and ensure you have both long codes and toll-free numbers assigned.
- **Receiving 'messaging_profile_id required' error** — Using the standard `/v2/messages` endpoint instead of `/v2/messages/number_pool`. Use the Number Pool send endpoint which requires `messaging_profile_id` instead of `from`.
