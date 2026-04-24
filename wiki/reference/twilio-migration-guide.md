---
title: Twilio Migration Guide
summary: Telnyx's Programmable Fax system for migrating from Twilio.
sources:
  - url: https://developers.telnyx.com/development/migration/twilio-migration-guide/index
    content_hash: ff292626ff9b5722f9276327ff29f5ed66cab769bf20d9a43550c79bb3e0507e
updated_at: 2026-04-10T00:00:00Z
---

# Twilio Migration Guide

Telnyx's Programmable Fax system for migrating from Twilio. Start building on Telnyx today.

\| [cURL](#curl) | [Python](#python) | [PHP](#php) | [Node](#node) | [Java](#java) | [.NET](#net) | [Ruby](#ruby) |

***

As of December 17th, Twilio will go forward with sunsetting support for their Programmable Fax offering. As such, we have outlined a step-by-step guide to make the transition to Telnyx's Programmable Fax system as painless as possible. This guide will inform and detail the process from start to finish to get you started using Fax with Telnyx!

Transitioning is quite simple, as the general configuration of the app mirrors Twilio's implementation. In most cases, the only change you will have to make in the code itself is the authentication parameters and the send function.

## cURL

### Part 1: Account configuration

To get started using Programmable Fax with Telnyx, you will be required to make an account and attain the following items. A guide on how to set this up can be found at our [Quickstart](../tutorial/quickstart-guide-for-programmable-fax.md)

You will ultimately need the following configured:

* A valid [Telnyx Portal Account](https://telnyx.com/sign-up)
* A [Telnyx Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles?utm_source=referral\&utm_medium=github_referral\&utm_campaign=cross-site-link) (If you are intending to send Faxes Outbound)
* A [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* A [Telnyx Phone Number](https://portal.telnyx.com/#/app/numbers/search-numbers) that's enabled with a [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)

Do note, to receive updates and status of your faxes (both inbound and outbound), you will need to setup a Webhook in the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications). This is where we will be sending you all information regarding the fax. For more information on this, you can scroll down to "Part 3: Recieving Faxes" section.

After your account is configured, take note of the following items that you will need to send your specified faxes programmatically.

* Your [API V2 Key](https://portal.telnyx.com/#/app/api-keys)
* Your App ID of the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* Your [Phone Number](https://portal.telnyx.com/#/app/numbers/my-numbers) that you procured from the previous step.

That's it from the portal perspective! With the 3 pieces of information from above we are ready to start sending and recieving faxes with Telnyx!

### Part 2: Sending faxes

Sending outbound faxes requires:

* A *To* number (Destination)
* A *From* number (Generally the number you have procured from above)
* A public facing URL which points to the document you are intending to send, in PDF format.

The code to initiate a fax sendoff would be as follows:

<Callout type="warning">Don't forget to update `YOUR_API_KEY` in the examples.

```
curl -X POST https://api.telnyx.com/v2/faxes \
  --data-urlencode "media_url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" \
  --data-urlencode "connection_id=YOUR_FAX_APP_ID" \
  --data-urlencode "to=YOUR_DESTINATION_NUMBER" \
  --data-urlencode "from=YOUR_FROM_NUMBER" \
  --header "Authorization: Bearer YOUR_API_KEY"
```

A successful example JSON response to the request will look like:

```bash theme={null}
{
  "data": {
    "connection_id": "c-1",
    "created_at": "2020-05-05T09:59:12",
    "direction": "outbound",
    "from": "+123",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "media_url": "http://www.example.com/fax.pdf",
    "quality": "high",
    "record_type": "fax",
    "status": "queued",
    "store_media": true,
    "stored_media_url": "https://s3.amazonaws.com/faxes-dev/user-1/cf4a6b52-bf8e-4945-9f49-611d0d2b083b.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=xxxxxxxxxx%2F20200505%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200505T095917Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=fac2af40464fcc77673ad762db86e34f9c1b91a82699b5578c5327f53874df51",
    "to": "+456",
    "updated_at": "2020-05-05T09:59:12",
    "webhook_failover_url": "",
    "webhook_url": "http://www.example.com/webhooks"
  }
}
```

### Part 3: Receiving faxes

In order to receive faxes, you will need to setup a webhook mentioned earlier.

In order for the webhooks in this tutorial to work, Telnyx must be able to send your web application an HTTP request over the Internet. That means your application needs to have a URL or IP address that Telnyx can reach. Telnyx sends webhooks to the URL or IP address to notify your application of incoming faxes.

For the purpose of this tutorial, we're using [ngrok](https://ngrok.com/), a popular tunneling tool used to expose a locally running application to the internet. ngrok gives you a public URL for a local port on your development machine, which you can use to configure your Telnyx webhooks as described above.

Download and install ngrok, then use it at the command line to create a tunnel to whatever port your web application is running on. For example, this command will create a public URL for a web application listening on port 3000.

```xml theme={null}
ngrok http 3000
```

After executing that command, you will see that ngrok has given your application a public URL that you can use in your webhook connection configuration in the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

<img alt="TwiML Twilio Telnyx Conference Flow" />

Grab your ngrok public URL and head back to the Programmable Fax Application you configured earlier. Now in the field under "Send a webhook to the URL" enter your new ngrok URL from either of the "Forwarding" URLs ngrok provided us with depending on if you want to use HTTP or HTTPS.

You're now all set up to receive webhooks for events related to inbound faxes. If you use the same Programmable Fax Application for sending faxes, you will receive events to the same ngrok URL you just created.

#### Example Webhooks

If you have set everything up correctly, any time an inbound fax is received you can expect to receive the following webhooks:

| Webhook Name                   | Description                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `fax.receiving.started`        | The fax has begun transmitting to Telnyx successfully.                       |
| `fax.media.processing.started` | Telnyx has received the fax and is generating the digital PDF file.          |
| `fax.received`                 | The PDF has been generated and the file is ready to be downloaded.           |
| `fax.failed`                   | Transmission of the fax failed. Check the `failure_reason` for more details. |

#### Fax has begun transmitting to Telnyx

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Fax transmission is complete and Telnyx is converting to PDF

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### PDF has been generated and is ready for download

The `media_url` field contains a signed AWS link to a PDF of the received fax. This URL is valid for 10 minutes before the file is no longer accessible so be sure to download the file if you wish to keep it!

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Uh oh, something has gone wrong and the fax failed

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

## Python

### Part 1: Account configuration

To get started using Programmable Fax with Telnyx, you will be required to make an account and attain the following items. A guide on how to set this up can be found at our [Quickstart](../tutorial/quickstart-guide-for-programmable-fax.md)

You will ultimately need the following configured:

* A valid [Telnyx Portal Account](https://telnyx.com/sign-up)
* A [Telnyx Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles?utm_source=referral\&utm_medium=github_referral\&utm_campaign=cross-site-link) (If you are intending to send Faxes Outbound)
* A [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* A [Telnyx Phone Number](https://portal.telnyx.com/#/app/numbers/search-numbers) that's enabled with a [Telnyx Fax Appliction](https://portal.telnyx.com/#/app/fax/applications)

Do note, to receive updates and status of your faxes (both inbound and outbound), you will need to setup a Webhook in the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications). This is where we will be sending you all information regarding the fax. For more information on this, you can scroll down to "Part 3: Recieving Faxes" section.

After your account is configured, take note of the following items that you will need to send your specified faxes programmatically.

* Your [API V2 Key](https://portal.telnyx.com/#/app/api-keys)
* Your App ID of the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* Your [Phone Number](https://portal.telnyx.com/#/app/numbers/my-numbers) that you procured from the previous step.

That's it from the portal perspective! With the 3 pieces of information from above we are ready to start sending and receiving faxes with Telnyx!

### Part 2: Sending Faxes

Sending outbound faxes requires:

* A *To* number (Destination)
* A *From* number (Generally the number you have procured from above)
* A public facing URL which points to the document you are intending to send, in PDF format.

The code to initiate a fax sendoff would be as follows:

```python theme={null}
import telnyx

telnyx.api_key = "YOUR_API_KEY"

fax_app_id = "YOUR_FAX_APP_ID"
your_telnyx_number = "YOUR_TELNYX_NUMBER"
desitnation_number = "YOUR_DESIRED_DESTINATION_NUMBER"

fax_send = telnyx.Fax.create(
            connection_id=TELNYX_FAX_CONNECTION_ID,
            to=to_phone_number,
            from_=from_phone_number,
            media_url=file_url
)
```

A successful example JSON response to the request will look like:

```bash theme={null}
{
  "data": {
    "connection_id": "c-1",
    "created_at": "2020-05-05T09:59:12",
    "direction": "outbound",
    "from": "+123",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "media_url": "http://www.example.com/fax.pdf",
    "quality": "high",
    "record_type": "fax",
    "status": "queued",
    "store_media": true,
    "stored_media_url": "https://s3.amazonaws.com/faxes-dev/user-1/cf4a6b52-bf8e-4945-9f49-611d0d2b083b.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=xxxxxxxxxx%2F20200505%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200505T095917Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=fac2af40464fcc77673ad762db86e34f9c1b91a82699b5578c5327f53874df51",
    "to": "+456",
    "updated_at": "2020-05-05T09:59:12",
    "webhook_failover_url": "",
    "webhook_url": "http://www.example.com/webhooks"
  }
}
```

### Part 3: Receiving faxes

In order to receive faxes, you will need to setup a webhook mentioned earlier.

In order for the webhooks in this tutorial to work, Telnyx must be able to send your web application an HTTP request over the Internet. That means your application needs to have a URL or IP address that Telnyx can reach. Telnyx sends webhooks to the URL or IP address to notify your application of incoming faxes.

For the purpose of this tutorial, we're using [ngrok](https://ngrok.com/), a popular tunneling tool used to expose a locally running application to the internet. ngrok gives you a public URL for a local port on your development machine, which you can use to configure your Telnyx webhooks as described above.

Download and install ngrok, then use it at the command line to create a tunnel to whatever port your web application is running on. For example, this command will create a public URL for a web application listening on port 3000.

```bash theme={null}
ngrok http 3000
```

After executing that command, you will see that ngrok has given your application a public URL that you can use in your webhook connection configuration in the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

<img alt="TwiML Twilio Telnyx Conference Flow" />

Grab your ngrok public URL and head back to the Programmable Fax Application you configured earlier. Now in the field under "Send a webhook to the URL" enter your new ngrok URL from either of the "Forwarding" URLs ngrok provided us with depending on if you want to use HTTP or HTTPS.

You're now all set up to receive webhooks for events related to inbound faxes. If you use the same Programmable Fax Application for sending faxes, you will receive events to the same ngrok URL you just created.

#### Example Webhooks

If you have set everything up correctly, any time an inbound fax is received you can expect to receive the following webhooks:

| Webhook Name                   | Description                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `fax.receiving.started`        | The fax has begun transmitting to Telnyx successfully.                       |
| `fax.media.processing.started` | Telnyx has received the fax and is generating the digital PDF file.          |
| `fax.received`                 | The PDF has been generated and the file is ready to be downloaded.           |
| `fax.failed`                   | Transmission of the fax failed. Check the `failure_reason` for more details. |

#### Fax has begun transmitting to Telnyx

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Fax transmission is complete and Telnyx is converting to PDF

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### PDF has been generated and is ready for download

The `media_url` field contains a signed AWS link to a PDF of the received fax. This URL is valid for 10 minutes before the file is no longer accessible so be sure to download the file if you wish to keep it!

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Uh oh, something has gone wrong and the fax failed

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

## PHP

### Part 1: Account configuration

To get started using Programmable Fax with Telnyx, you will be required to make an account and attain the following items. A guide on how to set this up can be found at our [Quickstart](../tutorial/quickstart-guide-for-programmable-fax.md)

You will ultimately need the following configured:

* A valid [Telnyx Portal Account](https://telnyx.com/sign-up)
* A [Telnyx Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles?utm_source=referral\&utm_medium=github_referral\&utm_campaign=cross-site-link) (If you are intending to send Faxes Outbound)
* A [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* A [Telnyx Phone Number](https://portal.telnyx.com/#/app/numbers/search-numbers) that's enabled with a [Telnyx Fax Appliction](https://portal.telnyx.com/#/app/fax/applications)

Do note, to receive updates and status of your faxes (both inbound and outbound), you will need to setup a Webhook in the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications). This is where we will be sending you all information regarding the fax. For more information on this, you can scroll down to "Part 3: Recieving Faxes" section.

After your account is configured, take note of the following items that you will need to send your specified faxes programmatically.

* Your [API V2 Key](https://portal.telnyx.com/#/app/api-keys)
* Your App ID of the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* Your [Phone Number](https://portal.telnyx.com/#/app/numbers/my-numbers) that you procured from the previous step.

That's it from the portal perspective! With the 3 pieces of information from above we are ready to start sending and receiving faxes with Telnyx!

### Part 2: Sending Faxes

Sending outbound faxes requires:

* A *To* number (Destination)
* A *From* number (Generally the number you have procured from above)
* A public facing URL which points to the document you are intending to send, in PDF format.

The code to initiate a fax sendoff would be as follows:

```php theme={null}
<?php
require_once __DIR__.'/vendor/autoload.php';

\Telnyx\Telnyx::setApiKey('YOUR_API_KEY');

$your_telnyx_number = 'YOUR_FROM_NUMBER';
$destination_number = 'YOUR_DESTINATION_NUMBER';
$connection_id = 'YOUR_CONNECTIONID';
$media_url = 'YOUR_MEDIA_URL';

$new_fax = \Telnyx\Message::Create(['from' => $your_telnyx_number, 'to' => $destination_number, 'connection_id' => $connection_id, 'media_url' => $media_url]);
```

A successful example JSON response to the request will look like:

```bash theme={null}
{
  "data": {
    "connection_id": "c-1",
    "created_at": "2020-05-05T09:59:12",
    "direction": "outbound",
    "from": "+123",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "media_url": "http://www.example.com/fax.pdf",
    "quality": "high",
    "record_type": "fax",
    "status": "queued",
    "store_media": true,
    "stored_media_url": "https://s3.amazonaws.com/faxes-dev/user-1/cf4a6b52-bf8e-4945-9f49-611d0d2b083b.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=xxxxxxxxxx%2F20200505%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200505T095917Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=fac2af40464fcc77673ad762db86e34f9c1b91a82699b5578c5327f53874df51",
    "to": "+456",
    "updated_at": "2020-05-05T09:59:12",
    "webhook_failover_url": "",
    "webhook_url": "http://www.example.com/webhooks"
  }
}
```

### Part 3: Receiving faxes

In order to receive faxes, you will need to setup a webhook mentioned earlier.

In order for the webhooks in this tutorial to work, Telnyx must be able to send your web application an HTTP request over the Internet. That means your application needs to have a URL or IP address that Telnyx can reach. Telnyx sends webhooks to the URL or IP address to notify your application of incoming faxes.

For the purpose of this tutorial, we're using [ngrok](https://ngrok.com/), a popular tunneling tool used to expose a locally running application to the internet. ngrok gives you a public URL for a local port on your development machine, which you can use to configure your Telnyx webhooks as described above.

Download and install ngrok, then use it at the command line to create a tunnel to whatever port your web application is running on. For example, this command will create a public URL for a web application listening on port 3000.

```bash theme={null}
ngrok http 3000
```

After executing that command, you will see that ngrok has given your application a public URL that you can use in your webhook connection configuration in the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

<img alt="TwiML Twilio Telnyx Conference Flow" />

Grab your ngrok public URL and head back to the Programmable Fax Application you configured earlier. Now in the field under "Send a webhook to the URL" enter your new ngrok URL from either of the "Forwarding" URLs ngrok provided us with depending on if you want to use HTTP or HTTPS.

You're now all set up to receive webhooks for events related to inbound faxes. If you use the same Programmable Fax Application for sending faxes, you will receive events to the same ngrok URL you just created.

#### Example Webhooks

If you have set everything up correctly, any time an inbound fax is received you can expect to receive the following webhooks:

| Webhook Name                   | Description                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `fax.receiving.started`        | The fax has begun transmitting to Telnyx successfully.                       |
| `fax.media.processing.started` | Telnyx has received the fax and is generating the digital PDF file.          |
| `fax.received`                 | The PDF has been generated and the file is ready to be downloaded.           |
| `fax.failed`                   | Transmission of the fax failed. Check the `failure_reason` for more details. |

#### Fax has begun transmitting to Telnyx

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Fax transmission is complete and Telnyx is converting to PDF

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### PDF has been generated and is ready for download

The `media_url` field contains a signed AWS link to a PDF of the received fax. This URL is valid for 10 minutes before the file is no longer accessible so be sure to download the file if you wish to keep it!

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Uh oh, something has gone wrong and the fax failed

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

## Node

### Part 1: Account Configuration

To get started using Programmable Fax with Telnyx, you will be required to make an account and attain the following items. A guide on how to set this up can be found at our [Quickstart](../tutorial/quickstart-guide-for-programmable-fax.md)

You will ultimately need the following configured:

* A valid [Telnyx Portal Account](https://telnyx.com/sign-up)
* A [Telnyx Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles?utm_source=referral\&utm_medium=github_referral\&utm_campaign=cross-site-link) (If you are intending to send Faxes Outbound)
* A [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* A [Telnyx Phone Number](https://portal.telnyx.com/#/app/numbers/search-numbers) that's enabled with a [Telnyx Fax Appliction](https://portal.telnyx.com/#/app/fax/applications)

Do note, to receive updates and status of your faxes (both inbound and outbound), you will need to setup a Webhook in the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications). This is where we will be sending you all information regarding the fax. For more information on this, you can scroll down to "Part 3: Recieving Faxes" section.

After your account is configured, take note of the following items that you will need to send your specified faxes programmatically.

* Your [API V2 Key](https://portal.telnyx.com/#/app/api-keys)
* Your App ID of the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* Your [Phone Number](https://portal.telnyx.com/#/app/numbers/my-numbers) that you procured from the previous step.

That's it from the portal perspective! With the 3 pieces of information from above we are ready to start sending and receiving faxes with Telnyx!

### Part 2: Sending Faxes

Sending outbound faxes requires:

* A *To* number (Destination)
* A *From* number (Generally the number you have procured from above)
* A public facing URL which points to the document you are intending to send, in PDF format.

The code to initiate a fax sendoff would be as follows:

```javascript theme={null}
import Telnyx from 'telnyx';

const telnyx = new Telnyx("YOUR_API_KEY");

telnyx.faxes.create(
 {
   'from': 'YOUR_FROM_NUMBER',
   'to': 'YOUR_DESTINATION_NUMBER',
   'connection_id': 'YOUR_FAX_APP_ID'
   'media_url': 'YOUR_MEDIA_URL'
 },
 function(err, response) {
   // asynchronously called
   console.log(response);
 }
);
```

A successful example JSON response to the request will look like:

```bash theme={null}
{
  "data": {
    "connection_id": "c-1",
    "created_at": "2020-05-05T09:59:12",
    "direction": "outbound",
    "from": "+123",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "media_url": "http://www.example.com/fax.pdf",
    "quality": "high",
    "record_type": "fax",
    "status": "queued",
    "store_media": true,
    "stored_media_url": "https://s3.amazonaws.com/faxes-dev/user-1/cf4a6b52-bf8e-4945-9f49-611d0d2b083b.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=xxxxxxxxxx%2F20200505%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200505T095917Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=fac2af40464fcc77673ad762db86e34f9c1b91a82699b5578c5327f53874df51",
    "to": "+456",
    "updated_at": "2020-05-05T09:59:12",
    "webhook_failover_url": "",
    "webhook_url": "http://www.example.com/webhooks"
  }
}
```

### Part 3: Receiving Faxes

In order to receive faxes, you will need to setup a webhook mentioned earlier.

In order for the webhooks in this tutorial to work, Telnyx must be able to send your web application an HTTP request over the Internet. That means your application needs to have a URL or IP address that Telnyx can reach. Telnyx sends webhooks to the URL or IP address to notify your application of incoming faxes.

For the purpose of this tutorial, we're using [ngrok](https://ngrok.com/), a popular tunneling tool used to expose a locally running application to the internet. ngrok gives you a public URL for a local port on your development machine, which you can use to configure your Telnyx webhooks as described above.

Download and install ngrok, then use it at the command line to create a tunnel to whatever port your web application is running on. For example, this command will create a public URL for a web application listening on port 3000.

```xml theme={null}
ngrok http 3000
```

After executing that command, you will see that ngrok has given your application a public URL that you can use in your webhook connection configuration in the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

<img alt="TwiML Twilio Telnyx Conference Flow" />

Grab your ngrok public URL and head back to the Programmable Fax Application you configured earlier. Now in the field under "Send a webhook to the URL" enter your new ngrok URL from either of the "Forwarding" URLs ngrok provided us with depending on if you want to use HTTP or HTTPS.

You're now all set up to receive webhooks for events related to inbound faxes. If you use the same Programmable Fax Application for sending faxes, you will receive events to the same ngrok URL you just created.

#### Example Webhooks

If you have set everything up correctly, any time an inbound fax is received you can expect to receive the following webhooks:

| Webhook Name                   | Description                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `fax.receiving.started`        | The fax has begun transmitting to Telnyx successfully.                       |
| `fax.media.processing.started` | Telnyx has received the fax and is generating the digital PDF file.          |
| `fax.received`                 | The PDF has been generated and the file is ready to be downloaded.           |
| `fax.failed`                   | Transmission of the fax failed. Check the `failure_reason` for more details. |

#### Fax has begun transmitting to Telnyx

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Fax transmission is complete and Telnyx is converting to PDF

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### PDF has been generated and is ready for download

The `media_url` field contains a signed AWS link to a PDF of the received fax. This URL is valid for 10 minutes before the file is no longer accessible so be sure to download the file if you wish to keep it!

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Uh oh, something has gone wrong and the fax failed

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

## Java

### Part 1: Account Configuration

To get started using Programmable Fax with Telnyx, you will be required to make an account and attain the following items. A guide on how to set this up can be found at our [Quickstart](../tutorial/quickstart-guide-for-programmable-fax.md)

You will ultimately need the following configured:

* A valid [Telnyx Portal Account](https://telnyx.com/sign-up)
* A [Telnyx Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles?utm_source=referral\&utm_medium=github_referral\&utm_campaign=cross-site-link) (If you are intending to send Faxes Outbound)
* A [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* A [Telnyx Phone Number](https://portal.telnyx.com/#/app/numbers/search-numbers) that's enabled with a [Telnyx Fax Appliction](https://portal.telnyx.com/#/app/fax/applications)

Do note, to receive updates and status of your faxes (both inbound and outbound), you will need to setup a Webhook in the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications). This is where we will be sending you all information regarding the fax. For more information on this, you can scroll down to "Part 3: Receiving Faxes" section.

After your account is configured, take note of the following items that you will need to send your specified faxes programmatically.

* Your [API V2 Key](https://portal.telnyx.com/#/app/api-keys)
* Your App ID of the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* Your [Phone Number](https://portal.telnyx.com/#/app/numbers/my-numbers) that you procured from the previous step.

That's it from the portal perspective! With the 3 pieces of information from above we are ready to start sending and receiving faxes with Telnyx!

### Part 2: Sending faxes

Sending outbound faxes requires:

* A *To* number (Destination)
* A *From* number (Generally the number you have procured from above)
* A public facing URL which points to the document you are intending to send, in PDF format.

The code to initiate a fax sendoff would be as follows:

```
curl -X POST https://api.telnyx.com/v2/faxes \
--data-urlencode "media_url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" \
--data-urlencode "connection_id=YOUR_FAX_APP_ID" \
--data-urlencode "to=YOUR_DESTINATION_NUMBER" \
--data-urlencode "from=YOUR_FROM_NUMBER" \
--header "Authorization: Bearer YOUR_API_KEY"
```

A successful example JSON response to the request will look like:

```
{
  "data": {
    "connection_id": "c-1",
    "created_at": "2020-05-05T09:59:12",
    "direction": "outbound",
    "from": "+123",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "media_url": "http://www.example.com/fax.pdf",
    "quality": "high",
    "record_type": "fax",
    "status": "queued",
    "store_media": true,
    "stored_media_url": "https://s3.amazonaws.com/faxes-dev/user-1/cf4a6b52-bf8e-4945-9f49-611d0d2b083b.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=xxxxxxxxxx%2F20200505%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200505T095917Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=fac2af40464fcc77673ad762db86e34f9c1b91a82699b5578c5327f53874df51",
    "to": "+456",
    "updated_at": "2020-05-05T09:59:12",
    "webhook_failover_url": "",
    "webhook_url": "http://www.example.com/webhooks"
  }
}
```

### Part 3: Receiving faxes

In order to receive faxes, you will need to setup a webhook mentioned earlier.

In order for the webhooks in this tutorial to work, Telnyx must be able to send your web application an HTTP request over the Internet. That means your application needs to have a URL or IP address that Telnyx can reach. Telnyx sends webhooks to the URL or IP address to notify your application of incoming faxes.

For the purpose of this tutorial, we're using [ngrok](https://ngrok.com/), a popular tunneling tool used to expose a locally running application to the internet. ngrok gives you a public URL for a local port on your development machine, which you can use to configure your Telnyx webhooks as described above.

Download and install ngrok, then use it at the command line to create a tunnel to whatever port your web application is running on. For example, this command will create a public URL for a web application listening on port 3000.

```bash theme={null}
ngrok http 3000
```

After executing that command, you will see that ngrok has given your application a public URL that you can use in your webhook connection configuration in the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

<img alt="TwiML Twilio Telnyx Conference Flow" />

Grab your ngrok public URL and head back to the Programmable Fax Application you configured earlier. Now in the field under "Send a webhook to the URL" enter your new ngrok URL from either of the "Forwarding" URLs ngrok provided us with depending on if you want to use HTTP or HTTPS.

You're now all set up to receive webhooks for events related to inbound faxes. If you use the same Programmable Fax Application for sending faxes, you will receive events to the same ngrok URL you just created.

#### Example Webhooks

If you have set everything up correctly, any time an inbound fax is received you can expect to receive the following webhooks:

| Webhook Name                   | Description                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `fax.receiving.started`        | The fax has begun transmitting to Telnyx successfully.                       |
| `fax.media.processing.started` | Telnyx has received the fax and is generating the digital PDF file.          |
| `fax.received`                 | The PDF has been generated and the file is ready to be downloaded.           |
| `fax.failed`                   | Transmission of the fax failed. Check the `failure_reason` for more details. |

#### Fax has begun transmitting to Telnyx

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Fax transmission is complete and Telnyx is converting to PDF

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### PDF has been generated and is ready for download

The `media_url` field contains a signed AWS link to a PDF of the received fax. This URL is valid for 10 minutes before the file is no longer accessible so be sure to download the file if you wish to keep it!

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Uh oh, something has gone wrong and the fax failed

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

## .NET

### Part 1: Account configuration

To get started using Programmable Fax with Telnyx, you will be required to make an account and attain the following items. A guide on how to set this up can be found at our [Quickstart](../tutorial/quickstart-guide-for-programmable-fax.md)

You will ultimately need the following configured:

* A valid [Telnyx Portal Account](https://telnyx.com/sign-up)
* A [Telnyx Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles?utm_source=referral\&utm_medium=github_referral\&utm_campaign=cross-site-link) (If you are intending to send Faxes Outbound)
* A [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* A [Telnyx Phone Number](https://portal.telnyx.com/#/app/numbers/search-numbers) that's enabled with a [Telnyx Fax Appliction](https://portal.telnyx.com/#/app/fax/applications)

Do note, to recieve updates and status of your faxes (both inbound and outbound), you will need to setup a Webhook in the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications). This is where we will be sending you all information regarding the fax. For more information on this, you can scroll down to "Part 3: Recieving Faxes" section.

After your account is configured, take note of the following items that you will need to send your specified faxes programmatically.

* Your [API V2 Key](https://portal.telnyx.com/#/app/api-keys)
* Your App ID of the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* Your [Phone Number](https://portal.telnyx.com/#/app/numbers/my-numbers) that you procured from the previous step.

That's it from the portal perspective! With the 3 pieces of information from above we are ready to start sending and recieving faxes with Telnyx!

### Part 2: Sending faxes

Sending outbound faxes requires:

* A *To* number (Destination)
* A *From* number (Generally the number you have procured from above)
* A public facing URL which points to the document you are intending to send, in PDF format.

Follow the steps below to send Fax messages with dotnet core v3.1+

1. Using the dotnet CLI create a new console application and change directories to the newly created folder. Then add the Telnyx.net package.

```bash theme={null}
$ dotnet new console --output send-fax
$ cd send-fax
$ dotnet add package Telnyx.net
```

2. Open the 'Program.cs' file created for you in the directory. It should look something like the code below:

```csharp theme={null}
using System;

namespace send_sms
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
```

3. Tell the application to use Telnyx.net by adding: `using Telnyx;` before the `namespace`
4. In order to use the Asynchronous methods, we need to modify our Main method to return a Task and make it async.
   4.1 `static void Main(string[] args)` should be `static async Task Main(string[] args)
     4.2 Add `using System.Threading.Tasks;`before the`namespace\`

A successful example JSON response to the request will look like:

```bash theme={null}
{
  "data": {
    "connection_id": "c-1",
    "created_at": "2020-05-05T09:59:12",
    "direction": "outbound",
    "from": "+123",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "media_url": "http://www.example.com/fax.pdf",
    "quality": "high",
    "record_type": "fax",
    "status": "queued",
    "store_media": true,
    "stored_media_url": "https://s3.amazonaws.com/faxes-dev/user-1/cf4a6b52-bf8e-4945-9f49-611d0d2b083b.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=xxxxxxxxxx%2F20200505%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200505T095917Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=fac2af40464fcc77673ad762db86e34f9c1b91a82699b5578c5327f53874df51",
    "to": "+456",
    "updated_at": "2020-05-05T09:59:12",
    "webhook_failover_url": "",
    "webhook_url": "http://www.example.com/webhooks"
  }
}
```

### Part 3: Recieving faxes

In order to receive faxes, you will need to setup a webhook mentioned earlier.

In order for the webhooks in this tutorial to work, Telnyx must be able to send your web application an HTTP request over the Internet. That means your application needs to have a URL or IP address that Telnyx can reach. Telnyx sends webhooks to the URL or IP address to notify your application of incoming faxes.

For the purpose of this tutorial, we're using [ngrok](https://ngrok.com/), a popular tunneling tool used to expose a locally running application to the internet. ngrok gives you a public URL for a local port on your development machine, which you can use to configure your Telnyx webhooks as described above.

Download and install ngrok, then use it at the command line to create a tunnel to whatever port your web application is running on. For example, this command will create a public URL for a web application listening on port 3000.

```bash theme={null}
ngrok http 3000
```

After executing that command, you will see that ngrok has given your application a public URL that you can use in your webhook connection configuration in the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

<img alt="TwiML Twilio Telnyx Conference Flow" />

Grab your ngrok public URL and head back to the Programmable Fax Application you configured earlier. Now in the field under "Send a webhook to the URL" enter your new ngrok URL from either of the "Forwarding" URLs ngrok provided us with depending on if you want to use HTTP or HTTPS.

You're now all set up to receive webhooks for events related to inbound faxes. If you use the same Programmable Fax Application for sending faxes, you will receive events to the same ngrok URL you just created.

#### Example Webhooks

If you have set everything up correctly, any time an inbound fax is received you can expect to receive the following webhooks:

| Webhook Name                   | Description                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `fax.receiving.started`        | The fax has begun transmitting to Telnyx successfully.                       |
| `fax.media.processing.started` | Telnyx has received the fax and is generating the digital PDF file.          |
| `fax.received`                 | The PDF has been generated and the file is ready to be downloaded.           |
| `fax.failed`                   | Transmission of the fax failed. Check the `failure_reason` for more details. |

#### Fax has begun transmitting to Telnyx

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Fax transmission is complete and Telnyx is converting to PDF

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### PDF has been generated and is ready for download

The `media_url` field contains a signed AWS link to a PDF of the received fax. This URL is valid for 10 minutes before the file is no longer accessible so be sure to download the file if you wish to keep it!

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Uh oh, something has gone wrong and the fax failed

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

## Ruby

### Part 1: Account configuration

To get started using Programmable Fax with Telnyx, you will be required to make an account and attain the following items. A guide on how to set this up can be found at our [Quickstart](../tutorial/quickstart-guide-for-programmable-fax.md)

You will ultimately need the following configured:

* A valid [Telnyx Portal Account](https://telnyx.com/sign-up)
* A [Telnyx Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles?utm_source=referral\&utm_medium=github_referral\&utm_campaign=cross-site-link) (If you are intending to send Faxes Outbound)
* A [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* A [Telnyx Phone Number](https://portal.telnyx.com/#/app/numbers/search-numbers) that's enabled with a [Telnyx Fax Appliction](https://portal.telnyx.com/#/app/fax/applications)

Do note, to recieve updates and status of your faxes (both inbound and outbound), you will need to setup a Webhook in the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications). This is where we will be sending you all information regarding the fax. For more information on this, you can scroll down to "Part 3: Recieving Faxes" section.

After your account is configured, take note of the following items that you will need to send your specified faxes programmatically.

* Your [API V2 Key](https://portal.telnyx.com/#/app/api-keys)
* Your App ID of the [Telnyx Fax Application](https://portal.telnyx.com/#/app/fax/applications)
* Your [Phone Number](https://portal.telnyx.com/#/app/numbers/my-numbers) that you procured from the previous step.

That's it from the portal perspective! With the 3 pieces of information from above we are ready to start sending and recieving faxes with Telnyx!

### Part 2: Sending faxes

Sending outbound faxes requires:

* A *To* number (Destination)
* A *From* number (Generally the number you have procured from above)
* A public facing URL which points to the document you are intending to send, in PDF format.

The code to initiate a fax sendoff would be as follows:

```
curl -X POST https://api.telnyx.com/v2/faxes \
--data-urlencode "media_url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" \
--data-urlencode "connection_id=YOUR_FAX_APP_ID" \
--data-urlencode "to=YOUR_DESTINATION_NUMBER" \
--data-urlencode "from=YOUR_FROM_NUMBER" \
--header "Authorization: Bearer YOUR_API_KEY"
```

A successful example JSON response to the request will look like:

```bash theme={null}
{
  "data": {
    "connection_id": "c-1",
    "created_at": "2020-05-05T09:59:12",
    "direction": "outbound",
    "from": "+123",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "media_url": "http://www.example.com/fax.pdf",
    "quality": "high",
    "record_type": "fax",
    "status": "queued",
    "store_media": true,
    "stored_media_url": "https://s3.amazonaws.com/faxes-dev/user-1/cf4a6b52-bf8e-4945-9f49-611d0d2b083b.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=xxxxxxxxxx%2F20200505%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200505T095917Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=fac2af40464fcc77673ad762db86e34f9c1b91a82699b5578c5327f53874df51",
    "to": "+456",
    "updated_at": "2020-05-05T09:59:12",
    "webhook_failover_url": "",
    "webhook_url": "http://www.example.com/webhooks"
  }
}
```

### Part 3: Receiving faxes

In order to receive faxes, you will need to setup a webhook mentioned earlier.

In order for the webhooks in this tutorial to work, Telnyx must be able to send your web application an HTTP request over the Internet. That means your application needs to have a URL or IP address that Telnyx can reach. Telnyx sends webhooks to the URL or IP address to notify your application of incoming faxes.

For the purpose of this tutorial, we're using [ngrok](https://ngrok.com/), a popular tunneling tool used to expose a locally running application to the internet. ngrok gives you a public URL for a local port on your development machine, which you can use to configure your Telnyx webhooks as described above.

Download and install ngrok, then use it at the command line to create a tunnel to whatever port your web application is running on. For example, this command will create a public URL for a web application listening on port 3000.

```bash theme={null}
ngrok http 3000
```

After executing that command, you will see that ngrok has given your application a public URL that you can use in your webhook connection configuration in the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

<img alt="TwiML Twilio Telnyx Conference Flow" />

Grab your ngrok public URL and head back to the Programmable Fax Application you configured earlier. Now in the field under "Send a webhook to the URL" enter your new ngrok URL from either of the "Forwarding" URLs ngrok provided us with depending on if you want to use HTTP or HTTPS.

You're now all set up to receive webhooks for events related to inbound faxes. If you use the same Programmable Fax Application for sending faxes, you will receive events to the same ngrok URL you just created.

#### Example Webhooks

If you have set everything up correctly, any time an inbound fax is received you can expect to receive the following webhooks:

| Webhook Name                   | Description                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `fax.receiving.started`        | The fax has begun transmitting to Telnyx successfully.                       |
| `fax.media.processing.started` | Telnyx has received the fax and is generating the digital PDF file.          |
| `fax.received`                 | The PDF has been generated and the file is ready to be downloaded.           |
| `fax.failed`                   | Transmission of the fax failed. Check the `failure_reason` for more details. |

#### Fax has begun transmitting to Telnyx

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Fax transmission is complete and Telnyx is converting to PDF

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### PDF has been generated and is ready for download

The `media_url` field contains a signed AWS link to a PDF of the received fax. This URL is valid for 10 minutes before the file is no longer accessible so be sure to download the file if you wish to keep it!

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```

#### Uh oh, something has gone wrong and the fax failed

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
      "user_id": "19a75cea-02c6-4b9a-84fa-c9bc8341feb8"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://1a3097.ngrok.io/"
  }
}
```


## Related Pages

- [OpenAI API Migration Guide](../runbooks/openai-api-migration-guide.md)
