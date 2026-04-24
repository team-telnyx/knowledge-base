---
title: Flutter WebRTC SDK Message
summary: The TelnyxRTC Flutter Message represents a message received from the Telnyx Socket that the client can react to.
sources:
  - url: https://developers.telnyx.com/development/webrtc/flutter-sdk/classes/messages/telnyx-message/index
    content_hash: 5c31a31eac99d070e0e850c7761289956eb9e1d7304877cc483f059b355bbb78
updated_at: 2026-04-10T00:00:00Z
---

# Flutter WebRTC SDK Message

The TelnyxRTC Flutter Message represents a message received from the Telnyx Socket that the client can react to.

### TelnyxMessage

This class is used to represent a message received from the Telnyx Socket. It contains a `socketMethod` which is a string representing the type of message received and a `ReceivedMessage` which contains the message data.

```dart theme={null}
class TelnyxMessage {
  String socketMethod;
  ReceivedMessage message;

  TelnyxMessage({required this.socketMethod, required this.message});
}
```

### Socket Methods

The socket method can be one of the following:

```dart theme={null}
class SocketMethod {
  static const answer = 'telnyx_rtc.answer';
  static const invite = 'telnyx_rtc.invite';
  static const bye = 'telnyx_rtc.bye';
  static const modify = 'telnyx_rtc.modify';
  static const media = 'telnyx_rtc.media';
  static const info = 'telnyx_rtc.info';
  static const ringing = 'telnyx_rtc.ringing';
  static const clientReady = 'telnyx_rtc.clientReady';
  static const gatewayState = 'telnyx_rtc.gatewayState';
  static const ping = 'telnyx_rtc.ping';
  static const login = 'login';
  static const attachCall = 'telnyx_rtc.attachCalls';
  static const attach = 'telnyx_rtc.attach';
}
```

### ReceivedMessage

The received message contains the data of the message received from the Telnyx Socket. It will contain the actual message as well as the state of the Call, client and SDK.


## Related Pages

- [Flutter WebRTC SDK Socket Error Message](../reference/flutter-webrtc-sdk-socket-error-message.md)
- [Flutter WebRTC SDK Socket Message Handler](../reference/flutter-webrtc-sdk-socket-message-handler.md)
- [Flutter WebRTC SDK Socket Error Handler](../reference/flutter-webrtc-sdk-socket-error-handler.md)
