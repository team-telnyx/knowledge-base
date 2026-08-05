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

*Part 3 of 3 — see also: [Part 1](programmable-fax--part-1.md), [Part 2](programmable-fax--part-2.md)*

Telnyx Programmable Fax provides HTTP API endpoints for sending, receiving, and managing faxes. This page covers account setup, sending and receiving faxes via the API, webhook handling, and an email-to-fax tutorial.

## Email to Fax Tutorial

This tutorial walks through building an application that bridges email and fax using the Telnyx Fax API, Mailgun, and AWS S3. You can clone the sample application from the [GitHub repo](https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-fax-email-webinar).

### Environment variables

The application uses [python-dotenv](https://github.com/theskumar/python-dotenv) to manage environment variables. Copy `.env.sample` to `.env` and update the values:

| Variable | Description |
| --- | --- |
| `TELNYX_API_KEY` | Your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys). |
| `TELNYX_PUBLIC_KEY` | [Telnyx Public Key](https://portal.telnyx.com/#/app/account/public-key). |
| `TELNYX_S3_BUCKET` | The name of the bucket to upload media attachments. |
| `TELNYX_FAX_CONNECTION_ID` | The [connection ID](https://portal.telnyx.com/#/app/fax/applications) for your Fax Applications. |
| `MAILGUN_API_KEY` | Your [Mailgun](https://www.mailgun.com/) API key. |
| `MAILGUN_DOMAIN` | Your [Mailgun](https://app.mailgun.com/app/sending/domains) domain. |
| `PORT` | Defaults to `8000`. The port the app will be served on. |

### Callback URLs

| Callback Type | URL |
| --- | --- |
| Fax Callbacks | `{ngrok-url}/faxes` |
| Email Callbacks | `{ngrok-url}/email/inbound` |

### Install and run

Clone the repo and start the server:

```
git clone https://github.com/team-telnyx/demo-python-telnyx.git
```

Launch ngrok for the configured port:

```
./ngrok http 8000
```

Then start the server:

```
python app.py
```

### How it works

**Receiving a fax and sending an email:**

1. Receive the webhook from Telnyx indicating a fax is incoming.
2. Filter for the `fax.received` webhook for inbound faxes.
3. Extract the `to`/`from` and other information about the fax.
4. Download the attachment and save locally.
5. Look up the association between phone number and email.
6. Create and send an email via Mailgun with the downloaded media as an attachment.

**Sending a fax from an email:**

1. Receive a webhook from Mailgun for an incoming email.
2. Extract the prefix of the email address (e.g. `19198675309@MAILGUN_DOMAIN.com` → `19198675309`) and prepend `+`.
3. Look up the association between email and phone number to determine the `from` phone number.
4. Save the first attachment locally.
5. Upload the attachment to S3.
6. Create and send a fax to the phone number extracted above.

### In-memory database

The sample app uses a hard-coded in-memory database to minimize dependencies. Each entry associates an email with a Telnyx phone number:

```
DB = [
    {
        "email": "@telnyx.com",
        "phone_number": "+"
    }
]
```

- `phone_number` is a Telnyx phone number.
- `email` is the email to associate with that phone number.

The data flow is:

- Receiving: `{+19198675309} ==(faxes)==> {telnyx_phone_number} ==(emails)==> {email_as_defined}`
- Sending: `{email_as_defined} ==(emails)==> {destination_phone_number@MAILGUN_DOMAIN} ==(faxes)==> {destination_phone_number}`

### Configure the webhook URL

In the Mission Control Portal, click the edit symbol next to your Fax Profile. In "Inbound Settings" → "Webhook URL", paste the ngrok forwarding address and append `/faxes` to direct requests to your webhook endpoint. Leave "Failover URL" blank unless you want Telnyx to retry on failure.

Once everything is set up, you can:

- Fax your phone number and receive an email.
- Email `{19198675309}@domain.com` an attachment to send a fax to `{19198675309}`.

## Next Steps

- Explore advanced features like receiving faxes and detailed webhook management.
- Dive deeper into [Sending Commands](sending-commands.md) and [Receiving Webhooks](receiving-webhooks.md).
- Join the [Telnyx developer Slack community](https://joinslack.telnyx.com/) to see what other developers are building.
- For support, visit the [Telnyx support center](https://support.telnyx.com/).
