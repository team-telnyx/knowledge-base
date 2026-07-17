---
title: Telnyx Wireless and Messaging Reference
summary: A consolidated reference covering Telnyx eSIM setup (QR code and manual activation),
  manual IMSI selection, SIM connectivity logs and wireless connectivity states, SIM
  data limits and notifications, SIM theft prevention via IMEI authorization, MMS
  sending/receiving with FAQs, group messaging, bulk messaging via Google Sheets,
  number pooling, and the international voice spend limit.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
- url: https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving
- url: https://support.telnyx.com/en/articles/3154822-number-pooling
- url: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
- url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
- url: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs
- url: https://support.telnyx.com/en/articles/5761437-sim-card-theft-prevention
- url: https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code
- url: https://support.telnyx.com/en/articles/8228452-email-notification-international-spend-limit
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
- url: https://support.telnyx.com/en/articles/9183726-manual-imsi-selection-on-telnyx-sim
updated_at: 2026-07-17T08:59:32Z
---

# Telnyx Wireless and Messaging Reference

*Part 2 of 4 — see also: [Part 1](telnyx-wireless-and-messaging-reference--part-1.md), [Part 3](telnyx-wireless-and-messaging-reference--part-3.md), [Part 4](telnyx-wireless-and-messaging-reference--part-4.md)*

A consolidated reference covering Telnyx eSIM setup (QR code and manual activation), manual IMSI selection, SIM connectivity logs and wireless connectivity states, SIM data limits and notifications, SIM theft prevention via IMEI authorization, MMS sending/receiving with FAQs, group messaging, bulk messaging via Google Sheets, number pooling, and the international voice spend limit.

## SIM Data Limits and Notifications

To prevent bill shock from excessive data usage, enable data limits on SIM cards and SIM groups. When consumption reaches 80% of the limit, the organization owner receives an email alert. When the data limit is reached, another email alert is sent and the related SIMs are disabled to prevent further consumption.

### SIM group data limits

1. Log into [SIM Groups](https://portal.telnyx.com/#/wireless/sim-groups).
2. Click on a SIM Group and scroll to the data section.
3. Click **Custom** and input the preferred data limit.

### Individual SIM card data limits

1. Log into [SIM Cards](https://portal.telnyx.com/#/wireless/sim-cards).
2. Click on a SIM Card and scroll to the data section.
3. Click **Custom** and input the preferred data limit.

### Data usage notifications

1. **Establish a notification profile:** Navigate to the [Notification Setup](https://portal.telnyx.com/#/advanced-features/notifications) page and define a notification profile.
2. **Select a notification channel:** Create a notification channel and choose from SMS, Voice, Email, or Webhook.
3. **Configure notification settings:** Select **Data Usage Notifications** as the preferred notification type.
4. **Link the notification profile to the SIM card:** Assign the profile to the **Usage Notification Threshold** section of the SIM card.

Once configured, alerts are sent from portal@telnyx.com when data usage reaches the predefined threshold.

## SIM Card Theft Prevention

Add up to 5 authorized IMEIs to SIMs in a SIM fleet to ensure they can only be used by authorized devices. An [IMEI (International Mobile Equipment Identity)](https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity) is a unique identifier for a mobile device. SIM cards can be configured to auto-disable when an unauthorized IMEI is recognized, via the SIM Card drill-down section.

Allow up to 5 minutes for SIM cards to be disabled after an unauthorized IMEI is recognized. An email is dispatched to the account when this occurs. If no authorized IMEIs are added, all devices are considered authorized (the default configuration).

## MMS Sending and Receiving

Telnyx supports sending and receiving MMS messages through API V1 and API V2. See the [Sending SMS and MMS Quick Start Guide](https://developers.telnyx.com/docs/messaging/messages/send-message) and [Receiving SMS and MMS Quick Start Guide](https://developers.telnyx.com/docs/messaging/messages/receive-message) for setup.

### Sending MMS

API V1 example:

```
curl --request POST 'https://sms.telnyx.com/messages' \
--header 'Accept: application/json' \
--header 'x-profile-secret: v1 messaging profile secret' \
--header 'Content-Type: application/json' \
--data-raw '{
  "from": "+your purchased number",
  "to": "+the number you want to message",
  "body": {
    "delivery_status_webhook_url": "your webhook url",
    "text": "Did you get this image?",
    "subject": "Bear Picture",
    "media_urls": [
      {"img": "https://placebear.com/802/503.jpg"}
    ]
  }
}'
```

API V2 example:

```
curl --request POST 'https://api.telnyx.com/v2/messages' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer API V2 KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "from": "+your purchased number",
  "to": "+the number you want to message",
  "webhook_url": "your webhook url",
  "text": "Did you get this image?",
  "subject": "Bear Picture",
  "media_urls": ["https://placebear.com/802/503.jpg"]
}'
```

### Supported file types and sizes

Supported MIME types include `text/plain`, `text/vcard`, `image/jpeg`, `image/png`, `image/gif`, `video/3gpp`, and `video/mp4`.

Maximum attachment size varies by carrier tier:

- Tier 1 (Verizon, T-Mobile, AT&T, Sprint): up to 1 MB
- Tier 2: up to 600 KB
- Tier 3: up to 300 KB

Total message size is capped at 1 MB, with no more than 10 `media_urls` allowed. By default, accounts are limited to 1 MMS message per second; contact [sales@telnyx.com](mailto:sales@telnyx.com) to increase this limit. Use the [number lookup service](https://developers.telnyx.com/docs/identity) to discover the carrier for a phone number.

### Receiving MMS

A DID's settings determine whether the number is SMS or MMS capable (indicated by a checkmark). It is up to the user to distinguish MMS and SMS messages arriving at the webhook; one way is to check the `Content-Type` header (it will be `multipart/form-data` for MMS).

## MMS FAQs

### Character limits

MMS allows a significantly higher number of characters per message than SMS, with no standardized limit. Many carriers allow several thousand characters per message. Limits depend on the carrier and device, ranging from 300 KB to over 1 MB per message including both text and multimedia content.

### Content type and caching

The content type should match one of the supported MIME types, or `application/octet-stream` (in which case Telnyx attempts to guess the content type from the media binary). Outbound media files are cached within Telnyx for one hour; changing the media URL (e.g. adding a query parameter) invalidates the cache. To restrict media access to Telnyx only, whitelist `192.76.120.192` and `192.76.120.193`.

### International MMS

MMS between countries (e.g. USA to Brazil) is not currently supported. MMS messaging through Telnyx is only supported within the USA and Canada.

### Delivery receipts (DLRs)

Three kinds of DLRs are expected for each MMS:

1. **Internal DLR:** Generated when the MMS is successfully submitted to the terminating carriers. Changes the stored MDR status to "sent".
2. **MM4_forward.RES:** Received when terminating carriers pass the MMS to the destination carrier. Changes the stored MDR status to "delivered".
3. **MM4_delivery_report.REQ:** Sometimes received from the destination carrier, indicating what happened to the message (usually delivered to the handset).

### Toll-free and short-code MMS

MMS can be sent from a Toll-Free Number at a rate limit of 1200 messages per minute, subject to account-wide rate limits (15 messages per second). Sending MMS from a short code requires the short code to be provisioned with terminating carriers and the campaign approved by all major carriers.

### Long-text as MMS

To send a long-text message as MMS with no attachments, set the parameter `type=MMS`. Including the `media_urls` property in a request without attachments will cause an SMS to be treated as an MMS.

### MMS Fallback

When using Telnyx's [MMS converter feature](https://developers.telnyx.com/docs/messaging/messages/mms-converter), if the destination number does not support MMS, the MMS is automatically converted into an SMS message. Webhooks indicate the protocol used: if fallback occurs, the webhook shows that an SMS was sent; otherwise, it shows that an MMS was sent. In fallback cases, the recipient receives an SMS with each media URL from the original MMS displayed on separate lines following the message body.

### MMS Transcoding

The [mms_transcoding](https://developers.telnyx.com/docs/messaging/messages/mms-transcoding) feature adjusts media size to comply with destination carrier and phone number type size requirements. Only images and videos are resized; animated GIFs are not supported and must be sent in a small enough size. Resizing typically reduces media quality. Images are converted to JPEG and videos to H.264 MP4.
