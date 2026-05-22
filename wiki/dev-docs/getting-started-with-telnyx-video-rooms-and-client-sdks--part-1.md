---
title: Getting Started with Telnyx Video Rooms and Client SDKs
summary: Build real‑time video into web, Android, and iOS apps with Telnyx Video Rooms.
  This guide explains core concepts (rooms, participants, streams, subscriptions,
  state), how to create rooms and client join tokens, and how to connect, publish,
  and subscribe using the JavaScript, Android, and iOS SDKs—plus token refresh, events,
  and useful server APIs.
sources:
- url: https://developers.telnyx.com/docs/video/get-started/index
- url: https://developers.telnyx.com/docs/video/android-client-sdk
- url: https://developers.telnyx.com/docs/video/ios-client-sdk
- url: https://developers.telnyx.com/docs/video/javascript-sdk/index
- url: https://developers.telnyx.com/docs/video/javascript-sdk/javascript-video-tutorial
- url: https://developers.telnyx.com/docs/video/javascript-sdk/room-events
updated_at: 2026-05-20T09:31:10Z
---

# Getting Started with Telnyx Video Rooms and Client SDKs

*Part 1 of 2 — see also: [Part 2](getting-started-with-telnyx-video-rooms-and-client-sdks--part-2.md)*

Build real‑time video into web, Android, and iOS apps with Telnyx Video Rooms. This guide explains core concepts (rooms, participants, streams, subscriptions, state), how to create rooms and client join tokens, and how to connect, publish, and subscribe using the JavaScript, Android, and iOS SDKs—plus token refresh, events, and useful server APIs.

## Prerequisites and authentication
- Telnyx Mission Control account and an API Key (Portal → API Keys). Use it to call REST APIs that create rooms and generate client join tokens.
- A short‑lived Client Join Token (JWT) is required by clients to enter a room. A Refresh Token (JWT) accompanies it to obtain a fresh client token when it expires.

Useful API reference endpoints:
- Rooms: https://developers.telnyx.com/api-reference/rooms/view-a-list-of-rooms
- Generate client join token: https://developers.telnyx.com/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room
- Room Sessions: https://developers.telnyx.com/api-reference/room-sessions/view-a-list-of-room-sessions
- Room Participants: https://developers.telnyx.com/api-reference/room-participants/view-a-list-of-room-participants
- Room Recordings: https://developers.telnyx.com/api-reference/room-recordings/view-a-list-of-room-recordings
- Room Compositions: https://developers.telnyx.com/api-reference/room-compositions/view-a-list-of-room-compositions

## Core concepts and architecture
- Room: A virtual place where participants communicate in real time (audio/video/screen share).
- Participant: One Local Participant (you) and one or more Remote Participants.
- Stream: Media shared by a participant, identified by participantId and streamKey; can contain audio and/or video tracks.
- Subscription: Your client must subscribe to a remote participant’s stream to receive its media.
- Room State: An immutable snapshot of participants, streams, and status (initialized → connecting → connected → …). SDKs emit state updates to drive your UI.

Platform pieces:
- Client SDKs (JavaScript, Android, iOS) handle WebRTC capture, publishing, subscribing, and state.
- Server APIs create/manage rooms, sessions, recordings/compositions, and participants.

## Create a room and generate client tokens
1) Create a room via REST (Bearer YOUR_API_KEY). See Rooms API.
2) Generate a Client Join Token for that room (defaults to ~10 minutes TTL). You’ll also receive a Refresh Token to mint new client tokens when needed. See Rooms Client Tokens API.
3) Deliver the short‑lived client token to your app (e.g., from your backend) and use it with the SDK to connect.

## JavaScript SDK quickstart
- Install and import:
  - npm install @telnyx/video --save
  - import { Room, createLocalParticipant } from '@telnyx/video'
- Connect with a client token and optional participant context (serialized JSON you want others to see, e.g., name/id):

```js
const room = new Room('<ROOM_ID>', {
  clientToken: '<CLIENT_TOKEN>',
  localParticipant: createLocalParticipant({
    context: JSON.stringify({ name: 'Alice', id: 42 }),
  }),
});

room.on('state_changed', (state) => {
  // Use immutable state to render UI (status, participants, streams)
});

await room.connect();
```

- Publish local camera/mic:
  - Option A (constraints):
    room.publish('self', { constraints: { audio: true, video: true } });
  - Option B (tracks): Acquire MediaStreamTracks and add them:

```js
const ms = await navigator.mediaDevices.getUserMedia({ audio: true, video: true });
await room.addStream('self', {
  audio: ms.getAudioTracks()[0],
  video: ms.getVideoTracks()[0],
});
```

- Subscribe to a remote stream (use the stream id/key from state or the stream_published event):

```js
await room.addSubscription('<remoteParticipantId>', 'self', { audio: true, video: true });
const remote = room.getParticipantStream('<remoteParticipantId>', 'self');
const media = new MediaStream([remote.audioTrack, remote.videoTrack]);
videoEl.srcObject = media;
```

- Key JS events (see [Room and Events](room-and-events.md)):
  - state_changed, connected, disconnected
  - participant_joined / participant_left / participant_leaving
  - stream_published / stream_unpublished
  - track_enabled / track_disabled (and censored/uncensored)
  - audio_activity
  - subscription_started / subscription_reconfigured / subscription_ended
  - message_received, network_metrics_report

- WebRTC stats: room.getWebRTCStatsForStream(participantId, streamKey)

For a guided walkthrough, see [JavaScript Video Tutorial](javascript-video-tutorial.md).

## Android SDK quickstart
Repo: https://github.com/team-telnyx/telnyx-video-android

- Gradle setup (JitPack): add maven { url 'https://jitpack.io' } and dependency:
  implementation 'com.github.team-telnyx:telnyx-video-android:<tag>'
- Permissions: INTERNET, CAMERA, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS.
- Connect:

```kotlin
val room = Room(
  context = context,
  roomId = UUID.fromString("<ROOM_ID>"),
  roomToken = "<CLIENT_TOKEN>",
  externalData = ExternalData(id = 1234, username = "Android User"),
  enableMessages = false
)
room.connect()
```

- Publish audio/video:
  - Create a PublishConfigHelper (direction, streamKey, streamId), then:
    - createAudioTrack(...), createVideoTrack(...), and room.addStream(...) for a new stream
    - room.updateStream(...) to add/remove tracks later
- Remove track/stream: stopCapture()/disposeAudio() then updateStream; or room.removeStream(streamKey)
- Subscribe and render video:
  - Initialize a SurfaceViewRenderer via room.setParticipantSurface(participantId, surface, streamKey)
  - room.addSubscription(participantId, streamKey, streamConfig)
  - Attach the provided VideoTrack with addSink(surface)
- Observables to drive UI:
  - State (status, participants, streams, publishers, subscriptions)
  - Participants, Joined/Leaving events, Connection status
  - Participant stream changed, Talking (audio activity)
- WebRTC stats: room.getWebRTCStatsForStream(participantId, streamKey, callback)

## iOS SDK quickstart
Repo: https://github.com/team-telnyx/telnyx-video-ios
Demo app: https://github.com/team-telnyx/telnyx-meet-ios

- Install via CocoaPods (see releases in the repo).
- Create and connect a Room with context:

```swift
Room.createRoom(
  id: "<ROOM_ID>",
  clientToken: "<CLIENT_TOKEN>",
  context: ["userid": 12345, "username": "Jane"]
) { room in
  room.connect { status in /* handle .connecting/.connected */ }
}
```

- Local media: use MediaDevices to getUserMedia(audio: Bool, video: Bool) and optionally set capture format/fps.
- Publish/unpublish:
  - room.addStream(key: "camera/mic", audio: microphoneTrack, video: cameraTrack)
  - room.removeStream(key: "camera/mic")
- Subscriptions:
  - room.addSubscription(participantId:..., key:..., audio: true, video: true)
  - pause/resume/update/removeSubscription
- Room API highlights:
  - connect, disconnect, updateClientToken
  - addStream, updateStream, removeStream
  - add/pause/resume/update/removeSubscription
  - getWebRTCStatsForStream, getState, getLocalParticipant, getLocalStreams, getParticipantStream(s)
- Events to wire UI:
  - onStateChanged, onConnected, onDisconnected
  - onParticipantJoined/onParticipantLeft
  - onStreamPublished/onStreamUnpublished
  - onTrackEnabled/onTrackDisabled
  - onSubscriptionStarted/Paused/Resumed/Reconfigured/Ended
  - onError

## Managing token expiry
- Client tokens are short‑lived (default TTL ~600s). Refresh them before expiry using the Refresh Token and your backend.
- SDKs support updating tokens at runtime:
  - JavaScript: room.updateClientToken('<NEW_TOKEN>')
  - iOS: room.updateClientToken(clientToken: ...)
  - Android: obtain a fresh token and reconnect or follow SDK guidance to update
- If a token isn’t refreshed in time, the SDK will disconnect. Handle reconnect flows and show UI prompts.
