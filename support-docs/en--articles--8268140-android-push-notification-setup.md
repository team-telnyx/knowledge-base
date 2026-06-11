---
source_url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
scraped: 2026-06-11
---

Android Push Notification Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Android Push Notification Setup

Integrate Android push notifications with Telnyx's WebRTC SDK. Start here!

Written by David

Updated over 3 weeks ago

Table of contents

# Android Push Notification Setup

The Telnyx Android Client WebRTC SDK makes use of Firebase Cloud Messaging in order to deliver push notifications. If you would like to receive notifications when receiving calls on your Android mobile device you will have to enable Firebase Cloud Messaging within your application.

## Requirements

* Set up a Firebase console account
* Create a Firebase project
* Add Firebase to your Android Application
* Setup a Push Credential within the Telnyx Portal
* Generate a Firebase Cloud Messaging instance token
* Send the token with your login message

Adding Firebase to your application is a simple process. Click on the Android icon on the home screen of the console to start:

[![firebase-pn-screen](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952322/7fa0a9c0a1ec06d967a3456e/unnamed.png?expires=1781168400&signature=5e32345480de250317a47fbdc857af935122f2d46c954328e7148d915efe70ee&req=fCAuH8x8noNdFb4f3HP0gNY7yYIv%2FFBVyokLv6ujZBTHZmU6mNEjtq1uye6T%0AJn2jhEd4M0fomZmPZA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952322/7fa0a9c0a1ec06d967a3456e/unnamed.png?expires=1781168400&signature=5e32345480de250317a47fbdc857af935122f2d46c954328e7148d915efe70ee&req=fCAuH8x8noNdFb4f3HP0gNY7yYIv%2FFBVyokLv6ujZBTHZmU6mNEjtq1uye6T%0AJn2jhEd4M0fomZmPZA%3D%3D%0A)

## Register Application

Next, enter your application details and register your application

[![add-firebase-to-app](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952326/8cf36be1f5dd7cc104ca8526/add-firebase-to-app.png?expires=1781168400&signature=0cf9916b8a6d8df0383bbd60177a4640d68021aeb04b585b74a206449d51e568&req=fCAuH8x8noNZFb4f3HP0gEkwB1R7Z3XuAmUXM0EYSqO8pp4zytI%2BB1fiyvAO%0A1G3TJQbh8TsdpMJn0w%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952326/8cf36be1f5dd7cc104ca8526/add-firebase-to-app.png?expires=1781168400&signature=0cf9916b8a6d8df0383bbd60177a4640d68021aeb04b585b74a206449d51e568&req=fCAuH8x8noNZFb4f3HP0gEkwB1R7Z3XuAmUXM0EYSqO8pp4zytI%2BB1fiyvAO%0A1G3TJQbh8TsdpMJn0w%3D%3D%0A)

After your application is registered, Firebase will generate a google-services.json file for you which will need to be added to your project root directory:

[![download-config-file-firebase](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952340/cc948090b0244343e6b6af78/download-config-file-firebase.png?expires=1781168400&signature=dc168d9cdfb8f09bfc4c2dc0ffb0ad9773c45bec5a8d8997bb934d64ecbd2347&req=fCAuH8x8noVfFb4f3HP0gNmO7d0j%2BVa8ZHKB4ClKdlOXB0%2BKOXJSFQZsiSGp%0AL01OMJjW%2ByDOQcgR5A%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952340/cc948090b0244343e6b6af78/download-config-file-firebase.png?expires=1781168400&signature=dc168d9cdfb8f09bfc4c2dc0ffb0ad9773c45bec5a8d8997bb934d64ecbd2347&req=fCAuH8x8noVfFb4f3HP0gNmO7d0j%2BVa8ZHKB4ClKdlOXB0%2BKOXJSFQZsiSGp%0AL01OMJjW%2ByDOQcgR5A%3D%3D%0A)

## Firebase Configuration

After that, you can follow this guide on how to enable the firebase products within your application <https://firebase.google.com/docs/android/setup#add-config-file>

An alternative method is to add Firebase using the Firebase Assistant within Android Studio if it is setup within your IDE.

You can view steps on how to register via this option here: <https://firebase.google.com/docs/android/setup#assistant>

Once your application is set up within the Firebase Console, you will be able to access the server key required for portal setup.

You can access the server key by going into your project overview -> project settings and selecting Cloud Messaging. Once there, the project credentials will be visible for use in our portal setup.

[![add-server-key](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952350/c7dfd82ab71ed9ff465faaff/add-server-key.png?expires=1781168400&signature=e2b87a60b91928c718e5dddaf5832695e37e2870b37a631ecad19834ca12cc8f&req=fCAuH8x8noRfFb4f3HP0gMr7q25xeigek0oOd9cy8YdK%2B5a5QQRZVsmUaQBx%0AYfA5koheLv3GRIt9xQ%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952350/c7dfd82ab71ed9ff465faaff/add-server-key.png?expires=1781168400&signature=e2b87a60b91928c718e5dddaf5832695e37e2870b37a631ecad19834ca12cc8f&req=fCAuH8x8noRfFb4f3HP0gMr7q25xeigek0oOd9cy8YdK%2B5a5QQRZVsmUaQBx%0AYfA5koheLv3GRIt9xQ%3D%3D%0A)

## Android VoIP Credential Setup

The next step is to set up your Android VoIP credentials in the portal.

1. Go to [portal.telnyx.com](https://portal.telnyx.com/#/login/sign-in) and login.
2. Go to the [API Keys & Credentials](https://portal.telnyx.com/#/api-keys) section on the left panel under Account Settings.
3. From the top bar go to the [Credentials](https://portal.telnyx.com/#/api-keys/push-credentials) tab and select “Add” >> Android Credential

[![api-keys-pn](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952365/31c2ae0077eb776644a3e9c2/api-keys-pn.jpg?expires=1781168400&signature=e0cba488535d9e06d412745963d64bc84aed6a336666841d06d5cd0baa6a2ff2&req=fCAuH8x8nodaFb4f3HP0gK6YXpLXy47D%2BadbV9ekCptJfOudBqgwywUlpysJ%0Agmgk1zyPpNj5tq836A%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952365/31c2ae0077eb776644a3e9c2/api-keys-pn.jpg?expires=1781168400&signature=e0cba488535d9e06d412745963d64bc84aed6a336666841d06d5cd0baa6a2ff2&req=fCAuH8x8nodaFb4f3HP0gK6YXpLXy47D%2BadbV9ekCptJfOudBqgwywUlpysJ%0Agmgk1zyPpNj5tq836A%3D%3D%0A)

1. Enter the details required for your Android Push Credentials. This includes a Credential name and the server key from firebase mentioned in an earlier step.

[![add-android-push-credential](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952372/0c9e90b5a327e7e4290a294d/add-android-push-credential.png?expires=1781168400&signature=c40ef3db4ffdd5227eb4c6ae4afb0def682ac030cf0a3f3ffb44ed8ba31019eb&req=fCAuH8x8noZdFb4f3HP0gIexYmA4RbnNh6eP7i%2FMm0NTL9Drd6Ecpye9H8Bv%0AgyPbPdfOKDD%2FTI1jWg%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952372/0c9e90b5a327e7e4290a294d/add-android-push-credential.png?expires=1781168400&signature=c40ef3db4ffdd5227eb4c6ae4afb0def682ac030cf0a3f3ffb44ed8ba31019eb&req=fCAuH8x8noZdFb4f3HP0gIexYmA4RbnNh6eP7i%2FMm0NTL9Drd6Ecpye9H8Bv%0AgyPbPdfOKDD%2FTI1jWg%3D%3D%0A)

Save the new push credential by pressing the Add Push Credential button

We can now attach this Android Push Credential to a SIP Connection:

1. go to **Voice Suite → SIP Trunking** section on the left panel.
2. Open the Settings menu of the SIP connection that you want to add a Push Credential to or [create a new SIP Connection](https://portal.telnyx.com/#/voice/connections) .
3. Select the WebRTC tab.
4. Go to the Android Section and select the PN credential you previously created.

[![sip-connection-pn](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952378/13a9aa4be75b4565ebf781b9/sip-connection-pn.png?expires=1781168400&signature=c1438b01b0b6c8306304db7bf0ac8807b61c161115710e2fe193478c8c9ce2ca&req=fCAuH8x8noZXFb4f3HP0gCETqeBtSkrhHAGLbrVsoEoJvjnIm33ZNaAcgWSR%0AhJxO87YBE1MfK52nxw%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952378/13a9aa4be75b4565ebf781b9/sip-connection-pn.png?expires=1781168400&signature=c1438b01b0b6c8306304db7bf0ac8807b61c161115710e2fe193478c8c9ce2ca&req=fCAuH8x8noZXFb4f3HP0gCETqeBtSkrhHAGLbrVsoEoJvjnIm33ZNaAcgWSR%0AhJxO87YBE1MfK52nxw%3D%3D%0A)

## Final Steps

The portal setup is complete. Now when firebase is properly integrated within your application, you will be able to retrieve a token with a method such as this:

```
private fun getFCMToken() { FirebaseApp.initializeApp(this) FirebaseMessaging.getInstance().token.addOnCompleteListener { task -> if (!task.isSuccessful) { Timber.d("Fetching FCM registration token failed") } else if (task.isSuccessful){ // Get new FCM registration token try { token = task.result } catch (e: IOException) { Timber.d(e) } Timber.d("FCM token received: $token") } } }
```

Note: After pasting the above content, Kindly check and remove any new line added

The final step is to create a MessagingService for your application.

The MessagingService is the class that handles FCM messages and creates notifications for the device from these messages. You can read about the firebase messaging service class here: <https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService>

We have a sample implementation for you to take a look at here: <https://github.com/team-telnyx/telnyx-webrtc-android/blob/main/app/src/main/java/com/telnyx/webrtc/sdk/utility/MyFirebaseMessagingService.kt>

Once this class is created, remember to update your manifest and specify the newly created service like so:

<https://firebase.google.com/docs/cloud-messaging/android/client#manifest>

You are now ready to receive push notifications via Firebase Messaging Service.

---

Related Articles

[MicroSIP: Setup with Telnyx](https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx)[Grandstream Wave Lite (Android)](https://support.telnyx.com/en/articles/6184897-grandstream-wave-lite-android)[Grandstream GDS3710: Wave Lite (Android)](https://support.telnyx.com/en/articles/6187273-grandstream-gds3710-wave-lite-android)[Grandstream GXV3370](https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370)[How to Setup iOS Push Notifications](https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications)

Did this answer your question?

😞😐😃

Table of contents
