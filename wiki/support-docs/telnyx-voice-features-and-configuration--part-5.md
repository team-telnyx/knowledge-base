---
title: Telnyx Voice Features and Configuration
summary: This page consolidates Telnyx support documentation covering call forwarding,
  conference calls, TeXML Bin voicemail and call forwarding, sending and receiving
  SMS with the Python SDK, debugging tools, configuring Call Control/TeXML applications,
  voicemail setup, TeXML and Voice API compatibility, Android and iOS push notification
  setup, webhook CA errors, and Voice API essentials.
sources:
- url: https://support.telnyx.com/en/articles/1130657-call-forwarding
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
- url: https://support.telnyx.com/en/articles/13386198-texml-bin-simple-voicemail-and-call-forwarding
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
- url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
- url: https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail
- url: https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility
- url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
- url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
- url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
- url: https://support.telnyx.com/en/collections/133140-voice-api-essentials
- url: https://support.telnyx.com/en/collections/17907095-texml-tutorials
- url: https://support.telnyx.com/en/collections/5782829-webrtc-voice-sdk
updated_at: 2026-07-17T09:05:29Z
---

# Telnyx Voice Features and Configuration

*Part 5 of 6 — see also: [Part 1](telnyx-voice-features-and-configuration--part-1.md), [Part 2](telnyx-voice-features-and-configuration--part-2.md), [Part 3](telnyx-voice-features-and-configuration--part-3.md), [Part 4](telnyx-voice-features-and-configuration--part-4.md), [Part 6](telnyx-voice-features-and-configuration--part-6.md)*

This page consolidates Telnyx support documentation covering call forwarding, conference calls, TeXML Bin voicemail and call forwarding, sending and receiving SMS with the Python SDK, debugging tools, configuring Call Control/TeXML applications, voicemail setup, TeXML and Voice API compatibility, Android and iOS push notification setup, webhook CA errors, and Voice API essentials.

## Android Push Notification Setup

The Telnyx Android Client WebRTC SDK makes use of Firebase Cloud Messaging in order to deliver push notifications. If you would like to receive notifications when receiving calls on your Android mobile device, you will have to enable Firebase Cloud Messaging within your application.

### Requirements

- Set up a Firebase console account.
- Create a Firebase project.
- Add Firebase to your Android Application.
- Set up a Push Credential within the Telnyx Portal.
- Generate a Firebase Cloud Messaging instance token.
- Send the token with your login message.

Adding Firebase to your application is a simple process. Click on the Android icon on the home screen of the console to start:

![firebase-pn-screen](_images/58a5f41bbc2e59fb.png)

### Register Application

Next, enter your application details and register your application.

![add-firebase-to-app](_images/ea56394ba142133e.png)

After your application is registered, Firebase will generate a `google-services.json` file for you which will need to be added to your project root directory:

![download-config-file-firebase](_images/13c428a1084bd6d6.png)

### Firebase Configuration

Follow the Firebase guide on how to enable the Firebase products within your application: <https://firebase.google.com/docs/android/setup#add-config-file>

An alternative method is to add Firebase using the Firebase Assistant within Android Studio if it is set up within your IDE. You can view steps on how to register via this option here: <https://firebase.google.com/docs/android/setup#assistant>

Once your application is set up within the Firebase Console, you will be able to access the server key required for portal setup. You can access the server key by going into your project overview → project settings and selecting Cloud Messaging. Once there, the project credentials will be visible for use in our portal setup.

![add-server-key](_images/d9ecf2ff2de51000.png)

### Android VoIP Credential Setup

The next step is to set up your Android VoIP credentials in the portal.

1. Go to [portal.telnyx.com](https://portal.telnyx.com/#/login/sign-in) and login.
2. Go to the API Keys & Credentials section on the left panel under Account Settings.
3. From the top bar go to the Credentials tab and select "Add" >> Android Credential.

![api-keys-pn](_images/955cadecd586b3a9.jpg)

4. Enter the details required for your Android Push Credentials. This includes a Credential name and the server key from Firebase mentioned in an earlier step.

![add-android-push-credential](_images/e37482e2940557cb.png)

Save the new push credential by pressing the Add Push Credential button.

We can now attach this Android Push Credential to a SIP Connection:

1. Go to **Voice Suite → SIP Trunking** section on the left panel.
2. Open the Settings menu of the SIP connection that you want to add a Push Credential to, or create a new SIP Connection.
3. Select the WebRTC tab.
4. Go to the Android Section and select the PN credential you previously created.

![sip-connection-pn](_images/66f71ff545d4cab3.png)

### Final Steps

The portal setup is complete. Now when Firebase is properly integrated within your application, you will be able to retrieve a token with a method such as this:

```kotlin
private fun getFCMToken() {
  FirebaseApp.initializeApp(this)
  FirebaseMessaging.getInstance().token.addOnCompleteListener { task ->
    if (!task.isSuccessful) {
      Timber.d("Fetching FCM registration token failed")
    } else if (task.isSuccessful) {
      // Get new FCM registration token
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

The final step is to create a `MessagingService` for your application. The `MessagingService` is the class that handles FCM messages and creates notifications for the device from these messages. You can read about the Firebase messaging service class here: <https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService>

A sample implementation is available here: <https://github.com/team-telnyx/telnyx-webrtc-android/blob/main/app/src/main/java/com/telnyx/webrtc/sdk/utility/MyFirebaseMessagingService.kt>

Once this class is created, remember to update your manifest and specify the newly created service: <https://firebase.google.com/docs/cloud-messaging/android/client#manifest>

You are now ready to receive push notifications via Firebase Messaging Service.
