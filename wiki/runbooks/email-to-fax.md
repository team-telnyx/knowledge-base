---
title: Email to Fax
summary: Telnyx's Programmable Fax allows you to send faxes from your email.
sources:
  - url: https://developers.telnyx.com/docs/programmable-fax/email-to-fax/index
    content_hash: a848cfa312fc13dc6eb010a8c908722ddf94b6dfbaf3c05ddf957bff31429a39
updated_at: 2026-04-10T00:00:00Z
---

# Email to Fax

Telnyx's Programmable Fax allows you to send faxes from your email. This tutorial will show you how to do it in Python.

**⏱ 60 minutes build time.**

**🧰 Clone the sample application from our <a href="https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-fax-email-webinar">
GitHub repo
</a>**

In this tutorial, you'll learn how to use the Telnyx Fax API to receieve faxes to your email in Python.

Our Programmable Fax API, combined with our Numbers API, provides everything you need to build a robust call tracking application:

The Numbers API enables you to search the Telnyx phone number inventory in real time; filtering by Area Code, City/State, and more to find the perfect local number for your use-case.
Call Control enables you to quickly setup dynamic forwarding numbers, toggle dual-channel recording, join/leave dynamic conferences, and pull post-call analytics.
By following this tutorial, you'll be able to:

> 1. Configure a Telnyx portal account.
> 2. Set up a Telnyx Fax profile and an outbound voice profile.
> 3. How to send a fax to your email using Telnyx.
> 4. How to send a fax using your email and to Telnyx Fax profile.

## What you'll need to get started with email to fax

1. A Telnyx account- take a minute to <a href="https://telnyx.com/sign-up">
   sign up
   </a> to our self-service portal.
2. A Telnyx phone number that's enabled with a <a href="https://portal.telnyx.com/#/app/fax/applications">
   Telnyx Fax Appliction
   </a> and a Telnyx <a href="https://portal.telnyx.com/#/app/outbound-profiles?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link">
   Outbound Voice profile
   </a>.
3. Ability to receive webhooks (with something like [ngrok](../reference/ngrok.md#ngrok "ngrok"))
4. [Python and PIP](https://developers.telnyx.com/development/sdk/python "Python and PIP") installed
5. An AWS Account setup with proper profiles and groups with IAM for S3. Check out the <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html">
   Quickstart
   </a> for more information.
6. Finally you'll need a <a href="https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-fax-email-webinar">
   Mailgun account
   </a>. If you're planning on using this guide to build an email to fax application you'll need an account with the ability to setup <a href="https://app.mailgun.com/app/receiving/routes">
   inbound routes
   </a>.

### Create a Telnyx Mission Control Portal account

To get started, you'll need to <a href="https://telnyx.com/sign-up">
create an account
</a>. Verify your email address and you can log into the <a href="https://portal.telnyx.com">
Mission Control Portal
</a> to get started.

### Usage

The following environmental variables need to be set:

<table>
  <tbody>
    <tr>
      <td>Variable</td>
      <td>Description</td>
    </tr>

    <tr>
      <td>TELNYX\_API\_KEY</td>
      <td>Your <a href="https://portal.telnyx.com/#/app/api-keys?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link">Telnyx API Key</a></td>
    </tr>

    <tr>
      <td>TELNYX\_PUBLIC\_KEY</td>
      <td><a href="https://portal.telnyx.com/#/app/account/public-key?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link">Telnyx Public Key</a></td>
    </tr>

    <tr>
      <td>TELNYX\_S3\_BUCKET</td>
      <td>The name of the bucket to upload the media attachments</td>
    </tr>

    <tr>
      <td>TELNYX\_FAX\_CONNECTION\_ID</td>
      <td>The <a href="https://portal.telnyx.com/#/app/fax/applications">connection ID</a> for your Fax Applications</td>
    </tr>

    <tr>
      <td>MAILGUN\_API\_KEY</td>
      <td>Your <a href="https://www.mailgun.com/">Mailgun API</a> Key</td>
    </tr>

    <tr>
      <td>MAILGUN\_DOMAIN</td>
      <td>Your <a href="https://app.mailgun.com/app/sending/domains">Mailgun</a> Domain.</td>
    </tr>

    <tr>
      <td>PORT</td>
      <td><strong>Defaults to 8000</strong> The port the app will be served</td>
    </tr>
  </tbody>
</table>

### .env file

This app uses the excellent <a href="https://github.com/theskumar/python-dotenv">python-dotenv</a> package to manage environment variables.

Make a copy of <a href="https://github.com/team-telnyx/demo-python-telnyx/blob/master/flask-fax-email-webinar/.env.sample">.env.sample</a> and save as .env and update the variables to match your creds.

TELNYX\_PUBLIC\_KEY="+kWXUag92mcUMFQopVlff7ctD/m2S/IoXv+AlI1/5a0="
TELNYX\_API\_KEY="KEYI"
TELNYX\_S3\_BUCKET=telnyx-mms-demo
TELNYX\_FAX\_CONNECTION\_ID=36092346987
MAILGUN\_API\_KEY="123-432-123"
MAILGUN\_DOMAIN="sandbox367c5ec1512d458e95f5e5c60f5fe97a.mailgun.org"
PORT=8000

### Callback URLs for Telnyx application

<table>
  <tbody>
    <tr>
      <td>Callback Type</td>
      <td>URL</td>
    </tr>

    <tr>
      <td>Fax Callbacks</td>
      <td>`{ngrok-url}/faxes`</td>
    </tr>

    <tr>
      <td>Email Callbacks</td>
      <td>`{ngrok-url}/email/inbound`</td>
    </tr>
  </tbody>
</table>

### Install

Run the following commands to get started:

\$ git clone [https://github.com/team-telnyx/demo-python-telnyx.git](https://github.com/team-telnyx/demo-python-telnyx.git)

### Ngrok

This application is served on the port defined in the runtime environment (or in the .env file). Be sure to launch ngrok for that port:

./ngrok http 8000

ngrok by @inconshreveable                                                                                                                               (Ctrl+C to quit)

Session Status                online
Account                       Little Bobby Tables (Plan: Free)
Version                       2.3.35
Region                        United States (us)
Web Interface                 [http://127.0.0.1:4040](http://127.0.0.1:4040)
Forwarding                    [http://your-url.ngrok.io](http://your-url.ngrok.io) -> [http://localhost:8000](http://localhost:8000)
Forwarding                    [https://your-url.ngrok.io](https://your-url.ngrok.io) -> [http://localhost:8000](http://localhost:8000)

Connections                   ttl     opn     rt1     rt5     p50     p90
0       0       0.00    0.00    0.00    0.00

At this point you can point your application to generated ngrok URL + path:

(Example: `http://{your-url}.ngrok.io/faxes`).

## Run

### High level code overview

#### Receiving fax, sending email

1. Receive the webhook from Telnyx indicating fax is incoming
2. We only only care about the <code>fax.received</code> webhook for <code>inbound</code> faxes
3. Extract the <code>to/from</code> and other information about the fax
4. Download the attachment and save locally
5. Lookup the association between phone\_number and email
6. Create and send an email via Mailgun with downloaded media as an attachment

#### Sending fax

1. Receive webhook from mailgun for incoming email
2. Extract the prefix of the email <code>([19198675309@MAILGUN\_DOMAIN.com](mailto:19198675309@MAILGUN_DOMAIN.com)</code>, we want <code>19198675309)</code> and prepend the +
3. Lookup the association between email and phone\_number to determine the <code>from</code> phone number.
4. Save the first attachment locally
5. Upload the attachment to S3
6. Create and send a fax to the phone number extracted above

### Update "DB"

The app as provided uses a dumb-hard-coded database to minimize dependencies for the sake of examples. There is an in memory database defined at the top that associates an email to a Telnyx number.

```
    DB = [
{
    "email": "@telnyx.com",
    "phone_number": "+"
}
    ]
```

* <code>phone\_number</code> is a **Telnyx** phone number
* <code>email</code> is the email to associate with that phone number

#### Receiving faxes

```
{+19198675309} ==(faxes)==> {telnyx_phone_number} ==(emails)==> {email_as_defined}
```

#### Sending faxes

```
{email_as_defined} ==(emails)==> {destination_phone_number@MAILGUN_DOMAIN} ==(faxes)==> {destination_phone_number}
```

### Launch the app and update callbacks

Start the server <code>python app.py</code>

When you are able to run the server locally, the final step involves making your application accessible from the Internet. So far, we've set up a local web server. This is typically not accessible from the public internet, making testing inbound requests to web applications difficult.

The best workaround is a tunneling service. They come with client software that runs on your computer and opens an outgoing permanent connection to a publicly available server in a data center. Then, they assign a public URL (typically on a random or custom subdomain) on that server to your account. The public server acts as a proxy that accepts incoming connections to your URL, forwards (tunnels) them through the already established connection and sends them to the local web server as if they originated from the same machine. The most popular tunneling tool is <code>ngrok</code>.

Check out the [ngrok setup](../reference/ngrok.md#ngrok "ngrok setup") walkthrough to set it up on your computer and start receiving webhooks from inbound faxes to your newly created application.

Once you've set up <code>ngrok</code> or another tunneling service you can add the public proxy URL to your Inbound Settings in the Mission Control Portal. To do this, click the edit symbol \[✎] next to your Fax Profile. In the "Inbound Settings" > "Webhook URL" field, paste the forwarding address from ngrok into the Webhook URL field. Add <code>faxes</code> to the end of the URL to direct the request to the webhook endpoint in your server.

For now you'll leave “Failover URL” blank, but if you'd like to have Telnyx resend the webhook in the case where sending to the Webhook URL fails, you can specify an alternate address in this field.

Once everything is setup, you should now be able to:

* Fax your phone number and receive an email
* Email `{19198675309}@domain.com` an attachment to send a fax to `{19198675309}`

<hr />

## Fax follow-Ons

Now that you've successfully sent a fax to your email and phone number, you can explore more fax features and discover ideas to build new applications.

Our <a href="https://joinslack.telnyx.com/">developer Slack community</a> is full of Python developers like you - be sure to join to see what your fellow developers are building!
