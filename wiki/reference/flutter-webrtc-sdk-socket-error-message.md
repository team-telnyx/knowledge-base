---
title: Flutter WebRTC SDK Socket Error Message
summary: The TelnyxRTC Flutter Error represents an error received from the Telnyx Socket that the client can react and handle.
sources:
  - url: https://developers.telnyx.com/development/webrtc/flutter-sdk/classes/messages/telnyx-socket-error/index
    content_hash: fbf19530722e7592acfe35de5bbd717524e0c138abc688139c66de2513c50d31
updated_at: 2026-04-10T00:00:00Z
---

# Flutter WebRTC SDK Socket Error Message

The TelnyxRTC Flutter Error represents an error received from the Telnyx Socket that the client can react and handle.

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

- [Flutter WebRTC SDK Socket Error Handler](../reference/flutter-webrtc-sdk-socket-error-handler.md)
- [Flutter WebRTC SDK Socket Message Handler](../reference/flutter-webrtc-sdk-socket-message-handler.md)
- [Flutter WebRTC SDK Message](../reference/flutter-webrtc-sdk-message.md)
