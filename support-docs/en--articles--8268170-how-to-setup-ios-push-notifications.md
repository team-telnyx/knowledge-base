---
source_url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
title: "How to Setup iOS Push Notifications"
description: "Resolve the CA error for your webhook URL. See Telnyx guidance and requirements Learn more about How to Setup iOS Push Notifications with Telnyx."
scraped: 2026-07-08
content_hash: 82f5445a802d5adcf8d1c85b4f62d223ee1807a51b53b48ce7c5ba2af3d83d2d
---







# How to Setup iOS Push Notifications

Resolve the CA error for your webhook URL. See Telnyx guidance and requirements Learn more about How to Setup iOS Push Notifications with Telnyx.




## How to Setup iOS Push Notifications

The Telnyx iOS Client WebRTC SDK makes use of APNS in order to deliver push notifications. If you would like to receive notifications when receiving calls on your iOS mobile device you will have to configure a VoIP push certificate.

## Creating a VoIP push certificate

In order to generate VoIP push certificates you will need:

* An Apple developer account
* App BundleID
* CSR (Certificate Signing Request): Explained on Step #7
* Go to <https://developer.apple.com/> and login with your credentials.
* In the **Overview** section, select **“Certificates, Identifiers & Profiles”**

![ios-people-certs-appstoreconnect](_images/16c6050608cf40cd.png)

## Certificates, Identifies & Profiles

Press the blue “+” button to add a new Certificate:

![ios-certs-id-profiles](_images/bc9abbea4fc0f6ba.png)

1. Search for “ **VoIP Services Certificate** ” and Click “ **Continue** ”:

   ![ios-voipservices-cert-desc](_images/0fea7cc6a3f84ea7.png)
2. Select the **BundleID** of the target application, and click “ **Continue** ”

   ![ios-create-voipservices-cert](_images/dc08c037276d24ab.png)
3. Then, you will be requested to upload a CSR from your Mac.

   ![ios-create-voipservices-cert](_images/d33041b6d8c05fb6.png)

## Generate CSR

In order to generate a CSR:

a. Open the KeyChain Access of your mac.

b. Go to Keychain Access >> Certificate Assistance > Request a Certificate from a Certificate Authority.

![ios-export-voipservices-request](_images/67e987c8e410efb6.png)

c. Add your email address and select “Save to disk” option, and click “**Continue**”

![ios-cert-information](_images/9fc5f6e043364ef1.png)

d. Save the Certificate Signing Request (CSR) into your Mac.

![ios-save-csr](_images/f9a6b73a2c0e7fad.png)

## Download Certificate

1. Once you have created your CSR, press “Choose File” and select the certSign created on step #7. Click “ **Continue** ” and you are done.

   ![ios-create-voipservices-cert](_images/d33041b6d8c05fb6.png)
2. The new Certificate has been created. Now you need to download it:

   ![ios-download-cert](_images/45365bef1e07dd4e.png)
3. Search for the downloaded file (usually named voip\_services.cer) and double click on it to install it on your Mac. And that’s all for now!

## Obtain your Cert.pem and Key.pem files

In order to allow the Telnyx VoIP push service to send notifications to your app, you will need to export the VoIP certificate and key:

1. Open Keychain Access on your Mac (where you have installed the VoIP certificate by following the “ **Creating a VoIP push certificate** ” instructions).
2. Search for “VoIP services” and verify that you have the certificate installed for the BundleID of your application.

   ![ios-keychain-access](_images/6f490bcaadd08703.png)
3. Open the contextual menu and select “Export”:

   ![ios-export-voipservices](_images/ea31cbc6fb1b8169.jpg)
4. Save the .p12 file (A password will be requested before saving it):

   ![ios-save-certificate](_images/c0db77120a4ffe02.jpg)
5. Once the certificate is created you will need to run the following commands to obtain the **cert.pem** and **key.pem** files:

   ```
   $ openssl pkcs12 -in PATH_TO_YOUR_P12 -nokeys -out cert.pem -nodes $ openssl pkcs12 -in PATH_TO_YOUR_P12 -nocerts -out key.pem -nodes $ openssl rsa -in key.pem -out key.pem
   ```

Note: After pasting the above content, Kindly check and remove any new line added

1. Now you can go to your Portal account and configure your PN credential.

## Setup your iOS VoIP credentials on your Portal

### Create an iOS Push Credential:

1. Go to portal.telnyx.com and login.
2. Go to the **[API Keys](https://portal.telnyx.com/#/api-keys)** section.
3. From the top bar go to the **Credentials** tab and select “ **Add** ” >> **iOS Credential**

   ![ios-api-keys-pn](_images/955cadecd586b3a9.jpg)
4. Set a credential name (You can use your app bundle ID to easy identify your PN credential) and then copy and paste the contents of your **cert.pem** and **key.pem** files into the defined sections (Notice that you need to copy from ---BEGIN ####--- to ---END--- sections including those marks):

   ![ios-add-pn](_images/7e98b9d642517e6f.jpg)
5. Save the new push credential by pressing the **Add Push Credential** button.

## Assign your iOS Push Credential to a SIP Connection:

1. Go to the **SIP Connections** section on the left panel.
2. Open the Settings menu of the SIP connection that you want to add a Push Credential or [create a new SIP Connection](https://portal.telnyx.com/#/voice/connections) .
3. Select the WEBRTC tab.
4. Go to the iOS Section and select the PN credential created on “ **Create an iOS Push Credential** ”

![ios-select-pn](_images/5555a19d553557f1.png)

That’s done. You can now go to your code and start implementing **PushKit** and **Callkit** using the **TelnyxRTC SDK** and receive VoIP push notifications into your iOS device.

Did this answer your question?

😞😐😃
