---
title: Flutter Push Notifications
summary: Configure push notifications for the Telnyx Flutter Voice SDK on both Android and iOS.
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter/index
    content_hash: 51103c5b873c9edd8549d2286bc7a85d1a7695a29592c29dec1f0682eb38f0ff
updated_at: 2026-04-10T00:00:00Z
---

# Flutter Push Notifications

Configure push notifications for the Telnyx Flutter Voice SDK on both Android and iOS.

## Prerequisites

* A [Telnyx account](https://portal.telnyx.com) with a configured SIP Connection
* The Telnyx Flutter Voice SDK integrated into your application
* **Android**: A [Firebase project](https://console.firebase.google.com/) with Cloud Messaging enabled
* **iOS**: An [Apple Developer account](https://developer.apple.com/) with a VoIP push certificate

## Portal setup

Flutter apps are cross-platform, so you need credentials for each platform you target:

* **Android**: Follow the [Android portal setup](android-push-notifications.md#portal-setup) to create an Android push credential using your Firebase service account JSON.
* **iOS**: Follow the [iOS portal setup](ios-push-notifications.md#portal-setup) to create an iOS push credential using your VoIP certificate PEM files.

Attach both credentials to your SIP Connection under the **WebRTC** tab in the Telnyx Portal.

***

## App setup

### Android — Firebase Cloud Messaging

#### 1. Listen for background push notifications

Register a background message handler in your `main` method:

```dart theme={null}
@pragma('vm:entry-point')
Future<void> main() async {
    WidgetsFlutterBinding.ensureInitialized();

    if (defaultTargetPlatform == TargetPlatform.android) {
        await Firebase.initializeApp();
        FirebaseMessaging.onBackgroundMessage(
            _firebaseMessagingBackgroundHandler,
        );
        await FirebaseMessaging.instance
            .setForegroundNotificationPresentationOptions(
                alert: true,
                badge: true,
                sound: true,
            );
    }
    runApp(const MyApp());
}
```

#### 2. Handle the push notification

Process the incoming message and show a call notification using a plugin like [FlutterCallkitIncoming](https://pub.dev/packages/flutter_callkit_incoming):

```dart theme={null}
Future<void> _firebaseMessagingBackgroundHandler(
    RemoteMessage message,
) async {
    // Show incoming call notification
    CallKitParams callKitParams = CallKitParams(
        android: ...,
        ios: ...,
        extra: message.data,
    );
    await FlutterCallkitIncoming.showCallkitIncoming(callKitParams);

    // Listen for user action
    FlutterCallkitIncoming.onEvent.listen((CallEvent? event) async {
        switch (event!.event) {
            case Event.actionCallAccept:
                TelnyxClient.setPushMetaData(
                    message.data, isAnswer: true, isDecline: false,
                );
                break;
            case Event.actionCallDecline:
                TelnyxClient.setPushMetaData(
                    message.data, isAnswer: false, isDecline: true,
                );
                break;
        }
    });
}
```

#### 3. Create a high-importance notification channel (Android 8.0+)

For Android 8.0 and higher, create a dedicated notification channel so incoming call notifications display as heads-up alerts. Use the [flutter\_local\_notifications](https://pub.dev/packages/flutter_local_notifications) package to configure the channel with maximum importance.

### iOS — Apple Push Notification Service

For iOS, the Flutter SDK uses APNS through the native PushKit integration. Configure your iOS project following the standard [iOS app setup](ios-push-notifications.md#app-setup), which includes:

1. Enabling Push Notifications and Background Modes (VoIP) capabilities in Xcode.
2. Configuring PushKit to register for VoIP pushes.
3. Reporting incoming calls to CallKit (required on iOS 13+).

The Flutter SDK handles the bridge between native push events and your Dart code.

***

## Troubleshooting

### Android-specific issues

* **FCM token not received**: Ensure `Firebase.initializeApp()` is called before requesting the token and that `google-services.json` is correctly placed.
* **Notifications not showing in background**: Verify your background handler is annotated with `@pragma('vm:entry-point')` and registered via `FirebaseMessaging.onBackgroundMessage`.
* **Low-priority notifications**: Create a notification channel with `Importance.max` for incoming call alerts.

### iOS-specific issues

* **No push notifications**: Confirm the VoIP push certificate matches your Bundle ID and is uploaded to the Telnyx Portal.
* **App terminated on push**: On iOS 13+, you must report every VoIP push to CallKit or the system kills your app.
* **Environment mismatch**: Use sandbox for debug builds and production for release/TestFlight builds.

### General

* **Push works but no call invitation**: The push notification only signals that a call is incoming. Your app must reconnect to the TelnyxClient socket after receiving the push so the actual invitation can be delivered.
* **Multidevice**: A user can register up to 5 push tokens. If a 6th is added, the oldest is removed.

## Next steps

* [Push notifications overview](push-notifications-overview.md) — Multidevice support and architecture
* [Flutter SDK reference](https://developers.telnyx.com/development/webrtc/flutter-sdk) — Full SDK documentation
* [Mobile Push Credentials API](/api/webrtc/mobile-push-credentials) — Manage credentials programmatically


## Related Pages

- [Flutter Push Notification App Setup](../reference/flutter-push-notification-app-setup.md)
- [Flutter Push Notification Portal Setup](../reference/flutter-push-notification-portal-setup.md)
- [iOS Push Notifications](../runbooks/ios-push-notifications.md)
- [React Native Push Notifications](../runbooks/react-native-push-notifications.md)
- [Android Push Notifications](../runbooks/android-push-notifications.md)
