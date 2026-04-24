---
title: Receive SMS and MMS Messages
summary: Receive inbound SMS and MMS messages via webhooks using the Telnyx Messaging API — with auto-reply, MMS media handling, and webhook signature verification.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/receive-message/index
    content_hash: c4387189bdb87b254b5bd2e2359c19ae5a618f7ae1d3cce1a71ea0ee8cfda6d7
updated_at: 2026-04-10T00:00:00Z
---

# Receive SMS and MMS Messages

Receive inbound SMS and MMS messages via webhooks using the Telnyx Messaging API — with auto-reply, MMS media handling, and webhook signature verification.

Receive inbound SMS and MMS messages via webhooks. When someone texts your Telnyx number, Telnyx sends an HTTP `POST` request with the message details to your configured webhook URL.

## Prerequisites

* A Telnyx phone number assigned to a [messaging profile](send-your-first-message.md)
* A webhook URL configured on your messaging profile
* [ngrok](../reference/ngrok.md) or similar tool for local development

> **Note:** Already have a webhook server? Skip to [Configure your webhook URL](#3-configure-your-webhook-url) to point it at your messaging profile.

## Quick Start

1. **Create a webhook server**

    Build a web server that accepts `POST` requests from Telnyx:

      ```javascript
      import express from 'express';

      const app = express();
      app.use(express.json());

      app.post('/webhooks', (req, res) => {
        const { data } = req.body;

        if (data.event_type === 'message.received') {
          const { payload } = data;
          console.log(`From: ${payload.from.phone_number}`);
          console.log(`Text: ${payload.text}`);
          console.log(`Type: ${payload.type}`); // SMS or MMS

          if (payload.media?.length > 0) {
            console.log(`Media attachments: ${payload.media.length}`);
            payload.media.forEach(m => console.log(`  ${m.content_type}: ${m.url}`));
          }
        }

        res.sendStatus(200);
      });

      app.listen(5000, () => console.log('Webhook server running on port 5000'));
      ```

      ```python
      from flask import Flask, request

      app = Flask(__name__)

      @app.route('/webhooks', methods=['POST'])
      def webhooks():
          data = request.json.get('data', {})

          if data.get('event_type') == 'message.received':
              payload = data.get('payload', {})
              print(f"From: {payload['from']['phone_number']}")
              print(f"Text: {payload.get('text')}")
              print(f"Type: {payload.get('type')}")  # SMS or MMS

              for media in payload.get('media', []):
                  print(f"  {media['content_type']}: {media['url']}")

          return '', 200

      if __name__ == "__main__":
          app.run(port=5000)
      ```

      ```ruby
      require 'sinatra'
      require 'json'

      set :port, 5000

      post '/webhooks' do
        body = JSON.parse(request.body.read)
        data = body['data']

        if data['event_type'] == 'message.received'
          payload = data['payload']
          puts "From: #{payload['from']['phone_number']}"
          puts "Text: #{payload['text']}"
          puts "Type: #{payload['type']}"

          (payload['media'] || []).each do |media|
            puts "  #{media['content_type']}: #{media['url']}"
          end
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

      type WebhookEvent struct {
      	Data struct {
      		EventType string `json:"event_type"`
      		Payload   struct {
      			From struct {
      				PhoneNumber string `json:"phone_number"`
      			} `json:"from"`
      			Text  string `json:"text"`
      			Type  string `json:"type"`
      			Media []struct {
      				URL         string `json:"url"`
      				ContentType string `json:"content_type"`
      			} `json:"media"`
      		} `json:"payload"`
      	} `json:"data"`
      }

      func webhookHandler(w http.ResponseWriter, r *http.Request) {
      	var event WebhookEvent
      	json.NewDecoder(r.Body).Decode(&event)

      	if event.Data.EventType == "message.received" {
      		p := event.Data.Payload
      		fmt.Printf("From: %s\n", p.From.PhoneNumber)
      		fmt.Printf("Text: %s\n", p.Text)
      		fmt.Printf("Type: %s\n", p.Type)

      		for _, m := range p.Media {
      			fmt.Printf("  %s: %s\n", m.ContentType, m.URL)
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
      import com.google.gson.JsonArray;
      import com.google.gson.JsonObject;
      import com.google.gson.JsonParser;
      import java.io.InputStream;
      import java.net.InetSocketAddress;

      public class WebhookServer {
          public static void main(String[] args) throws Exception {
              HttpServer server = HttpServer.create(new InetSocketAddress(5000), 0);

              server.createContext("/webhooks", exchange -> {
                  if ("POST".equals(exchange.getRequestMethod())) {
                      InputStream is = exchange.getRequestBody();
                      String body = new String(is.readAllBytes());
                      JsonObject json = JsonParser.parseString(body).getAsJsonObject();
                      JsonObject data = json.getAsJsonObject("data");

                      if ("message.received".equals(data.get("event_type").getAsString())) {
                          JsonObject payload = data.getAsJsonObject("payload");
                          String from = payload.getAsJsonObject("from").get("phone_number").getAsString();
                          System.out.println("From: " + from);
                          System.out.println("Text: " + payload.get("text").getAsString());
                          System.out.println("Type: " + payload.get("type").getAsString());

                          JsonArray media = payload.getAsJsonArray("media");
                          if (media != null) {
                              media.forEach(m -> {
                                  JsonObject obj = m.getAsJsonObject();
                                  System.out.println("  " + obj.get("content_type").getAsString()
                                      + ": " + obj.get("url").getAsString());
                              });
                          }
                      }

                      exchange.sendResponseHeaders(200, -1);
                  }
              });

              server.start();
              System.out.println("Webhook server running on port 5000");
          }
      }
      ```

      ```csharp .NET theme={null}
      using System.Text.Json;

      var builder = WebApplication.CreateBuilder(args);
      var app = builder.Build();

      app.MapPost("/webhooks", async (HttpRequest request) =>
      {
          using var doc = await JsonDocument.ParseAsync(request.Body);
          var data = doc.RootElement.GetProperty("data");

          if (data.GetProperty("event_type").GetString() == "message.received")
          {
              var payload = data.GetProperty("payload");
              Console.WriteLine($"From: {payload.GetProperty("from").GetProperty("phone_number").GetString()}");
              Console.WriteLine($"Text: {payload.GetProperty("text").GetString()}");
              Console.WriteLine($"Type: {payload.GetProperty("type").GetString()}");

              if (payload.TryGetProperty("media", out var media))
              {
                  foreach (var m in media.EnumerateArray())
                  {
                      Console.WriteLine($"  {m.GetProperty("content_type").GetString()}: {m.GetProperty("url").GetString()}");
                  }
              }
          }

          return Results.Ok();
      });

      app.Run("http://localhost:5000");
      ```

      ```php
      <?php

      $payload = json_decode(file_get_contents('php://input'), true);
      $data = $payload['data'] ?? [];

      if (($data['event_type'] ?? '') === 'message.received') {
          $msg = $data['payload'];
          echo "From: " . $msg['from']['phone_number'] . "\n";
          echo "Text: " . ($msg['text'] ?? '') . "\n";
          echo "Type: " . ($msg['type'] ?? '') . "\n";

          foreach ($msg['media'] ?? [] as $media) {
              echo "  {$media['content_type']}: {$media['url']}\n";
          }
      }

      http_response_code(200);
      ```

2. **Expose your local server**

    Use ngrok to create a public URL that forwards to your local server:

    ```bash theme={null}
    ngrok http 5000
    ```

    Copy the forwarding URL (e.g., `https://abc123.ngrok.io`).

3. **Configure your webhook URL**

    Set the webhook URL on your messaging profile via the [Portal](https://portal.telnyx.com/#/app/messaging) or API:

    ```bash theme={null}
    curl -X PATCH "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -d '{
        "webhook_url": "https://abc123.ngrok.io/webhooks"
      }'
    ```

      Find your messaging profile ID in the [Portal](https://portal.telnyx.com/#/app/messaging) or via the [List Messaging Profiles](https://developers.telnyx.com/api-reference/profiles/list-messaging-profiles) endpoint.

4. **Test it**

    Send a text message from your phone to your Telnyx number. You should see the message details logged in your server console.

    You can also test locally without a phone:

    ```bash theme={null}
    curl -X POST http://localhost:5000/webhooks \
      -H "Content-Type: application/json" \
      -d '{
        "data": {
          "event_type": "message.received",
          "payload": {
            "from": {"phone_number": "+15551234567"},
            "to": [{"phone_number": "+15559876543"}],
            "text": "Hello from test!",
            "type": "SMS",
            "media": []
          }
        }
      }'
    ```

> **Warning:** Your webhook must return a `2xx` response within **2 seconds** (API v2) or 5 seconds (API v1). If delivery fails, Telnyx retries up to 2 times per URL. With a failover URL configured, that's up to 4 total attempts.

***

## Auto-Reply to Incoming Messages

A common pattern is sending an automatic reply when a message arrives. Combine your webhook handler with the [Send Message](send-your-first-message.md) API:

  ```javascript
  import express from 'express';
  import Telnyx from 'telnyx';

  const app = express();
  app.use(express.json());

  const client = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

  app.post('/webhooks', async (req, res) => {
    const { data } = req.body;

    if (data.event_type === 'message.received') {
      const { payload } = data;
      const from = payload.from.phone_number;
      const to = payload.to[0].phone_number;

      // Send auto-reply
      await client.messages.send({
        from: to,   // Reply from the number that received the message
        to: from,   // Reply to the sender
        text: `Thanks for your message! We received: "${payload.text}"`
      });

      console.log(`Auto-reply sent to ${from}`);
    }

    res.sendStatus(200);
  });

  app.listen(5000);
  ```

  ```python
  import os
  from flask import Flask, request
  from telnyx import Telnyx

  app = Flask(__name__)
  client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

  @app.route('/webhooks', methods=['POST'])
  def webhooks():
      data = request.json.get('data', {})

      if data.get('event_type') == 'message.received':
          payload = data.get('payload', {})
          sender = payload['from']['phone_number']
          recipient = payload['to'][0]['phone_number']

          # Send auto-reply
          client.messages.send(
              from_=recipient,
              to=sender,
              text=f'Thanks for your message! We received: "{payload.get("text")}"'
          )

          print(f"Auto-reply sent to {sender}")

      return '', 200

  if __name__ == "__main__":
      app.run(port=5000)
  ```

  ```ruby
  require 'sinatra'
  require 'json'
  require 'telnyx'

  Telnyx.api_key = ENV['TELNYX_API_KEY']

  post '/webhooks' do
    body = JSON.parse(request.body.read)
    data = body['data']

    if data['event_type'] == 'message.received'
      payload = data['payload']
      sender = payload['from']['phone_number']
      recipient = payload['to'][0]['phone_number']

      Telnyx::Message.create(
        from: recipient,
        to: sender,
        text: "Thanks for your message! We received: \"#{payload['text']}\""
      )

      puts "Auto-reply sent to #{sender}"
    end

    status 200
  end
  ```

  ```go
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"net/http"
  	"os"

  	"github.com/team-telnyx/telnyx-go"
  	"github.com/team-telnyx/telnyx-go/option"
  )

  func main() {
  	client := telnyx.NewClient(
  		option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
  	)

  	http.HandleFunc("/webhooks", func(w http.ResponseWriter, r *http.Request) {
  		var event WebhookEvent
  		json.NewDecoder(r.Body).Decode(&event)

  		if event.Data.EventType == "message.received" {
  			p := event.Data.Payload
  			sender := p.From.PhoneNumber
  			recipient := p.To[0].PhoneNumber

  			client.Messages.Send(context.TODO(), telnyx.MessageSendParams{
  				From: recipient,
  				To:   sender,
  				Text: fmt.Sprintf("Thanks for your message! We received: \"%s\"", p.Text),
  			})

  			fmt.Printf("Auto-reply sent to %s\n", sender)
  		}

  		w.WriteHeader(http.StatusOK)
  	})

  	fmt.Println("Server running on port 5000")
  	http.ListenAndServe(":5000", nil)
  }
  ```

> **Warning:** **Avoid reply loops.** If both sides auto-reply, they'll ping each other forever. Guard against this by checking the sender isn't one of your own numbers, or by tracking recently replied conversations.

***

## Webhook Payload Reference

### Inbound SMS

```json theme={null}
{
  "data": {
    "event_type": "message.received",
    "id": "b301ed3f-1490-491f-995f-6e64e69674d4",
    "occurred_at": "2024-01-15T20:16:07.588+00:00",
    "payload": {
      "direction": "inbound",
      "encoding": "GSM-7",
      "from": {
        "carrier": "T-Mobile USA",
        "line_type": "long_code",
        "phone_number": "+13125550001",
        "status": "webhook_delivered"
      },
      "id": "84cca175-9755-4859-b67f-4730d7f58aa3",
      "media": [],
      "messaging_profile_id": "740572b6-099c-44a1-89b9-6c92163bc68d",
      "parts": 1,
      "received_at": "2024-01-15T20:16:07.503+00:00",
      "record_type": "message",
      "text": "Hello from Telnyx!",
      "to": [
        {
          "carrier": "Telnyx",
          "line_type": "Wireless",
          "phone_number": "+17735550002",
          "status": "webhook_delivered"
        }
      ],
      "type": "SMS"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhooks"
  }
}
```

### Inbound MMS

MMS messages include a `media` array with downloadable attachments:

```json theme={null}
{
  "data": {
    "event_type": "message.received",
    "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "occurred_at": "2024-01-15T20:18:30.000+00:00",
    "payload": {
      "direction": "inbound",
      "from": {
        "carrier": "T-Mobile USA",
        "line_type": "long_code",
        "phone_number": "+13125550001"
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "media": [
        {
          "url": "https://media.telnyx.com/example-image.png",
          "content_type": "image/png",
          "sha256": "ab1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b",
          "size": 102400
        }
      ],
      "messaging_profile_id": "740572b6-099c-44a1-89b9-6c92163bc68d",
      "parts": 1,
      "received_at": "2024-01-15T20:18:30.000+00:00",
      "record_type": "message",
      "text": "Check out this photo!",
      "to": [
        {
          "carrier": "Telnyx",
          "line_type": "Wireless",
          "phone_number": "+17735550002"
        }
      ],
      "type": "MMS"
    },
    "record_type": "event"
  }
}
```

> **Note:** MMS media URLs expire after **30 days**. Download and store media files if you need long-term access.

### Webhook Payload Schema

### Top-level fields

    | Field               | Type      | Description                                    |
    | ------------------- | --------- | ---------------------------------------------- |
    | `data.event_type`   | `string`  | Always `message.received` for inbound messages |
    | `data.id`           | `string`  | Unique event ID (UUID) — use for idempotency   |
    | `data.occurred_at`  | `string`  | ISO 8601 timestamp when the event occurred     |
    | `data.record_type`  | `string`  | Always `event`                                 |
    | `meta.attempt`      | `integer` | Webhook delivery attempt number (1–3)          |
    | `meta.delivered_to` | `string`  | The webhook URL this was delivered to          |

### Payload fields

    | Field                          | Type      | Description                                                               |
    | ------------------------------ | --------- | ------------------------------------------------------------------------- |
    | `payload.id`                   | `string`  | Unique message ID (UUID) — use for deduplication                          |
    | `payload.direction`            | `string`  | Always `inbound` for received messages                                    |
    | `payload.from.phone_number`    | `string`  | Sender's phone number (E.164 format)                                      |
    | `payload.from.carrier`         | `string`  | Sender's carrier name                                                     |
    | `payload.from.line_type`       | `string`  | `long_code`, `toll_free`, `short_code`, etc.                              |
    | `payload.to[].phone_number`    | `string`  | Your Telnyx number that received the message                              |
    | `payload.text`                 | `string`  | Message body (may be `null` for media-only MMS)                           |
    | `payload.type`                 | `string`  | `SMS` or `MMS`                                                            |
    | `payload.encoding`             | `string`  | `GSM-7` or `UCS-2` ([details](message-encoding.md)) |
    | `payload.parts`                | `integer` | Number of message segments                                                |
    | `payload.messaging_profile_id` | `string`  | Messaging profile that received the message                               |
    | `payload.received_at`          | `string`  | ISO 8601 timestamp when the message was received                          |
    | `payload.record_type`          | `string`  | Always `message`                                                          |

### Media fields (MMS)

    | Field                          | Type      | Description                                     |
    | ------------------------------ | --------- | ----------------------------------------------- |
    | `payload.media`                | `array`   | Array of media attachments (empty for SMS)      |
    | `payload.media[].url`          | `string`  | Authenticated download URL (expires in 30 days) |
    | `payload.media[].content_type` | `string`  | MIME type (e.g., `image/png`, `video/mp4`)      |
    | `payload.media[].sha256`       | `string`  | SHA-256 hash of the media file                  |
    | `payload.media[].size`         | `integer` | File size in bytes                              |

    **Supported MMS media types:**

    * Images: `image/jpeg`, `image/png`, `image/gif`, `image/bmp`, `image/webp`
    * Video: `video/mp4`, `video/3gpp`
    * Audio: `audio/mpeg`, `audio/ogg`, `audio/amr`
    * Files: `application/pdf`, `text/vcard`, `text/calendar`

***

## Downloading MMS Media

Download media attachments from inbound MMS messages using the URLs in the `media` array. Authenticate with your API key:

  ```javascript
  import fs from 'fs';

  async function downloadMedia(mediaUrl, apiKey) {
    const response = await fetch(mediaUrl, {
      headers: { 'Authorization': `Bearer ${apiKey}` }
    });

    const buffer = Buffer.from(await response.arrayBuffer());
    const filename = mediaUrl.split('/').pop();
    fs.writeFileSync(filename, buffer);
    console.log(`Downloaded: ${filename} (${buffer.length} bytes)`);
  }

  // In your webhook handler:
  for (const media of payload.media) {
    await downloadMedia(media.url, process.env.TELNYX_API_KEY);
  }
  ```

  ```python
  import requests
  import os

  def download_media(media_url, api_key):
      response = requests.get(
          media_url,
          headers={"Authorization": f"Bearer {api_key}"}
      )
      filename = media_url.split("/")[-1]
      with open(filename, "wb") as f:
          f.write(response.content)
      print(f"Downloaded: {filename} ({len(response.content)} bytes)")

  # In your webhook handler:
  for media in payload.get("media", []):
      download_media(media["url"], os.environ["TELNYX_API_KEY"])
  ```

  ```go
  func downloadMedia(mediaURL, apiKey string) error {
  	req, _ := http.NewRequest("GET", mediaURL, nil)
  	req.Header.Set("Authorization", "Bearer "+apiKey)

  	resp, err := http.DefaultClient.Do(req)
  	if err != nil {
  		return err
  	}
  	defer resp.Body.Close()

  	parts := strings.Split(mediaURL, "/")
  	filename := parts[len(parts)-1]

  	file, _ := os.Create(filename)
  	defer file.Close()

  	written, _ := io.Copy(file, resp.Body)
  	fmt.Printf("Downloaded: %s (%d bytes)\n", filename, written)
  	return nil
  }
  ```

  ```ruby
  require 'net/http'
  require 'uri'

  def download_media(media_url, api_key)
    uri = URI.parse(media_url)
    request = Net::HTTP::Get.new(uri)
    request['Authorization'] = "Bearer #{api_key}"

    response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
      http.request(request)
    end

    filename = File.basename(uri.path)
    File.open(filename, 'wb') { |f| f.write(response.body) }
    puts "Downloaded: #{filename} (#{response.body.bytesize} bytes)"
  end
  ```

  ```java
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.file.Path;

  public static void downloadMedia(String mediaUrl, String apiKey) throws Exception {
      HttpClient client = HttpClient.newHttpClient();
      HttpRequest request = HttpRequest.newBuilder()
          .uri(URI.create(mediaUrl))
          .header("Authorization", "Bearer " + apiKey)
          .build();

      String filename = mediaUrl.substring(mediaUrl.lastIndexOf('/') + 1);
      client.send(request, HttpResponse.BodyHandlers.ofFile(Path.of(filename)));
      System.out.println("Downloaded: " + filename);
  }
  ```

  ```csharp .NET theme={null}
  using var httpClient = new HttpClient();
  httpClient.DefaultRequestHeaders.Authorization =
      new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", apiKey);

  var response = await httpClient.GetAsync(mediaUrl);
  var bytes = await response.Content.ReadAsByteArrayAsync();
  var filename = new Uri(mediaUrl).Segments.Last();
  await File.WriteAllBytesAsync(filename, bytes);
  Console.WriteLine($"Downloaded: {filename} ({bytes.Length} bytes)");
  ```

  ```php
  <?php
  $ch = curl_init($mediaUrl);
  curl_setopt($ch, CURLOPT_HTTPHEADER, ["Authorization: Bearer $apiKey"]);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  $data = curl_exec($ch);
  curl_close($ch);

  $filename = basename(parse_url($mediaUrl, PHP_URL_PATH));
  file_put_contents($filename, $data);
  echo "Downloaded: $filename (" . strlen($data) . " bytes)\n";
  ```

  ```bash
  curl -o downloaded-media.png \
    -H "Authorization: Bearer YOUR_API_KEY" \
    "https://media.telnyx.com/example-image.png"
  ```

***

## Verifying Webhook Signatures

In production, verify webhook signatures to confirm requests are from Telnyx. All webhooks are signed using **ED25519** public key cryptography.

Each webhook includes two headers:

* `telnyx-signature-ed25519` — Base64-encoded signature
* `telnyx-timestamp` — Unix timestamp when the webhook was sent

  ```javascript
  import Telnyx from 'telnyx';

  const telnyx = new Telnyx('YOUR_API_KEY');

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
      res.sendStatus(400);
    }
  });
  ```

  ```python
  import telnyx

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
      except telnyx.error.SignatureVerificationError as e:
          print(f"Signature verification failed: {e}")
          return '', 400
  ```

  ```ruby
  require 'telnyx'

  Telnyx.api_key = 'YOUR_API_KEY'
  Telnyx.public_key = 'YOUR_PUBLIC_KEY'

  post '/webhooks' do
    payload = request.body.read
    signature = request.env['HTTP_TELNYX_SIGNATURE_ED25519']
    timestamp = request.env['HTTP_TELNYX_TIMESTAMP']

    begin
      event = Telnyx::Webhook.construct_event(payload, signature, timestamp)
      puts "Verified event: #{event['data']['event_type']}"
      status 200
    rescue Telnyx::SignatureVerificationError => e
      puts "Signature verification failed: #{e.message}"
      status 400
    end
  end
  ```

  ```csharp .NET theme={null}
  using Telnyx;

  app.MapPost("/webhooks", async (HttpRequest request) =>
  {
      var payload = await new StreamReader(request.Body).ReadToEndAsync();
      var signature = request.Headers["telnyx-signature-ed25519"].ToString();
      var timestamp = request.Headers["telnyx-timestamp"].ToString();

      try
      {
          var webhookEvent = Webhook.ConstructEvent(payload, signature, timestamp);
          Console.WriteLine($"Verified event: {webhookEvent.EventType}");
          return Results.Ok();
      }
      catch (TelnyxSignatureVerificationException e)
      {
          Console.WriteLine($"Signature verification failed: {e.Message}");
          return Results.BadRequest();
      }
  });
  ```

  ```php
  <?php
  require_once 'vendor/autoload.php';

  $payload = file_get_contents('php://input');
  $signature = $_SERVER['HTTP_TELNYX_SIGNATURE_ED25519'] ?? '';
  $timestamp = $_SERVER['HTTP_TELNYX_TIMESTAMP'] ?? '';

  try {
      $event = \Telnyx\Webhook::constructEvent($payload, $signature, $timestamp);
      echo "Verified event: " . $event['data']['event_type'];
      http_response_code(200);
  } catch (\Telnyx\Exception\SignatureVerificationException $e) {
      echo "Signature verification failed: " . $e->getMessage();
      http_response_code(400);
  }
  ```

Get your public key from the [Mission Control Portal](https://portal.telnyx.com) under **Account Settings > Keys & Credentials > Public Key**.

  For detailed webhook signature verification, see [Webhook Fundamentals](../reference/webhook-fundamentals-complete-guide-to-telnyx-webhooks.md).

***

## Handling Failed Webhooks

When webhook delivery fails, Telnyx retries automatically. Build resilience into your architecture:

  ```javascript
  import express from 'express';
  import { createClient } from 'redis';

  const app = express();
  app.use(express.json());

  const redis = createClient();
  await redis.connect();

  app.post('/webhooks', async (req, res) => {
    // Respond immediately to avoid timeout
    res.sendStatus(200);

    const { data } = req.body;
    const messageId = data.payload?.id;

    // Deduplicate using Redis (TTL: 24 hours)
    if (messageId) {
      const exists = await redis.get(`msg:${messageId}`);
      if (exists) return; // Already processed
      await redis.set(`msg:${messageId}`, '1', { EX: 86400 });
    }

    // Process asynchronously
    try {
      await processMessage(data);
    } catch (err) {
      console.error(`Failed to process ${messageId}:`, err);
      // Log to dead letter queue for manual review
      await redis.lpush('webhook:failed', JSON.stringify({ data, error: err.message }));
    }
  });
  ```

  ```python
  import redis
  import json
  import threading
  from flask import Flask, request

  app = Flask(__name__)
  r = redis.Redis()

  def process_async(data, message_id):
      """Process webhook in background thread."""
      try:
          process_message(data)
      except Exception as e:
          print(f"Failed to process {message_id}: {e}")
          r.lpush("webhook:failed", json.dumps({"data": data, "error": str(e)}))

  @app.route('/webhooks', methods=['POST'])
  def webhooks():
      data = request.json.get('data', {})
      message_id = data.get('payload', {}).get('id')

      # Deduplicate
      if message_id:
          if r.get(f"msg:{message_id}"):
              return '', 200
          r.set(f"msg:{message_id}", "1", ex=86400)

      # Process in background thread — return 200 immediately
      # For production, use Celery or RQ instead of threads
      threading.Thread(target=process_async, args=(data, message_id)).start()

      return '', 200
  ```

  For high-volume applications, use a message queue (Redis, SQS, RabbitMQ) between your webhook endpoint and processing logic. This ensures you always respond within the 2-second timeout.

***

## Troubleshooting

**Webhooks not arriving**

  **Check your webhook URL is configured:**

  ```bash theme={null}
  curl -s "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
    -H "Authorization: Bearer YOUR_API_KEY" | jq '.data.webhook_url'
  ```

  **Common causes:**

  * Webhook URL not set on the messaging profile
  * Phone number not assigned to the messaging profile
  * Server not publicly accessible (use ngrok for local dev)
  * Firewall blocking Telnyx IPs

  **Test your endpoint directly:**

  ```bash theme={null}
  curl -X POST https://your-server.com/webhooks \
    -H "Content-Type: application/json" \
    -d '{"data":{"event_type":"message.received","payload":{"text":"test"}}}'
  ```

---

**Receiving duplicate webhooks**

  Duplicates happen when your server doesn't respond with `2xx` within the timeout (2 seconds for API v2). Telnyx retries up to 2 times.

  **Fix:** Return `200` immediately, then process the message asynchronously. Use the `payload.id` field to deduplicate.

  ```javascript theme={null}
  // Deduplicate using a Set (use Redis in production)
  const processed = new Set();

  app.post('/webhooks', (req, res) => {
    res.sendStatus(200); // Respond immediately

    const messageId = req.body.data.payload?.id;
    if (messageId && processed.has(messageId)) return;
    processed.add(messageId);

    // Process message asynchronously
    handleMessage(req.body.data);
  });
  ```

---

**Webhook timeout errors**

  Your server must respond within **2 seconds** (API v2) or 5 seconds (API v1).

  **Solutions:**

  * Return `200` immediately, process in background
  * Use a message queue (Redis, SQS, RabbitMQ) for heavy processing
  * Set up a [failover URL](https://developers.telnyx.com/api-reference/profiles/update-a-messaging-profile) as a backup

---

**Missing media in MMS**

  * Check the `type` field is `MMS` (SMS messages have an empty `media` array)
  * Media URLs require authentication — include your API key in the `Authorization` header
  * Media URLs expire after 30 days
  * Verify your number is MMS-enabled in the [Portal](https://portal.telnyx.com/#/app/numbers/my-numbers)

---

***

## Webhook URL Hierarchy

Telnyx checks for webhook URLs in this order:

1. **Request body** — URLs provided when [sending a message](https://developers.telnyx.com/api-reference/messages/send-a-message) (outbound delivery receipts only)
2. **Messaging profile** — URLs configured on the profile
3. **No URL** — Webhook delivery is skipped

Configure a **failover URL** on your messaging profile for redundancy. If the primary URL fails all retry attempts, Telnyx sends to the failover URL.

***

## Related Webhook Events

Your webhook URL receives more than just `message.received`. For delivery status tracking and other events, see [Receiving Webhooks](receiving-webhooks-for-messaging.md).

| Event               | Description                                     |
| ------------------- | ----------------------------------------------- |
| `message.received`  | Inbound SMS or MMS received (this guide)        |
| `message.sent`      | Outbound message accepted by carrier            |
| `message.finalized` | Final delivery status (delivered, failed, etc.) |

***

## Next Steps

  - [Send Messages](send-your-first-message.md) — Send outbound SMS and MMS messages

  - [Webhooks Reference](receiving-webhooks-for-messaging.md) — All webhook event types and payload details

  - [Message Encoding](message-encoding.md) — Understand GSM-7, UCS-2, and message segmentation

  - [Auto-Reply with Opt-Out](advanced-opt-in-out-management.md) — Handle STOP/HELP keywords automatically


## Related Pages

- [Schedule SMS and MMS Messages](../runbooks/schedule-sms-and-mms-messages.md)
- [Send RCS Messages](../runbooks/send-rcs-messages.md)
