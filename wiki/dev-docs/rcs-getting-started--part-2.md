---
title: RCS Getting Started
summary: RCS (Rich Communication Services) is a messaging protocol that delivers app-like
  experiences in the native messaging app without requiring a download. This guide
  covers the Telnyx RCS approval process, how to create a messaging profile, send
  rich cards and suggested replies, and handle incoming RCS messages via webhooks.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index
- url: https://developers.telnyx.com/docs/messaging/messages/receive-message
updated_at: 2026-08-05T13:57:03Z
---

# RCS Getting Started

*Part 2 of 4 — see also: [Part 1](rcs-getting-started--part-1.md), [Part 3](rcs-getting-started--part-3.md), [Part 4](rcs-getting-started--part-4.md)*

RCS (Rich Communication Services) is a messaging protocol that delivers app-like experiences in the native messaging app without requiring a download. This guide covers the Telnyx RCS approval process, how to create a messaging profile, send rich cards and suggested replies, and handle incoming RCS messages via webhooks.

## Send an RCS message

Once your RCS Agent is in testing stage (or fully approved), you can send messages to your beta test numbers or approved destinations.

### Text message

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

```csharp
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

### Rich card

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

Media URLs must be publicly accessible. Supported formats include JPEG, PNG, and GIF for images.

### Suggested replies

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

```json
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
