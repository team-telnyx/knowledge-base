---
title: Programmable Fax
summary: Telnyx Programmable Fax is an HTTP API for sending, receiving, and managing
  faxes. This page covers the core concepts (Fax Applications, Outbound Voice Profiles,
  and Webhooks), the portal quickstart for setting up an account, phone number, and
  application, how to send and receive faxes via the API, the full set of fax-related
  webhooks and failure reasons, and a reference email-to-fax / fax-to-email implementation
  built with Python, Flask, Mailgun, and S3.
sources:
- url: https://developers.telnyx.com/docs/programmable-fax/email-to-fax
- url: https://developers.telnyx.com/docs/programmable-fax/get-started/index
- url: https://developers.telnyx.com/docs/programmable-fax/quickstart
- url: https://developers.telnyx.com/docs/programmable-fax/receive-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/receiving-webhooks
- url: https://developers.telnyx.com/docs/programmable-fax/send-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/sending-commands
updated_at: 2026-07-17T09:16:03Z
---

# Programmable Fax

*Part 1 of 2 — see also: [Part 2](programmable-fax--part-2.md)*

Telnyx Programmable Fax is an HTTP API for sending, receiving, and managing faxes. This page covers the core concepts (Fax Applications, Outbound Voice Profiles, and Webhooks), the portal quickstart for setting up an account, phone number, and application, how to send and receive faxes via the API, the full set of fax-related webhooks and failure reasons, and a reference email-to-fax / fax-to-email implementation built with Python, Flask, Mailgun, and S3.

## Overview

Telnyx Programmable Fax lets you send, receive, and manage faxes through a set of HTTP endpoints. The service is built around three core concepts: a **Programmable Fax Application** (which configures inbound traffic and authentication for your phone numbers), an **Outbound Voice Profile** (which manages outbound traffic, billing, and allowed destinations), and **Webhooks** (HTTP callbacks that notify your server about fax events).

To get started you need a Telnyx account, a phone number with a Programmable Fax Application attached, and a Telnyx V2 API authentication key generated from the [Mission Control Portal](https://portal.telnyx.com/#/app/api-keys).

## Quickstart Setup

Follow these steps in the Telnyx Portal to get a working fax setup:

1. **Sign up** for a Telnyx Mission Control Portal account at [telnyx.com/sign-up](https://telnyx.com/sign-up).
2. **Create a Programmable Fax Application.** In the left-hand navigation, select ["Programmable Fax"](https://portal.telnyx.com/#/call-control/fax), click "Add New App", and set a webhook URL (for testing, you can use an endpoint created at [hookbin.com](https://hookbin.com)).
3. **Buy or port a phone number** from the [Numbers section](https://portal.telnyx.com/#/app/numbers/search-numbers) of the portal. You can also do this programmatically via the [Number Search](/api-reference/phone-number-search/list-available-phone-numbers) and [Number Orders](/api-reference/phone-number-orders/create-a-number-order) APIs.
4. **Assign the phone number** to the Programmable Fax Application you created, via the [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) section.
5. **Create an Outbound Voice Profile** (required for outbound faxes). Select ["Outbound Voice Profiles"](https://portal.telnyx.com/#/app/outbound-profiles), click "+Add New Profile", and configure the profile name, the Programmable Fax Application, traffic type, service plan, and billing method. See the [Outbound Voice Profiles](/docs/voice/outbound-voice-profiles) docs for more.

## Sending a Fax via API

The Programmable Fax API supports PDF files. To send a fax, POST to `https://api.telnyx.com/v2/faxes` with the following parameters:

| Parameter | Description |
| --- | --- |
| `media_url` | The URL of the PDF used for the fax's media. |
| `connection_id` | The app ID or connection ID to send the fax with. |
| `to` | The fax-enabled phone number (in E.164 format), or SIP URI, the fax will be sent to. |
| `from` | The phone number, in E.164 format, the fax will be sent from. |
| `Authorization: Bearer` | The prefix to your API V2 key. |

Example using cURL:

```
curl -X POST https://api.telnyx.com/v2/faxes \
--data-urlencode "media_url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" \
--data-urlencode "connection_id=1232154810234" \
--data-urlencode "to=+13129457420" \
--data-urlencode "from=+19459457421" \
--header "Authorization: Bearer APIAuthKey_fromPortal"
```

A successful request returns `HTTP 202`. Other response codes include `403 Forbidden`, `404 Not Found`, and `422 Invalid Parameters`.

## Receiving a Fax via API

Once your Programmable Fax Application is configured with a webhook URL, Telnyx will deliver webhooks for inbound fax events. For local development, expose your app to the internet using a tunneling tool such as [ngrok](https://ngrok.com/):

```
ngrok http 3000
```

Then paste the ngrok forwarding URL into the "Send a webhook to the URL" field of your Programmable Fax Application.

The inbound fax lifecycle produces the following webhooks:

| Webhook | Description |
| --- | --- |
| `fax.receiving.started` | The fax has begun transmitting to Telnyx successfully. |
| `fax.media.processing.started` | Telnyx has received the fax and is generating the digital PDF file. |
| `fax.received` | The PDF has been generated and the file is ready to be downloaded. |
| `fax.failed` | Transmission of the fax failed. Check the `failure_reason` for more details. |

The `fax.received` webhook includes a `media_url` field containing a signed AWS link to a PDF of the received fax. This URL is valid for 10 minutes, so download the file promptly if you want to keep it.

## Webhooks

When you send a Programmable Fax command and receive a successful response (HTTP 200 OK), Telnyx delivers a webhook to the primary URL specified on the Application associated with the call. If that URL does not resolve, or your application returns a non-200 response, the webhook is delivered to the failover URL (if configured).

To minimize delivery time, Telnyx does not enforce webhook ordering and retries delivery if your application does not respond within a time threshold. As a result, you may encounter out-of-order, simultaneous, or duplicate webhooks. To prevent duplicate commands, send a `command_id` parameter with your commands — Telnyx ignores commands with duplicate `command_ids` within 60 seconds.

### Outbound Fax Webhooks

When you place an outbound fax, you receive a series of webhooks indicating its status:

| Webhook | Description |
| --- | --- |
| `fax.queued` | Telnyx successfully received the request to send the fax. |
| `fax.media.processed` | The media has been processed. |
| `fax.sending.started` | The fax has begun transmitting. |
| `fax.delivered` | The fax was successfully delivered. |
| `fax.failed` | The fax failed to deliver. |

### Webhook Payload Fields

| Field | Description |
| --- | --- |
| `record_type` | Description of the record. |
| `id` | Unique id for the webhook. |
| `event_type` | The type of event. |
| `occurred_at` | ISO-8601 datetime of when the event occurred. |
| `to` | Destination number or SIP URI of the call. |
| `from` | Number or SIP URI placing the call. |
| `fax_id` | Unique ID for the Programmable Fax. |
| `client_state` | Configurable state to track commands. |
| `status` | One of `queued`, `media.processed`, `sending.started`, `delivered`, `failed`. |

### Possible Failure Reasons

Inspect the `failure_reason` field in a webhook's payload to debug failed deliveries. Possible values include:

- `account_disabled`
- `connection_channel_limit_exceeded`
- `destination_invalid`
- `destination_not_in_countries_whitelist`
- `destination_not_in_service_plan`
- `destination_unreachable`
- `fax_initial_communication_timeout`
- `fax_signaling_error`
- `invalid_ecm_response_from_receiver`
- `no_outbound_profile`
- `outbound_profile_channel_limit_exceeded`
- `outbound_profile_daily_spend_limit_exceeded`
- `receiver_call_dropped`
- `receiver_communication_error`
- `receiver_decline`
- `receiver_incompatible_destination`
- `receiver_invalid_number_format`
- `receiver_no_answer`
- `receiver_no_response`
- `receiver_recovery_on_timer_expire`
- `receiver_unallocated_number`
- `service_unavailable`
- `unverified_destination_not_allowed`
- `unverified_origination_number`
- `user_busy`
- `user_channel_limit_exceeded`
