---
title: Telnyx Network, Webhook, and Push Notification Configuration
summary: This page consolidates Telnyx guidance on whitelisting SIP signaling, media,
  and webhook IP addresses; configuring and verifying webhooks (including signature
  rotation); setting up iOS and Android push notifications for the WebRTC SDK; and
  accessing support resources such as the status page, bug reporting, and the Bot-to-Bot
  Knowledge Agent API.
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
- url: https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
- url: https://support.telnyx.com/en/articles/6707731-telnyx-status-page
- url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
- url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
- url: https://support.telnyx.com/en/collections/5782829-webrtc-voice-sdk
updated_at: 2026-08-05T13:24:23Z
---

# Telnyx Network, Webhook, and Push Notification Configuration

*Part 2 of 5 — see also: [Part 1](telnyx-network-webhook-and-push-notification-configuration--part-1.md), [Part 3](telnyx-network-webhook-and-push-notification-configuration--part-3.md), [Part 4](telnyx-network-webhook-and-push-notification-configuration--part-4.md), [Part 5](telnyx-network-webhook-and-push-notification-configuration--part-5.md)*

This page consolidates Telnyx guidance on whitelisting SIP signaling, media, and webhook IP addresses; configuring and verifying webhooks (including signature rotation); setting up iOS and Android push notifications for the WebRTC SDK; and accessing support resources such as the status page, bug reporting, and the Bot-to-Bot Knowledge Agent API.

## Webhook Delivery and IP Whitelisting

A webhook (also called a web callback or HTTP push API) delivers data to other applications in real time as events happen. You can configure webhook URLs on your SIP Connection or Applications (voice, fax, or messaging) to be notified about events Telnyx sends to you.

Webhooks are sent from the IP range of the region where your calls are anchored. The [Guide to SIP AnchorSite Settings](guide-to-sip-anchorsite-settings.md) controls which region your calls can be anchored. If you use an ACL or firewall, whitelist the regional network IP assignments listed above.

### Webhook Source IPs by Region

Telnyx programmable services, including TeXML, Fax, Messaging, and Call Control, deliver webhooks from the following regional IPs. These IPs also apply to WebSocket stream connections, which are typically initiated using the Dial and Start Stream APIs; WebSocket traffic leverages the same delivery infrastructure as webhooks.

- **US**
  - CH1 (US-Central): 192.76.120.128/29
  - DC2 (US-East): 192.76.120.136/29
  - SV1 (US-West): 192.76.120.144/29
- **Europe**
  - LD6 (London, UK): 185.246.41.0/29
  - FR5 (Frankfurt, DE): 185.246.41.8/29
  - AM6 (Amsterdam, NL): 185.246.41.16/29
- **Asia-Pacific (APAC)**
  - SY1 (Sydney): 103.115.244.0/29
  - SG1 (Singapore): 103.115.244.8/29

### Webhook Requirements

For webhooks to work, you need a publicly accessible HTTP server that can receive webhook requests at one or more specified URLs. HTTPS is strongly recommended over HTTP. A walkthrough of setting up a basic application for receiving webhooks is available in the [Telnyx developer docs](https://developers.telnyx.com/docs/messaging/messages/receive-message).

### URL Hierarchy

If webhooks are provided in the request body, those are used; otherwise, if the profile has webhooks, those are used. If neither has webhooks, no webhook delivery is attempted.

### Acknowledging and Retrying Webhooks

To acknowledge receipt of a webhook, your endpoint should return a `2xx` HTTP status code. Any other information returned in the request headers or body is ignored. All response codes outside this range, including `3xx` codes, indicate that Telnyx did not receive the webhook. URL redirection or a "Not Modified" response is treated as a failure.

Webhooks are retried to each of the supplied URLs if your application does not respond within 2000 milliseconds. A timeout typically occurs when the webhook URL endpoint does not return a response; Telnyx times out the original request and retries once more. You can identify a timeout in the [Debugging / Webhook section](https://portal.telnyx.com/#/app/debugging/webhook?enableAlerts=true) of the Mission Control Portal, where a response code of `0` indicates a timeout.

![Webhook retries dashboard view](_images/6acaf77c60e71aa0.png)

If your primary webhook URL goes down, specify a failover URL as a backup so Telnyx can send webhook events to the failover URL when there is an issue with the primary URL. You can click into the status to view the request and response headers as well as the response payload, which can help indicate further issues.

![Request and response header example](_images/3edb8875ca1f41d1.png)

### Webhook Best Practices

If your webhook script performs complex logic or makes network calls, it may time out before Telnyx sees its complete execution. Have your webhook endpoint immediately acknowledge receipt by returning a `2xx` HTTP status code, and then perform the rest of its duties.

Webhook endpoints may occasionally receive the same event more than once. Guard against duplicated event receipts by making your event processing idempotent — for example, by logging the events you have processed and skipping already-logged events. Additionally, verify webhook signatures to confirm that received events are being sent from Telnyx.

### Webhook Signature Verification

Telnyx signs the webhook events it sends to clients so that the authenticity of the request can be verified. Webhook signing in API V2 uses public key encryption. Telnyx stores a public-private key pair and uses the private key to sign the payload. The public key is available in the [Mission Control Portal](https://portal.telnyx.com/#/app/account/public-key) under account settings in the left-hand navigation bar > Keys & Credentials > Public Key sub tab.

The signature for the payload is calculated by building a string that is the combination of the timestamp of when the request was initiated, the pipe `|` character, and the JSON payload. The signature is then `Base64` encoded:

```
Base64.encode64("#{timestamp}|#{payload}")
```

The signature (Base64 encoded) and the timestamp (in Unix format) are assigned to the request headers `telnyx-signature-ed25519` and `telnyx-timestamp` respectively. You can then use cryptographic libraries in your language of choice to verify the signature using the public key. Reference implementations are available in:

- [telnyx-python](https://github.com/team-telnyx/telnyx-python/blob/master/telnyx/webhook.py)
- [telnyx-ruby](https://github.com/team-telnyx/telnyx-ruby/blob/master/lib/telnyx/webhook.rb)
- [telnyx-node](https://github.com/team-telnyx/telnyx-node/blob/master/lib/Webhooks.js)

### Rotating the Webhook Signing Key

If your public key has been compromised, or you want to rotate it as a regular practice, follow the steps in the [Update Webhook Sign Key Guide](update-webhook-sign-key-guide.md).

**Step 1 — Create an inactive public key.** Run the following curl command in a terminal or import it into Postman:

```
curl -X POST https://api.telnyx.com/v2/inactive_key -H "Authorization: Bearer $API_KEY"
```

Replace `$API_KEY` with your Telnyx API V2 key. A successful response looks like:

```
{
    "data": {
        "id": "a896de0d-b250-450d-8ac4-ca901dcc73d6",
        "public": "iGtB96aTJO4SmJPzRPqW20Zc10AWCiN8OQLE5Tg330U=",
        "record_type": "public_key"
    }
}
```

Take note of the `id` field — it is required to activate the key.

**Step 2 — Activate the inactive public key.** When ready to rotate, activate the key created in the previous step:

```
curl -X POST https://api.telnyx.com/v2/inactive_key/a896de0d-b250-450d-8ac4-ca901dcc73d6/activate -H "Authorization: Bearer $API_KEY"
```

The key is referenced by its `id`. A successful activation returns:

```
{
    "data": {
        "result": "success"
    }
}
```

Important notes on rotation:

- Only one inactive key can be added to an organization (managed account). Subsequent requests to create a new inactive key override the previous inactive key.
- Activation of inactive keys is not immediate and can take up to 60 minutes to propagate across the entire account. There is a period of time during which both the current and new keys could be active at the same time.
