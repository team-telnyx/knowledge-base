---
title: WebRTC Flutter Client Push Notifications Configuration
summary: This class contains all the properties related to Push Notifications.
sources:
  - url: https://developers.telnyx.com/development/webrtc/flutter-sdk/method-objects/push-metadata/index
    content_hash: eb84fef9759c9c4e0d76d6c64ad098c7e4a2c327a3bb15151011401391746434
updated_at: 2026-04-10T00:00:00Z
---

# WebRTC Flutter Client Push Notifications Configuration

This class contains all the properties related to Push Notifications

### PushMetaData

This class is used to represent the metadata received from a push notification. It contains a `callerName`, `callerNumber`, `callId`, `voiceSdkId`, `isAnswer` and `isDecline` which are strings representing the metadata received from the push notification.

the `isAnswer` and `isDecline` are boolean values representing the state of the call.

the `callerName`, `callerNumber`, `callId`, `voiceSdkId` are strings representing information about the caller and SDK.

```dart theme={null}
class PushMetaData {
  PushMetaData({
    this.callerName,
    this.callerNumber,
    this.callId,
    this.voiceSdkId,
  });

  String? callerName;
  String? callerNumber;
  String? callId;
  String? voiceSdkId;
  bool? isAnswer;
  bool? isDecline;

  PushMetaData.fromJson(Map<dynamic, dynamic> json) {
    callerName = json['caller_name'];
    callerNumber = json['caller_number'];
    callId = json['call_id'];
    voiceSdkId = json['voice_sdk_id'];
    isAnswer = json['isAnswer'];
    isDecline = json['isDecline'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = <String, dynamic>{};
    data['caller_name'] = callerName;
    data['caller_number'] = callerNumber;
    data['call_id'] = callId;
    data['voice_sdk_id'] = voiceSdkId;
    data['isAnswer'] = isAnswer;
    data['isDecline'] = isDecline;
    return data;
  }
}
```


## Related Pages

- [WebRTC Flutter Client Configuration](../reference/webrtc-flutter-client-configuration.md)
- [Flutter Push Notifications](../runbooks/flutter-push-notifications.md)
- [Flutter Push Notification App Setup](../reference/flutter-push-notification-app-setup.md)
