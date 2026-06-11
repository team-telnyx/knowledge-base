---
source_url: https://support.telnyx.com/en/articles/5822901-vtech-vcs754-telnyx-setup
scraped: 2026-06-11
---

Vtech VCS754: Telnyx Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Vtech VCS754: Telnyx Setup

Learn how to configure the Vtech VCS754 ErisStation with Telnyx for enhanced conference calling experiences.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_56aed7a079)

The "Vtech VCS754 ErisStation" conference phone features a compact, all-in-one design makes it easy to keep everything together—no clutter, no hassle. Built-in charging stations with magnetic bays ensure the microphones are charged and available for the next meeting.

Every Eristation conference phone comes with portable DECT 6.0 microphones with Orbitlink Wireless Technology.

Additional documentation:

* [Administrator and provisioning manual](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754_Admin_Provisioning_Manual%20-%20Rev%204.pdf)
* [User manual](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754_User_Guide%20-%20Rev%204.pdf)
* [Quick start guide](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754_QSG%20-%20Rev%203.pdf)
* [Quick start guide](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754-WM_QSG%20-%20Rev%203.pdf) (WM version of device)
* [Vtech product support](https://www.vtechphones.com/support/technical-support)

---

# Instructions for configuring the Vtech VCS754 ErisStation conference phone

In this activity you will:

1. [Get your device's IP address and log into the web portal](#h_7cf26709da)
2. [Configure your VCS754 conference phone](#h_c6f602a629)
3. [Configure signaling settings](#h_7845ccb0eb)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for VCS754 ErisStation/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Get your device's IP address and log into the web portal

In this step, you'll obtain the IP address from your D7xx, which you'll need to log into the web portal in the next step.

1. Click on the **Menu** button of the phone.
2. Scroll down and select **Status** and from here, select **Network** . You can find the IP address here. Take note of it. You'll need it for the next step.
3. From a computer on the same network as the phone, open a web browser and enter *http://* followed by the IP address you just obtained into the browser's address bar.
4. You'll be asked to log in. Out of the box, the default credentials are:

   1. **User:** *admin*
   2. **Password:** *admin*

[Back to Top](#h_56aed7a079)

## 2. Configure your VCS754 conference phone

In this step, you'll create a [SIP trunk](https://telnyx.com/products/sip-trunks) and connect your phone to Telnyx.

1. Click on the **System** tab at the top of the page.
2. Use the left-hand navigation to select the account you want to configure. Click on it to open the editor.
3. Find the **General Account Settings** section and provide the following information:

   1. **Account Label:** Give this a name that makes sense for you.
   2. **Display Name**: This is your caller ID. You can choose whatever you like, but keep in mind the following naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   3. **User Identifer**: Your Telnyx account ID
   4. **Authentication Name**: Your Telnyx account ID
   5. **Authentication Password**: Your Telnyx account password
   6. **Dial Plan**: x+P (By default)
4. Find the **SIP Server** section and provide the following information:

   1. **Server Address**: *sip.telnyx.com*
   2. **Port**: *5060* if you have not enabled TLS encryption. If you have, choose *5061*.
5. Use the same values you entered in step 4 in the **Registration**, **Outbound Proxy**, **Backup Outbound Proxy** sections.

   [![Registration, Outbound Proxy, Backup Outbound Proxy sections.](https://downloads.intercomcdn.com/i/o/436123065/4b8452642eaa5d64df18f3ee/1.png?expires=1781168400&signature=b17e56eca9d9a06c05b54c01a44d2f280e00a6a73fb0647470c3f48e28df2cdc&req=cCMhF8t9nYdaFb4f3HP0gJjq0I5uTrcZn8SNzpA8ZKkrq%2BGU5fQzfFzWrQJQ%0A%2FqY%3D%0A)](https://downloads.intercomcdn.com/i/o/436123065/4b8452642eaa5d64df18f3ee/1.png?expires=1781168400&signature=b17e56eca9d9a06c05b54c01a44d2f280e00a6a73fb0647470c3f48e28df2cdc&req=cCMhF8t9nYdaFb4f3HP0gJjq0I5uTrcZn8SNzpA8ZKkrq%2BGU5fQzfFzWrQJQ%0A%2FqY%3D%0A)
6. Find the Audio section and provide the following information:

   1. Ringer Tone: Choose the one you prefer
   2. **Codec Priority** fields: Set your codecs in priority sequence that meets your needs.   
      ​  
      Telnyx supports the following codecs:

      1. ulaw(g711u)
      2. alaw(g711a)
      3. g722
      4. g729
   3. **Enable Voice Encryption (SRTP):** Check the box *IF you are using TLS/encryption*

      [![Audio section](https://downloads.intercomcdn.com/i/o/436128646/1643e4464aa55760cdbdab9c/2.png?expires=1781168400&signature=36e649b239a09a5df016fe0dcce348640f3f09a7ac7e928452632e9bbd54b765&req=cCMhF8t2m4VZFb4f3HP0gJ34Crl1%2FqowrCS8i5a9gXRvMuey9Bu1arSseODR%0AuZc%3D%0A)](https://downloads.intercomcdn.com/i/o/436128646/1643e4464aa55760cdbdab9c/2.png?expires=1781168400&signature=36e649b239a09a5df016fe0dcce348640f3f09a7ac7e928452632e9bbd54b765&req=cCMhF8t2m4VZFb4f3HP0gJ34Crl1%2FqowrCS8i5a9gXRvMuey9Bu1arSseODR%0AuZc%3D%0A)

[Back to Top](#h_56aed7a079)

## 3. Configure signaling settings

In this section, we'll set the port and transport protocol for the account.

1. Click on the **System** tab at the top of the page.
2. Use the left-hand navigation to select **Signaling Settings** and enter the following information:

   1. **Local SIP Port**: *5060* if you have not enabled TLS encryption. If you have, choose *5061*.
   2. **Transport**: *UDP* or *TCP* if you have not enabled TLS encryption. If you have, choose *TLS/TCP*.

That's it! You've finished configuring your Vtech VCS754 profile, and can now start testing calls!

[Back to Top](#h_56aed7a079)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Administrator and provisioning manual](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754_Admin_Provisioning_Manual%20-%20Rev%204.pdf)
* [User manual](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754_User_Guide%20-%20Rev%204.pdf)
* [Quick start guide](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754_QSG%20-%20Rev%203.pdf)
* [Quick start guide](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754-WM_QSG%20-%20Rev%203.pdf) (WM version of device)
* [Vtech product support](https://www.vtechphones.com/support/technical-support)

---

---

Related Articles

[Panasonic KX-HDV: Telnyx setup](https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)[Snom C520: Telnyx Setup](https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup)[Konftel 300IPx: Telnyx Setup](https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup)[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)

Did this answer your question?

😞😐😃

Table of contents
