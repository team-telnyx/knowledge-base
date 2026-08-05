---
title: WebRTC Voice SDKs
summary: The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate
  and control Telnyx call legs from browsers and mobile devices. They translate between
  the WebRTC standard and Telnyx's SIP platform, providing worldwide PSTN coverage
  under the Programmable Voice API umbrella. This page covers SDK architecture, authentication
  options, the JS SDK client and call lifecycle, demo app setup, configuration interfaces,
  and Android push notifications.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/architecture
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index
- url: https://developers.telnyx.com/docs/voice/webrtc/fundamentals
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/icalloptions
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/iclientoptions
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
updated_at: 2026-08-05T14:08:20Z
---

# WebRTC Voice SDKs

*Part 7 of 7 — see also: [Part 1](webrtc-voice-sdks--part-1.md), [Part 2](webrtc-voice-sdks--part-2.md), [Part 3](webrtc-voice-sdks--part-3.md), [Part 4](webrtc-voice-sdks--part-4.md), [Part 5](webrtc-voice-sdks--part-5.md), [Part 6](webrtc-voice-sdks--part-6.md)*

The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate and control Telnyx call legs from browsers and mobile devices. They translate between the WebRTC standard and Telnyx's SIP platform, providing worldwide PSTN coverage under the Programmable Voice API umbrella. This page covers SDK architecture, authentication options, the JS SDK client and call lifecycle, demo app setup, configuration interfaces, and Android push notifications.

## Android Push Notifications

**Prerequisites:**

- A [Telnyx account](https://portal.telnyx.com) with a configured SIP Connection.
- A [Firebase project](https://console.firebase.google.com/) with Cloud Messaging enabled.
- The Telnyx Android WebRTC SDK integrated into your application.

### Portal Setup

#### 1. Configure Firebase Cloud Messaging

1. Go to the [Firebase Console](https://console.firebase.google.com/) and open your project.
2. Navigate to **Project Overview → Project Settings → Service Accounts**.
3. Select **Generate New Private Key** to download a service account JSON file.

The Firebase Cloud Messaging HTTP v1 API uses a service account JSON key, not the legacy server key. Make sure you download the full service account JSON file.

#### 2. Create an Android push credential in the Telnyx Portal

1. Go to [portal.telnyx.com](https://portal.telnyx.com) and log in.
2. Navigate to **API Keys** in the left panel.
3. Select the **Credentials** tab, then click **Add → Android Credential**.
4. Enter a credential name and paste the contents of the service account JSON file into the **Project Account JSON** field.
5. Click **Add Push Credential** to save.

#### 3. Attach the credential to a SIP Connection

1. Navigate to **SIP Connections** in the left panel.
2. Open the SIP Connection you want to configure (or [create a new one](/docs/voice/sip-trunking/get-started)).
3. Select the **WebRTC** tab.
4. In the **Android** section, select the push credential you created.
5. Save the SIP Connection.

### App Setup

#### Retrieve the FCM token

After integrating Firebase into your Android application ([Firebase setup guide](https://firebase.google.com/docs/android/setup)), retrieve the FCM registration token:

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

#### Pass the token to the SDK

Provide the FCM token when connecting the `TelnyxClient`. The SDK registers it with Telnyx so push notifications can be routed to this device:

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

#### Handle incoming push notifications

Create a `FirebaseMessagingService` to process incoming FCM messages. Parse the `metadata` field from the notification payload and pass it to your notification UI:

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

    // Show incoming call notification with metadata
    showIncomingCallNotification(metadata)
}
```

When the user answers, reconnect to the socket with the push metadata so the SDK can receive the pending invitation:

```kotlin
telnyxClient.connect(
    txPushMetaData = txPushMetaData,
    credentialConfig = credentialConfig,
)
```

#### Decline calls from push notifications

The SDK provides `connectWithDeclinePush()` to decline incoming calls without fully reconnecting:

```kotlin
telnyxClient.connectWithDeclinePush(
    config = credentialConfig,
    txPushMetaData = txPushMetaData.toJson()
)
```

This connects briefly with a `decline_push: true` parameter, handles the decline, and disconnects automatically.

#### Android 14 permissions

Android 14 requires explicit notification permissions. Add these to your `AndroidManifest.xml`:

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

### Troubleshooting

#### FCM token not passed to login

Verify that the FCM token is retrieved successfully and included in the `CredentialConfig` or `TokenConfig` passed to `connect()`. Check your logs for the token value.

#### Incorrect google-services.json

Confirm that the `google-services.json` file is in your app module's root directory and the package name matches your application.

#### Wrong push credential on the SIP Connection

In the Telnyx Portal, open your SIP Connection → **WebRTC** tab → **Android** section and verify the correct credential is selected.

#### Invalid push credential

If the service account JSON is malformed or from the wrong Firebase project, push delivery fails silently. Generate a fresh key from the Firebase Console and update the credential in the Portal.

#### Testing push delivery

The SDK repository includes a testing tool in the `push-notification-tool/` directory that sends test FCM notifications to verify your setup independently of the Telnyx call flow:

```bash
cd push-notification-tool
npm install
npm start
```

If test notifications arrive but calls don't trigger pushes, the issue is in your Portal or SIP Connection configuration rather than Firebase.

### Next Steps

- [Push notifications overview](/docs/voice/webrtc/push-notifications) — Multidevice support and architecture.
- [Android SDK reference](/development/webrtc/android-sdk) — Full SDK documentation.
- [Mobile Push Credentials API](/api/webrtc/mobile-push-credentials) — Manage credentials programmatically.
