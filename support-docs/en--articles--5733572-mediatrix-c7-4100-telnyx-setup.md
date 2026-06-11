---
source_url: https://support.telnyx.com/en/articles/5733572-mediatrix-c7-4100-telnyx-setup
scraped: 2026-06-11
---

Mediatrix C7/4100: Telnyx Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Mediatrix C7/4100: Telnyx Setup

Learn how to connect and configure your Mediatrix C7 or Mediatrix 4100 to work with your Telnyx Mission Control Portal.

C

Written by Customer Success

June 6, 2024

Table of contents

[Jump to Instructions](#h_3ae36cf660)

The [Mediatrix C7 Series gateways](https://documentation.media5corp.com/pages/viewpage.action?pageId=16547905) combine a VoIP Analog Adaptor and Media Gateway in both a secure and reliable platform. They feature a FXS, FXO, and BRI interfaces while still hitting a very cost-effective price point, delivering a simple-setup and transparent connection to PSTN and analog terminals.

|  |
| --- |
| ***Note:*** *While this document uses the Mediatrix C7 setup as an example, the setup criteria for the 4100 should be the same. Where any differences exist, this document will call it out.* |

Further documentation:

* <https://documentation.media5corp.com/pages/viewpage.action?pageId=16547905> - Mediatrix C7 technical documentation

---

# Instructions for configuring Mediatrix C7/4100 to work with your Telnyx Mission Control Portal

In this document, you will:

1. [Connect your Mediatrix device to your network](#h_551f05d9d8)
2. [Access the Mediatrix GUI](#h_b693b7e47d)
3. [Set the Telnyx server FQDN](#h_e85191689a)
4. [Restart all required services](#h_3a643db00c)
5. [Register telephony ports](#h_c2a49e6d16)
6. [Set the Telnyx credentials on new telephony ports](#h_ca254f6f5d)
7. [Set auto-routing to support the Telnyx username format](#h_1ce65d73eb)
8. [Disable the G.711 a-law codec (*North America only*)](#h_d622167dc2)
9. [Set dial patterns (DTMF maps)](#h_016aa39444)
10. [Set a time server](#h_60f8910ea6)

**Video Walkthrough**

Coming soon! Check back frequently as we are updating our documentation.  
​  
​

**Pre-Requisites**

* It is STRONGLY recommended that your device has the latest firmware updates:

  + [Download latest](https://documentation.media5corp.com/display/DGWLATEST/Latest+DGW)
* You have a [number](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) in your account.
* You have [configured a connection.](https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection)
* You have [assigned that number to the connection.](https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection)
* You have [configured an outbound profile.](https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles)
* You have assigned your connection to the outbound profile.

## 1. Connect your Mediatrix device to your network

In this step, you'll establish a hard wired connection between your Mediatrix C7/4100 device to your network.

1. Find the ethernet ports on your device (The C7 and 4100 both have 2):

   * Connect your device to your router/network via the **ETH1** (**WAN** on the 4100) ethernet port. It is already set to get an IP address from a DHCP server.
   * Find the **ETH2** (**LAN** on the 4100) ethernet port. It has a default IP address of 192.168.1.2 and is used to directly manage your device through a web browser.
2. Check the Power LED light.

   1. If the light is **ON**, you can now connect a phone to one of the telephony ports and dial **\*#\*0** and the device will play back the IP address the device has. Take note of this, as you'll need it in the next step.
   2. If the light is **OFF**, perform the following initial troubleshooting steps before calling for any additional help, as the following are usually the most likely culprits:

      1. Ensure the network cable is properly connected between your device and your network gateway.
      2. Ensure that the port on your router/network switch is active.
      3. If the first two steps don't solve the problem, connect your device to your computer through the **ETH2/LAN** port.

[Back to Top](#h_3ae36cf660)

## 2. Access the Mediatrix GUI

In this step, you'll access the configuration settings by connecting to your device via a web browser and ensure you can log in.

1. From a computer connected (via ethernet or wifi) to the same network as your Mediatrix, open your preferred web browser.
2. Enter the IP address you obtained in step 1.1 to reach the Mediatrix GUI login page.

For your first login, you'll need to use the Mediatrix default login:

1. Username: public
2. Password: (empty - no default password)

[![Mediatrix default login. ](https://downloads.intercomcdn.com/i/o/419078170/ef926fa424a0d0bc52c174c5/Mediatrix.jpeg?expires=1781168400&signature=385d9baab1491b7fc8e50ede503831808fd61099e16b957f325087d4d2ad7697&req=cCEuFs52nIZfFb4f3HP0gIWzWWjvstXlBjeG63iU8VBH3Y0GgGogTNBvNg3H%0A4yy8fy70K8ZwiFQvKQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/419078170/ef926fa424a0d0bc52c174c5/Mediatrix.jpeg?expires=1781168400&signature=385d9baab1491b7fc8e50ede503831808fd61099e16b957f325087d4d2ad7697&req=cCEuFs52nIZfFb4f3HP0gIWzWWjvstXlBjeG63iU8VBH3Y0GgGogTNBvNg3H%0A4yy8fy70K8ZwiFQvKQ%3D%3D%0A)

[Back to Top](#h_3ae36cf660)

## 3. Set the Telnyx server FQDN

In this step, you're going to set the Fully Qualified Domain Name (FQDN) so the device knows to connect to Telnyx.

1. Once you're logged into your Mediatrix GUI, click on **SIP** in the top menu.
2. Click on the **Servers** sub-menu.
3. Find the **Registrar Host** field and enter the registrar FQDN associated with your account (i.e.: sip.telnyx.com).
4. In the **Proxy Host** field, enter the proxy FQDN associated with your account (i.e.: sip.telnyx.com)
5. Click **Apply**.

   [![Mediatrix Telnyx server FQDN. ](https://downloads.intercomcdn.com/i/o/419103627/b90ee8e9bfbfa2dffb82bd3d/Mediatrix_SIP_servers_menu.png?expires=1781168400&signature=2df5d52bdb381bafafbc8433acb650cde7c0c03286ba22930f5bbc260cde3f2e&req=cCEuF8l9m4NYFb4f3HP0gPcWIH4RKTh%2BB8g9at5vzw60o48srqPd%2FuTYkdcF%0AHuE%3D%0A)](https://downloads.intercomcdn.com/i/o/419103627/b90ee8e9bfbfa2dffb82bd3d/Mediatrix_SIP_servers_menu.png?expires=1781168400&signature=2df5d52bdb381bafafbc8433acb650cde7c0c03286ba22930f5bbc260cde3f2e&req=cCEuF8l9m4NYFb4f3HP0gPcWIH4RKTh%2BB8g9at5vzw60o48srqPd%2FuTYkdcF%0AHuE%3D%0A)

[Back to Top](#h_3ae36cf660)

## 4. Restart required services

Once you've set the Telnyx servers in the previous step, you'll need to perform a services restart to apply changes.

1. After clicking **Apply** in the previous step, you'll get a message at the top of the screen telling you to restart required services. You'll have the option to either open the **Services Table** and do this manually, or just **Restart Required Services** from the link in the message.

   [![Restart Required Services section. ](https://downloads.intercomcdn.com/i/o/419108515/a8693db56aa2258e727a4a6e/Mediatrix_restart_services.png?expires=1781168400&signature=a61be8819174bd15386498066c012db7084675b20ceebae064f7d3952a82dfc4&req=cCEuF8l2mIBaFb4f3HP0gAlA6WMRh1v3bGJxQFgMnFH3JfJIZsIU5OlKe9yi%0AwXo%3D%0A)](https://downloads.intercomcdn.com/i/o/419108515/a8693db56aa2258e727a4a6e/Mediatrix_restart_services.png?expires=1781168400&signature=a61be8819174bd15386498066c012db7084675b20ceebae064f7d3952a82dfc4&req=cCEuF8l2mIBaFb4f3HP0gAlA6WMRh1v3bGJxQFgMnFH3JfJIZsIU5OlKe9yi%0AwXo%3D%0A)

[Back to Top](#h_3ae36cf660)

## 5. Register telephony ports

In this section, you'll enable all the analog ports you will be registering with this service.

1. Click on **SIP** in the top menu.
2. Click on the **Registrations** sub-menu.
3. For every analog port you want to register, provide the following information:

   1. **Username:** Enter the associated Telnyx username for your account or sub-account
   2. **Friendly Name:** This is your choice, and is the name that will be displayed when you make calls.
   3. **Register:** Enable
4. Click **Apply**.

   [![Registrations sub-menu in the SIP section. ](https://downloads.intercomcdn.com/i/o/419113143/110ba65791572ea9738ac3cb/Mediatrix_credentials_01.png?expires=1781168400&signature=bd83a0a25bab82fd7dd427a922ea7e72f7c04d6a7732a21237b7083ae837aaef&req=cCEuF8h9nIVcFb4f3HP0gEUGUnOkbM2vJVtaoxjbJ5lieFUiw2jxSL7ZkDfm%0A10c%3D%0A)](https://downloads.intercomcdn.com/i/o/419113143/110ba65791572ea9738ac3cb/Mediatrix_credentials_01.png?expires=1781168400&signature=bd83a0a25bab82fd7dd427a922ea7e72f7c04d6a7732a21237b7083ae837aaef&req=cCEuF8h9nIVcFb4f3HP0gEUGUnOkbM2vJVtaoxjbJ5lieFUiw2jxSL7ZkDfm%0A10c%3D%0A)

[Back to Top](#h_3ae36cf660)

## 6. Set the Telnyx Credentials

In this section, you'll set the Telnyx credentials for each of the telephony ports you just entered in step 5.

1. Click on **SIP** in the top menu.
2. Click on the **Authentications** sub-menu.
3. Click on **Edit All Entries** to open the telephony port entries for editing.
4. For each entry you've registered enter the following:

   1. **Criteria:** Endpoint
   2. **Endpoint:** Select the telephony port to register
   3. **Validate Realm:** Disable
   4. **Username:** Enter your Telnyx account/sub-account username.
   5. **Password:** Enter your telnyx account/sub account password.
5. Click **Apply & Refresh Registration**.

   [![Authentications sub-menu of the SIP domain. ](https://downloads.intercomcdn.com/i/o/419117538/a6befab44ace8534e89878e8/Mediatrix_credentials_02.png?expires=1781168400&signature=ad54525eb1af0eaaec3a25e1324748d576e145d4e68eabf70536abf67b0fef39&req=cCEuF8h5mIJXFb4f3HP0gEu%2FHZX%2FOedLaoXvcHFx5EfUXOB%2Bfkn7PMP8ZBAg%0Aqm8%3D%0A)](https://downloads.intercomcdn.com/i/o/419117538/a6befab44ace8534e89878e8/Mediatrix_credentials_02.png?expires=1781168400&signature=ad54525eb1af0eaaec3a25e1324748d576e145d4e68eabf70536abf67b0fef39&req=cCEuF8h5mIJXFb4f3HP0gEu%2FHZX%2FOedLaoXvcHFx5EfUXOB%2Bfkn7PMP8ZBAg%0Aqm8%3D%0A)

[Back to Top](#h_3ae36cf660)

## 7. Set auto-routing to support the Telnyx username format

Now you'll set the criteria for auto-routing to ensure your system is set up to use SIP.

1. Click on **Call Router** in the top menu.
2. Click on **Auto-routing** in the submenu.
3. In the settings you see, set the following configurations:

   1. **Auto-routing:** Enable
   2. **Criteria Type:** SIP Username
4. Click **Apply**.

   [![Call Router domain. ](https://downloads.intercomcdn.com/i/o/419120345/c78bde584110c62bfd94611b/Mediatrix_Call_Router_01.png?expires=1781168400&signature=1c8f888871df1cace3644e1542adb8665f9ab0b26d3c3732ce3f2cc90aeac696&req=cCEuF8t%2BnoVaFb4f3HP0gAQeSloCPnWD%2F%2Fag5I8yx2iVllr7g4JA0ey6W9Q5%0Aiwc%3D%0A)](https://downloads.intercomcdn.com/i/o/419120345/c78bde584110c62bfd94611b/Mediatrix_Call_Router_01.png?expires=1781168400&signature=1c8f888871df1cace3644e1542adb8665f9ab0b26d3c3732ce3f2cc90aeac696&req=cCEuF8t%2BnoVaFb4f3HP0gAQeSloCPnWD%2F%2Fag5I8yx2iVllr7g4JA0ey6W9Q5%0Aiwc%3D%0A)
5. In order to validate that your call router is set correctly, click on the **Status** sub-menu (in the **Call Router** menu).
6. Find the **Route** table (under the **Type** column) and make sure auto routes are present and configured as expected.

   [![Routing status for modified configurations. ](https://downloads.intercomcdn.com/i/o/419123572/472dec0e764492581271bf6a/Mediatrix_Call_Router_02.png?expires=1781168400&signature=9da871116be9dcf01dd332deab6b42a1b232a5715825324415627902c12fb8fe&req=cCEuF8t9mIZdFb4f3HP0gPsrIldYHCSBJtwnFLd5zZzSCvmyPyc5ueK3kd8A%0ALlY%3D%0A)](https://downloads.intercomcdn.com/i/o/419123572/472dec0e764492581271bf6a/Mediatrix_Call_Router_02.png?expires=1781168400&signature=9da871116be9dcf01dd332deab6b42a1b232a5715825324415627902c12fb8fe&req=cCEuF8t9mIZdFb4f3HP0gPsrIldYHCSBJtwnFLd5zZzSCvmyPyc5ueK3kd8A%0ALlY%3D%0A)

[Back to Top](#h_3ae36cf660)

## 8. Disable G.711 a-law codec (*North America only*)

If you're in North America or Japan, you'll want to disable the G.711 a-law codec, as Mu-law (also written µ-Law) is the encoding scheme for voice traffic in these regions. Once you've disabled this codec, you'll configure the µ-Law codec.

1. Click on **Media** in the top menu.
2. Click on the **Codecs** sub-menu.
3. Find **G.711 a-law** and **disable** for both **Voice** and **Data**.
4. Click **Apply**.

   [![Media in the top menu. ](https://downloads.intercomcdn.com/i/o/419129900/4072978b62391e60588195b1/Mediatrix_Codecs_Setup.png?expires=1781168400&signature=7e245818c9c6dde638ebbbf0b30da43a4b8ac170c4ad4822cbf21731dbb0de11&req=cCEuF8t3lIFfFb4f3HP0gADrUYq8qIA%2F6%2BM%2B5G36gUF2Dhq%2Fm2eLlCTr0J8h%0AJH8%3D%0A)](https://downloads.intercomcdn.com/i/o/419129900/4072978b62391e60588195b1/Mediatrix_Codecs_Setup.png?expires=1781168400&signature=7e245818c9c6dde638ebbbf0b30da43a4b8ac170c4ad4822cbf21731dbb0de11&req=cCEuF8t3lIFfFb4f3HP0gADrUYq8qIA%2F6%2BM%2B5G36gUF2Dhq%2Fm2eLlCTr0J8h%0AJH8%3D%0A)
5. Perform a [services restart](#h_3a643db00c).
6. Next, find the G.711 µ-Law and click the pencil icon under the **Advanced** column.
7. A new window will open.
8. Find the **Minimum and Maximum Packetization time** ("ptime") fields and set the following configurations:

   1. **Minimum Packetization:** 20ms
   2. **Maximum Packetization:** 30ms
9. Click **Apply**.

   [![Minimum and Maximum Packetization time of the u-Law section. ](https://downloads.intercomcdn.com/i/o/419134942/f475aba4aa270f6ec98a1638/Ptime.jpeg?expires=1781168400&signature=e9ce76023cb4d635737b2e3effbee411275bd3e9b7fec592c157e8601a31d552&req=cCEuF8p6lIVdFb4f3HP0gCWfCB%2BvezVJCm4n2ZqAb9TJXa76WD3IRxUaz8FR%0Args%3D%0A)](https://downloads.intercomcdn.com/i/o/419134942/f475aba4aa270f6ec98a1638/Ptime.jpeg?expires=1781168400&signature=e9ce76023cb4d635737b2e3effbee411275bd3e9b7fec592c157e8601a31d552&req=cCEuF8p6lIVdFb4f3HP0gCWfCB%2BvezVJCm4n2ZqAb9TJXa76WD3IRxUaz8FR%0Args%3D%0A)

[Back to Top](#h_3ae36cf660)

## 9. Set dial patterns (DTMF maps)

In this section, you'll change your [DTMF](https://support.telnyx.com/en/articles/1130710-what-is-dtmf) maps settings in order to use standard star codes/feature codes, such as \*97 (voicemail).

1. Click on **Telephony** in the top menu.
2. Click on **DTMF Maps** in the sub-menu.
3. In the table on this page, find the second row and configure the following:

   1. **DTMF Map:** \*xx
   2. **Transformation:** x

   [![Telephony in the top menu section.](https://downloads.intercomcdn.com/i/o/419139289/7c2f9291ae034d83b9375dbf/MtxDtmf.png?expires=1781168400&signature=80273f729b30efec15c29633cc2c7405533b55a635e325ea7fa2bb36f18de1cb&req=cCEuF8p3n4lWFb4f3HP0gM8EAw%2Btt64%2BPoXA0MIQ9XFlLdnQuwx1dJLd%2Bl7w%0A%2Fqo%3D%0A)](https://downloads.intercomcdn.com/i/o/419139289/7c2f9291ae034d83b9375dbf/MtxDtmf.png?expires=1781168400&signature=80273f729b30efec15c29633cc2c7405533b55a635e325ea7fa2bb36f18de1cb&req=cCEuF8p3n4lWFb4f3HP0gM8EAw%2Btt64%2BPoXA0MIQ9XFlLdnQuwx1dJLd%2Bl7w%0A%2Fqo%3D%0A)
4. Click **Apply**.

[Back to Top](#h_3ae36cf660)

## 10. (OPTIONAL) Set a time server

This section may not be required, but if your DHCP server doesn't also provide an SNTP server, this section will allow you to configure it manually.

1. Click on **Network** in the top-menu.
2. Click on **Host** in the sub-menu.
3. Find the **SNTP Configuration** table and configure the following settings:

   1. **SNTP Configuration Source:** Static
   2. **Primary SNTP:** *pool.ntp.org* (Or any known and reachable SNTP server)

   [![Time server settings interface. ](https://downloads.intercomcdn.com/i/o/419142009/2ad0afb61e904c7462f3df6c/Mediatrix_SNTP_Server.png?expires=1781168400&signature=8f235f13d551a5a4e8ebc3afbb7aee0e6968bc4990e2c6c5d06f01c34d52ca8a&req=cCEuF818nYFWFb4f3HP0gLszt%2BrEoXJ4Mw1IKmqlfCbo%2Fv64TJdmCZgLpVLD%0A9CY%3D%0A)](https://downloads.intercomcdn.com/i/o/419142009/2ad0afb61e904c7462f3df6c/Mediatrix_SNTP_Server.png?expires=1781168400&signature=8f235f13d551a5a4e8ebc3afbb7aee0e6968bc4990e2c6c5d06f01c34d52ca8a&req=cCEuF818nYFWFb4f3HP0gLszt%2BrEoXJ4Mw1IKmqlfCbo%2Fv64TJdmCZgLpVLD%0A9CY%3D%0A)
4. Click **Apply**.

That's it, you've now completed the configuration of your Mediatrix C7/4100 device.  
​

[Back to Top](#h_3ae36cf660)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Check out the [Mediatrix](https://documentation.media5corp.com/pages/viewpage.action?pageId=16547905) technical documentation.

---

Related Articles

[Zoiper 5 Pro: Telnyx Setup](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup)[Flyingvoice: Telnyx Setup](https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup)[Panasonic KX-HDV: Telnyx setup](https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)

Did this answer your question?

😞😐😃

Table of contents
