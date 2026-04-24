---
title: Send a Fax via API
summary: Telnyx offers powerful faxing capabilities through our programmable fax API.
sources:
  - url: https://developers.telnyx.com/docs/programmable-fax/send-a-fax-api/index
    content_hash: 0e479075904a816cfef1d48eed01ffdc4e582cadff4e6fd8fe2772c6051447d6
updated_at: 2026-04-10T00:00:00Z
---

# Send a Fax via API

Telnyx offers powerful faxing capabilities through our programmable fax API. In this tutorial, we'll show you how to send a fax using our API. With just a few simple steps, you can have your faxes sent quickly and easily.

The Telnyx Programmable Fax API lets you send, receive, and manage faxes through a set of easy-to-use HTTP endpoints.

In this guide, you'll learn how to send a fax using the Programmable Fax API in four simple steps.

## Step 1: Setting up with Telnyx

### Setup a Telnyx account, phone number, and programmable fax application

First, follow our [Quickstart](../tutorial/quickstart-guide-for-programmable-fax.md) guide to create a Telnyx account, phone number, and Fax Application.

## Step 2: API authentication

> If you already have a Telnyx V2 API Authentication key, skip to Step 3.

1. In the Telnyx <a href="https://portal.telnyx.com/">
   Mission Control Portal
   </a>, in the left menu bar navigate to "<a href="https://portal.telnyx.com/#/app/api-keys">
   API Keys
   </a>".
2. Ensure, API V2 is selected in the horizontal menu bar.
3. Click "Create API key"
4. Copy the API key and save it somewhere safe.

## Step 3: Send a PDF with the programmable fax API using curl

The Telnyx Programmable Fax API supports PDF files. To initiate sending a fax, we need to send the request to the Telnyx Programmable Fax API endpoint `https://api.telnyx.com/v2/faxes`.

We need to send additional parameters containing authentication information with the request, so Telnyx knows which account to send the fax from and information about the destination and file being sent.

<table>
  <tbody>
    <tr>
      <td>Header</td>
      <td>Description</td>
    </tr>

    <tr>
      <td>media\_url</td>
      <td>The URL of the PDF used for the fax's media.</td>
    </tr>

    <tr>
      <td>connection\_id</td>
      <td>The app ID or connection ID to send the fax with.</td>
    </tr>

    <tr>
      <td>to</td>
      <td>The fax enabled phone number (in E.164 format), or SIP URI, the fax will be sent to.</td>
    </tr>

    <tr>
      <td>from</td>
      <td>The phone number, in E.164 format, the fax will be sent from.</td>
    </tr>

    <tr>
      <td>Authorizaton: Bearer</td>
      <td>The prefix to your API V2 key created in Step 2.</td>
    </tr>
  </tbody>
</table>

Now that we know what we need to include in our request, we can use a number of different methods to structure and send it. In this example, we are going to use <code>curl</code> straight from the command line. You can also use a client such as <a href="https://www.postman.com/">
Postman
</a> to structure your request.

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/faxes \
--data-urlencode "media_url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" \
--data-urlencode "connection_id=1232154810234" \
--data-urlencode "to=+13129457420" \
--data-urlencode "from=+19459457421" \
--header "Authorization: Bearer APIAuthKey_fromPortal"
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Simply copy the above code into your favorite text editor, paste in your parameters from the table in place of the existing data, and execute the command.

## Step 4: Verify HTTP response and receive webhooks

If you have successfully structured your command and the fax has begun sending, the Programmable Fax API will respond with <code>HTTP 202</code>.

If you do not receive a <code>HTTP 202</code> response, double-check your request and try again. Explanations of other response codes can be found in our [API reference](sending-commands.md#response-when-sending-command).

Once the request to send the fax has been successfullly received by Telnyx, you should begin receiving a series of webhooks to the URL that you specified in your Fax Application.

The webhooks you should receive are:

* `fax.queued`
* `fax.media.processed`
* `fax.sending.started`
* `fax.delivered`
* `fax.failed`

That's it! Once you've received a `fax.delivered` webhook, your fax has been delivered to its destinaion.

## Webhook examples

#### On successful delivery

```json theme={null}
{
  "event_type": "fax.delivered",
  "id": "3320554f-6b74-4138-a74b-a1e2ec7eaf8b",
  "occurred_at": "2022-01-07T10:01:43.677850Z",
  "payload": {
    "call_duration_secs": 79,
    "connection_id": "1232154810234",
    "direction": "outbound",
    "fax_id": "c62be5bc-9b13-4b6c-abda-34dd8b541287",
    "from": "+19459457421",
    "original_media_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    "page_count": 1,
    "status": "delivered",
    "to": "+13129457420",
    "user_id": "bdaa1f9f-1018-4156-867d-6c4ac9f556eb"
  }
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

#### On failed delivery

```json theme={null}
{
  "event_type": "fax.failed",
  "id": "d906ecda-db21-428e-9ca0-74dae7e7c144",
  "occurred_at": "2022-01-05T22:23:46.888808Z",
  "payload": {
    "connection_id": "1232154810234",
    "direction": "outbound",
    "failure_reason": "user_busy",
    "fax_id": "f7b303ed-674c-4962-951b-848380510893",
    "from": "+19459457421",
    "original_media_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    "status": "failed",
    "to": "+13129457420",
    "user_id": "417b0cc2-39e0-4ab9-b116-e56543649aa9"
  }
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

#### Possible failure reasons

Inspect the `failure_reason` field in webhook's payload to debug failed deliveries of your faxes. The possible failure reasons are:

* `account_disabled`
* `connection_channel_limit_exceeded`
* `destination_invalid`
* `destination_not_in_countries_whitelist`
* `destination_not_in_service_plan`
* `destination_unreachable`
* `fax_initial_communication_timeout`
* `fax_signaling_error`
* `invalid_ecm_response_from_receiver`
* `no_outbound_profile`
* `outbound_profile_channel_limit_exceeded`
* `outbound_profile_daily_spend_limit_exceeded`
* `receiver_call_dropped`
* `receiver_communication_error`
* `receiver_decline`
* `receiver_incompatible_destination`
* `receiver_invalid_number_format`
* `receiver_no_answer`
* `receiver_no_response`
* `receiver_recovery_on_timer_expire`
* `receiver_unallocated_number`
* `service_unavailable`
* `user_busy`
* `user_channel_limit_exceeded`

## Where to next?

Continue to our next tutorial to learn how to [receive inbound faxes](receive-a-fax-via-api.md) via API.


## Related Pages

- [Receive a Fax via API](../runbooks/receive-a-fax-via-api.md)
