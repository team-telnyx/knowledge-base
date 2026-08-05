---
title: WebRTC Voice SDKs
summary: The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate
  and control Telnyx call legs from browsers and mobile devices. They translate between
  the WebRTC standard and Telnyx's SIP platform, providing worldwide PSTN coverage
  under the Programmable Voice API umbrella. This page covers SDK architecture, authentication
  options, the JS SDK client and call lifecycle, demo app setup, configuration interfaces,
  and Android push notifications.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/architecture
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index
- url: https://developers.telnyx.com/docs/voice/webrtc/fundamentals
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/icalloptions
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/iclientoptions
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
updated_at: 2026-08-05T14:08:20Z
---

# WebRTC Voice SDKs

*Part 4 of 7 — see also: [Part 1](webrtc-voice-sdks--part-1.md), [Part 2](webrtc-voice-sdks--part-2.md), [Part 3](webrtc-voice-sdks--part-3.md), [Part 5](webrtc-voice-sdks--part-5.md), [Part 6](webrtc-voice-sdks--part-6.md), [Part 7](webrtc-voice-sdks--part-7.md)*

The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate and control Telnyx call legs from browsers and mobile devices. They translate between the WebRTC standard and Telnyx's SIP platform, providing worldwide PSTN coverage under the Programmable Voice API umbrella. This page covers SDK architecture, authentication options, the JS SDK client and call lifecycle, demo app setup, configuration interfaces, and Android push notifications.

## JS SDK Demo App

To lower the onboarding barrier, a JS SDK demo app was built and made accessible at [webrtc.telnyx.com](https://webrtc.telnyx.com). To use it, complete the following procedure. Only API requests are presented here, as frequent UI improvements render portal screenshots out of date.

### Pre-req 1: Account Balance

Sign up and top up the account with a small amount of credit, e.g. $5.

### Pre-req 2: Outbound Voice Profile (OVP)

```http
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

### Pre-req 3: Credential Based SIP Connection

```http
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

The `outbound_voice_profile_id` is the `id` returned in the previous API request.

### Pre-req 4: Phone Number

For ease of activation, choose US or CA phone numbers as there are no regulatory requirements for their immediate use.

```http
GET /v2/available_phone_numbers?filter[country_code]=US HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

In the response, choose a phone number. Place an order with the desired phone number and the `connection_id` from the previous step:

```http
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

The order will be `pending` in the immediate response. After a short wait, poll the order status:

```http
GET /v2/number_orders/3d8bd753-2162-4ce2-bc5e-96b5cad7fedb HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

Ensure the `status` is `success` before proceeding.

### Setting Up and Using the Demo App

Follow the [Voice SDK Authentication via Telephony Credentials](voice-sdk-authentication-via-telephony-credentials.md) instructions to create a telephony credential. The demo app should have the following configuration:

- "Authentication" → "Credential"
- "SIP Username" → from telephony credential
- "Password" → from telephony credential
- "Caller ID Name" → purchased phone number in +E164 format
- "Caller ID Number" → purchased phone number in +E164 format

After clicking "Connect", you should see `registered` in the log to the right.

### Making a Call

To make an outbound call, put the destination phone number in +E164 format. Ensure the destination country is in the `whitelisted_destinations` of the configured OVP.

### Receiving a Call

Open another tab and successfully register another client. From that client, dial `[xxx]@sip.telnyx.com` where `xxx` is the `sip_username` of the telephony credential of the first client. It starts with `gencred`.

![WebRTC demo app](_images/webrtc-demo.png)

Alternatively, register this client with the credentials of the SIP connection created earlier. You may dial the phone number directly from your mobile device. See [WebRTC Voice SDKs Fundamentals](webrtc-voice-sdks-fundamentals.md) for more detail on dialing registered clients.
