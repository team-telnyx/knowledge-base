---
title: Outbound dialer implementation
summary: Build an automated outbound dialer system using Telnyx WebRTC and Call Control API for high-volume calling campaigns.
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/outbound-dialer/index
    content_hash: 795b1cee4fd3829464699970cb65e8d99421c99ab23e2e37e9e4b827a0c08802
updated_at: 2026-04-10T00:00:00Z
---

# Outbound dialer implementation

Build an automated outbound dialer system using Telnyx WebRTC and Call Control API for high-volume calling campaigns.

Build an automated outbound dialer system that enables agents to make high-volume outbound calls efficiently using Telnyx WebRTC and Call Control API.

## Overview

In building an outbound dialer solution leveraging Telnyx WebRTC, enable SIP connection credentials with Park Outbound Calls and webhook events to combine front-end WebRTC functionality with backend voice application.

### Key features

**Park Outbound Calls**

* Combine front-end WebRTC application with backend voice application using Telnyx Voice APIs.
* Enable advanced call flow control and routing.
* [Learn more about Park Outbound Calls](https://support.telnyx.com/en/articles/4351104-sip-connection-settings#h_7e20c5a7f7).

**Webhook events**

* Monitor SIP connection events in real-time.
* Receive notifications for call events: dialing, answering, bridging, hang-up, voicemail completion.
* Primary/failover URL configuration for reliability.

### Required components

1. WebRTC Client.
2. Backend Server Application.
3. SIP Connection with Park Outbound Calls Enabled (select TeXML option when using the TeXML approach).

## Frontend implementation

In a typical front-end WebRTC application, there are many components that should be supported.

**Agent status management**: The outbound dialer application should be able to display the agent's current status, such as, but not limited to, Available, Unavailable, Busy, and Offline. This type of management should not only act as an indicator for other agents but also limit agents' ability to transfer calls to unavailable agents.

This status should also be correlated with the WebRTC client state. This means that when an agent's status is set to available, the WebRTC client should be fully registered and ready to place outbound calls. This should be handled at a global level, typically using state management frameworks such as [Global Context APIs](https://react.dev/reference/react/useContext) or [Redux](https://redux.js.org/).

Here is an example softphone application (WebRTC client) with an option to change its current state.

<img alt="Outbound dialer agent status management interface" />

**Call control toolbar**: The toolbar is a set of buttons within your WebRTC client dialer for handling calls, with options like Answer, Hangup, Mute/Unmute, Hold/Unhold, and selecting the caller ID. Here is an example of a dialer component.

<img alt="Outbound dialer call control toolbar with call handling options" />

Here are the functions written in JavaScript React which would be used to build the above options in the frontend app:

## Backend implementation

### Voice API

    The backend implementation is a crucial component of a successful call. The following sequence diagram covers a typical outbound call flow using [Telnyx Voice API](https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands). Below the sequence diagram, I describe each step.

    <img alt="Outbound dialer backend architecture diagram" />

    ### 1. Client Registers with Telnyx

    The process starts with the WebRTC client (the Front End App) connecting to Telnyx by sending a `Client.connect (Register)` request. This is essentially the WebRTC client registering with Telnyx to initiate communications.

    ```javascript theme={null}
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

    ### 2. Initiating a Call

    Once the WebRTC client is connected, it requests to initiate a call by sending a `Client.newCall(destinationNumber,callerNumber)` method to Telnyx. The request requires the destination number and the caller number. This request is routed from the front-end WebRTC client application to the back-end server application, which acts as the intermediary between the client and Telnyx for controlling call logic.

    ```javascript theme={null}
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

    ### 3. Dialing PSTN (command)

    The backend server then instructs Telnyx to dial the destination number in the PSTN using the `Dial PSTN with Dial Command`. This command triggers Telnyx to initiate an outbound call to the PSTN.

    ```bash theme={null}
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

    ### 4. Call Initiated (webhook)

    Telnyx acknowledges the initiation of the call process by triggering a `call.initiated` webhook to the backend server. This webhook indicates that the call process has started but does not necessarily mean the call has been answered.

    ```json theme={null}
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

    ### 5. PSTN Outbound Call

    Telnyx makes the outbound call to the destination number in the PSTN network.

    ### 6. PSTN Answered (webhook)

    When the PSTN destination answers the call, Telnyx sends a notification back to the backend server through a `call.answered` webhook, indicating that the call had been successfully answered on the PSTN side.

    ```json theme={null}
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

    ### 7. Bridging Call Legs (command)

    After the call is answered, the next step is to bridge the call between the WebRTC client and the PSTN to enable two-way communication. The backend server sends a Bridge Call Legs: `call.bridge(call_control_id)` command to Telnyx, instructing it to connect the two call legs.

    ```bash theme={null}
    curl -X POST https://api.telnyx.com/v2/calls/{call_control_id_WebRTC}/actions/bridge \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_TOKEN' \
    -d '{
      "call_control_id": "PSTN_CALL_CONTROL_ID"
    }'
    ```

    ### 8. Call Bridged (webhook)

    Once the call legs are successfully bridged, Telnyx triggers a `call.bridged` webhook to the backend server, indicating that the WebRTC agent and the PSTN call are now connected, and the call is in progress.

    ```json theme={null}
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

    ### 9. Call In Progress

    With the bridge established, the WebRTC agent (the user on the front-end client) and the PSTN participant can now communicate. This state continues until either party terminates the call. If the call is ended, Telnyx triggers a `call.hangup` webhook. An example `call.hangup` event is provided below.

    ```json theme={null}
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

### TeXML

    The backend implementation is a crucial component of a successful call. The following sequence diagram covers a typical outbound call flow using Telnyx TeXML API. Below the sequence diagram, I describe each step.

    <img alt="Outbound dialer backend architecture diagram" />

    ### 1. Client Registers with Telnyx

    The process starts with the WebRTC client (the Front End App) connecting to Telnyx by sending a `Client.connect (Register)` request. This is essentially the WebRTC client registering with Telnyx to initiate communications.

    ```javascript theme={null}
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

    ### 2. Initiating a Call

    Once the WebRTC client is connected, it requests to initiate a call by sending a `Client.newCall(destinationNumber,callerNumber)` method to Telnyx. The request requires the destination number and the caller number. This request is routed from the front-end WebRTC client application to the back-end server application, which acts as the intermediary between the client and Telnyx for controlling call logic.

    ```javascript theme={null}
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

    ### 3. Dialing PSTN (command)

    The backend server then instructs Telnyx to dial the first destination number. This command triggers Telnyx to initiate an outbound call to the PSTN.

    ```bash theme={null}
    curl -L 'https://api.telnyx.com/v2/texml/Accounts/:account_sid/Calls' \
    -H 'Content-Type: application/json' \
    -H 'Accept: application/json' \
    -H 'Authorization: Bearer ' \
    -d '{
      "To": "+13121230000",
      "From": "+13120001234",
      "Url": "https://www.example.com/texml.xml",
      "StatusCallback": "https://www.example.com/statuscallback-listener"
    }'
    ```

    ### 4. TeXML Dial Verb

    The Url parameter hits a server that then instructs Telnyx using XML to dial the second PSTN transfer B-leg. The verb triggers Telnyx to initiate an outbound call to the second PSTN leg.

    ```xml theme={null}
    <?xml version="1.0" encoding="UTF-8"?>

        +18771234567

    ```

    <Callout type="info">
      TeXML Dial expected callbacks can be found [here](dial.md#expected-callbacks).

## Next steps

* Review [WebRTC authentication](https://developers.telnyx.com/development/webrtc/auth/credential-connections) options.
* Explore [Call Control API](https://developers.telnyx.com/api-reference/call-control-applications/list-call-control-applications) documentation.
* Learn more about [webhook fundamentals](https://developers.telnyx.com/development/api-fundamentals/webhooks/receiving-webhooks).
