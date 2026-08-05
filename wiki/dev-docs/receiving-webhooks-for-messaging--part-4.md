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

*Part 4 of 6 — see also: [Part 1](receiving-webhooks-for-messaging--part-1.md), [Part 2](receiving-webhooks-for-messaging--part-2.md), [Part 3](receiving-webhooks-for-messaging--part-3.md), [Part 5](receiving-webhooks-for-messaging--part-5.md), [Part 6](receiving-webhooks-for-messaging--part-6.md)*

Telnyx delivers webhooks to notify applications about messaging events in real time, including inbound messages, delivery status updates, read receipts, and suggestion responses. This page covers webhook event types, payload structures for SMS/MMS and RCS, signature verification, retry behavior, and best practices for production webhook handling.

## Webhook signature verification

Telnyx signs every webhook using **Ed25519 public key cryptography** so you can verify that requests genuinely come from Telnyx. **This is strongly recommended for production deployments.**

Each webhook request includes two headers:

| Header | Description |
| --- | --- |
| `telnyx-signature-ed25519` | Base64-encoded Ed25519 signature |
| `telnyx-timestamp` | Unix timestamp of when the request was signed |

The signature is computed over the string `{timestamp}|{json_payload}`.

### Get your public key

Find your public key in the [Mission Control Portal](https://portal.telnyx.com/#/app/api-keys) under **Keys & Credentials → Public Key**.

### Verification examples

**Node**

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

**Python**

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

**Ruby**

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

**Go**

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

**Java**

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

**.NET**

```csharp
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

**PHP**

```php
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

**Timestamp tolerance:** To prevent replay attacks, reject webhooks where `telnyx-timestamp` is more than 5 minutes old.
