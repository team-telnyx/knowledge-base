---
title: Telnyx Video SDKs
summary: Telnyx Video Rooms provide a real-time audio, video, and screen-share platform
  accessible via JavaScript, Android, and iOS client SDKs. This page covers the core
  concepts, prerequisites, and SDK-specific usage for building video applications
  with Telnyx.
sources:
- url: https://developers.telnyx.com/docs/video/android-client-sdk
- url: https://developers.telnyx.com/docs/video/get-started/index
- url: https://developers.telnyx.com/docs/video/ios-client-sdk
- url: https://developers.telnyx.com/docs/video/javascript-sdk/index
- url: https://developers.telnyx.com/docs/video/javascript-sdk/javascript-video-tutorial
- url: https://developers.telnyx.com/docs/video/javascript-sdk/room-events
- url: https://developers.telnyx.com/docs/voice/outbound-voice-profiles
- url: https://developers.telnyx.com/docs/voice/overview/index
updated_at: 2026-06-11T10:40:58Z
---

# Telnyx Video SDKs

*Part 3 of 4 — see also: [Part 1](telnyx-video-sdks--part-1.md), [Part 2](telnyx-video-sdks--part-2.md), [Part 4](telnyx-video-sdks--part-4.md)*

Telnyx Video Rooms provide a real-time audio, video, and screen-share platform accessible via JavaScript, Android, and iOS client SDKs. This page covers the core concepts, prerequisites, and SDK-specific usage for building video applications with Telnyx.

## Android SDK

The Android SDK makes it easy to add video calling to an Android app. The [repository](https://github.com/team-telnyx/telnyx-video-android) contains two modules: the `sdk` module and a demo `app` module.

### Installation

Add Jitpack.io to your root-level `build.gradle`:

```groovy
allprojects {
    repositories {
        ...
        maven { url 'https://jitpack.io' }
    }
}
```

Add the dependency in your app-level `build.gradle`:

```groovy
dependencies {
    implementation 'com.github.team-telnyx:telnyx-video-android:<tag>'
}
```

Replace `<tag>` with the release version. Then import the SDK:

```kotlin
import com.telnyx.video.sdk.*
```

### Permissions

Add these permissions to your AndroidManifest:

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.CAMERA"/>
<uses-permission android:name="android.permission.RECORD_AUDIO"/>
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>
```

### Connect to a Room

```kotlin
room = Room(
    context = context,
    roomId = UUID.fromString(roomId),
    roomToken = tokenInfo.token,
    externalData = ExternalData(id = 1234, username = "Android Participant"),
    enableMessages = false
)

room.connect()
```

### Publishing Streams

Use `PublishConfigHelper` with the application context, camera direction, `streamKey`, and `streamId`:

```kotlin
// Audio
publishConfigHelper = PublishConfigHelper(
    context = requireContext(),
    direction = CameraDirection.FRONT,
    streamKey = SELF_STREAM_KEY,
    streamId = SELF_STREAM_ID
)
publishConfigHelper.createAudioTrack(true, AUDIO_TRACK_KEY)
room.addStream(publishConfigHelper)
```

To add video to the same stream:

```kotlin
publishConfigHelper.setSurfaceView(selfSurfaceRenderer)
publishConfigHelper.createVideoTrack(
    CapturerConstraints.WIDTH.value,
    CapturerConstraints.HEIGHT.value,
    CapturerConstraints.FPS.value,
    true, // isTrackEnabled?
    VIDEO_TRACK_KEY
)
room.updateStream(publishConfigHelper)
```

Since the stream already exists, call `updateStream` instead of `addStream`.

### Removing Tracks and Streams

Remove a video track:

```kotlin
publishConfigHelper?.let {
    it.stopCapture()
    roomsViewModel.updateStream(it)
    selfSurface?.let { surface -> it.releaseSurfaceView(surface) }
}
```

Remove an audio track:

```kotlin
publishConfigHelper?.let {
    it.disposeAudio()
    roomsViewModel.updateStream(it)
}
```

Remove an entire stream (all tracks):

```kotlin
room.removeStream(SELF_STREAM_KEY)
```

### Subscribing to a Remote Stream

Subscribing to a video stream involves three steps:

1. **Initialize the surface** — provide the `SurfaceViewRenderer` to the SDK using `room.setParticipantSurface(participantId, surface, streamKey)` so it can initialize in the proper WebRTC EglContext.
2. **Add the surface as a sink** — call `videoTrack.addSink(surfaceViewRenderer)` and `videoTrack.setEnabled(true)` on the track from the participant's stream.
3. **Subscribe** — call `room.addSubscription(participantId, streamKey, streamConfig)` with a `StreamConfig` specifying whether to subscribe to audio, video, or both.

To remove a subscription:

```kotlin
room.removeSubscription(participantId, streamKey)
```

Properly release surfaces:

```kotlin
videoTrack.removeSink(surfaceViewRenderer)
surfaceViewRenderer.release()
```

### Observables

The Android SDK uses `MutableLiveData` observables for room state and events:

| Observable | Type | Description |
|------------|------|-------------|
| `getStateObservable()` | `MutableLiveData<State>` | Current state of the room (action, status, participants, streams, publishers, subscriptions) |
| `getParticipantsObservable()` | `MutableLiveData<MutableList<Participant>>` | List of participants present upon joining (not re-emitted on changes) |
| `getJoinedRoomObservable()` | `MutableLiveData<Event<RoomUI>>` | Fired once connected and initial participant list is retrieved |
| `getJoinedParticipant()` | `MutableLiveData<Event<Participant>>` | A remote participant joined after the client connected |
| `getLeavingParticipantId()` | `MutableLiveData<Pair<Long, String>>` | Publisher ID that left and reason (`"Left"` or `"Kicked"`) |
| `getConnectionStatus()` | `LiveData<Boolean>` | `true` when WebSocket connected to the room |
| `getParticipantStreamChanged()` | `MutableLiveData<Event<Participant>>` | Participant changed their audio/video stream status |
| `getParticipantTalking()` | `MutableLiveData<Pair<Participant, String?>>` | Participant talking status changed (stream key) |

The `Event` wrapper ensures observables are only handled once. Use `getContentIfNotHandled()` for single-consumption or `peekContent()` to read without marking as handled.

### Stream Status

Track statuses apply to audio, video, and screen share:

- `UNKNOWN` — Initial status; no information available yet
- `ENABLED` — The participant is sharing this media; you can subscribe to it
- `DISABLED` — The participant is not sharing this media; unsubscribe if previously subscribed

### WebRTC Stats

Call `room.getWebRTCStatsForStream(participantId, streamKey, callback)` to retrieve stats once. For periodic updates, use a coroutine or runnable:

```kotlin
mStatsJob = CoroutineScope(Dispatchers.Default).launch {
    while (isActive) {
        room.getWebRTCStatsForStream(participantId, streamKey) { stats ->
            // Process stats
        }
        delay(2000)
    }
}
```

Stats can be parsed into typed models:

- **Remote Video** — `RemoteVideoStreamStats` (bytesReceived, frameHeight, frameWidth, framesDecoded, framesDropped, framesPerSecond, framesReceived, packetsLost, packetsReceived, totalInterFrameDelay). Filter `RTCStatsReport` for `type == "inbound-rtp"` containing `mediaType: "video"`.
- **Local Video** — `LocalVideoStreamStats` (bytesSent, codecId, frameHeight, frameWidth, framesEncoded, framesPerSecond, framesSent, headerBytesSent, nackCount, packetsSent). Filter for `type == "outbound-rtp"` containing `mediaType: "video"`.
- **Remote Audio** — `RemoteAudioStreamStats` (audioLevel, bytesReceived, codecId, headerBytesReceived, jitter, packetsLost, packetsReceived, totalAudioEnergy, totalSamplesDuration, totalSamplesReceived). Filter for `type == "inbound-rtp"` containing `mediaType: "audio"`.
- **Local Audio** — `LocalAudioStreamStats` (bytesSent, codecId, headerBytesSent, packetsSent, retransmittedBytesSent, retransmittedPacketsSent). Filter for `type == "outbound-rtp"` containing `mediaType: "audio"`.
