---
title: Advanced Opt-In/Out Management
summary: Configure custom opt-in and opt-out keywords, auto-responses, and country-specific messaging to maintain CTIA & TCPA compliance.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/advanced-opt-in-out/index
    content_hash: 91c96d0ad359152235a75c4dedb3595291a3b606000c108239392478be4cd9a9
updated_at: 2026-04-10T00:00:00Z
---

# Advanced Opt-In/Out Management

Configure custom opt-in and opt-out keywords, auto-responses, and country-specific messaging to maintain CTIA & TCPA compliance.

Advanced Opt-In/Out lets you customize keyword triggers and auto-responses on your messaging profile. Configure country-specific responses, custom keywords, and track opt-out behavior via webhooks — all while maintaining CTIA & TCPA compliance.

## Default behavior

Without custom configuration, Telnyx handles standard opt-in/out keywords automatically:

### Opt-out keywords

    These keywords create a **block rule** preventing further messages to the recipient:

    | Keyword       | Action         |
    | ------------- | -------------- |
    | `STOP`        | Block messages |
    | `STOPALL`     | Block messages |
    | `STOP ALL`    | Block messages |
    | `UNSUBSCRIBE` | Block messages |
    | `CANCEL`      | Block messages |
    | `END`         | Block messages |
    | `QUIT`        | Block messages |

### Opt-in keywords

    These keywords **remove an existing block rule**, allowing messages to resume:

    | Keyword  | Action       |
    | -------- | ------------ |
    | `START`  | Remove block |
    | `UNSTOP` | Remove block |

> **Note:** Block rules operate at the **messaging profile level**. If a user opts out from one number on your profile, they're opted out from all numbers on that profile.

When you attempt to message a blocked recipient, the API returns:

```json theme={null}
{
  "errors": [
    {
      "code": "40300",
      "title": "Blocked due to STOP message",
      "detail": "Messages cannot be sent from '{from}' to '{to}' due to an existing block rule."
    }
  ]
}
```

***

## Create custom auto-responses

Configure custom keyword responses for opt-in, opt-out, and help messages:

  ```bash
  # Create a custom opt-in auto-response
  curl -X POST \
    https://api.telnyx.com/v2/messaging_profiles/{profile_id}/autoresp_configs \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "op": "start",
      "keywords": ["JOIN", "SUBSCRIBE", "YES"],
      "resp_text": "Welcome to Acme alerts! You'\''ll receive up to 4 msgs/month. Reply HELP for help, STOP to cancel. Msg&data rates may apply.",
      "country_code": "US"
    }'

  # Create a custom HELP response
  curl -X POST \
    https://api.telnyx.com/v2/messaging_profiles/{profile_id}/autoresp_configs \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "op": "help",
      "keywords": ["HELP", "INFO"],
      "resp_text": "Acme Corp: For support call 1-800-555-0123 or email help@acme.com. Reply STOP to opt out. Msg&data rates may apply.",
      "country_code": "US"
    }'

  # Create a custom opt-out response
  curl -X POST \
    https://api.telnyx.com/v2/messaging_profiles/{profile_id}/autoresp_configs \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "op": "stop",
      "keywords": ["STOP", "QUIT", "CANCEL"],
      "resp_text": "You have been unsubscribed from Acme alerts. Reply START to resubscribe.",
      "country_code": "US"
    }'
  ```

  ```python
  import os
  import requests

  API_KEY = os.environ.get("TELNYX_API_KEY")
  PROFILE_ID = "your_messaging_profile_id"

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json",
  }

  # Custom opt-in response
  response = requests.post(
      f"https://api.telnyx.com/v2/messaging_profiles/{PROFILE_ID}/autoresp_configs",
      headers=headers,
      json={
          "op": "start",
          "keywords": ["JOIN", "SUBSCRIBE", "YES"],
          "resp_text": (
              "Welcome to Acme alerts! You'll receive up to 4 msgs/month. "
              "Reply HELP for help, STOP to cancel. Msg&data rates may apply."
          ),
          "country_code": "US",
      },
  )
  print(f"Opt-in config created: {response.json()['data']['id']}")

  # Custom HELP response
  response = requests.post(
      f"https://api.telnyx.com/v2/messaging_profiles/{PROFILE_ID}/autoresp_configs",
      headers=headers,
      json={
          "op": "help",
          "keywords": ["HELP", "INFO"],
          "resp_text": (
              "Acme Corp: For support call 1-800-555-0123 or email help@acme.com. "
              "Reply STOP to opt out. Msg&data rates may apply."
          ),
          "country_code": "US",
      },
  )
  print(f"Help config created: {response.json()['data']['id']}")
  ```

  ```javascript
  const axios = require('axios');

  const headers = {
    Authorization: `Bearer ${process.env.TELNYX_API_KEY}`,
    'Content-Type': 'application/json',
  };
  const profileId = 'your_messaging_profile_id';
  const baseUrl = `https://api.telnyx.com/v2/messaging_profiles/${profileId}/autoresp_configs`;

  // Custom opt-in response
  const optIn = await axios.post(baseUrl, {
    op: 'start',
    keywords: ['JOIN', 'SUBSCRIBE', 'YES'],
    resp_text: "Welcome to Acme alerts! You'll receive up to 4 msgs/month. Reply HELP for help, STOP to cancel.",
    country_code: 'US',
  }, { headers });
  console.log(`Opt-in config: ${optIn.data.data.id}`);

  // Custom HELP response
  const help = await axios.post(baseUrl, {
    op: 'help',
    keywords: ['HELP', 'INFO'],
    resp_text: 'Acme Corp: For support call 1-800-555-0123. Reply STOP to opt out.',
    country_code: 'US',
  }, { headers });
  console.log(`Help config: ${help.data.data.id}`);
  ```

  ```ruby
  require "net/http"
  require "json"
  require "uri"

  api_key = ENV["TELNYX_API_KEY"]
  profile_id = "your_messaging_profile_id"
  base_url = "https://api.telnyx.com/v2/messaging_profiles/#{profile_id}/autoresp_configs"

  def create_config(url, api_key, data)
    uri = URI(url)
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true
    request = Net::HTTP::Post.new(uri)
    request["Authorization"] = "Bearer #{api_key}"
    request["Content-Type"] = "application/json"
    request.body = data.to_json
    response = http.request(request)
    JSON.parse(response.body)
  end

  # Opt-in
  result = create_config(base_url, api_key, {
    op: "start",
    keywords: ["JOIN", "SUBSCRIBE", "YES"],
    resp_text: "Welcome to Acme alerts! Reply HELP for help, STOP to cancel.",
    country_code: "US"
  })
  puts "Opt-in config: #{result['data']['id']}"
  ```

  ```go
  package main

  import (
    "bytes"
    "encoding/json"
    "fmt"
    "net/http"
    "os"
  )

  func createAutoResponse(profileID string, data map[string]interface{}) {
    url := fmt.Sprintf("https://api.telnyx.com/v2/messaging_profiles/%s/autoresp_configs", profileID)
    body, _ := json.Marshal(data)
    req, _ := http.NewRequest("POST", url, bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer "+os.Getenv("TELNYX_API_KEY"))
    req.Header.Set("Content-Type", "application/json")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    var result map[string]interface{}
    json.NewDecoder(resp.Body).Decode(&result)
    data2 := result["data"].(map[string]interface{})
    fmt.Printf("Config created: %s\n", data2["id"])
  }

  func main() {
    profileID := "your_messaging_profile_id"

    createAutoResponse(profileID, map[string]interface{}{
      "op":           "start",
      "keywords":     []string{"JOIN", "SUBSCRIBE", "YES"},
      "resp_text":    "Welcome to Acme alerts! Reply HELP for help, STOP to cancel.",
      "country_code": "US",
    })
  }
  ```

  ```php
  <?php
  $apiKey = getenv('TELNYX_API_KEY');
  $profileId = 'your_messaging_profile_id';
  $url = "https://api.telnyx.com/v2/messaging_profiles/{$profileId}/autoresp_configs";

  function createAutoResponse(string $url, string $apiKey, array $data): array
  {
      $ch = curl_init($url);
      curl_setopt_array($ch, [
          CURLOPT_POST => true,
          CURLOPT_RETURNTRANSFER => true,
          CURLOPT_HTTPHEADER => [
              "Authorization: Bearer {$apiKey}",
              'Content-Type: application/json',
          ],
          CURLOPT_POSTFIELDS => json_encode($data),
      ]);
      $response = json_decode(curl_exec($ch), true);
      curl_close($ch);
      return $response;
  }

  // Opt-in
  $result = createAutoResponse($url, $apiKey, [
      'op' => 'start',
      'keywords' => ['JOIN', 'SUBSCRIBE', 'YES'],
      'resp_text' => "Welcome to Acme alerts! Reply HELP for help, STOP to cancel.",
      'country_code' => 'US',
  ]);
  echo "Opt-in config: {$result['data']['id']}\n";
  ```

### Operation types

| Operation (`op`) | Purpose                      | Default keywords                              |
| ---------------- | ---------------------------- | --------------------------------------------- |
| `start`          | Opt-in — removes block rule  | START, UNSTOP                                 |
| `stop`           | Opt-out — creates block rule | STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT |
| `help`           | Help — sends info response   | HELP                                          |
| Custom           | Any custom keyword response  | (none)                                        |

***

## Country-specific auto-responses

Configure different responses per country using ISO 3166-1 alpha-2 codes. This enables localized language support:

  ```bash
  # English (US)
  curl -X POST \
    https://api.telnyx.com/v2/messaging_profiles/{profile_id}/autoresp_configs \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "op": "stop",
      "keywords": ["STOP"],
      "resp_text": "You have been unsubscribed. Reply START to resubscribe.",
      "country_code": "US"
    }'

  # Spanish (Mexico)
  curl -X POST \
    https://api.telnyx.com/v2/messaging_profiles/{profile_id}/autoresp_configs \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "op": "stop",
      "keywords": ["PARAR", "DETENER"],
      "resp_text": "Te has dado de baja. Responde INICIO para volver a suscribirte.",
      "country_code": "MX"
    }'

  # French (Canada)
  curl -X POST \
    https://api.telnyx.com/v2/messaging_profiles/{profile_id}/autoresp_configs \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "op": "stop",
      "keywords": ["ARRET", "ARRETER"],
      "resp_text": "Vous êtes désabonné. Répondez DEBUT pour vous réabonner.",
      "country_code": "CA"
    }'

  # UK English
  curl -X POST \
    https://api.telnyx.com/v2/messaging_profiles/{profile_id}/autoresp_configs \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "op": "start",
      "keywords": ["START"],
      "resp_text": "You are now subscribed to receive messages from Acme. Reply STOP to opt out.",
      "country_code": "GB"
    }'
  ```

> **Note:** The feature is **language agnostic** — you can use keywords and responses in any language. The `country_code` field determines which auto-response applies based on the sender's number origin.

***

## Track opt-out behavior via webhooks

When a user sends an opt-in, opt-out, or help keyword, the inbound message webhook includes an `autoresponse_type` field:

```json theme={null}
{
  "data": {
    "event_type": "message.received",
    "payload": {
      "autoresponse_type": "STOP",
      "from": {
        "phone_number": "+15559876543"
      },
      "text": "STOP",
      "to": [
        {
          "phone_number": "+15551234567"
        }
      ]
    }
  }
}
```

### Handle opt-out webhooks

  ```python
  from flask import Flask, request, jsonify

  app = Flask(__name__)

  @app.route("/webhooks/messaging", methods=["POST"])
  def handle_webhook():
      data = request.json["data"]

      if data["event_type"] != "message.received":
          return jsonify({"status": "ignored"}), 200

      payload = data["payload"]
      autoresponse_type = payload.get("autoresponse_type")
      phone = payload["from"]["phone_number"]

      if autoresponse_type == "STOP":
          # User opted out — update your database
          db.execute(
              "UPDATE subscribers SET opted_out = TRUE, opted_out_at = NOW() "
              "WHERE phone = %s",
              (phone,),
          )
          print(f"User {phone} opted out")

      elif autoresponse_type == "START":
          # User opted back in
          db.execute(
              "UPDATE subscribers SET opted_out = FALSE "
              "WHERE phone = %s",
              (phone,),
          )
          print(f"User {phone} opted back in")

      elif autoresponse_type == "HELP":
          # User requested help — log for support
          print(f"User {phone} requested help")

      return jsonify({"status": "ok"}), 200
  ```

  ```javascript
  import express from 'express';

  const app = express();
  app.use(express.json());

  app.post('/webhooks/messaging', async (req, res) => {
    const { data } = req.body;

    if (data.event_type !== 'message.received') {
      return res.json({ status: 'ignored' });
    }

    const { autoresponse_type } = data.payload;
    const phone = data.payload.from.phone_number;

    switch (autoresponse_type) {
      case 'STOP':
        await db.query(
          'UPDATE subscribers SET opted_out = TRUE WHERE phone = $1',
          [phone]
        );
        console.log(`User ${phone} opted out`);
        break;

      case 'START':
        await db.query(
          'UPDATE subscribers SET opted_out = FALSE WHERE phone = $1',
          [phone]
        );
        console.log(`User ${phone} opted back in`);
        break;

      case 'HELP':
        console.log(`User ${phone} requested help`);
        break;
    }

    res.json({ status: 'ok' });
  });
  ```

> **Note:** The `autoresponse_type` field is also available in your [SMS Logs](message-detail-records.md) via Detail Record Search reporting.

***

## Limitations

**Reserved keywords**

    **START**, **STOP**, and **HELP** are reserved keywords for their respective operations and **cannot be reassigned** to different operations. You can add additional keywords to each operation, but the defaults always remain active.

---

**Auto-response minimum length**

    Default operations (start, stop, help) require a **minimum 20 characters** for the auto-response message. This ensures compliance with carrier requirements.

---

**Maximum keywords per configuration**

    Each auto-response configuration supports a maximum of **20 trigger keywords**.

---

**Toll-free limitations**

    Toll-free numbers have a **separate carrier-level opt-out system** that Telnyx cannot customize or remove. When a user texts STOP to a toll-free number:

    1. The carrier sends its own auto-reply:

    > *NETWORK MSG: You replied with the word "stop" which blocks all texts sent from this number. Text back "unstop" to receive messages again.*

    2. Your custom STOP response is **also sent** (if configured)
    3. The carrier block is applied independently of Telnyx's block rule

    When a user texts START or UNSTOP:

    > *NETWORK MSG: You have replied "unstop" and will begin receiving messages again from this number.*

    > **Warning:** You cannot prevent the carrier's NETWORK MSG responses on toll-free numbers. Design your custom responses to complement (not contradict) these messages.

---

**Block rule scope**

    Block rules apply at the **messaging profile level**, not the individual number level. If a user opts out from any number on your profile, they're blocked from all numbers on that profile.

    To manage separate opt-out lists for different programs, use separate messaging profiles.

---

***

## Related resources

  - [Messaging Profiles](../concepts/messaging-profiles-overview.md) — Configure the messaging profile that manages your opt-in/out rules.

  - [Webhooks](receiving-webhooks-for-messaging.md) — Set up webhooks to receive opt-in/out events.

  - [Short Codes](short-codes.md) — Short code keyword handling and carrier certification.

  - [Toll-Free Verification](toll-free-verification-with-business-registration-fields.md) — Toll-free number verification and compliance.
