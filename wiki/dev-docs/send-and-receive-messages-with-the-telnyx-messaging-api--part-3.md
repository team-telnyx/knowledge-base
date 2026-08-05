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

*Part 3 of 6 — see also: [Part 1](send-and-receive-messages-with-the-telnyx-messaging-api--part-1.md), [Part 2](send-and-receive-messages-with-the-telnyx-messaging-api--part-2.md), [Part 4](send-and-receive-messages-with-the-telnyx-messaging-api--part-4.md), [Part 5](send-and-receive-messages-with-the-telnyx-messaging-api--part-5.md), [Part 6](send-and-receive-messages-with-the-telnyx-messaging-api--part-6.md)*

Walks through sending your first SMS and MMS with the Telnyx Messaging API, including setup, code samples in multiple languages, error handling, rate limiting, webhook-based delivery tracking, and inbound MMS processing.

## Receive an MMS

Inbound MMS messages arrive as webhooks to your messaging profile's webhook URL. The `media` array contains attachment details.

### Webhook Payload

```
{
  "data": {
    "event_type": "message.received",
    "payload": {
      "from": { "phone_number": "+18005550101" },
      "to": [{ "phone_number": "+18005550100" }],
      "text": "Check out this photo!",
      "media": [
        {
          "url": "https://media.telnyx.com/abc123/image.jpg",
          "content_type": "image/jpeg",
          "size": 245760
        }
      ]
    }
  }
}
```

**Media URLs are ephemeral.** Telnyx-hosted media links expire. Download and store attachments in your own storage immediately upon receipt.

### Process Inbound MMS

#### Python

```
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TELNYX_API_KEY = os.getenv("TELNYX_API_KEY")
MEDIA_DIR = "./received_media"
os.makedirs(MEDIA_DIR, exist_ok=True)

@app.route("/webhooks", methods=["POST"])
def webhooks():
    body = request.json
    event_type = body["data"]["event_type"]

    if event_type != "message.received":
        return jsonify({"status": "ignored"}), 200

    payload = body["data"]["payload"]
    from_number = payload["from"]["phone_number"]
    text = payload.get("text", "")
    media = payload.get("media", [])

    print(f"From: {from_number} | Text: {text} | Attachments: {len(media)}")

    # Download each attachment
    saved_files = []
    for item in media:
        resp = requests.get(item["url"])
        ext = item["content_type"].split("/")[-1]
        filename = f"{MEDIA_DIR}/{from_number}_{len(saved_files)}.{ext}"
        with open(filename, "wb") as f:
            f.write(resp.content)
        saved_files.append(filename)
        print(f"  Saved: {filename} ({item['size']} bytes)")

    return jsonify({"status": "ok", "files": len(saved_files)}), 200

if __name__ == "__main__":
    app.run(port=8000)
```

#### Node

```
const express = require("express");
const axios = require("axios");
const fs = require("fs");
const path = require("path");

const app = express();
app.use(express.json());

const MEDIA_DIR = "./received_media";
fs.mkdirSync(MEDIA_DIR, { recursive: true });

app.post("/webhooks", async (req, res) => {
  const { event_type, payload } = req.body.data;

  if (event_type !== "message.received") {
    return res.json({ status: "ignored" });
  }

  const from = payload.from.phone_number;
  const text = payload.text || "";
  const media = payload.media || [];

  console.log(`From: ${from} | Text: ${text} | Attachments: ${media.length}`);

  for (let i = 0; i < media.length; i++) {
    const resp = await axios.get(media[i].url, { responseType: "arraybuffer" });
    const ext = media[i].content_type.split("/").pop();
    const filename = path.join(MEDIA_DIR, `${from}_${i}.${ext}`);
    fs.writeFileSync(filename, resp.data);
    console.log(`  Saved: ${filename} (${media[i].size} bytes)`);
  }

  res.json({ status: "ok", files: media.length });
});

app.listen(8000, () => console.log("Listening on port 8000"));
```

#### Ruby

```
require "sinatra"
require "net/http"
require "json"
require "fileutils"

MEDIA_DIR = "./received_media"
FileUtils.mkdir_p(MEDIA_DIR)

post "/webhooks" do
  body = JSON.parse(request.body.read)
  event_type = body.dig("data", "event_type")

  return { status: "ignored" }.to_json unless event_type == "message.received"

  payload = body.dig("data", "payload")
  from = payload.dig("from", "phone_number")
  media = payload.fetch("media", [])

  puts "From: #{from} | Attachments: #{media.length}"

  media.each_with_index do |item, i|
    uri = URI(item["url"])
    resp = Net::HTTP.get(uri)
    ext = item["content_type"].split("/").last
    filename = "#{MEDIA_DIR}/#{from}_#{i}.#{ext}"
    File.binwrite(filename, resp)
    puts "  Saved: #{filename}"
  end

  { status: "ok" }.to_json
end
```

#### Go

```
package main

import (
    "encoding/json"
    "fmt"
    "io"
    "net/http"
    "os"
    "path/filepath"
    "strings"
)

const mediaDir = "./received_media"

type Webhook struct {
    Data struct {
        EventType string `json:"event_type"`
        Payload   struct {
            From  struct{ PhoneNumber string `json:"phone_number"` } `json:"from"`
            Text  string `json:"text"`
            Media []struct {
                URL         string `json:"url"`
                ContentType string `json:"content_type"`
                Size        int    `json:"size"`
            } `json:"media"`
        } `json:"payload"`
    } `json:"data"`
}

func handler(w http.ResponseWriter, r *http.Request) {
    var wh Webhook
    json.NewDecoder(r.Body).Decode(&wh)

    if wh.Data.EventType != "message.received" {
        json.NewEncoder(w).Encode(map[string]string{"status": "ignored"})
        return
    }

    from := wh.Data.Payload.From.PhoneNumber
    fmt.Printf("From: %s | Attachments: %d\n", from, len(wh.Data.Payload.Media))

    for i, item := range wh.Data.Payload.Media {
        resp, _ := http.Get(item.URL)
        defer resp.Body.Close()
        ext := strings.Split(item.ContentType, "/")[1]
        filename := filepath.Join(mediaDir, fmt.Sprintf("%s_%d.%s", from, i, ext))
        f, _ := os.Create(filename)
        io.Copy(f, resp.Body)
        f.Close()
        fmt.Printf("  Saved: %s\n", filename)
    }

    json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
}

func main() {
    os.MkdirAll(mediaDir, 0755)
    http.HandleFunc("/webhooks", handler)
    fmt.Println("Listening on port 8000")
    http.ListenAndServe(":8000", nil)
}
```

### Reply with Media

Echo received media back to the sender, or reply with different media:

#### Python

```
import telnyx
import os

telnyx.api_key = os.getenv("TELNYX_API_KEY")

def handle_mms_webhook(payload):
    """Reply to inbound MMS with the same media + a text response."""
    from_number = payload["from"]["phone_number"]
    to_number = payload["to"][0]["phone_number"]
    media = payload.get("media", [])

    # Reply with the same media echoed back
    media_urls = [item["url"] for item in media]

    reply = telnyx.Message.create(
        from_=to_number,
        to=from_number,
        text=f"Thanks! Received {len(media)} attachment(s).",
        media_urls=media_urls if media_urls else None,
        messaging_profile_id="YOUR_MESSAGING_PROFILE_ID"
    )

    print(f"Reply sent: {reply.id}")
```

#### Node

```
const telnyx = require("telnyx")(process.env.TELNYX_API_KEY);

async function handleMmsWebhook(payload) {
  const from = payload.from.phone_number;
  const to = payload.to[0].phone_number;
  const media = payload.media || [];
  const mediaUrls = media.map((m) => m.url);

  const reply = await telnyx.messages.create({
    from: to,
    to: from,
    text: `Thanks! Received ${media.length} attachment(s).`,
    media_urls: mediaUrls.length ? mediaUrls : undefined,
    messaging_profile_id: "YOUR_MESSAGING_PROFILE_ID",
  });

  console.log(`Reply sent: ${reply.data.id}`);
}
```

### Store Media Externally (Optional)

For production use, store received media in your own cloud storage rather than relying on ephemeral Telnyx URLs.

#### Upload to AWS S3

```
import boto3
import requests
from urllib.parse import urlparse

s3 = boto3.client("s3")
BUCKET = "your-mms-bucket"

def save_to_s3(media_url, from_number, index):
    resp = requests.get(media_url)
    content_type = resp.headers.get("content-type", "application/octet-stream")
    ext = content_type.split("/")[-1]
    key = f"mms/{from_number}/{index}.{ext}"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=resp.content,
        ContentType=content_type
    )
    return f"s3://{BUCKET}/{key}"
```

#### Upload to Google Cloud Storage

```
from google.cloud import storage
import requests

gcs = storage.Client()
bucket = gcs.bucket("your-mms-bucket")

def save_to_gcs(media_url, from_number, index):
    resp = requests.get(media_url)
    content_type = resp.headers.get("content-type", "application/octet-stream")
    ext = content_type.split("/")[-1]

    blob = bucket.blob(f"mms/{from_number}/{index}.{ext}")
    blob.upload_from_string(resp.content, content_type=content_type)
    return blob.public_url
```
