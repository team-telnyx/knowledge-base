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

*Part 4 of 4 — see also: [Part 1](telnyx-video-sdks--part-1.md), [Part 2](telnyx-video-sdks--part-2.md), [Part 3](telnyx-video-sdks--part-3.md)*

Telnyx Video Rooms provide a real-time audio, video, and screen-share platform accessible via JavaScript, Android, and iOS client SDKs. This page covers the core concepts, prerequisites, and SDK-specific usage for building video applications with Telnyx.

## iOS SDK

The iOS SDK provides functionality to join and interact with a video room from an iOS application. The [repository](https://github.com/team-telnyx/telnyx-video-ios) is available on GitHub, and a sample app ([Telnyx Meet](https://github.com/team-telnyx/telnyx-meet-ios)) demonstrates usage.

### Installation

The iOS SDK is installed via CocoaPods. See the [releases repo](https://github.com/team-telnyx/telnyx-video-ios) for instructions.

### Connect to a Room

```swift
Room.createRoom(
    id: "92f83cf907b6426197ca6ccc83f3cba3",
    clientToken: accessToken,
    context: ["userid": 12345, "username": "jane doe"]
) { room in
    room.connect { status in
        let localParticipant = room.getLocalParticipant()
    }
}
```

The `context` parameter is a dictionary of any details you want to include about the local participant (e.g., userId, username from an external system). These details are available to all remote participants.

### Working with Local Media

Use `MediaDevices` to capture audio and video:

```swift
let stream = MediaDevices.shared().getUserMedia(audio: true, video: true)
let cameraTrack = stream.videoTracks.first
let microphoneTrack = stream.audioTracks.first
```

To run in the simulator, provide a video file name to `MediaDevices` — it will be used as the camera track source. The video file must be in the Main bundle.

### Setting Video Quality

You can configure camera resolution and FPS using `MediaDevices`:

```swift
#if !targetEnvironment(simulator)
guard let camera = RTCCameraVideoCapturer.captureDevices().first(where: {
    $0.position == MediaDevices.shared().cameraPosition
}) else { return }

guard let captureFormat = RTCCameraVideoCapturer.supportedFormats(for: camera)
    .sorted { CMVideoFormatDescriptionGetDimensions($0.formatDescription).width <
              CMVideoFormatDescriptionGetDimensions($1.formatDescription).width }
    .first else { return }

let fps = captureFormat.videoSupportedFrameRateRanges
    .sorted { $0.maxFrameRate < $1.maxFrameRate }.first!

MediaDevices.shared().set(format: captureFormat, fps: Int(fps.maxFrameRate))
#endif
```

Choosing the highest resolution and FPS may cause lag on poor bandwidth.

### Publishing a Stream

```swift
room.connect { status in
    room.onStreamPublished = { participantId, streamKey in }

    room.addStream(
        key: "camera/mic",
        audio: microphoneTrack,
        video: cameraTrack
    ) { }
}
```

### Unpublishing a Stream

```swift
room.onStreamUnpublished = { participantId, streamKey in }
room.removeStream(key: "camera/mic") { }
```

### Working with Remote Participants

```swift
room.connect {
    room.onParticipantJoined = { participantId in
        // Triggered for both new joins and participants already in the room
    }
}
```

### Subscribing to a Remote Stream

When a remote participant publishes a stream, subscribe to it:

```swift
room.connect { status in
    room.onStreamPublished = { participantId, streamKey in
        room.addSubscription(
            participantId: participantId,
            key: streamKey,
            audio: true,
            video: true
        )
    }

    room.onSubscriptionStarted = { participantId, streamKey in
        let aliceStream = room.getParticipantStream(participantId: participantId, key: streamKey)
        let cameraTrack = aliceStream.videoTrack
        let micTrack = aliceStream.audioTrack
    }
}
```

### Disconnecting

```swift
room.disconnect {
    // Room status is now .disconnected
}
```

### Room API Methods

| Method | Description |
|--------|-------------|
| `connect(statusChanged)` | Connect to the room |
| `disconnect(completion)` | Disconnect from the room |
| `updateClientToken(clientToken, completion)` | Refresh the client token |
| `addStream(key, audio, video, completion, onFailed)` | Publish a stream |
| `updateStream(key, audio, video, completion, onFailed)` | Update an existing stream |
| `removeStream(key, completion, onFailed)` | Remove/unpublish a stream |
| `addSubscription(participantId, key, audio, video, completion, onFailed)` | Subscribe to a remote stream |
| `pauseSubscription(participantId, key, completion, onFailed)` | Pause a subscription |
| `resumeSubscription(participantId, key, completion, onFailed)` | Resume a paused subscription |
| `updateSubscription(participantId, key, audio, video, completion, onFailed)` | Reconfigure a subscription |
| `removeSubscription(participantId, key, completion, onFailed)` | End a subscription |
| `getWebRTCStatsForStream(participantId, streamKey, completion)` | Get WebRTC stats |
| `getState()` | Get current room state |
| `getLocalParticipant()` | Get the local participant |
| `getLocalStreams()` | Get local streams |
| `getParticipantStream(participantId, key)` | Get a specific remote stream |
| `getParticipantStreams(participantId)` | Get all streams for a remote participant |

### Room Events (iOS)

| Event | Description |
|-------|-------------|
| `onStateChanged` | Room state updated |
| `onConnected` | Connected to the room |
| `onDisconnected` | Disconnected from the room |
| `onParticipantJoined` | Remote participant joined |
| `onParticipantLeft` | Remote participant left |
| `onStreamPublished` | Stream published (local or remote) |
| `onStreamUnpublished` | Stream unpublished |
| `onTrackEnabled` | Stream track enabled |
| `onTrackDisabled` | Stream track disabled |
| `onSubscriptionStarted` | Subscription to remote stream started |
| `onSubscriptionPaused` | Subscription paused |
| `onSubscriptionResumed` | Subscription resumed |
| `onSubscriptionReconfigured` | Subscription reconfigured |
| `onSubscriptionEnded` | Subscription ended |
| `onError` | Error processing incoming events |

## Server APIs

The following REST APIs manage server-side resources:

- **Rooms** — Create and manage rooms
- **Client Access Tokens** — Generate and refresh tokens for room access
- **Sessions** — Manage room sessions; end a session; mute/unmute/kick all participants
- **Participants** — Search participants by filters such as session ID
- **Recordings** — Manage recordings, including bulk delete
- **Compositions** — Create and manage compositions
