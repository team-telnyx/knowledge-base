---
title: Flutter WebRTC SDK Socket Error Handler
summary: The event handler that is used as a callback function when errors are received from the Telnyx Websocket Connection.
sources:
  - url: https://developers.telnyx.com/development/webrtc/flutter-sdk/event-handlers/on-socket-error-received/index
    content_hash: 8195c7bf209850e5e077f26c3eb53462d7feb5965fb4810c37005d5a15acbfd3
updated_at: 2026-04-10T00:00:00Z
---

# Flutter WebRTC SDK Socket Error Handler

The event handler that is used as a callback function when errors are received from the Telnyx Websocket Connection.

### onSocketErrorReceived

The `onSocketErrorReceived` event handler is called when an error is received from the WebSocket connection.

```dart theme={null}
typedef OnSocketErrorReceived = void Function(TelnyxSocketError message);
```

### TelnyxSocketError

This class is used to represent an error received from the Telnyx Socket. It contains an `errorCode`
which is an integer representing the error code and an `errorMessage` which is a string representing
the error message.

```dart theme={null}
class TelnyxSocketError {
  int errorCode = 0;
  String errorMessage = '';

  TelnyxSocketError({required this.errorCode, required this.errorMessage});

  TelnyxSocketError.fromJson(Map<String, dynamic> json) {
    errorCode = json['code'] ?? 0;
    errorMessage = json['message'] ?? '';
  }
}
```

### Error Codes

The error code can be one of the following:

```dart theme={null}
class TelnyxErrorConstants {
  static const tokenError = 'Token registration error';
  static const tokenErrorCode = -32000;
  static const credentialError = 'Credential registration error';
  static const credentialErrorCode = -32001;
  static const gatewayTimeoutError = 'Gateway registration timeout';
  static const gatewayTimeoutErrorCode = -32003;
  static const gatewayFailedError = 'Gateway registration failed';
  static const gatewayFailedErrorCode = -32004;
  static const callNotFound = 'Call not found';
}
```


## Related Pages

- [Flutter WebRTC SDK Socket Message Handler](../reference/flutter-webrtc-sdk-socket-message-handler.md)
- [Flutter WebRTC SDK Socket Error Message](../reference/flutter-webrtc-sdk-socket-error-message.md)
- [WebRTC iOS SDK Error Handling](../reference/webrtc-ios-sdk-error-handling.md)
- [Flutter WebRTC SDK Message](../reference/flutter-webrtc-sdk-message.md)
- [WebRTC Flutter SDK Error Handling](../reference/webrtc-flutter-sdk-error-handling.md)
