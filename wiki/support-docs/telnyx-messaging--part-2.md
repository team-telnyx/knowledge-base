---
title: Telnyx Messaging
summary: A consolidated guide to Telnyx messaging capabilities, covering SMS and MMS
  sending and receiving, messaging profile configuration, Zapier-based automations,
  third-party integrations, bulk and group messaging, and frequently asked questions
  about MMS limits, file types, and delivery behavior.
sources:
- url: https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving
- url: https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number
- url: https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier
- url: https://support.telnyx.com/en/articles/3270136-telnyx-global-sims-faqs
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
- url: https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number
- url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
- url: https://support.telnyx.com/en/articles/7885470-chiro8000-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
updated_at: 2026-08-05T13:35:00Z
---

# Telnyx Messaging

*Part 2 of 3 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 3](telnyx-messaging--part-3.md)*

A consolidated guide to Telnyx messaging capabilities, covering SMS and MMS sending and receiving, messaging profile configuration, Zapier-based automations, third-party integrations, bulk and group messaging, and frequently asked questions about MMS limits, file types, and delivery behavior.

## MMS FAQs

### Character Limits

MMS allows significantly more characters than SMS — many carriers accept several thousand characters per message. The exact limit varies by carrier and device, and the total size is constrained by the multimedia content as well as the text.

### Content Type for Stored Media

The `content-type` should match one of the supported MIME types listed above. `application/octet-stream` is also accepted, in which case Telnyx attempts to infer the type from the binary content.

### Media Caching

Outbound media files are cached by Telnyx for one hour. Appending a spurious query parameter to the URL invalidates the cache.

### Securing Media

To restrict media access to Telnyx only, whitelist the IPs **192.76.120.192** and **192.76.120.193**.

### Cross-Border MMS

MMS between countries (for example, USA to Brazil) is not currently supported. Telnyx is exploring international MMS and developing a Rich Communication Services (RCS) product, expected to enter beta by the end of 2024 or early Q1 2025.

### Delivery Receipts (DLRs)

Three DLRs are typically generated for each MMS:

1. **Internal DLR** — generated when Telnyx successfully submits the MMS to the terminating carrier; status becomes `sent`.
2. **MM4_forward.RES** — received when the terminating carrier passes the message to the destination carrier; status becomes `delivered`.
3. **MM4_delivery_report.REQ** — sometimes received from the destination carrier, indicating handset delivery.

### MMS from Toll-Free Numbers

MMS can be sent from toll-free numbers at a rate limit of 1,200 messages per minute. Account-wide limits (15 messages per second) also apply.

### MMS from Short Codes

A short code must be provisioned with Telnyx's terminating carriers, and the campaign must be approved by all major carriers.

### Long Text as MMS

To send a long text message as MMS without attachments, set the parameter `type=MMS`.

### SMS Treated as MMS

If `media_urls` is included in the request, the message is treated as MMS even if the array is empty. Only include `media_urls` when you intend to send MMS.

### MMS Fallback

When enabled on the messaging profile, MMS Fallback automatically converts an MMS into an SMS with each media URL appended on a separate line if the destination does not support MMS. Webhooks indicate the protocol used (`sms` for fallback, `mms` otherwise). See the [MMS Converter API docs](https://developers.telnyx.com/docs/messaging/messages/mms-converter).

### MMS Transcoding

When enabled, MMS Transcoding resizes images and videos to meet destination carrier size limits, allowing MMS up to 5 MB. Images are converted to JPEG and videos to H.264 MP4. Animated GIFs are not transcoded and must be sent at a small enough size. See the [MMS Transcoding API docs](https://developers.telnyx.com/docs/messaging/messages/mms-transcoding).

## Group Messaging (Bulk MMS)

Group Messaging is built on the MMS protocol and supports multi-party conversations for +1 numbers in the US and Canada. It is available only via the API V2 `group_mms` endpoint and supports up to 8 recipients per conversation.

Example request:

```
curl -i -X POST \
https://api.telnyx.com/v2/messages/group_mms \
-H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
-H 'Content-Type: application/json' \
-d '{
"from": "+13125790427",
"to": ["+18655551234", "+13125551234"],
"text": "Greetings from Telnyx!",
"media_urls": ["http://placekitten.com/320/240"]
}'
```

Behavior and limitations:

- An individual webhook status update is delivered per recipient following the V2 schema.
- Inbound and outbound delivery webhooks list all participants of the group message.
- Handset delivery status is `unknown` for non-Telnyx recipients.
- Individual message detail records are cut per recipient in the portal and reporting APIs.
- A `group_message_id` attribute correlates each record to the overarching group conversation, returned via API response, webhooks, and detail records.
- Group messaging is charged per recipient at standard MMS rates plus carrier passthrough fees.
- Only US/Canadian destinations are supported, and only long codes — toll-free and short code are not supported.
- Standard MMS protocol limitations apply.

Ensure your messaging profile uses a V2 webhook version to receive inbound group messages.

## Zapier Automations

Zapier can be used to build no-code automations on top of Telnyx messaging. Connect your account at the [Telnyx Zapier integration page](https://zapier.com/apps/telnyx/integrations) using an API V2 key. Best practice: attach only a single number to any messaging profile used for Zaps, since all messages to numbers on that profile will trigger the Zap.

### Forwarding SMS to Your Mobile Number

Create a Zap with **Telnyx > Receive a Message** as the trigger and **Telnyx > Send SMS** as the action. Configure:

- **Source Number** — your Telnyx number in E.164 format (e.g., `+14155551234`).
- **Destination Number** — your personal mobile number in E.164 format (e.g., `+13105559876`).
- **Message Content** — a template such as `FWD FROM: [From Phone Number] BODY: [Text]`, using Zapier variables from the trigger.

Test the action, then publish the Zap. For US long codes, ensure 10DLC registration is complete.

### Automated Replies

Use the same trigger/action pattern, but set the **Destination Number** to the `From Phone Number` variable so the reply goes back to the original sender. Enter your desired auto-reply text in **Message Content**. For US destinations, ensure your number is associated with a registered 10DLC campaign and an active messaging profile.

### Forwarding Texts to Email

> **Note:** As of the source publication, the "Receive a Message" Zap trigger is outdated and the steps in this article do not currently function. Telnyx is working on a fix.

The intended flow is: **Telnyx > Receive a Message** trigger, then an email provider (e.g., Gmail) **Send an Email** action. Copy the webhook URL Zapier provides and assign it to your Telnyx messaging profile. Send a test SMS to your Telnyx number so Zapier can capture a sample payload. Configure the email action with `To`, `Subject`, and a body containing `From`, `To`, and `Body` Zapier variables, then publish.
