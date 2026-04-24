---
title: Anatomy of a JS SDK Client & Call
summary: While some differences exist between the JS SDK and the mobile SDKs, they follow a similar client lifecycle and call flow.
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy/index
    content_hash: 3f4456cda93380a58af3983fbabd2201712d11e1013119755929810522f521eb
updated_at: 2026-04-10T00:00:00Z
---

# Anatomy of a JS SDK Client & Call

While some differences exist between the JS SDK and the mobile SDKs, they follow a similar client lifecycle and call flow.

The JS SDK demo app is used here as it’s far easier to set up the application (just load up webrtc.telnyx.com) and perform debugging using browser tooling.

## Overview

The SDK does two main things:

* Establishes an active websocket connection to send and receive signaling messages to and from rtc.telnyx.com.
* Establishes a media session for a call

To achieve the above, it employs the following suite of APIs:

* [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
* [WebRTC API](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API)
* [Media Capture and Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Media_Capture_and_Streams_API)

## Client Instantiation & Authentication

1. Go to webrtc.telnyx.com
2. Right click; Inspect; Select Network tab and filter WS traffic
3. Follow [this page](https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app) to successfully register the demo app.

<img alt="" />

In the browser, the following sequence of JSON-RPC messages is observed.

Message 1: client → rtc.telnyx.com

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": "2c754d41-b7e6-422d-b39f-661a139cd5b3",
  "method": "login",
  "params": {
    "login": "xxx",
    "passwd": "yyy",
    "userVariables": {},
    "loginParams": {},
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "sessid": "cf7894a7-c225-428a-a8ae-4145833e6ddb"
  }
}
```

Message 2: rtc.telnyx.com → client

```json theme={null}
{
  "id": "2c754d41-b7e6-422d-b39f-661a139cd5b3",
  "jsonrpc": "2.0",
  "result": {
    "message": "logged in",
    "sessid": "cf7894a7-c225-428a-a8ae-4145833e6ddb"
  },
  "voice_sdk_id": "VSDK1Ch8eUTpaTTKMC3HTSjybKJ3apyGYgw"
}
```

Message 3: rtc.telnyx.com → client

```json theme={null}
{
  "id": 138417,
  "jsonrpc": "2.0",
  "method": "telnyx_rtc.clientReady",
  "params": {
    "reattached_sessions": []
  },
  "voice_sdk_id": "VSDK1Ch8eUTpaTTKMC3HTSjybKJ3apyGYgw"
}
```

Message 4: client → rtc.telnyx.com

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": "660360fb-3f46-4f63-804b-973e429c7c22",
  "method": "telnyx_rtc.gatewayState",
  "params": {}
}
```

Message 5: rtc.telnyx.com → client

```json theme={null}
{
  "id": "660360fb-3f46-4f63-804b-973e429c7c22",
  "jsonrpc": "2.0",
  "result": {
    "params": {
      "state": "REGED"
    },
    "sessid": "cf7894a7-c225-428a-a8ae-4145833e6ddb"
  },
  "voice_sdk_id": "VSDK1Ch8eUTpaTTKMC3HTSjybKJ3apyGYgw"
}
```

The above interaction is caused by the demo app instantiating and connecting the SDK client.

```javascript theme={null}
const client = new TelnyxRTC({login: "xxx", password: "yyy"});
client.connect();
```

At a high level, when the client is instantiated, it…

* creates a [session object](https://github.com/team-telnyx/webrtc/blob/main/packages/js/src/Modules/Verto/BaseSession.ts#L42) and
* registers handlers for all [4 socket events](https://github.com/team-telnyx/webrtc/blob/main/packages/js/src/Modules/Verto/BaseSession.ts#L335)

Invoking the `connect` method on the SDK client …

* Initiates a WebSocket connection to rtc.telnyx.com
* Once the socket is open, the [login message](https://github.com/team-telnyx/webrtc/blob/main/packages/js/src/Modules/Verto/index.ts#L63) is sent to rtc.telnyx.com.

At this point, Message #1 and #2 are observed.

Message #3, #4, and #5, is the result of the logic [here](https://github.com/team-telnyx/webrtc/blob/main/packages/js/src/Modules/Verto/webrtc/VertoHandler.ts#L120)

* A `telnyx_rtc.clientReady` event from rtc.telnyx.com triggers a `telnyx_rtc.gateState` query from the SDK client
* A `REGED` event from rtc.telnyx.com bubbles up as [`telnyx.ready`](https://github.com/team-telnyx/webrtc/blob/main/packages/js/docs/ts/classes/TelnyxRTC.md#events).

At this point, the SDK client is authenticated to make or receive a call.

## Call Initiation

1. In another tab, open chrome://webrtc-internals/
2. Fill in “Call destination” with +18008648331 (United Airlines IVR)
3. Click “Call”

In the browser, the following sequence of JSON-RPC messages is observed.

Message 1: client → rtc.telnyx.com

```json theme={null}
{
   "jsonrpc":"2.0",
   "id":"71344c55-10a9-4f6a-b8a8-ebaa9347bc95",
   "method":"telnyx_rtc.invite",
   "params":{
      "sessid":"cf7894a7-c225-428a-a8ae-4145833e6ddb",
      "sdp":"[ABRIDGED SDP]",
      "dialogParams":{
         "audio":true,
         "useStereo":false,
         "debug":false,
         "debugOutput":"socket",
         "attach":false,
         "screenShare":false,
         "userVariables":{
            "microphoneLabel":"Default - AirPods"
         },
         "mediaSettings":{

         },
         "iceServers":[
            {
               "urls":"turn:turn.telnyx.com:3478?transport=tcp",
               "username":"testuser",
               "credential":"testpassword"
            },
            {
               "urls":"stun:stun.telnyx.com:3478"
            },
            {
               "urls":[
                  "stun:stun.l.google.com:19302"
               ]
            }
         ],
         "localElement":"localVideo",
         "remoteElement":"remoteVideo",
         "ringtoneFile":"https://webrtc.telnyx.com/sounds/incoming_call.mp3",
         "stats":true,
         "callID":"074e7e59-6859-4b8b-8743-83df82e7f776",
         "destination_number":"+18008648331",
         "remote_caller_id_name":"Outbound Call",
         "remote_caller_id_number":"+18008648331",
         "caller_id_name":"+15734038245",
         "caller_id_number":"XXX"
      },
      "User-Agent":"Web-2.16.0"
   }
}
```

Message 2: rtc.telnyx.com → client

```json theme={null}
{
  "id": "71344c55-10a9-4f6a-b8a8-ebaa9347bc95",
  "jsonrpc": "2.0",
  "result": {
    "callID": "074e7e59-6859-4b8b-8743-83df82e7f776",
    "message": "CALL CREATED",
    "sessid": "cf7894a7-c225-428a-a8ae-4145833e6ddb"
  },
  "voice_sdk_id": "VSDK1CiEGUTpa63GGtH2nSmyTHM7KIwlL_w"
}
```

Message 3: rtc.telnyx.com → client

```json theme={null}
{
  "id": 254271,
  "jsonrpc": "2.0",
  "method": "telnyx_rtc.ringing",
  "params": {
    "callID": "074e7e59-6859-4b8b-8743-83df82e7f776",
    "callee_id_name": "Outbound Call",
    "callee_id_number": "+18008648331",
    "caller_id_name": "+15734038245",
    "caller_id_number": "XXX",
    "dialogParams": {
      "custom_headers": []
    },
    "display_direction": "inbound",
    "telnyx_leg_id": "b6a23a2c-7e12-11ef-ab96-02420aef821f",
    "telnyx_session_id": "b6a23ea0-7e12-11ef-a5d3-02420aef821f"
  },
  "voice_sdk_id": "VSDK1CiEGUTpa63GGtH2nSmyTHM7KIwlL_w"
}
```

Message 4: client → rtc.telnyx.com

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 254271,
  "result": {
    "method": "telnyx_rtc.ringing"
  }
}
```

Message 5: rtc.telnyx.com → client

```json theme={null}
{
  "id": 254274,
  "jsonrpc": "2.0",
  "method": "telnyx_rtc.media",
  "params": {
    "callID": "074e7e59-6859-4b8b-8743-83df82e7f776",
    "dialogParams": {
      "custom_headers": []
    },
    "sdp": "[ABRIDGED SDP]",
    "variables": {
      "Core-UUID": "be37d1d2-14e2-45de-af9f-0b2807445761",
      "Event-Calling-File": "switch_channel.c",
      "Event-Calling-Function": "switch_channel_get_variables_prefix",
      "Event-Calling-Line-Number": "4632",
      "Event-Date-GMT": "Sun, 29 Sep 2024 03:27:13 GMT",
      "Event-Date-Local": "2024-09-29 03:27:13",
      "Event-Date-Timestamp": "1727580433259250",
      "Event-Name": "CHANNEL_DATA",
      "Event-Sequence": "1071399",
      "FreeSWITCH-Hostname": "b2bua-rtc-canary.tel-sy1-ibm-prod-413",
      "FreeSWITCH-IPv4": "10.33.6.81",
      "FreeSWITCH-IPv6": "::1",
      "FreeSWITCH-Switchname": "b2bua-rtc-canary.tel-sy1-ibm-prod-413"
    }
  },
  "voice_sdk_id": "VSDK1CiEGUTpa63GGtH2nSmyTHM7KIwlL_w"
}
```

Message 6: client → rtc.telnyx.com

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 254274,
  "result": {
    "method": "telnyx_rtc.media"
  }
}
```

Message 7: rtc.telnyx.com → client

```json theme={null}
{
  "id": 254275,
  "jsonrpc": "2.0",
  "method": "telnyx_rtc.answer",
  "params": {
    "callID": "074e7e59-6859-4b8b-8743-83df82e7f776",
    "dialogParams": {
      "custom_headers": []
    },
    "variables": {
      "Core-UUID": "be37d1d2-14e2-45de-af9f-0b2807445761",
      "Event-Calling-File": "switch_channel.c",
      "Event-Calling-Function": "switch_channel_get_variables_prefix",
      "Event-Calling-Line-Number": "4632",
      "Event-Date-GMT": "Sun, 29 Sep 2024 03:27:15 GMT",
      "Event-Date-Local": "2024-09-29 03:27:15",
      "Event-Date-Timestamp": "1727580435119306",
      "Event-Name": "CHANNEL_DATA",
      "Event-Sequence": "1071412",
      "FreeSWITCH-Hostname": "b2bua-rtc-canary.tel-sy1-ibm-prod-413",
      "FreeSWITCH-IPv4": "10.33.6.81",
      "FreeSWITCH-IPv6": "::1",
      "FreeSWITCH-Switchname": "b2bua-rtc-canary.tel-sy1-ibm-prod-413"
    }
  },
  "voice_sdk_id": "VSDK1CiEGUTpa63GGtH2nSmyTHM7KIwlL_w"
}
```

Message 8: client → rtc.telnyx.com

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 254275,
  "result": {
    "method": "telnyx_rtc.answer"
  }
}
```

At this point, the media will flow.

All of the above interaction is the result of the following SDK API call.

```javascript theme={null}
client.newCall(options);
```

Under the hood, the SDK performs many steps before Message #1 (INVITE) is even sent.

<img alt="" />

Broadly speaking, the following are the essential steps with the relevant data picked out from the JSON dump.

1. [`RTCPeerConnection`](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection) is instantiated.
2. [`getUserMedia`](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) is invoked to obtain user’s permission for audio and eventually the [`MediaStream`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream)

```json theme={null}
{
  "audio_track_info": "id:6bd2b2da-d615-4ef3-9ac2-394abb22d6b0 label:Default - AirPods",
  "pid": 44341,
  "request_id": 29,
  "request_type": "getUserMedia",
  "rid": 303,
  "stream_id": "7cc701ad-3a35-4c2a-9b1e-c4c7b209f30c",
  "timestamp": 1727582437707.941
}
```

3. [`addTransceiver`](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/addTransceiver) is invoked to add the local stream to the sender of the `RTCPeerConnection`.

```json theme={null}
{
  "time": "9/28/2024, 11:00:37 PM",
  "type": "transceiverAdded",
  "value": "Caused by: addTransceiver\n\ngetTransceivers()[0]:{\n  mid:null,\n  kind:'audio',\n  sender:{\n    track:'6bd2b2da-d615-4ef3-9ac2-394abb22d6b0',\n    streams:['7cc701ad-3a35-4c2a-9b1e-c4c7b209f30c'],\n    encodings: [\n      {active: true, },\n    ],\n  },\n  receiver:{\n    track:'434cac64-3afe-4705-bfe7-979d9530b58e',\n    streams:[],\n  },\n  direction:'sendrecv',\n  currentDirection:null,\n}"
}
```

4. The previous step triggers the [`negotiationneeded`](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/negotiationneeded_event) event.

```json theme={null}
{
  "time": "9/28/2024, 11:00:37 PM",
  "type": "negotiationneeded",
  "value": ""
}
```

5. In the event handler, the SDK invokes [`createOffer`](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/createOffer).

```json theme={null}
{
  "time": "9/28/2024, 11:00:37 PM",
  "type": "createOffer",
  "value": "options: {offerToReceiveVideo: 0, offerToReceiveAudio: 1, voiceActivityDetection: true, iceRestart: false}"
}
```

6. This API call will eventually create a [`RTCSessionDescription`](https://developer.mozilla.org/en-US/docs/Web/API/RTCSessionDescription) with information on the local media stream.

```json theme={null}
{
  "time": "9/28/2024, 11:00:37 PM",
  "type": "createOfferOnSuccess",
  "value": "type: offer, sdp: [ABRIDGED SDP]"
}
```

7. The SDK will then invoke the [`setLocalDescription`](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/setLocalDescription) to set the SDP of the client peer.

```json theme={null}
{
  "time": "9/28/2024, 11:00:37 PM",
  "type": "setLocalDescription",
  "value": "type: offer, sdp: [ABRIDGED SDP]"
}
```

8. Concurrently, `createOffer` also kicks off the ICE candidate gathering.

```json theme={null}
   {
     "time": "9/28/2024, 11:00:37 PM",
     "type": "icegatheringstatechange",
     "value": "gathering"
    },
    ...,
    {
     "time": "9/28/2024, 11:00:37 PM",
     "type": "icecandidate",
     "value": "sdpMid: 0, sdpMLineIndex: 0, candidate: candidate:134647514 1 udp 1685855999 18.163.7.125 59374 typ srflx raddr 100.113.237.26 rport 59374 generation 0 ufrag ccb7 network-id 3 network-cost 50, url: stun:stun.l.google.com:19302"
    }
```

9. When all is done, `icecandidate` event triggers with `candidate = null` to indicate the process is completed. Subsequently, the existing local SDP parameters are augmented with the ICE candidates.
10. At this point, all necessary info are present to send the invite to rtc.telnyx.com.
11. As a result, on the websocket, Message #1 through #4 are observed.
12. At Message #5, rtc.telnyx.com sends over its SDP in the `telnyx_rtc.media` events.
13. Upon receipt of this message, the SDK invokes [`setRemoteDescription`](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/setRemoteDescription) to set the SDP of the remote peer.

```json theme={null}
{
  "time": "9/28/2024, 11:00:44 PM",
  "type": "setRemoteDescription",
  "value": "type: answer, sdp: [ABRIDGED SDP]"
}
```

14. Finally, two peers of the `RTCPeerConnection` are fully identified. [connectionState](https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState) changes from connecting to connected.

```json theme={null}
{
  "time": "9/28/2024, 11:00:44 PM",
  "type": "connectionstatechange",
  "value": "connecting"
},
...
{
  "time": "9/28/2024, 11:00:45 PM",
  "type": "connectionstatechange",
  "value": "connected"
}
```

15. Media will flow over UDP.
