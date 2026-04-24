---
title: Android Portal Setup
summary: A step-by-step guide to setting up push notifications in Android.
sources:
  - url: https://developers.telnyx.com/development/webrtc/android-sdk/push-notification/portal-setup/index
    content_hash: e7ea569fb6404e03127629a249b0dee7dfee10b254ab46bac8091dd18e57aeae
updated_at: 2026-04-10T00:00:00Z
---

# Android Portal Setup

A step-by-step guide to setting up push notifications in Android. Learn how to configure and implement notifications to ensure seamless communication in your application.

The Telnyx Android Client WebRTC SDK makes use of Firebase Cloud Messaging to deliver push notifications. If you want to receive notifications when receiving calls on your Android mobile device you need to enable Firebase Cloud Messaging within your application.

To do this you need to:

* Set up a Firebase console account
* Create a Firebase project
* Add Firebase to your Android Application
* Setup a Push Credential within the Telnyx Portal
* Generate a Firebase Cloud Messaging instance token
* Send the token with your login message

Adding Firebase to your application is a simple process. Click on the Android icon on the home screen of the console to start:

<img alt="firebase-pn-screen" />

Next, enter your application details and register your application

<img alt="add-firebase-to-app" />

After your application is registered, Firebase will generate a google-services.json file for you which will need to be added to your project root directory:

<img alt="download-config-file-firebase" />

After that, you can follow this guide on how to enable the Firebase products within your application [https://firebase.google.com/docs/android/setup#add-config-file](https://firebase.google.com/docs/android/setup#add-config-file)

An alternative method is to add Firebase using the Firebase Assistant within Android Studio if it is set up within your IDE. You can view steps on how to register via this option here:
[https://firebase.google.com/docs/android/setup#assistant](https://firebase.google.com/docs/android/setup#assistant)

Once your application is set up within the Firebase Console, you will be able to access the server key required for portal setup. You can access the server key file in JSON format by going into your project overview -> project settings -> Service Account and selecting Generate New Private Key.

<img alt="generate-server-key" />

The next step is to set up your Android VoIP credentials in the portal.

1. Go to portal.telnyx.com and log in.
2. Go to the API Keys section on the left panel.
3. From the top bar go to the Credentials tab and select “Add” >> Android Credential

<img alt="api-keys-pn" />

4. Enter the details required for your Android Push Credentials. This includes a Credential name and the generated server key in JSON format in the field Project Account json

<img alt="add-android-push-credential" />

Save the new push credential by pressing the Add Push Credential button

We can now attach this Android Push Credential to a SIP Connection:

1. Go to the SIP Connections section on the left panel.
2. Open the Settings menu of the SIP connection that you want to add a Push Credential to or [create a new SIP Connection](https://developers.telnyx.com/docs/voice/sip-trunking/quickstart).
3. Select the WebRTC tab.
4. Go to the Android Section and select the PN credential you previously created.


## Related Pages

- [iOS Portal Setup](../reference/ios-portal-setup.md)
- [Portal Setup](../reference/portal-setup.md)
