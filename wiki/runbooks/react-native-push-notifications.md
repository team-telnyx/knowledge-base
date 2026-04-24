---
title: React Native Push Notifications
summary: Configure push notifications for the Telnyx React Native Voice SDK on both Android and iOS.
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native/index
    content_hash: 07f36b306ba66a747e45fa86226178f9b43aecbd82e7442f643c0bf970db43e7
updated_at: 2026-04-10T00:00:00Z
---

# React Native Push Notifications

Configure push notifications for the Telnyx React Native Voice SDK on both Android and iOS.

## Prerequisites

* A [Telnyx account](https://portal.telnyx.com) with a configured SIP Connection
* The `@telnyx/react-voice-commons-sdk` integrated into your application
* **Android**: A [Firebase project](https://console.firebase.google.com/) with Cloud Messaging enabled
* **iOS**: An [Apple Developer account](https://developer.apple.com/) with a VoIP push certificate

## Portal setup

React Native apps are cross-platform, so you need credentials for each platform you target:

* **Android**: Follow the [Android portal setup](android-push-notifications.md#portal-setup) to create an Android push credential using your Firebase service account JSON.
* **iOS**: Follow the [iOS portal setup](ios-push-notifications.md#portal-setup) to create an iOS push credential using your VoIP certificate PEM files.

Attach both credentials to your SIP Connection under the **WebRTC** tab in the Telnyx Portal.

***

## App setup

### Install dependencies

```bash theme={null}


## Related Pages

- [iOS Push Notifications](../runbooks/ios-push-notifications.md)
- [Android Push Notifications](../runbooks/android-push-notifications.md)
- [Flutter Push Notifications](../runbooks/flutter-push-notifications.md)
- [Data Usage Notifications](../runbooks/data-usage-notifications.md)
- [iOS Push Notification Setup](../reference/ios-push-notification-setup.md)
