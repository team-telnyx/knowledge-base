---
title: 'Telnyx Messaging: Setup, Sending Options, and Integrations'
summary: 'A practical guide to get Telnyx messaging ready end‑to‑end: prepare your
  account, create and assign a Messaging Profile, test and send via the Portal, API,
  SDKs and no‑code tools, understand porting/hosted SMS nuances, and review key compliance
  and feature controls.'
sources:
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
- url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
- url: https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
- url: https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow
- url: https://support.telnyx.com/en/collections/133103-telnyx-sms-guide
updated_at: 2026-05-20T14:28:29Z
---

# Telnyx Messaging: Setup, Sending Options, and Integrations

*Part 1 of 2 — see also: [Part 2](telnyx-messaging-setup-sending-options-and-integrations--part-2.md)*

A practical guide to get Telnyx messaging ready end‑to‑end: prepare your account, create and assign a Messaging Profile, test and send via the Portal, API, SDKs and no‑code tools, understand porting/hosted SMS nuances, and review key compliance and feature controls.

## Prerequisites and account setup
- Verification and billing: Ensure Level 1 Verification is complete (required to assign messaging to numbers) and add a payment method so you can buy numbers and send traffic.
- Numbers (DIDs): Buy or port in SMS/MMS‑capable numbers and confirm they show SMS available before purchase. Assign a Messaging Profile to each number you plan to use.
- Traffic type and compliance: Determine if your traffic is A2P or P2P. For US/CA A2P on 10DLC long codes, register brands/campaigns; Toll‑Free requires verification; Short Codes have their own ordering/compliance. Review the Acceptable Use Policy for Messaging.
- Tip: If you see “Not SMS Capable” on a number or get “Could not enable messaging on the number.” when assigning a profile, the number may not support messaging or industry NNID provisioning may still be updating—try again or contact support.

## Create and configure a Messaging Profile
- Create: In Mission Control, go to Programmable Messaging → Add New Profile. API v2 is the default and recommended.
- Inbound settings (required for receiving and delivery updates): Add your webhook URL (HTTP) so Telnyx can deliver inbound messages to your app and send outbound status callbacks. Learn more about webhooks: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
- Outbound controls:
  - Alphanumeric Sender ID: Set a default for one‑way international messaging (typically a business name; not supported for US/CA P2P/A2P long codes).
  - Manage Allowed Destinations: Whitelist international countries to permit or restrict sending (reduces fraud exposure).
  - Number Pooling: Send from a pool of numbers to help with higher volume and better local match behavior. https://support.telnyx.com/en/articles/3154822-number-pooling
  - MMS Fallback: Convert MMS to SMS with a media URL where MMS isn’t supported.
  - MMS Transcoding: Compress images/videos to meet carrier size limits (send MMS up to 5 MB).
  - Daily Spend Limit per connection: Cap daily USD spend for outbound; resets at 00:00:00 UTC. https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits
- Save the profile, then locate the profile’s Unique ID in its settings when needed.
- Assign to numbers: Numbers → My Numbers → edit the Messaging Profile column and select your profile.
- Security update (effective Mar 1, 2024): New or edited profiles must specify whitelisted destination countries, and a default Alphanumeric Sender ID is required when attempting non‑US termination.

## Quick testing in the Portal (Learn & Build)
Use Learn & Build (Programmable Messaging → Learn & Build) to send a one‑off test without code:
- Ensure you’ve purchased a number and assigned your Messaging Profile.
- Compose a template or free‑form message, set From (your Telnyx number) and To (e.g., your mobile), optionally add an image, then Send.
- The Raw Response pane shows webhook payload details sent to your profile’s webhook URL.

## Send messages via the API (Postman or code)
- API v2 (recommended): POST to https://api.telnyx.com/v2/messages with Authorization: Bearer YOUR_API_KEY. Include fields such as from (your Telnyx number), to (E.164 destination), text (message body), and optionally media_urls for MMS.
- API v1 (legacy): POST to https://sms.telnyx.com/messages using the x-profile-secret header and a body that includes from, to, and body.
- Get an API key in Mission Control: https://portal.telnyx.com/#/app/api-keys
- Postman how‑to: https://developers.telnyx.com/docs/messaging/messages/mission-control-portal-set-up and error reference: https://developers.telnyx.com/api/errors

## Receive messages and delivery updates
- Set a webhook URL on your Messaging Profile to receive inbound messages and outbound status callbacks.
- Your application should acknowledge Telnyx webhooks and process the event payloads (v2 schema recommended for new builds).

## Use the Python SDK (send/receive)
- Send: Video walk‑through using the Telnyx Python SDK to send a text: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
- Receive: Video walk‑through for receiving an inbound text via SDK/webhooks: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
- Developer docs and setup: https://developers.telnyx.com/

## Send in bulk from Google Sheets (no servers)
- Build a simple Google Apps Script that iterates rows and calls the v2 Messages API with your API key, From number, and per‑row destinations/text.
- This approach updates a Status column per send and is ideal for small lists/prototypes. Guide: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
- Note: For some international destinations, the From may be replaced by an Alphanumeric Sender ID. Details: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id

## Group MMS (multi‑party) messaging
- Start multi‑party conversations over MMS to up to 8 recipients (US/CA long codes only). Charged per recipient.
- v2 only; make sure your profile uses v2 webhooks to receive inbound group messages.
- You’ll get a webhook per recipient; a group_message_id lets you correlate records. Handset delivery status is unknown for non‑Telnyx recipients.
- Docs and example: https://developers.telnyx.com/docs/messaging/messages/group-messaging

## No‑code forwarding with Telnyx Flow
- Build a drag‑and‑drop workflow to forward inbound SMS/MMS from your Telnyx number to a mobile number.
- Typical pattern: Inbound Message → Switch (SMS/MMS) → Send Message (forward). You can invert From/To or set a fixed From.
- Requires numbers enabled for messaging and assigned to an approved 10DLC campaign for US long‑code A2P use. Guide: https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow

## Integrate with Textable
- In Textable signup, choose Telnyx V2 as the provider, set your DID, and leave Account ID blank.
- Create a Telnyx Messaging Profile with Inbound Protocol HTTP and set the webhook URL to https://app01.textable.co/receive?provider=telnyxv2
- Create an API v2 key in Mission Control and paste into Textable’s Access Token.
- Assign your number’s Messaging Profile to this profile and save. Guide: https://support.telnyx.com/en/articles/3685327-textable-setup-guide

## Zapier integration status (forward to email)
- Telnyx’s Zapier “Receive a Message” trigger is currently outdated and not functioning; Telnyx is working on a fix. If/when available, the flow is: create a Zap with Telnyx → Receive a Message, copy Zapier’s webhook URL into your Messaging Profile, test, then add an email action (e.g., Gmail) to forward message details. Guide and status note: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
- Consider Telnyx Flow for no‑code message forwarding while Zapier is being updated.

## Ported numbers: SMS routing and timing
- Voice and SMS porting are separate. NNID controls SMS routing for US/CA local and toll‑free.
- At FOC, the losing carrier should release NNID so SMS follows voice; occasionally they delay or block.
- Typical activation times: ~90% of US/CA locals within 10 minutes; remaining in 1–2 business days. Toll‑free: usually within 10 minutes, but if delayed, 4–5 business days.
- If SMS fails after voice ports, confirm the number has a Messaging Profile assigned; then open a support ticket if issues persist.
- Developer visibility into messaging porting: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
- Overview: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
