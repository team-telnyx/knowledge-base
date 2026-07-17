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

*Part 4 of 5 — see also: [Part 1](telnyx-video-sdks--part-1.md), [Part 2](telnyx-video-sdks--part-2.md), [Part 3](telnyx-video-sdks--part-3.md), [Part 5](telnyx-video-sdks--part-5.md)*

Telnyx Video Rooms is a platform for adding real-time audio and video to Web, Android, and iOS applications, built on REST APIs and Client SDKs. This page covers the core concepts (Rooms, Participants, Streams, Subscriptions), server-side prerequisites (API key, Room creation, client token), and detailed usage of the JavaScript, iOS, and Android SDKs including installation, connecting, publishing and subscribing to streams, room events, and WebRTC stats.

## Android SDK

The Telnyx Video Android SDK is simple to use and makes it easy to get started with video calling. With this SDK, you can easily add video calling to your app with just a few lines of code. It provides all the functionality you need to join and interact with a Telnyx Room from an Android application.

The SDK repo is at [team-telnyx/telnyx-video-android](https://github.com/team-telnyx/telnyx-video-android).

### Project structure

- **SDK project:** `sdk` module, containing all Telnyx SDK components as well as tests.
- **Demo application:** `app` module, containing a sample demo application utilizing the `sdk` module.

### Adding the SDK to your Android client application

Add Jitpack.io as a repository within your root level build file:

```
allprojects {
    repositories {
        ...
        maven { url 'https://jitpack.io' }
    }
}
```

Add the dependency within the app level build file:

```
dependencies {
    implementation 'com.github.team-telnyx:telnyx-video-android:<tag>'
}
```

`<tag>` should be replaced with the release version. Then, import the TelnyxVideo SDK into your application code at the top of the class:

```
import com.telnyx.video.sdk.*
```

The `*` symbol will import the whole SDK which will then be available for use within that class.

Remember to add and handle `INTERNET`, `RECORD_AUDIO`, and `ACCESS_NETWORK_STATE` permissions in order to properly use the SDK:

```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.CAMERA"/>
<uses-permission android:name="android.permission.RECORD_AUDIO"/>
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>
```

### Connect to Room

To connect, you'll need to provide a `participantName` that will identify your user in that room. You'll also need to provide an instance of `ExternalData` that will contain a `username` of type String and an Integer `id`. You will also provide your Android application's context in `context`:

```
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

### Publish video/audio stream

To publish a video or audio stream, you need an instance of `PublishConfigHelper` with the application context, camera direction, `streamKey` (unique for each stream published), and `streamId` (unique for each stream published):

```
// AUDIO
publishConfigHelper =
        PublishConfigHelper(
            context = requireContext(),
            direction = CameraDirection.FRONT,
            streamKey = SELF_STREAM_KEY, // a key to identify this stream i.e: "self"
            streamId = SELF_STREAM_ID // RANDOM id to this stream i.e: "qlkj323kj423"
        )
    publishConfigHelper.createAudioTrack(true, // isTrackEnabled?
                                        AUDIO_TRACK_KEY // i.e: "myMic", "002"
                                        )
...
room.addStream(publishConfigHelper) // This stream is new. addStream() is called.
```

New streams can be created via the `PublishConfigHelper` class for both audio and video. They can be created together or added later independently:

```
// VIDEO
// NOTE: in this case, video is published in the same stream as above
publishConfigHelper.setSurfaceView(selfSurfaceRenderer) // Provide SurfaceRenderer

publishConfigHelper.createVideoTrack(
            CapturerConstraints.WIDTH.value,  // i.e: 1280
            CapturerConstraints.HEIGHT.value, // i.e: 720
            CapturerConstraints.FPS.value,    // i.e: 30 (fps)
            true, // isTrackEnabled?
            VIDEO_TRACK_KEY // i.e: "cameraFeed", "001"
        )
...
room.updateStream(publishConfigHelper) // Stream already created, therefore updateStream is called.
```

Since the stream is already created, it is only necessary to add the video track to `PublishConfigHelper` and "update" the stream.

### Remove video/audio track

To remove a video or audio track, `publishConfigHelper` has to be modified in order to remove the unwanted track:

```
// Considering publishConfigHelper is the same instance as above
publishConfigHelper?.let {
            it.stopCapture()   // In case of video, we "stop the capture", update the stream, and release the surface
            roomsViewModel.updateStream(it)
            selfSurface?.let { surface -> it.releaseSurfaceView(surface) }
        }
...
publishConfigHelper?.let {
            it.disposeAudio()    // In case of audio, we "dispose" audio and update the stream.
            roomsViewModel.updateStream(it)
        }
```

### Remove stream

By removing the stream, you will remove all tracks added to it:

```
room.removeStream(SELF_STREAM_KEY) // a key to identify this stream i.e: "self"
```

### Video/Audio Observables

The Telnyx Video SDK for Android works with mutable live data, and all the information you need to build your UI is provided through **observables** that contain the most up-to-date information of the state of the room, such as current participant list, talking events, stream information, participants added, participants leaving, etc.

**State Observable.** `room.getStateObservable()` returns a `MutableLiveData<State>`. This observable provides the current state of a room at any given moment. The `State` object contains:

```
data class State(
    val action: String,
    val status: String,
    val participants: List<Participant>,
    val streams: HashMap<Long, Stream>,
    val publishers: List<Publisher>,
    val subscriptions: List<Subscription>
)
```

- `action` — the cause of the latest change of State:

```
enum class StateAction(val action: String) {
    INITIALIZING_ROOM("initializing room"),
    STATUS_CHANGED("status changed"),
    ADD_PARTICIPANT("add participant"),
    REMOVE_PARTICIPANT("remove participant"),
    ADD_STREAM("add stream"),
    REMOVE_STREAM("remove stream"),
    ADD_SUBSCRIPTION("add subscription"),
    UPDATE_SUBSCRIPTION("update subscription"),
    REMOVE_SUBSCRIPTION("remove subscription"),
    PUBLISH("publish"),
    UNPUBLISH("unpublish"),
    UPDATE_PUBLISHED_STREAM("update published stream"),
    AUDIO_ACTIVITY("audio activity")
}
```

- `status` — the status of the Room session when that action happened:

```
enum class Status(val status: String) {
    INITIALIZED("initialized"),
    CONNECTING("connecting"),
    CONNECTED("connected"),
    DISCONNECTING("disconnecting"),
    DISCONNECTED("disconnected")
}
```

- `participants` — the list of participants present in a room. A `Participant` is a UI representation, in variables, for an attendee to the room session:

```
data class Participant(
    var id: Long,
    val participantId: String,
    var externalUsername: String? = null,
    val isSelf: Boolean,
    var streams: MutableList<ParticipantStream> = mutableListOf(),
    var isTalking: String?,
    var isAudioCensored: Boolean? = false,
    var audioBridgeId: Long? = null,
    var canReceiveMessages: Boolean = false
) : Serializable

data class ParticipantStream(
    val publishingId: Long? = null,
    var streamKey: String? = null,
    var audioEnabled: StreamStatus = StreamStatus.UNKNOWN,
    var videoEnabled: StreamStatus = StreamStatus.UNKNOWN,
    var audioTrack: AudioTrack? = null,
    var videoTrack: VideoTrack? = null
)

enum class StreamStatus(val request: String) {
    UNKNOWN("unknown"),
    ENABLED("enabled"),
    DISABLED("disabled")
}
```

- `streams` — a `HashMap<Long, Stream>` containing a track of the currently available streams and the id of the publisher streaming them. A stream contains tracks for video, audio, or both:

```
data class Stream(
    val id: String,
    val key: String,
    val participantId: String,
    val origin: String,
    var isAudioEnabled: Boolean? = null,
    var isVideoEnabled: Boolean? = null,
    var isAudioCensored: Boolean? = null,
    var isVideoCensored: Boolean? = null
)
```

- `publishers` — tracks all publishers in the room. A `Publisher` is an instance of an attendee or participant sharing some stream content in the room. A single Participant sharing multiple streams can be linked to multiple Publisher ids:

```
data class Publisher(
    val audio_codec: String?,
    val video_codec: String?,
    val display: String, // see DisplayParameters.kt
    val id: Long,
    val talking: Boolean,
    val audio_moderated: Boolean? // aka Censored
)

data class DisplayParameters(
    val participantId: String,
    val telephonyEngineParticipant: Boolean? = null,
    val external: String? = null,
    val stream: StreamData? = null,
    val canReceiveMessages: Boolean? = null
)
```

- `subscriptions` — each time a publisher starts streaming information, you have the option of subscribing/unsubscribing to/from it. This list tracks all the subscriptions:

```
data class Subscription(
    var publisherId: Long,
    var status: SubscriptionStatus
)

enum class SubscriptionStatus(val status: String) {
    NEVER_REQUESTED("never_requested"),
    PENDING("pending"),
    STARTED("started"),
    PAUSED("paused")
}
```

### Event observables

Some observables will have a `MutableLiveData` of `Event`. `Event` is a wrapper of `LiveData` that ensures you only handle an observable once, no matter how many times you're set to observe it. If the contents have already been handled, you won't get that content again, unless you `peekContent()` instead.

```
open class Event<out T>(private val content: T) {
    var hasBeenHandled = false
        private set

    fun getContentIfNotHandled(): T? {
        return if (hasBeenHandled) {
            null
        } else {
            hasBeenHandled = true
            content
        }
    }

    fun peekContent(): T = content
}
```

**Participants Observable.** `room.getParticipantsObservable()` returns a `MutableLiveData<MutableList<Participant>>`. This mutable list is received as soon as you join a Room session and contains a list of the participants already present in the room, including yourself. The SDK will keep this list updated but won't post the changes, so this observer won't be fired again.

```
roomsViewModel.getParticipants().observe(viewLifecycleOwner) { participants ->
    participants.let { participantList ->
        participantAdapter.setData(participantList)
        if (participantList.size > 0){
            selfParticipantId = participantList[0].participantId
            selfParticipantHandleId = participantList[0].id
        }
    }
}
```

**Joined Room Observable.** `room.getJoinedRoomObservable()` returns a `MutableLiveData<Event<RoomUI>>`. This fires an event as soon as you have connected to a room and retrieved an initial list of participants. It is useful when you want to update UI as soon as you have joined the room successfully. This is different from `Status.CONNECTED`, which is issued when you have successfully joined your plugins to handle session audio.

**Joined Participant Observable.** `room.getJoinedParticipant()` returns a `MutableLiveData<Event<Participant>>`. You receive the participant that has joined the room after the client has already joined:

```
roomsViewModel.getJoinedParticipant().observe(viewLifecycleOwner) { participantJoined ->
    participantJoined?.let { joinedParticipantEvent ->
        joinedParticipantEvent.getContentIfNotHandled()?.let {
            participantsAdapter.addParticipant(it)
        }
    }
}
```

**Leaving participant id Observable.** `room.getLeavingParticipantId()` returns a `MutableLiveData<Pair<Long, String>>`. You receive the publisherId that has left the room, and a reason for its exit (`"Left"` or `"Kicked"`):

```
roomsViewModel.getLeavingParticipantId()
    .observe(viewLifecycleOwner) { participantLeavingId ->
        participantLeavingId?.let { (id, reason) ->
            participantAdapter.removeParticipant(id)
            if (id == selfParticipantHandleId && reason == "kicked") {
                // It's ourselves, remove from the room.
                goBack(wasKicked = true)
                Toast.makeText(requireContext(), "You were kicked!", Toast.LENGTH_LONG).show()
            }
        }
    }
}
```

**Connected to room Observable.** `room.getConnectionStatus()` returns a `LiveData<Boolean>`. Receives `true` when the WebSocket has been opened and the room is connected:

```
roomsViewModel.connectedToRoomObservable().observe(this.viewLifecycleOwner) {
    it?.let { isConnected ->
        if (isConnected) {
            buttonCreateRoom.isEnabled = true
        }
    }
}
```

**Participant stream changed Observable.** `room.getParticipantStreamChanged()` returns a `MutableLiveData<Event<Participant>>`. You receive an event with the participant that has recently changed its video and/or audio stream status. The mutable list of participants will also be updated with this change, but here the specific individual is received.

### Stream status

```
enum class StreamStatus(val request: String) {
    UNKNOWN("unknown"),
    ENABLED("enabled"),
    DISABLED("disabled")
}
```

These statuses apply for audio, video, and shared screen:

- `UNKNOWN` — initial status. We don't have information on whether this participant is sharing audio/video/screen.
- `ENABLED` — the participant is sharing audio/video/screen and we can subscribe to a stream for it.
- `DISABLED` — the participant is not sharing audio/video/screen. If we were subscribed to that participant's audio/video/screen we can unsubscribe from it.

### Subscribe to a video stream

In order to subscribe to a video stream, three actions need to be performed:

1. Provide the SDK with the same instance of `SurfaceViewRenderer` you want to init:

```
room.setParticipantSurface(
    participantId: String,
    surface: SurfaceViewRenderer,
    streamKey: String // Stream key to identify the webrtc connection to init this surface
)
```

This will use the proper WebRTC Connection to provide an `EglContext` for the surface to be init.

2. Use `addSink()` to add a `SurfaceViewRenderer` instance to the `videoTrack` provided for a Participant, and set that track to enable: `videoTrack?.setEnabled(true)`.

3. Subscribe to the stream a participant is providing:

```
participantTileListener.subscribeTileToStream(model.participantId, "self")

// Eventually calls:
room.addSubscription(
    participantId: String,
    streamKey: String,
    streamConfig: StreamConfig,
)
```

- `participantId` — the participant id that uniquely identifies a single participant in the room
- `streamKey` — e.g. `"SharingSubscriptions"`, `"CameraSubscriptions"`
- `streamConfig` — whether you want to subscribe to audio/video or both. By default we will attempt both.

### Remove subscription to a video stream

To remove a subscription:

```
room.removeSubscription(participantId: String, streamKey: String)
```

A good practice when handling surfaces is to make sure you remove this surface properly from the rendering context before eliminating or removing the surface from the UI:

```
// Here, order is important
videoTrack.removeSink(surfaceViewRenderer)
surfaceViewRenderer.release()
```

### Participant Talking Observable

`room.getParticipantTalking()` returns a `MutableLiveData<Pair<Participant, String?>>`. You receive the participant that has updated its talking status, and the stream key. This information is also modified in the Participants list. `isTalking` can be either `"talking"` or `"stopped-talking"`.

### Stats

The SDK provides `getWebRTCStatsForStream()` to retrieve WebRTC stats. This request brings stats one time only, so if you want to keep receiving stats, you will need to use a runnable or coroutine to recursively request for them:

```
mStatsjob = CoroutineScope(Dispatchers.Default).launch {
        while (isActive) {
            room.getWebRTCStatsForStream(participantId, streamKey, callback)
            delay(2000)
    }
```

You must provide `participantId`, `streamKey` (the key that identifies the stream you need the stats from), and `callback` (an `RTCStatsCollectorCallback` you provide to the WebRTC peer connection in order to retrieve the stats). In Kotlin, the method call looks like:

```
room.getWebRTCStatsForStream(participantId, streamKey) { stats ->
    ...
    ...
}
```

You can later parse the information retrieved to obtain the specific information you go after. The sample app demonstrates models used for audio and video, both local and remote.

**Remote Video stats.** WebRTC's `RTCStatsReport` can be parsed and mapped to `RemoteVideoStreamStats`:

```
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

```
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

**Local Video stats.** WebRTC's `RTCStatsReport` can be parsed and mapped to `LocalVideoStreamStats`:

```
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

```
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

**Remote audio stats.** WebRTC's `RTCStatsReport` can be parsed and mapped to `RemoteAudioStreamStats`:

```
data class RemoteAudioStreamStats(
    val audioLevel: Double,
    val bytesReceived: Int,
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

```
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

**Local audio stats.** WebRTC's `RTCStatsReport` can be parsed and mapped to `LocalAudioStreamStats`:

```
data class LocalAudioStreamStats(
    val bytesSent: Int,
    val codecId: String,
    val headerBytesSent: Int,
    val packetsSent: Int,
    val retransmittedBytesSent: Int,
    val retransmittedPacketsSent: Int,
) : StreamStats()
```

```
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
