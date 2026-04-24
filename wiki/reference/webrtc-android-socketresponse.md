---
title: WebRTC Android SocketResponse
summary: Data class used with communication between socket connection and TelnyxClient.
sources:
  - url: https://developers.telnyx.com/development/webrtc/android-sdk/socket/socketresponse/index
    content_hash: 4b7c2bea28bad479cfdb4fb407e4628a10f908067bb9ef847fe0868e6a73460f
updated_at: 2026-04-10T00:00:00Z
---

# WebRTC Android SocketResponse

Data class used with communication between socket connection and TelnyxClient

## SocketResponse

Data class used with communication between socket connection and TelnyxClient.

```kotlin theme={null}
data class SocketResponse<out T>(var status: SocketStatus, val data: T?, val errorMessage: String?)
```

Where SocketStatus is a Enum class:

```kotlin theme={null}
enum class SocketStatus {
ESTABLISHED,
MESSAGERECEIVED,
ERROR,
LOADING,
DISCONNECT
}
```

The SocketStatus can be one of the following

* ESTABLISHED a connection to the socket has been established

* MESSAGERECEIVED the socket has received a message

* ERROR the socket has encountered an error

* LOADING the socket is loading a connection

* DISCONNECT when the socket is disconnect


## Related Pages

- [WebRTC Android Client](../reference/webrtc-android-client.md)
- [WebRTC Android Config](../reference/webrtc-android-config.md)
- [WebRTC Android Call](../reference/webrtc-android-call.md)
- [WebRTC Android SDK Error Handling](../reference/webrtc-android-sdk-error-handling.md)
- [WebRTC Android ChangeLog](../reference/webrtc-android-changelog.md)
