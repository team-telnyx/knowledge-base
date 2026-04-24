---
title: Receive a Fax via API
summary: Telnyx's Programmable Fax API makes it easy to receive faxes from anywhere in the world.
sources:
  - url: https://developers.telnyx.com/docs/programmable-fax/receive-a-fax-api/index
    content_hash: cacea3fe13355dbf3465c2cf750b1576be3bb42575d4f34d308fa97305c857b8
updated_at: 2026-04-10T00:00:00Z
---

# Receive a Fax via API

Telnyx's Programmable Fax API makes it easy to receive faxes from anywhere in the world. With just a few lines of code, you can start receiving faxes in your own applications and workflows.

The Telnyx Programmable Fax API lets you send, receive and manage faxes through a set of easy-to-use HTTP endpoints.

In this guide, you'll learn how to handle receiving a fax using the Programmable Fax API.

## Step 1: Setup with Telnyx

### Setup a Telnyx account, phone number, and programmable fax application

First, follow our [Quickstart](../tutorial/quickstart-guide-for-programmable-fax.md) guide to create a Telnyx account, phone number, and Fax Application.

The phone number that you select and associate with the Programmable Fax Application will receive incoming fax calls. You can also port an existing number to Telnyx and use it for Programmable Fax.

### Step 2: Receiving Webhooks

In order for the webhooks in this tutorial to work, Telnyx must be able to send your web application an HTTP request over the Internet. That means your application needs to have a URL or IP address that Telnyx can reach. Telnyx sends webhooks to the URL or IP address to notify your application of incoming faxes.

For the purpose of this tutorial, we're using <a href="https://ngrok.com/">
ngrok
</a>, a popular tunneling tool used to expose a locally running application to the internet. ngrok gives you a public URL for a local port on your development machine, which you can use to configure your Telnyx webhooks as described above.

Download and install ngrok, then use it at the command line to create a tunnel to whatever port your web application is running on. For example, this command will create a public URL for a web application listening on port 3000.

```bash theme={null}
ngrok http 3000
```

After executing that command, you will see that ngrok has given your application a public URL that you can use in your webhook connection configuration in the <a href="https://portal.telnyx.com/">
Telnyx Mission Control Portal
</a>.

<img alt="Send and receive fax using Telnyx Programmable Fax API" />

Grab your ngrok public URL and head back to the Programmable Fax Application you configured earlier. Now in the field under "Send a webhook to the URL" enter your new ngrok URL from either of the "Forwarding" URLs ngrok provided us with depending on if you want to use HTTP or HTTPS.

You're now all set up to receive webhooks for events related to inbound faxes. If you use the same Programmable Fax Application for sending faxes, you will receive events to the same ngrok URL you just created.

### Example Webhooks

If you have set everything up correctly, any time an inbound fax is received you can expect to receive the following webhooks:

<table>
  <tbody>
    <tr>
      <td>Webhook Name</td>
      <td>Description</td>
    </tr>

    <tr>
      <td><code>fax.receiving.started</code></td>
      <td>The fax has begun transmitting to Telnyx successfully.</td>
    </tr>

    <tr>
      <td><code>fax.media.processing.started</code></td>
      <td>Telnyx has received the fax and is generating the digital PDF file.</td>
    </tr>

    <tr>
      <td><code>fax.received</code></td>
      <td>The PDF has been generated and the file is ready to be downloaded.</td>
    </tr>

    <tr>
      <td><code>fax.failed</code></td>
      <td>Transmission of the fax failed. Check the \<code>failure\_reason\</code> for more details.</td>
    </tr>
  </tbody>
</table>

### Fax has begun transmitting to Telnyx

```json theme={null}
{
  "data": {
    "event_type": "fax.receiving.started",
    "id": "bc004786-f166-4dd3-8c5d-737990b501bc",
    "occurred_at": "2020-08-27T16:33:29.684247Z",
    "payload": {
      "connection_id": "1447842681660114324",
      "direction": "inbound",
      "fax_id": "9fbc3f0d-5495-42af-9a4e-c57a235d9182",
      "from": "+16132484872",
      "status": "receiving",
      "to": "+17733372863",
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8",
      "caller_id": "+16132484872"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

### Fax transmission is complete and Telnyx is converting to PDF

```json theme={null}
{
  "data": {
    "event_type": "fax.media.processing.started",
    "id": "35e33b02-6365-47d0-93b7-3bfec97c467e",
    "occurred_at": "2020-08-27T16:33:33.175396Z",
    "payload": {
      "connection_id": "1447842681660114324",
      "direction": "inbound",
      "fax_id": "f72eebbe-f9b6-4f0f-b652-03e742e110d5",
      "from": "+16132484850",
      "status": "media.processing",
      "page_count": 2,
      "to": "+17733372863",
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8",
      "caller_id": "+16132484872"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

### PDF has been generated and is ready for download

The <code>media\_url</code> field contains a signed AWS link to a PDF of the received fax. This URL is valid for 10 minutes before the file is no longer accessible so be sure to download the file if you wish to keep it!

```json theme={null}
{
  "data": {
    "event_type": "fax.received",
    "id": "4844b70c-3c6c-4c3a-ba2e-e4c785f02d24",
    "occurred_at": "2020-08-27T16:33:36.843054Z",
    "payload": {
      "call_duration_secs": 50,
      "connection_id": "1447842681660114324",
      "direction": "inbound",
      "fax_id": "f72eebbe-f9b6-4f0f-b652-03e742e110d5",
      "from": "+16132484850",
      "media_url": "https://s3.amazonaws.com/faxes-prod/19a75cea-02c6-4b9a-84fa-c9bc8341feb8/f72eebbe-f9b6-4f0f-b652-03e742e110d5.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=...%2F20200827%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200827T163336Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=...",
      "page_count": 2,
      "partial_content": false,
      "status": "received",
      "to": "+17733372863",
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8",
      "caller_id": "+16132484872"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

### Uh oh, something has gone wrong and the fax failed

Inbound faxes can fail for a variety of reasons. Some of the most common reasons are that the sending party hung up before the fax was finished transmitting or didn't send anything at all.

```json theme={null}
{
  "data": {
    "event_type": "fax.failed",
    "id": "1a7405a6-696c-4369-a0b1-168e4bb7e22c",
    "occurred_at": "2020-08-27T16:17:51.844250Z",
    "payload": {
      "connection_id": "1447842681660114324",
      "direction": "inbound",
      "failure_reason": "sender_call_dropped",
      "fax_id": "181533f3-b0b8-4bcd-ab01-b33cd8698508",
      "from": "+16617480240",
      "status": "failed",
      "to": "+17733372863",
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8",
      "caller_id": "+16132484872"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

### Where to next?

Go back to our previous tutorial to learn how to [send outbound faxes](send-a-fax-via-api.md) via API.


## Related Pages

- [Send a Fax via API](../runbooks/send-a-fax-via-api.md)
