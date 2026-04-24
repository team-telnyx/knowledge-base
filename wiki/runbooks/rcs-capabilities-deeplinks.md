---
title: RCS Capabilities & Deeplinks
summary: Query device RCS capabilities before sending and generate deeplinks to start RCS conversations from websites or QR codes.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/rcs-capabilities/index
    content_hash: 388da005bcf51430cbed0cc19f789493467dcc7c00be626dc5ca225befacc046
updated_at: 2026-04-10T00:00:00Z
---

# RCS Capabilities & Deeplinks

Query device RCS capabilities before sending and generate deeplinks to start RCS conversations from websites or QR codes.

Check whether a recipient's device supports RCS — and which features it supports — before sending. This lets you adapt your message format (rich card vs. plain text) and fall back to SMS when needed.

## Query single number

Check RCS capabilities for a single phone number:

  ```bash
  curl -s https://api.telnyx.com/v2/messaging/rcs/capabilities/{agent_id}/{phone_number} \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

  ```python
  import os
  import requests

  API_KEY = os.environ.get("TELNYX_API_KEY")
  AGENT_ID = "your_agent_id"

  headers = {"Authorization": f"Bearer {API_KEY}"}

  def check_rcs_capabilities(phone_number: str) -> dict:
      """Check if a phone number supports RCS and which features."""
      response = requests.get(
          f"https://api.telnyx.com/v2/messaging/rcs/capabilities/{AGENT_ID}/{phone_number}",
          headers=headers,
      )
      data = response.json()["data"]
      return {
          "phone_number": data["phone_number"],
          "rcs_enabled": bool(data.get("features")),
          "features": data.get("features") or [],
          "supports_rich_cards": "RICHCARD_STANDALONE" in (data.get("features") or []),
          "supports_carousel": "RICHCARD_CAROUSEL" in (data.get("features") or []),
      }

  result = check_rcs_capabilities("+15559876543")
  print(f"RCS enabled: {result['rcs_enabled']}")
  print(f"Features: {result['features']}")
  ```

  ```javascript
  const axios = require('axios');

  const headers = {
    Authorization: `Bearer ${process.env.TELNYX_API_KEY}`,
  };
  const agentId = 'your_agent_id';

  async function checkRcsCapabilities(phoneNumber) {
    const response = await axios.get(
      `https://api.telnyx.com/v2/messaging/rcs/capabilities/${agentId}/${phoneNumber}`,
      { headers }
    );
    const { data } = response.data;
    return {
      phoneNumber: data.phone_number,
      rcsEnabled: Boolean(data.features?.length),
      features: data.features || [],
      supportsRichCards: data.features?.includes('RICHCARD_STANDALONE') ?? false,
      supportsCarousel: data.features?.includes('RICHCARD_CAROUSEL') ?? false,
    };
  }

  const result = await checkRcsCapabilities('+15559876543');
  console.log(`RCS enabled: ${result.rcsEnabled}`);
  console.log(`Features: ${result.features.join(', ')}`);
  ```

  ```ruby
  require "net/http"
  require "json"
  require "uri"

  api_key = ENV["TELNYX_API_KEY"]
  agent_id = "your_agent_id"

  def check_rcs(agent_id, phone_number, api_key)
    uri = URI("https://api.telnyx.com/v2/messaging/rcs/capabilities/#{agent_id}/#{phone_number}")
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true
    request = Net::HTTP::Get.new(uri)
    request["Authorization"] = "Bearer #{api_key}"
    response = http.request(request)
    data = JSON.parse(response.body)["data"]
    {
      rcs_enabled: !data["features"].nil? && !data["features"].empty?,
      features: data["features"] || []
    }
  end

  result = check_rcs(agent_id, "+15559876543", api_key)
  puts "RCS enabled: #{result[:rcs_enabled]}"
  ```

  ```go
  package main

  import (
    "encoding/json"
    "fmt"
    "net/http"
    "os"
  )

  func checkRCS(agentID, phoneNumber string) ([]string, error) {
    url := fmt.Sprintf("https://api.telnyx.com/v2/messaging/rcs/capabilities/%s/%s", agentID, phoneNumber)
    req, _ := http.NewRequest("GET", url, nil)
    req.Header.Set("Authorization", "Bearer "+os.Getenv("TELNYX_API_KEY"))

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
      return nil, err
    }
    defer resp.Body.Close()

    var result struct {
      Data struct {
        Features []string `json:"features"`
      } `json:"data"`
    }
    json.NewDecoder(resp.Body).Decode(&result)
    return result.Data.Features, nil
  }

  func main() {
    features, _ := checkRCS("your_agent_id", "+15559876543")
    fmt.Printf("Features: %v\n", features)
  }
  ```

  ```php
  <?php
  $apiKey = getenv('TELNYX_API_KEY');
  $agentId = 'your_agent_id';
  $phoneNumber = '+15559876543';

  $ch = curl_init("https://api.telnyx.com/v2/messaging/rcs/capabilities/{$agentId}/{$phoneNumber}");
  curl_setopt_array($ch, [
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => ["Authorization: Bearer {$apiKey}"],
  ]);

  $data = json_decode(curl_exec($ch), true)['data'];
  curl_close($ch);

  $rcsEnabled = !empty($data['features']);
  echo "RCS enabled: " . ($rcsEnabled ? 'yes' : 'no') . "\n";
  echo "Features: " . implode(', ', $data['features'] ?? []) . "\n";
  ```

### Response examples

### Full RCS support

    ```json theme={null}
    {
      "data": {
        "record_type": "rcs.capabilities",
        "phone_number": "+15559876543",
        "agent_id": "your_agent_id",
        "agent_name": "Acme Bot",
        "features": [
          "ACTION_CREATE_CALENDAR_EVENT",
          "ACTION_DIAL",
          "ACTION_OPEN_URL",
          "ACTION_OPEN_URL_IN_WEBVIEW",
          "ACTION_SHARE_LOCATION",
          "ACTION_VIEW_LOCATION",
          "RICHCARD_CAROUSEL",
          "RICHCARD_STANDALONE"
        ],
        "status": "Success"
      }
    }
    ```

### Generic RCS (limited features)

    ```json theme={null}
    {
      "data": {
        "features": ["GENERIC_RCS_FEATURE"],
        "status": "Success"
      }
    }
    ```

    The device supports RCS but specific features couldn't be determined. Send basic RCS text — avoid rich cards.

### No RCS support

    ```json theme={null}
    {
      "data": {
        "features": null,
        "status": "RCS is disabled or agent is not provisioned for the carrier"
      }
    }
    ```

    Fall back to SMS/MMS for this recipient.

### Feature reference

| Feature                        | Description                 | Use for                      |
| ------------------------------ | --------------------------- | ---------------------------- |
| `RICHCARD_STANDALONE`          | Single rich card support    | Product cards, order updates |
| `RICHCARD_CAROUSEL`            | Swipeable carousel cards    | Product listings, menus      |
| `ACTION_OPEN_URL`              | Open URL button             | Links to websites            |
| `ACTION_OPEN_URL_IN_WEBVIEW`   | Open URL in webview         | In-app browsing              |
| `ACTION_DIAL`                  | Phone call button           | Click-to-call                |
| `ACTION_VIEW_LOCATION`         | View map location           | Directions, store locator    |
| `ACTION_SHARE_LOCATION`        | Share user's location       | Delivery tracking            |
| `ACTION_CREATE_CALENDAR_EVENT` | Add calendar event          | Appointment booking          |
| `ACTION_COMPOSE`               | Compose message             | Message drafting             |
| `GENERIC_RCS_FEATURE`          | Basic RCS (details unknown) | Text-only RCS                |

***

## Bulk capability query

Check up to 100 numbers at once to efficiently segment your audience:

  ```bash
  curl -X POST https://api.telnyx.com/v2/messaging/rcs/bulk_capabilities \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "agent_id": "your_agent_id",
      "phone_numbers": ["+15551234567", "+15559876543", "+15550001111"]
    }'
  ```

  ```python
  def bulk_check_rcs(phone_numbers: list[str]) -> dict:
      """Check RCS capabilities for up to 100 numbers."""
      response = requests.post(
          "https://api.telnyx.com/v2/messaging/rcs/bulk_capabilities",
          headers={**headers, "Content-Type": "application/json"},
          json={
              "agent_id": AGENT_ID,
              "phone_numbers": phone_numbers,
          },
      )

      results = {"rcs": [], "sms_fallback": []}
      for entry in response.json()["data"]:
          if entry.get("features"):
              results["rcs"].append(entry["phone_number"])
          else:
              results["sms_fallback"].append(entry["phone_number"])

      return results

  # Segment audience
  numbers = ["+15551234567", "+15559876543", "+15550001111"]
  segments = bulk_check_rcs(numbers)
  print(f"RCS capable: {len(segments['rcs'])}")
  print(f"SMS fallback: {len(segments['sms_fallback'])}")
  ```

  ```javascript
  async function bulkCheckRcs(phoneNumbers) {
    const response = await axios.post(
      'https://api.telnyx.com/v2/messaging/rcs/bulk_capabilities',
      {
        agent_id: agentId,
        phone_numbers: phoneNumbers,
      },
      { headers: { ...headers, 'Content-Type': 'application/json' } }
    );

    const results = { rcs: [], smsFallback: [] };
    for (const entry of response.data.data) {
      if (entry.features?.length) {
        results.rcs.push(entry.phone_number);
      } else {
        results.smsFallback.push(entry.phone_number);
      }
    }
    return results;
  }

  const segments = await bulkCheckRcs(['+15551234567', '+15559876543']);
  console.log(`RCS: ${segments.rcs.length}, SMS: ${segments.smsFallback.length}`);
  ```

> **Warning:** RCS capability queries can be **slow** (several seconds per request). For time-sensitive applications, cache results and refresh periodically rather than querying before every message.

***

## Send with automatic fallback

Use capability queries to send the best possible message format:

```python
def send_adaptive_message(to: str, title: str, body: str, image_url: str = None):
    """Send RCS rich card if supported, otherwise fall back to SMS."""
    caps = check_rcs_capabilities(to)

    if caps["supports_rich_cards"] and image_url:
        # Send rich card
        requests.post(
            "https://api.telnyx.com/v2/messages/rcs",
            headers={**headers, "Content-Type": "application/json"},
            json={
                "agent_id": AGENT_ID,
                "to": to,
                "messaging_profile_id": PROFILE_ID,
                "agent_message": {
                    "content_message": {
                        "rich_card": {
                            "standalone_card": {
                                "card_orientation": "VERTICAL",
                                "card_content": {
                                    "title": title,
                                    "description": body,
                                    "media": {
                                        "height": "MEDIUM",
                                        "content_info": {"file_url": image_url},
                                    },
                                },
                            }
                        }
                    }
                },
                "fallback": {
                    "from": FROM_NUMBER,
                    "text": f"{title}\n{body}",
                },
            },
        )
    elif caps["rcs_enabled"]:
        # Send RCS text (no rich card support)
        requests.post(
            "https://api.telnyx.com/v2/messages/rcs",
            headers={**headers, "Content-Type": "application/json"},
            json={
                "agent_id": AGENT_ID,
                "to": to,
                "messaging_profile_id": PROFILE_ID,
                "agent_message": {
                    "content_message": {"text": f"{title}\n{body}"}
                },
                "fallback": {"from": FROM_NUMBER, "text": f"{title}\n{body}"},
            },
        )
    else:
        # Send SMS directly
        requests.post(
            "https://api.telnyx.com/v2/messages",
            headers={**headers, "Content-Type": "application/json"},
            json={"from": FROM_NUMBER, "to": to, "text": f"{title}\n{body}"},
        )
```

***

## RCS Deeplinks

Deeplinks let users start an RCS conversation from a website, email, or QR code — without having your number saved.

### Generate a deeplink

  ```bash
  # With fallback phone number and message body
  curl -s 'https://api.telnyx.com/v2/messages/rcs/deeplinks/{agent_id}?phone_number=%2B15554443333&body=hello%20world' \
    -H "Authorization: Bearer YOUR_API_KEY"

  # Without fallback (RCS only)
  curl -s 'https://api.telnyx.com/v2/messages/rcs/deeplinks/{agent_id}' \
    -H "Authorization: Bearer YOUR_API_KEY"
  ```

  ```python
  import urllib.parse

  def generate_deeplink(
      agent_id: str,
      fallback_phone: str = None,
      message_body: str = None,
  ) -> str:
      """Generate an RCS deeplink URL."""
      url = f"https://api.telnyx.com/v2/messages/rcs/deeplinks/{agent_id}"
      params = {}
      if fallback_phone:
          params["phone_number"] = fallback_phone
      if message_body:
          params["body"] = message_body

      if params:
          url += "?" + urllib.parse.urlencode(params)

      response = requests.get(url, headers=headers)
      return response.json()["data"]["url"]

  # Generate deeplink with fallback
  link = generate_deeplink(
      agent_id="your_agent_id",
      fallback_phone="+15554443333",
      message_body="Hi, I'd like to learn more!",
  )
  print(f"Deeplink: {link}")
  ```

  ```javascript
  async function generateDeeplink(agentId, fallbackPhone, messageBody) {
    const params = new URLSearchParams();
    if (fallbackPhone) params.set('phone_number', fallbackPhone);
    if (messageBody) params.set('body', messageBody);

    const url = `https://api.telnyx.com/v2/messages/rcs/deeplinks/${agentId}${
      params.toString() ? '?' + params.toString() : ''
    }`;

    const response = await axios.get(url, { headers });
    return response.data.data.url;
  }

  const link = await generateDeeplink('your_agent_id', '+15554443333', 'Hi!');
  console.log(`Deeplink: ${link}`);
  ```

### Response

```json theme={null}
{
  "data": {
    "url": "sms:+18445550001?service_id=agent_id%40rbm.goog&body=hello%20world"
  }
}
```

### Use deeplinks

**Website button**

    Embed the deeplink in an HTML button or link. The URL won't open directly in a browser — it must be an `<a>` tag or button click:

    ```html theme={null}
    <a href="sms:+18445550001?service_id=agent_id%40rbm.goog&body=Hi!"
       class="rcs-button">
      💬 Chat with us on RCS
    </a>
    ```

---

**QR code**

    Convert the deeplink URL to a QR code for print materials, in-store signage, or business cards. Users scan with their camera to open an RCS conversation.

---

**Email campaigns**

    Include the deeplink in marketing emails as a CTA button. When tapped on Android with Google Messages, it opens the RCS conversation directly.

---

### Requirements

| Requirement    | Details                                                              |
| -------------- | -------------------------------------------------------------------- |
| **Device**     | Android with Google Messages installed                               |
| **OS version** | `messages.android_20241029_00` or later                              |
| **Fallback**   | Use `phone_number` parameter for non-RCS devices (opens SMS instead) |

***

## Related resources

  - [Send RCS Messages](send-rcs-messages.md) — Send text, rich cards, carousels, and suggested actions.

  - [RCS Webhooks](receiving-rcs-webhooks.md) — Handle inbound RCS messages and delivery events.

  - [RCS Getting Started](../tutorial/rcs-getting-started.md) — Set up your RCS agent and get approved.

  - [RCS API Reference](https://developers.telnyx.com/api-reference/rcs-messaging/send-an-rcs-message) — Full API reference for RCS messaging.


## Related Pages

- [RCS Deeplinks](../runbooks/rcs-deeplinks.md)
