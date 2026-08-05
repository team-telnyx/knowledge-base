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

*Part 3 of 3 — see also: [Part 1](getting-started-with-ios-client-sdk--part-1.md), [Part 2](getting-started-with-ios-client-sdk--part-2.md)*

The Telnyx Video iOS SDK provides the functionality needed to join and interact with a video room from an iOS application. This page covers the core concepts of the Video API, the Room API surface, lifecycle events, installation, prerequisites, and code examples for connecting, publishing local media, subscribing to remote streams, and disconnecting.

## Working with Remote Participants and Streams

### A Remote Participant Who Joins or Leaves the Room

When a remote participant joins a room you will be notified with the `Room.onParticipantJoined` event, and similarly with `Room.onParticipantLeft` when a remote participant leaves. You can use these events to keep track of participants in the room.

```swift
room.connect {
  room.onParticipantJoined = {
    participantId in
    // This event will trigger when a remote participant joins the room
  }
}
```

### Remote Participants Already in the Room

When you connect to a `Room` there may already be remote participants in the `Room`. To understand who is in the `Room` after you connect, use the `onParticipantJoined` event.

```swift
room.connect {
  room.onParticipantJoined = {
    participantId in
    // The event triggers for remote participants who are already in the room, just like it does for a new remote participant that joins the room.
  }
}
```

### Display a Remote Participant's Media

In order to display a remote participant's media, it helps to review how subscriptions work in the API. Review the Video API overview for a better understanding of how a `Room` is modeled, especially `Stream` and `Subscription`.

> **Key point about Subscriptions:** In order to display media from a remote stream you need to subscribe to it. Your `Room` does not automatically subscribe to a remote stream being published. It is your choice to decide whether to subscribe to a given stream.

### Subscribing to a Stream

Suppose the app you are building has two users, Alice and Bob.

First, Alice joins the `Room` and starts publishing a stream with audio from her microphone and video from her camera:

> *The app on Alice's device runs the following code…*

```swift
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

Bob wants to get Alice's stream so he can display it. To do so he needs to subscribe to Alice's stream.

> *The app on Bob's device runs the following code…*

```swift
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
  room.onSubscriptionStarted = {
    participantId, streamKey in
    // Bob needs to fetch the stream so he can display it
    let aliceStream = room.getParticipantStream(participantId: participantId, key: streamKey)

    // Alice's stream has a key of 'self' which has the audio track from her microphone and a video from her device's camera. Bob can use these tracks and display them as Alice in his app.
    let aliceCameraTrack = aliceStream.videoTrack
    let aliceMicrophoneTrack = aliceStream.audioTrack
  }
}
```

### Handling Remote Streams Already Publishing in the Room

After you connect to a Room there may be remote participants already in the `Room` who are publishing streams. To deal with that, use the `onStreamPublished` event:

```swift
room.connect { status in
  // After connecting to a room the onStreamPublished event will trigger for remote streams
  // that are already being published in the room
  room.onStreamPublished = {
          participantId, streamKey in

  }
}
```

## Disconnecting from a Room

To disconnect from a room:

```swift
room.disconnect {
  // after the room disconnects its status is .disconnected
}
```

When you disconnect from a `Room`, all `Remote Participant`s will be notified that you have left the `Room` because the `Room.onParticipantLeft` event will fire on their `Room` instance.
