---
title: Receiving Webhooks for Programmable Fax
summary: Telnyx's Programmable Fax API allows you to easily send and receive faxes from your applications.
sources:
  - url: https://developers.telnyx.com/docs/programmable-fax/receiving-webhooks/index
    content_hash: dd65c1eb4f7be8746994d7d471477809decdb2278fbd0d2fab79f27f8a111a0f
updated_at: 2026-04-10T00:00:00Z
---

# Receiving Webhooks for Programmable Fax

Telnyx's Programmable Fax API allows you to easily send and receive faxes from your applications. With our easy-to-use webhooks, you can quickly get notified when a fax is sent or received.

When you send a Programmable Fax command and receive a successful response (i.e. 200 OK), you can expect to receive a webhook. The webhook will be delivered to the primary URL specified on the Application associated with the call. If that URL does not resolve, or your application returns a non 200 OK response, the webhook will be delivered to the failover URL, if one has been specified.

In order to minimize webhook delivery time, Telnyx:

* does not enforce the order in which webhooks are delivered
* retries webhook delivery if your application does not respond within a certain time threshold.

As a result, you may encounter:

* out-of-order webhooks
* simultaneous (or near simultaneous) webhooks
* duplicate webhooks

Duplicate webhooks may cause your application to issue duplicate commands. You can instruct Telnyx to ignore duplicate commands by sending a command\_id parameter as part of your commands. Commands with duplicate `command_ids` within 60 seconds will be ignored.

## Example: Receiving a webhook from an outbound fax

When you place an outbound fax, you will receive a number of webhooks indicating the current status of the fax. The first webhook you will receive will have A queued status indicating that Telnyx successfully received the request to send the fax.

```json theme={null}
{
  "data": {
    "event_type": "fax.queued",
    "id": "3691d047-d22a-424d-80ed-fe871981aa6d",
    "occurred_at": "2020-04-22T19:32:12.538002Z",
    "record_type": "event",
    "payload": {
      "call_duration_secs": 50,
      "connection_id": "7267xxxxxxxxxxxxxx",
      "direction": "outbound",
      "fax_id": "b679398e-8b4c-46bd-8630-6797f1ab5228",
      "from": "+35319605860",
      "original_media_url": "https://www.telnyx.com/telnyx-fax/1.pdf",
      "partial_content": true,
      "status": "queued",
      "to": "+13129457420",
      "user_id": "a5b1dfa3-fd2e-4e02-8ea4-xxxxxxxxxxxx"
    }
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "http://example.com/webhooks"
  }
}
```

<table>
  <tbody>
    <tr>
      <td>FIELD</td>
      <td>VALUE</td>
    </tr>

    <tr>
      <td>record\_type</td>
      <td>Description of the record.</td>
    </tr>

    <tr>
      <td>id</td>
      <td>unique id for the webhook</td>
    </tr>

    <tr>
      <td>event\_type</td>
      <td>The type of event</td>
    </tr>

    <tr>
      <td>occurred\_at</td>
      <td>ISO-8601 datetime of when event occured</td>
    </tr>

    <tr>
      <td>to</td>
      <td>Destination number or SIP URI of the call</td>
    </tr>

    <tr>
      <td>from</td>
      <td>Number or SIP URI placing the call</td>
    </tr>

    <tr>
      <td>fax\_id</td>
      <td>Unique ID for the Programmable Fax</td>
    </tr>

    <tr>
      <td>client\_state</td>
      <td>Configurable state to track commands</td>
    </tr>

    <tr>
      <td>status</td>
      <td>Can be one of <code>queued</code>, <code>media.processed</code>, <code>sending.started</code>, <code>delivered</code>, <code>failed</code></td>
    </tr>
  </tbody>
</table>

## Example: Receiving a webhook on successful fax delivery

```bash theme={null}
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

## Example: Receiving a webhook on failed fax delivery

```bash theme={null}
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

## Possible failure reasons

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
* `unverified_destination_not_allowed`
* `unverified_origination_number`
* `user_busy`
* `user_channel_limit_exceeded`


## Related Pages

- [Receiving Webhooks for Programmable Voice](../runbooks/receiving-webhooks-for-programmable-voice.md)
- [Receiving Webhooks for Messaging](../runbooks/receiving-webhooks-for-messaging.md)
- [Receiving Webhooks for Telnyx Verify](../runbooks/receiving-webhooks-for-telnyx-verify.md)
- [Sending Commands for Programmable Voice](../runbooks/sending-commands-for-programmable-voice.md)
- [Quickstart Guide for Programmable Fax](../tutorial/quickstart-guide-for-programmable-fax.md)
