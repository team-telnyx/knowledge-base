---
title: 'MMS on Telnyx: Send, Receive, Transcode, and Fallback'
summary: 'A practical guide to building reliable MMS on Telnyx: how to send and receive
  media, supported formats and carrier limits, automatic transcoding, SMS fallback
  via the MMS converter, SMIL layout options, webhook handling, troubleshooting, delivery
  tracking, and related considerations like smart encoding, short codes, hosted SMS,
  and international compliance.'
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
  content_hash: c1170108efe8f40ee053818783b267e8bb09f4e7fed4f60a6772d66aa4d1f05e
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
  content_hash: ca095990aab836d2aa3b4f9e5d33b71d0a15de17a380e9ab0141a27ded30593e
- url: https://developers.telnyx.com/docs/messaging/messages/send-receive-mms/index
  content_hash: 9ce0ee8a34ff4b8c1c3576db4cd783008cd6dc35cbb9fa75f2eae9210858a7b5
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
  content_hash: 068dc6b892add243aca5da3612d51f14007aef5eb40a4bc86fb405e612c9c722
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
  content_hash: 8450fe5d7671f1b21ac17858f82dcdeebf73c51a20e389c91e3e7e67fcada5b5
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer
  content_hash: 9111d04c7a75618918cdd448b825331907871740c1e083ac4da72dede23751b1
- url: https://developers.telnyx.com/docs/messaging/messages/short-code/index
  content_hash: ce0868cc920695f42f990988e96ade435a00e8c1f09c27133e6b85a49788b70e
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
  content_hash: 13c9c1044f0ca315e13a70869adfb590e562b27586a9babf623a7bf209edb32c
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
  content_hash: 673d56a70d91c759b3fbe582e917295110576bf1d00ed51c06c003008930ec74
- url: https://developers.telnyx.com/docs/messaging/messages/smart-encoding/index
  content_hash: 7d1cc8891283c44da700350819b3d567cef37fe8c86925c6dd41fffcc05948a5
updated_at: 2026-05-20T09:03:49Z
---

# MMS on Telnyx: Send, Receive, Transcode, and Fallback

A practical guide to building reliable MMS on Telnyx: how to send and receive media, supported formats and carrier limits, automatic transcoding, SMS fallback via the MMS converter, SMIL layout options, webhook handling, troubleshooting, delivery tracking, and related considerations like smart encoding, short codes, hosted SMS, and international compliance.

## Supported senders and coverage

- MMS is supported on US/Canada Long Code (10DLC), Toll-Free, and Short Code numbers. International MMS support varies by carrier and destination.
- You can enable messaging (SMS/MMS) for many existing landlines and business numbers without moving voice by using [Hosted SMS](hosted-sms.md).
- Short codes support MMS and provide the highest throughput; see [Short Codes](short-codes.md).

## Compose and send MMS

- Include one or more publicly accessible media URLs via the `media_urls` array. Up to 10 URLs are allowed per message.
- You can include text with your media via the `text` field.
- Media is fetched at send time; URLs must be reachable (no authentication), fast to respond, return the correct Content-Type, and ideally use HTTPS.

See end-to-end examples and SDK snippets in [Send & Receive MMS](send-receive-mms.md).

## Handle inbound MMS and media storage

- Inbound MMS arrives via webhooks (e.g., `message.received`). Attachments appear in a `media` array with `url`, `content_type`, and `size`.
- Inbound media URLs are ephemeral. Download and store important media immediately (e.g., your own S3/GCS bucket). [Send & Receive MMS](send-receive-mms.md) includes sample handlers and storage patterns.

## Supported media and size limits

- Images: JPEG, PNG, GIF, BMP, TIFF, WebP (broadest carrier support)
- Video: MP4, 3GP, MOV (H.264 recommended)
- Audio: MP3, WAV, AMR, OGG (limited carrier support)
- Documents: PDF, vCard (.vcf), iCal (.ics) (limited carrier support)
- Animated GIFs are not transcoded automatically; ensure they are under the carrier limit.

Carrier size limits vary by carrier and sender type. A safe universal target is 600 KB total media to maximize deliverability across carriers. For details and a carrier matrix, see [MMS Media & Transcoding](mms-media-transcoding.md).

## Automatic MMS transcoding

- Enable automatic resizing and format adjustment with the `mms_transcoding` setting on your messaging profile.
- How it works: Telnyx detects the destination carrier’s limit, then resizes media to fit — images to JPEG, videos to H.264 MP4.
- Transcoding can reduce quality; pre-optimizing your media (e.g., images ~640×480 at ~80% JPEG quality, short videos targeting 480p and under ~600 KB total) gives you more control.

Configuration and best-practice guidance: [MMS Media & Transcoding](mms-media-transcoding.md).

## MMS converter: fallback to SMS

- When the destination cannot receive MMS, enable fallback with `mms_fall_back_to_sms` on your messaging profile.
- If fallback occurs, Telnyx sends an SMS: the message body (if any), followed by each media URL on its own line. No shortlinking or transformation of your URLs is applied.
- Delivery webhooks reflect the actual protocol used (e.g., the MDR/webhook will indicate SMS if fallback occurred).

Examples of what recipients see when fallback happens:
- Body + one URL: your text, then the exact media URL on the next line.
- Body + multiple URLs: your text, then each media URL on its own line.
- Only media: just the URL(s), one per line.

See feature behavior and enablement in [MMS converter](mms-converter.md).

## Customize layout with SMIL templates

- Telnyx auto-generates SMIL based on `text` and `media_urls`. Advanced users can supply `smil_template` to define layout and timing.
- Use placeholders like `{{ text }}`, `{{ 0 }}`, `{{ 1 }}` to reference message text and media by index.
- The template must be JSON-escaped when set in the API request.
- Many modern handsets (notably iPhones) ignore SMIL and render using their own layout.

Details and examples: [Specifying SMIL Template](specifying-smil-template.md).

## Best practices for reliable MMS

- Optimize media before sending to stay within carrier limits and control quality.
- Keep total media ≤600 KB to maximize cross-carrier delivery (or enable transcoding).
- Host media at fast, publicly accessible HTTPS URLs with correct Content-Type headers.
- Download inbound media immediately; Telnyx-hosted URLs expire.
- If your message is text-only, prefer SMS for lower cost, faster delivery, and fewer failure points.

Additional guidance in [MMS Media & Transcoding](mms-media-transcoding.md) and [Send & Receive MMS](send-receive-mms.md).

## Troubleshoot common MMS issues

- Recipient received SMS instead of MMS
  - Cause: Destination carrier/handset doesn’t support MMS or the media URL was unreachable.
  - Fix: Verify public reachability of media; confirm the recipient supports MMS; check MDR/webhooks to see if fallback or a failure occurred.
- Media too large — rejected or fails
  - Cause: Total media exceeds the carrier limit.
  - Fix: Pre-compress to ≤600 KB total, reduce dimensions/bitrate, or enable `mms_transcoding`.
- Inbound media URL returns 404
  - Cause: Ephemeral links expired.
  - Fix: Download and store immediately upon webhook receipt.
- MMS not supported on my number
  - Cause: Sender type/number capability.
  - Fix: Use a US/Canada Long Code, Toll-Free, or Short Code with MMS enabled on your profile; consider [Hosted SMS](hosted-sms.md) for landlines.

For deep diagnostics and error codes, consult [Message Detail Records](message-detail-records.md).

## Track delivery with Message Detail Records

- Each message has an MDR with status, metadata, cost, and any errors.
- Outbound statuses include `queued`, `sent`, `delivered`, and terminal failures (e.g., `failed`, `gw_timeout`, `dlr_timeout`).
- Costs may be null immediately after send; final costs arrive with the `message.finalized` webhook.
- Prefer webhooks (`message.sent`, `message.delivered`, `message.finalized`) over polling.

Schema, statuses, and best practices: [Message Detail Records](message-detail-records.md).

## How SMS smart encoding relates to MMS

- Smart encoding affects SMS only (MMS/RCS use UTF-8 by default). It replaces certain Unicode characters with GSM-7 equivalents to reduce segment count and cost.
- This matters when MMS fallback sends as SMS: enabling profile-level `smart_encoding` can prevent unexpected multi-part SMS costs due to curly quotes, em dashes, etc.
- You can override per message with the `encoding` parameter (`auto`, `gsm7`, `ucs2`).

Learn more in [Smart Encoding](smart-encoding.md).

## Short codes and MMS at scale

- Short codes support MMS with the highest A2P throughput (up to ~1,000 MPS) and strong carrier trust.
- They require application and carrier certification (weeks-long process) and must support standard keywords (STOP/HELP). Telnyx manages required keyword handling; STOP cannot be disabled.

Provisioning, use cases, and compliance: [Short Codes](short-codes.md).

## Hosted SMS numbers and MMS

- [Hosted SMS](hosted-sms.md) lets you add SMS/MMS to numbers that stay with your current voice provider (hosting is not porting). Typical flow: eligibility check, order creation, ownership verification, document upload, Telnyx review.
- If numbers already belong to another Telnyx account, the order is treated as an [Internal Hosted SMS Transfer](internal-hosted-sms-transfer.md) with a 72-hour approval window for the current owner.

## International considerations for MMS

- International MMS support varies by carrier; confirm capabilities per destination.
- For SMS to international destinations, ensure sender type, consent, opt-out language, quiet hours, and any pre-registration (e.g., India DLT, France OACP, Singapore SSIR) are in place.
- US/Canada do not support alphanumeric sender IDs; use 10DLC, Toll-Free, or Short Code.

Country requirements and best practices: [International SMS Compliance Guide](international-sms-compliance-guide.md).
