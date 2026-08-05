---
title: Send and Receive Messages with the Telnyx Messaging API
summary: Walks through sending your first SMS and MMS with the Telnyx Messaging API,
  including setup, code samples in multiple languages, error handling, rate limiting,
  webhook-based delivery tracking, and inbound MMS processing.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/send-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-receive-mms/index
updated_at: 2026-08-05T13:58:28Z
---

# Send and Receive Messages with the Telnyx Messaging API

*Part 5 of 6 — see also: [Part 1](send-and-receive-messages-with-the-telnyx-messaging-api--part-1.md), [Part 2](send-and-receive-messages-with-the-telnyx-messaging-api--part-2.md), [Part 3](send-and-receive-messages-with-the-telnyx-messaging-api--part-3.md), [Part 4](send-and-receive-messages-with-the-telnyx-messaging-api--part-4.md), [Part 6](send-and-receive-messages-with-the-telnyx-messaging-api--part-6.md)*

Walks through sending your first SMS and MMS with the Telnyx Messaging API, including setup, code samples in multiple languages, error handling, rate limiting, webhook-based delivery tracking, and inbound MMS processing.

## Webhooks and Delivery Tracking

After sending a message, Telnyx delivers real-time status updates via webhooks. Configure a webhook URL on your [Messaging Profile](https://portal.telnyx.com/#/app/messaging) to receive these events automatically.

### Message Lifecycle Events

Messages progress through these statuses:

| Event | Status | Description |
| --- | --- | --- |
| `message.sent` | `sent` | Message accepted and sent to the carrier |
| `message.finalized` | `delivered` | Carrier confirmed delivery to the handset |
| `message.finalized` | `delivery_failed` | Carrier could not deliver the message |
| `message.finalized` | `delivery_unconfirmed` | No delivery confirmation received from the carrier |

Not all carriers return delivery receipts. Some messages may remain in `sent` status without a finalized event. US carriers generally support delivery receipts for SMS; international coverage varies.

### Webhook Payload Example

```
{
  "data": {
    "event_type": "message.finalized",
    "id": "e6e3e550-4e3f-4b3a-9e10-1c2d3e4f5a6b",
    "occurred_at": "2026-03-05T18:30:00.000+00:00",
    "payload": {
      "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
      "record_type": "message",
      "direction": "outbound",
      "type": "SMS",
      "from": { "phone_number": "+15551234567" },
      "to": [
        {
          "phone_number": "+15559876543",
          "status": "delivered"
        }
      ],
      "text": "Hello, world!",
      "parts": 1,
      "cost": { "amount": "0.0051", "currency": "USD" },
      "errors": [],
      "completed_at": "2026-03-05T18:30:00.000+00:00"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

### Processing Webhooks

Set up an endpoint to receive webhook `POST` requests and return a `200` response. Telnyx retries failed deliveries with exponential backoff.

#### Node

```
import express from 'express';

const app = express();
app.use(express.json());

app.post('/webhooks/messaging', (req, res) => {
  const event = req.body.data;

  switch (event.event_type) {
    case 'message.sent':
      console.log(`Message ${event.payload.id} sent`);
      break;
    case 'message.finalized': {
      const status = event.payload.to[0].status;
      if (status === 'delivered') {
        console.log(`Message ${event.payload.id} delivered`);
      } else if (status === 'delivery_failed') {
        console.error(`Message ${event.payload.id} failed:`, event.payload.errors);
      }
      break;
    }
  }

  res.sendStatus(200);
});

app.listen(3000, () => console.log('Webhook server listening on port 3000'));
```

#### Python

```
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhooks/messaging", methods=["POST"])
def handle_webhook():
    event = request.json["data"]

    if event["event_type"] == "message.sent":
        print(f"Message {event['payload']['id']} sent")
    elif event["event_type"] == "message.finalized":
        status = event["payload"]["to"][0]["status"]
        if status == "delivered":
            print(f"Message {event['payload']['id']} delivered")
        elif status == "delivery_failed":
            print(f"Message {event['payload']['id']} failed:", event["payload"]["errors"])

    return jsonify(success=True), 200

if __name__ == "__main__":
    app.run(port=3000)
```

#### Ruby

```
require "sinatra"
require "json"

post "/webhooks/messaging" do
  event = JSON.parse(request.body.read)["data"]

  case event["event_type"]
  when "message.sent"
    puts "Message #{event['payload']['id']} sent"
  when "message.finalized"
    status = event["payload"]["to"][0]["status"]
    if status == "delivered"
      puts "Message #{event['payload']['id']} delivered"
    elsif status == "delivery_failed"
      puts "Message #{event['payload']['id']} failed: #{event['payload']['errors']}"
    end
  end

  status 200
  json success: true
end
```

#### Go

```
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type WebhookEvent struct {
	Data struct {
		EventType string `json:"event_type"`
		Payload   struct {
			ID   string `json:"id"`
			To   []struct {
				Status string `json:"status"`
			} `json:"to"`
			Errors []map[string]interface{} `json:"errors"`
		} `json:"payload"`
	} `json:"data"`
}

func handleWebhook(w http.ResponseWriter, r *http.Request) {
	var event WebhookEvent
	if err := json.NewDecoder(r.Body).Decode(&event); err != nil {
		http.Error(w, "Bad request", 400)
		return
	}

	switch event.Data.EventType {
	case "message.sent":
		fmt.Printf("Message %s sent\n", event.Data.Payload.ID)
	case "message.finalized":
		if len(event.Data.Payload.To) > 0 {
			status := event.Data.Payload.To[0].Status
			if status == "delivered" {
				fmt.Printf("Message %s delivered\n", event.Data.Payload.ID)
			} else if status == "delivery_failed" {
				fmt.Printf("Message %s failed: %v\n", event.Data.Payload.ID, event.Data.Payload.Errors)
			}
		}
	}

	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]bool{"success": true})
}

func main() {
	http.HandleFunc("/webhooks/messaging", handleWebhook)
	log.Println("Webhook server listening on port 3000")
	log.Fatal(http.ListenAndServe(":3000", nil))
}
```

#### Java

```
package com.telnyx.example;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class WebhookServer {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(3000), 0);
        server.createContext("/webhooks/messaging", WebhookServer::handleWebhook);
        System.out.println("Webhook server listening on port 3000");
        server.start();
    }

    private static void handleWebhook(HttpExchange exchange) throws IOException {
        JsonNode body = mapper.readTree(exchange.getRequestBody());
        JsonNode data = body.get("data");
        String eventType = data.get("event_type").asText();
        String messageId = data.get("payload").get("id").asText();

        if ("message.sent".equals(eventType)) {
            System.out.printf("Message %s sent%n", messageId);
        } else if ("message.finalized".equals(eventType)) {
            String status = data.get("payload").get("to").get(0).get("status").asText();
            if ("delivered".equals(status)) {
                System.out.printf("Message %s delivered%n", messageId);
            } else if ("delivery_failed".equals(status)) {
                System.out.printf("Message %s failed: %s%n", messageId, data.get("payload").get("errors"));
            }
        }

        String response = "{\"success\":true}";
        exchange.sendResponseHeaders(200, response.length());
        try (OutputStream os = exchange.getResponseBody()) {
            os.write(response.getBytes());
        }
    }
}
```

#### .NET

```
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using System.Text.Json;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapPost("/webhooks/messaging", async (HttpContext context) =>
{
    using var doc = await JsonDocument.ParseAsync(context.Request.Body);
    var data = doc.RootElement.GetProperty("data");
    var eventType = data.GetProperty("event_type").GetString();
    var messageId = data.GetProperty("payload").GetProperty("id").GetString();

    if (eventType == "message.sent")
    {
        Console.WriteLine($"Message {messageId} sent");
    }
    else if (eventType == "message.finalized")
    {
        var status = data.GetProperty("payload").GetProperty("to")[0].GetProperty("status").GetString();
        if (status == "delivered")
            Console.WriteLine($"Message {messageId} delivered");
        else if (status == "delivery_failed")
            Console.WriteLine($"Message {messageId} failed: {data.GetProperty("payload").GetProperty("errors")}");
    }

    return Results.Ok(new { success = true });
});

app.Run("http://localhost:3000");
```

#### PHP

```
<?php
$payload = json_decode(file_get_contents('php://input'), true);
$event = $payload['data'];

switch ($event['event_type']) {
    case 'message.sent':
        error_log("Message {$event['payload']['id']} sent");
        break;
    case 'message.finalized':
        $status = $event['payload']['to'][0]['status'];
        if ($status === 'delivered') {
            error_log("Message {$event['payload']['id']} delivered");
        } elseif ($status === 'delivery_failed') {
            error_log("Message {$event['payload']['id']} failed: " . json_encode($event['payload']['errors']));
        }
        break;
}

http_response_code(200);
echo json_encode(['success' => true]);
```

### Retrieve Message Status via API

You can also check a message's current status by its ID:

```
curl -X GET "https://api.telnyx.com/v2/messages/b0c7e8cb-6227-4c74-9f32-c7f80c30934b" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

```
const message = await client.messages.retrieve('b0c7e8cb-6227-4c74-9f32-c7f80c30934b');
console.log(message.data.to[0].status); // "delivered"
```

```
message = client.messages.retrieve("b0c7e8cb-6227-4c74-9f32-c7f80c30934b")
print(message.data.to[0].status)  # "delivered"
```

### Delivery Failure Error Codes

When a message fails delivery, the `errors` array in the webhook payload contains error codes:

| Code | Description | Action |
| --- | --- | --- |
| `30003` | Unreachable destination | Verify the number is active and can receive SMS |
| `30004` | Message blocked by carrier | Check content compliance and sender registration |
| `30005` | Unknown destination | Number may be disconnected or invalid |
| `30006` | Landline or unreachable | Number cannot receive SMS (landline, VoIP) |
| `30007` | Carrier violation | Message rejected due to content filtering |
| `30008` | Destination capacity exceeded | Retry after a delay |

For a complete error code reference, see the [Messaging Error Codes](/docs/messaging/messages/error-codes) guide.

### Webhook Security

Validate incoming webhooks to ensure they're from Telnyx:

1. **IP allowlisting** — Telnyx sends webhooks from `192.76.120.192/27`
2. **HTTPS endpoints** — Always use HTTPS for your webhook URL
3. **Respond quickly** — Return `200` within 5 seconds to prevent retries

If your endpoint consistently fails to respond, Telnyx will retry with exponential backoff and eventually disable the webhook. Monitor your endpoint health to avoid missing delivery events.
