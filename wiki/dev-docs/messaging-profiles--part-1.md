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

*Part 1 of 6 — see also: [Part 2](messaging-profiles--part-2.md), [Part 3](messaging-profiles--part-3.md), [Part 4](messaging-profiles--part-4.md), [Part 5](messaging-profiles--part-5.md), [Part 6](messaging-profiles--part-6.md)*

A messaging profile is the central configuration object for Telnyx messaging. It groups phone numbers, defines webhook URLs, and controls features such as number pooling, smart encoding, MMS transcoding, MMS-to-SMS fallback, spend limits, and URL shortening. Every phone number used for messaging must be assigned to a messaging profile.

## What a messaging profile controls

A messaging profile is the central configuration object for your Telnyx messaging setup. It groups your phone numbers, defines webhook URLs, and controls features like number pooling, smart encoding, and spend limits. Every phone number you use for messaging must be assigned to a messaging profile.

| Setting | Description | Default |
| --- | --- | --- |
| **Webhook URL** | Where inbound messages and delivery status events are sent | None (required) |
| **Number Pool** | Distribute messages across multiple numbers automatically | Disabled |
| **Sticky Sender** | Keep the same sender number for each recipient | Disabled |
| **Geomatch** | Select sender numbers based on geographic proximity | Disabled |
| **Smart Encoding** | Replace Unicode characters with GSM-7 equivalents | Disabled |
| **MMS Transcoding** | Automatically resize media for carrier limits | Disabled |
| **MMS Converter** | Fall back to SMS when the destination cannot receive MMS | Disabled |
| **Spend Limit** | Daily spend cap to prevent unexpected costs | Disabled |
| **URL Shortening** | Shorten URLs in outbound messages | Disabled |

## Create a messaging profile

Create a profile via the API or in the [Telnyx Portal](https://portal.telnyx.com/#/app/messaging) under **Messaging > Messaging Profiles**.

```bash
curl -X POST https://api.telnyx.com/v2/messaging_profiles \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "name": "My Messaging Profile",
    "webhook_url": "https://example.com/webhooks/messaging",
    "webhook_failover_url": "https://example.com/webhooks/messaging/failover"
  }'
```

```python
import os
from telnyx import Telnyx

client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

profile = client.messaging_profiles.create(
    name="My Messaging Profile",
    webhook_url="https://example.com/webhooks/messaging",
    webhook_failover_url="https://example.com/webhooks/messaging/failover",
)

print(f"Profile created: {profile.data.id}")
```

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

const profile = await client.messagingProfiles.create({
  name: 'My Messaging Profile',
  webhook_url: 'https://example.com/webhooks/messaging',
  webhook_failover_url: 'https://example.com/webhooks/messaging/failover',
});

console.log(`Profile created: ${profile.data.id}`);
```

```ruby
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

profile = client.messaging_profiles.create(
  name: "My Messaging Profile",
  webhook_url: "https://example.com/webhooks/messaging",
  webhook_failover_url: "https://example.com/webhooks/messaging/failover"
)

puts "Profile created: #{profile.data.id}"
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
  profile, err := client.MessagingProfiles.Create(
    context.TODO(),
    telnyx.MessagingProfileCreateParams{
      Name:               "My Messaging Profile",
      WebhookURL:         "https://example.com/webhooks/messaging",
      WebhookFailoverURL: telnyx.String("https://example.com/webhooks/messaging/failover"),
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("Profile created: %s\n", profile.Data.ID)
}
```

```java
package com.telnyx.example;

import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileCreateParams;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        var params = MessagingProfileCreateParams.builder()
            .name("My Messaging Profile")
            .webhookUrl("https://example.com/webhooks/messaging")
            .webhookFailoverUrl("https://example.com/webhooks/messaging/failover")
            .build();

        var profile = client.messagingProfiles().create(params);
        System.out.println("Profile created: " + profile.data().id());
    }
}
```

```csharp
using Telnyx;

TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

var service = new MessagingProfileService();
var profile = await service.CreateAsync(new MessagingProfileCreateOptions
{
    Name = "My Messaging Profile",
    WebhookUrl = "https://example.com/webhooks/messaging",
    WebhookFailoverUrl = "https://example.com/webhooks/messaging/failover"
});

Console.WriteLine($"Profile created: {profile.Data.Id}");
```

```php
<?php
require_once 'vendor/autoload.php';

\Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

$profile = \Telnyx\MessagingProfile::Create([
    'name' => 'My Messaging Profile',
    'webhook_url' => 'https://example.com/webhooks/messaging',
    'webhook_failover_url' => 'https://example.com/webhooks/messaging/failover'
]);

echo "Profile created: {$profile->id}\n";
```

## Configure profile features

Update an existing profile to enable features such as number pooling, smart encoding, MMS transcoding, and spend limits:

```bash
curl -X PATCH https://api.telnyx.com/v2/messaging_profiles/{profile_id} \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "number_pool_settings": {
      "geomatch": true,
      "sticky_sender": true,
      "skip_unhealthy": true
    },
    "smart_encoding": true,
    "mms_transcoding": true,
    "daily_spend_limit_enabled": true,
    "daily_spend_limit": "50.00"
  }'
```

```python
response = client.messaging_profiles.update(
    "your_messaging_profile_id",
    number_pool_settings={
        "geomatch": True,
        "sticky_sender": True,
        "skip_unhealthy": True,
    },
    smart_encoding=True,
    mms_transcoding=True,
    daily_spend_limit_enabled=True,
    daily_spend_limit="50.00",
)

print(f"Profile updated: {response.data.id}")
```

```javascript
const response = await client.messagingProfiles.update(
  'your_messaging_profile_id',
  {
    number_pool_settings: {
      geomatch: true,
      sticky_sender: true,
      skip_unhealthy: true,
    },
    smart_encoding: true,
    mms_transcoding: true,
    daily_spend_limit_enabled: true,
    daily_spend_limit: '50.00',
  }
);

console.log(`Profile updated: ${response.data.id}`);
```

## Webhook configuration

Every messaging profile needs a **webhook URL** to receive:

- **Inbound messages** — SMS/MMS received on your numbers
- **Delivery status updates** — sent, delivered, failed, etc.
- **Spend limit notifications** — when daily limits are reached

Configure a **failover URL** as a backup in case your primary webhook is unreachable.

| Setting | Description |
| --- | --- |
| `webhook_url` | Primary URL for all messaging events |
| `webhook_failover_url` | Backup URL if primary fails |
| `webhook_api_version` | API version for webhook payloads (`1` or `2`) |

See [Webhooks](webhooks.md) for implementation details.
