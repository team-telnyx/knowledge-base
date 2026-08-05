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

*Part 3 of 3 — see also: [Part 1](getting-started-with-android-client-sdk--part-1.md), [Part 2](getting-started-with-android-client-sdk--part-2.md)*

The Telnyx Video Android SDK enables developers to add video calling to Android applications with minimal code, providing full functionality to join and interact with Telnyx Rooms. This guide covers installation, room connection, stream publishing and subscription, observables for UI updates, and WebRTC stats retrieval.

## Subscribe to a video stream

In order to subscribe to a **video stream**, three actions need to be performed:

```kotlin
StreamStatus.ENABLED -> {
    // This notifies the WebRTC connection we're ready to receive stream information
    participantTileListener.subscribeTileToStream(model.participantId, "self")

    itemView.participant_tile_surface.visibility = View.VISIBLE
    itemView.participant_tile_place_holder.visibility = View.GONE

    // This ensures surfaces are initialized in an EglContext provided inside WebRTC connection
    participantTileListener.notifyTileSurfaceId(
        itemView.participant_tile_surface,
        model.participantId,
        "self"
    )

    model.streams.find { it.streamKey == "self" }?.videoTrack?.let {
        if (viewHolderMap[holder] != it) {  // NOTE: keep a map of surfaces to release

            // Updates only if previous register differs from what we need
            viewHolderMap[holder]?.removeSink(holder.itemView.participant_tile_surface)
            holder.itemView.participant_tile_surface.release()
            viewHolderMap[holder] = it

            it.addSink(itemView.participant_tile_surface)
            it.setEnabled(true)
        }
    }
}
```

1. Provide the SDK with the same instance of `SurfaceViewRenderer` you want to *init*:

```kotlin
room.setParticipantSurface(
    participantId: String,
    surface: SurfaceViewRenderer,
    streamKey: String // Stream key to identify the webrtc connection to init this surface
)
```

This uses the proper **WebRTC Connection** to provide an `EglContext` for the surface to be *init*.

2. Use method `addSink()` to add a `SurfaceViewRenderer` instance to the `videoTrack` provided for a participant, and set that track to enable: `videoTrack?.setEnabled(true)`.

3. Subscribe to the stream a participant is providing:

```kotlin
participantTileListener.subscribeTileToStream(model.participantId, "self")

// Eventually calls:
room.addSubscription(
    participantId: String,
    streamKey: String,
    streamConfig: StreamConfig,
)
```

- `participantId` is the participant id that uniquely identifies a single participant in the room.
- `streamKey` e.g.: "SharingSubscriptions", "CameraSubscriptions".
- `streamConfig` whether you want to subscribe to audio/video or both. By default, both are attempted.

## Remove subscription to a video stream

To remove a subscription, issue:

```kotlin
room.removeSubscription(participantId: String, streamKey: String)
```

A good practice when handling surfaces is to make sure you remove the surface properly from the rendering context before eliminating or removing the surface from the UI:

```kotlin
// Here, order is important
videoTrack.removeSink(surfaceViewRenderer)
surfaceViewRenderer.release()
```

## Participant Talking Observable

```kotlin
room.getParticipantTalking()
// MutableLiveData<Pair<Participant, String?>>
```

You receive the participant that has updated its talking status, and the stream key. This information is also modified in the participants list:

```kotlin
data class Participant(
    ...
    var isTalking: String?, // Can either be "talking" or "stopped-talking"
    ...
) : Serializable
```

## Stats

The method `getWebRTCStatsForStream()` retrieves WebRTC stats. This request brings stats one time only, so if you want to keep receiving stats, you need to use a runnable or coroutine to recursively request them:

```kotlin
mStatsjob = CoroutineScope(Dispatchers.Default).launch {
    while (isActive) {
        room.getWebRTCStatsForStream(participantId, streamKey, callback)
        delay(2000)
    }
}
```

You must provide `participantId`, `streamKey` (the key that identifies the stream you need stats from), and `callback` (an `RTCStatsCollectorCallback` provided to the WebRTC peer connection to retrieve the stats). In Kotlin, the method call looks like:

```kotlin
room.getWebRTCStatsForStream(participantId, streamKey) { stats ->
    ...
    ...
}
```

You can later parse the information retrieved to obtain the specific information you need. The sample app demonstrates the models used for audio and video, both local and remote.

### Remote Video stats

WEBRTC's `RTCStatsReport` can be parsed and mapped to `RemoteVideoStreamStats`:

```kotlin
data class RemoteVideoStreamStats(
    val bytesReceived: Int,
    val frameHeight: Int,
    val frameWidth: Int,
    val framesDecoded: Int,
    val framesDropped: Int,
    val framesPerSecond: Double,
    val framesReceived: Int,
    val packetsLost: Int,
    val packetsReceived: Int,
    val totalInterFrameDelay: Double
) : StreamStats()
```

```kotlin
stats.statsMap.values.filter { it.type == "inbound-rtp" }
    .findLast { it.toString().contains("mediaType: \"video\"") }
    ?.let { rtcVideoStats ->
        val videoStreamStats =
            gson.fromJson(
                rtcVideoStats.toString(),
                RemoteVideoStreamStats::class.java
            )
        videoStreamStats?.let {
            Timber.tag("RoomFragment")
                .d("ParticipantID: $participantId video STATS: $it")
            // Proceed to use stats
        }
    }
```

### Local Video stats

WEBRTC's `RTCStatsReport` can be parsed and mapped to `LocalVideoStreamStats`:

```kotlin
data class LocalVideoStreamStats(
    val bytesSent: Int,
    val codecId: String,
    val frameHeight: Int,
    val frameWidth: Int,
    val framesEncoded: Int,
    val framesPerSecond: Double,
    val framesSent: Int,
    val headerBytesSent: Int,
    val nackCount: Int,
    val packetsSent: Int,
) : StreamStats()
```

```kotlin
stats.statsMap.values.filter { it.type == "outbound-rtp" }
    .findLast { it.toString().contains("mediaType: \"video\"") }
    ?.let { rtcVideoStats ->
        val videoStreamStats =
            gson.fromJson(
                rtcVideoStats.toString(),
                LocalVideoStreamStats::class.java
            )
        videoStreamStats?.let {
            Timber.tag("RoomFragment")
                .d("SelfParticipant video STATS: $it")
            // Proceed to use stats
        }
    }
```

### Remote audio stats

WEBRTC's `RTCStatsReport` can be parsed and mapped to `RemoteAudioStreamStats`:

```kotlin
data class RemoteAudioStreamStats(
    val audioLevel: Double,
    val bytesReceived: Int,
    val codecId: String,
    val headerBytesReceived: Int,
    val jitter: Double,
    val packetsLost: Int,
    val packetsReceived: Int,
    val totalAudioEnergy: Double,
    val totalSamplesDuration: Double,
    val totalSamplesReceived: Int,
) : StreamStats()
```

```kotlin
stats.statsMap.values.filter { it.type == "inbound-rtp" }
    .findLast { it.toString().contains("mediaType: \"audio\"") }
    ?.let { rtcStats ->
        val audioStreamStats =
            gson.fromJson(
                rtcStats.toString(),
                RemoteAudioStreamStats::class.java
            )
        audioStreamStats?.let {
            // Proceed to use stats
        }
    }
```

### Local audio stats

WEBRTC's `RTCStatsReport` can be parsed and mapped to `LocalAudioStreamStats`:

```kotlin
data class LocalAudioStreamStats(
    val bytesSent: Int,
    val codecId: String,
    val headerBytesSent: Int,
    val packetsSent: Int,
    val retransmittedBytesSent: Int,
    val retransmittedPacketsSent: Int,
) : StreamStats()
```

```kotlin
stats.statsMap.values.filter { it.type == "outbound-rtp" }
    .findLast { it.toString().contains("mediaType: \"audio\"") }
    ?.let { rtcStats ->
        val audioStreamStats =
            gson.fromJson(
                rtcStats.toString(),
                LocalAudioStreamStats::class.java
            )
        audioStreamStats?.let {
            // Proceed to use stats
        }
    }
```
