---
title: Contact center (CCaaS) implementation
summary: Build a complete contact center solution using Telnyx WebRTC with advanced call control and routing capabilities.
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/contact-center/index
    content_hash: a243c945d15a2f118455baf6a4044db450d910402f35d1f2c5686c12078ab589
updated_at: 2026-04-10T00:00:00Z
---

# Contact center (CCaaS) implementation

Build a complete contact center solution using Telnyx WebRTC with advanced call control and routing capabilities.

## Overview

In building a Contact Center as a Service solution leveraging Telnyx WebRTC, enable SIP connection credentials with Park Outbound Calls and webhook events for enhanced functionality and seamless communication flows.

### Key features

**Webhook events**

* Monitor SIP connection events in real-time.
* Receive notifications for call events: dialing, answering, bridging, hang-up, voicemail completion.
* Primary/failover URL configuration for reliability.

**Park Outbound Calls**

* Temporarily hold calls until further instructions via Voice API.
* Enable additional processing or decision-making before connecting.
* Provide customizable call handling experiences.

**Backend application requirements**

* Utilize Telnyx's call control capabilities (Voice API documentation).
* Issue commands based on webhook events: answer, play audio, bridge, transfer.
* Handle sophisticated workflows for call routing.

### Inbound call flow

1. User calls main number, answered with text-to-speech greeting.
2. IVR menu presents options to mark call attributes (language, skills, department).
3. Call transferred to queue, parked while waiting for agent.
4. Auto-transfer to most idle agent or manual cherry-picking.
5. Call recording initiated when agent answers.
6. Call forwarded to multiple agents simultaneously with recording enabled.
7. Additional call control: mute, hold, transcription, text-to-speech announcements.

## Frontend implementation

### Authentication

Agent desktop applications should have an authentication process implemented. We recommend using authentication tokens generated from individual telephony credentials created for each agent. When an agent logs in, the frontend app requests an authentication token from the backend, which is then used for subsequent API requests in the WebRTC client.

When a call is received, you can see which agents are logged in with the on-demand generated credentials. Your call center service would use our Call Control API to dial each of the generated credentials to connect the caller with one of the available agents. Once agents are logged in, make sure your WebRTC client informs your call center backend that the agents are registered. This ensures the backend has a list of agents it can dial each time an inbound call is received to the main number.

See more details in the [User authentication](#user-authentication) section in the Backend implementation for the Voice API methods to be used on the backend side.

### Agent desktop application

Agent desktop application should support the following options:

**Agent status management**: The agent should be able to report their current status, such as Available or Unavailable, so the backend application can see the currently available agents and decide which agent should receive the next call.

Here is an example softphone application (WebRTC client) with an option to choose a preferred audio device.

<img alt="Agent desktop application with status management" />

**Call control toolbar**: The toolbar is a set of buttons for handling calls, with options like Pickup, Disconnect, Mute, Hold, etc.

<img alt="Call control toolbar with call handling options" />

**Queue view** allows you to monitor the calls parked in the queues and pick up a call manually. You can also present additional data like a position in a queue and estimated wait time.

<img alt="Queue view showing parked calls" />

Here are the functions which would be used to build the above options in the frontend app:

### Audio device settings

Get a list of available audio devices:

```javascript theme={null}
async function() {
  const client = new TelnyxRTC(options);
  let result = await client.getDevices();
  console.log(result);
}
```

Set active audio device:

```javascript theme={null}
const constraints = await client.setAudioSettings({
  micId: '772e94959e12e589b1cc71133d32edf543d3315cfd1d0a4076a60601d4ff4df8',
  micLabel: 'Internal Microphone (Built-in)',
  echoCancellation: false
})
```

### Call control toolbar

Toggle microphone:

```javascript theme={null}
await call.toggleAudioMute()
console.log(call.state) // => 'muted'

await call.toggleAudioMute()
console.log(call.state) // => 'unmuted'
```

Toggle call hold:

```javascript theme={null}
await call.toggleHold()
console.log(call.state) // => 'held'

await call.toggleHold()
console.log(call.state) // => 'active'
```

## Backend implementation

The backend application handles call routing, IVR logic, and agent management through Telnyx Voice API webhooks.

### User authentication

For each user, generate on-demand telephony credentials which should be stored in a database and associated with the user login. Agent desktop application should request an authentication token to be created based on the telephony credentials.

**Generate on-demand telephony credentials**

On-Demand Credentials help you onboard new customers or team members under your SIP connection, allowing you to separate each user with their own security credentials. This solution is ideal for integrating WebRTC into your own platforms, enabling your backend system to create outbound calls to each on-demand generated credential.

You can use the optional parameter `expires_at` if you would like to set an expiration time for the credentials.

```javascript theme={null}
const telnyx = require('telnyx')('YOUR_API_KEY');

const { data: telephonyCredentials } = await telnyx.telephonyCredentials.create({
  "connection_id": "1234567890",
  "name": "My-new-credential",
  "expires_at": EXPIRATION_DATE
});
```

**Create authentication token**

```javascript theme={null}
const telnyx = require('telnyx')('YOUR_API_KEY');

const accessToken = await telnyx.telephonyCredentials.generateAccessTokenFromCredential('CREDENTIAL_ID');
```

### Call flow

In the backend application, we can fully control the call flow from the initiation of the call up to the call disconnect event. Based on the webhook notification, we can decide what kind of actions should be applied to the call.

To monitor the call and proceed with the call flow, we should monitor call event types received on the webhook URL. Having an integration with the CRM application, we can retrieve caller data, for instance based on the caller number:

```javascript theme={null}
app.post("/api/voice/inbound", async (req, res) => {
  const { event_type } = req.body.data;
  const { payload } = req.body.data;

  const callData = await telnyx.calls.retrieve(payload.call_control_id);
  const isAlive = callData.data.is_alive;

  switch (event_type) {
    case "call.initiated":
      if (payload.direction === "incoming") {
        userObj = await get_caller_data({ voiceNumber: payload.to });
      } else userObj = await get_caller_data({ voiceNumber: payload.from });
      call_initiated(req, userObj);
      break;
    case "call.answered":
      call_answered(req, userObj);
      break;
    case "call.dtmf.received":
      call_dtmf_received(req, userObj);
      break;
    case "call.bridged":
      call_bridged(req, userObj);
      break;
    case "call.hangup":
      call_hangup(req, userObj);
      break;
    case "call.recording.saved":
      call_recording_saved(req, userObj);
      break;
    case "call.enqueued":
      call_enqueued(req, userObj);
      break;
    case "call.dequeued":
      call_dequeued(req, userObj);
      break;
    case "call.transcription":
      handleTranscription(payload, userObj);
      break;
    default:
  }

  return res.status(200).send({});
});
```

For the `call.initiated` webhook, you should answer the call and provide an initial greeting with IVR options using the speak option:

```javascript theme={null}
const call_initiated = async (req) => {
  const { payload } = req.body.data;
  const call = new telnyx.Call({
    call_control_id: payload.call_control_id,
  });

  console.log(`Call initiated: ${payload.call_control_id}`);

  try {
    await call.answer();
    console.log("Call answered:", payload.call_control_id);

    await call.speak({
      payload: welcomePrompt,
      voice: "male",
      language: language,
    });
  } catch (err) {
    console.log("Error answering a call:", err.message);
  }
};
```

Later, you can observe DTMF digits received to choose the next action in your call flow:

```javascript theme={null}
const call_dtmf_received = async (req) => {
  const { payload } = req.body.data;
  const call = new telnyx.Call({
    call_control_id: payload.call_control_id,
  });

  console.log("DTMF received:", payload.digit);

  if (payload.digit === "1") {
    console.log("Transferring call to external number:", transferNumber);
    await call.transfer({
      to: transferNumber,
    });
  } else if (payload.digit === "2") {
    const queueName = "Sales";
    console.log("Transferring call to a queue: " + queueName);
    await call.enqueue({
      queue_name: queueName,
    });
  }
};
```

When the call is enqueued, you can play a prompt and music to a caller waiting for an available agent. At that stage, you should update your frontend interface in a queue view with information about the new incoming call. You can use the WebSocket interface to emit data to the agent desktop application.

```javascript theme={null}
const call_enqueued = async (req) => {
  const { payload } = req.body.data;

  const call = new telnyx.Call({
    call_control_id: payload.call_control_id,
  });

  console.log(
    `Call ${payload.call_control_id} enqueued in ${payload.queue} queue`
  );

  try {
    await call.speak({
      payload: "Please wait while we connect you to an agent",
      voice: "male",
      language: "en-US",
    });

    await call.playback_start({
      audio_url: `https://${process.env.API_SERVER_URL}/audio/queue_music.mp3`,
    });

    const emitObj = {
      type: "call-enqueued",
      payload: payload,
    };
    await Socket.io.emit(JSON.stringify(emitObj));
  } catch (error) {
    console.log("Error has occurred on call enqueued event:", error.message);
  }
};
```

Based on the other event types, additional actions may be performed according to your designed call flow. Please refer to our [Voice API documentation](https://developers.telnyx.com/api-reference/call-commands/dial) to check all your actions in your call scenario.

## Next steps

* Review [WebRTC authentication](https://developers.telnyx.com/development/webrtc/auth/credential-connections) options.
* Explore [Call Control API](https://developers.telnyx.com/api-reference/call-control-applications/list-call-control-applications) documentation.
* Learn more about [webhook fundamentals](https://developers.telnyx.com/development/api-fundamentals/webhooks/receiving-webhooks).
