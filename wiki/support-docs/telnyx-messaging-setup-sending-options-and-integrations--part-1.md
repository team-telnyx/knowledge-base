---
title: 'Telnyx Messaging: Setup, Sending Options, and Integrations'
summary: 'A practical guide to get Telnyx messaging ready end‑to‑end: prepare your
  account, create and assign a Messaging Profile, test and send via the Portal, API,
  SDKs and no‑code tools, understand porting/hosted SMS nuances, and review key compliance
  and feature controls.'
sources:
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
  content_hash: aa34ff90f76a15ee7d2bf9af5180bf966364481c0a299655356bbb9d403c4bf3
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
  content_hash: 2f8418ab1159e3217d2cf5825a9b2bfe2f0d52942276a8bc19a9dcfbcbefe09f
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
  content_hash: 00e98248fa9d6b2033e21916ed13907c44587f73fadcdd3e2105b5252a79cbed
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
  content_hash: be9ea16aa3592c7fe80c95d0197798698ee6b0bdfee29a186f5dc1c93f3d06bf
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
  content_hash: 7ad9572a930d73ff6f3dbddab1b36e4155ae7327dc84fc3d8e0460cb2f5b6b96
- url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
  content_hash: 22cfd8f20e858a82a4ed5c8e3bb0c530391fc56c387439433ca9085d5672cd8f
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
  content_hash: 90ddeba650dcedf970a636ed3f72761d545049909ab66b77e2451cedfa4d70a1
- url: https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control
  content_hash: e656a0304e86302b75eaa282824b9e5228425d0014923ab6bc949d058b5d20c1
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
  content_hash: 62f4c57ce8f57d37bf054374b009d9af17a5571928f93124406909a2068989e8
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
  content_hash: 7a0853f155d617c9da2a4baf20765126a5208ed52cbdf6f6ba01b10dc843867a
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
  content_hash: 7de41c4cff709c280eb160524c8299a8efbdbab5bc91bb4a0b270fb42cfbd65f
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
  content_hash: da9316aca19025388915c0c695c93c6d08af42d3f1bc20f0d4e5b0dcbad1b1e7
- url: https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow
  content_hash: 9305c7d07dada70a40def46178ac551ae7d8f5886edfa1890b955cd680bb8282
- url: https://support.telnyx.com/en/collections/133103-telnyx-sms-guide
  content_hash: a45ce6e0d88c4ef16226913a8d21ec716b713173a849a20ad5c7e320ec6b9313
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
