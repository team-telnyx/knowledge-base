---
title: Send RCS Messages
summary: Send rich RCS messages with text, rich cards, carousels, and suggested actions using the Telnyx RCS API.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/send-an-rcs-message/index
    content_hash: 90b2eb4aeaa3396d0363713692600f0cbec24f30da619974a23aecafacddc256
updated_at: 2026-04-10T00:00:00Z
---

# Send RCS Messages

Send rich RCS messages with text, rich cards, carousels, and suggested actions using the Telnyx RCS API. Includes SDK examples and SMS fallback.

Send rich, interactive messages using RCS (Rich Communication Services). This guide covers sending text, rich cards, carousels, and configuring SMS fallback for non-RCS devices.

> **Note:** **New to RCS?** Start with the [RCS Getting Started](../tutorial/rcs-getting-started.md) guide to set up your RCS agent and get approved by Google.

## Prerequisites

* A verified [RCS agent](../tutorial/rcs-getting-started.md) approved by Google
* A [messaging profile](../concepts/messaging-profiles-overview.md) with RCS enabled
* Your agent ID (from the RCS agent setup)

***

## Send a text message

The simplest RCS message — plain text with optional suggested replies:

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages/rcs \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "agent_id": "your_agent_id",
      "to": "+15559876543",
      "messaging_profile_id": "your_messaging_profile_id",
      "agent_message": {
        "content_message": {
          "text": "Hi! How can we help you today?"
        }
      }
    }'
  ```

  ```python
  import os
  import requests

  API_KEY = os.environ.get("TELNYX_API_KEY")
  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json",
  }

  response = requests.post(
      "https://api.telnyx.com/v2/messages/rcs",
      headers=headers,
      json={
          "agent_id": "your_agent_id",
          "to": "+15559876543",
          "messaging_profile_id": "your_messaging_profile_id",
          "agent_message": {
              "content_message": {
                  "text": "Hi! How can we help you today?"
              }
          },
      },
  )

  print(f"Message sent: {response.json()['data']['id']}")
  ```

  ```javascript
  const axios = require('axios');

  const headers = {
    Authorization: `Bearer ${process.env.TELNYX_API_KEY}`,
    'Content-Type': 'application/json',
  };

  const response = await axios.post(
    'https://api.telnyx.com/v2/messages/rcs',
    {
      agent_id: 'your_agent_id',
      to: '+15559876543',
      messaging_profile_id: 'your_messaging_profile_id',
      agent_message: {
        content_message: {
          text: 'Hi! How can we help you today?',
        },
      },
    },
    { headers }
  );

  console.log(`Message sent: ${response.data.data.id}`);
  ```

  ```ruby
  require "net/http"
  require "json"
  require "uri"

  uri = URI("https://api.telnyx.com/v2/messages/rcs")
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true

  request = Net::HTTP::Post.new(uri)
  request["Authorization"] = "Bearer #{ENV['TELNYX_API_KEY']}"
  request["Content-Type"] = "application/json"
  request.body = {
    agent_id: "your_agent_id",
    to: "+15559876543",
    messaging_profile_id: "your_messaging_profile_id",
    agent_message: {
      content_message: {
        text: "Hi! How can we help you today?"
      }
    }
  }.to_json

  response = http.request(request)
  data = JSON.parse(response.body)
  puts "Message sent: #{data['data']['id']}"
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

  func main() {
    payload := map[string]interface{}{
      "agent_id":              "your_agent_id",
      "to":                    "+15559876543",
      "messaging_profile_id":  "your_messaging_profile_id",
      "agent_message": map[string]interface{}{
        "content_message": map[string]interface{}{
          "text": "Hi! How can we help you today?",
        },
      },
    }

    body, _ := json.Marshal(payload)
    req, _ := http.NewRequest("POST", "https://api.telnyx.com/v2/messages/rcs", bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer "+os.Getenv("TELNYX_API_KEY"))
    req.Header.Set("Content-Type", "application/json")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    var result map[string]interface{}
    json.NewDecoder(resp.Body).Decode(&result)
    data := result["data"].(map[string]interface{})
    fmt.Printf("Message sent: %s\n", data["id"])
  }
  ```

  ```php
  <?php
  $apiKey = getenv('TELNYX_API_KEY');

  $payload = [
      'agent_id' => 'your_agent_id',
      'to' => '+15559876543',
      'messaging_profile_id' => 'your_messaging_profile_id',
      'agent_message' => [
          'content_message' => [
              'text' => 'Hi! How can we help you today?'
          ]
      ]
  ];

  $ch = curl_init('https://api.telnyx.com/v2/messages/rcs');
  curl_setopt_array($ch, [
      CURLOPT_POST => true,
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => [
          "Authorization: Bearer {$apiKey}",
          'Content-Type: application/json',
      ],
      CURLOPT_POSTFIELDS => json_encode($payload),
  ]);

  $response = json_decode(curl_exec($ch), true);
  curl_close($ch);

  echo "Message sent: {$response['data']['id']}\n";
  ```

***

## Send a rich card

Rich cards display media, text, and action buttons in an interactive format:

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages/rcs \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "agent_id": "your_agent_id",
      "to": "+15559876543",
      "messaging_profile_id": "your_messaging_profile_id",
      "agent_message": {
        "content_message": {
          "rich_card": {
            "standalone_card": {
              "card_orientation": "VERTICAL",
              "thumbnail_image_alignment": "LEFT",
              "card_content": {
                "title": "Order Shipped! 📦",
                "description": "Your order #12345 is on its way. Expected delivery: March 15.",
                "media": {
                  "height": "MEDIUM",
                  "content_info": {
                    "file_url": "https://example.com/shipping.jpg",
                    "content_type": "image/jpeg"
                  }
                },
                "suggestions": [
                  {
                    "action": {
                      "text": "Track Order",
                      "open_url_action": {
                        "url": "https://example.com/track/12345"
                      }
                    }
                  },
                  {
                    "reply": {
                      "text": "Contact Support",
                      "postback_data": "support_request"
                    }
                  }
                ]
              }
            }
          }
        }
      }
    }'
  ```

  ```python
  response = requests.post(
      "https://api.telnyx.com/v2/messages/rcs",
      headers=headers,
      json={
          "agent_id": "your_agent_id",
          "to": "+15559876543",
          "messaging_profile_id": "your_messaging_profile_id",
          "agent_message": {
              "content_message": {
                  "rich_card": {
                      "standalone_card": {
                          "card_orientation": "VERTICAL",
                          "thumbnail_image_alignment": "LEFT",
                          "card_content": {
                              "title": "Order Shipped! 📦",
                              "description": "Your order #12345 is on its way.",
                              "media": {
                                  "height": "MEDIUM",
                                  "content_info": {
                                      "file_url": "https://example.com/shipping.jpg",
                                      "content_type": "image/jpeg",
                                  },
                              },
                              "suggestions": [
                                  {
                                      "action": {
                                          "text": "Track Order",
                                          "open_url_action": {
                                              "url": "https://example.com/track/12345"
                                          },
                                      }
                                  },
                                  {
                                      "reply": {
                                          "text": "Contact Support",
                                          "postback_data": "support_request",
                                      }
                                  },
                              ],
                          },
                      }
                  }
              }
          },
      },
  )

  print(f"Rich card sent: {response.json()['data']['id']}")
  ```

  ```javascript
  const response = await axios.post(
    'https://api.telnyx.com/v2/messages/rcs',
    {
      agent_id: 'your_agent_id',
      to: '+15559876543',
      messaging_profile_id: 'your_messaging_profile_id',
      agent_message: {
        content_message: {
          rich_card: {
            standalone_card: {
              card_orientation: 'VERTICAL',
              thumbnail_image_alignment: 'LEFT',
              card_content: {
                title: 'Order Shipped! 📦',
                description: 'Your order #12345 is on its way.',
                media: {
                  height: 'MEDIUM',
                  content_info: {
                    file_url: 'https://example.com/shipping.jpg',
                    content_type: 'image/jpeg',
                  },
                },
                suggestions: [
                  {
                    action: {
                      text: 'Track Order',
                      open_url_action: {
                        url: 'https://example.com/track/12345',
                      },
                    },
                  },
                  {
                    reply: {
                      text: 'Contact Support',
                      postback_data: 'support_request',
                    },
                  },
                ],
              },
            },
          },
        },
      },
    },
    { headers }
  );

  console.log(`Rich card sent: ${response.data.data.id}`);
  ```

### Card options

| Property                    | Values                    | Description                            |
| --------------------------- | ------------------------- | -------------------------------------- |
| `card_orientation`          | `VERTICAL`, `HORIZONTAL`  | Card layout direction                  |
| `thumbnail_image_alignment` | `LEFT`, `RIGHT`           | Image position (horizontal cards only) |
| `media.height`              | `SHORT`, `MEDIUM`, `TALL` | Image display height                   |

***

## Send a carousel

Display multiple cards in a swipeable carousel — ideal for product listings:

```bash
curl -X POST https://api.telnyx.com/v2/messages/rcs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "agent_id": "your_agent_id",
    "to": "+15559876543",
    "messaging_profile_id": "your_messaging_profile_id",
    "agent_message": {
      "content_message": {
        "rich_card": {
          "carousel_card": {
            "card_width": "MEDIUM",
            "card_contents": [
              {
                "title": "Classic Burger",
                "description": "$8.99 — Our signature burger",
                "media": {
                  "height": "MEDIUM",
                  "content_info": {
                    "file_url": "https://example.com/burger.jpg"
                  }
                },
                "suggestions": [
                  {
                    "action": {
                      "text": "Order Now",
                      "open_url_action": {
                        "url": "https://example.com/order/burger"
                      }
                    }
                  }
                ]
              },
              {
                "title": "Veggie Wrap",
                "description": "$7.49 — Fresh and healthy",
                "media": {
                  "height": "MEDIUM",
                  "content_info": {
                    "file_url": "https://example.com/wrap.jpg"
                  }
                },
                "suggestions": [
                  {
                    "action": {
                      "text": "Order Now",
                      "open_url_action": {
                        "url": "https://example.com/order/wrap"
                      }
                    }
                  }
                ]
              }
            ]
          }
        }
      }
    }
  }'
```

> **Note:** Carousels require a minimum of 2 cards and a maximum of 10. All cards in a carousel use the same `card_width`.

***

## Add suggested actions

Suggestions appear as tappable buttons below your message:

### Suggested replies

    Quick reply buttons that send a predefined response back to your webhook:

    ```json theme={null}
    "suggestions": [
      {
        "reply": {
          "text": "Yes, confirm",
          "postback_data": "confirm_order_12345"
        }
      },
      {
        "reply": {
          "text": "No, cancel",
          "postback_data": "cancel_order_12345"
        }
      }
    ]
    ```

### URL actions

    Open a URL in the device browser:

    ```json theme={null}
    "suggestions": [
      {
        "action": {
          "text": "Visit Website",
          "open_url_action": {
            "url": "https://example.com"
          }
        }
      }
    ]
    ```

### Dial actions

    Initiate a phone call:

    ```json theme={null}
    "suggestions": [
      {
        "action": {
          "text": "Call Us",
          "dial_action": {
            "phone_number": "+15551234567"
          }
        }
      }
    ]
    ```

### Location actions

    Open a map location:

    ```json theme={null}
    "suggestions": [
      {
        "action": {
          "text": "Get Directions",
          "view_location_action": {
            "lat_long": {
              "latitude": 40.7128,
              "longitude": -74.0060
            },
            "label": "Acme Corp HQ"
          }
        }
      }
    ]
    ```

***

## SMS fallback

Not all devices support RCS. Configure automatic SMS fallback for non-RCS recipients:

  ```bash
  curl -X POST https://api.telnyx.com/v2/messages/rcs \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{
      "agent_id": "your_agent_id",
      "to": "+15559876543",
      "messaging_profile_id": "your_messaging_profile_id",
      "agent_message": {
        "content_message": {
          "text": "Your order #12345 has shipped! Track at https://example.com/track/12345"
        }
      },
      "fallback": {
        "from": "+15551234567",
        "text": "Your order #12345 has shipped! Track at https://example.com/track/12345"
      }
    }'
  ```

  ```python
  response = requests.post(
      "https://api.telnyx.com/v2/messages/rcs",
      headers=headers,
      json={
          "agent_id": "your_agent_id",
          "to": "+15559876543",
          "messaging_profile_id": "your_messaging_profile_id",
          "agent_message": {
              "content_message": {
                  "text": "Your order #12345 has shipped! Track at https://example.com/track/12345"
              }
          },
          "fallback": {
              "from": "+15551234567",
              "text": "Your order #12345 has shipped! Track at https://example.com/track/12345",
          },
      },
  )

  data = response.json()["data"]
  print(f"Sent via: {data['type']}")  # "RCS" or "SMS" depending on device support
  ```

  ```javascript
  const response = await axios.post(
    'https://api.telnyx.com/v2/messages/rcs',
    {
      agent_id: 'your_agent_id',
      to: '+15559876543',
      messaging_profile_id: 'your_messaging_profile_id',
      agent_message: {
        content_message: {
          text: 'Your order #12345 has shipped!',
        },
      },
      fallback: {
        from: '+15551234567',
        text: 'Your order #12345 has shipped! Track at https://example.com/track/12345',
      },
    },
    { headers }
  );

  console.log(`Sent via: ${response.data.data.type}`);
  ```

> **Warning:** The `fallback.from` number must be a Telnyx number on your messaging profile with SMS capability. The fallback message is plain text only — rich card content is not included.

***

## RCS vs. SMS/MMS comparison

| Feature               | RCS                | SMS          | MMS          |
| --------------------- | ------------------ | ------------ | ------------ |
| **Rich cards**        | ✅                  | ❌            | ❌            |
| **Carousels**         | ✅                  | ❌            | ❌            |
| **Suggested actions** | ✅                  | ❌            | ❌            |
| **Read receipts**     | ✅                  | ❌            | ❌            |
| **Typing indicators** | ✅                  | ❌            | ❌            |
| **Images/video**      | ✅ High-res         | ❌            | ✅ Compressed |
| **Character limit**   | None               | 160/segment  | None         |
| **Device support**    | Android (+ iOS 18) | Universal    | Universal    |
| **Encoding**          | UTF-8              | GSM-7/UTF-16 | UTF-8        |

***

## Related resources

  - [RCS Getting Started](../tutorial/rcs-getting-started.md) — Set up your RCS agent and get approved by Google.

  - [RCS Capabilities](rcs-capabilities-deeplinks.md) — Check device RCS capability before sending.

  - [RCS Webhooks](receiving-rcs-webhooks.md) — Handle inbound RCS messages and delivery events.

  - [RCS API Reference](https://developers.telnyx.com/api-reference/rcs-messaging/send-an-rcs-message) — Full API reference for RCS messaging.


## Related Pages

- [Send WhatsApp Messages](../runbooks/send-whatsapp-messages.md)
- [Send Your First Message](../runbooks/send-your-first-message.md)
- [Schedule SMS and MMS Messages](../runbooks/schedule-sms-and-mms-messages.md)
- [Messages](../runbooks/messages.md)
- [Messages](../runbooks/messages-2.md)
