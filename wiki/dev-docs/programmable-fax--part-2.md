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

*Part 2 of 2 — see also: [Part 1](programmable-fax--part-1.md)*

Telnyx Programmable Fax is an HTTP API for sending, receiving, and managing faxes. This page covers the core concepts (Fax Applications, Outbound Voice Profiles, and Webhooks), the portal quickstart for setting up an account, phone number, and application, how to send and receive faxes via the API, the full set of fax-related webhooks and failure reasons, and a reference email-to-fax / fax-to-email implementation built with Python, Flask, Mailgun, and S3.

## Email to Fax

Telnyx Programmable Fax can be combined with an email service (such as Mailgun) and S3 to build an email-to-fax and fax-to-email bridge. The reference implementation is a Python/Flask app available in the [demo-python-telnyx GitHub repo](https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-fax-email-webinar).

### Prerequisites

- A Telnyx account with a phone number enabled with a [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications) and a [Telnyx Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles).
- A tunneling tool such as [ngrok](/development/development-tools/ngrok-setup/index#ngrok) to receive webhooks locally.
- [Python and PIP](/development/sdk/python) installed.
- An AWS account with IAM configured for S3 (see the [boto3 Quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)).
- A [Mailgun account](https://www.mailgun.com/) with the ability to set up [inbound routes](https://app.mailgun.com/app/receiving/routes).

### Environment Variables

| Variable | Description |
| --- | --- |
| `TELNYX_API_KEY` | Your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys). |
| `TELNYX_PUBLIC_KEY` | Your [Telnyx Public Key](https://portal.telnyx.com/#/app/account/public-key). |
| `TELNYX_S3_BUCKET` | The name of the bucket to upload media attachments. |
| `TELNYX_FAX_CONNECTION_ID` | The [connection ID](https://portal.telnyx.com/#/app/fax/applications) for your Fax Application. |
| `MAILGUN_API_KEY` | Your Mailgun API key. |
| `MAILGUN_DOMAIN` | Your [Mailgun sending domain](https://app.mailgun.com/app/sending/domains). |
| `PORT` | The port the app will be served (defaults to 8000). |

The app uses [python-dotenv](https://github.com/theskumar/python-dotenv) to manage these variables. Copy `.env.sample` to `.env` and fill in your credentials.

### Callback URLs

| Callback Type | URL |
| --- | --- |
| Fax Callbacks | `{ngrok-url}/faxes` |
| Email Callbacks | `{ngrok-url}/email/inbound` |

### How It Works

**Receiving a fax and sending it as email:**

1. Receive the webhook from Telnyx indicating a fax is incoming.
2. Filter for the `fax.received` webhook for inbound faxes.
3. Extract the `to`/`from` and other information about the fax.
4. Download the attachment and save locally.
5. Look up the association between phone number and email.
6. Create and send an email via Mailgun with the downloaded media as an attachment.

**Sending a fax from email:**

1. Receive a webhook from Mailgun for an incoming email.
2. Extract the prefix of the email address (e.g. `19198675309@MAILGUN_DOMAIN.com` → `19198675309`) and prepend `+`.
3. Look up the association between email and phone number to determine the `from` phone number.
4. Save the first attachment locally.
5. Upload the attachment to S3.
6. Create and send a fax to the phone number extracted above.

The reference app uses a hard-coded in-memory database that associates an email with a Telnyx phone number. The flow is:

- Receiving: `{+19198675309} ==(faxes)==> {telnyx_phone_number} ==(emails)==> {email_as_defined}`
- Sending: `{email_as_defined} ==(emails)==> {destination_phone_number@MAILGUN_DOMAIN} ==(faxes)==> {destination_phone_number}`

## Glossary

- **Programmable Fax Application**: A configuration within the Telnyx platform used to manage inbound and outbound fax traffic, including authentication and handling of fax transmissions.
- **Outbound Voice Profile**: A setting in Telnyx that allows users to initiate outbound traffic, including faxes, with configurations for billing, traffic management, and permitted destinations.
- **Fax ID**: A unique identifier assigned to each fax transmission, used to track and manage specific fax communications.
- **Media URL**: The URL pointing to the document you wish to fax, typically in PDF format.
- **Connection ID**: An identifier for your specific application or connection within Telnyx, used to route the fax correctly.
- **E.164 Format**: An internationally recognized format for phone numbers, used in the `to` and `from` fields of fax commands.
- **Failure Reason**: A field in the webhook payload that provides the reason for a fax's failure.
- **Ngrok**: A tunneling tool used to expose a local server to the internet, often used for testing webhook endpoints in development.
- **cURL**: A command-line tool used for sending requests to URLs, commonly used for interacting with APIs like Telnyx's Programmable Fax API.

## Additional Resources

- [Telnyx API reference](https://developers.telnyx.com/docs/programmable-fax/sending-commands) for in-depth endpoint documentation.
- [Telnyx support](https://support.telnyx.com/) for troubleshooting help.
- [Telnyx developer Slack community](https://joinslack.telnyx.com/) for peer support.
- Related guides: [Quickstart Guide for Programmable Fax](quickstart-guide-for-programmable-fax.md), [Send a Fax via API](send-a-fax-via-api.md), [Receive a Fax via API](receive-a-fax-via-api.md), [Receiving Webhooks for Programmable Fax](receiving-webhooks-for-programmable-fax.md), [Sending Commands](sending-commands.md), [Email to Fax](email-to-fax.md).
