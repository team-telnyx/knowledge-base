---
title: Receiving Webhooks for Messaging
summary: Telnyx delivers webhooks to notify applications about messaging events in
  real time, including inbound messages, delivery status updates, read receipts, and
  suggestion responses. This page covers webhook event types, payload structures for
  SMS/MMS and RCS, signature verification, retry behavior, and best practices for
  production webhook handling.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-rcs-webhooks/index
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks/index
updated_at: 2026-08-05T14:01:55Z
---

# Receiving Webhooks for Messaging

*Part 5 of 6 — see also: [Part 1](receiving-webhooks-for-messaging--part-1.md), [Part 2](receiving-webhooks-for-messaging--part-2.md), [Part 3](receiving-webhooks-for-messaging--part-3.md), [Part 4](receiving-webhooks-for-messaging--part-4.md), [Part 6](receiving-webhooks-for-messaging--part-6.md)*

Telnyx delivers webhooks to notify applications about messaging events in real time, including inbound messages, delivery status updates, read receipts, and suggestion responses. This page covers webhook event types, payload structures for SMS/MMS and RCS, signature verification, retry behavior, and best practices for production webhook handling.

## Handling webhooks in your application

### Basic webhook handler

**Node**

```javascript
import express from 'express';

const app = express();
app.use(express.json());

app.post('/webhooks', (req, res) => {
  // Respond immediately to avoid timeout
  res.sendStatus(200);

  const { data } = req.body;

  switch (data.event_type) {
    case 'message.received':
      handleInboundMessage(data.payload);
      break;
    case 'message.sent':
      handleMessageSent(data.payload);
      break;
    case 'message.finalized':
      handleDeliveryReceipt(data.payload);
      break;
  }
});

function handleInboundMessage(payload) {
  const from = payload.from.phone_number;
  const text = payload.text;
  console.log(`Inbound from ${from}: ${text}`);

  // Check for MMS media
  if (payload.media?.length > 0) {
    payload.media.forEach(m => console.log(`Media: ${m.url} (${m.content_type})`));
  }
}

function handleMessageSent(payload) {
  console.log(`Message ${payload.id} sent to carrier`);
}

function handleDeliveryReceipt(payload) {
  const status = payload.to[0]?.status;
  console.log(`Message ${payload.id} finalized: ${status}`);

  if (status === 'delivery_failed') {
    console.error('Delivery failed:', payload.errors);
  }
}

app.listen(5000, () => console.log('Webhook server running on port 5000'));
```

**Python**

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhooks', methods=['POST'])
def webhooks():
    data = request.json.get('data', {})
    event_type = data.get('event_type')
    payload = data.get('payload', {})

    if event_type == 'message.received':
        handle_inbound_message(payload)
    elif event_type == 'message.sent':
        handle_message_sent(payload)
    elif event_type == 'message.finalized':
        handle_delivery_receipt(payload)

    return '', 200

def handle_inbound_message(payload):
    from_number = payload['from']['phone_number']
    text = payload.get('text', '')
    print(f"Inbound from {from_number}: {text}")

    for media in payload.get('media', []):
        print(f"Media: {media['url']} ({media['content_type']})")

def handle_message_sent(payload):
    print(f"Message {payload['id']} sent to carrier")

def handle_delivery_receipt(payload):
    status = payload['to'][0]['status']
    print(f"Message {payload['id']} finalized: {status}")

    if status == 'delivery_failed':
        print(f"Delivery failed: {payload.get('errors')}")

if __name__ == '__main__':
    app.run(port=5000)
```

**Ruby**

```ruby
require 'sinatra'
require 'json'

post '/webhooks' do
  body = JSON.parse(request.body.read)
  data = body['data']
  payload = data['payload']

  case data['event_type']
  when 'message.received'
    puts "Inbound from #{payload['from']['phone_number']}: #{payload['text']}"
    payload['media']&.each { |m| puts "Media: #{m['url']}" }
  when 'message.sent'
    puts "Message #{payload['id']} sent to carrier"
  when 'message.finalized'
    status_val = payload['to'][0]['status']
    puts "Message #{payload['id']} finalized: #{status_val}"
    puts "Errors: #{payload['errors']}" if status_val == 'delivery_failed'
  end

  status 200
end
```

**Go**

```go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Webhook struct {
	Data struct {
		EventType string `json:"event_type"`
		Payload   struct {
			ID   string `json:"id"`
			From struct {
				PhoneNumber string `json:"phone_number"`
			} `json:"from"`
			To []struct {
				PhoneNumber string `json:"phone_number"`
				Status      string `json:"status"`
			} `json:"to"`
			Text   string `json:"text"`
			Media  []struct {
				URL         string `json:"url"`
				ContentType string `json:"content_type"`
			} `json:"media"`
			Errors []struct {
				Code   string `json:"code"`
				Title  string `json:"title"`
			} `json:"errors"`
		} `json:"payload"`
	} `json:"data"`
}

func webhookHandler(w http.ResponseWriter, r *http.Request) {
	var wh Webhook
	json.NewDecoder(r.Body).Decode(&wh)

	switch wh.Data.EventType {
	case "message.received":
		fmt.Printf("Inbound from %s: %s\n", wh.Data.Payload.From.PhoneNumber, wh.Data.Payload.Text)
		for _, m := range wh.Data.Payload.Media {
			fmt.Printf("Media: %s (%s)\n", m.URL, m.ContentType)
		}
	case "message.sent":
		fmt.Printf("Message %s sent to carrier\n", wh.Data.Payload.ID)
	case "message.finalized":
		if len(wh.Data.Payload.To) > 0 {
			fmt.Printf("Message %s finalized: %s\n", wh.Data.Payload.ID, wh.Data.Payload.To[0].Status)
		}
	}

	w.WriteHeader(http.StatusOK)
}

func main() {
	http.HandleFunc("/webhooks", webhookHandler)
	fmt.Println("Webhook server running on port 5000")
	http.ListenAndServe(":5000", nil)
}
```

**Java**

```java
package com.example.webhook;

import com.sun.net.httpserver.HttpServer;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import java.io.InputStream;
import java.net.InetSocketAddress;

public class WebhookServer {
    public static void main(String[] args) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(5000), 0);

        server.createContext("/webhooks", exchange -> {
            InputStream is = exchange.getRequestBody();
            String body = new String(is.readAllBytes());
            JsonObject json = JsonParser.parseString(body).getAsJsonObject();
            JsonObject data = json.getAsJsonObject("data");
            String eventType = data.get("event_type").getAsString();
            JsonObject payload = data.getAsJsonObject("payload");

            switch (eventType) {
                case "message.received":
                    String from = payload.getAsJsonObject("from")
                        .get("phone_number").getAsString();
                    String text = payload.get("text").getAsString();
                    System.out.println("Inbound from " + from + ": " + text);
                    break;
                case "message.sent":
                    System.out.println("Message " + payload.get("id").getAsString() + " sent");
                    break;
                case "message.finalized":
                    String status = payload.getAsJsonArray("to").get(0)
                        .getAsJsonObject().get("status").getAsString();
                    System.out.println("Message " + payload.get("id").getAsString()
                        + " finalized: " + status);
                    break;
            }

            exchange.sendResponseHeaders(200, -1);
        });

        server.start();
        System.out.println("Webhook server running on port 5000");
    }
}
```

**.NET**

```csharp
using Microsoft.AspNetCore.Mvc;
using System.Text.Json;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapPost("/webhooks", async (HttpContext context) =>
{
    using var reader = new StreamReader(context.Request.Body);
    var body = await reader.ReadToEndAsync();
    var json = JsonDocument.Parse(body);
    var data = json.RootElement.GetProperty("data");
    var eventType = data.GetProperty("event_type").GetString();
    var payload = data.GetProperty("payload");

    switch (eventType)
    {
        case "message.received":
            var from = payload.GetProperty("from").GetProperty("phone_number").GetString();
            var text = payload.GetProperty("text").GetString();
            Console.WriteLine($"Inbound from {from}: {text}");
            break;
        case "message.sent":
            Console.WriteLine($"Message {payload.GetProperty("id").GetString()} sent");
            break;
        case "message.finalized":
            var status = payload.GetProperty("to")[0].GetProperty("status").GetString();
            Console.WriteLine($"Message {payload.GetProperty("id").GetString()} finalized: {status}");
            break;
    }

    return Results.Ok();
});

app.Run("http://0.0.0.0:5000");
```

**PHP**

```php
$body = json_decode(file_get_contents('php://input'), true);
$data = $body['data'] ?? [];
$eventType = $data['event_type'] ?? '';
$payload = $data['payload'] ?? [];

switch ($eventType) {
    case 'message.received':
        $from = $payload['from']['phone_number'];
        $text = $payload['text'] ?? '';
        echo "Inbound from {$from}: {$text}\n";

        foreach ($payload['media'] ?? [] as $media) {
            echo "Media: {$media['url']} ({$media['content_type']})\n";
        }
        break;

    case 'message.sent':
        echo "Message {$payload['id']} sent to carrier\n";
        break;

    case 'message.finalized':
        $status = $payload['to'][0]['status'] ?? 'unknown';
        echo "Message {$payload['id']} finalized: {$status}\n";

        if ($status === 'delivery_failed') {
            echo "Errors: " . json_encode($payload['errors']) . "\n";
        }
        break;
}

http_response_code(200);
```

### RCS webhook handler

When handling RCS webhooks, route on `message.read` and the nested `body` structure for inbound types (text, file, location, suggestion response):

**Python**

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhooks/rcs", methods=["POST"])
def handle_rcs_webhook():
    event = request.json
    event_type = event["data"]["event_type"]
    payload = event["data"]["payload"]

    if event_type == "message.received":
        handle_inbound(payload)
    elif event_type == "message.sent":
        print(f"Message {payload['id']} sent")
    elif event_type == "message.finalized":
        handle_delivery(payload)
    elif event_type == "message.read":
        handle_read_receipt(payload)

    return jsonify({"status": "ok"}), 200

def handle_inbound(payload):
    body = payload["body"]
    sender = payload["from"]["phone_number"]

    if "text" in body:
        print(f"Text from {sender}: {body['text']}")
    elif "user_file" in body:
        file_info = body["user_file"]["payload"]
        print(f"File from {sender}: {file_info['file_name']} ({file_info['mime_type']})")
    elif "location" in body:
        loc = body["location"]
        print(f"Location from {sender}: {loc['latitude']}, {loc['longitude']}")
    elif "suggestion_response" in body:
        resp = body["suggestion_response"]
        print(f"Suggestion from {sender}: {resp['text']} (postback: {resp['postback_data']})")

def handle_delivery(payload):
    message_id = payload["id"]
    for recipient in payload.get("to", []):
        status = recipient.get("status")
        phone = recipient.get("phone_number")
        print(f"Message {message_id} to {phone}: {status}")

        if status == "delivery_failed":
            # Implement fallback — e.g., send via SMS
            print(f"Delivery failed for {phone}, triggering SMS fallback")

def handle_read_receipt(payload):
    message_id = payload["id"]
    for recipient in payload.get("to", []):
        phone = recipient.get("phone_number")
        print(f"Message {message_id} read by {phone}")
        # Update message status in your database

if __name__ == "__main__":
    app.run(port=5000)
```

**Node**

```javascript
const express = require('express');
const app = express();
app.use(express.json());

app.post('/webhooks/rcs', (req, res) => {
  const event = req.body;
  const eventType = event.data.event_type;
  const payload = event.data.payload;

  switch (eventType) {
    case 'message.received':
      handleInbound(payload);
      break;
    case 'message.sent':
      console.log(`Message ${payload.id} sent`);
      break;
    case 'message.finalized':
      handleDelivery(payload);
      break;
    case 'message.read':
      handleReadReceipt(payload);
      break;
  }

  res.status(200).json({ status: 'ok' });
});

function handleInbound(payload) {
  const body = payload.body;
  const sender = payload.from.phone_number;

  if (body.text) {
    console.log(`Text from ${sender}: ${body.text}`);
  } else if (body.user_file) {
    const file = body.user_file.payload;
    console.log(`File from ${sender}: ${file.file_name} (${file.mime_type})`);
  } else if (body.location) {
    console.log(`Location from ${sender}: ${body.location.latitude}, ${body.location.longitude}`);
  } else if (body.suggestion_response) {
    const resp = body.suggestion_response;
    console.log(`Suggestion from ${sender}: ${resp.text} (postback: ${resp.postback_data})`);
  }
}

function handleDelivery(payload) {
  const messageId = payload.id;
  for (const recipient of payload.to || []) {
    console.log(`Message ${messageId} to ${recipient.phone_number}: ${recipient.status}`);

    if (recipient.status === 'delivery_failed') {
      console.log(`Delivery failed for ${recipient.phone_number}, triggering SMS fallback`);
    }
  }
}

function handleReadReceipt(payload) {
  const messageId = payload.id;
  for (const recipient of payload.to || []) {
    console.log(`Message ${messageId} read by ${recipient.phone_number}`);
    // Update message status in your database
  }
}

app.listen(5000, () => console.log('RCS webhook server running on port 5000'));
```

### Building a unified SMS + RCS webhook handler

If your application handles both SMS/MMS and RCS, normalize the different payload structures into a common format:

**Python**

```python
def normalize_message(event):
    """Normalize SMS/MMS and RCS webhook payloads into a common format."""
    payload = event["data"]["payload"]
    msg_type = payload.get("type", "SMS")

    if msg_type == "RCS":
        # RCS: body is nested object
        body = payload.get("body", {})
        text = body.get("text", "")
        media = []
        if "user_file" in body:
            file_info = body["user_file"]["payload"]
            media.append({
                "url": file_info["file_uri"],
                "content_type": file_info["mime_type"],
                "size": file_info.get("file_size_bytes"),
            })
        sender = payload.get("from", {}).get("phone_number", "")
    else:
        # SMS/MMS: body is flat
        text = payload.get("text", "")
        media = [
            {"url": m["url"], "content_type": m["content_type"]}
            for m in payload.get("media", [])
        ]
        sender = payload.get("from", {}).get("phone_number", "")

    return {
        "id": payload["id"],
        "type": msg_type,
        "sender": sender,
        "text": text,
        "media": media,
        "direction": payload.get("direction"),
    }
```

**Node**

```javascript
function normalizeMessage(event) {
  const payload = event.data.payload;
  const msgType = payload.type || 'SMS';

  if (msgType === 'RCS') {
    const body = payload.body || {};
    const media = [];
    if (body.user_file) {
      const file = body.user_file.payload;
      media.push({
        url: file.file_uri,
        contentType: file.mime_type,
        size: file.file_size_bytes,
      });
    }
    return {
      id: payload.id,
      type: msgType,
      sender: payload.from?.phone_number || '',
      text: body.text || '',
      media,
      direction: payload.direction,
    };
  }

  // SMS/MMS
  return {
    id: payload.id,
    type: msgType,
    sender: payload.from?.phone_number || '',
    text: payload.text || '',
    media: (payload.media || []).map(m => ({
      url: m.url,
      contentType: m.content_type,
    })),
    direction: payload.direction,
  };
}
```
