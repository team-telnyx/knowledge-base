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

*Part 4 of 8 — see also: [Part 1](telnyx-voice-messaging-and-billing-reference--part-1.md), [Part 2](telnyx-voice-messaging-and-billing-reference--part-2.md), [Part 3](telnyx-voice-messaging-and-billing-reference--part-3.md), [Part 5](telnyx-voice-messaging-and-billing-reference--part-5.md), [Part 6](telnyx-voice-messaging-and-billing-reference--part-6.md), [Part 7](telnyx-voice-messaging-and-billing-reference--part-7.md), [Part 8](telnyx-voice-messaging-and-billing-reference--part-8.md)*

This page consolidates Telnyx documentation covering VoIP and telecommunications protocols (RTP, UDP, TCP, SIP, SDP), audio codecs and SDP parameters, external call transfers, webhooks (including WhatsApp webhooks and signing key rotation), A2P vs P2P traffic types and the P2P exemption process, toll-free opt-in workflow templates, and payment methods including ACH Direct Debit and Bitcoin.

## Webhooks

A webhook (also called a web callback or HTTP push API) is a way for an app to provide other applications with real-time information. A webhook delivers data to other applications as it happens, meaning you get data immediately.

You can choose to be notified about events that Telnyx sends to you by configuring webhook URLs in your SIP Connection or Applications (voice, fax, or messaging). Webhooks will be sent from the IP range of the region where your calls are anchored; see the [Guide to SIP Anchorsite Settings](guide-to-sip-anchorsite-settings.md) for more on controlling which region calls are anchored in.

### Whitelisting

If you use an ACL or firewall on your network, make sure to whitelist Telnyx's network IP assignments per region.

### Requirements

A publicly accessible HTTP server is required to receive webhook requests at one or more specified URLs. HTTPS is highly recommended over HTTP. A basic tutorial for receiving webhooks is available in the developer documentation.

### Hierarchy of URLs

If webhooks are provided in the request body, those are used; otherwise, if the profile has webhooks, those are used. If neither has webhooks, no webhook delivery is attempted.

### Delivery Status Updates

Telnyx Messaging Services will attempt to notify you about each status update based on the hierarchy of URLs above.

### Delivery Status Payload

Example webhook event for a delivery receipt returned to the sender after sending a message through a Telnyx long code to a T-Mobile long code:

```json
{
   "data":{
      "event_type":"message.finalized",
      "id":"4ee8c3a6-4995-4309-a3c6-38e3db9ea4be",
      "occurred_at":"2019-12-09T21:32:14.148+00:00",
      "payload":{
         "completed_at":"2019-12-09T21:32:14.148+00:00",
         "cost":null,
         "direction":"outbound",
         "encoding":"GSM-7",
         "errors":[
         ],
         "from":{
            "carrier":"T-Mobile USA",
            "line_type":"Wireless",
            "phone_number":"+13125000000",
            "status":"webhook_delivered"
         },
         "id":"ac012cbf-5e09-46af-a69a-7c0e2d90993c",
         "media":[
         ],
         "messaging_profile_id":"83d2343b-553f-4c5f-b8c8-fd27004f94bf",
         "organization_id":"9d76d591-1b7d-405d-8c64-1320ee070245",
         "parts":1,
         "received_at":"2019-12-09T21:32:13.552+00:00",
         "record_type":"message",
         "sent_at":"2019-12-09T21:32:13.596+00:00",
         "tags":[
         ],
         "text":"Hello there!",
         "to":[
            {
               "carrier":"T-MOBILE USA, INC.",
               "line_type":"Wireless",
               "phone_number":"+13125000000",
               "status":"delivered"
            }
         ],
         "type":"SMS",
         "valid_until":"2019-12-09T22:32:13.552+00:00",
         "webhook_failover_url":"",
         "webhook_url":"http://webhook.site/af3a92e7-e150-442c-9fe6-61658ce26b1a"
      },
      "record_type":"event"
   },
   "meta":{
      "attempt":1,
      "delivered_to":"http://webhook.site/af3a92e7-e150-442c-9fe6-61658ce26b1a"
   }
}
```

![Delivery statuses and description table.](_images/2146954307b5b56c.png)

### Incoming Message Payload

Telnyx can use webhooks to notify you of new inbound messages to your SMS-capable long code and toll-free phone numbers. This feature is enabled by configuring the incoming webhooks on the associated messaging profile. Regardless of whether webhook delivery is configured, records of received messages are still available in reports via the Mission Control Portal or the Reports API endpoint.

Example webhook event for a Telnyx long code receiving a text message from a T-Mobile long code:

```json
{
   "data":{
      "event_type":"message.received",
      "id":"b301ed3f-1490-491f-995f-6e64e69674d4",
      "occurred_at":"2019-12-09T20:16:07.588+00:00",
      "payload":{
         "completed_at":null,
         "cost":null,
         "direction":"inbound",
         "encoding":"GSM-7",
         "errors":[
         ],
         "from":{
            "carrier":"T-Mobile USA",
            "line_type":"long_code",
            "phone_number":"+1312500000",
            "status":"webhook_delivered"
         },
         "id":"84cca175-9755-4859-b67f-4730d7f58aa3",
         "media":[
         ],
         "messaging_profile_id":"740572b6-099c-44a1-89b9-6c92163bc68d",
         "organization_id":"47a530f8-4362-4526-829b-bcee17fd9f7a",
         "parts":1,
         "received_at":"2019-12-09T20:16:07.503+00:00",
         "record_type":"message",
         "sent_at":null,
         "tags":[
         ],
         "text":"Hello from Telnyx!",
         "to":[
            {
               "carrier":"Telnyx",
               "line_type":"Wireless",
               "phone_number":"+1773005000",
               "status":"webhook_delivered"
            }
         ],
         "type":"SMS",
         "valid_until":null,
         "webhook_failover_url":null,
         "webhook_url":"http://webhook.site/04bbd2e3-09b5-4c9e-95de-a1debeb9e675"
      },
      "record_type":"event"
   },
   "meta":{
      "attempt":1,
      "delivered_to":"http://webhook.site/04bbd2e3-09b5-4c9e-95de-a1debeb9e675"
   }
}
```

Note: MMS media links are available for 30 days after message receipt. After 30 days the link expires and the media is no longer available through Telnyx.

### Responding to a Webhook

To acknowledge receipt of a webhook, your endpoint should return a `2xx` HTTP status code. Any other information returned in the request headers or body is ignored. All response codes outside this range, including `3xx` codes, indicate that you did not receive the webhook. URL redirection or a "Not Modified" response is treated as a failure.

### Retries

Webhooks will be retried to each of the supplied URLs if your application does not respond in 2000 milliseconds. This is typically seen when the webhook URL endpoint does not return a response; Telnyx will time out the original request and attempt to retry one more time. You can determine when a timeout occurs by reviewing the Debugging / Webhook section, where you will see a response code of 0.

![Webhook retries dashboard view](_images/6acaf77c60e71aa0.png)

If your primary webhook URL goes down, specify a failover URL as a backup so Telnyx can send webhook events to the failover URL in the event of an issue with the primary URL.

You can click into the status to view the request and response headers as well as the response payload, which might help indicate further issues. In the example below, a successful 200 response is shown.

![Request and response header example](_images/3edb8875ca1f41d1.png)

### Best Practices

If your webhook script performs complex logic or makes network calls, the script may time out before Telnyx sees its complete execution. For that reason, you may want to have your webhook endpoint immediately acknowledge receipt by returning a `2xx` HTTP status code, and then perform the rest of its duties.

Webhook endpoints may occasionally receive the same event more than once. Guard against duplicated event receipts by making your event processing idempotent — for example, by logging the events you've processed and not processing already-logged events. Additionally, verify webhook signatures to confirm that received events are being sent from Telnyx.

Telnyx signs the webhook events it sends to clients so that the authenticity of the request can be verified. Webhook signing in API V2 uses public key encryption. Telnyx stores a public-private key pair and uses the private key to sign the payload. The public key is available in the Mission Control Portal under account settings in the left-hand navigation bar > Keys & Credentials > Public Key sub tab.

The signature for the payload is calculated by building a string that is the combination of the timestamp of when the request was initiated, the pipe `|` character, and the JSON payload. The signature is then Base64 encoded:

```
Base64.encode64("#{timestamp}|#{payload}")
```

The signature (Base64 encoded) and the timestamp (in Unix format) are assigned to the request headers `telnyx-signature-ed25519` and `telnyx-timestamp` respectively. You can then use cryptographic libraries in your language of choice to verify the signature using the public key. Examples are available in the [telnyx-python](https://github.com/team-telnyx/telnyx-python/blob/master/telnyx/webhook.py), [telnyx-ruby](https://github.com/team-telnyx/telnyx-ruby/blob/master/lib/telnyx/webhook.rb), and [telnyx-node](https://github.com/team-telnyx/telnyx-node/blob/master/lib/Webhooks.js) repositories.
