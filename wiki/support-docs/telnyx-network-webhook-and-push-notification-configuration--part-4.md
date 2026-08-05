---
title: Telnyx Network, Webhook, and Push Notification Configuration
summary: This page consolidates Telnyx guidance on whitelisting SIP signaling, media,
  and webhook IP addresses; configuring and verifying webhooks (including signature
  rotation); setting up iOS and Android push notifications for the WebRTC SDK; and
  accessing support resources such as the status page, bug reporting, and the Bot-to-Bot
  Knowledge Agent API.
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
- url: https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
- url: https://support.telnyx.com/en/articles/6707731-telnyx-status-page
- url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
- url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
- url: https://support.telnyx.com/en/collections/5782829-webrtc-voice-sdk
updated_at: 2026-08-05T13:24:23Z
---

# Telnyx Network, Webhook, and Push Notification Configuration

*Part 4 of 5 — see also: [Part 1](telnyx-network-webhook-and-push-notification-configuration--part-1.md), [Part 2](telnyx-network-webhook-and-push-notification-configuration--part-2.md), [Part 3](telnyx-network-webhook-and-push-notification-configuration--part-3.md), [Part 5](telnyx-network-webhook-and-push-notification-configuration--part-5.md)*

This page consolidates Telnyx guidance on whitelisting SIP signaling, media, and webhook IP addresses; configuring and verifying webhooks (including signature rotation); setting up iOS and Android push notifications for the WebRTC SDK; and accessing support resources such as the status page, bug reporting, and the Bot-to-Bot Knowledge Agent API.

## Android Push Notifications (WebRTC SDK)

The Telnyx Android Client WebRTC SDK uses Firebase Cloud Messaging (FCM) to deliver push notifications. To receive notifications when receiving calls on an Android mobile device, enable Firebase Cloud Messaging within your application.

### Requirements

- Set up a Firebase console account
- Create a Firebase project
- Add Firebase to your Android Application
- Set up a Push Credential within the Telnyx Portal
- Generate a Firebase Cloud Messaging instance token
- Send the token with your login message

### Registering the Application

1. Click the Android icon on the Firebase console home screen.

![firebase-pn-screen](_images/58a5f41bbc2e59fb.png)

2. Enter your application details and register your application.

![add-firebase-to-app](_images/ea56394ba142133e.png)

3. After registration, Firebase generates a `google-services.json` file that must be added to your project root directory.

![download-config-file-firebase](_images/13c428a1084bd6d6.png)

### Firebase Configuration

Follow the [Firebase Android setup guide](https://firebase.google.com/docs/android/setup#add-config-file) to enable Firebase products within your application. Alternatively, add Firebase using the Firebase Assistant within Android Studio if it is set up in your IDE; see the [assistant steps](https://firebase.google.com/docs/android/setup#assistant).

Once your application is set up within the Firebase Console, you can access the server key required for portal setup. Go to **Project Overview → Project Settings → Cloud Messaging** to view the project credentials.

![add-server-key](_images/d9ecf2ff2de51000.png)

### Android VoIP Credential Setup in the Portal

1. Go to [portal.telnyx.com](https://portal.telnyx.com/#/login/sign-in) and log in.
2. Go to the [API Keys & Credentials](https://portal.telnyx.com/#/api-keys) section on the left panel under Account Settings.
3. From the top bar, go to the [Credentials](https://portal.telnyx.com/#/api-keys/push-credentials) tab and select **Add → Android Credential**.

![api-keys-pn](_images/955cadecd586b3a9.jpg)

4. Enter the details required for your Android Push Credentials, including a credential name and the server key from Firebase.

![add-android-push-credential](_images/e37482e2940557cb.png)

5. Save the new push credential by pressing **Add Push Credential**.

### Attaching the Android Push Credential to a SIP Connection

1. Go to **Voice Suite → SIP Trunking** on the left panel.
2. Open the Settings menu of the SIP connection you want to add a Push Credential to, or [create a new SIP Connection](https://portal.telnyx.com/#/voice/connections).
3. Select the **WebRTC** tab.
4. Go to the Android Section and select the PN credential you previously created.

![sip-connection-pn](_images/66f71ff545d4cab3.png)

### Final Steps

Once Firebase is integrated within your application, retrieve a token with a method such as:

```
private fun getFCMToken() {
  FirebaseApp.initializeApp(this)
  FirebaseMessaging.getInstance().token.addOnCompleteListener { task ->
    if (!task.isSuccessful) {
      Timber.d("Fetching FCM registration token failed")
    } else if (task.isSuccessful) {
      try {
        token = task.result
      } catch (e: IOException) {
        Timber.d(e)
      }
      Timber.d("FCM token received: $token")
    }
  }
}
```

Create a `MessagingService` for your application. The `MessagingService` is the class that handles FCM messages and creates notifications for the device from these messages. See the [Firebase MessagingService reference](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService) and a [sample implementation](https://github.com/team-telnyx/telnyx-webrtc-android/blob/main/app/src/main/java/com/telnyx/webrtc/sdk/utility/MyFirebaseMessagingService.kt).

Once the class is created, update your manifest and specify the newly created service as described in the [Firebase Android client manifest guide](https://firebase.google.com/docs/cloud-messaging/android/client#manifest). You are now ready to receive push notifications via Firebase Messaging Service.

## Status Page and Incident Visibility

The Telnyx status page provides real-time updates on incidents and maintenance schedules: <https://status.telnyx.com/>. You can subscribe to updates in real time through multiple channels.
