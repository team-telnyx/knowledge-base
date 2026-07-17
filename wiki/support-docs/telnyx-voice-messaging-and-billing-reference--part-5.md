---
title: Telnyx Voice, Messaging, and Billing Reference
summary: This page consolidates Telnyx documentation covering VoIP and telecommunications
  protocols (RTP, UDP, TCP, SIP, SDP), audio codecs and SDP parameters, external call
  transfers, webhooks (including WhatsApp webhooks and signing key rotation), A2P
  vs P2P traffic types and the P2P exemption process, toll-free opt-in workflow templates,
  and payment methods including ACH Direct Debit and Bitcoin.
sources:
- url: https://support.telnyx.com/en/articles/1130723-voip-telecommunications-protocols
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
- url: https://support.telnyx.com/en/articles/13986487-how-to-configure-whatsapp-webhooks
- url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
- url: https://support.telnyx.com/en/articles/7045419-ach-direct-debit-payment-method
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
- url: https://support.telnyx.com/en/articles/8379618-bitcoin-payment-method
- url: https://support.telnyx.com/en/articles/8685561-p2p-definition-and-exemption-process
updated_at: 2026-07-17T09:07:29Z
---

# Telnyx Voice, Messaging, and Billing Reference

*Part 5 of 8 — see also: [Part 1](telnyx-voice-messaging-and-billing-reference--part-1.md), [Part 2](telnyx-voice-messaging-and-billing-reference--part-2.md), [Part 3](telnyx-voice-messaging-and-billing-reference--part-3.md), [Part 4](telnyx-voice-messaging-and-billing-reference--part-4.md), [Part 6](telnyx-voice-messaging-and-billing-reference--part-6.md), [Part 7](telnyx-voice-messaging-and-billing-reference--part-7.md), [Part 8](telnyx-voice-messaging-and-billing-reference--part-8.md)*

This page consolidates Telnyx documentation covering VoIP and telecommunications protocols (RTP, UDP, TCP, SIP, SDP), audio codecs and SDP parameters, external call transfers, webhooks (including WhatsApp webhooks and signing key rotation), A2P vs P2P traffic types and the P2P exemption process, toll-free opt-in workflow templates, and payment methods including ACH Direct Debit and Bitcoin.

## WhatsApp Webhooks

Webhooks let you receive real-time notifications when customers send you WhatsApp messages and when your outbound messages are delivered, read, or fail. Configure your webhook URL through the WABA webhook settings in the Telnyx API or Portal.

### Setting Up Webhooks

**Via the Telnyx Portal:**

1. Go to **Messaging → WhatsApp**
2. Select your WhatsApp Business Account
3. Navigate to the webhook configuration section
4. Enter your webhook URL (must be HTTPS)
5. Save the configuration

**Via the API:**

Use the WABA webhook configuration endpoint to set your webhook URL programmatically. You can also specify a `webhook_url` per message when sending via `POST /v2/messages/whatsapp`.

### Webhook Events

**Inbound Messages** — When a customer sends you a message, you receive a webhook with the message content. The payload includes:

- Sender's phone number
- Message type (text, image, video, document, audio, location, contacts, interactive reply)
- Message content (text body, media URL, location coordinates, etc.)
- Timestamp
- Message ID (for replying with context)

**Delivery Status Updates** — For each outbound message, you receive status webhooks as the message progresses:

| Status | Meaning |
| --- | --- |
| `sent` | Message accepted by WhatsApp |
| `delivered` | Message delivered to recipient's device |
| `read` | Recipient opened/read the message |
| `failed` | Message could not be delivered |

Delivery status webhooks include the `billing_type` field (e.g., `whatsapp_marketing`, `whatsapp_utility`, `whatsapp_service`) so you can track costs.

### Webhook Requirements

- **HTTPS** — Your endpoint must use HTTPS with a valid SSL certificate.
- **200 response** — Return a 200 status code within 5 seconds to acknowledge receipt.
- **Idempotency** — You may receive the same webhook multiple times; handle duplicates gracefully using the message ID.

### Testing Webhooks

For development, you can use tools like [ngrok](https://ngrok.com) or [Hookdeck](https://hookdeck.com) to expose a local endpoint to the internet and inspect incoming webhook payloads.

## Updating the Webhook Signing Key

Telnyx signs the webhook events it sends to clients so that the authenticity of the request can be verified. Webhook signing in API V2 uses public key encryption. The public key is available in the Mission Control Portal under account settings in the left-hand navigation bar > Keys & Credentials > Public Key sub tab.

If your public key has been compromised and you need to update it, or if you would like to rotate it as a regular practice, follow the steps below.

### Step 1 — Creating an Inactive Public Key

To create a new inactive public signing key, run the following curl command in a terminal or import it into Postman:

```
curl -X POST https://api.telnyx.com/v2/inactive_key -H "Authorization: Bearer $API_KEY"
```

Replace `$API_KEY` with your Telnyx API V2 key. If the request succeeds, you will receive a response similar to:

```json
{
    "data": {
        "id": "a896de0d-b250-450d-8ac4-ca901dcc73d6",
        "public": "iGtB96aTJO4SmJPzRPqW20Zc10AWCiN8OQLE5Tg330U=",
        "record_type": "public_key"
    }
}
```

Take note of the `id` field — it is required to activate this key in the next step.

### Step 2 — Activating the Inactive Public Key

Once you are ready to rotate the existing public key, activate the key you created in the previous step:

```
curl -X POST https://api.telnyx.com/v2/inactive_key/a896de0d-b250-450d-8ac4-ca901dcc73d6/activate -H "Authorization: Bearer $API_KEY"
```

The key is referenced by its `id`, which you received in the previous step. You can use the example below and replace `{id}` with the actual value:

```
https://api.telnyx.com/v2/inactive_key/{id}/activate
```

If the activation is successful, you will receive a response similar to:

```json
{
    "data": {
        "result": "success"
    }
}
```

### Important Notes

- Only 1 inactive key can be added to an organization (managed account). Subsequent requests to create a new inactive key will override the previous inactive key.
- Activation of inactive keys is not immediate and can take up to 60 minutes to propagate across the entire account. There is a period of time that both (current and new) keys could be active at the same time.

## Traffic Type: A2P vs P2P

The Telnyx Traffic Type feature allows users to select if an eligible number will be routed to an end user as Application-to-Person (A2P) or Person-to-Person (P2P) traffic. Selecting a traffic type that aligns with the number's messaging use case will improve message deliverability.

- **A2P Traffic Type** — Generally used for domestic messaging and one-way communication with large campaigns. This traffic type does not support international messaging.
- **P2P Traffic Type** — Ideal for two-way communication and allows customers to send messages internationally.

Note: Some numbers do not have the option to select P2P, because only numbers assigned to the Telnyx SPID can currently switch between A2P and P2P at this time. See the [A2P vs P2P resource](https://telnyx.com/resources/sms-numbers-traffic-types) for more details. CTIA's [Messaging Principles and Best Practices](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf) offer recommendations to help guide your decision.
