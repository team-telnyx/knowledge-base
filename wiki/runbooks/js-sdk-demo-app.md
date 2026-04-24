---
title: JS SDK Demo App
summary: To lower onboarding barrier, a JS SDK demo app was built and made accessible at [webrtc.telnyx.com](https://webrtc.telnyx.com).
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
    content_hash: b815fa267f5dd7f3b6c4ea79b0b6cdcee025d3912338c017e68a8d356cb66fb1
updated_at: 2026-04-10T00:00:00Z
---

# JS SDK Demo App

To lower onboarding barrier, a JS SDK demo app was built and made accessible at [webrtc.telnyx.com](https://webrtc.telnyx.com).

To use it, complete the following procedure.

Instead of portal.telnyx.com screenshots being displayed, only API requests are presented, as frequent UI improvements render this page out of date.

## Pre-req 1: Account Balance

Sign up and top up the account with a small amount of credit, e.g. \$5.

## Pre-req 2: Outbound Voice Profile (OVP)

```json theme={null}
POST /v2/outbound_voice_profiles HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 78

{
    "name": "webrtc",
    "whitelisted_destinations": [
        "US"
    ]
}
```

## Pre-req 3: Credential Based SIP Connection

```json theme={null}
POST /v2/credential_connections HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 288

{
    "active": true,
    "password": "xxx",
    "user_name": "xxx",
    "anchorsite_override": "Latency",
    "connection_name": "sample-connection",
    "sip_uri_calling_preference": null,
    "outbound": {
        "outbound_voice_profile_id": "2532742229592638840"
    }
}
```

where the `outbound_voice_profile_id` is the `id` returned in the previous API request.

## Pre-req 4: Phone Number

For ease of activation, choose US or CA phone numbers as there exists no regulatory requirements for their immediate use.

```json theme={null}
GET /v2/available_phone_numbers?filter[country_code]=US HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

In the response, choose a phone number. Place an order with the desired phone number and the `connection_id` from the previous step.

```json theme={null}
POST /v2/number_orders HTTP/1.1
Host: api.telnyx.com
Content-Type: application/json
Authorization: Bearer XXX
Content-Length: 119

{
  "phone_numbers": [
    {
      "phone_number": "+18669236951"
    }
  ],
  "connection_id": "2532747013766776351"
}
```

The order will be `pending` in the immediate response. After a short wait, poll the order status.

```json theme={null}
GET /v2/number_orders/3d8bd753-2162-4ce2-bc5e-96b5cad7fedb HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

Ensure the `status` is `success` before proceeding.

```json theme={null}
{
    "data": {
        "updated_at": "2024-10-02T12:42:01.637193+00:00",
        "created_at": "2024-10-02T12:42:01.637193+00:00",
        "requirements_met": true,
        "messaging_profile_id": null,
        "customer_reference": null,
        "phone_numbers": [
            {
                "requirements_status": "approved",
                "requirements_met": true,
                "phone_number": "+18669236951",
                "country_code": "US",
                "bundle_id": null,
                "id": "be663ad6-e9c2-4943-a6fa-0bfaddccaae1",
                "regulatory_requirements": [],
                "phone_number_type": "toll_free",
                "status": "success",
                "record_type": "number_order_phone_number"
            }
        ],
        "connection_id": "2532747013766776351",
        "phone_numbers_count": 1,
        "billing_group_id": null,
        "id": "3d8bd753-2162-4ce2-bc5e-96b5cad7fedb",
        "sub_number_orders_ids": [
            "407cae20-03af-4b0d-a613-fdfb241d4bc1"
        ],
        "status": "success",
        "record_type": "number_order"
    }
}
```

## Setting Up and Using the Demo App

Follow [this instruction](https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials) to create a telephony credential.

The demo app should have the following configuration

* “Authentication” → “Credential”
* “SIP Username” → from telephony credential
* “Password” → from telephony credential
* “Caller ID Name” → purchased phone number in +E164 format
* “Caller ID Number” → purchased phone number in +E164 format

After clicking “Connect”, you should see `registered` in the log to the right.

## Making Call

To make an outbound call, put the destination phone number in +E164 format. Ensure the destination country is in the `whitelisted_destinations` of the configured OVP.

## Receiving Call

Open another tab and successfully register another client. From that client, dial `[xxx]@sip.telnyx.com` where `xxx` is the `sip_username` of the telephony credential of the first client. It starts with `gencred`.

<img alt="" />

Alternatively, register this client with the credentials of the SIP connection created earlier. You may dial the phone number directly from your mobile device.

See [Dialing Registered Clients](https://developers.telnyx.com/docs/voice/webrtc/sdk-commonalities#dialing-registered-clients) for more detail.

## Additional Resources

* [Anatomy of the JS SDK](https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy#overview).
* [OVP API Reference](https://developers.telnyx.com/api-reference/outbound-voice-profiles/create-an-outbound-voice-profile)
* [Credential Based Connection API Reference](https://developers.telnyx.com/api-reference/credential-connections/create-a-credential-connection#create-a-credential-connection)
* [Number Searching API Reference](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers)
* [Number Order API Reference](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order)
