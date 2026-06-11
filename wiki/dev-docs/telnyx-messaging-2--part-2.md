---
title: Telnyx Messaging
summary: Telnyx Messaging provides APIs and infrastructure for sending and receiving
  SMS, MMS, and RCS messages globally. This page covers phone number configuration,
  messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international
  compliance, and RCS with AI integration.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
  content_hash: d98fde358c8bb0a6117412a2971da4898405065ec7c3650984ae9a6494d9dcd3
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
  content_hash: 192a65ec89e4ea6a7be165a7b17a5e44f6ecd3121b756cc292aebd63a50fee49
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
  content_hash: e691bcb40f682bbc7d1087d2755ac4c3680e9cf93520f97c0d86645ab7657ad4
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
  content_hash: 458a86b8e1297624173a766ba456ed0768c0cb62eb8d60575ce3367c8625c318
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
  content_hash: 362df72c3dbe5bdfb19da2c433895133466aa88bd4ab4737f7754ecf0892fa18
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
  content_hash: f170f09f5d980d0e492e300a0e07ce6b1591881c60d71f8f506f2a02ad2cc34b
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
  content_hash: 62bd8025784ec0901f20d6bc1597886e9df41722271dcc11c7b8d8a86d2c94a1
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration/index
  content_hash: c088661a2d1c9ce8faaf92b86e072d0951aa7bf6301ed3bc75f1825e75c5b505
- url: https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index
  content_hash: 33d60e88cce1298b6009415cd6dc5afb26a05430927e0b5e286cd9ec8770efaa
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
  content_hash: 6adf9a29c630ce93d9fd16b676d2d2df67db1a1772c5e97c9e33646f6597ec0f
updated_at: 2026-06-11T10:38:14Z
---

# Telnyx Messaging

*Part 2 of 5 — see also: [Part 1](telnyx-messaging-2--part-1.md), [Part 3](telnyx-messaging-2--part-3.md), [Part 4](telnyx-messaging-2--part-4.md), [Part 5](telnyx-messaging-2--part-5.md)*

Telnyx Messaging provides APIs and infrastructure for sending and receiving SMS, MMS, and RCS messages globally. This page covers phone number configuration, messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international compliance, and RCS with AI integration.

## Message Encoding

SMS messages are encoded into segments of 140 bytes each. Billing is per segment, so understanding encoding is key to controlling costs.

| Encoding | Bits per char | Single segment | Multi-part segment |
|---|---|---|---|
| GSM 7-bit | 7 | 160 chars | 153 chars |
| ASCII 7-bit | 7 | 160 chars | 153 chars |
| ASCII 8-bit | 8 | 140 chars | 134 chars |
| UTF-16 | 16 | 70 chars | 67 chars |

A single non-GSM-7 character (like an emoji or curly quote) switches the **entire message** to UTF-16, cutting capacity from 160 to 70 characters per segment — potentially more than doubling costs.

### How segments work

Every SMS is transmitted in 140-byte units. Multi-part messages add a 6-byte User Data Header (UDH) to each segment for reassembly:

- **GSM-7**: ≤160 chars → 1 segment; >160 chars → ⌈chars / 153⌉ segments (max 10)
- **UTF-16**: ≤70 chars → 1 segment; >70 chars → ⌈chars / 67⌉ segments (max 10)

### Encoding by sender type

| Sender type | Default encoding | Fallback |
|---|---|---|
| Long Code | GSM 7-bit | UTF-16 |
| Toll-Free | GSM 7-bit | UTF-16 |
| Short Code | ASCII 7-bit | UTF-16 |
| Alphanumeric | GSM 7-bit | UTF-16 |

MMS and RCS messages use UTF-8 and are not affected by these limits.

### GSM-7 character set

Standard characters count as 1 character each. Extended characters (tilde `~`, circumflex `^`, pipe `|`, backslash `\`, curly brackets `{}`, square brackets `[]`, euro sign `€`) count as **2 characters** each because they require an escape sequence. A message with 155 standard characters and 3 pipe characters uses 155 + (3 × 2) = 161 character slots, requiring 2 segments.

### Common encoding issues

- **Unexpected UTF-16**: Curly quotes, em dashes, and ellipses from word processors force UTF-16. Enable [Smart Encoding](smart-encoding.md) or manually replace them.
- **Emojis**: Force UTF-16 encoding, and most emojis count as 2 UTF-16 characters (surrogate pairs). Avoid emojis in SMS if cost matters.
- **Extended GSM-7 characters**: Characters like `[]`, `{}`, `|` cost 2 chars each, causing unexpected segment splits.
- **Copy-pasted text**: Word processors often replace straight quotes with curly quotes and hyphens with em dashes. Sanitize input or enable smart encoding.
- **Non-Latin scripts**: Chinese, Arabic, Cyrillic, etc. have no GSM-7 equivalents, so UTF-16 is always used. Plan for higher segment counts or use MMS.
- **Truncated/split messages**: Some older devices may not reassemble messages over 3–4 segments correctly.

### Detecting encoding programmatically

Before sending, check if a message will use GSM-7 or UTF-16 to estimate costs. Test each character against the GSM-7 basic and extended sets. For GSM-7, count extended characters twice and apply segment formulas. For UTF-16, count surrogate pairs (code points > U+FFFF) as 2 characters.

### Encoding best practices

1. Enable [Smart Encoding](smart-encoding.md) on your messaging profile — the single biggest cost-saving measure.
2. Validate segment counts before sending.
3. Sanitize user-generated content to strip or replace invisible Unicode characters.
4. Keep messages under 160 chars (GSM-7) or 70 chars (UTF-16) to avoid multi-part overhead.
5. For messages needing emojis or non-Latin scripts, use MMS or RCS instead of SMS.

## MMS Handling

MMS messages let you send images, videos, and other media alongside text. MMS is supported on long code, toll-free, and short code numbers in the US and Canada. International MMS support varies by carrier.

### Sending MMS

Include one or more `media_urls` in your message request (up to 10 URLs per message). Each URL must be publicly accessible — Telnyx fetches the media at send time.

```
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "from": "+15551234567",
    "to": "+15559876543",
    "text": "Check out this image!",
    "media_urls": ["https://example.com/image.jpg"]
  }'
```

### Supported media types

| Category | Formats | Notes |
|---|---|---|
| Images | JPEG, PNG, GIF, BMP, TIFF, WebP | Most widely supported |
| Video | MP4, 3GP, MOV | H.264 codec recommended |
| Audio | MP3, WAV, AMR, OGG | Limited carrier support |
| Documents | PDF, vCard (.vcf), iCal (.ics) | Limited carrier support |

Animated GIFs are not supported for transcoding and must be under carrier size limits.

### Carrier size limits

| Carrier | Long Code | Toll-Free | Short Code |
|---|---|---|---|
| AT&T | 1 MB | 600 KB | 600 KB |
| T-Mobile | 1.5 MB | 600 KB | 1 MB |
| Verizon | 1 MB | 600 KB | 1.2 MB |

The safe maximum across all carriers and sender types is **600 KB**.

### Automatic transcoding

When `mms_transcoding` is enabled on your messaging profile, Telnyx automatically resizes oversized media to comply with carrier limits. Images are converted to JPEG and videos to H.264 MP4. Animated GIFs are not resized. Enable it via API or in the portal under your messaging profile settings.

For best results, pre-optimize media: resize images to 640×480 or smaller (JPEG at 80% quality), compress videos to H.264 under 30 seconds at 480p, and target under 600 KB total.

### MMS Converter (fallback to SMS)

When `mms_fall_back_to_sms` is enabled on a messaging profile, MMS messages to destinations that don't support MMS are automatically converted to SMS. The text body is preserved and media URLs are appended on separate lines. Webhooks indicate the actual protocol used (SMS or MMS). This is not enabled by default.

### MMS best practices

- Ensure media URLs are publicly accessible, return correct `Content-Type` headers, use HTTPS, and respond quickly.
- Download and store inbound MMS media immediately — webhook URLs are ephemeral.
- Use SMS for text-only messages (cheaper, faster, more reliable).
