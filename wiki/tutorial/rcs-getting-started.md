---
title: RCS Getting Started
summary: Get started with RCS messaging using the Telnyx RCS API.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index
    content_hash: e79895232286fdeb1eb6347f3040550ee80b3b24f1cb88de99d10e44c2ccd938
updated_at: 2026-04-10T00:00:00Z
---

# RCS Getting Started

Get started with RCS messaging using the Telnyx RCS API.

Send rich, interactive messages with RCS (Rich Communication Services). This guide covers the setup process, approval timeline, and how to send your first RCS message.

## What is RCS?

RCS is a messaging protocol that delivers app-like experiences in the native messaging app—no app download required. Unlike SMS/MMS, RCS supports:

* **Rich cards** with images, titles, and action buttons
* **Carousels** for product showcases
* **Suggested replies** for quick responses
* **Read receipts** and typing indicators
* **High-resolution media** (images, video, files)

<Callout type="info">
  RCS is currently supported on Android devices. Apple announced RCS support in iOS 18.

## Prerequisites

* A [Telnyx account](https://telnyx.com/sign-up)

## Approval process

RCS requires agent registration and carrier approval before you can send messages to the general public. The process is similar to short code approval:

1. **Submit your RCS Agent**

    [Contact sales](https://telnyx.com/contact-us) to start the onboarding process. Provide your brand details, use case, and sample message content.

2. **Testing stage**

    Once submitted, Telnyx moves your agent into a testing stage. During this phase, you can invite beta test numbers using the API to test your integration while waiting for carrier approval.

3. **Carrier approval**

    Carriers review and approve your agent. This process typically takes **4-6 weeks**, similar to short code approval.

4. **Go live**

    Once approved, your RCS Agent can send messages to any RCS-capable device.

<Callout type="info">
  **Testing during approval:** You don't have to wait for full carrier approval to start testing. Once your agent is in testing stage, you can add beta numbers and send test messages via the API.

## 1. Create a Messaging Profile

5. **Go to Messaging**

    Navigate to [Messaging](https://portal.telnyx.com/#/app/messaging) in the portal.

6. **Create a profile**

    Click **Add new profile**, give it a name (e.g., "RCS Profile"), and click **Save**.

7. **Note your profile ID**

    Copy the Messaging Profile ID—you'll need it when sending messages.

## 2. Get your API key

Go to [API Keys](https://portal.telnyx.com/#/app/api-keys) and copy your API key (or create one if needed).

## 3. Send an RCS message

Once your RCS Agent is in testing stage (or fully approved), you can send messages to your beta test numbers or approved destinations.

### Text Message

    Send a simple text message via RCS:

      ```bash
      curl -X POST https://api.telnyx.com/v2/messages/rcs \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
          "agent_id": "your_rcs_agent_id",
          "to": "+15559876543",
          "messaging_profile_id": "your_messaging_profile_id",
          "agent_message": {
            "content_message": {
              "text": "Hello from Telnyx RCS!"
            }
          }
        }'
      ```

      ```javascript
      import Telnyx from 'telnyx';

      const client = new Telnyx({
        apiKey: process.env['TELNYX_API_KEY'],
      });

      const response = await client.messages.rcs.send({
        agent_id: 'your_rcs_agent_id',
        to: '+15559876543',
        messaging_profile_id: 'your_messaging_profile_id',
        agent_message: {
          content_message: {
            text: 'Hello from Telnyx RCS!'
          }
        }
      });

      console.log(response.data);
      ```

      ```python
      import os
      from telnyx import Telnyx

      client = Telnyx(
          api_key=os.environ.get("TELNYX_API_KEY"),
      )

      response = client.messages.rcs.send(
          agent_id="your_rcs_agent_id",
          to="+15559876543",
          messaging_profile_id="your_messaging_profile_id",
          agent_message={
              "content_message": {
                  "text": "Hello from Telnyx RCS!"
              }
          }
      )

      print(response.data)
      ```

      ```ruby
      require "telnyx"

      client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

      response = client.messages.rcs.send(
        agent_id: "your_rcs_agent_id",
        to: "+15559876543",
        messaging_profile_id: "your_messaging_profile_id",
        agent_message: {
          content_message: {
            text: "Hello from Telnyx RCS!"
          }
        }
      )

      puts(response)
      ```

      ```go
      package main

      import (
        "context"
        "fmt"
        "os"

        "github.com/team-telnyx/telnyx-go/v4"
        "github.com/team-telnyx/telnyx-go/v4/option"
      )

      func main() {
        client := telnyx.NewClient(
          option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
        )
        response, err := client.Messages.Rcs.Send(context.TODO(), telnyx.MessageRcSendParams{
          AgentID:            telnyx.String("your_rcs_agent_id"),
          To:                 telnyx.String("+15559876543"),
          MessagingProfileID: telnyx.String("your_messaging_profile_id"),
          AgentMessage: telnyx.RcsAgentMessageParam{
            ContentMessage: telnyx.RcsAgentMessageContentMessageParam{
              Text: telnyx.String("Hello from Telnyx RCS!"),
            },
          },
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
      import com.telnyx.sdk.models.messages.RcsMessageSendParams;
      import com.telnyx.sdk.models.messages.RcsMessageSendResponse;

      public final class Main {
          public static void main(String[] args) {
              TelnyxClient client = TelnyxOkHttpClient.fromEnv();

              RcsMessageSendParams params = RcsMessageSendParams.builder()
                  .agentId("your_rcs_agent_id")
                  .to("+15559876543")
                  .messagingProfileId("your_messaging_profile_id")
                  .agentMessage(RcsAgentMessage.builder()
                      .contentMessage(RcsContentMessage.builder()
                          .text("Hello from Telnyx RCS!")
                          .build())
                      .build())
                  .build();

              RcsMessageSendResponse response = client.messages().sendRcs(params);
              System.out.println(response);
          }
      }
      ```

      ```csharp .NET theme={null}
      using Telnyx;

      var client = new TelnyxClient(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

      var response = await client.Messages.SendRcsAsync(new RcsMessageSendParams
      {
          AgentId = "your_rcs_agent_id",
          To = "+15559876543",
          MessagingProfileId = "your_messaging_profile_id",
          AgentMessage = new RcsAgentMessage
          {
              ContentMessage = new RcsContentMessage
              {
                  Text = "Hello from Telnyx RCS!"
              }
          }
      });

      Console.WriteLine(response);
      ```

      ```php
      <?php
      require 'vendor/autoload.php';

      \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

      $response = \Telnyx\Message::createRcs([
          'agent_id' => 'your_rcs_agent_id',
          'to' => '+15559876543',
          'messaging_profile_id' => 'your_messaging_profile_id',
          'agent_message' => [
              'content_message' => [
                  'text' => 'Hello from Telnyx RCS!'
              ]
          ]
      ]);

      print_r($response);
      ```

### Rich Card

    Send a rich card with an image and action button:

      ```bash
      curl -X POST https://api.telnyx.com/v2/messages/rcs \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
          "agent_id": "your_rcs_agent_id",
          "to": "+15559876543",
          "messaging_profile_id": "your_messaging_profile_id",
          "agent_message": {
            "content_message": {
              "rich_card": {
                "standalone_card": {
                  "card_orientation": "VERTICAL",
                  "thumbnail_image_alignment": "LEFT",
                  "card_content": {
                    "title": "Welcome to Telnyx",
                    "description": "Experience rich messaging with RCS",
                    "media": {
                      "height": "MEDIUM",
                      "content_info": {
                        "file_url": "https://example.com/image.jpg"
                      }
                    },
                    "suggestions": [
                      {
                        "action": {
                          "text": "Learn More",
                          "postback_data": "learn_more_clicked",
                          "open_url_action": {
                            "url": "https://telnyx.com"
                          }
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

      ```javascript
      import Telnyx from 'telnyx';

      const client = new Telnyx({
        apiKey: process.env['TELNYX_API_KEY'],
      });

      const response = await client.messages.rcs.send({
        agent_id: 'your_rcs_agent_id',
        to: '+15559876543',
        messaging_profile_id: 'your_messaging_profile_id',
        agent_message: {
          content_message: {
            rich_card: {
              standalone_card: {
                card_orientation: 'VERTICAL',
                thumbnail_image_alignment: 'LEFT',
                card_content: {
                  title: 'Welcome to Telnyx',
                  description: 'Experience rich messaging with RCS',
                  media: {
                    height: 'MEDIUM',
                    content_info: {
                      file_url: 'https://example.com/image.jpg'
                    }
                  },
                  suggestions: [
                    {
                      action: {
                        text: 'Learn More',
                        postback_data: 'learn_more_clicked',
                        open_url_action: {
                          url: 'https://telnyx.com'
                        }
                      }
                    }
                  ]
                }
              }
            }
          }
        }
      });

      console.log(response.data);
      ```

      ```python
      import os
      from telnyx import Telnyx

      client = Telnyx(
          api_key=os.environ.get("TELNYX_API_KEY"),
      )

      response = client.messages.rcs.send(
          agent_id="your_rcs_agent_id",
          to="+15559876543",
          messaging_profile_id="your_messaging_profile_id",
          agent_message={
              "content_message": {
                  "rich_card": {
                      "standalone_card": {
                          "card_orientation": "VERTICAL",
                          "thumbnail_image_alignment": "LEFT",
                          "card_content": {
                              "title": "Welcome to Telnyx",
                              "description": "Experience rich messaging with RCS",
                              "media": {
                                  "height": "MEDIUM",
                                  "content_info": {
                                      "file_url": "https://example.com/image.jpg"
                                  }
                              },
                              "suggestions": [
                                  {
                                      "action": {
                                          "text": "Learn More",
                                          "postback_data": "learn_more_clicked",
                                          "open_url_action": {
                                              "url": "https://telnyx.com"
                                          }
                                      }
                                  }
                              ]
                          }
                      }
                  }
              }
          }
      )

      print(response.data)
      ```

    <Callout type="tip">
      Media URLs must be publicly accessible. Supported formats include JPEG, PNG, and GIF for images.

### Suggested Replies

    Add suggested reply buttons for quick customer responses:

      ```bash
      curl -X POST https://api.telnyx.com/v2/messages/rcs \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
          "agent_id": "your_rcs_agent_id",
          "to": "+15559876543",
          "messaging_profile_id": "your_messaging_profile_id",
          "agent_message": {
            "content_message": {
              "text": "How would you rate your experience?",
              "suggestions": [
                {
                  "reply": {
                    "text": "Great!",
                    "postback_data": "rating_great"
                  }
                },
                {
                  "reply": {
                    "text": "Good",
                    "postback_data": "rating_good"
                  }
                },
                {
                  "reply": {
                    "text": "Could be better",
                    "postback_data": "rating_poor"
                  }
                }
              ]
            }
          }
        }'
      ```

      ```javascript
      import Telnyx from 'telnyx';

      const client = new Telnyx({
        apiKey: process.env['TELNYX_API_KEY'],
      });

      const response = await client.messages.rcs.send({
        agent_id: 'your_rcs_agent_id',
        to: '+15559876543',
        messaging_profile_id: 'your_messaging_profile_id',
        agent_message: {
          content_message: {
            text: 'How would you rate your experience?',
            suggestions: [
              {
                reply: {
                  text: 'Great!',
                  postback_data: 'rating_great'
                }
              },
              {
                reply: {
                  text: 'Good',
                  postback_data: 'rating_good'
                }
              },
              {
                reply: {
                  text: 'Could be better',
                  postback_data: 'rating_poor'
                }
              }
            ]
          }
        }
      });

      console.log(response.data);
      ```

      ```python
      import os
      from telnyx import Telnyx

      client = Telnyx(
          api_key=os.environ.get("TELNYX_API_KEY"),
      )

      response = client.messages.rcs.send(
          agent_id="your_rcs_agent_id",
          to="+15559876543",
          messaging_profile_id="your_messaging_profile_id",
          agent_message={
              "content_message": {
                  "text": "How would you rate your experience?",
                  "suggestions": [
                      {
                          "reply": {
                              "text": "Great!",
                              "postback_data": "rating_great"
                          }
                      },
                      {
                          "reply": {
                              "text": "Good",
                              "postback_data": "rating_good"
                          }
                      },
                      {
                          "reply": {
                              "text": "Could be better",
                              "postback_data": "rating_poor"
                          }
                      }
                  ]
              }
          }
      )

      print(response.data)
      ```

### Response

A successful response looks like this:

```json theme={null}
{
  "data": {
    "record_type": "message",
    "direction": "outbound",
    "id": "40319c33-f083-4d2a-a433-a91983b41be5",
    "type": "RCS",
    "messaging_profile_id": "400199c4-6145-43d2-a471-4c459220fcae",
    "from": {
      "agent_id": "your_rcs_agent_id",
      "carrier": "Telnyx",
      "agent_name": "Your Brand"
    },
    "to": [
      {
        "phone_number": "+15559876543",
        "status": "queued",
        "carrier": "T-MOBILE USA, INC.",
        "line_type": "Wireless"
      }
    ],
    "encoding": "utf-8",
    "parts": 1,
    "rcs_message_category": "basic_message"
  }
}
```

## 4. Handle incoming messages

Set up a webhook to receive customer replies. See [Receiving RCS Webhooks](../runbooks/receiving-rcs-webhooks.md) for details.

## RCS vs SMS comparison

| Feature              | RCS                             | SMS                         |
| -------------------- | ------------------------------- | --------------------------- |
| Rich media           | ✅ Images, video, files          | ❌ Text only (MMS for media) |
| Interactive buttons  | ✅ Suggested replies & actions   | ❌                           |
| Read receipts        | ✅                               | ❌                           |
| Typing indicators    | ✅                               | ❌                           |
| Branding             | ✅ Logo, colors, verified sender | ❌                           |
| Character limit      | None                            | 160 (GSM-7)                 |
| Carrier registration | Required                        | 10DLC/Toll-free required    |

## Next steps

  - [RCS with AI Assistant](../runbooks/rcs-with-ai-assistant.md) — Add AI-powered responses to your RCS agent

  - [RCS Webhooks](../runbooks/receiving-rcs-webhooks.md) — Handle incoming RCS messages

  - [RCS Capabilities](../runbooks/rcs-capabilities-deeplinks.md) — Check if a number supports RCS

  - [API Reference](https://developers.telnyx.com/api-reference/rcs-messaging/send-an-rcs-message) — Explore all RCS parameters


## Related Pages

- [Getting Started with 10DLC](../tutorial/getting-started-with-10dlc.md)
- [Getting Started with Video](../runbooks/getting-started-with-video.md)
