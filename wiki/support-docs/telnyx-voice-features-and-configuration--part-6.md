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

*Part 6 of 6 — see also: [Part 1](telnyx-voice-features-and-configuration--part-1.md), [Part 2](telnyx-voice-features-and-configuration--part-2.md), [Part 3](telnyx-voice-features-and-configuration--part-3.md), [Part 4](telnyx-voice-features-and-configuration--part-4.md), [Part 5](telnyx-voice-features-and-configuration--part-5.md)*

This page consolidates Telnyx support documentation covering call forwarding, conference calls, TeXML Bin voicemail and call forwarding, sending and receiving SMS with the Python SDK, debugging tools, configuring Call Control/TeXML applications, voicemail setup, TeXML and Voice API compatibility, Android and iOS push notification setup, webhook CA errors, and Voice API essentials.

## iOS Push Notification Setup

The Telnyx iOS Client WebRTC SDK makes use of APNS in order to deliver push notifications. If you would like to receive notifications when receiving calls on your iOS mobile device, you will have to configure a VoIP push certificate.

### Creating a VoIP Push Certificate

In order to generate VoIP push certificates you will need:

- An Apple developer account.
- App BundleID.
- CSR (Certificate Signing Request).

Go to <https://developer.apple.com/> and login with your credentials. In the **Overview** section, select **"Certificates, Identifiers & Profiles"**.

![ios-people-certs-appstoreconnect](_images/16c6050608cf40cd.png)

Press the blue "+" button to add a new Certificate:

![ios-certs-id-profiles](_images/bc9abbea4fc0f6ba.png)

1. Search for "**VoIP Services Certificate**" and click "**Continue**":

   ![ios-voipservices-cert-desc](_images/0fea7cc6a3f84ea7.png)
2. Select the **BundleID** of the target application, and click "**Continue**":

   ![ios-create-voipservices-cert](_images/dc08c037276d24ab.png)
3. Then, you will be requested to upload a CSR from your Mac.

   ![ios-create-voipservices-cert](_images/d33041b6d8c05fb6.png)

### Generate CSR

To generate a CSR:

a. Open the Keychain Access of your Mac.

b. Go to Keychain Access >> Certificate Assistance > Request a Certificate from a Certificate Authority.

![ios-export-voipservices-request](_images/67e987c8e410efb6.png)

c. Add your email address and select "Save to disk" option, and click "**Continue**".

![ios-cert-information](_images/9fc5f6e043364ef1.png)

d. Save the Certificate Signing Request (CSR) into your Mac.

![ios-save-csr](_images/f9a6b73a2c0e7fad.png)

### Download Certificate

1. Once you have created your CSR, press "Choose File" and select the certSign created earlier. Click "**Continue**" and you are done.

   ![ios-create-voipservices-cert](_images/d33041b6d8c05fb6.png)
2. The new Certificate has been created. Now you need to download it:

   ![ios-download-cert](_images/45365bef1e07dd4e.png)
3. Search for the downloaded file (usually named `voip_services.cer`) and double-click on it to install it on your Mac.

### Obtain Your Cert.pem and Key.pem Files

In order to allow the Telnyx VoIP push service to send notifications to your app, you will need to export the VoIP certificate and key:

1. Open Keychain Access on your Mac (where you have installed the VoIP certificate).
2. Search for "VoIP services" and verify that you have the certificate installed for the BundleID of your application.

   ![ios-keychain-access](_images/6f490bcaadd08703.png)
3. Open the contextual menu and select "Export":

   ![ios-export-voipservices](_images/ea31cbc6fb1b8169.jpg)
4. Save the `.p12` file (a password will be requested before saving it):

   ![ios-save-certificate](_images/c0db77120a4ffe02.jpg)
5. Once the certificate is created, run the following commands to obtain the **cert.pem** and **key.pem** files:

   ```
   $ openssl pkcs12 -in PATH_TO_YOUR_P12 -nokeys -out cert.pem -nodes
   $ openssl pkcs12 -in PATH_TO_YOUR_P12 -nocerts -out key.pem -nodes
   $ openssl rsa -in key.pem -out key.pem
   ```

6. Now you can go to your Portal account and configure your PN credential.

### Set Up Your iOS VoIP Credentials on Your Portal

**Create an iOS Push Credential:**

1. Go to portal.telnyx.com and login.
2. Go to the API Keys section.
3. From the top bar go to the **Credentials** tab and select "**Add**" >> **iOS Credential**.

   ![ios-api-keys-pn](_images/955cadecd586b3a9.jpg)
4. Set a credential name (you can use your app bundle ID to easily identify your PN credential) and then copy and paste the contents of your **cert.pem** and **key.pem** files into the defined sections (notice that you need to copy from `---BEGIN ####---` to `---END---` sections including those marks):

   ![ios-add-pn](_images/7e98b9d642517e6f.jpg)
5. Save the new push credential by pressing the **Add Push Credential** button.

**Assign your iOS Push Credential to a SIP Connection:**

1. Go to the **SIP Connections** section on the left panel.
2. Open the Settings menu of the SIP connection that you want to add a Push Credential, or create a new SIP Connection.
3. Select the WEBRTC tab.
4. Go to the iOS Section and select the PN credential created earlier.

![ios-select-pn](_images/5555a19d553557f1.png)

You can now go to your code and start implementing **PushKit** and **Callkit** using the **TelnyxRTC SDK** and receive VoIP push notifications into your iOS device.

## Webhook Issue: CA Error

If the error says the certificate authority (CA) isn't recognized and your payload is being sent to the failover webhook URL instead of the primary, that means the connection can't be established over HTTPS.

There are two options:

(a) Make sure your server has a certificate that is signed by a known CA.

(b) Use HTTP instead of HTTPS.

More about Certificate Authority is available in the Certificate Error article.

## Voice API Essentials

The Voice API Essentials collection provides helpful links that explain Mission Control Portal features and troubleshooting tips across several categories:

### Call Control / TeXML

Integrate Call Control using TeXML with Telnyx for enhanced voice capabilities.

- [Configuring Call Control/TeXML Applications - Voice API](configuring-call-control-texml-applications-voice-api.md)
- [TeXML and Telnyx Voice API compatibility](texml-and-telnyx-voice-api-compatibility.md)
- Real-Time Transcription

### Guide to Telnyx E911 Services

Learn about Telnyx's E911 services. Set up, register addresses, and and test E911.

- E911 Setup Guide
- Register E911 addresses
- How do I test E911 service?

### General Voice API Help

Get assistance with Telnyx's Voice API: UK TPS, Google Verified Calls, STIR/SHAKEN.

- UK TPS Register: Guidelines
- Google Verified Calls FAQ
- STIR/SHAKEN With Telnyx
- Caller ID Outbound vs CNAM
- Distinguish your outbound profiles & DIDs
- US Local Call Completion
- Robocall Mitigation Database
- CLI & CLD Validation FAQ
- Canadian STIR/SHAKEN Implementation FAQs

## TeXML Tutorials

The TeXML tutorials collection contains product tutorials for TeXML:

- [TeXML Bin Simple Voicemail and Call Forwarding](texml-bin-simple-voicemail-and-call-forwarding.md)
- Twilio TwiML Conference on Telnyx

## WebRTC Voice SDK

Telnyx provides detailed setup guides for iOS and Android push notifications using the WebRTC Voice SDK:

- [How to Setup iOS Push Notifications](how-to-setup-ios-push-notifications.md)
- [Android Push Notification Setup](android-push-notification-setup.md)
