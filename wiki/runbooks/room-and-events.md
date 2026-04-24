---
title: Room and Events
summary: Telnyx's video JavaScript SDK lets you manage room events and join/leave notifications.
sources:
  - url: https://developers.telnyx.com/docs/video/javascript-sdk/room-events/index
    content_hash: 6c30419d02eb8286671ca8b3f2513c11342cc36a9fa6794b74ba918a52af8e8f
updated_at: 2026-04-10T00:00:00Z
---

# Room and Events

Telnyx's video JavaScript SDK lets you manage room events and join/leave notifications.

Telnyx's video JavaScript SDK lets you manage room events and join/leave notifications.

We've made it much easier to add video capability to your web application using our Javascript SDK.

The `Room` object and the `Events` that occur in a `Room` is the API you will use to build your video application. We've extensively documented the interface for the `Room` and `Events` objects, below.

## Room

```javascript theme={null}
export type Room = Immutable<{
  /// The unique identifier of the Room instance
  id: string;

  /// Event listener/handler for various events that are triggered in the room.
  /// See the Events interface for a list.
  on<E extends keyof Events>(event: E, callback: Events[E]): Unsubscribe;

  /// Connects a Room instance to the server
  /// The state of the room, specifically the status of the room, will change while it's connecting,
  /// if you can listen to these changes with the state_changed event.
  /// Once the room is connected its local partipant will available in State.
  connect: () => Promise<void>;

  /// Disconnect a Room instance from the server
  /// The status of the state of the room will change while it's disconnecting.
  disconnect: () => Promise<void>;

  /// Updates the client token
  /// The client token is a short lived access token that expires after a time to live in seconds,
  /// which needs to be refreshed using a refresh token.
  /// If you are farmilar with how JWT's work you'll understand, head here for [more details](https://jwt.io)
  /// This was set when the client token was created - the default TTL is 600 seconds or 10 minutes.
  ///
  /// Client tokens need to refreshed before they expire otherise the Room instance will automatically
  /// disconnect.
  /// It's up to the developer to keep the client token fresh.
  /// To create a client token please use the `generate_join_client_token` endpoint
  /// To refresh a token please use `refresh_client_token` endpoint
  updateClientToken: (clientToken: string) => Promise<void>;

  /// Gets the state of the Room
  /// What does the state of the room look like?
  /*
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
  */

  /// State is important because there can be lot of things changing in a room at any given moment, especially for really large rooms.
  /// Participants leaving the room, new participants joining, other starting/stopping their video, a moderator kicking
  /// a participant out.
  /// It would be a lot to keep track of manually, which is why we have state.
  /// Don't worry we've abstracted all the accounting, inside our SDK, and provided you with helper methods
  /// like this one, getParticipant(), and getLocalStreams() to make access simple.
  getState: () => State;

  /// Participants and Streams
  /// There's a two entities that are important to understand
  /// and as you can see from the State interface above they are big
  /// part of the State of the Room.
  ///
  /// Stream
  /// A stream represents media stream published by Participant in a Room.
  /// It's identified by it's participantId and streamKey and typically has a audio track or a video
  /// track, or both.

  /// Participants
  /// There are two type of participants: local and remote.
  /// Remote Participant - other participants in the room who are not the local participant.
  /// A local partipant subscribes to streams published by remote participants.
  ///
  /// Local Participant - is the person on a mobile device or desktop that joins the room to publish a stream.
  /// **NOTE**: There can only be one local participant in a room at a given time.

  /// Gets the local participant for a given Room instance
  /// You can use this method to find more details about the local participant in the Room
  ///
  /// What does a Participant look like?
  /*
    export type Participant = Immutable<{
      id: string;
      context?: string;
      streams: {
        [key: string]: Stream['id'];
      };
      canReceiveMessages: boolean;
      origin: 'local' | 'remote' | 'telephony_engine';
    }>;
  */
  getLocalParticipant: () => Participant;

  /// Get the streams associated to the local participant
  getLocalStreams: () => { [key: Stream['key']]: Stream };

  /// Add a stream to a Room
  /// key - is the unique identifier for the stream based on its realted participant.
  /// tracks.audio - the audio track
  /// tracks.video - the video track
  /// Once the promise is completed you can assume that the stream has started publishing in the room.
  addStream: (
    key: Stream['key'],
    tracks?: {
      audio?: MediaStreamTrack;
      video?:
        | MediaStreamTrack
        | { track?: MediaStreamTrack; options?: { enableSimulcast?: boolean } };
    }
  ) => Promise<void>;

  /// Update an existing stream in a Room
  /// key - identifier of the stream
  /// tracks.audio - the audio track
  /// tracks.video - the video track
  ///
  /// Why would you update a Stream?
  /// If you wanted to mute the audio of a particular stream you would update
  /// it and set the track to null
  updateStream: (
    key: Stream['key'],
    tracks?: {
      audio?: MediaStreamTrack;
      video?:
        | MediaStreamTrack
        | { track?: MediaStreamTrack; options?: { enableSimulcast?: boolean } };
    }
  ) => Promise<void>;

  /// Remove a stream
  /// key - identifier of the stream
  /// Removing a stream removes or unpublishes it from the room.
  removeStream: (key: string) => Promise<void>;

  /// Subscriptions
  /// A subscription is used to subscribed to a stream published by a Remote Participant

  /// Subscribe to a stream belonging to a remote participant
  /// participantId - the id of the remote participant
  /// key - the stream key of the stream
  /// config.audio - flag to indicate if you'd like to subscribe to the remote streams' audio
  // config.video - flag to indicate if you'd like to subscribe to the remote streams' video
  /// When the promise is fullfilled a remote stream is added to state.streams
  /// which then can be used to render the audio or video of that stream.
  /// You can access remote participant streams more easily using the getParticipantsStreams
  // and getParticipantStreams helper methods below.
  ///
  /// A developer is not required to subscribe to every remote stream being published in the room instead
  /// they can choose. This is very useful in situations conserving bandwidth and cpu resources is a priority,
  /// For example:
  /// A developer building a vidoe conferencing application and wants to support 100+ participants may only want subscribe
  /// to 15-20 participants at a time display each set in a seperate page, thus significantly saving bandwith and resources.
  addSubscription: (
    participantId: Participant['id'],
    key: Stream['key'],
    config: { audio: boolean; video: boolean }
  ) => Promise<void>;

  /// Update an existing subscription
  /// participantId - the id of the remote participant
  /// key - the stream key of the stream
  /// config.audio - flag to indicate if you'd like to subscribe to the remote streams' audio
  // config.video - flag to indicate if you'd like to subscribe to the remote streams' video
  /// When a remote participant toggles audio or video on a stream that you're subscribed to
  /// you'll need to update that subscription.
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
  /// It presents the same data you'd get from doing:
  /// RTCRtpSender.getStats() - https://developer.mozilla.org/en-US/docs/Web/API/RTCRtpSender/getStats
  /// RTCRtpReceiver.getStats() - https://developer.mozilla.org/en-US/docs/Web/API/RTCRtpReceiver/getStats
  /// using the standard WebRTC APIs but in a much more readable format.
  getWebRTCStatsForStream: (
    participantId: Participant['id'],
    key: Stream['key']
  ) => Promise;

  /// Send a message to one, more than one, or all participants in the room
  /// message - a message type, current only 'text' is supported
  /// receipients? - an array of participants to send the message, if
  /// null the message is broadcasted to everyone in the room.
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

## Room events

```javascript theme={null}
export interface Events {
  /// Triggered when the state of the room changes
  /// For more
  /// TODO
  state_changed: (state: State) => void;

  /// Triggers on a Room instance when it connects to the server
  connected: (state: State) => void;

  /// Triggers on a Room instance when it disconnects from the server
  disconnected: (state: State) => void;

  /// Triggered when a remote participant joins the room
  /// Only triggered for remote participants the local participant does not
  /// need to be notified that they've joined the room since they've initiated
  /// that action themselves by connecting to the Room
  participant_joined: (participant: Participant['id'], state: State) => void;

  /// Triggered when a  participant is leaving the room because they were kicked
  /// due to a moderator event
  /// Unlike the joined and left events the local participant can be kicked from the room
  participant_leaving: (
    participant: Participant['id'],
    reason: 'kicked' | null,
    state: State
  ) => void;

  /// Triggered when a remote participant leaves the room
  participant_left: (participantId: Participant['id'], state: State) => void;

  /// Triggered after successfully adding or publishing a stream to the room
  /// This event is triggered for local and remote streams.
  /// A local stream is one that's published by the local participant in the Room
  /// A remote stream is one that's published by a remote participant in the Room
  stream_published: (
    participantId: Participant['id'],
    key: Stream['key'],
    state: State
  ) => void;

  /// Triggered after successfully unregistering a stream
  /// This event is triggered for both local and remote streams.
  /// It triggered when the local or remote participant remove or stops publishing a stream.
  /// When a remote participant leaves a room it will trigger for any of their related streams.
  stream_unpublished: (
    participantId: Participant['id'],
    key: Stream['key'],
    state: State
  ) => void;

  /// Triggered when a local stream or a remote stream track has been enabled.
  /// Notifies consumers about remote stream tracks being enabled.
  /// For example: when audio is unmuted or video has started on a remote stream.
  track_enabled: (
    participantId: Participant['id'],
    key: Stream['key'],
    kind: 'audio' | 'video',
    state: State
  ) => void;

  /// The oposite of track_enabled
  /// Triggers when a local stream or a remote stream track has been disabled.
  /// Notifies consumers about remote stream tracks being disabled.
  /// For example: when audio is muted or video has stopped on a remote stream.
  track_disabled: (
    participantId: Participant['id'],
    key: Stream['key'],
    kind: 'audio' | 'video',
    state: State
  ) => void;

  /// Triggered  when a track is censored due to a moderator event
  /// Like the kick moderator event in participant_leaving, both local and remote streams can be
  /// censored.
  ///
  /// Since a Stream consists of an audio and video track, either can be censored by a moderator
  /// If the audio or video track on given stream is null, effectively nothing happens.
  track_censored: (
    participantId: Participant['id'],
    key: Stream['key'],
    kind: 'audio' | 'video',
    state: State
  ) => void;

  /// Triggered when a  track is uncensored due to a moderator event
  /// Opposite of track_censored
  /// Naturally, a track must be censored to order be uncensored.
  track_uncensored: (
    participantId: Participant['id'],
    key: Stream['key'],
    kind: 'audio' | 'video',
    state: State
  ) => void;

  /// Triggered when there is audio activity from a particular stream or participant talking in the Room
  /// When there's audio activity when a participant speaking this event will trigger with the participant id that's talking and the stream key will be null
  audio_activity: (
    participantId: Participant['id'],
    key: Stream['key'] | null,
    state: State
  ) => void;

  /// Triggered a subscription to a remote stream is started
  subscription_started: (
    participantId: Participant['id'],
    key: Stream['key'],
    state: State
  ) => void;

  /// Triggered when the subscription is reconfigured using the updateSubscription method
  subscription_reconfigured: (
    participantId: Participant['id'],
    key: Stream['key'],
    state: State
  ) => void;

  /// Triggered when subscription is removed or ended for a remote stream
  /// A subscription can be ended by calling `removeSubscription(ParticipantId,StreamKey)`
  /// This is also triggered when a remote participant leaves the room.
  subscription_ended: (
    participantId: Participant['id'],
    key: Stream['key'],
    state: State
  ) => void;

  /// onMessageReceived
  /// Triggered when a new message is recieved either by one or more participants or broadcasted to all participants
  /// in the room.
  /// participantId - sender of the message
  /// recipients - an array of participants the message was sent to. when null the message was broadcasted to the all participants in the room.
  message_received: (
    participantId: Participant['id'], // the participant that sent the message
    message: Message,
    recipients: Array<Participant['id']> | null,
    state: State
  ) => void;

  network_metrics_report: (networkMetrics: NetworkMetrics) => void;
}
```


## Related Pages

- [Port-in events](../runbooks/port-in-events.md)
- [Port-out events](../runbooks/port-out-events.md)
