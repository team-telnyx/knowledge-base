---
source_url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
scraped: 2026-06-11
---

How to Setup iOS Push Notifications | Telnyx Help Center

[Skip to main content](#main-content)

# How to Setup iOS Push Notifications

Resolve the CA error for your webhook URL. Understand the root cause and solutions.

Written by David

Updated over 3 weeks ago

Table of contents

# How to Setup iOS Push Notifications

The Telnyx iOS Client WebRTC SDK makes use of APNS in order to deliver push notifications. If you would like to receive notifications when receiving calls on your iOS mobile device you will have to configure a VoIP push certificate.

## Creating a VoIP push certificate

In order to generate VoIP push certificates you will need:

* An Apple developer account
* App BundleID
* CSR (Certificate Signing Request): Explained on Step #7
* Go to <https://developer.apple.com/> and login with your credentials.
* In the **Overview** section, select **“Certificates, Identifiers & Profiles”**

[![ios-people-certs-appstoreconnect](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952382/a6b0958f9a2e843963da192b/ios-people-certs-appstoreconnect.png?expires=1781168400&signature=00788297eaf3e12769c96081acc8dcc4745eeca0c9a1b872ff3124f51043136f&req=fCAuH8x8noldFb4f3HP0gF0gVmE5Oxuk3I3TALPOiztrk%2B2cKy96bEJmKLjj%0AFPj%2BpD8Rjb8wyF%2FZcw%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952382/a6b0958f9a2e843963da192b/ios-people-certs-appstoreconnect.png?expires=1781168400&signature=00788297eaf3e12769c96081acc8dcc4745eeca0c9a1b872ff3124f51043136f&req=fCAuH8x8noldFb4f3HP0gF0gVmE5Oxuk3I3TALPOiztrk%2B2cKy96bEJmKLjj%0AFPj%2BpD8Rjb8wyF%2FZcw%3D%3D%0A)

## Certificates, Identifies & Profiles

Press the blue “+” button to add a new Certificate:

[![ios-certs-id-profiles](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952391/5956e7cfd1ed3563504b59fb/ios-certs-id-profiles.png?expires=1781168400&signature=389974228bd0d701939fb5b7ee08337c7b3a0d0753bdc709a80dceac2aaf5121&req=fCAuH8x8noheFb4f3HP0gLB5zFHOOfUONztVNs4%2FtPlCk14vfhi1QUVnO2fw%0AUjZHInMwFBqzbIoRXg%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952391/5956e7cfd1ed3563504b59fb/ios-certs-id-profiles.png?expires=1781168400&signature=389974228bd0d701939fb5b7ee08337c7b3a0d0753bdc709a80dceac2aaf5121&req=fCAuH8x8noheFb4f3HP0gLB5zFHOOfUONztVNs4%2FtPlCk14vfhi1QUVnO2fw%0AUjZHInMwFBqzbIoRXg%3D%3D%0A)

1. Search for “ **VoIP Services Certificate** ” and Click “ **Continue** ”:

   [![ios-voipservices-cert-desc](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952398/a3cd3f98e376a0ab815b9694/ios-voipservices-cert-desc.png?expires=1781168400&signature=3b6beba8f51830c53bdbc99e25140a1dd80c68fcea50d3f90085d96034f9aab1&req=fCAuH8x8nohXFb4f3HP0gFz50GZSTfRkgMlceBTf94%2BV8uFzRjIyFdcs2D1S%0AonI%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952398/a3cd3f98e376a0ab815b9694/ios-voipservices-cert-desc.png?expires=1781168400&signature=3b6beba8f51830c53bdbc99e25140a1dd80c68fcea50d3f90085d96034f9aab1&req=fCAuH8x8nohXFb4f3HP0gFz50GZSTfRkgMlceBTf94%2BV8uFzRjIyFdcs2D1S%0AonI%3D%0A)
2. Select the **BundleID** of the target application, and click “ **Continue** ”

   [![ios-create-voipservices-cert](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952410/c027c5f40a3553ad47150669/ios-create-voip-srv.png?expires=1781168400&signature=736d22292593468ff2e3bf56746c23e0330fbf15a1b8088021782fff52fa0668&req=fCAuH8x8mYBfFb4f3HP0gMGuUBqfWVqwIvQVnYrGnIVq%2FTFh3Tocw9az%2FwPV%0Abdw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952410/c027c5f40a3553ad47150669/ios-create-voip-srv.png?expires=1781168400&signature=736d22292593468ff2e3bf56746c23e0330fbf15a1b8088021782fff52fa0668&req=fCAuH8x8mYBfFb4f3HP0gMGuUBqfWVqwIvQVnYrGnIVq%2FTFh3Tocw9az%2FwPV%0Abdw%3D%0A)
3. Then, you will be requested to upload a CSR from your Mac.

   [![ios-create-voipservices-cert](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952411/9b027418e3e2e1575d79f765/ios-create-voipservices-cert.png?expires=1781168400&signature=67ef9a3179b359d1c6cd374d29f4653fe33245cf1b65f238b7e24b73539e28e6&req=fCAuH8x8mYBeFb4f3HP0gASVMQt97g2j%2FID%2FW8A3zIBghr8cAaqpmHAlGSYm%0AIuE%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952411/9b027418e3e2e1575d79f765/ios-create-voipservices-cert.png?expires=1781168400&signature=67ef9a3179b359d1c6cd374d29f4653fe33245cf1b65f238b7e24b73539e28e6&req=fCAuH8x8mYBeFb4f3HP0gASVMQt97g2j%2FID%2FW8A3zIBghr8cAaqpmHAlGSYm%0AIuE%3D%0A)

## Generate CSR

In order to generate a CSR:

a. Open the KeyChain Access of your mac.

b. Go to Keychain Access >> Certificate Assistance > Request a Certificate from a Certificate Authority.

[![ios-export-voipservices-request](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952416/aae5ca08a29dd9cc5aa87d64/ios-request-cert-keychain.png?expires=1781168400&signature=1b5c13ea409c9b1e76e4b78b0168f773f2aca2062cd768913e39289e28ee6eef&req=fCAuH8x8mYBZFb4f3HP0gHthT5kY9z7zr%2FttWRxUsybOSY5zxVAs0qOly5TA%0ALPe7aIpldXGeZF%2Fc2A%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952416/aae5ca08a29dd9cc5aa87d64/ios-request-cert-keychain.png?expires=1781168400&signature=1b5c13ea409c9b1e76e4b78b0168f773f2aca2062cd768913e39289e28ee6eef&req=fCAuH8x8mYBZFb4f3HP0gHthT5kY9z7zr%2FttWRxUsybOSY5zxVAs0qOly5TA%0ALPe7aIpldXGeZF%2Fc2A%3D%3D%0A)

c. Add your email address and select “Save to disk” option, and click “**Continue**”

[![ios-cert-information](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952423/0f1cb89b57582f0612bc87f5/ios-cert-information.png?expires=1781168400&signature=892a4612ee4ab263f24ea8a74eb2dc52d754258fc634b27b94c5466e7d835a33&req=fCAuH8x8mYNcFb4f3HP0gNmxNGj3zVlyZkQrbOAIlyc8LCcHoJ0y6LU7F%2FDR%0AkaCzTKqtJaKDgGahGw%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952423/0f1cb89b57582f0612bc87f5/ios-cert-information.png?expires=1781168400&signature=892a4612ee4ab263f24ea8a74eb2dc52d754258fc634b27b94c5466e7d835a33&req=fCAuH8x8mYNcFb4f3HP0gNmxNGj3zVlyZkQrbOAIlyc8LCcHoJ0y6LU7F%2FDR%0AkaCzTKqtJaKDgGahGw%3D%3D%0A)

d. Save the Certificate Signing Request (CSR) into your Mac.

[![ios-save-csr](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952428/9d585d19bfef8fe0a3e3d831/ios-save-csr.png?expires=1781168400&signature=7c9eec7462f652ee9f90e227ac6bdf4e57076f1bde12832e4f3c83f764a61d6c&req=fCAuH8x8mYNXFb4f3HP0gCZmfnRCZfgEdK4ckiMkxSiqe%2FJKpurnZegecwIw%0Ac2DoFkGWN2Y7i4IVIA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952428/9d585d19bfef8fe0a3e3d831/ios-save-csr.png?expires=1781168400&signature=7c9eec7462f652ee9f90e227ac6bdf4e57076f1bde12832e4f3c83f764a61d6c&req=fCAuH8x8mYNXFb4f3HP0gCZmfnRCZfgEdK4ckiMkxSiqe%2FJKpurnZegecwIw%0Ac2DoFkGWN2Y7i4IVIA%3D%3D%0A)

## Download Certificate

1. Once you have created your CSR, press “Choose File” and select the certSign created on step #7. Click “ **Continue** ” and you are done.

   [![ios-create-voipservices-cert](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952434/af01597791f37ae4cb0af625/ios-create-voipservices-cert.png?expires=1781168400&signature=eb6496ee1bdeae8613df7bd91acec8171792a9016ec70ff317ef2aeb2660c456&req=fCAuH8x8mYJbFb4f3HP0gJ4UyALeAJmr0mV7Hw6g7bTOZ0ojldFmFKyzFW%2Fh%0Aynw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952434/af01597791f37ae4cb0af625/ios-create-voipservices-cert.png?expires=1781168400&signature=eb6496ee1bdeae8613df7bd91acec8171792a9016ec70ff317ef2aeb2660c456&req=fCAuH8x8mYJbFb4f3HP0gJ4UyALeAJmr0mV7Hw6g7bTOZ0ojldFmFKyzFW%2Fh%0Aynw%3D%0A)
2. The new Certificate has been created. Now you need to download it:

   [![ios-download-cert](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952439/b349734e4924f9b8b48abe9b/ios-download-cert.png?expires=1781168400&signature=b7f1aaaca8818d2b9b632ef7c510a1bea3601b0f9afb1ca2ee719128614ea900&req=fCAuH8x8mYJWFb4f3HP0gOvff9NwKwdFK%2BRG%2F9%2Bgy90Qwv4YoJGH57YE74ri%0AbTg%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952439/b349734e4924f9b8b48abe9b/ios-download-cert.png?expires=1781168400&signature=b7f1aaaca8818d2b9b632ef7c510a1bea3601b0f9afb1ca2ee719128614ea900&req=fCAuH8x8mYJWFb4f3HP0gOvff9NwKwdFK%2BRG%2F9%2Bgy90Qwv4YoJGH57YE74ri%0AbTg%3D%0A)
3. Search for the downloaded file (usually named voip\_services.cer) and double click on it to install it on your Mac. And that’s all for now!

## Obtain your Cert.pem and Key.pem files

In order to allow the Telnyx VoIP push service to send notifications to your app, you will need to export the VoIP certificate and key:

1. Open Keychain Access on your Mac (where you have installed the VoIP certificate by following the “ **Creating a VoIP push certificate** ” instructions).
2. Search for “VoIP services” and verify that you have the certificate installed for the BundleID of your application.

   [![ios-keychain-access](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952449/f486216fddc2de8a77f300d3/ios-keychain-access.png?expires=1781168400&signature=5253194a0148ea66b89ee0918b84acf24afdf86ebab925ad2ed1943237ec1f40&req=fCAuH8x8mYVWFb4f3HP0gO8sEey95s%2BW9WEwZ6TbMIZbvlc%2FS29KxF579MKB%0Asnw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952449/f486216fddc2de8a77f300d3/ios-keychain-access.png?expires=1781168400&signature=5253194a0148ea66b89ee0918b84acf24afdf86ebab925ad2ed1943237ec1f40&req=fCAuH8x8mYVWFb4f3HP0gO8sEey95s%2BW9WEwZ6TbMIZbvlc%2FS29KxF579MKB%0Asnw%3D%0A)
3. Open the contextual menu and select “Export”:

   [![ios-export-voipservices](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952462/c4138e1a4c8ebc4af5bacf91/ios-export-voipservices.jpg?expires=1781168400&signature=2afb1c4f8f2e7a17648db4b9a3d6dad3bc0b1cfe8ec0b683e5c44494f10bf348&req=fCAuH8x8mYddFb4f3HP0gJaeyeE4vcAI1hymqS5ss1pIAy%2BDy2v67mHpogdw%0An98%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952462/c4138e1a4c8ebc4af5bacf91/ios-export-voipservices.jpg?expires=1781168400&signature=2afb1c4f8f2e7a17648db4b9a3d6dad3bc0b1cfe8ec0b683e5c44494f10bf348&req=fCAuH8x8mYddFb4f3HP0gJaeyeE4vcAI1hymqS5ss1pIAy%2BDy2v67mHpogdw%0An98%3D%0A)
4. Save the .p12 file (A password will be requested before saving it):

   [![ios-save-certificate](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952471/d0f49421390132a118352167/ios-save-certificate.jpg?expires=1781168400&signature=bb07ec53032e694a494cbf08f425560000bb14d0759e684635e1b7608c2f8f92&req=fCAuH8x8mYZeFb4f3HP0gOR%2B%2FccPl3NXhSTng8EFgSrunf634GzC2Mf2HiaD%0A314%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952471/d0f49421390132a118352167/ios-save-certificate.jpg?expires=1781168400&signature=bb07ec53032e694a494cbf08f425560000bb14d0759e684635e1b7608c2f8f92&req=fCAuH8x8mYZeFb4f3HP0gOR%2B%2FccPl3NXhSTng8EFgSrunf634GzC2Mf2HiaD%0A314%3D%0A)
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

   [![ios-api-keys-pn](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952478/d25b8cde799b6ccabb9a11d9/ios-api-keys-pn.jpg?expires=1781168400&signature=b69ca95a6428e0e446f3653a9e28d5b7019fb1aeae879c281e6e68c2d7be64bd&req=fCAuH8x8mYZXFb4f3HP0gCHzvQ4Pw7Im1xM%2BQULRUZw8ZoR%2BI%2FIblCSslE%2B%2B%0AMbQ%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952478/d25b8cde799b6ccabb9a11d9/ios-api-keys-pn.jpg?expires=1781168400&signature=b69ca95a6428e0e446f3653a9e28d5b7019fb1aeae879c281e6e68c2d7be64bd&req=fCAuH8x8mYZXFb4f3HP0gCHzvQ4Pw7Im1xM%2BQULRUZw8ZoR%2BI%2FIblCSslE%2B%2B%0AMbQ%3D%0A)
4. Set a credential name (You can use your app bundle ID to easy identify your PN credential) and then copy and paste the contents of your **cert.pem** and **key.pem** files into the defined sections (Notice that you need to copy from ---BEGIN ####--- to ---END--- sections including those marks):

   [![ios-add-pn](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952481/71b24524974caf7f8c5e55d6/ios-add-pn.jpg?expires=1781168400&signature=604579da55acace7216a186d7b2ffd1d7e652e790158607f774376d0668150e5&req=fCAuH8x8mYleFb4f3HP0gCuRYlLf4OTgJhw7nuegO2dQxL61DNlOiCJSicsX%0AxK4%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952481/71b24524974caf7f8c5e55d6/ios-add-pn.jpg?expires=1781168400&signature=604579da55acace7216a186d7b2ffd1d7e652e790158607f774376d0668150e5&req=fCAuH8x8mYleFb4f3HP0gCuRYlLf4OTgJhw7nuegO2dQxL61DNlOiCJSicsX%0AxK4%3D%0A)
5. Save the new push credential by pressing the **Add Push Credential** button.

## Assign your iOS Push Credential to a SIP Connection:

1. Go to the **SIP Connections** section on the left panel.
2. Open the Settings menu of the SIP connection that you want to add a Push Credential or [create a new SIP Connection](https://portal.telnyx.com/#/voice/connections) .
3. Select the WEBRTC tab.
4. Go to the iOS Section and select the PN credential created on “ **Create an iOS Push Credential** ”

[![ios-select-pn](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952488/fb43824094b87c329326a69b/ios-select-pn.png?expires=1781168400&signature=d4accf3c2689f0893db55e9591a1c2ec5da2af57dc7d822a63c0c0a80d8a42f5&req=fCAuH8x8mYlXFb4f3HP0gGG6elHDCkr8yHwiHY8l4yoV8Gou%2BMxH0oEDLDC3%0ACjy7Yp9CNLjxaV0G5w%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809952488/fb43824094b87c329326a69b/ios-select-pn.png?expires=1781168400&signature=d4accf3c2689f0893db55e9591a1c2ec5da2af57dc7d822a63c0c0a80d8a42f5&req=fCAuH8x8mYlXFb4f3HP0gGG6elHDCkr8yHwiHY8l4yoV8Gou%2BMxH0oEDLDC3%0ACjy7Yp9CNLjxaV0G5w%3D%3D%0A)

That’s done. You can now go to your code and start implementing **PushKit** and **Callkit** using the **TelnyxRTC SDK** and receive VoIP push notifications into your iOS device.

Did this answer your question?

😞😐😃

Table of contents
