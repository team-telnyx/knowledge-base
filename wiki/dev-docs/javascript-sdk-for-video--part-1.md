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

*Part 1 of 2 — see also: [Part 2](javascript-sdk-for-video--part-2.md)*

The Telnyx Video JavaScript SDK provides browser-based functionality for joining and interacting with video rooms, including publishing local media, subscribing to remote streams, and reacting to room events. This page covers installation, core concepts (Room, Participant, Stream, Subscription), the Room API, the full set of room events, and a step-by-step tutorial for building a working caller/callee video app.

## Overview

The Telnyx Video Client SDK provides all the functionality you need to join and interact with a video room from a browser. It exposes a `Room` object that represents a real-time audio/video/screen-share session, along with an event-driven API for tracking participants, streams, and subscriptions.

Core concepts:

- **Room** — a real-time audio/video/screen-share session with one or more participants.
- **Participant** — a person inside a `Room`. Each room has one `Local Participant` and zero or more `Remote Participants`.
- **Stream** — an audio/video media stream shared by a participant. A stream is identified by its `participantId` and `streamKey`.
- **Subscription** — the mechanism used to receive a stream belonging to a remote participant.

## Installation

Install the `@telnyx/video` npm module and import it in your application code:

```bash
npm install @telnyx/video --save
```

```js
// main.js
import { Room, createLocalParticipant } from '@telnyx/video';
```

## Connecting to a room

To connect to a video room you need a client token with the necessary grants to join the room. Create a `Room` instance, register a `state_changed` listener, and call `connect()`:

```js
const room = new Room(roomId, {
  clientToken: '<CLIENT_TOKEN_FOR_THE_ROOM>',
  localParticipant: createLocalParticipant({
    context: JSON.stringify({ name: 'Bob The Builder', id: 1 }),
  }),
});

const stateCallback = (state) => {
  // the state object is immutable and can be easily integrated with most modern UI libraries like React, Vue etc.
};

room.on('state_changed', stateCallback);

room.connect().then(() => {
  console.log('You are connected to the room!');
});
```

The `context` field lets you attach arbitrary data (for example, a user ID from your database) to the local participant.

## Understanding the state of the room

The `state_changed` callback receives an immutable `State` object representing the SDK at that point in time. Because the state is immutable, modern UI libraries such as React and Vue can compare successive states and re-render only the components that changed.

```ts
type Status =
  | 'initialized'
  | 'connecting'
  | 'connected'
  | 'disconnecting'
  | 'disconnected';

interface State {
  status: Status;
  localParticipantId: Participant['id'];
  participants: {
    [id: string]: Participant;
  };
  streams: {
    [id: string]: Stream;
  };
}
```

The local participant's ID is a UUID v4 generated when the local participant is created. The `Participant` interface is:

```ts
interface Participant {
  id: string;
  context?: string;
  streams: {
    [key: string]: Stream['id'];
  };
}
```

As the SDK progresses through `initialized` → `connecting` → `connected`, the only field that changes in the early states is `status`. Once connected, you can begin publishing streams.

## Publishing a local stream

Define media constraints and call `room.publish()` with a string key that identifies the stream (for example, `'self'` for the camera/mic stream or `'presentation'` for a screen share):

```js
const constraints = { audio: true, video: true };

room.publish('self', {
  constraints: { audio: true, video: true },
});
```

The browser will prompt for camera and microphone permissions. Once granted, the SDK configures and publishes the stream. You cannot publish another stream with the same key until the current one is published or removed.

The resulting `Stream` object includes:

- `id`, `key`, `constraints`, `bitrate` (default `256000`, configurable)
- `audioActive`, `videoActive` — whether the audio/video track is being published
- `source` — a `MediaStream` instance usable for rendering
- `audioTrack`, `videoTrack` — `MediaStreamTrack` instances once available
- `isSpeaking` — whether the audio level indicates the participant is speaking
- `isRemote` — whether the stream originates from a remote source
- `isPublishing` — whether the stream is being published
- `isConfiguring` — whether the SDK is currently negotiating the WebRTC connection
- `participantId` — the owning participant

Once the WebRTC connection is negotiated, `isPublishing` and `isConfiguring` both become `false` and the stream is available for subscription by other clients in the room.

## Remote participants and streams

A room can have multiple participants. The `participants` map in state lists everyone currently in the room. When a new participant joins, their entry appears in `participants` and any streams they publish appear in `streams`.

Remote stream objects include a few additional properties:

- `videoCodec`, `audioCodec` — the codecs used by the remote stream (for example `vp8` and `opus`). Use these to decide whether the browser can decode the tracks.
- `subscription.status` — starts as `'unsubscribed'` and changes to `'subscribed'` once the client subscribes.

## Subscribing to a remote stream

Use `room.subscribe()` with the remote stream's ID to begin WebRTC negotiation. Once successful, `subscription.status` becomes `'subscribed'` and the `source` `MediaStream` can be rendered in the UI. If the remote participant unpublishes the stream, the SDK automatically unsubscribes and the stream is removed from state.

```js
room.subscribe('a87dd242-de78-4c19-a09c-23b336c9f25e');
```

## Room API reference

The `Room` object exposes the following methods:

- `on(event, callback)` — register an event listener; returns an unsubscribe function.
- `connect()` — connect the room to the server. The state `status` transitions through `connecting` to `connected`.
- `disconnect()` — disconnect the room from the server.
- `updateClientToken(clientToken)` — refresh the short-lived client token. Tokens default to a TTL of 600 seconds (10 minutes); if a token expires the room disconnects automatically. Use the `generate_join_client_token` endpoint to create a token and `refresh_client_token` to refresh it.
- `getState()` — return the current `State`.
- `getLocalParticipant()` — return the local `Participant`.
- `getLocalStreams()` — return the local participant's streams keyed by stream key.
- `addStream(key, tracks)` — publish a stream. `tracks.audio` and `tracks.video` accept `MediaStreamTrack` instances; `video` may also be an object `{ track, options: { enableSimulcast } }`.
- `updateStream(key, tracks)` — update an existing stream (for example, set `audio` to `null` to mute).
- `removeStream(key)` — unpublish a stream.
- `addSubscription(participantId, key, config)` — subscribe to a remote stream. `config` specifies `{ audio, video }` booleans. Subscriptions are opt-in, which is useful for conserving bandwidth in large rooms (for example, subscribing to only 15–20 of 100+ participants at a time).
- `updateSubscription(participantId, key, config)` — reconfigure an existing subscription (for example, when a remote participant toggles audio or video).
- `removeSubscription(participantId, key)` — stop subscribing to a remote stream.
- `getParticipantStreams(participantId)` — helper returning a `Map` of all streams for a remote participant.
- `getParticipantStream(participantId, key)` — helper returning a single remote stream.
- `getWebRTCStatsForStream(participantId, key)` — return readable WebRTC statistics for a stream (equivalent to `RTCRtpSender.getStats()` / `RTCRtpReceiver.getStats()`).
- `sendMessage(message, recipients?)` — send a message to one, several, or all participants. Currently only `'text'` messages are supported. If `recipients` is omitted, the message is broadcast to everyone.
- `enableNetworkMetricsReport(participantIds, options?)` / `disableNetworkMetricsReport(participantIds?)` — toggle network metrics reporting.

The `Participant` type also includes `canReceiveMessages: boolean` and `origin: 'local' | 'remote' | 'telephony_engine'`.
