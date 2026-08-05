---
title: Outbound dialer implementation
summary: Build an automated outbound dialer system that enables agents to make high-volume
  outbound calls efficiently using Telnyx WebRTC and the Call Control API. This page
  covers the required components, frontend implementation details, and two backend
  implementation approaches (Voice API and TeXML) for a complete outbound dialer solution.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/outbound-dialer
updated_at: 2026-08-05T14:07:50Z
---

# Outbound dialer implementation

*Part 2 of 3 — see also: [Part 1](outbound-dialer-implementation--part-1.md), [Part 3](outbound-dialer-implementation--part-3.md)*

Build an automated outbound dialer system that enables agents to make high-volume outbound calls efficiently using Telnyx WebRTC and the Call Control API. This page covers the required components, frontend implementation details, and two backend implementation approaches (Voice API and TeXML) for a complete outbound dialer solution.

## Backend implementation

The backend implementation is a crucial component of a successful call. Two approaches are supported:

- Voice API
- TeXML

![Outbound dialer backend architecture diagram](https://mintcdn.com/telnyx/VYiRDGy8TCRNJLEC/img/outbound-dialer-backend.png?fit=max&auto=format&n=VYiRDGy8TCRNJLEC&q=85&s=523802b99fe1d2ebb3dc7d3920e0eb2b)

### Voice API approach

The following sequence diagram covers a typical outbound call flow using the [Telnyx Voice API](https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands).

#### 1. Client Registers with Telnyx

The process starts with the WebRTC client (the Front End App) connecting to Telnyx by sending a `Client.connect (Register)` request. This is essentially the WebRTC client registering with Telnyx to initiate communications.

```javascript
function connect() {
  client = new TelnyxWebRTC.TelnyxRTC({
    env: env,
    login: document.getElementById('username').value,
    password: document.getElementById('password').value,
    ringtoneFile: './sounds/incoming_call.mp3',
    // ringbackFile: './sounds/ringback_tone.mp3',
  });

  if (document.getElementById('audio').checked) {
    client.enableMicrophone();
  } else {
    client.disableMicrophone();
  }

  client.on('telnyx.ready', function () {
    btnConnect.classList.add('d-none');
    btnDisconnect.classList.remove('d-none');
    connectStatus.innerHTML = 'Connected';
    startCall.disabled = false;
  });

  //Socket close, error and updating call states
  ...
}
```

#### 2. Initiating a Call

Once the WebRTC client is connected, it requests to initiate a call by sending a `Client.newCall(destinationNumber,callerNumber)` method to Telnyx. The request requires the destination number and the caller number. This request is routed from the front-end WebRTC client application to the back-end server application, which acts as the intermediary between the client and Telnyx for controlling call logic.

```javascript
//Make Call
function makeCall() {
  const params = {
    callerName: 'Caller Name',
    callerNumber: 'Caller Number',
    destinationNumber: document.getElementById('number').value, // required!
    audio: document.getElementById('audio').checked,
    video: document.getElementById('video').checked
      ? { aspectRatio: 16 / 9 }
      : false,
  };

  currentCall = client.newCall(params);
}
```

#### 3. Dialing PSTN (command)

The backend server then instructs Telnyx to dial the destination number in the PSTN using the `Dial PSTN with Dial Command`. This command triggers Telnyx to initiate an outbound call to the PSTN.

```bash
curl -X POST https://api.telnyx.com/v2/calls \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer YOUR_API_TOKEN' \
-d '{
  "connection_id": "YOUR_CONNECTION_ID",
  "to": "+E.164 PSTNNUMBER",
  "from": "+E.164 CALLERNUMBER",
  "webhook_url": "https://yourserver.app/telnyx-webhooks"
}'
```

#### 4. Call Initiated (webhook)

Telnyx acknowledges the initiation of the call process by triggering a `call.initiated` webhook to the backend server. This webhook indicates that the call process has started but does not necessarily mean the call has been answered.

```json
{
  "data": {
    "record_type": "event",
    "event_type": "call.initiated",
    "id": "uuid-of-the-event",
    "occurred_at": "2024-03-25T14:00:00Z",
    "payload": {
      "call_control_id": "call_control_id_of_the_initiated_call",
      "connection_id": "connection_id_used_in_the_call",
      "call_leg_id": "unique_id_for_call_leg",
      "custom_headers": [
        {
          "header_name": "X-Custom-Header",
          "header_value": "CustomValue"
        }
      ],
      "call_session_id": "unique_id_for_the_call_session",
      "client_state": "optional_client_defined_state",
      "from": "+12345678901",
      "to": "+10987654321",
      "direction": "outgoing",
      "state": "parked"
    }
  }
}
```

#### 5. PSTN Outbound Call

Telnyx makes the outbound call to the destination number in the PSTN network.

#### 6. PSTN Answered (webhook)

When the PSTN destination answers the call, Telnyx sends a notification back to the backend server through a `call.answered` webhook, indicating that the call had been successfully answered on the PSTN side.

```json
{
  "data": {
    "record_type": "event",
    "event_type": "call.answered",
    "id": "uuid-of-the-event",
    "occurred_at": "2024-03-25T13:45:00Z",
    "payload": {
      "call_control_id": "call_control_id_of_the_call",
      "connection_id": "connection_id_used_in_the_call",
      "call_leg_id": "unique_id_for_call_leg",
      "call_session_id": "unique_id_for_the_call_session",
      "client_state": "optional_client_defined_state",
      "custom_headers": [
        {
          "header_name": "X-Header-Example",
          "header_value": "HeaderValue"
        }
      ],
      "from": "+12345678901",
      "to": "+10987654321",
      "state": "answered"
    }
  }
}
```

#### 7. Bridging Call Legs (command)

After the call is answered, the next step is to bridge the call between the WebRTC client and the PSTN to enable two-way communication. The backend server sends a Bridge Call Legs: `call.bridge(call_control_id)` command to Telnyx, instructing it to connect the two call legs.

```bash
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id_WebRTC}/actions/bridge \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer YOUR_API_TOKEN' \
-d '{
  "call_control_id": "PSTN_CALL_CONTROL_ID"
}'
```

#### 8. Call Bridged (webhook)

Once the call legs are successfully bridged, Telnyx triggers a `call.bridged` webhook to the backend server, indicating that the WebRTC agent and the PSTN call are now connected, and the call is in progress.

```json
{
  "data": {
    "record_type": "event",
    "event_type": "call.bridged",
    "id": "uuid-of-the-event",
    "occurred_at": "2024-03-25T12:34:56Z",
    "payload": {
      "call_control_id": "call_control_id_of_the_call",
      "connection_id": "connection_id_used_in_the_call",
      "call_leg_id": "unique_id_for_call_leg",
      "call_session_id": "unique_id_for_the_call_session",
      "client_state": "optional_client_defined_state",
      "from": "+12345678901",
      "to": "+10987654321",
      "state": "bridged"
    }
  }
}
```

#### 9. Call In Progress

With the bridge established, the WebRTC agent (the user on the front-end client) and the PSTN participant can now communicate. This state continues until either party terminates the call. If the call is ended, Telnyx triggers a `call.hangup` webhook. An example `call.hangup` event is provided below.

```json
{
  "data": {
    "record_type": "event",
    "event_type": "call.hangup",
    "id": "uuid-example-1234",
    "occurred_at": "2024-03-28T12:34:56Z",
    "payload": {
      "call_control_id": "call_control_id_example_5678",
      "connection_id": "connection_id_example_9012",
      "call_leg_id": "call_leg_id_example_3456",
      "call_session_id": "call_session_id_example_7890",
      "client_state": "example_state",
      "from": "+12345678901",
      "to": "+10987654321",
      "start_time": "2024-03-28T12:00:00Z",
      "state": "hangup",
      "hangup_cause": "normal_clearing",
      "hangup_source": "caller",
      "sip_hangup_cause": "16"
    }
  }
}
```

### TeXML approach

The following sequence diagram covers a typical outbound call flow using the Telnyx TeXML API.

#### 1. Client Registers with Telnyx

The process starts with the WebRTC client (the Front End App) connecting to Telnyx by sending a `Client.connect (Register)` request. This is essentially the WebRTC client registering with Telnyx to initiate communications.

```javascript
function connect() {
  client = new TelnyxWebRTC.TelnyxRTC({
    env: env,
    login: document.getElementById('username').value,
    password: document.getElementById('password').value,
    ringtoneFile: './sounds/incoming_call.mp3',
    // ringbackFile: './sounds/ringback_tone.mp3',
  });

  if (document.getElementById('audio').checked) {
    client.enableMicrophone();
  } else {
    client.disableMicrophone();
  }

  client.on('telnyx.ready', function () {
    btnConnect.classList.add('d-none');
    btnDisconnect.classList.remove('d-none');
    connectStatus.innerHTML = 'Connected';
    startCall.disabled = false;
  });

  //Socket close, error and updating call states
  ...
}
```

#### 2. Initiating a Call

Once the WebRTC client is connected, it requests to initiate a call by sending a `Client.newCall(destinationNumber,callerNumber)` method to Telnyx. The request requires the destination number and the caller number. This request is routed from the front-end WebRTC client application to the back-end server application, which acts as the intermediary between the client and Telnyx for controlling call logic.

```javascript
//Make Call
function makeCall() {
  const params = {
    callerName: 'Caller Name',
    callerNumber: 'Caller Number',
    destinationNumber: document.getElementById('number').value, // required!
    audio: document.getElementById('audio').checked,
    video: document.getElementById('video').checked
      ? { aspectRatio: 16 / 9 }
      : false,
  };

  currentCall = client.newCall(params);
}
```

#### 3. Dialing PSTN (command)

The backend server then instructs Telnyx to dial the first destination number. This command triggers Telnyx to initiate an outbound call to the PSTN.

```bash
curl -L 'https://api.telnyx.com/v2/texml/Accounts/:account_sid/Calls' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "To": "+13121230000",
  "From": "+13120001234",
  "Url": "https://www.example.com/texml.xml",
  "StatusCallback": "https://www.example.com/statuscallback-listener"
}'
```

#### 4. TeXML Dial Verb

The Url parameter hits a server that then instructs Telnyx using XML to dial the second PSTN transfer B-leg. The verb triggers Telnyx to initiate an outbound call to the second PSTN leg.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Number>+18771234567</Number>
  </Dial>
</Response>
```

TeXML Dial expected callbacks can be found [here](/docs/voice/programmable-voice/texml-verbs/dial#expected-callbacks).
