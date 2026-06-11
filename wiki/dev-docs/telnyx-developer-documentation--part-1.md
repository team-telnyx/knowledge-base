---
title: Telnyx Developer Documentation
summary: A comprehensive guide to Telnyx's Programmable Fax, Reporting & Analytics,
  and Speech & Voice APIs, covering setup, sending and receiving faxes, webhook handling,
  usage reporting, session analysis, and real-time speech-to-text and text-to-speech
  streaming.
sources:
- url: https://developers.telnyx.com/docs/programmable-fax/email-to-fax
- url: https://developers.telnyx.com/docs/programmable-fax/get-started/index
- url: https://developers.telnyx.com/docs/programmable-fax/quickstart
- url: https://developers.telnyx.com/docs/programmable-fax/receive-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/receiving-webhooks
- url: https://developers.telnyx.com/docs/programmable-fax/send-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/sending-commands
- url: https://developers.telnyx.com/docs/reporting/on-demand-reports/index
- url: https://developers.telnyx.com/docs/reporting/session-analysis
- url: https://developers.telnyx.com/docs/reporting/usage-reports/index
- url: https://developers.telnyx.com/docs/tts-stt/stt-websocket-streaming
- url: https://developers.telnyx.com/docs/tts-stt/telnyx-ultra-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-available-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-websocket-streaming
updated_at: 2026-06-11T10:41:11Z
---

# Telnyx Developer Documentation

*Part 1 of 3 — see also: [Part 2](telnyx-developer-documentation--part-2.md), [Part 3](telnyx-developer-documentation--part-3.md)*

A comprehensive guide to Telnyx's Programmable Fax, Reporting & Analytics, and Speech & Voice APIs, covering setup, sending and receiving faxes, webhook handling, usage reporting, session analysis, and real-time speech-to-text and text-to-speech streaming.

## Programmable Fax

Telnyx Programmable Fax lets you send, receive, and manage faxes through HTTP endpoints. It integrates with the Numbers API for phone number management and the Call Control API for dynamic call handling.

### Getting Started

To use Programmable Fax you need:

1. A Telnyx account — [sign up](https://telnyx.com/sign-up) at the Mission Control Portal.
2. A [Programmable Fax Application](https://portal.telnyx.com/#/call-control/fax) configured with a webhook URL.
3. A phone number (purchased or ported) assigned to that Fax Application.
4. An [Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles) (required for outbound faxes only) with your Fax Application attached.

Generate a Telnyx V2 API key from **Portal → API Keys → Create API key**.

### Quickstart Setup

1. **Create a Fax Application** — In the portal, navigate to "Programmable Fax" → "Add New App". Set a webhook URL (for testing, use [hookbin](https://hookbin.com)).
2. **Buy or port a number** — Under **Numbers**, use "Search & Buy Numbers" or "Port Numbers". This can also be done via the REST API for [searching](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) and [ordering](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order).
3. **Assign the number** — In **My Numbers**, assign your number to the Fax Application.
4. **Create an Outbound Voice Profile** — Navigate to "Outbound Voice Profiles" → "+Add New Profile". Add the Fax Application, traffic type, service plan, and billing method. See [Outbound Voice Profiles](outbound-voice-profiles.md) for programmatic setup.

### Sending a Fax via API

Send a `POST` to `https://api.telnyx.com/v2/faxes` with the following parameters:

| Parameter | Description |
|---|---|
| `media_url` | URL of the PDF to fax |
| `connection_id` | Your Fax Application / connection ID |
| `to` | Destination number in E.164 format |
| `from` | Originating number in E.164 format |
| `Authorization` | `Bearer YOUR_API_KEY` |

```bash
curl -X POST https://api.telnyx.com/v2/faxes \
  --data-urlencode "media_url=https://example.com/document.pdf" \
  --data-urlencode "connection_id=1232154810234" \
  --data-urlencode "to=+13129457420" \
  --data-urlencode "from=+19459457421" \
  --header "Authorization: Bearer YOUR_API_KEY"
```

A successful request returns **HTTP 202**. The API supports PDF files only.

### Receiving a Fax

When an inbound fax arrives at your Telnyx number, Telnyx sends webhooks to the URL configured on your Fax Application. To make your local dev server accessible, use a tunneling tool such as [ngrok](https://ngrok.com/):

```bash
ngrok http 3000
```

Then set the forwarding URL (e.g. `https://your-url.ngrok.io/faxes`) as the webhook URL on your Fax Application.

The `fax.received` webhook includes a `media_url` field with a signed S3 link to the PDF. **This URL expires after 10 minutes** — download the file promptly if you need to keep it.

### Webhooks and Events

Webhooks are delivered to the primary URL on the Application. If that URL fails or returns a non-200 response, delivery falls back to the failover URL if configured. Telnyx does not enforce webhook ordering and may retry delivery, so you can encounter out-of-order, near-simultaneous, or duplicate webhooks. Use a `command_id` parameter to deduplicate — commands with duplicate `command_id` values within 60 seconds are ignored.

#### Outbound Fax Webhook Sequence

| Event | Description |
|---|---|
| `fax.queued` | Telnyx received the request to send the fax |
| `fax.media.processed` | The media has been processed and is ready |
| `fax.sending.started` | The fax transmission has begun |
| `fax.delivered` | The fax was delivered successfully |
| `fax.failed` | The fax failed — check `failure_reason` |

#### Inbound Fax Webhook Sequence

| Event | Description |
|---|---|
| `fax.receiving.started` | The fax has begun transmitting to Telnyx |
| `fax.media.processing.started` | Telnyx is generating the digital PDF |
| `fax.received` | The PDF is ready for download (contains `media_url`) |
| `fax.failed` | Transmission failed — check `failure_reason` |

#### Failure Reasons

Inspect the `failure_reason` field in failed webhook payloads. Possible values include:

- `account_disabled`, `connection_channel_limit_exceeded`, `destination_invalid`, `destination_not_in_countries_whitelist`, `destination_not_in_service_plan`, `destination_unreachable`
- `fax_initial_communication_timeout`, `fax_signaling_error`, `invalid_ecm_response_from_receiver`
- `no_outbound_profile`, `outbound_profile_channel_limit_exceeded`, `outbound_profile_daily_spend_limit_exceeded`
- `receiver_call_dropped`, `receiver_communication_error`, `receiver_decline`, `receiver_incompatible_destination`, `receiver_invalid_number_format`, `receiver_no_answer`, `receiver_no_response`, `receiver_recovery_on_timer_expire`, `receiver_unallocated_number`
- `service_unavailable`, `unverified_destination_not_allowed`, `unverified_origination_number`, `user_busy`, `user_channel_limit_exceeded`

#### Webhook Payload Fields

| Field | Description |
|---|---|
| `record_type` | Description of the record |
| `id` | Unique webhook ID |
| `event_type` | The event type |
| `occurred_at` | ISO-8601 datetime of the event |
| `to` | Destination number or SIP URI |
| `from` | Originating number or SIP URI |
| `fax_id` | Unique ID for the fax transmission |
| `status` | One of `queued`, `media.processed`, `sending.started`, `delivered`, `failed` |

### API Response Codes

| HTTP Status | Meaning |
|---|---|
| 202 | OK — request succeeded |
| 403 | Forbidden — not authorized |
| 404 | Not Found |
| 422 | Invalid Parameters |

### Email-to-Fax Integration

You can build a bidirectional email-to-fax application using Telnyx Fax API, [Mailgun](https://www.mailgun.com/) for email, and AWS S3 for media storage. A sample application is available on [GitHub](https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-fax-email-webinar).

#### Prerequisites

- Telnyx account with a Fax-enabled number and Outbound Voice Profile
- Webhook endpoint (e.g. via [ngrok](https://ngrok.com/))
- Python and PIP installed
- AWS account with S3 access (see [boto3 quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html))
- Mailgun account with [inbound routes](https://app.mailgun.com/app/receiving/routes) configured

#### Environment Variables

| Variable | Description |
|---|---|
| `TELNYX_API_KEY` | Your Telnyx API Key |
| `TELNYX_PUBLIC_KEY` | Telnyx Public Key |
| `TELNYX_S3_BUCKET` | S3 bucket name for media uploads |
| `TELNYX_FAX_CONNECTION_ID` | Fax Application connection ID |
| `MAILGUN_API_KEY` | Mailgun API key |
| `MAILGUN_DOMAIN` | Mailgun domain |
| `PORT` | Server port (defaults to 8000) |

Use `python-dotenv` to manage these from a `.env` file.

#### Callback URLs

| Callback Type | URL Pattern |
|---|---|
| Fax Callbacks | `{ngrok-url}/faxes` |
| Email Callbacks | `{ngrok-url}/email/inbound` |

#### Receiving a Fax → Sending an Email

1. Receive webhook from Telnyx for an incoming fax (only the `fax.received` event for `inbound` faxes matters).
2. Extract `to`/`from` and other fax metadata.
3. Download the PDF attachment and save locally.
4. Look up the phone-number-to-email association.
5. Send an email via Mailgun with the downloaded media as an attachment.

#### Sending a Fax from an Email

1. Receive webhook from Mailgun for an incoming email.
2. Extract the phone number prefix from the email address (e.g. `19198675309@MAILGUN_DOMAIN.com` → `+19198675309`).
3. Look up the email-to-phone-number association to determine the `from` number.
4. Save the first attachment locally.
5. Upload the attachment to S3.
6. Send a fax to the extracted phone number via the Telnyx API.

The sample app uses a simple in-memory database to map emails to phone numbers:

```python
DB = [
    {"email": "user@example.com", "phone_number": "+19198675309"}
]
```

---
