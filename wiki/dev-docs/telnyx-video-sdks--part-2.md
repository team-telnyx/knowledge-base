---
title: Telnyx Video SDKs
summary: Telnyx Video Rooms provide a real-time audio, video, and screen-share platform
  accessible via JavaScript, Android, and iOS client SDKs. This page covers the core
  concepts, prerequisites, and SDK-specific usage for building video applications
  with Telnyx.
sources:
- url: https://developers.telnyx.com/docs/video/android-client-sdk
  content_hash: 7230b41146e3a6bdc50ae5c6906c158e5938177ce4916adf38f5246f0379789f
- url: https://developers.telnyx.com/docs/video/get-started/index
  content_hash: 4a8b12fd54cb2addeb6012b4c1270463b99c3588387686a479c204346139f963
- url: https://developers.telnyx.com/docs/video/ios-client-sdk
  content_hash: aa7c3284af98900dfd128454c2f648435c50ce615b47b6596ce922fea3b2c74b
- url: https://developers.telnyx.com/docs/video/javascript-sdk/index
  content_hash: 2795b93096ae650de721364e955a12d28e8e7c18ee96e785b80795ffd89523f1
- url: https://developers.telnyx.com/docs/video/javascript-sdk/javascript-video-tutorial
  content_hash: 0bfd39b1a48ae6f3a85d0a8adb4744c20f4e74ab48b38b1624ee3e63edfd5ae8
- url: https://developers.telnyx.com/docs/video/javascript-sdk/room-events
  content_hash: a433db2aded6a73e8472b085ebe3c98eac836ab39b4e7ec548b6d6813304d24e
- url: https://developers.telnyx.com/docs/voice/outbound-voice-profiles
  content_hash: 990ff92ea817f97ee8ee20fe8e3e95aa4a967e6d550f12368d8d3b1aa57b1cdc
- url: https://developers.telnyx.com/docs/voice/overview/index
  content_hash: 021018458a01a48106693b027d7ca00d5e0560ff763aa5557e854994cff10ec9
updated_at: 2026-06-11T10:40:58Z
---

# Telnyx Video SDKs

*Part 2 of 4 — see also: [Part 1](telnyx-video-sdks--part-1.md), [Part 3](telnyx-video-sdks--part-3.md), [Part 4](telnyx-video-sdks--part-4.md)*

Telnyx Video Rooms provide a real-time audio, video, and screen-share platform accessible via JavaScript, Android, and iOS client SDKs. This page covers the core concepts, prerequisites, and SDK-specific usage for building video applications with Telnyx.

## JavaScript SDK

The JavaScript SDK (`@telnyx/video`) provides all the functionality needed to join and interact with a video room from a browser.

### Installation

```bash
npm install @telnyx/video --save
```

### Import and Connect

```javascript
import { Room, createLocalParticipant } from '@telnyx/video';

const room = new Room(roomId, {
  clientToken: '<CLIENT_TOKEN_FOR_THE_ROOM>',
  localParticipant: createLocalParticipant({
    context: JSON.stringify({ name: 'Bob The Builder', id: 1 }),
  }),
});

room.on('state_changed', (state) => {
  // state is immutable — integrates easily with React, Vue, etc.
});

room.connect().then(() => {
  console.log('You are connected to the room!');
});
```

The `context` field on the local participant is any data you want to associate with that participant (e.g., a user ID from your database). It will be available to all remote participants.

### State Object

The `state_changed` callback receives an immutable state object:

```typescript
type Status =
  | 'initialized'
  | 'connecting'
  | 'connected'
  | 'disconnecting'
  | 'disconnected';

interface State {
  status: Status;
  localParticipantId: Participant['id'];
  participants: { [id: string]: Participant };
  streams: { [id: string]: Stream };
}
```

A `Participant` contains an `id`, optional `context` string, a map of stream keys to stream IDs, a `canReceiveMessages` flag, and an `origin` (`local`, `remote`, or `telephony_engine`).

A `Stream` contains properties such as `id`, `key`, `constraints`, `bitrate`, `audioActive`, `videoActive`, `source` (MediaStream), `audioTrack`, `videoTrack`, `isSpeaking`, `isRemote`, `isPublishing`, `isConfiguring`, `participantId`, and a `subscription` object with a `status` field.

### Publishing a Stream

```javascript
room.publish('self', {
  constraints: { audio: true, video: true },
});
```

The first argument is a string key that identifies this stream (e.g., `'self'` for camera/mic, `'presentation'` for screen share). Once published, the stream's `isPublishing` flag becomes `true` while the WebRTC connection is negotiated. When complete, `isPublishing` and `isConfiguring` both become `false`, and `audioActive`/`videoActive` become `true`.

You can also use `addStream` with explicit tracks:

```javascript
await room.addStream('caller', {
  audio: callerAudioTrack,
  video: callerVideoTrack,
});
```

### Subscribing to a Remote Stream

Remote streams are not automatically subscribed to. You must explicitly subscribe:

```javascript
room.on('stream_published', async (participantId, streamKey, state) => {
  const participant = state.participants.get(participantId);
  if (participant.origin === 'local') return; // ignore local streams

  await room.addSubscription(participantId, streamKey, {
    audio: true,
    video: true,
  });
});
```

Once subscribed, access the remote stream and render it:

```javascript
room.on('subscription_started', (participantId, streamKey, state) => {
  const remoteStream = room.getParticipantStream(participantId, streamKey);
  const remoteMediaStream = new MediaStream([
    remoteStream.audioTrack,
    remoteStream.videoTrack,
  ]);
  const videoElement = document.getElementById('callee');
  videoElement.srcObject = remoteMediaStream;
});
```

If a remote participant unpublishes a stream, the SDK automatically unsubscribes.

### Room API

Key methods on the `Room` object:

| Method | Description |
|--------|-------------|
| `connect()` | Connect to the server |
| `disconnect()` | Disconnect from the server |
| `updateClientToken(clientToken)` | Refresh the client token before it expires |
| `getState()` | Get current room state |
| `getLocalParticipant()` | Get the local participant |
| `getLocalStreams()` | Get streams for the local participant |
| `addStream(key, tracks)` | Publish a stream |
| `updateStream(key, tracks)` | Update an existing stream (e.g., mute by setting track to null) |
| `removeStream(key)` | Unpublish/remove a stream |
| `addSubscription(participantId, key, config)` | Subscribe to a remote stream |
| `updateSubscription(participantId, key, config)` | Update a subscription |
| `removeSubscription(participantId, key)` | Stop subscribing to a remote stream |
| `getParticipantStreams(participantId)` | Get all streams for a remote participant |
| `getParticipantStream(participantId, key)` | Get a specific remote participant stream |
| `getWebRTCStatsForStream(participantId, key)` | Get WebRTC stats for a stream |
| `sendMessage(message, recipients?)` | Send a message to one or more participants |

### Room Events

| Event | Description |
|-------|-------------|
| `state_changed` | Room state updated |
| `connected` | Room connected to server |
| `disconnected` | Room disconnected from server |
| `participant_joined` | Remote participant joined |
| `participant_left` | Remote participant left |
| `participant_leaving` | Participant leaving (includes reason, e.g., `'kicked'`) |
| `stream_published` | Stream published (local or remote) |
| `stream_unpublished` | Stream unpublished (local or remote) |
| `track_enabled` | Stream track enabled (e.g., unmute) |
| `track_disabled` | Stream track disabled (e.g., mute) |
| `track_censored` | Track censored by moderator |
| `track_uncensored` | Track uncensored by moderator |
| `audio_activity` | Audio activity detected (participant speaking) |
| `subscription_started` | Subscription to remote stream started |
| `subscription_reconfigured` | Subscription updated via `updateSubscription` |
| `subscription_ended` | Subscription ended or remote participant left |
| `message_received` | Message received from another participant |
| `network_metrics_report` | Network metrics report |

### Disconnecting

```javascript
room.disconnect().then(() => {
  console.log('Disconnected from room');
});
```

All remote participants will be notified via the `participant_left` event.
