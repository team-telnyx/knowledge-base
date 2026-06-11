---
title: Telnyx WebRTC Voice SDKs
summary: Comprehensive guide to the Telnyx WebRTC Voice SDKs covering architecture,
  authentication, push notifications across all platforms, call states, dialing, use
  cases, debugging, and costs.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/flutter
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/index
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/ios
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/react-native
- url: https://developers.telnyx.com/docs/voice/webrtc/sdk-commonalities
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/debug-logs
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/detail-records/index
- url: https://developers.telnyx.com/docs/voice/webrtc/troubleshooting/interpreting-debug-data/index
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/contact-center/index
- url: https://developers.telnyx.com/docs/voice/webrtc/use-cases/outbound-dialer
updated_at: 2026-06-11T10:49:57Z
---

# Telnyx WebRTC Voice SDKs

*Part 2 of 4 — see also: [Part 1](telnyx-webrtc-voice-sdks--part-1.md), [Part 3](telnyx-webrtc-voice-sdks--part-3.md), [Part 4](telnyx-webrtc-voice-sdks--part-4.md)*

Comprehensive guide to the Telnyx WebRTC Voice SDKs covering architecture, authentication, push notifications across all platforms, call states, dialing, use cases, debugging, and costs.

## Push Notifications

### How Push Notifications Work

When a client connects to the Telnyx WebRTC platform, it maintains a WebSocket connection that receives incoming call invitations in real time. If the app moves to the background or the device terminates it, the socket closes and calls can no longer reach the device.

Push notifications bridge this gap. During login the SDK registers a platform-specific push token (FCM for Android, APNS for iOS) with Telnyx. When an incoming call targets that user, Telnyx sends a push notification through the appropriate service. The device wakes the app, which reconnects to the socket and receives the actual call invitation.

```
Caller ──▶ Telnyx Platform ──▶ FCM / APNS ──▶ Device
                                                 │
                                          App wakes up
                                                 │
                                     Reconnects WebSocket
                                                 │
                                   Receives call invitation
```

### Multidevice Support

A single user can register up to **5 push tokens** across iOS (APNS) and Android (FCM) devices. Each login that provides a push token registers it with Telnyx. If a sixth token is added, the least-recently-used token is removed. This means up to five devices can receive push notifications for the same incoming call simultaneously.

### Portal Setup

Push notification configuration has two parts: creating a push credential in the Telnyx Portal and attaching it to a SIP Connection, then integrating the push service in your app code.

#### Android Credential (Firebase Cloud Messaging)

1. Go to the [Firebase Console](https://console.firebase.google.com/) and open your project.
2. Navigate to **Project Overview → Project Settings → Service Accounts**.
3. Select **Generate New Private Key** to download a service account JSON file. The FCM HTTP v1 API uses this service account JSON key, not the legacy server key.
4. In the [Telnyx Portal](https://portal.telnyx.com), navigate to **API Keys → Credentials** tab, click **Add → Android Credential**.
5. Enter a credential name and paste the full contents of the service account JSON file into the **Project Account JSON** field.
6. Click **Add Push Credential** to save.
7. Navigate to **SIP Connections**, open your connection, select the **WebRTC** tab, and in the **Android** section select the push credential you created. Save the SIP Connection.

#### iOS Credential (Apple Push Notification Service)

First, create a VoIP push certificate:

1. Sign in at [developer.apple.com](https://developer.apple.com/), navigate to **Certificates, Identifiers & Profiles**, and create a new **VoIP Services Certificate** for your app's Bundle ID.
2. Upload a CSR (generated via **Keychain Access → Certificate Assistant → Request a Certificate from a Certificate Authority**).
3. Download the generated certificate and double-click to install it in Keychain.

A single VoIP Services Certificate works for both APNS sandbox and production. You need a separate certificate for each Bundle ID.

Next, export the PEM files:

1. In **Keychain Access**, find the VoIP Services certificate, right-click and **Export** as a `.p12` file.
2. Extract PEM files:

```bash
openssl pkcs12 -in PATH_TO_YOUR_P12 -nokeys -out cert.pem -nodes -legacy
openssl pkcs12 -in PATH_TO_YOUR_P12 -nocerts -out key.pem -nodes -legacy
openssl rsa -in key.pem -out key.pem
```

Then create the credential in the Telnyx Portal:

1. Navigate to **API Keys → Credentials** tab, click **Add → iOS Credential**.
2. Enter a credential name (using your Bundle ID is recommended).
3. Paste the full contents of `cert.pem` (including `-----BEGIN CERTIFICATE-----` / `-----END CERTIFICATE-----` markers) into the certificate field.
4. Paste the full contents of `key.pem` (including `-----BEGIN RSA PRIVATE KEY-----` / `-----END RSA PRIVATE KEY-----` markers) into the key field.
5. Click **Add Push Credential** to save.
6. Navigate to **SIP Connections**, open your connection, select the **WebRTC** tab, and in the **iOS** section select the push credential. Save the SIP Connection.

#### Cross-Platform Apps (Flutter and React Native)

Cross-platform apps need credentials for each target platform. Follow the Android portal setup above to create an Android push credential using your Firebase service account JSON, and the iOS portal setup to create an iOS push credential using your VoIP certificate PEM files. Attach both credentials to your SIP Connection under the **WebRTC** tab.

### Android App Setup

**Retrieve the FCM token:**

```kotlin
private fun getFCMToken() {
    FirebaseApp.initializeApp(this)
    FirebaseMessaging.getInstance().token.addOnCompleteListener { task ->
        if (!task.isSuccessful) {
            Log.w(TAG, "Fetching FCM registration token failed", task.exception)
            return@addOnCompleteListener
        }
        val token = task.result
        Log.d(TAG, "FCM token received: $token")
    }
}
```

**Pass the token to the SDK:**

```kotlin
val credentialConfig = CredentialConfig(
    sipUser = username,
    sipPassword = password,
    fcmToken = fcmToken
)

telnyxClient.connect(
    txPushMetaData = txPushMetaData,
    credentialConfig = credentialConfig,
)
```

**Handle incoming push notifications:** Create a `FirebaseMessagingService` and parse the `metadata` field from the notification payload:

```kotlin
override fun onMessageReceived(remoteMessage: RemoteMessage) {
    super.onMessageReceived(remoteMessage)
    val params = remoteMessage.data
    val objects = JSONObject(params as Map<*, *>)
    val metadata = objects.getString("metadata")
    val isMissedCall = objects.getString("message") == "Missed call!"

    if (isMissedCall) {
        // Handle missed call — stop ringing, dismiss notification
        return
    }
    showIncomingCallNotification(metadata)
}
```

When the user answers, reconnect with the push metadata so the SDK receives the pending invitation:

```kotlin
telnyxClient.connect(
    txPushMetaData = txPushMetaData,
    credentialConfig = credentialConfig,
)
```

**Decline calls from push:** The SDK provides `connectWithDeclinePush()` to decline without fully reconnecting:

```kotlin
telnyxClient.connectWithDeclinePush(
    config = credentialConfig,
    txPushMetaData = txPushMetaData.toJson()
)
```

This connects briefly with a `decline_push: true` parameter, handles the decline, and disconnects automatically.

**Android 14 permissions** — Add to `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_PHONE_CALL" />

<service
    android:name=".YourNotificationService"
    android:foregroundServiceType="phoneCall"
    android:exported="true" />
```

Request `POST_NOTIFICATIONS` at runtime before showing notifications.

### iOS App Setup

**Enable push notification capabilities** in Xcode: add **Push Notifications** and **Background Modes** with **Voice over IP** enabled.

**Configure PushKit:**

```swift
import PushKit

private var pushRegistry = PKPushRegistry(queue: DispatchQueue.main)

func initPushKit() {
    pushRegistry.delegate = self
    pushRegistry.desiredPushTypes = Set([.voIP])
}
```

Implement `PKPushRegistryDelegate`:

```swift
extension AppDelegate: PKPushRegistryDelegate {
    func pushRegistry(_ registry: PKPushRegistry,
                      didUpdate credentials: PKPushCredentials,
                      for type: PKPushType) {
        if type == .voIP {
            let deviceToken = credentials.token.map { String(format: "%02X", $0) }.joined()
            // Store this token — pass it to TelnyxClient on login
        }
    }

    func pushRegistry(_ registry: PKPushRegistry,
                      didReceiveIncomingPushWith payload: PKPushPayload,
                      for type: PKPushType,
                      completion: @escaping () -> Void) {
        if payload.type == .voIP {
            handleVoIPPushNotification(payload: payload)
        }
        completion()
    }
}
```

**Pass the token to the SDK:**

```swift
let txConfig = TxConfig(
    sipUser: sipUser,
    password: password,
    pushDeviceToken: "DEVICE_APNS_TOKEN",
    logLevel: .all
)
```

**Handle incoming VoIP push notifications** — reconnect the client and report the call to CallKit:

```swift
func handleVoIPPushNotification(payload: PKPushPayload) {
    guard let metadata = payload.dictionaryPayload["metadata"] as? [String: Any] else { return }
    // ... process caller info ...

    try? telnyxClient?.processVoIPNotification(
        txConfig: txConfig,
        serverConfiguration: serverConfig,
        pushMetaData: metadata
    )

    // Report incoming call to CallKit
    let callHandle = CXHandle(type: .generic, value: caller)
    let callUpdate = CXCallUpdate()
    callUpdate.remoteHandle = callHandle
    callUpdate.hasVideo = false

    if let callId = metadata["call_id"] as? String, let uuid = UUID(uuidString: callId) {
        provider.reportNewIncomingCall(with: uuid, update: callUpdate) { error in
            // ...
        }
    }
}
```

On iOS 13.0 and later, you **must** report incoming VoIP push notifications to CallKit. If you fail to do so, the system will terminate your app.

**Disable push notifications:**

```swift
telnyxClient.disablePushNotifications()
```

Signing back in with the same credentials re-enables push notifications.

**APNS environment:** Set `pushEnvironment` to `sandbox` for debug builds and `production` for release/TestFlight builds in `TxConfig`.

### Flutter App Setup

**Android (Firebase Cloud Messaging):**

1. Register a background message handler in `main`:

```dart
@pragma('vm:entry-point')
Future<void> main() async {
    WidgetsFlutterBinding.ensureInitialized();
    if (defaultTargetPlatform == TargetPlatform.android) {
        await Firebase.initializeApp();
        FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
        await FirebaseMessaging.instance.setForegroundNotificationPresentationOptions(
            alert: true, badge: true, sound: true,
        );
    }
    runApp(const MyApp());
}
```

2. Handle the push notification using a plugin like [FlutterCallkitIncoming](https://pub.dev/packages/flutter_callkit_incoming). On user action (accept/decline), call `TelnyxClient.setPushMetaData()` with `isAnswer` and `isDecline` flags.
3. Create a high-importance notification channel (Android 8.0+) using [flutter_local_notifications](https://pub.dev/packages/flutter_local_notifications) with `Importance.max` for incoming call heads-up alerts.

**iOS (APNS):** The Flutter SDK uses APNS through the native PushKit integration. Configure your iOS project following the standard iOS app setup (enabling Push Notifications and Background Modes/VoIP capabilities in Xcode, configuring PushKit, and reporting incoming calls to CallKit on iOS 13+). The Flutter SDK handles the bridge between native push events and Dart code.

### React Native App Setup

**Install dependencies:**

```bash
npm install react-native-voip-push-notification
# If using Expo for Android FCM:
npx expo install expo-notifications
```

**Android:**

1. Place `google-services.json` from Firebase in your project root.
2. Add the Firebase messaging service to `AndroidManifest.xml`:

```xml
<service
    android:name=".AppFirebaseMessagingService"
    android:exported="false">
    <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
    </intent-filter>
</service>
```

3. The SDK handles FCM token retrieval internally on Android. Pass credentials when connecting via `TelnyxVoIPClient`.

**iOS:**

1. Use `react-native-voip-push-notification` to register for VoIP pushes and capture the device token:

```js
import VoipPushNotification from 'react-native-voip-push-notification';

VoipPushNotification.addEventListener('register', (token) => {
    // Store token — pass to SDK on login
});

VoipPushNotification.addEventListener('notification', (notification) => {
    const metadata = notification.metadata;
    // Process the call...
});

VoipPushNotification.registerVoipToken();
```

2. In Xcode, add **Push Notifications** and **Background Modes** with **Voice over IP**. On iOS 13+, you must report every VoIP push to CallKit or the system will terminate your app.
