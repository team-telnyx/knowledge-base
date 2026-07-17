---
title: Telnyx Video SDKs
summary: Telnyx Video Rooms is a platform for adding real-time audio and video to
  Web, Android, and iOS applications, built on REST APIs and Client SDKs. This page
  covers the core concepts (Rooms, Participants, Streams, Subscriptions), server-side
  prerequisites (API key, Room creation, client token), and detailed usage of the
  JavaScript, iOS, and Android SDKs including installation, connecting, publishing
  and subscribing to streams, room events, and WebRTC stats.
sources:
- url: https://developers.telnyx.com/docs/video/android-client-sdk
- url: https://developers.telnyx.com/docs/video/get-started/index
- url: https://developers.telnyx.com/docs/video/ios-client-sdk
- url: https://developers.telnyx.com/docs/video/javascript-sdk/index
- url: https://developers.telnyx.com/docs/video/javascript-sdk/javascript-video-tutorial
- url: https://developers.telnyx.com/docs/video/javascript-sdk/room-events
updated_at: 2026-07-17T09:18:10Z
---

# Telnyx Video SDKs

*Part 2 of 5 — see also: [Part 1](telnyx-video-sdks--part-1.md), [Part 3](telnyx-video-sdks--part-3.md), [Part 4](telnyx-video-sdks--part-4.md), [Part 5](telnyx-video-sdks--part-5.md)*

Telnyx Video Rooms is a platform for adding real-time audio and video to Web, Android, and iOS applications, built on REST APIs and Client SDKs. This page covers the core concepts (Rooms, Participants, Streams, Subscriptions), server-side prerequisites (API key, Room creation, client token), and detailed usage of the JavaScript, iOS, and Android SDKs including installation, connecting, publishing and subscribing to streams, room events, and WebRTC stats.

## JavaScript SDK

The Telnyx Video Client SDK provides all the functionality you need to join and interact with a video room from a browser.

### Installation

Install the `@telnyx/video` npm module as a dependency:

```
npm install @telnyx/video --save
```

Then import it in your application code:

```
// main.js
import { Room, createLocalParticipant } from '@telnyx/video';
```

### Connecting to a Room

Now you are ready to connect to a video room that you created. In order to connect to a video room you will require a client token that has the necessary grants to join the room.

```
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

### Understanding the State of the Video Room

The `state_changed` event callback contains the state of the SDK at that point in time. This is an immutable object that you can use in most modern UI libraries like React and Vue.

```
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

Every time the state of the SDK changes the `state_changed` callback is invoked with a new immutable state that represents the current state of the SDK. Since most modern UI libraries are able to compare the two immutable states and render only the components that changed, it makes it easier to integrate the SDK with them rather than depending on multiple event callbacks.

The participant object follows the TypeScript interface:

```
interface Participant {
  id: string;
  context?: string;
  streams: {
    [key: string]: Stream['id'];
  };
}
```

### Publishing your local camera and mic stream

In order to publish a stream you need to define the constraints of the media. The simplest form of the constraints is:

```
const constraints = { audio: true, video: true };
```

With these constraints the SDK will try to obtain both audio and video from the local participant. In order to publish the stream as the local participant you have to use the `publish` method available to you via the room object:

```
room.publish('self', {
  constraints: { audio: true, video: true },
});
```

The first argument to `publish` is a string that acts as the key that you can use to refer to this specific stream. You can use any valid string for this as long as you are consistent in your application. For example, you might use `'self'` for the camera/mic stream and `'presentation'` for screen-share video.

When you make the request to publish a stream, the browser will ask for the necessary permissions required to access the camera and mic. Once the permissions are acquired the SDK will configure and publish the stream to the room you are connected to. At this point you will receive the new state to the `state_changed` event callback with the newly created stream.

The stream object is the most complex object in the state of the SDK. Key properties include:

- `constraints` — the constraints provided by you
- `bitrate` — also configurable when you publish a stream (default `256000`)
- `audioActive` / `videoActive` — whether the audio/video track is being published
- `source` — an instance of `MediaStream` that can be used to render video/audio
- `audioTrack` / `videoTrack` — instances of `MediaStreamTrack` when the track is available
- `isSpeaking` — whether the audio level of the track is high enough to consider the participant who owns this stream is speaking
- `isRemote` — whether the stream originates from a remote source or not
- `isPublishing` — whether the stream is being published
- `isConfiguring` — whether the SDK is currently negotiating the WebRTC connection
- `participantId` — the ID of the participant this stream belongs to

You can't publish another stream of the same key until this stream is published or removed (by unpublishing).

### Knowing when a new participant joins the room

A video room can have multiple participants and you can get a list of all the participants connected to the room at the time by using the `participants` property in the state. If the participant is not publishing any streams the `streams` property of that participant will be an empty object.

For remote streams, the stream object has a few additional properties of interest:

- `videoCodec` / `audioCodec` — the codec used by the remote video/audio (e.g. `vp8`, `opus`); can be used to decide if the browser has the capabilities to decode the tracks
- `subscription.status` — initially `unsubscribed`; will change to `subscribed` once the client subscribes to this stream

### Subscribing to a remote stream

At this point you are ready to subscribe to the remote stream published by the participant. In order to do that you use the `subscribe` method from the room object:

```
room.subscribe('a87dd242-de78-4c19-a09c-23b336c9f25e');
```

This will start the WebRTC negotiation to receive the remote stream. Once successful the `subscription.status` will change to `subscribed`. You can use the `source` property, which is an instance of `MediaStream`, to render the media on the browser. If the remote participant unpublishes this stream the SDK will automatically unsubscribe from the stream and the stream will disappear from the state.

### Room API Reference

The `Room` object is the API you will use to build your video application.

```
export type Room = Immutable<{
  /// The unique identifier of the Room instance
  id: string;

  /// Event listener/handler for various events that are triggered in the room.
  on<E extends keyof Events>(event: E, callback: Events[E]): Unsubscribe;

  /// Connects a Room instance to the server
  connect: () => Promise<void>;

  /// Disconnect a Room instance from the server
  disconnect: () => Promise<void>;

  /// Updates the client token. The client token is a short-lived access token
  /// (default TTL is 600 seconds / 10 minutes) that needs to be refreshed using
  /// a refresh token. Client tokens need to be refreshed before they expire
  /// otherwise the Room instance will automatically disconnect.
  updateClientToken: (clientToken: string) => Promise<void>;

  /// Gets the state of the Room
  getState: () => State;

  /// Gets the local participant for a given Room instance
  getLocalParticipant: () => Participant;

  /// Get the streams associated to the local participant
  getLocalStreams: () => { [key: Stream['key']]: Stream };

  /// Add a stream to a Room
  addStream: (
    key: Stream['key'],
    tracks?: {
      audio?: MediaStreamTrack;
      video?: MediaStreamTrack | { track?: MediaStreamTrack; options?: { enableSimulcast?: boolean } };
    }
  ) => Promise<void>;

  /// Update an existing stream in a Room (e.g. to mute audio by setting the track to null)
  updateStream: (
    key: Stream['key'],
    tracks?: {
      audio?: MediaStreamTrack;
      video?: MediaStreamTrack | { track?: MediaStreamTrack; options?: { enableSimulcast?: boolean } };
    }
  ) => Promise<void>;

  /// Remove a stream (unpublishes it from the room)
  removeStream: (key: string) => Promise<void>;

  /// Subscribe to a stream belonging to a remote participant
  addSubscription: (
    participantId: Participant['id'],
    key: Stream['key'],
    config: { audio: boolean; video: boolean }
  ) => Promise<void>;

  /// Update an existing subscription (e.g. when a remote participant toggles audio or video)
  updateSubscription: (
    participantId: Participant['id'],
    key: Stream['key'],
    config: { audio: boolean; video: boolean }
  ) => Promise<void>;

  /// Remove or stop subscribing to a remote participant's stream
  removeSubscription: (
    participantId: Participant['id'],
    key: Stream['key']
  ) => Promise<void>;

  /// Helper method to easily access all streams for a given remote participant
  getParticipantStreams: (
    participantId: Participant['id']
  ) => Map<Stream['key'], Stream>;

  /// Helper method to easily access a remote participant stream
  getParticipantStream: (
    participantId: Participant['id'],
    key: Stream['key']
  ) => Stream | undefined;

  /// Provides statistics for a local or remote stream
  getWebRTCStatsForStream: (
    participantId: Participant['id'],
    key: Stream['key']
  ) => Promise<WebRTCStats>;

  /// Send a message to one, more than one, or all participants in the room
  sendMessage: (
    message: Message,
    recipients?: Array<Participant['id']>
  ) => Promise<void>;

  enableNetworkMetricsReport: (
    participantIds: Array<Participant['id']>,
    options?: { includeStreams?: boolean }
  ) => Promise<void>;

  disableNetworkMetricsReport: (
    participantIds?: Array<Participant['id']>
  ) => Promise<void>;
}>;
```

A developer is not required to subscribe to every remote stream being published in the room — they can choose. This is useful in situations where conserving bandwidth and CPU resources is a priority. For example, a developer building a video conferencing application that supports 100+ participants may only want to subscribe to 15–20 participants at a time, displaying each set in a separate page, thus significantly saving bandwidth and resources.

### Room Events

The `Events` interface lists every event that can fire on a `Room` instance.

```
export interface Events {
  /// Triggered when the state of the room changes
  state_changed: (state: State) => void;

  /// Triggers on a Room instance when it connects to the server
  connected: (state: State) => void;

  /// Triggers on a Room instance when it disconnects from the server
  disconnected: (state: State) => void;

  /// Triggered when a remote participant joins the room
  participant_joined: (participant: Participant['id'], state: State) => void;

  /// Triggered when a participant is leaving the room because they were kicked
  /// due to a moderator event. Unlike joined/left, the local participant can be kicked.
  participant_leaving: (
    participant: Participant['id'],
    reason: 'kicked' | null,
    state: State
  ) => void;

  /// Triggered when a remote participant leaves the room
  participant_left: (participantId: Participant['id'], state: State) => void;

  /// Triggered after successfully adding or publishing a stream to the room
  /// (fires for both local and remote streams)
  stream_published: (
    participantId: Participant['id'],
    key: Stream['key'],
    state: State
  ) => void;

  /// Triggered after successfully unregistering a stream
  stream_unpublished: (
    participantId: Participant['id'],
    key: Stream['key'],
    state: State
  ) => void;

  /// Triggered when a local or remote stream track has been enabled
  /// (e.g. when audio is unmuted or video has started on a remote stream)
  track_enabled: (
    participantId: Participant['id'],
    key: Stream['key'],
    kind: 'audio' | 'video',
    state: State
  ) => void;

  /// Triggered when a local or remote stream track has been disabled
  /// (e.g. when audio is muted or video has stopped on a remote stream)
  track_disabled: (
    participantId: Participant['id'],
    key: Stream['key'],
    kind: 'audio' | 'video',
    state: State
  ) => void;

  /// Triggered when a track is censored due to a moderator event
  track_censored: (
    participantId: Participant['id'],
    key: Stream['key'],
    kind: 'audio' | 'video',
    state: State
  ) => void;

  /// Triggered when a track is uncensored due to a moderator event
  track_uncensored: (
    participantId: Participant['id'],
    key: Stream['key'],
    kind: 'audio' | 'video',
    state: State
  ) => void;

  /// Triggered when there is audio activity from a particular stream or participant talking in the Room
  audio_activity: (
    participantId: Participant['id'],
    key: Stream['key'] | null,
    state: State
  ) => void;

  /// Triggered when a subscription to a remote stream is started
  subscription_started: (
    participantId: Participant['id'],
    key: Stream['key'],
    state: State
  ) => void;

  /// Triggered when the subscription is reconfigured using updateSubscription
  subscription_reconfigured: (
    participantId: Participant['id'],
    key: Stream['key'],
    state: State
  ) => void;

  /// Triggered when subscription is removed or ended for a remote stream
  subscription_ended: (
    participantId: Participant['id'],
    key: Stream['key'],
    state: State
  ) => void;

  /// Triggered when a new message is received
  message_received: (
    participantId: Participant['id'],
    message: Message,
    recipients: Array<Participant['id']> | null,
    state: State
  ) => void;

  network_metrics_report: (networkMetrics: NetworkMetrics) => void;
}
```

### JavaScript Video Tutorial

A walkthrough that builds a simple web app in vanilla JavaScript to make a video call with audio from a caller to a callee.

**Basic concepts of the video SDK:**

- A `Room` represents a real-time audio/video/screen-share session with other people or participants.
- A `Participant` represents a person inside a `Room`. Each `Room` has one `Local Participant` and one or more `Remote Participants`.
- A `Stream` represents the audio/video media streams shared by `Participants` in a `Room`. A `Stream` is identified by its `participantId` and `streamKey`.
- A `Participant` can have one or more `Stream`s associated with it.
- A `Subscription` is used to subscribe to a `Stream` belonging to a `Remote Participant`.

**Room Events used in the tutorial:**

- `connected` — triggers when a room instance has connected to the server
- `participant_joined` — triggers when a remote participant joins the room
- `stream_published` — triggers when a stream has started being published to the room
- `subscription_started` — triggers when subscription to a remote stream has started

Handling an event looks like this:

```
room.on("connected", async () => {
  ...
});
```

**Connect to the room and get local media:**

```
// connected to the room as the local participant
telnyxVideoClient.on("connected", async () => {
  // use the webrtc api to get media from devices
  let intercomStream = await navigator.mediaDevices.getUserMedia({
    audio: true,
    video: true
  });
  console.log("got local stream using getUserMedia...");

  // Get audio and video tracks from the MediaStream's
  // since the sdk works with MediaStreamTrack
  let intercomAudioTrack = intercomStream.getAudioTracks()[0];
  let intercomVideoTrack = intercomStream.getVideoTracks()[0];
});
```

**Publish the stream and render it:**

```
// add/publish a stream with a key "caller" to the room
await telnyxVideoClient.addStream("intercom", {
  audio: callerAudioTrack,
  video: callerVideoTrack
});
console.log("published local stream to the room...");
```

Render the stream to the DOM:

```
// connected to the room as the local participant
room.on("connected", async () => {
  // use the webrtc api to get media from devices
  let callerStream = await navigator.mediaDevices.getUserMedia({
    audio: true,
    video: true
  });
  console.log("got local stream using getUserMedia...");

  // Get audio and video tracks from the MediaStream's
  let callerAudioTrack = callerStream.getAudioTracks()[0];
  let callerVideoTrack = callerStream.getVideoTracks()[0];

  // add/publish the stream with the key "caller" to the room
  await room.addStream("caller", {
    audio: callerAudioTrack,
    video: callerVideoTrack
  });
  console.log("published local stream to the room...");

  // render the caller stream to the page/DOM
  let videoElement = document.getElementById("caller");
  videoElement.srcObject = callerStream;
});
```

**Subscribe to the callee's remote stream:**

The `stream_published` event is triggered for both local and remote streams. In the caller/callee scenario, you want to know when the callee's remote stream starts publishing so you can subscribe to it. The caller has already published a "caller" stream so that event can be ignored.

When a stream is published in a room it doesn't mean its audio and video tracks are accessible yet. In order to access a remote stream's tracks you must explicitly subscribe to that stream and wait for the `subscription_started` event.

```
// a stream has been published to the room
room.on("stream_published", async (participantId, streamKey, state) => {
  // ignore streams that are published by the local participant
  let participant = state.participants.get(participantId);
  if (participant.origin === "local") {
    return;
  }

  // the remote stream is identified using the participantId and streamKey
  // you need to subscribe to a remote stream in order to access its MediaStreamTracks
  await room.addSubscription(participantId, streamKey, {
    audio: true,
    video: true
  });
});
```

**Render the callee's remote stream:**

```
// a subscription to a remote stream has started
room.on("subscription_started", (participantId, streamKey, state) => {
  console.log(
    `subscription to the: ${participantId} ${streamKey} stream started...`
  );

  // use a helper method to easily access a remote participants' stream
  let remoteStream = room.getParticipantStream(participantId, streamKey);

  // create a MediaStream object from the remote stream's track so we can render it
  let remoteMediaStream = new MediaStream([
    remoteStream.audioTrack,
    remoteStream.videoTrack
  ]);
  const calleeVideo = document.getElementById("callee");
  calleeVideo.srcObject = remoteMediaStream;
});
```
