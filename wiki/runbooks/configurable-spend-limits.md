---
title: Configurable Spend Limits
summary: Set daily spending limits on messaging profiles to prevent unexpected costs.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
    content_hash: 284077106aa9fa25ad476d956f75e3f9e80e2e20782ad697a7c1d395afaaf98e
updated_at: 2026-04-10T00:00:00Z
---

# Configurable Spend Limits

Set daily spending limits on messaging profiles to prevent unexpected costs. Handle limit-reached webhooks and manage overrides.

Messaging profiles can be configured with a daily spending limit to prevent unexpected costs from bugs, traffic spikes, or human error. When the limit is reached, outbound messages are rejected until the limit resets at midnight UTC.

## Set up spend limits

Enable the `daily_spend_limit_enabled` flag and set a `daily_spend_limit` value (in USD) on your messaging profile:

  ```bash
  curl -X PATCH https://api.telnyx.com/v2/messaging_profiles/{profile_id} \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "daily_spend_limit_enabled": true,
      "daily_spend_limit": "10.00"
    }'
  ```

  ```python
  import os
  from telnyx import Telnyx

  client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

  response = client.messaging_profiles.update(
      "your_messaging_profile_id",
      daily_spend_limit_enabled=True,
      daily_spend_limit="10.00",
  )

  print(f"Spend limit set: ${response.data.daily_spend_limit}")
  ```

  ```javascript
  import Telnyx from 'telnyx';

  const client = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

  const response = await client.messagingProfiles.update(
    'your_messaging_profile_id',
    {
      daily_spend_limit_enabled: true,
      daily_spend_limit: '10.00',
    }
  );

  console.log(`Spend limit set: $${response.data.daily_spend_limit}`);
  ```

  ```ruby
  require "telnyx"

  client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

  response = client.messaging_profiles.update(
    "your_messaging_profile_id",
    daily_spend_limit_enabled: true,
    daily_spend_limit: "10.00"
  )

  puts "Spend limit set: $#{response.data.daily_spend_limit}"
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
        DailySpendLimitEnabled: telnyx.Bool(true),
        DailySpendLimit:        telnyx.String("10.00"),
      },
    )
    if err != nil {
      panic(err.Error())
    }
    fmt.Printf("Spend limit set: $%s\n", response.Data.DailySpendLimit)
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
              .dailySpendLimitEnabled(true)
              .dailySpendLimit("10.00")
              .build();

          var response = client.messagingProfiles()
              .update("your_messaging_profile_id", params);

          System.out.println("Spend limit set: $" + response.data().dailySpendLimit());
      }
  }
  ```

  ```csharp .NET theme={null}
  using Telnyx;

  TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

  var service = new MessagingProfileService();
  var response = await service.UpdateAsync(
      "your_messaging_profile_id",
      new MessagingProfileUpdateOptions
      {
          DailySpendLimitEnabled = true,
          DailySpendLimit = "10.00"
      }
  );

  Console.WriteLine($"Spend limit set: ${response.Data.DailySpendLimit}");
  ```

  ```php
  <?php
  require_once 'vendor/autoload.php';

  \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

  $response = \Telnyx\MessagingProfile::Update(
      'your_messaging_profile_id',
      [
          'daily_spend_limit_enabled' => true,
          'daily_spend_limit' => '10.00'
      ]
  );

  echo "Spend limit set: \${$response->daily_spend_limit}\n";
  ```

> **Note:** The `daily_spend_limit` value is a string representing USD (e.g., `"0.50"`, `"10.00"`, `"100.00"`). It applies per messaging profile — use separate profiles for different budgets.

***

## When the limit is reached

Once spending exceeds the configured limit, Telnyx:

1. **Rejects new messages** with HTTP `429` and error code `40333`
2. **Sends a webhook** to your configured URL
3. **Sends an email** notification to your account

### Error response

```json theme={null}
{
  "errors": [
    {
      "code": "40333",
      "title": "Messaging profile spend limit reached",
      "detail": "The daily spend limit configured on this messaging profile has been reached",
      "meta": {
        "url": "https://developers.telnyx.com/docs/overview/errors/40333"
      }
    }
  ]
}
```

### Webhook payload

```json theme={null}
{
  "data": {
    "event_type": "messaging-profile.spend-limit-reached",
    "id": "d21a2887-8007-4bb6-bd7d-f2874829918e",
    "occurred_at": "2024-08-20T19:17:08.918+00:00",
    "payload": {
      "configured_limit": "10.00",
      "current_cost": "10.02",
      "profile_id": "be3eb60a-a346-470a-886c-ab4e421711bd"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhook-url"
  }
}
```

> **Warning:** There may be a short delay between reaching the limit and enforcement. A small number of additional messages may be sent during this window, causing `current_cost` to slightly exceed `configured_limit`.

***

## Handle the spend limit webhook

Process the webhook to alert your team and gracefully handle the blocked state:

  ```python
  from flask import Flask, request, jsonify
  import logging

  app = Flask(__name__)
  logger = logging.getLogger(__name__)

  @app.route("/webhooks/messaging", methods=["POST"])
  def handle_webhook():
      data = request.json["data"]

      if data["event_type"] == "messaging-profile.spend-limit-reached":
          payload = data["payload"]
          logger.warning(
              "Spend limit reached! Profile: %s, Limit: $%s, Current: $%s",
              payload["profile_id"],
              payload["configured_limit"],
              payload["current_cost"],
          )

          # Alert your team (Slack, PagerDuty, email, etc.)
          alert_team(
              title="SMS Spend Limit Reached",
              message=f"Profile {payload['profile_id']} hit ${payload['configured_limit']} limit. "
                      f"Current spend: ${payload['current_cost']}. "
                      f"Messages are being rejected.",
          )

          # Optionally: queue messages for retry after midnight UTC
          # or switch to a backup profile

      return jsonify({"status": "ok"}), 200
  ```

  ```javascript
  import express from 'express';

  const app = express();
  app.use(express.json());

  app.post('/webhooks/messaging', (req, res) => {
    const { data } = req.body;

    if (data.event_type === 'messaging-profile.spend-limit-reached') {
      const { profile_id, configured_limit, current_cost } = data.payload;

      console.warn(
        `Spend limit reached! Profile: ${profile_id}, ` +
        `Limit: $${configured_limit}, Current: $${current_cost}`
      );

      // Alert your team
      alertTeam({
        title: 'SMS Spend Limit Reached',
        message: `Profile ${profile_id} hit $${configured_limit} limit. ` +
                 `Current spend: $${current_cost}. Messages are being rejected.`,
      });
    }

    res.json({ status: 'ok' });
  });
  ```

***

## Track spending

Monitor your messaging spend to take action before hitting the limit:

  ```python
  import os
  from telnyx import Telnyx

  client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

  def check_spend(profile_id: str) -> dict:
      """Check current spend against the configured limit."""
      profile = client.messaging_profiles.retrieve(profile_id)

      limit = float(profile.data.daily_spend_limit or 0)
      enabled = profile.data.daily_spend_limit_enabled

      return {
          "profile_id": profile_id,
          "limit_enabled": enabled,
          "daily_limit": limit,
      }

  def send_with_spend_check(profile_id: str, to: str, from_: str, text: str):
      """Send a message with pre-send spend checking."""
      try:
          response = client.messages.send(from_=from_, to=to, text=text)
          return {"status": "sent", "message_id": response.data.id}
      except Exception as e:
          error_code = getattr(e, "code", None)
          if error_code == "40333":
              return {"status": "blocked", "reason": "spend_limit_reached"}
          raise

  # Check profile status
  info = check_spend("your_messaging_profile_id")
  print(f"Limit enabled: {info['limit_enabled']}, Limit: ${info['daily_limit']}")
  ```

  ```javascript
  import Telnyx from 'telnyx';

  const client = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

  async function checkSpend(profileId) {
    const profile = await client.messagingProfiles.retrieve(profileId);
    return {
      profileId,
      limitEnabled: profile.data.daily_spend_limit_enabled,
      dailyLimit: parseFloat(profile.data.daily_spend_limit || '0'),
    };
  }

  async function sendWithSpendCheck(profileId, to, from, text) {
    try {
      const response = await client.messages.send({ from, to, text });
      return { status: 'sent', messageId: response.data.id };
    } catch (err) {
      if (err.rawType === '40333') {
        return { status: 'blocked', reason: 'spend_limit_reached' };
      }
      throw err;
    }
  }
  ```

***

## Reset and override

**Automatic daily reset**

    The running spend total resets automatically at **midnight UTC** each day. After reset, messages can be sent until the limit is exceeded again.

    > **Warning:** Changing the `daily_spend_limit` or `daily_spend_limit_enabled` values does **not** reset the running total. Only the midnight UTC reset clears accumulated spend.

---

**Temporary override (disable and re-enable)**

    If you've hit the limit but need to send urgent messages, temporarily disable the limit:

    ```python theme={null}
    # 1. Disable the limit
    client.messaging_profiles.update(
        profile_id, daily_spend_limit_enabled=False
    )

    # 2. Send urgent messages
    client.messages.send(from_=from_number, to=to_number, text="Urgent message")

    # 3. Re-enable the limit
    client.messaging_profiles.update(
        profile_id, daily_spend_limit_enabled=True
    )
    ```

    > **Warning:** Re-enabling does **not** reset the counter. If you were at $10.00 of a $10.00 limit, re-enabling will immediately block again. Either increase the limit or wait for the midnight UTC reset.

---

**Increase the limit**

    Raise the `daily_spend_limit` to allow more messages until the new limit is reached:

    ```python theme={null}
    # Increase from $10 to $25
    client.messaging_profiles.update(
        profile_id,
        daily_spend_limit="25.00"
    )
    ```

    This takes effect immediately — if current spend is $10.02 and the new limit is $25.00, messages will flow again until \$25.00 is reached.

---

***

## Best practices

1. **Set limits on all production profiles**

    Even if you don't expect high spend, a limit prevents runaway costs from application bugs or compromised API keys.

2. **Use separate profiles for different use cases**

    Create separate messaging profiles for transactional messages (OTP, alerts) and marketing messages, each with appropriate limits.

3. **Set up webhook monitoring**

    Always handle the `messaging-profile.spend-limit-reached` webhook to alert your team immediately.

4. **Build in error handling for 40333**

    Your application should gracefully handle the `40333` error code — queue messages for later delivery or switch to a backup profile.

5. **Review limits regularly**

    As your messaging volume grows, review and adjust limits to avoid unexpected blocks during peak periods.

***

## Related resources

  - [Messaging Profiles API](https://developers.telnyx.com/api-reference/messaging-profiles/update-a-messaging-profile) — API reference for configuring messaging profile settings.

  - [Message Detail Records](message-detail-records.md) — Track message costs and delivery status.

  - [Rate Limiting](rate-limiting.md) — Understand message throughput limits.

  - [Webhooks](receiving-webhooks-for-messaging.md) — Configure webhooks to receive spend limit notifications.
