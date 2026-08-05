---
title: WebRTC Voice SDKs - Flutter to Index
summary: A consolidated reference for the Telnyx WebRTC Voice SDKs covering shared
  concepts (client/call classes, call states, authentication, multi-client registration,
  common call-flow patterns, and pricing), platform-specific push notification setup
  for iOS, Android, Flutter, and React Native, and troubleshooting tools including
  call detail records and debug data interpretation.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/index
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native
- url: https://developers.telnyx.com/docs/voice/webrtc/sdk-commonalities
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/debug-logs
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/detail-records/index
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/interpreting-debug-data/index
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/contact-center/index
updated_at: 2026-08-05T14:08:06Z
---

# WebRTC Voice SDKs - Flutter to Index

*Part 4 of 5 — see also: [Part 1](webrtc-voice-sdks-flutter-to-index--part-1.md), [Part 2](webrtc-voice-sdks-flutter-to-index--part-2.md), [Part 3](webrtc-voice-sdks-flutter-to-index--part-3.md), [Part 5](webrtc-voice-sdks-flutter-to-index--part-5.md)*

A consolidated reference for the Telnyx WebRTC Voice SDKs covering shared concepts (client/call classes, call states, authentication, multi-client registration, common call-flow patterns, and pricing), platform-specific push notification setup for iOS, Android, Flutter, and React Native, and troubleshooting tools including call detail records and debug data interpretation.

## Contact Center (CCaaS) Implementation

A Contact Center as a Service solution built on Telnyx WebRTC uses SIP connection credentials with Park Outbound Calls and webhook events for enhanced functionality and seamless communication flows.

### Key features

**Webhook events**

- Monitor SIP connection events in real time.
- Receive notifications for call events: dialing, answering, bridging, hang-up, voicemail completion.
- Primary/failover URL configuration for reliability.

**Park Outbound Calls**

- Temporarily hold calls until further instructions via the Voice API.
- Enable additional processing or decision-making before connecting.
- Provide customizable call handling experiences.

**Backend application requirements**

- Use Telnyx's call control capabilities (Voice API).
- Issue commands based on webhook events: answer, play audio, bridge, transfer.
- Handle sophisticated workflows for call routing.

### Inbound call flow

1. User calls the main number, answered with a text-to-speech greeting.
2. IVR menu presents options to mark call attributes (language, skills, department).
3. Call transferred to a queue, parked while waiting for an agent.
4. Auto-transfer to the most idle agent or manual cherry-picking.
5. Call recording initiated when the agent answers.
6. Call forwarded to multiple agents simultaneously with recording enabled.
7. Additional call control: mute, hold, transcription, text-to-speech announcements.

### Frontend implementation

#### Authentication

Agent desktop applications should authenticate using tokens generated from individual telephony credentials created for each agent. When an agent logs in, the frontend requests an authentication token from the backend, which is then used for subsequent API requests in the WebRTC client. When a call is received, you can see which agents are logged in with the on-demand generated credentials. The call center service uses the Call Control API to dial each of the generated credentials to connect the caller with one of the available agents. Once agents are logged in, the WebRTC client informs the call center backend that the agents are registered, so the backend has a list of agents it can dial each time an inbound call is received.

#### Agent desktop application

The agent desktop application should support:

- **Agent status management** — the agent reports their current status (Available/Unavailable) so the backend can decide which agent receives the next call.

![Agent desktop application with status management](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/agent-desktop-application.png?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=5f75806bf0a64bd842b47228ab48dce3)

- **Call control toolbar** — buttons for handling calls: Pickup, Disconnect, Mute, Hold, etc.

![Call control toolbar with call handling options](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/call-control-toolbar.png?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=26966fe96c9b741336bf51d14aa0e0f1)

- **Queue view** — monitor calls parked in queues and pick up a call manually; present additional data like position in queue and estimated wait time.

![Queue view showing parked calls](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/queue-view.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=44d6c89695f93b0210194f1177f8656d)

#### Audio device settings

Get a list of available audio devices:

```
async function() {
  const client = new TelnyxRTC(options);
  let result = await client.getDevices();
  console.log(result);
}
```

Set the active audio device:

```
const constraints = await client.setAudioSettings({
  micId: '772e94959e12e589b1cc71133d32edf543d3315cfd1d0a4076a60601d4ff4df8',
  micLabel: 'Internal Microphone (Built-in)',
  echoCancellation: false
})
```

#### Call control toolbar

Toggle microphone:

```
await call.toggleAudioMute()
console.log(call.state) // => 'muted'

await call.toggleAudioMute()
console.log(call.state) // => 'unmuted'
```

Toggle call hold:

```
await call.toggleHold()
console.log(call.state) // => 'held'

await call.toggleHold()
console.log(call.state) // => 'active'
```

### Backend implementation

The backend application handles call routing, IVR logic, and agent management through Telnyx Voice API webhooks.

#### User authentication

For each user, generate on-demand telephony credentials stored in a database and associated with the user login. The agent desktop application requests an authentication token created from those telephony credentials.

Generate on-demand telephony credentials (optionally with `expires_at`):

```
const telnyx = require('telnyx')('YOUR_API_KEY');

const { data: telephonyCredentials } = await telnyx.telephonyCredentials.create({
  "connection_id": "1234567890",
  "name": "My-new-credential",
  "expires_at": EXPIRATION_DATE
});
```

Create an authentication token:

```
const telnyx = require('telnyx')('YOUR_API_KEY');

const accessToken = await telnyx.telephonyCredentials.generateAccessTokenFromCredential('CREDENTIAL_ID');
```

#### Call flow

The backend fully controls the call flow from initiation to disconnect. Based on webhook notifications, the backend decides which actions to apply. With CRM integration, caller data can be retrieved (e.g. by caller number):

```
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

For `call.initiated`, answer the call and provide an initial greeting with IVR options using `speak`:

```
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

Observe DTMF digits to choose the next action:

```
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

When the call is enqueued, play a prompt and music to the caller waiting for an available agent, and update the frontend queue view via WebSocket:

```
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

Additional actions for other event types can be performed per the [Voice API documentation](https://developers.telnyx.com/api-reference/call-commands/dial).
