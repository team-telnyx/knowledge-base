---
title: Messaging Profiles Overview
summary: Understand Telnyx messaging profiles — the central configuration for your messaging numbers, webhooks, features, and spend limits.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
    content_hash: 3b5a67e1efdd43af65fdf987a5e20d3413c8efaafc36acd9ba9f1226a83187c3
updated_at: 2026-04-10T00:00:00Z
---

# Messaging Profiles Overview

Understand Telnyx messaging profiles — the central configuration for your messaging numbers, webhooks, features, and spend limits.

A **messaging profile** is the central configuration object for your Telnyx messaging setup. It groups your phone numbers, defines webhook URLs, and controls features like number pooling, smart encoding, and spend limits.

Every phone number you use for messaging must be assigned to a messaging profile.

## What a messaging profile controls

| Setting             | Description                                                | Default         |
| ------------------- | ---------------------------------------------------------- | --------------- |
| **Webhook URL**     | Where inbound messages and delivery status events are sent | None (required) |
| **Number Pool**     | Distribute messages across multiple numbers automatically  | Disabled        |
| **Sticky Sender**   | Keep the same sender number for each recipient             | Disabled        |
| **Geomatch**        | Select sender numbers based on geographic proximity        | Disabled        |
| **Smart Encoding**  | Replace Unicode characters with GSM-7 equivalents          | Disabled        |
| **MMS Transcoding** | Automatically resize media for carrier limits              | Disabled        |
| **Spend Limit**     | Daily spend cap to prevent unexpected costs                | Disabled        |
| **URL Shortening**  | Shorten URLs in outbound messages                          | Disabled        |

***

## Create a messaging profile

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

  ```csharp .NET theme={null}
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

> **Note:** You can also create messaging profiles in the [Telnyx Portal](https://portal.telnyx.com/#/app/messaging) under **Messaging > Messaging Profiles**.

***

## Configure profile features

Update an existing profile to enable features:

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

***

## Profile features explained

**Webhook configuration**

    Every messaging profile needs a **webhook URL** to receive:

    * **Inbound messages** — SMS/MMS received on your numbers
    * **Delivery status updates** — sent, delivered, failed, etc.
    * **Spend limit notifications** — when daily limits are reached

    Configure a **failover URL** as a backup in case your primary webhook is unreachable.

    | Setting                | Description                                   |
    | ---------------------- | --------------------------------------------- |
    | `webhook_url`          | Primary URL for all messaging events          |
    | `webhook_failover_url` | Backup URL if primary fails                   |
    | `webhook_api_version`  | API version for webhook payloads (`1` or `2`) |

    See [Webhooks](../runbooks/receiving-webhooks-for-messaging.md) for implementation details.

---

**Number Pool**

    When enabled, messages sent from the profile automatically distribute across all assigned numbers. This increases throughput and helps avoid carrier filtering.

    **Settings:**

    | Setting            | Description                                           |
    | ------------------ | ----------------------------------------------------- |
    | `geomatch`         | Select sender number closest to recipient's area code |
    | `sticky_sender`    | Reuse the same sender number for each recipient       |
    | `skip_unhealthy`   | Skip numbers with delivery issues                     |
    | `long_code_weight` | Weight for long code selection (default: 1)           |
    | `toll_free_weight` | Weight for toll-free selection (default: 1)           |

    See [Number Pool](../runbooks/number-pool.md) for details.

---

**Smart Encoding**

    Automatically replaces Unicode characters (curly quotes, em dashes, etc.) with GSM-7 equivalents to keep messages in the more efficient encoding and reduce segment counts.

    A single curly quote can switch an entire message from GSM-7 (160 chars/segment) to UTF-16 (70 chars/segment), more than doubling costs.

    See [Smart Encoding](../runbooks/smart-encoding.md) for the full character substitution reference.

---

**MMS Transcoding**

    Automatically resizes images and videos to meet carrier size limits before delivery. When enabled:

    * Images are converted to JPEG
    * Videos are converted to H.264 MP4
    * Animated GIFs are not resized

    See [MMS Media & Transcoding](../runbooks/mms-media-transcoding.md) for carrier size limits.

---

**Spend Limits**

    Set a daily spending cap to prevent unexpected costs. When the limit is reached:

    * New messages are rejected with error `40333`
    * A webhook notification is sent
    * An email alert is sent to your account

    The limit resets at midnight UTC daily.

    See [Spend Limits](../runbooks/configurable-spend-limits.md) for configuration and webhook handling.

---

**URL Shortening**

    Automatically shorten URLs in outbound messages. Shortened URLs use your configured domain and track click-through rates.

    | Setting                                         | Description                      |
    | ----------------------------------------------- | -------------------------------- |
    | `url_shortener_settings.domain`                 | Custom domain for shortened URLs |
    | `url_shortener_settings.prefix`                 | URL prefix                       |
    | `url_shortener_settings.replace_blacklist_only` | Only replace blacklisted URLs    |
    | `url_shortener_settings.send_webhooks`          | Send click-tracking webhooks     |

---

***

## Assign phone numbers

After creating a profile, assign phone numbers to it:

  ```bash
  curl -X POST https://api.telnyx.com/v2/messaging_profiles/{profile_id}/phone_numbers \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{"phone_number_id": "your_phone_number_id"}'
  ```

  ```python
  # List numbers on a profile
  numbers = client.messaging_profiles.list_phone_numbers(
      "your_messaging_profile_id"
  )

  for number in numbers.data:
      print(f"{number.phone_number} ({number.type})")
  ```

  ```javascript
  // List numbers on a profile
  const numbers = await client.messagingProfiles.listPhoneNumbers(
    'your_messaging_profile_id'
  );

  numbers.data.forEach(n => {
    console.log(`${n.phone_number} (${n.type})`);
  });
  ```

> **Note:** You can also assign numbers to profiles in the [Telnyx Portal](https://portal.telnyx.com/#/app/messaging) by editing a messaging profile and selecting numbers.

***

## Common configurations

### Transactional (OTP, alerts)

    ```json theme={null}
    {
      "name": "Transactional Messages",
      "webhook_url": "https://api.example.com/webhooks/sms",
      "smart_encoding": true,
      "daily_spend_limit_enabled": true,
      "daily_spend_limit": "100.00"
    }
    ```

    **Best for:** OTP codes, account alerts, order confirmations.
    Low volume, high priority. Smart encoding reduces costs.

### Marketing campaigns

    ```json theme={null}
    {
      "name": "Marketing Campaigns",
      "webhook_url": "https://api.example.com/webhooks/marketing",
      "number_pool_settings": {
        "geomatch": true,
        "sticky_sender": true,
        "skip_unhealthy": true
      },
      "smart_encoding": true,
      "mms_transcoding": true,
      "daily_spend_limit_enabled": true,
      "daily_spend_limit": "500.00"
    }
    ```

    **Best for:** Promotional messages, newsletters. Number pool for throughput. Higher spend limit for volume.

### Support / Conversational

    ```json theme={null}
    {
      "name": "Customer Support",
      "webhook_url": "https://api.example.com/webhooks/support",
      "number_pool_settings": {
        "sticky_sender": true
      },
      "smart_encoding": true
    }
    ```

    **Best for:** Two-way conversations. Sticky sender ensures customers always see the same number.

***

## Related resources

  - [Number Pool](../runbooks/number-pool.md) — Distribute messages across multiple numbers for higher throughput.

  - [Smart Encoding](../runbooks/smart-encoding.md) — Reduce SMS costs by replacing Unicode with GSM-7 characters.

  - [Spend Limits](../runbooks/configurable-spend-limits.md) — Set daily spend caps to prevent unexpected costs.

  - [Webhooks](../runbooks/receiving-webhooks-for-messaging.md) — Receive inbound messages and delivery status updates.
