---
title: Receiving Webhooks for Messaging
summary: Learn how to receive, verify, and handle messaging webhooks from Telnyx.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks/index
    content_hash: 7c66129fbf8b2f454339d42d07f0597ad2280981a72f671aa180aa9ba8fbe0af
updated_at: 2026-04-10T00:00:00Z
---

# Receiving Webhooks for Messaging

Learn how to receive, verify, and handle messaging webhooks from Telnyx. Covers all event types, webhook signature verification, retry behavior, and SDK examples.

Telnyx sends webhooks to notify your application about messaging events in real time — inbound messages, delivery status updates, and errors. This guide covers every event type, payload structure, signature verification, and best practices for production webhook handling.

## Prerequisites

* A [Telnyx account](https://telnyx.com/sign-up) with a phone number assigned to a [messaging profile](send-your-first-message.md)
* A publicly accessible HTTPS endpoint (or [ngrok](../reference/ngrok.md) for local development)
* Your [API key](https://portal.telnyx.com/#/app/api-keys) and [public key](https://portal.telnyx.com/#/app/api-keys) (for signature verification)

## How webhook delivery works

1. **An event occurs**

    A message is received by your number, or a sent message changes status (queued → sent → delivered).

2. **Telnyx sends a POST request**

    An HTTP `POST` with a JSON payload is sent to your configured webhook URL.

3. **Your server responds**

    Return a `2xx` status code within **2 seconds** to acknowledge receipt.

4. **Failover and retries**

    If your server doesn't respond in time, Telnyx retries (up to 3 attempts per URL) and then tries your failover URL if configured.

### Webhook URL hierarchy

Telnyx determines where to send webhooks using this priority order:

1. **Per-message URLs** — `webhook_url` and `webhook_failover_url` in the [send message request body](https://developers.telnyx.com/api-reference/messages/send-a-message)
2. **Messaging profile URLs** — Configured on the [messaging profile](https://developers.telnyx.com/api-reference/profiles/create-a-messaging-profile)
3. **No webhook** — If neither is set, no webhook is delivered (events are still available in [Message Detail Records](message-detail-records.md))

***

## Webhook event types

Telnyx messaging produces the following webhook events:

| Event Type          | Trigger                                                                    | Direction |
| ------------------- | -------------------------------------------------------------------------- | --------- |
| `message.received`  | An inbound SMS/MMS arrives at your number                                  | Inbound   |
| `message.sent`      | An outbound message has been accepted and sent to the carrier              | Outbound  |
| `message.finalized` | An outbound message has reached a terminal state (delivered, failed, etc.) | Outbound  |

***

## Payload structure

All messaging webhooks share this top-level structure:

```json theme={null}
{
  "data": {
    "event_type": "message.received",
    "id": "unique-event-id",
    "occurred_at": "2024-01-15T20:16:07.588+00:00",
    "payload": { ... },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

| Field               | Description                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| `data.event_type`   | The event type (`message.received`, `message.sent`, `message.finalized`) |
| `data.id`           | Unique identifier for this webhook event                                 |
| `data.occurred_at`  | ISO 8601 timestamp of when the event occurred                            |
| `data.payload`      | Message details (see examples below)                                     |
| `data.record_type`  | Always `"event"`                                                         |
| `meta.attempt`      | Delivery attempt number (starts at 1)                                    |
| `meta.delivered_to` | The URL this webhook was delivered to                                    |

***

## Event examples

### Inbound message (`message.received`)

Triggered when your Telnyx number receives an SMS or MMS:

```json theme={null}
{
  "data": {
    "event_type": "message.received",
    "id": "b301ed3f-1490-491f-995f-6e64e69674d4",
    "occurred_at": "2024-01-15T20:16:07.588+00:00",
    "payload": {
      "completed_at": null,
      "cost": { "amount": "0.0000", "currency": "USD" },
      "direction": "inbound",
      "encoding": "GSM-7",
      "errors": [],
      "from": {
        "carrier": "T-Mobile USA",
        "line_type": "long_code",
        "phone_number": "+13125550001"
      },
      "id": "84cca175-9755-4859-b67f-4730d7f58aa3",
      "media": [],
      "messaging_profile_id": "740572b6-099c-44a1-89b9-6c92163bc68d",
      "organization_id": "47a530f8-4362-4526-829b-bcee17fd9f7a",
      "parts": 1,
      "received_at": "2024-01-15T20:16:07.503+00:00",
      "record_type": "message",
      "sent_at": null,
      "tags": [],
      "text": "Hello from Telnyx!",
      "to": [
        {
          "carrier": "Telnyx",
          "line_type": "Wireless",
          "phone_number": "+17735550002",
          "status": "webhook_delivered"
        }
      ],
      "type": "SMS",
      "valid_until": null,
      "webhook_failover_url": null,
      "webhook_url": "https://example.com/webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

**MMS inbound payload (with media)**

  MMS messages include a `media` array with URLs, content types, and file sizes:

  ```json theme={null}
  {
    "media": [
      {
        "url": "https://media.telnyx.com/example-image.png",
        "content_type": "image/png",
        "sha256": "ab1c2d3e4f...",
        "size": 102400
      }
    ],
    "type": "MMS"
  }
  ```

  > **Warning:** MMS media links expire after **30 days**. Download and store media files if you need long-term access.

---

### Message sent (`message.sent`)

Triggered when an outbound message has been accepted by the downstream carrier:

```json theme={null}
{
  "data": {
    "event_type": "message.sent",
    "id": "a1b2c3d4-5678-9012-abcd-ef1234567890",
    "occurred_at": "2024-01-15T21:32:13.596+00:00",
    "payload": {
      "completed_at": null,
      "cost": { "amount": "0.0051", "currency": "USD" },
      "direction": "outbound",
      "encoding": "GSM-7",
      "errors": [],
      "from": {
        "carrier": "Telnyx",
        "line_type": "Wireless",
        "phone_number": "+13125550001"
      },
      "id": "ac012cbf-5e09-46af-a69a-7c0e2d90993c",
      "media": [],
      "messaging_profile_id": "83d2343b-553f-4c5f-b8c8-fd27004f94bf",
      "organization_id": "9d76d591-1b7d-405d-8c64-1320ee070245",
      "parts": 1,
      "received_at": "2024-01-15T21:32:13.552+00:00",
      "record_type": "message",
      "sent_at": "2024-01-15T21:32:13.596+00:00",
      "text": "Hello there!",
      "to": [
        {
          "carrier": "T-MOBILE USA, INC.",
          "line_type": "Wireless",
          "phone_number": "+13125550002",
          "status": "sent"
        }
      ],
      "type": "SMS",
      "valid_until": "2024-01-15T22:32:13.552+00:00",
      "webhook_url": "https://example.com/webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

### Delivery receipt (`message.finalized`)

Triggered when a message reaches a terminal delivery state:

```json theme={null}
{
  "data": {
    "event_type": "message.finalized",
    "id": "4ee8c3a6-4995-4309-a3c6-38e3db9ea4be",
    "occurred_at": "2024-01-15T21:32:14.148+00:00",
    "payload": {
      "completed_at": "2024-01-15T21:32:14.148+00:00",
      "cost": {
        "amount": "0.0051",
        "currency": "USD"
      },
      "cost_breakdown": {
        "carrier_fee": { "amount": "0.00305", "currency": "USD" },
        "rate": { "amount": "0.00205", "currency": "USD" }
      },
      "direction": "outbound",
      "encoding": "GSM-7",
      "errors": [],
      "from": {
        "carrier": "Telnyx",
        "line_type": "Wireless",
        "phone_number": "+13125550001",
        "status": "webhook_delivered"
      },
      "id": "ac012cbf-5e09-46af-a69a-7c0e2d90993c",
      "media": [],
      "messaging_profile_id": "83d2343b-553f-4c5f-b8c8-fd27004f94bf",
      "organization_id": "9d76d591-1b7d-405d-8c64-1320ee070245",
      "parts": 1,
      "received_at": "2024-01-15T21:32:13.552+00:00",
      "record_type": "message",
      "sent_at": "2024-01-15T21:32:13.596+00:00",
      "tags": ["tag-a", "tag-b"],
      "text": "Hello there!",
      "to": [
        {
          "carrier": "T-MOBILE USA, INC.",
          "line_type": "Wireless",
          "phone_number": "+13125550002",
          "status": "delivered"
        }
      ],
      "type": "SMS",
      "valid_until": "2024-01-15T22:32:13.552+00:00",
      "webhook_url": "https://example.com/webhooks",
      "tcr_campaign_billable": true,
      "tcr_campaign_id": "CNZO3VL",
      "tcr_campaign_registered": "REGISTERED"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

### Delivery statuses

The `to[].status` field in `message.finalized` events indicates the final delivery outcome:

| Status                 | Description                                                |
| ---------------------- | ---------------------------------------------------------- |
| `queued`               | Message is queued on Telnyx's side                         |
| `sending`              | Message is being sent to an upstream carrier               |
| `sent`                 | Message has been sent to the upstream carrier              |
| `delivered`            | Carrier has confirmed delivery to the recipient            |
| `sending_failed`       | Telnyx failed to send the message to the carrier           |
| `delivery_failed`      | The carrier failed to deliver the message to the recipient |
| `delivery_unconfirmed` | No delivery confirmation was received from the carrier     |

**Common delivery failure error codes**

  When a message fails, the `errors` array in the payload contains details:

  ```json theme={null}
  {
    "errors": [
      {
        "code": "40300",
        "title": "Destination number unreachable",
        "detail": "The destination number is not reachable on the carrier network.",
        "source": { "pointer": "/to/0/phone_number" }
      }
    ]
  }
  ```

  Common error codes:

  | Code    | Meaning                               |
  | ------- | ------------------------------------- |
  | `40001` | Destination number invalid            |
  | `40002` | Destination number not in service     |
  | `40300` | Destination unreachable               |
  | `40008` | Message filtered by carrier           |
  | `40010` | Message blocked (spam/content filter) |
  | `47000` | 10DLC campaign required               |

  For a complete list, see the [Error Codes reference](../reference/api-error-codes.md).

---

***

## Webhook signature verification

Telnyx signs every webhook using **Ed25519 public key cryptography** so you can verify that requests genuinely come from Telnyx. **This is strongly recommended for production deployments.**

Each webhook request includes two headers:

| Header                     | Description                                   |
| -------------------------- | --------------------------------------------- |
| `telnyx-signature-ed25519` | Base64-encoded Ed25519 signature              |
| `telnyx-timestamp`         | Unix timestamp of when the request was signed |

The signature is computed over the string `{timestamp}|{json_payload}`.

### Get your public key

Find your public key in the [Mission Control Portal](https://portal.telnyx.com/#/app/api-keys) under **Keys & Credentials → Public Key**.

### Verification examples

  ```javascript
  import express from 'express';
  import Telnyx from 'telnyx';

  const app = express();
  app.use(express.json());

  const telnyx = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

  app.post('/webhooks', (req, res) => {
    const signature = req.headers['telnyx-signature-ed25519'];
    const timestamp = req.headers['telnyx-timestamp'];
    const payload = JSON.stringify(req.body);

    try {
      const event = telnyx.webhooks.constructEvent(
        payload,
        signature,
        timestamp,
        process.env.TELNYX_PUBLIC_KEY
      );
      console.log('Verified event:', event.data.event_type);
      res.sendStatus(200);
    } catch (err) {
      console.error('Signature verification failed:', err.message);
      res.sendStatus(403);
    }
  });

  app.listen(5000, () => console.log('Server running on port 5000'));
  ```

  ```python
  from flask import Flask, request
  import telnyx

  app = Flask(__name__)
  telnyx.api_key = "YOUR_API_KEY"
  telnyx.public_key = "YOUR_PUBLIC_KEY"

  @app.route('/webhooks', methods=['POST'])
  def webhooks():
      payload = request.data
      signature = request.headers.get('telnyx-signature-ed25519')
      timestamp = request.headers.get('telnyx-timestamp')

      try:
          event = telnyx.Webhook.construct_event(payload, signature, timestamp)
          print(f"Verified event: {event['data']['event_type']}")
          return '', 200
      except telnyx.error.SignatureVerificationError:
          return 'Invalid signature', 403
  ```

  ```ruby
  require 'sinatra'
  require 'telnyx'
  require 'json'

  Telnyx.api_key = ENV['TELNYX_API_KEY']
  Telnyx.public_key = ENV['TELNYX_PUBLIC_KEY']

  post '/webhooks' do
    payload = request.body.read
    signature = request.env['HTTP_TELNYX_SIGNATURE_ED25519']
    timestamp = request.env['HTTP_TELNYX_TIMESTAMP']

    begin
      event = Telnyx::Webhook.construct_event(payload, signature, timestamp)
      puts "Verified event: #{event['data']['event_type']}"
      status 200
    rescue Telnyx::SignatureVerificationError
      status 403
      body 'Invalid signature'
    end
  end
  ```

  ```go
  package main

  import (
  	"crypto/ed25519"
  	"encoding/base64"
  	"fmt"
  	"io"
  	"net/http"
  	"os"
  )

  func verifySignature(payload, signature, timestamp string, publicKey ed25519.PublicKey) bool {
  	signedPayload := timestamp + "|" + payload
  	sigBytes, err := base64.StdEncoding.DecodeString(signature)
  	if err != nil {
  		return false
  	}
  	return ed25519.Verify(publicKey, []byte(signedPayload), sigBytes)
  }

  func webhookHandler(w http.ResponseWriter, r *http.Request) {
  	body, _ := io.ReadAll(r.Body)
  	signature := r.Header.Get("telnyx-signature-ed25519")
  	timestamp := r.Header.Get("telnyx-timestamp")

  	pubKeyBytes, _ := base64.StdEncoding.DecodeString(os.Getenv("TELNYX_PUBLIC_KEY"))
  	publicKey := ed25519.PublicKey(pubKeyBytes)

  	if !verifySignature(string(body), signature, timestamp, publicKey) {
  		http.Error(w, "Invalid signature", http.StatusForbidden)
  		return
  	}

  	fmt.Println("Webhook verified and received")
  	w.WriteHeader(http.StatusOK)
  }

  func main() {
  	http.HandleFunc("/webhooks", webhookHandler)
  	fmt.Println("Server running on port 5000")
  	http.ListenAndServe(":5000", nil)
  }
  ```

  ```java
  package com.example.webhook;

  import com.sun.net.httpserver.HttpServer;
  import java.io.InputStream;
  import java.net.InetSocketAddress;
  import java.security.*;
  import java.security.spec.X509EncodedKeySpec;
  import java.util.Base64;

  public class WebhookServer {
      private static boolean verifySignature(String payload, String signature,
                                             String timestamp, String publicKeyBase64) throws Exception {
          byte[] pubKeyBytes = Base64.getDecoder().decode(publicKeyBase64);
          KeyFactory keyFactory = KeyFactory.getInstance("Ed25519");
          PublicKey publicKey = keyFactory.generatePublic(new X509EncodedKeySpec(pubKeyBytes));

          Signature sig = Signature.getInstance("Ed25519");
          sig.initVerify(publicKey);
          sig.update((timestamp + "|" + payload).getBytes());
          return sig.verify(Base64.getDecoder().decode(signature));
      }

      public static void main(String[] args) throws Exception {
          String publicKeyBase64 = System.getenv("TELNYX_PUBLIC_KEY");

          HttpServer server = HttpServer.create(new InetSocketAddress(5000), 0);
          server.createContext("/webhooks", exchange -> {
              InputStream is = exchange.getRequestBody();
              String body = new String(is.readAllBytes());
              String signature = exchange.getRequestHeaders().getFirst("telnyx-signature-ed25519");
              String timestamp = exchange.getRequestHeaders().getFirst("telnyx-timestamp");

              try {
                  if (verifySignature(body, signature, timestamp, publicKeyBase64)) {
                      System.out.println("Webhook verified");
                      exchange.sendResponseHeaders(200, -1);
                  } else {
                      exchange.sendResponseHeaders(403, -1);
                  }
              } catch (Exception e) {
                  exchange.sendResponseHeaders(500, -1);
              }
          });

          server.start();
          System.out.println("Server running on port 5000");
      }
  }
  ```

  ```csharp .NET theme={null}
  // Requires: dotnet add package NSec.Cryptography
  using System.Text;
  using NSec.Cryptography;

  var builder = WebApplication.CreateBuilder(args);
  var app = builder.Build();

  app.MapPost("/webhooks", async (HttpContext context) =>
  {
      using var reader = new StreamReader(context.Request.Body);
      var body = await reader.ReadToEndAsync();
      var signature = context.Request.Headers["telnyx-signature-ed25519"].ToString();
      var timestamp = context.Request.Headers["telnyx-timestamp"].ToString();

      var publicKeyBytes = Convert.FromBase64String(
          Environment.GetEnvironmentVariable("TELNYX_PUBLIC_KEY")!);
      var signedPayload = Encoding.UTF8.GetBytes($"{timestamp}|{body}");
      var signatureBytes = Convert.FromBase64String(signature);

      var algorithm = SignatureAlgorithm.Ed25519;
      var publicKey = PublicKey.Import(algorithm, publicKeyBytes, KeyBlobFormat.RawPublicKey);

      if (algorithm.Verify(publicKey, signedPayload, signatureBytes))
      {
          Console.WriteLine("Webhook verified");
          return Results.Ok();
      }

      return Results.StatusCode(403);
  });

  app.Run("http://0.0.0.0:5000");
  ```

  ```php
  <?php
  $payload = file_get_contents('php://input');
  $signature = $_SERVER['HTTP_TELNYX_SIGNATURE_ED25519'] ?? '';
  $timestamp = $_SERVER['HTTP_TELNYX_TIMESTAMP'] ?? '';
  $publicKey = getenv('TELNYX_PUBLIC_KEY');

  $signedPayload = $timestamp . '|' . $payload;
  $sigBytes = base64_decode($signature);
  $pubKeyBytes = base64_decode($publicKey);

  $valid = sodium_crypto_sign_verify_detached($sigBytes, $signedPayload, $pubKeyBytes);

  if (!$valid) {
      http_response_code(403);
      echo 'Invalid signature';
      exit;
  }

  http_response_code(200);
  echo 'Webhook verified';
  ```

<Callout type="warning">
  **Timestamp tolerance:** To prevent replay attacks, reject webhooks where `telnyx-timestamp` is more than 5 minutes old.

***

## Handling webhooks in your application

### Basic webhook handler

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

  ```csharp .NET theme={null}
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

  ```php
  <?php
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

***

## Retry behavior and error handling

### Retry policy

| Behavior             | Detail                                                             |
| -------------------- | ------------------------------------------------------------------ |
| **Timeout**          | Your endpoint must respond within **2 seconds** (API v2)           |
| **Retries**          | Up to **3 attempts** per URL with exponential backoff              |
| **Failover**         | If all retries fail, Telnyx tries the failover URL (if configured) |
| **Total attempts**   | Up to 6 total (3 primary + 3 failover)                             |
| **Success response** | Any `2xx` status code                                              |
| **Failure response** | Any non-`2xx` response, including `3xx` redirects                  |

### Best practices for reliability

1. **Respond immediately** — Return `200` before processing the event. Offload heavy logic to a background queue.
2. **Handle duplicates** — Webhooks may be delivered more than once. Use the `data.id` field as an idempotency key.
3. **Handle out-of-order delivery** — Events may arrive in a different order than they occurred. Use `data.occurred_at` timestamps to sequence events.
4. **Use HTTPS** — Always use TLS-encrypted endpoints in production.
5. **Verify signatures** — Validate `telnyx-signature-ed25519` headers to prevent spoofing.

***

## Webhook IP allowlist

If your server uses a firewall or ACL, allowlist the following Telnyx subnet:

```
192.76.120.192/27
```

***

## Troubleshooting

**Webhooks not arriving**

  1. **Check your messaging profile** — Confirm a webhook URL is configured in the [Portal](https://portal.telnyx.com/#/app/messaging) or via the API.
  2. **Test your endpoint** — Send a test POST request with `curl` to ensure your server is accessible:
     ```bash theme={null}
     curl -X POST https://your-endpoint.com/webhooks \
       -H "Content-Type: application/json" \
       -d '{"test": true}'
     ```
  3. **Check ngrok** — If using ngrok, verify the tunnel is running and the URL matches your profile configuration.
  4. **Check firewall** — Ensure `192.76.120.192/27` is allowlisted.
  5. **Check Message Detail Records** — Events are logged regardless of webhook delivery. Check [MDRs](message-detail-records.md) in the portal.

---

**Getting duplicate webhooks**

  This is expected behavior. Telnyx may deliver the same webhook more than once, especially during retries. Track processed event IDs (`data.id`) and skip duplicates:

  ```javascript theme={null}
  const processedEvents = new Set();

  app.post('/webhooks', (req, res) => {
    const eventId = req.body.data.id;
    if (processedEvents.has(eventId)) {
      return res.sendStatus(200); // Already processed
    }
    processedEvents.add(eventId);
    // Process event...
    res.sendStatus(200);
  });
  ```

  For production, use a persistent store (Redis, database) instead of in-memory sets.

---

**Webhooks arriving out of order**

  Telnyx does not guarantee delivery order. For example, `message.finalized` may arrive before `message.sent`. Use the `data.occurred_at` timestamp to determine event sequence, and design your logic to handle any arrival order.

---

**Signature verification failing**

  1. **Ensure you're reading the raw body** — Parse the signature against the raw request body, not a re-serialized JSON object.
  2. **Check your public key** — Verify you're using the correct public key from the [Portal](https://portal.telnyx.com/#/app/api-keys).
  3. **Check timestamp tolerance** — If you're rejecting stale timestamps, ensure your server clock is synchronized (NTP).

---

**Webhook timeouts (retries happening unexpectedly)**

  Your endpoint must respond within **2 seconds**. If your processing takes longer:

  * Return `200` immediately
  * Process the event asynchronously (use a message queue like Redis, RabbitMQ, or SQS)

---

***

## Next steps

  - [Receive Messages Tutorial](receive-sms-and-mms-messages.md) — Step-by-step guide to building a webhook server

  - [Send Your First Message](send-your-first-message.md) — Send SMS and MMS with the Messaging API

  - [Webhook Fundamentals](../reference/webhook-fundamentals-complete-guide-to-telnyx-webhooks.md) — Platform-wide webhook concepts, signing, and retry behavior

  - [Message Detail Records](message-detail-records.md) — Query historical message data and delivery statuses


## Related Pages

- [Receiving Webhooks for Telnyx Verify](../runbooks/receiving-webhooks-for-telnyx-verify.md)
- [Receiving Webhooks for Programmable Fax](../runbooks/receiving-webhooks-for-programmable-fax.md)
- [Receiving Webhooks for Programmable Voice](../runbooks/receiving-webhooks-for-programmable-voice.md)
- [Receiving RCS Webhooks](../runbooks/receiving-rcs-webhooks.md)
