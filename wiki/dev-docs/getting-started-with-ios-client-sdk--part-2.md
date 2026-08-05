---
title: Getting Started with iOS Client SDK
summary: The Telnyx Video iOS SDK provides the functionality needed to join and interact
  with a video room from an iOS application. This page covers the core concepts of
  the Video API, the Room API surface, lifecycle events, installation, prerequisites,
  and code examples for connecting, publishing local media, subscribing to remote
  streams, and disconnecting.
sources:
- url: https://developers.telnyx.com/docs/video/ios-client-sdk
updated_at: 2026-08-05T14:02:26Z
---

# Getting Started with iOS Client SDK

*Part 2 of 3 — see also: [Part 1](getting-started-with-ios-client-sdk--part-1.md), [Part 3](getting-started-with-ios-client-sdk--part-3.md)*

The Telnyx Video iOS SDK provides the functionality needed to join and interact with a video room from an iOS application. This page covers the core concepts of the Video API, the Room API surface, lifecycle events, installation, prerequisites, and code examples for connecting, publishing local media, subscribing to remote streams, and disconnecting.

## Participating in a Room

### Connect to a Room

First, create a `Room` instance and then connect to it. Once connected, you can start sharing audio/video streams with other participants in the room.

> **Important:** This simply creates an instance of a Room in code; it does not use the Rooms REST API to create a room (see "Create a Room to Join" above).

```swift
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

Once the room is connected you have joined the room as its local participant. You can see this more clearly by, after connecting, getting the local participant.

> **Important:** A `Room` only has one `Local Participant` but can have multiple `Remote Participant`s.

```swift
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

### What is Room Context?

Context is any details you want to include about the `LocalParticipant` of the `Room`. For example, you could use `context` to identify a `Participant` with fields from an external system by passing a `userId` and `username` as context. These details will be available to all `RemoteParticipant`s in the Room when they are notified about your presence in the `Room`.

## Working with Local Media

Publishing audio and/or video from your camera or microphone works by using `MediaDevices`. `MediaDevices` is a helper class provided to make it easy to grab local media from your device.

```swift
let stream = MediaDevices.shared().getUserMedia(audio:true, video:true)

// If you want to run your app in a simulator provide a video file name to MediaDevices and it will be used as the source for the cameraTrack. The video needs to be added to your Main.bundle, for things to work properly.

let cameraTrack = stream.videoTracks.first
let microphoneTrack = stream.audioTracks.first
```

### Setting the Quality of the Local Video

You can set the camera resolution and fps using `MediaDevices`.

```swift
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

> **Note:** If you choose the highest resolution and fps, the local video stream will lag if you have poor internet or bandwidth.

### Publishing a Stream

Once you have tracks from a local media device (for example, video from a camera and/or audio from your microphone) you can use those to create a `Stream` and publish it in the `Room`.

```swift
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

### Unpublishing a Stream

If you no longer want to continue publishing a stream you can `unpublish` it. The stream you want to unpublish must already be added.

```swift
room.connect { status in
  // onStreamUnpublished will trigger once the stream has been unpublished
  room.onStreamUnpublished = {
      participantId, streamKey in

  }

  room.removeStream(key: "camera/mic") {

  }
}
```
