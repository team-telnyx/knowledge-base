---
title: Getting Started with Android Client SDK
summary: The Telnyx Video Android SDK enables developers to add video calling to Android
  applications with minimal code, providing full functionality to join and interact
  with Telnyx Rooms. This guide covers installation, room connection, stream publishing
  and subscription, observables for UI updates, and WebRTC stats retrieval.
sources:
- url: https://developers.telnyx.com/docs/video/android-client-sdk
updated_at: 2026-08-05T14:02:07Z
---

# Getting Started with Android Client SDK

*Part 1 of 3 — see also: [Part 2](getting-started-with-android-client-sdk--part-2.md), [Part 3](getting-started-with-android-client-sdk--part-3.md)*

The Telnyx Video Android SDK enables developers to add video calling to Android applications with minimal code, providing full functionality to join and interact with Telnyx Rooms. This guide covers installation, room connection, stream publishing and subscription, observables for UI updates, and WebRTC stats retrieval.

## Overview

The Telnyx Video Android SDK is simple to use and makes it easy to get started with video calling. With this SDK, you can add video calling to your app with just a few lines of code. It provides all the functionality needed to join and interact with a Telnyx Room from an Android application.

The SDK source repository is available at [Android SDK](https://github.com/team-telnyx/telnyx-video-android).

## Project structure

- **SDK project**: `sdk` module, containing all Telnyx SDK components as well as tests.
- **Demo application**: `app` module, containing a sample demo application utilizing the `sdk` module.

## Adding the SDK to your Android client application

Add Jitpack.io as a repository within your root level build file:

```groovy
allprojects {
    repositories {
        ...
        maven { url 'https://jitpack.io' }
    }
}
```

Add the dependency within the app level build file:

```groovy
dependencies {
    implementation 'com.github.team-telnyx:telnyx-video-android:<tag>'
}
```

Replace `<tag>` with the release version. Then, import the TelnyxVideo SDK into your application code at the top of the class:

```kotlin
import com.telnyx.video.sdk.*
```

The `*` symbol imports the whole SDK, making it available for use within that class.

Remember to add and handle the `INTERNET`, `RECORD_AUDIO`, and `ACCESS_NETWORK_STATE` permissions in order to properly use the SDK:

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.CAMERA"/>
<uses-permission android:name="android.permission.RECORD_AUDIO"/>
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>
```

## Before connecting to a Room

### Get an API Key

You'll need an API key associated with your Mission Control Portal account under **API Keys**. See the [API Keys documentation](https://developers.telnyx.com/docs/development/api-fundamentals/create-api-keys) for instructions. An API key is your credential to access the API and allows you to:

- Authenticate to the REST API
- Manage your access tokens

### Create a Room to join (if it doesn't exist)

In order to join a room you must create it, if it doesn't already exist. See the [Room REST API](https://developers.telnyx.com/docs/api-reference/rooms/view-a-list-of-rooms) to create one. Additional resources on other endpoints are available to perform basic operations on a `Room`.

### Generate a client token to join a room

In order to join a room you must have a client token for that `Room`. The `client token` is short lived and you can refresh it using the `refresh token` provided with it when you request a `client token`. See the [Create Client Token documentation](https://developers.telnyx.com/docs/api-reference/rooms-client-tokens/create-client-token-to-join-a-room) to learn how to create a `client token`.

Once you have completed these steps, you are ready to connect to a video room that you previously created using the REST API.

## Connect to Room

To connect, provide a **participantName** that identifies your user in the room. You'll also need an instance of `ExternalData` containing a `username` of type `String` and an `Integer` `id`, plus your Android application's context in `context`:

```kotlin
room = Room(
    context = context,
    roomId = UUID.fromString(roomId),
    roomToken = tokenInfo.token,
    externalData = ExternalData(id = 1234, username = "Android Participant"),
    enableMessages = false
)
...
room.connect()
```

## Publish video/audio stream

To publish a video or audio stream, create an instance of `PublishConfigHelper` with the application context, camera direction, `streamKey` (unique for each stream published), and `streamId` (unique for each stream published):

```kotlin
// AUDIO
publishConfigHelper = PublishConfigHelper(
    context = requireContext(),
    direction = CameraDirection.FRONT,
    streamKey = SELF_STREAM_KEY, // a key to identify this stream i.e: "self"
    streamId = SELF_STREAM_ID    // RANDOM id to this stream i.e: "qlkj323kj423"
)
publishConfigHelper.createAudioTrack(
    true, // isTrackEnabled?
    AUDIO_TRACK_KEY // i.e: "myMic", "002"
)
...
room.addStream(publishConfigHelper) // This stream is new. addStream() is called.
```

New streams can be created via the `PublishConfigHelper` class for both audio and video. They can be created together or added later independently.

```kotlin
// VIDEO
// NOTE: in this case, video is published in the same stream as above
publishConfigHelper.setSurfaceView(selfSurfaceRenderer) // Provide SurfaceRenderer

publishConfigHelper.createVideoTrack(
    CapturerConstraints.WIDTH.value,  // i.e: 1280
    CapturerConstraints.HEIGHT.value, // i.e: 720
    CapturerConstraints.FPS.value,    // i.e: 30 (fps)
    true,                              // isTrackEnabled?
    VIDEO_TRACK_KEY                    // i.e: "cameraFeed", "001"
)
...
room.updateStream(publishConfigHelper) // Stream already created, therefore updateStream is called.
```

Since the stream is already created, it is only necessary to add the video track to `PublishConfigHelper` and "update" the stream.

## Remove video/audio track

To remove a video or audio track, modify `publishConfigHelper` to remove the unwanted track:

```kotlin
// Considering publishConfigHelper is the same instance as above
publishConfigHelper?.let {
    it.stopCapture()   // In case of video, we "stop the capture", update the stream, and release the surface
    roomsViewModel.updateStream(it)
    selfSurface?.let { surface -> it.releaseSurfaceView(surface) }
}
```

```java
publishConfigHelper?.let {
    it.disposeAudio()    // In case of audio, we "dispose" audio and update the stream.
    roomsViewModel.updateStream(it)
}
```

## Remove stream

By removing the stream, all tracks added to it are removed:

```kotlin
room.removeStream(SELF_STREAM_KEY) // a key to identify this stream i.e: "self"
```
