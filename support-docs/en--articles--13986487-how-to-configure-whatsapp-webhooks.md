---
source_url: https://support.telnyx.com/en/articles/13986487-how-to-configure-whatsapp-webhooks
title: "How to Configure WhatsApp Webhooks"
description: "Set up webhook endpoints to receive inbound WhatsApp messages and delivery status updates. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 3165ce048d08e449a328ce473f21437e7ae480a5538c6e42f26e248bbfc6b475
---







# How to Configure WhatsApp Webhooks

Set up webhook endpoints to receive inbound WhatsApp messages and delivery status updates. See Telnyx guidance and requirements.




## Overview

Webhooks let you receive real-time notifications when customers send you WhatsApp messages and when your outbound messages are delivered, read, or fail. Configure your webhook URL through the WABA webhook settings in the Telnyx API or Portal.

## Setting Up Webhooks

## Via the Telnyx Portal

1. Go to **Messaging → WhatsApp**
2. Select your WhatsApp Business Account
3. Navigate to the webhook configuration section
4. Enter your webhook URL (must be HTTPS)
5. Save the configuration

## Via the API

Use the WABA webhook configuration endpoint to set your webhook URL programmatically. You can also specify a `webhook_url` per message when sending via `POST /v2/messages/whatsapp`.

## Webhook Events

## Inbound Messages

When a customer sends you a message, you receive a webhook with the message content. The payload includes:

* Sender's phone number
* Message type (text, image, video, document, audio, location, contacts, interactive reply)
* Message content (text body, media URL, location coordinates, etc.)
* Timestamp
* Message ID (for replying with context)

## Delivery Status Updates

For each outbound message, you receive status webhooks as the message progresses:

|  |  |
| --- | --- |
| Status | Meaning |
| `sent` | Message accepted by WhatsApp |
| `delivered` | Message delivered to recipient's device |
| `read` | Recipient opened/read the message |
| `failed` | Message could not be delivered |

Delivery status webhooks include the `billing_type` field (e.g., `whatsapp_marketing`, `whatsapp_utility`, `whatsapp_service`) so you can track costs.

## Webhook Requirements

* **HTTPS** — Your endpoint must use HTTPS with a valid SSL certificate
* **200 response** — Return a 200 status code within 5 seconds to acknowledge receipt
* **Idempotency** — You may receive the same webhook multiple times; handle duplicates gracefully using the message ID

## Testing Webhooks

For development, you can use tools like [ngrok](https://ngrok.com) or [Hookdeck](https://hookdeck.com) to expose a local endpoint to the internet and inspect incoming webhook payloads.

## Related Resources

* [Receiving Webhooks Guide](https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks)

---

Related Articles

[How to Leverage Webhooks](https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks)[What is WhatsApp Business Platform?](https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform)[How to Set Up WhatsApp on Telnyx](https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)[WhatsApp Troubleshooting Guide](https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide)

Did this answer your question?

😞😐😃
