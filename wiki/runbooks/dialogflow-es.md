---
title: Dialogflow ES
summary: Telnyx's Dialogflow tutorial will teach you how to create and manage sophisticated voice interactions with your customers.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es/index
    content_hash: d4d73220eddd95482329ca039146478ec7dcf4276525eef9dcd3993a56ebcc0f
updated_at: 2026-04-10T00:00:00Z
---

# Dialogflow ES

Telnyx's Dialogflow tutorial will teach you how to create and manage sophisticated voice interactions with your customers.

Telnyx's Dialogflow tutorial will teach you how to create and manage sophisticated voice interactions with your customers.

In this tutorial, you will learn how to integrate your instance of Dialogflow ES, so that you can send the audio from the call to it and get the response from your bot plated on the call.

## Getting started

In order to do successfully integrate Dialogflow ES with Telnyx Voice API, you'll need to start by assigning the Dialogflow configuration to your Voice API application using the following update request.

### Dialogflow Connections request sample

<Callout type="info">
  *Don't forget to update `YOUR_API_KEY` here.*

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{ \
    service_account: “GOOGLE_APPLICATION_CREDENTIALS”
  }' \
  https://api.telnyx.com/v2/dialogflow_connections/{connection_id}
```

*Note that GOOGLE\_APPLICATION\_CREDENTIALS must be provided in a form of encoded json.*
<a href="https://cloud.google.com/dialogflow/es/docs/quick/setup#sa-create">Google Dialogflow Setup</a>.

When the configuration is assigned to the application users can enable the Dialogflow integration for every outbound or inbound call.

## Enabling dialogflow for outbound calls

```
curl --location --request POST 'https://api.telnyx.com/v2/calls' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "to":"+48662211095",
  "from":"+13127367481",
  "connection_id":"1714376719458109299",
  "enable_dialogflow": true
}'
```

## Enabling dialogflow for inbound calls

```
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"enable_dialogflow": true}' \
  https://api.telnyx.com/v2/calls/{call_control_id}/actions/answer
```

When the integration is enabled, users can expect the audio provided by Dialogflow will be played on the call, and the following webhooks will be delivered to the webhook url:

```
{
  "data": {
      "event_type": "dialogflow.detectintent.response",
      "id": "22cbf929-9a87-43ab-873b-b832ccf05a05",
      "occurred_at": "2022-05-23T16:01:53.301413Z",
      "payload": {
        "call_control_id": "v2:WE_lbN28P-h81n4xeceODATcx9J-FYci6WO4hP3Gp9Sb789WivnkMw",
        "call_leg_id": "a3dc0316-dab1-11ec-aaff-02420a0d6669",
        "call_session_id": "a3cf4428-dab1-11ec-84a9-02420a0d6669",
        "client_state": null,
        "confidence": 1,
        "connection_id": "1669581837548127492",
        "fulfillment_messages": [{
            "text": [
              "Hi! I'm the virtual car rental agent. I can help you start a new car rental reservation. How can I assist you today?"
            ]
          }
        ],
        "is_final": true,
        "stream_id": "eb724ae3-4f93-49d0-9ab5-c821b47c4fc5",
        "transcript": "hello"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/e437011a-bb4a-4f34-8060-30e6604c2cf6"
  }
}
```

## Need some assistance?

If you need some help, <a href="https://telnyx.com/contact-us">reach out</a> to a member of our team through our form or <a href="https://portal.telnyx.com">the portal</a>.
