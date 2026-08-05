---
title: 10DLC Campaign Use Cases and Event Notifications
summary: Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages,
  opt-in/opt-out requirements, and webhook event notifications for brands, campaigns,
  and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
updated_at: 2026-08-05T13:49:31Z
---

# 10DLC Campaign Use Cases and Event Notifications

*Part 7 of 8 — see also: [Part 1](10dlc-campaign-use-cases-and-event-notifications--part-1.md), [Part 2](10dlc-campaign-use-cases-and-event-notifications--part-2.md), [Part 3](10dlc-campaign-use-cases-and-event-notifications--part-3.md), [Part 4](10dlc-campaign-use-cases-and-event-notifications--part-4.md), [Part 5](10dlc-campaign-use-cases-and-event-notifications--part-5.md), [Part 6](10dlc-campaign-use-cases-and-event-notifications--part-6.md), [Part 8](10dlc-campaign-use-cases-and-event-notifications--part-8.md)*

Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages, opt-in/opt-out requirements, and webhook event notifications for brands, campaigns, and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.

## Processing Webhooks with SDK Examples

Handle 10DLC event notifications in your application to track registration status, respond to failures, and automate workflows:

**Python (Flask):**

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route("/webhooks/10dlc", methods=["POST"])
def handle_10dlc_webhook():
    """Process 10DLC event notifications."""
    event = request.json
    data = event["data"]
    event_type = data["event_type"]
    payload = data["payload"]
    event_id = data["id"]

    # Deduplicate — store processed event IDs
    if is_duplicate(event_id):
        return jsonify({"status": "already_processed"}), 200

    if event_type == "10dlc.brand.update":
        handle_brand_event(payload)
    elif event_type == "10dlc.campaign.update":
        handle_campaign_event(payload)
    elif event_type == "10dlc.phone_number.update":
        handle_phone_number_event(payload)

    mark_processed(event_id)
    return jsonify({"status": "ok"}), 200

def handle_brand_event(payload):
    brand_id = payload["brandId"]
    event_type = payload["type"]
    status = payload.get("status", "")

    if event_type == "REGISTRATION" and status == "failed":
        reasons = payload.get("reasons", [])
        logger.error(f"Brand {brand_id} registration failed: {reasons}")
        alert_team(f"10DLC brand registration failed: {reasons}")

    elif event_type == "TCR_BRAND_UPDATE":
        tcr_event = payload.get("eventType", "")
        if tcr_event == "BRAND_ADD":
            logger.info(f"Brand {brand_id} added to TCR")
        elif tcr_event == "BRAND_REVET":
            logger.info(f"Brand {brand_id} revet completed: {status}")

    elif event_type == "ORDER_EXTERNAL_VETTING":
        logger.info(f"Brand {brand_id} vetting order: {status}")

def handle_campaign_event(payload):
    campaign_id = payload.get("campaignId", "")
    event_type = payload["type"]
    status = payload.get("status", "")

    if event_type == "REGISTRATION" and status == "failed":
        reasons = payload.get("reasons", [])
        logger.error(f"Campaign {campaign_id} registration failed: {reasons}")

    elif event_type == "TELNYX_REVIEW":
        if status == "ACCEPTED":
            logger.info(f"Campaign {campaign_id} approved by Telnyx")
        elif status == "REJECTED":
            logger.warning(f"Campaign {campaign_id} rejected by Telnyx")

    elif event_type == "MNO_REVIEW":
        logger.info(f"Campaign {campaign_id} MNO review: {status}")

    elif event_type == "VERIFIED":
        logger.info(f"Campaign {campaign_id} fully provisioned!")
        # Campaign is ready — you can start sending messages

def handle_phone_number_event(payload):
    phone = payload.get("phoneNumber", "")
    status = payload.get("status", "")
    logger.info(f"Phone number {phone} 10DLC status: {status}")
```

**Node.js (Express):**

```javascript
import express from 'express';

const app = express();
app.use(express.json());

const processedEvents = new Set();

app.post('/webhooks/10dlc', (req, res) => {
  const { data } = req.body;
  const { event_type, payload, id: eventId } = data;

  // Deduplicate
  if (processedEvents.has(eventId)) {
    return res.json({ status: 'already_processed' });
  }

  switch (event_type) {
    case '10dlc.brand.update':
      handleBrandEvent(payload);
      break;
    case '10dlc.campaign.update':
      handleCampaignEvent(payload);
      break;
    case '10dlc.phone_number.update':
      handlePhoneNumberEvent(payload);
      break;
  }

  processedEvents.add(eventId);
  res.json({ status: 'ok' });
});

function handleBrandEvent(payload) {
  const { brandId, type, status, reasons } = payload;

  if (type === 'REGISTRATION' && status === 'failed') {
    console.error(`Brand ${brandId} registration failed:`, reasons);
    alertTeam(`10DLC brand registration failed: ${JSON.stringify(reasons)}`);
  } else if (type === 'TCR_BRAND_UPDATE') {
    console.log(`Brand ${brandId} TCR event: ${payload.eventType} (${status})`);
  } else if (type === 'ORDER_EXTERNAL_VETTING') {
    console.log(`Brand ${brandId} vetting: ${status}`);
  }
}

function handleCampaignEvent(payload) {
  const { campaignId, type, status, reasons } = payload;

  if (type === 'REGISTRATION' && status === 'failed') {
    console.error(`Campaign ${campaignId} failed:`, reasons);
  } else if (type === 'TELNYX_REVIEW') {
    console.log(`Campaign ${campaignId} Telnyx review: ${status}`);
  } else if (type === 'VERIFIED') {
    console.log(`Campaign ${campaignId} fully provisioned — ready to send!`);
  }
}

function handlePhoneNumberEvent(payload) {
  console.log(`Phone ${payload.phoneNumber} status: ${payload.status}`);
}

app.listen(3000, () => console.log('Webhook server running on port 3000'));
```

**Ruby (Sinatra):**

```ruby
require "sinatra"
require "json"

processed_events = Set.new

post "/webhooks/10dlc" do
  event = JSON.parse(request.body.read)
  data = event["data"]
  event_type = data["event_type"]
  payload = data["payload"]
  event_id = data["id"]

  return { status: "already_processed" }.to_json if processed_events.include?(event_id)

  case event_type
  when "10dlc.brand.update"
    if payload["type"] == "REGISTRATION" && payload["status"] == "failed"
      puts "Brand #{payload['brandId']} registration failed: #{payload['reasons']}"
    else
      puts "Brand #{payload['brandId']} event: #{payload['type']} (#{payload['status']})"
    end
  when "10dlc.campaign.update"
    if payload["type"] == "VERIFIED"
      puts "Campaign #{payload['campaignId']} fully provisioned!"
    else
      puts "Campaign event: #{payload['type']} (#{payload['status']})"
    end
  when "10dlc.phone_number.update"
    puts "Phone #{payload['phoneNumber']} status: #{payload['status']}"
  end

  processed_events.add(event_id)
  { status: "ok" }.to_json
end
```

**Go:**

```go
package main

import (
  "encoding/json"
  "fmt"
  "log"
  "net/http"
  "sync"
)

var (
  processed = make(map[string]bool)
  mu        sync.Mutex
)

type WebhookEvent struct {
  Data struct {
    EventType string                 `json:"event_type"`
    ID        string                 `json:"id"`
    Payload   map[string]interface{} `json:"payload"`
  } `json:"data"`
}

func handler(w http.ResponseWriter, r *http.Request) {
  var event WebhookEvent
  json.NewDecoder(r.Body).Decode(&event)

  mu.Lock()
  if processed[event.Data.ID] {
    mu.Unlock()
    json.NewEncoder(w).Encode(map[string]string{"status": "already_processed"})
    return
  }
  processed[event.Data.ID] = true
  mu.Unlock()

  p := event.Data.Payload
  switch event.Data.EventType {
  case "10dlc.brand.update":
    log.Printf("Brand %s event: %s (%s)", p["brandId"], p["type"], p["status"])
  case "10dlc.campaign.update":
    if p["type"] == "VERIFIED" {
      log.Printf("Campaign %s fully provisioned!", p["campaignId"])
    } else {
      log.Printf("Campaign %s event: %s (%s)", p["campaignId"], p["type"], p["status"])
    }
  case "10dlc.phone_number.update":
    log.Printf("Phone %s status: %s", p["phoneNumber"], p["status"])
  }

  w.Header().Set("Content-Type", "application/json")
  fmt.Fprintf(w, `{"status":"ok"}`)
}

func main() {
  http.HandleFunc("/webhooks/10dlc", handler)
  log.Println("Webhook server on :3000")
  log.Fatal(http.ListenAndServe(":3000", nil))
}
```

**PHP:**

```php
<?php
$processedEvents = [];

$input = json_decode(file_get_contents('php://input'), true);
$data = $input['data'];
$eventType = $data['event_type'];
$payload = $data['payload'];
$eventId = $data['id'];

header('Content-Type: application/json');

if (in_array($eventId, $processedEvents)) {
    echo json_encode(['status' => 'already_processed']);
    exit;
}

switch ($eventType) {
    case '10dlc.brand.update':
        if ($payload['type'] === 'REGISTRATION' && $payload['status'] === 'failed') {
            error_log("Brand {$payload['brandId']} registration failed: " . json_encode($payload['reasons']));
        } else {
            error_log("Brand {$payload['brandId']} event: {$payload['type']} ({$payload['status']})");
        }
        break;

    case '10dlc.campaign.update':
        if ($payload['type'] === 'VERIFIED') {
            error_log("Campaign {$payload['campaignId']} fully provisioned!");
        } else {
            error_log("Campaign event: {$payload['type']} ({$payload['status']})");
        }
        break;

    case '10dlc.phone_number.update':
        error_log("Phone {$payload['phoneNumber']} status: {$payload['status']}");
        break;
}

echo json_encode(['status' => 'ok']);
```

> **Important:** Always return a `200` response immediately, then process the webhook asynchronously. For production applications, use a message queue (Redis, RabbitMQ, SQS) to decouple webhook receipt from processing.
