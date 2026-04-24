---
title: Getting Started with iOS Client SDK
summary: The Telnyx iOS Client SDK makes it easy to get started with video calling and messaging on your iPhone or iPad.
sources:
  - url: https://developers.telnyx.com/docs/video/ios-client-sdk/index
    content_hash: df982a82f6379f7dfc29af2d3b19c35bf09766fb071c9aa30e5e8de762af1af6
updated_at: 2026-04-10T00:00:00Z
---

# Getting Started with iOS Client SDK

The Telnyx iOS Client SDK makes it easy to get started with video calling and messaging on your iPhone or iPad. With just a few lines of code, you can start making calls and sending messages between devices.

The Telnyx Video iOS SDK provides the functionality you need to join and interact with a video room from an iOS application.

#### A link to the repo can be found here:

<a href="https://github.com/team-telnyx/telnyx-video-ios">iOS SDK</a>

## If you prefer to jump right in

<a href="https://github.com/team-telnyx/telnyx-meet-ios">Have a look at our demo app: Telnyx Meet.</a>

## An overview of the Video API

These are important concepts to understand.

* A `Room` represents a real time audio/video/screen share session with other people or participants. It is fundamental to building a video application.

* A `Participant` represents a person inside a `Room`. Each `Room` has one `Local Participant` and one or more `Remote Participants`.

* `Room State` tracks the state of the room as it changes making it extremely easy to understand what's happened to a `Room`.

  * `Room State` could change due to a `Local Participant` has started publishing a stream or because a `Remote Participant`left.

* A `Stream` represents the audio/video media streams that are shared by `Participants` in a `Room`
  * A `Stream` is indentified by it's `participantId` and `streamKey`

* A `Participant` can have one or more `Stream`'s associated with it.

* A `Subscription` is used to subscribe to a `Stream` belonging to a `Remote Participant`

## API of a Room

This should give you high level overview of the Room API and it's functionality.

```
    func connect(statusChanged: @escaping (_ status: RoomStatus) -> Void)

    func disconnect(completion: @escaping () -> Void)

    func updateClientToken(clientToken: String, completion: () -> Void)

    func addStream(key: StreamKey, audio: RTCAudioTrack?, video: RTCVideoTrack?, completion:
    @escaping OnSuccess, onFailed: @escaping OnFailed)

    func updateStream(key: StreamKey, audio: RTCAudioTrack?, video: RTCVideoTrack?, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

    func removeStream(key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

    func addSubscription(participantId: ParticipantId, key: StreamKey, audio: Bool, video: Bool, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

    func pauseSubscription(participantId: ParticipantId, key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

    func resumeSubscription(participantId: ParticipantId, key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

    func updateSubscription(participantId: ParticipantId, key: StreamKey, audio: Bool, video: Bool, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

    func removeSubscription(participantId: ParticipantId, key: StreamKey, completion: @escaping OnSuccess, onFailed: @escaping OnFailed)

    func getWebRTCStatsForStream(participantId: ParticipantId, streamKey: StreamKey, completion: @escaping (_ stats: [String: [String: Any]]) -> Void)

    /// Helpers methods
    func getState() -> State
    func getLocalParticipant() throws -> Participant
    func getLocalStreams() throws -> [StreamKey: Stream]
    func getParticipantStream(participantId: ParticipantId, key: StreamKey) -> Stream?
    func getParticipantStreams(participantId: ParticipantId) throws -> [StreamKey: Stream]
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Events that are triggered in a Room

Here's a list of events that will fire as you make API calls.

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

  /// Triggered when a local stream or a remote stream track has been enabled.
  /// Notifies consumers about remote stream tracks being enabled. For example: when audio is unmuted or video has started on a remote stream.
  var onTrackEnabled: ((_ participantId: ParticipantId, _ streamKey: StreamKey, _ kind: String) -> Void)?

  /// The oposite of` onTrackEnabled`. Triggers when a local stream or a remote stream track has been disabled.
  /// Notifies consumers about remote stream tracks being disabled. For example: when audio is muted or video has stopped on a remote stream.
  var onTrackDisabled: ((_ participantId: ParticipantId, _ streamKey: StreamKey, _ kind: String) -> Void)?

  /// Triggered when subscribed to a remote participant's stream.
  var onSubscriptionStarted: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

  /// Triggered when an ongoing subscription is paused.
  var onSubscriptionPaused: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

  /// Triggered when a paused subsription is resumed.
  var onSubscriptionResumed: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

  /// Triggered when the subscription is reconfigured.
  var onSubscriptionReconfigured: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

  /// Triggered when subscription is ended for a remote participant's stream.
  /// The subscription can be ended by calling `removeSubscription(ParticipantId,StreamKey)` or when the remote participant leaves.
  var onSubscriptionEnded: ((_ participantId: ParticipantId, _ streamKey: StreamKey) -> Void)?

  /// onError
  /// Triggered when there's an error processing incoming events from the server.
  var onError: ((_ error: SdkError) -> Void)?
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Understanding the state of the Room

Everything in the SDK centers around the `Room` object. When the state of the `Room` changes (e.g. a new participant joins or a remote participant starts publishing a stream) the `onStateChanged` event is triggered.

The event is invoked with a `state` parameter which contains the current of the state of the `Room`.

```
 /// Triggered each time the state is updated.
 var onStateChanged: ((_ state: State) -> Void)?
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Before getting started

## Install the SDK

Currently, the Telnyx iOS Video SDK can be installed using CocoaPods. For instructions on that <a href="https://github.com/team-telnyx/telnyx-video-ios">check out our releases repo for iOS</a>

## Get an API Key

You'll need an API key which is associated with your Mission Control Portal account under **API Keys**. You can learn how to do that [here](../reference/create-and-manage-api-keys.md).

An API key is your credential to access our API. It allows you to:

* to authenicate to the Rest API
* to manage your access tokens

## Create a Room to join (if it doesn't exist)

In order to join a room you must create it, if it doesn't already exist. See our [Room Rest API](https://developers.telnyx.com/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room) to create one.

There's also additional resources on other endpoints available to perform basic operations on a `Room`.

## Generate an a client token to join a room

In order to join a room you must have a client token for that `Room`. The `client token` is short lived and you will be able to refresh it using the `refresh token` provided with it when you  request a `client token`.

Please see the [docs here](https://developers.telnyx.com/api-reference/rooms-client-tokens/create-client-token-to-join-a-room#create-client-token-to-join-a-room) to learn how to create a `client token`.

## Code Examples

Enough already let's get to the code. Here are some code examples to get your wet feet on how to start building something with the iOS video SDK.

## Participating in a Room

## Connect to a room

First, you'll need to create a `Room` instance and then connect to it. Once you're connected to a room, you can start sharing audio/video streams with other participant in the rooms.

**Important Note:**
This simply creates an instance of a Room in code it does not use the Rooms Rest API to create a room, mentioned above in "Create a Room to join"\*

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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Once the room is connected you've joined the room as it's local participant. You can see this more clearly by, after connecting, get the local participant.

**Important Note:**
`Room` only has one `Local Participant` but can have multiple `Remote Participant`s.

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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## What is Room context?

Context is any details you want to include about the `LocalParticipant` of the `Room`.

For instance, let's say you want to use `context` to identify a `Participant` with fields from an external system. You could pass a `userId` and `username` as context, like the code snippet above.

These details will be available to all `RemoteParticipant`s in the Room, when they are notified about your presence in the `Room`.

## Working with local media

Publishing audio and/or video from your camera or microphone works by using `MediaDevices`. `MediaDevices` is a helper class that we provide for you to make it easy to grab local media from your device.

```
let stream = MediaDevices.shared().getUserMedia(audio:true, video:true)

// If you want to run your app in a simulator provide a video file name to MediaDevices and it wil be used as the source for the cameraTrack. The video needs to be added to your Main.bundle, for things to work properly.

let cameraTrack = stream.videoTracks.first
let microphoneTrack = stream.audioTracks.first
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Setting the quality of the local video

You can set the camera resolution and fps using `MediaDevices`.

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
// Set the resolution and fps to `Mediadevices`.
MediaDevices.shared().set(format: captureFormat, fps: Int(fps.maxFrameRate))
#endif
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

**Note: If you choose highest resolution and fps, the local video stream will lag if you have poor internet / bandwith**

## Publishing a stream

Once you have tracks from say, a local media device like video from a camera and/our audio from your micrphone you can use those to create a `Stream` and publish it in the `Room`.

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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Unpublishing a stream

If you can longer want to continue publishing a stream you can `unpublish` it.
Naturally the stream you want to unpublish must be added already.

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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Working with Remote Participants and Streams

## A remote participant who joins or leaves the room

When a remote participant joins a a room you will be notified with the `Room.onParticipantJoined` event. And similiarly with `Room.onParticipantLeaving` when a remote participant leaves.

You can use these events to keep track of participants in the room.

```
room.connect {
  room.onParticipantJoined = {
    participantId in
    // This event will trigger when a remote participant joins the room
  }
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Remote participants already in the room

When you connect to a `Room` there may already be remote participants in the `Room`. To understand who is in the `Room` after you connect use the `onParticipantJoined` event.

```
room.connect {
  room.onParticipantJoined = {
    participantId in
    // The event triggers for remote participants who are already in the room, just like it does for a new remote participant that joins the room.
  }
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Display a remote participant's media

In order to understand how to display a remote participants' media let's review on subscriptions work in the API.

It might be helpful to review the Video API overview to get a better understanding of how a `Room` is modeled, especially `Stream` and `Subscription`.

**Major 🔑 about Subscriptions**
In order to display media from a remote stream you need to subscribe to it.

It's important to understand that your `Room` doesn't automatically subscribe to a remote stream being published. It's your **choice to decide whether to subscribe to a given stream.**

## Subscribing to a stream

So let's say the app your building has two users - let's them call them Alice and Bob.

First, Alice joins the `Room` and starts publishing a stream with audio from her microhone and video from her camera like this:
*NOTE: The app on Alice's device runs the following code...*

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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Bob wants to get Alice's stream so he can display it. In order to do so he needs to subscribe to Alice's stream.
*NOTE: The app on Bob's device runs the following code...*

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

    // Alice's stream has a key of 'self' which has the audio track from her microphone and a video from her device's camera. Bob can use these tracks and display them as Alice in his app.
    let aliceCameraTrack = aliceStream.videoTrack
    let aliceMicrophoneTrack = aliceStream.audioTrack
  }
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Handling remote streams that are already publishing in the Room

After you connect to a Room there may be remote participants already in the `Room` who are publishing streams in the Room.

To deal with that use the `onStreamPublished` event:

```
room.connect { status in
  // After connecting to a room the onStreamPublished event will trigger for remote stream
  // that are already being published in the room
  // The onStreamPublished event will trigger
  room.onStreamPublished = {
          participantId, streamKey in

  }
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## Disconnecting from a Room

To disconect from a room do:

```
room.disconnect {
  // after the room disconnect that it's status is .disconnected
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

When you disconnect from a `Room` all `Remote Participant`'s will be notified that you've left the `Room` because the `Room.onParticipantLeft` event will fire on their `Room` instance.


## Related Pages

- [Getting Started with Android Client SDK](../runbooks/getting-started-with-android-client-sdk.md)
- [Getting Started with Video](../runbooks/getting-started-with-video.md)
- [Getting Started with 10DLC](../tutorial/getting-started-with-10dlc.md)
- [Getting started with port-in orders](../tutorial/getting-started-with-port-in-orders.md)
- [Getting Started with JavaScript SDK for Video](../runbooks/getting-started-with-javascript-sdk-for-video.md)
