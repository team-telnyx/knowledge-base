---
title: Programmable Fax
summary: Telnyx Programmable Fax provides HTTP API endpoints for sending, receiving,
  and managing faxes. This page covers account setup, sending and receiving faxes
  via the API, webhook handling, and an email-to-fax tutorial.
sources:
- url: https://developers.telnyx.com/docs/programmable-fax/email-to-fax
- url: https://developers.telnyx.com/docs/programmable-fax/get-started/index
- url: https://developers.telnyx.com/docs/programmable-fax/quickstart
- url: https://developers.telnyx.com/docs/programmable-fax/receive-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/receiving-webhooks
- url: https://developers.telnyx.com/docs/programmable-fax/send-a-fax-api
- url: https://developers.telnyx.com/docs/programmable-fax/sending-commands
updated_at: 2026-08-05T14:01:02Z
---

# Programmable Fax

*Part 1 of 3 — see also: [Part 2](programmable-fax--part-2.md), [Part 3](programmable-fax--part-3.md)*

Telnyx Programmable Fax provides HTTP API endpoints for sending, receiving, and managing faxes. This page covers account setup, sending and receiving faxes via the API, webhook handling, and an email-to-fax tutorial.

## Overview

Telnyx Programmable Fax lets you send, receive, and manage faxes through a set of HTTP endpoints. The service combines a Programmable Fax Application (for inbound traffic and authentication) with an Outbound Voice Profile (for outbound traffic, billing, and allowed destinations), and notifies your server of fax events via webhooks.

Core concepts to be aware of:

- **Programmable Fax Application** — a configuration within the Telnyx platform that manages inbound and outbound fax traffic, including authentication and webhook handling.
- **Outbound Voice Profile** — a setting that allows users to initiate outbound traffic, including faxes, with configurations for billing, traffic management, and permitted destinations.
- **fax_id** — a unique identifier assigned to each fax transmission, used to track and manage specific fax communications.
- **media_url** — the URL pointing to the document to fax, typically in PDF format.
- **connection_id** — an identifier for your specific application or connection within Telnyx, used to route the fax correctly.
- **E.164 format** — the internationally recognized format for phone numbers, used in the `to` and `from` fields.
- **failure_reason** — a field in the webhook payload that explains why a fax failed.

## Prerequisites

Before you begin, you will need:

- A Telnyx account — [sign up](https://telnyx.com/sign-up) for the self-service portal.
- A Telnyx phone number enabled with a [Programmable Fax Application](https://portal.telnyx.com/#/app/fax/applications) and a Telnyx [Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles).
- A Telnyx V2 API Authentication key generated via the [Mission Control Portal](https://portal.telnyx.com/#/app/api-keys).
- A way to receive webhooks locally during development, such as [ngrok](ngrok.md).
- For the email-to-fax tutorial: Python and PIP installed, an AWS account with S3 access, and a [Mailgun](https://www.mailgun.com/) account with inbound routes configured.

## Quickstart: Portal Setup

Follow these steps in the Telnyx Portal to get up and running:

1. **Sign up** for a Telnyx Mission Control Portal account at [telnyx.com/sign-up](https://telnyx.com/sign-up).
2. **Create a Programmable Fax Application** by selecting "Programmable Fax" in the left-hand navigation menu and clicking "Add New App". For testing, you can set the webhook URL using an endpoint you create at [hookbin.com](https://hookbin.com).
3. **Buy or port a phone number** in the Numbers section of the [Telnyx Portal](https://portal.telnyx.com/#/app/numbers/search-numbers). You can also do this programmatically via the [number searching](/api-reference/phone-number-search/list-available-phone-numbers) and [ordering](/api-reference/phone-number-orders/create-a-number-order) APIs.
4. **Assign your phone number** to the Programmable Fax Application via the [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) section.

![Assign phone number to Programmable Fax Application](_images/Docs_Images__1_.png)

5. **Create an Outbound Voice Profile** (required for outbound faxes) by selecting "Outbound Voice Profiles" on the left-hand navigation menu, clicking "+Add New Profile", and configuring the profile name, the Programmable Fax Application, traffic type, service plan, and billing method. You can also do this programmatically via the [Outbound Voice Profiles API](/docs/voice/outbound-voice-profiles).

## Sending a Fax via API

To send a fax, POST to the Programmable Fax API endpoint `https://api.telnyx.com/v2/faxes`. The API supports PDF files.

### Authentication

Generate a Telnyx V2 API key in the [Mission Control Portal](https://portal.telnyx.com/) under "API Keys" (ensure API V2 is selected), then include it as a bearer token in the `Authorization` header.

### Request parameters

| Field | Description |
| --- | --- |
| `media_url` | The URL of the PDF used for the fax's media. |
| `connection_id` | The app ID or connection ID to send the fax with. |
| `to` | The fax-enabled phone number (in E.164 format), or SIP URI, the fax will be sent to. |
| `from` | The phone number, in E.164 format, the fax will be sent from. |
| `Authorization: Bearer` | The prefix to your API V2 key. |

### Example: send a fax with cURL

```
curl -X POST https://api.telnyx.com/v2/faxes \
--data-urlencode "media_url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" \
--data-urlencode "connection_id=1232154810234" \
--data-urlencode "to=+13129457420" \
--data-urlencode "from=+19459457421" \
--header "Authorization: Bearer APIAuthKey_fromPortal"
```

### Response codes

| HTTP Status | Message | Description |
| --- | --- | --- |
| 202 | OK | The request succeeded. |
| 403 | Forbidden | The request was valid, but the user is not authorized to perform this action. |
| 404 | Not Found | The requested resource could not be found. |
| 422 | Invalid Parameters | The request has invalid parameters. |

A successful request returns `HTTP 202` and triggers a series of webhooks to the URL configured on your Fax Application.

## Receiving a Fax via API

The phone number associated with your Programmable Fax Application will receive incoming fax calls. You can also port an existing number to Telnyx and use it for Programmable Fax.

### Webhook setup

Telnyx must be able to send your web application an HTTP request over the internet, so your application needs a publicly reachable URL or IP address. For local development, use [ngrok](ngrok.md) to expose your local port:

```
ngrok http 3000
```

Grab the ngrok public URL and paste it into the "Send a webhook to the URL" field of your Programmable Fax Application in the [Mission Control Portal](https://portal.telnyx.com/).

![Send and receive fax using Telnyx Programmable Fax API](_images/twiml-conferencing-3.png)

### Inbound fax webhooks

| Webhook | Description |
| --- | --- |
| `fax.receiving.started` | The fax has begun transmitting to Telnyx successfully. |
| `fax.media.processing.started` | Telnyx has received the fax and is generating the digital PDF file. |
| `fax.received` | The PDF has been generated and the file is ready to be downloaded. |
| `fax.failed` | Transmission of the fax failed. Check the `failure_reason` for more details. |

The `fax.received` webhook includes a `media_url` field containing a signed AWS link to a PDF of the received fax. This URL is valid for 10 minutes, so download the file promptly if you wish to keep it.
