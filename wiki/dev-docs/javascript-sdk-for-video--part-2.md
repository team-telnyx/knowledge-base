---
title: JavaScript SDK for Video
summary: The Telnyx Video JavaScript SDK provides browser-based functionality for
  joining and interacting with video rooms, including publishing local media, subscribing
  to remote streams, and reacting to room events. This page covers installation, core
  concepts (Room, Participant, Stream, Subscription), the Room API, the full set of
  room events, and a step-by-step tutorial for building a working caller/callee video
  app.
sources:
- url: https://developers.telnyx.com/docs/video/javascript-sdk/index
- url: https://developers.telnyx.com/docs/video/javascript-sdk/javascript-video-tutorial
- url: https://developers.telnyx.com/docs/video/javascript-sdk/room-events
updated_at: 2026-08-05T14:02:33Z
---

# JavaScript SDK for Video

*Part 2 of 2 — see also: [Part 1](javascript-sdk-for-video--part-1.md)*

The Telnyx Video JavaScript SDK provides browser-based functionality for joining and interacting with video rooms, including publishing local media, subscribing to remote streams, and reacting to room events. This page covers installation, core concepts (Room, Participant, Stream, Subscription), the Room API, the full set of room events, and a step-by-step tutorial for building a working caller/callee video app.

## Room events

The `Events` interface lists every event emitted by a `Room` instance:

- `state_changed(state)` — fires whenever the room state changes.
- `connected(state)` — fires when the room connects to the server.
- `disconnected(state)` — fires when the room disconnects.
- `participant_joined(participantId, state)` — fires when a remote participant joins. Not fired for the local participant.
- `participant_leaving(participantId, reason, state)` — fires when a participant is leaving, including when the local participant is kicked by a moderator. `reason` is `'kicked'` or `null`.
- `participant_left(participantId, state)` — fires when a remote participant leaves.
- `stream_published(participantId, key, state)` — fires after a stream is successfully published. Fires for both local and remote streams.
- `stream_unpublished(participantId, key, state)` — fires when a stream is unregistered. Fires for both local and remote streams, and for any remaining streams when a remote participant leaves.
- `track_enabled(participantId, key, kind, state)` — fires when an audio or video track is enabled (for example, audio unmuted or video started on a remote stream).
- `track_disabled(participantId, key, kind, state)` — opposite of `track_enabled`.
- `track_censored(participantId, key, kind, state)` — fires when a track is censored by a moderator. If the corresponding track is `null`, nothing visible happens.
- `track_uncensored(participantId, key, kind, state)` — opposite of `track_censored`.
- `audio_activity(participantId, key, state)` — fires when there is audio activity. `key` is `null` when the activity corresponds to a participant speaking rather than a specific stream.
- `subscription_started(participantId, key, state)` — fires when a subscription to a remote stream starts.
- `subscription_reconfigured(participantId, key, state)` — fires when a subscription is reconfigured via `updateSubscription`.
- `subscription_ended(participantId, key, state)` — fires when a subscription ends, either via `removeSubscription` or because the remote participant left.
- `message_received(participantId, message, recipients, state)` — fires when a message is received. `recipients` is `null` when the message was broadcast to all participants.
- `network_metrics_report(networkMetrics)` — fires with network metrics when reporting is enabled.

Register a handler with `room.on(eventName, handler)`:

```js
room.on('connected', async () => {
  // ...
});
```

## Tutorial: build a caller/callee video app

This walkthrough builds a vanilla JavaScript web app that places a video call between a caller and a callee.

### Get an API key

You need a Telnyx account and an API key to interact with the Rooms API.

- [Sign up](https://telnyx.com/sign-up) for a free account if you don't have one.
- Navigate to [API Keys](https://portal.telnyx.com/#/app/api-keys) and click **Create API Key**.
- Copy the key.

### Create a room

Use the Rooms API to create a room. Replace `YOUR_API_KEY` with your key:

```bash
curl -X POST "https://api.telnyx.com/v2/rooms" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  --data-binary '{
  "unique_name": "My room",
  "max_participants": "10",
  "webhook_event_url": "https://example.com",
  "enable_recording": "false"
}'
```

The response includes an `id` field — that is your new room's ID.

### Generate a client token

Use the [create a room client token endpoint](https://developers.telnyx.com/api-reference/rooms/create-a-room#create-a-room) to mint a client access token. Replace `ROOM_ID` with the room ID from the previous step:

```bash
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"refresh_token_ttl_secs":3600,"token_ttl_secs":600}' \
  https://api.telnyx.com/v2/rooms/ROOM_ID/actions/generate_join_client_token
```

The `token` field in the response is the client access token used to join the room.

### Checkpoint

At this point you should have:

- An API key
- A room ID
- A room client access token

### Connect and get local media

Inside the `room.initialize` block, connect to the room and use the standard WebRTC API to obtain local audio and video tracks:

```js
room.on("connected", async () => {
  let callerStream = await navigator.mediaDevices.getUserMedia({
    audio: true,
    video: true
  });
  console.log("got local stream using getUserMedia...");

  let callerAudioTrack = callerStream.getAudioTracks()[0];
  let callerVideoTrack = callerStream.getVideoTracks()[0];
});
```

### Publish and render the local stream

Publish the local stream with the key `"caller"` and render it to the DOM:

```js
room.on("connected", async () => {
  let callerStream = await navigator.mediaDevices.getUserMedia({
    audio: true,
    video: true
  });
  console.log("got local stream using getUserMedia...");

  let callerAudioTrack = callerStream.getAudioTracks()[0];
  let callerVideoTrack = callerStream.getVideoTracks()[0];

  await room.addStream("caller", {
    audio: callerAudioTrack,
    video: callerVideoTrack
  });
  console.log("published local stream to the room...");

  let videoElement = document.getElementById("caller");
  videoElement.srcObject = callerStream;
});
```

### Subscribe to the callee's remote stream

The `stream_published` event fires for both local and remote streams. Ignore the caller's own stream and subscribe to the remote one:

```js
room.on("stream_published", async (participantId, streamKey, state) => {
  let participant = state.participants.get(participantId);
  if (participant.origin === "local") {
    return;
  }

  await room.addSubscription(participantId, streamKey, {
    audio: true,
    video: true
  });
});
```

### Render the callee's remote stream

When the subscription starts, retrieve the remote stream and render it:

```js
room.on("subscription_started", (participantId, streamKey, state) => {
  console.log(
    `subscription to the: ${participantId} ${streamKey} stream started...`
  );

  let remoteStream = room.getParticipantStream(participantId, streamKey);

  let remoteMediaStream = new MediaStream([
    remoteStream.audioTrack,
    remoteStream.videoTrack
  ]);
  const calleeVideo = document.getElementById("callee");
  calleeVideo.srcObject = remoteMediaStream;
});
```

### Run the app

- Open the [sandbox](https://codesandbox.io/s/first-telnyx-video-call-zgk33u?file=/src/main.js) in one tab — this is the caller.
- Open the [deployed app](https://zgk33u.csb.app/) in another tab — this is the callee.

From the caller app, click the call button, allow camera/microphone access, and confirm you see your local video. From the callee app, click the call button; the caller's app will log the subscription and render the callee's video/audio. If you see errors, your client token has likely expired — regenerate it using the steps above.
