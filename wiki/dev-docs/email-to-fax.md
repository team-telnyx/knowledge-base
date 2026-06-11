---
title: Email to Fax
summary: Learn how to build an email-to-fax and fax-to-email workflow with Telnyx
  Programmable Fax. This guide covers prerequisites, Telnyx setup, the sample app
  (Python, Mailgun, AWS S3), webhook configuration, event handling, and tips for sending/receiving
  faxes via API.
sources:
- url: https://developers.telnyx.com/docs/programmable-fax/email-to-fax
- url: https://developers.telnyx.com/docs/programmable-fax/get-started/index
- url: https://developers.telnyx.com/docs/programmable-fax/quickstart
- url: https://developers.telnyx.com/docs/programmable-fax/receive-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/receiving-webhooks
- url: https://developers.telnyx.com/docs/programmable-fax/send-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/sending-commands
updated_at: 2026-05-20T09:25:36Z
---

# Email to Fax

Learn how to build an email-to-fax and fax-to-email workflow with Telnyx Programmable Fax. This guide covers prerequisites, Telnyx setup, the sample app (Python, Mailgun, AWS S3), webhook configuration, event handling, and tips for sending/receiving faxes via API.

## Requirements and Accounts

Before you start, make sure you have:
- A Telnyx account and API key (V2). See [Getting Started with Telnyx Programmable Fax](getting-started-with-telnyx-programmable-fax.md).
- A Telnyx phone number assigned to a Programmable Fax Application.
- An Outbound Voice Profile (required for sending/outbound; not required for inbound). See [Quickstart Guide for Programmable Fax](quickstart-guide-for-programmable-fax.md).
- Ability to receive webhooks (e.g., via ngrok) and a public callback URL.
- Python and pip installed (for the sample app).
- An AWS account with S3 permissions (to store outbound fax media from email attachments).
- A Mailgun account with inbound routes (to accept emails and trigger email-to-fax).

## Configure Telnyx for Programmable Fax

1. Create a Programmable Fax Application and set its webhook URL (temporary ngrok URL works in development). See [Quickstart Guide for Programmable Fax](quickstart-guide-for-programmable-fax.md).
2. Buy or port a phone number and assign it to the Fax Application.
3. Create an Outbound Voice Profile and assign your Fax Application if you plan to send faxes. See [Getting Started with Telnyx Programmable Fax](getting-started-with-telnyx-programmable-fax.md).
4. Generate a V2 API key in the Mission Control Portal for API calls.

Key concepts:
- Connection ID (a.k.a. Application/Connection): routes faxes and ties to your app settings.
- E.164 format: use +<country><number> for all phone numbers (e.g., +13125551234).

## Environment Variables (.env)

The sample app uses environment variables (e.g., via python-dotenv):
- TELNYX_API_KEY: your Telnyx API V2 key
- TELNYX_PUBLIC_KEY: Telnyx public key (for webhook signature verification)
- TELNYX_S3_BUCKET: S3 bucket to upload media attachments
- TELNYX_FAX_CONNECTION_ID: your Fax Application/Connection ID
- MAILGUN_API_KEY: Mailgun API key
- MAILGUN_DOMAIN: Mailgun sending domain
- PORT: app port (defaults to 8000)

Create a .env file and populate these values before running the app.

## Install the Sample App

- Clone the Python demo app that bridges email and fax: https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-fax-email-webinar
- Install dependencies and ensure your .env is configured as above.

## Expose Your App and Set Webhook URLs

- Start your local server on PORT (default 8000).
- Run ngrok (or a similar tunneling tool) to expose your app, e.g., `ngrok http 8000`.
- Configure your Fax Application callbacks to hit your public URL:
  - Fax callbacks: {NGROK_URL}/faxes
  - Email callbacks (from Mailgun): {NGROK_URL}/email/inbound
- Optionally configure a Failover URL in your Fax Application for webhook retries.

## Map Emails to Numbers

The sample demonstrates a simple in-memory mapping from a user email to a Telnyx phone number and vice versa. In production, replace this with a persistent data store. Each mapping should include:
- phone_number: a Telnyx-owned, fax-enabled number (E.164)
- email: the user’s email address to receive faxes and authorize email-to-fax

## How the Flow Works: Fax-to-Email

- Telnyx sends webhooks for inbound faxes to your /faxes endpoint.
- On `fax.received`, your app downloads the fax PDF from the short-lived media URL and emails it to the mapped recipient via Mailgun.
- The mapping translates the called Telnyx number to the intended email recipient.

Tip: The inbound `media_url` is a signed link that expires quickly (about 10 minutes). Download and persist the file (e.g., to S3) if you need to retain it.

## How the Flow Works: Email-to-Fax

- Mailgun delivers inbound emails to your /email/inbound endpoint.
- The destination fax number is parsed from the local part of the recipient address, e.g., 19198675309@YOUR_MAILGUN_DOMAIN → +19198675309.
- Your app looks up the sender’s email to find the authorized Telnyx "from" number.
- The first attachment is stored (e.g., uploaded to S3) and its public URL is used as the fax media.
- Your app sends a fax via the Telnyx API using connection_id, to, from, and media_url. See [Send a Fax via API](send-a-fax-via-api.md).

## Inbound Fax Webhook Events

When a fax is received on your Telnyx number (direction=inbound), expect events to your Fax Application webhook URL:
- fax.receiving.started: inbound transmission to Telnyx has begun.
- fax.media.processing.started: Telnyx is generating the PDF.
- fax.received: PDF is ready; includes media_url and page_count.
- fax.failed: inbound transmission failed (see failure_reason for details).

See [Receive a Fax via API](receive-a-fax-via-api.md) for more on handling inbound events and downloading media.

## Outbound Fax Webhooks and Delivery Behavior

When sending a fax via API (direction=outbound), you should receive:
- fax.queued → fax.media.processed → fax.sending.started → fax.delivered or fax.failed

Delivery guarantees and ordering:
- Webhooks may arrive out of order, simultaneously, or be duplicated.
- Telnyx retries delivery if your app doesn’t respond promptly.
- Use idempotency with a command_id in your requests; commands with the same command_id within ~60 seconds are ignored, helping prevent duplicate sends.

See [Receiving Webhooks for Programmable Fax](receiving-webhooks-for-programmable-fax.md) for details and payload fields.

## Sending and Receiving Faxes via API (cURL)

Send an outbound fax with cURL using your V2 API key:

curl -X POST https://api.telnyx.com/v2/faxes \
--data-urlencode "media_url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" \
--data-urlencode "connection_id=YOUR_CONNECTION_ID" \
--data-urlencode "to=+1XXXXXXXXXX" \
--data-urlencode "from=+1YYYYYYYYYY" \
--header "Authorization: Bearer YOUR_API_KEY"

- HTTP 202 indicates the fax was accepted for processing. Other responses include 403 (Forbidden), 404 (Not Found), 422 (Invalid Parameters). See [Sending Commands](sending-commands.md).
- Track progress via webhooks listed above.

## Troubleshooting and Failure Reasons

If you receive `fax.failed`, inspect the payload’s failure_reason. Common outbound reasons include (non-exhaustive):
- account_disabled
- connection_channel_limit_exceeded
- destination_invalid
- destination_not_in_countries_whitelist
- destination_not_in_service_plan
- destination_unreachable
- fax_initial_communication_timeout
- fax_signaling_error
- invalid_ecm_response_from_receiver
- no_outbound_profile
- outbound_profile_channel_limit_exceeded
- outbound_profile_daily_spend_limit_exceeded
- receiver_call_dropped
- receiver_communication_error
- receiver_decline
- receiver_incompatible_destination
- receiver_invalid_number_format
- receiver_no_answer
- receiver_no_response
- receiver_recovery_on_timer_expire
- receiver_unallocated_number
- service_unavailable
- unverified_destination_not_allowed
- unverified_origination_number
- user_busy
- user_channel_limit_exceeded

Tips:
- Verify E.164 formatting for to/from numbers.
- Ensure your Fax Application is assigned to the number and to the Outbound Voice Profile for sending.
- Confirm media_url is an accessible PDF (for outbound) and fetch inbound media promptly before it expires.
- Check webhook signature verification using TELNYX_PUBLIC_KEY and that your webhook endpoint returns 2xx quickly.

## Next Steps and Resources

- Deep dive into sending: [Send a Fax via API](send-a-fax-via-api.md) and [Sending Commands](sending-commands.md).
- Build robust inbound handling: [Receive a Fax via API](receive-a-fax-via-api.md) and [Receiving Webhooks for Programmable Fax](receiving-webhooks-for-programmable-fax.md).
- Review platform setup and concepts: [Getting Started with Telnyx Programmable Fax](getting-started-with-telnyx-programmable-fax.md) and [Quickstart Guide for Programmable Fax](quickstart-guide-for-programmable-fax.md).
- Join the community for implementation tips and patterns: https://joinslack.telnyx.com/
