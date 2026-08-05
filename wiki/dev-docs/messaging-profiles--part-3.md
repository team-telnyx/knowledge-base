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

*Part 3 of 6 — see also: [Part 1](messaging-profiles--part-1.md), [Part 2](messaging-profiles--part-2.md), [Part 4](messaging-profiles--part-4.md), [Part 5](messaging-profiles--part-5.md), [Part 6](messaging-profiles--part-6.md)*

A messaging profile is the central configuration object for Telnyx messaging. It groups phone numbers, defines webhook URLs, and controls features such as number pooling, smart encoding, MMS transcoding, MMS-to-SMS fallback, spend limits, and URL shortening. Every phone number used for messaging must be assigned to a messaging profile.

## Smart Encoding

Automatically replaces Unicode characters (curly quotes, em dashes, etc.) with GSM-7 equivalents to keep messages in the more efficient encoding and reduce segment counts. A single curly quote can switch an entire message from GSM-7 (160 chars/segment) to UTF-16 (70 chars/segment), more than doubling costs. See [Smart Encoding](smart-encoding.md) for the full character substitution reference.

## MMS Transcoding

Automatically resizes images and videos to meet carrier size limits before delivery. When enabled:

- Images are converted to JPEG
- Videos are converted to H.264 MP4
- Animated GIFs are not resized

### Carrier size limits

Each US carrier imposes different maximum MMS message sizes based on the sender type. Messages exceeding these limits will be rejected by the carrier.

| Carrier | Long Code | Toll-Free | Short Code |
| --- | --- | --- | --- |
| AT&T | 1 MB | 600 KB | 600 KB |
| T-Mobile | 1.5 MB | 600 KB | 1 MB |
| Verizon | 1 MB | 600 KB | 1.2 MB |

The **safe maximum** across all carriers and sender types is **600 KB**. To guarantee delivery to all recipients regardless of carrier, keep your total media under this limit — or enable transcoding.

### Enable MMS Transcoding

Enable `mms_transcoding` on your messaging profile to apply it to all MMS sent through that profile.

```bash
curl -X PATCH https://api.telnyx.com/v2/messaging_profiles/{profile_id} \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "mms_transcoding": true
  }'
```

```python
import os
from telnyx import Telnyx

client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

response = client.messaging_profiles.update(
    "your_messaging_profile_id",
    mms_transcoding=True,
)

print(response.data)
```

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'],
});

const response = await client.messagingProfiles.update(
  'your_messaging_profile_id',
  { mms_transcoding: true }
);

console.log(response.data);
```

```ruby
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

response = client.messaging_profiles.update(
  "your_messaging_profile_id",
  mms_transcoding: true
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
  response, err := client.MessagingProfiles.Update(
    context.TODO(),
    "your_messaging_profile_id",
    telnyx.MessagingProfileUpdateParams{
      MMSTranscoding: telnyx.Bool(true),
    },
  )
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
import com.telnyx.sdk.models.messagingprofiles.MessagingProfileUpdateParams;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        var params = MessagingProfileUpdateParams.builder()
            .mmsTranscoding(true)
            .build();

        var response = client.messagingProfiles()
            .update("your_messaging_profile_id", params);

        System.out.println(response);
    }
}
```

```csharp
using Telnyx;

TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

var service = new MessagingProfileService();
var response = await service.UpdateAsync(
    "your_messaging_profile_id",
    new MessagingProfileUpdateOptions
    {
        MmsTranscoding = true
    }
);

Console.WriteLine(response.Data);
```

```php
<?php
require_once 'vendor/autoload.php';

\Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

$response = \Telnyx\MessagingProfile::Update(
    'your_messaging_profile_id',
    ['mms_transcoding' => true]
);

print_r($response);
```

In the [Telnyx Portal](https://portal.telnyx.com/#/app/messaging), navigate to **Messaging > Messaging Profiles**, select the profile, toggle **MMS Transcoding** to enabled, and save.

### MMS best practices

- **Optimize media before sending** — Pre-optimize for the best balance of quality and deliverability. Resize images to 640×480 or smaller using JPEG at 80% quality, compress videos to H.264 under 30 seconds targeting 480p, and stay under 600 KB for universal carrier compatibility.
- **Use publicly accessible URLs** — Media URLs must be publicly accessible; Telnyx fetches them at send time. URLs should not require authentication, respond quickly, return the correct `Content-Type` header, and use HTTPS.
- **Handle inbound MMS media** — Inbound MMS media URLs in webhooks are ephemeral and expire after a short period. Always download and store important media to your own storage (e.g., AWS S3) immediately upon receiving the webhook.
- **Consider SMS for text-only messages** — SMS is cheaper, faster, and more reliable than MMS. Only use MMS when you actually need to include media content.

## MMS Converter

While your message's source number may support sending MMS, the destination number might not support receiving it. Normally, this will prevent you from sending MMS to this destination. When **MMS converter** is enabled on your messaging profile, however, your MMS will be converted to an SMS message by Telnyx and then sent to the destination. Messages sent as SMS are unaffected by this feature and will be sent as usual.

The resultant webhooks for messages sent with this feature enabled will indicate the protocol that was used to send the message. For example: when an MMS message is sent and fallback happens, the webhook will indicate that an SMS message was sent, and when an MMS message is sent and fallback doesn't happen, the webhook will indicate that an MMS message was sent.

If fallback happens, the destination will receive an SMS formatted to contain the media URLs specified in the request. Each media URL will appear on its own line, immediately after the message body, if any. Media URLs appear on the destination exactly as provided in the request — no shortlinking or other transformations are applied.

### Examples

If your request includes `"text": "message body that\nis potentially spread across multiple lines"` and `"media_urls": ["https://example.com/image.png"]`, the destination receives:

```
message body that
is potentially spread across multiple lines
https://example.com/image.png
```

If your request includes `"text": "message body"` and `"media_urls": ["https://example.com/one.png", "https://example.com/two.png"]`, the destination receives:

```
message body
https://example.com/one.png
https://example.com/two.png
```

If your request doesn't set `text` and includes `"media_urls": ["https://example.com/image.png"]`, the destination receives:

```
https://example.com/image.png
```

### Enable MMS Converter

This behavior is not enabled by default. It is controlled at the messaging profile level by an optional boolean field called `mms_fall_back_to_sms`, which you can either set at creation time or update later on an existing messaging profile.

## Spend Limits

Set a daily spending cap to prevent unexpected costs. When the limit is reached:

- New messages are rejected with error `40333`
- A webhook notification is sent
- An email alert is sent to your account

The limit resets at midnight UTC daily. See [Spend Limits](spend-limits.md) for configuration and webhook handling.
