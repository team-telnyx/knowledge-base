---
title: WebRTC Voice SDKs - Flutter to Index
summary: A consolidated reference for the Telnyx WebRTC Voice SDKs covering shared
  concepts (client/call classes, call states, authentication, multi-client registration,
  common call-flow patterns, and pricing), platform-specific push notification setup
  for iOS, Android, Flutter, and React Native, and troubleshooting tools including
  call detail records and debug data interpretation.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/index
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native
- url: https://developers.telnyx.com/docs/voice/webrtc/sdk-commonalities
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/debug-logs
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/detail-records/index
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/interpreting-debug-data/index
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/contact-center/index
updated_at: 2026-08-05T14:08:06Z
---

# WebRTC Voice SDKs - Flutter to Index

*Part 2 of 5 — see also: [Part 1](webrtc-voice-sdks-flutter-to-index--part-1.md), [Part 3](webrtc-voice-sdks-flutter-to-index--part-3.md), [Part 4](webrtc-voice-sdks-flutter-to-index--part-4.md), [Part 5](webrtc-voice-sdks-flutter-to-index--part-5.md)*

A consolidated reference for the Telnyx WebRTC Voice SDKs covering shared concepts (client/call classes, call states, authentication, multi-client registration, common call-flow patterns, and pricing), platform-specific push notification setup for iOS, Android, Flutter, and React Native, and troubleshooting tools including call detail records and debug data interpretation.

## Push Notifications

Push notification configuration has two parts: **portal setup** (create a push credential in the Telnyx Portal and attach it to a SIP Connection) and **app setup** (integrate the push service into your application code and pass the token to the SDK on login).

| Platform | Push service | Credential type | Guide |
| --- | --- | --- | --- |
| Android | Firebase Cloud Messaging (FCM) | Android Credential (service account JSON) | [Android Push Notifications](android-push-notifications.md) |
| iOS | Apple Push Notification Service (APNS) | iOS Credential (`cert.pem` + `key.pem`) | [iOS Push Notifications](ios-push-notifications.md) |
| Flutter | FCM (Android) + APNS (iOS) | Both credentials required | [Flutter Push Notifications](flutter-push-notifications.md) |
| React Native | FCM (Android) + APNS (iOS) | Both credentials required | [React Native Push Notifications](react-native-push-notifications.md) |

### Multidevice support

A single user can register up to **5 push tokens** across iOS (APNS) and Android (FCM) devices. Each login that provides a push token registers it; if a sixth token is added, the least-recently-used token is removed. Up to five devices can therefore receive push notifications for the same incoming call simultaneously.

### iOS push setup

**Prerequisites:** a Telnyx account with a configured SIP Connection, an Apple Developer account, and the Telnyx iOS WebRTC SDK integrated.

**Portal setup:**

1. Create a VoIP Services Certificate in the Apple Developer portal (Certificates, Identifiers & Profiles → + → VoIP Services Certificate). You need an Apple Developer account, your app's Bundle ID, and a CSR from your Mac. Generate a CSR via Keychain Access → Certificate Assistant → Request a Certificate from a Certificate Authority. A single VoIP Services Certificate works for both APNS sandbox and production environments; you need a separate certificate for each Bundle ID.
2. Export `cert.pem` and `key.pem` from the installed certificate. In Keychain Access, export the certificate as a `.p12` file, then run:

```
openssl pkcs12 -in PATH_TO_YOUR_P12 -nokeys -out cert.pem -nodes -legacy
openssl pkcs12 -in PATH_TO_YOUR_P12 -nocerts -out key.pem -nodes -legacy
openssl rsa -in key.pem -out key.pem
```

3. In the Telnyx Portal, go to **API Keys → Credentials → Add → iOS Credential**, name the credential (using the Bundle ID is recommended), paste the full contents of `cert.pem` (including the `-----BEGIN/END CERTIFICATE-----` markers) and `key.pem` (including the `-----BEGIN/END RSA PRIVATE KEY-----` markers), and save.
4. Attach the credential to a SIP Connection: open the connection, select the **WebRTC** tab, choose the credential in the **iOS** section, and save.

**App setup:**

- In Xcode, add the **Push Notifications** capability and add **Background Modes** with **Voice over IP** enabled.
- Configure PushKit by setting `pushRegistry.delegate` and `pushRegistry.desiredPushTypes = Set([.voIP])`. Capture the device token in `pushRegistry(_:didUpdate:for:)` and store it for login.
- Pass the APNS device token to the SDK via `TxConfig(pushDeviceToken:)` when connecting, either with SIP credentials or a JWT.
- On a VoIP push, call `telnyxClient.processVoIPNotification(txConfig:serverConfiguration:pushMetaData:)` and report the incoming call to CallKit. On iOS 13.0 and later, every VoIP push **must** be reported to CallKit or the system will terminate the app.
- To disable push notifications for the current user, call `telnyxClient.disablePushNotifications()`. Signing back in with the same credentials re-enables them.

**Troubleshooting:**

- Verify the VoIP Services Certificate is not expired and matches the Bundle ID. Different Bundle IDs require separate certificates.
- Confirm the APNS device token is captured in `pushRegistry(_:didUpdate:for:)` and included in `TxConfig` when calling `connect()`.
- In the Telnyx Portal, verify the correct credential is selected under SIP Connection → WebRTC → iOS.
- Match the APNS environment to the build: sandbox for debug/Xcode builds, production for release/TestFlight. Set `pushEnvironment` accordingly in `TxConfig`.
- The SDK repository includes a `push-notification-tool/` (Node) for testing push delivery. Common errors: `BadDeviceToken` (invalid/expired token), `BadCertificate` (invalid/expired cert files), `BadTopic` (Bundle ID mismatch), `TopicDisallowed` (certificate lacks VoIP permissions).

### Android push setup

**Prerequisites:** a Telnyx account with a configured SIP Connection, a Firebase project with Cloud Messaging enabled, and the Telnyx Android WebRTC SDK integrated.

**Portal setup:** create an Android push credential in the Telnyx Portal using your Firebase service account JSON, then attach it to your SIP Connection under the **WebRTC** tab.

**App setup:**

- Place `google-services.json` in your project root and ensure the package name matches your app.
- Declare a Firebase messaging service in `AndroidManifest.xml` with the `com.google.firebase.MESSAGING_EVENT` intent filter.
- The SDK handles FCM token retrieval internally on Android; pass the token to the SDK when connecting.
- For Android 8.0+, create a dedicated high-importance notification channel (e.g. via `flutter_local_notifications` on Flutter) so incoming call notifications display as heads-up alerts.

**Troubleshooting:**

- FCM token not received: verify `google-services.json` is in the correct location and the package name matches your app.
- No notifications in background: ensure the Firebase messaging service is declared in the Android manifest.
- Wrong credential on SIP Connection: check Telnyx Portal → SIP Connection → WebRTC → Android.
- Low-priority notifications: create a notification channel with `Importance.max` for incoming call alerts.

### Flutter push setup

**Prerequisites:** a Telnyx account with a configured SIP Connection, the Telnyx Flutter Voice SDK integrated, a Firebase project with Cloud Messaging enabled (Android), and an Apple Developer account with a VoIP push certificate (iOS).

**Portal setup:** Flutter apps are cross-platform, so create both an Android push credential (from your Firebase service account JSON) and an iOS push credential (from your VoIP certificate PEM files), and attach both to your SIP Connection under the **WebRTC** tab.

**App setup — Android (FCM):**

1. Register a background message handler in `main`:

```
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

2. Handle the push and show a call notification using a plugin like [FlutterCallkitIncoming](https://pub.dev/packages/flutter_callkit_incoming). On accept/decline, call `TelnyxClient.setPushMetaData(message.data, isAnswer: ..., isDecline: ...)`.
3. For Android 8.0+, create a high-importance notification channel using [flutter_local_notifications](https://pub.dev/packages/flutter_local_notifications) so incoming call notifications display as heads-up alerts.

**App setup — iOS (APNS):** the Flutter SDK uses APNS through the native PushKit integration. Configure your iOS project per the standard iOS app setup: enable Push Notifications and Background Modes (VoIP) capabilities in Xcode, configure PushKit to register for VoIP pushes, and report incoming calls to CallKit (required on iOS 13+). The Flutter SDK bridges native push events to your Dart code.

**Troubleshooting:**

- FCM token not received: ensure `Firebase.initializeApp()` is called before requesting the token and that `google-services.json` is correctly placed.
- Notifications not showing in background: verify the background handler is annotated with `@pragma('vm:entry-point')` and registered via `FirebaseMessaging.onBackgroundMessage`.
- Low-priority notifications: create a notification channel with `Importance.max` for incoming call alerts.
- No push notifications on iOS: confirm the VoIP push certificate matches your Bundle ID and is uploaded to the Telnyx Portal.
- App terminated on push (iOS 13+): you must report every VoIP push to CallKit or the system kills your app.
- Environment mismatch: use sandbox for debug builds and production for release/TestFlight.
- Push works but no call invitation: the push only signals an incoming call. Your app must reconnect to the `TelnyxClient` socket after receiving the push so the actual invitation can be delivered.
- Multidevice: a user can register up to 5 push tokens; if a 6th is added, the oldest is removed.

### React Native push setup

**Prerequisites:** a Telnyx account with a configured SIP Connection, the `@telnyx/react-voice-commons-sdk` integrated, a Firebase project with Cloud Messaging enabled (Android), and an Apple Developer account with a VoIP push certificate (iOS).

**Portal setup:** create both an Android push credential (Firebase service account JSON) and an iOS push credential (VoIP certificate PEM files), and attach both to your SIP Connection under the **WebRTC** tab.

**App setup — install dependencies:**

```
# iOS VoIP push notifications
npm install react-native-voip-push-notification

# Expo notifications for Android FCM token (if using Expo)
npx expo install expo-notifications
```

**App setup — Android (FCM):**

1. Place `google-services.json` in your project root (same level as `package.json`).
2. Add the Firebase messaging service to `android/app/src/main/AndroidManifest.xml`:

```
<application>
    <service
        android:name=".AppFirebaseMessagingService"
        android:exported="false">
        <intent-filter>
            <action android:name="com.google.firebase.MESSAGING_EVENT" />
        </intent-filter>
    </service>
</application>
```

3. The SDK handles FCM token retrieval internally on Android; pass the token to the SDK when connecting:

```
import { TelnyxVoIPClient } from '@telnyx/react-voice-commons-sdk';

const client = new TelnyxVoIPClient({
    credentialConfig: {
        sipUser: 'username',
        sipPassword: 'password',
    },
});
```

**App setup — iOS (APNS):**

1. Use `react-native-voip-push-notification` to register for VoIP pushes and capture the device token via the `register` event; handle incoming pushes via the `notification` event. Call `VoipPushNotification.registerVoipToken()` to start.
2. In Xcode, add the **Push Notifications** capability and add **Background Modes** with **Voice over IP** enabled. On iOS 13.0 and later, every VoIP push must be reported to CallKit or the system will terminate the app.

**Troubleshooting:**

- FCM token not received: verify `google-services.json` is in the correct location and the package name matches your app.
- No notifications in background: ensure the Firebase messaging service is declared in the Android manifest.
- Wrong credential on SIP Connection: check Telnyx Portal → SIP Connection → WebRTC → Android.
- No push notifications on iOS: confirm the VoIP push certificate matches your Bundle ID and is uploaded to the Telnyx Portal.
- App terminated on push (iOS 13+): report every VoIP push to CallKit.
- Environment mismatch: use sandbox for debug builds and production for release/TestFlight.
- Push works but no call invitation: the push signals an incoming call; your app must reconnect to the socket after receiving the push so the SDK can receive the actual invitation.
- Multidevice: a user can register up to 5 push tokens across iOS and Android devices.

### API reference

Push credentials can also be managed programmatically via the [Mobile Push Credentials API](https://developers.telnyx.com/api/webrtc/mobile-push-credentials).
