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

*Part 3 of 5 — see also: [Part 1](telnyx-video-sdks--part-1.md), [Part 2](telnyx-video-sdks--part-2.md), [Part 4](telnyx-video-sdks--part-4.md), [Part 5](telnyx-video-sdks--part-5.md)*

Telnyx Video Rooms is a platform for adding real-time audio and video to Web, Android, and iOS applications, built on REST APIs and Client SDKs. This page covers the core concepts (Rooms, Participants, Streams, Subscriptions), server-side prerequisites (API key, Room creation, client token), and detailed usage of the JavaScript, iOS, and Android SDKs including installation, connecting, publishing and subscribing to streams, room events, and WebRTC stats.

## iOS SDK

The Telnyx Video iOS SDK provides the functionality you need to join and interact with a video room from an iOS application. A demo app, [Telnyx Meet](https://github.com/team-telnyx/telnyx-meet-ios), is available.

### Installation

Currently, the Telnyx iOS Video SDK can be installed using CocoaPods. See the [iOS releases repo](https://github.com/team-telnyx/telnyx-video-ios) for instructions.

### API of a Room

```
func connect(statusChanged: @escaping (_ status: RoomStatus) -> Void)

func disconnect(completion: @escaping () -> Void)

func updateClientToken(clientToken: String, completion: () -> Void)

func addStream(key: StreamKey, audio: RTCAudioTrack?, video: RTCVideoTrack?, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func updateStream(key: StreamKey, audio: RTCAudioTrack?, video: RTCVideoTrack?, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func removeStream(key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func addSubscription(participantId: ParticipantId, key: StreamKey, audio: Bool, video: Bool, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func pauseSubscription(participantId: ParticipantId, key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func resumeSubscription(participantId: ParticipantId, key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func updateSubscription(participantId: ParticipantId, key: StreamKey, audio: Bool, video: Bool, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func removeSubscription(participantId: ParticipantId, key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

func getWebRTCStatsForStream(participantId: ParticipantId, streamKey: StreamKey, completion: @escaping (_ stats: [String: [String: Any]]) -> Void)

/// Helper methods
func getState() -> State
func getLocalParticipant() throws -> Participant
func getLocalStreams() throws -> [StreamKey: Stream]
func getParticipantStream(participantId: ParticipantId, key: StreamKey) -> Stream?
func getParticipantStreams(participantId: ParticipantId) throws -> [StreamKey: Stream]
```

### Events triggered in a Room

```
/// Triggered each time the state is updated.
var onStateChanged: ((_ state: State) -> Void)?

/// Triggered when connected to a room.
var onConnected: (() -> Void)?

/// Triggered when disconnects from room / leaves room.
var onDisconnected: (() -> Void)?

/// Triggered when a remote participant joins the room.
var onParticipantJoined: ((_ participantId: ParticipantId, _ participant: Participant) -> Void)?

/// Triggered when a remote participant leaves the room.
var onParticipantLeft: ((_ participantId: ParticipantId) -> Void)?

/// Triggered after successfully registering a stream.
var onStreamPublished: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered after successfully unregistering a stream.
var onStreamUnpublished: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when a local or remote stream track has been enabled.
var onTrackEnabled: ((_ participantId: ParticipantId, _ streamKey: StreamKey, _ kind: String) -> Void)?

/// Triggered when a local or remote stream track has been disabled.
var onTrackDisabled: ((_ participantId: ParticipantId, _ streamKey: StreamKey, _ kind: String) -> Void)?

/// Triggered when subscribed to a remote participant's stream.
var onSubscriptionStarted: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when an ongoing subscription is paused.
var onSubscriptionPaused: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when a paused subscription is resumed.
var onSubscriptionResumed: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when the subscription is reconfigured.
var onSubscriptionReconfigured: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when subscription is ended for a remote participant's stream.
var onSubscriptionEnded: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

/// Triggered when there's an error processing incoming events from the server.
var onError: ((_ error: SdkError) -> Void)?
```

### Participating in a Room

**Connect to a room.** First, create a `Room` instance and then connect to it. Once you're connected to a room, you can start sharing audio/video streams with other participants in the room.

> This simply creates an instance of a Room in code; it does not use the Rooms REST API to create a room.

```
// Create an instance of a Room
Room.createRoom(
            id: "92f83cf907b6426197ca6ccc83f3cba3",
            clientToken: accessToken,
            context: ["userid": 12345, "username": "jane doe"])
{ room in
  // Once a room is created we can connect to it
  room.connect { status in

  }
}
```

Once the room is connected you've joined the room as its local participant. A `Room` only has one `Local Participant` but can have multiple `Remote Participant`s.

```
Room.createRoom(
            id: "92f83cf907b6426197ca6ccc83f3cba3",
            clientToken: accessToken,
            context: ["username": "jane doe"])
{ room in
    room.connect { status in
        let localParticipant = room.getLocalParticipant()
    }
}
```

**What is Room context?** Context is any details you want to include about the `LocalParticipant` of the `Room`. For instance, you could pass a `userId` and `username` as context to identify a `Participant` with fields from an external system. These details will be available to all `RemoteParticipant`s in the Room when they are notified about your presence.

### Working with local media

Publishing audio and/or video from your camera or microphone works by using `MediaDevices`, a helper class that makes it easy to grab local media from your device.

```
let stream = MediaDevices.shared().getUserMedia(audio:true, video:true)

// If you want to run your app in a simulator provide a video file name to MediaDevices
// and it will be used as the source for the cameraTrack. The video needs to be added to your Main.bundle.

let cameraTrack = stream.videoTracks.first
let microphoneTrack = stream.audioTracks.first
```

**Setting the quality of the local video.** You can set the camera resolution and fps using `MediaDevices`:

```
#if !targetEnvironment(simulator)
guard let camera = RTCCameraVideoCapturer.captureDevices().first(where: {
    $0.position == MediaDevices.shared().cameraPosition }) else {
        return
    }
// Choose a suitable resolution/capture format
guard let captureFormat = RTCCameraVideoCapturer.supportedFormats(for: camera).sorted { (f1, f2) -> Bool in
    let width1 = CMVideoFormatDescriptionGetDimensions(f1.formatDescription).width
    let width2 = CMVideoFormatDescriptionGetDimensions(f2.formatDescription).width
    return width1 < width2
}.first else {
    return
}
// Choose a suitable fps
let fps = captureFormat.videoSupportedFrameRateRanges.sorted { return $0.maxFrameRate < $1.maxFrameRate }.first!
// Set the resolution and fps to MediaDevices.
MediaDevices.shared().set(format: captureFormat, fps: Int(fps.maxFrameRate))
#endif
```

> If you choose the highest resolution and fps, the local video stream will lag if you have poor internet / bandwidth.

### Publishing and unpublishing a stream

Once you have tracks from a local media device (video from a camera and/or audio from a microphone) you can use those to create a `Stream` and publish it in the `Room`:

```
room.connect { status in
  let cameraTrack: RTCVideoTrack
  let microphoneTrack: RTCAudioTrack

  // The onStreamPublished will trigger once the stream has started publishing in the room
  room.onStreamPublished = {
          participantId, streamKey in

  }

  room.addStream(
      key: "camera/mic",
      audio: microphoneTrack,
      video: cameraTrack){

  }
}
```

To unpublish a stream, call `removeStream`:

```
room.connect { status in
  // onStreamUnpublished will trigger once the stream has been unpublished
  room.onStreamUnpublished = {
      participantId, streamKey in

  }

  room.removeStream(key: "camera/mic") {

  }
}
```

### Working with Remote Participants and Streams

When a remote participant joins a room you will be notified with the `Room.onParticipantJoined` event, and similarly with `Room.onParticipantLeaving` when a remote participant leaves. Use these events to keep track of participants in the room.

```
room.connect {
  room.onParticipantJoined = {
    participantId in
    // This event will trigger when a remote participant joins the room
  }
}
```

When you connect to a `Room` there may already be remote participants in the `Room`. The `onParticipantJoined` event also fires for remote participants who are already in the room.

**Display a remote participant's media.** In order to display media from a remote stream you need to subscribe to it. Your `Room` doesn't automatically subscribe to a remote stream being published — it's your choice to decide whether to subscribe to a given stream.

**Subscribing to a stream.** Alice joins the `Room` and starts publishing a stream with audio from her microphone and video from her camera:

```
room.connect{
  status in
  // Let's assume that we have the tracks for Alice's camera and microphone already

  // Alice starts publishing a stream in the room
  room.addStream(
      key: "self",
      audio: microphoneTrack,
      video: cameraTrack){
  }
}
```

Bob wants to get Alice's stream so he can display it. He needs to subscribe to Alice's stream:

```
room.connect { status in
  // onStreamPublished event is triggered notifying him that Alice's stream is being published
  room.onStreamPublished = {
          participantId, streamKey in

          // Bob subscribes to Alice's stream
          room.addSubscription(
            participantId: participantId,
            key: streamKey,
            audio: true,
            video: true
          )

  }

  // onSubscriptionStarted triggers when the subscription to Alice's stream has started
  room.onSubscritionStarted = {
    participantId, streamKey in
    // Bob needs to fetch the stream so he can display it
    let aliceStream = room.getParticipantStream(participantId: participantId, key: streamKey)

    // Alice's stream has a key of 'self' which has the audio track from her microphone
    // and a video from her device's camera. Bob can use these tracks and display them as Alice in his app.
    let aliceCameraTrack = aliceStream.videoTrack
    let aliceMicrophoneTrack = aliceStream.audioTrack
  }
}
```

**Handling remote streams that are already publishing in the Room.** After you connect to a Room there may be remote participants already in the `Room` who are publishing streams. The `onStreamPublished` event will trigger for those remote streams as well.

### Disconnecting from a Room

```
room.disconnect {
  // after the room disconnect that its status is .disconnected
}
```

When you disconnect from a `Room` all `Remote Participant`s will be notified that you've left the `Room` because the `Room.onParticipantLeft` event will fire on their `Room` instance.
