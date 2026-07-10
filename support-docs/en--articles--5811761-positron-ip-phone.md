---
source_url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
scraped: 2026-07-08
content_hash: 14fec6187162c602b6ebf6c5e0fce06ad450812c422ce4a20eabbd29067bb4e9
---

Positron IP Phone | Telnyx Help Center

[Skip to main content](#main-content)

# Positron IP Phone

Step-by-step guide to set up Positron IP phones with Telnyx. From obtaining the IP address to configuring SIP profiles: smooth communication

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_5644abe804)

The Positron line of IP Phones is a SIP phone with wideband audio support, dual Ethernet port and integrated Power over Ethernet. It is an option that is impressive, yet affordable. All the IP Phones are optimized for executives, administrative assistants and those working with bandwidth-intensive applications on collocated PCs. Line keys can also be configured as IP PBX features such as BLF, SCA, Intercom, Call Pickup, Call Park and many others. The high resolution screen and the HD voice features provide a high quality visual and authentic audio experience.

|  |
| --- |
| ***Note:*** *Aside from minor cosmetic UI differences, the configuration steps across Positron IP phones are identical. Therefore this document supports the configuration of the following Positron models:*  * *IP304/IP304C* * *IP408/IP408C* * *IP410C/IP410G* |

Additional documentation:

* Positron IP phone comparison
* Positron's IP PBX brochure
* Device warranty information
* Positron sales and support
* User manuals for:

  + IP304
  + IP304C
  + IP408
  + IP410C
  + IP410G

---

# Instructions for configuring your Positron IP304 phone

In this activity you will:

1. [Get your IP304's IP address and log into the web portal](#h_acbb4e0133)
2. (either) [Configure your SIP profile on the Positron web portal](#h_06d5d66263)
3. (or) [Configure your SIP profile from your phone](#h_da178fbbbc)
4. (OPTIONAL) [Import a TLS certificate](#h_8a6037d1bb)
5. (RECOMMENDED) [Change the default admin login credentials](#h_bfc52bc2b4)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Positron IP304 phone/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Get your IP304's IP address and log into the Positron web portal

In this step, you'll obtain the IP address from your IP304, which you'll need to log into the web portal in the next step.

1. From your phone, tap the **Menu** button on your phone and select **Status > Information** to see your IP address. Take note of this.

   ![Status &gt; Information section. ](_images/3d56dfaae0cdda0f.png)
2. From your computer, open a web browser and enter the IP address of your device that you obtained in [Step 1](https://support.telnyx.com/en/articles/5810226-fortifone-fon-570#h_2a7d29498d) into your address bar. Prepend with *http://*
3. Log into your device. The first time logging in, you'll use the default credentials (Don't forget to [change them after](#h_bfc52bc2b4)!)

   1. **Username:** *admin*
   2. **Password:** *admin*

   ![Version section.](_images/edd7ebaf4e7422dc.png)

[Back to Top](#h_5644abe804)

## 2. (either) Configure your SIP profile on the Positron web portal

In this step, you will set up your device and register it with Telnyx.

1. From your web portal, click on **Account** in the top navigation.
2. Click **Basic** in the left-hand nav and enter the following information:

   1. **Account:** Choose from the dropdown (likely *Account 1* unless other accounts have already been configured. In which case choose the one you're looking to set up.)
   2. **Account Active:** Select *Yes* to enable your account upon creation.
   3. **Primary SIP Server:** *sip.telnyx.com*
   4. **SIP Transport:** *UDP* (default).   
      ​  
      ​**Note that** if you are planning to encrypt calls and have [set up call encryption on your Telnyx portal](https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120#h_e14c90ac20), you should choose *TLS*.  
      ​
   5. **SIP User ID:** Your Telnyx account ID
   6. **Authentication ID:** Your Telnyx account ID
   7. **Authentication Password:** Your Telnyx account password

   ![Account section of the web portal. ](_images/8560d4e9a0143626.png)
3. Hit **Save**.

[Back to Top](#h_5644abe804)

## 3. (or) Configure your SIP profile from your phone

In this step, you will set up your device and register it with Telnyx.

1. From your phone, tap the **Menu** button on your phone and select **Settings > Advanced Settings > Accounts**

   1. **Account:** Select the account you want (likely *Account 1* unless other accounts have already been configured. In which case choose the one you're looking to set up.)
   2. **Account Active:** Select *On* to enable your account upon creation.
   3. **Primary SIP Server:** *sip.telnyx.com*
   4. **Proxy SIP Server:** *sip.telnyx.com* or leave blank
   5. **SIP User ID:** Your Telnyx account ID
   6. **Authentication ID:** Your Telnyx account ID
   7. **Authentication Password:** Your Telnyx account password

   ![Advanced Settings in the Accounts section. ](_images/80af6d4a769f3ea4.png)

## 3. (OPTIONAL) Import a TLS certificate

In this step, you'll upload your TLS certificate if you're using one.

1. From your web portal, click on **Management** in the top navigation.
2. Click **TLS Certs** in the left-hand nav and upload your document here.

   ![Management section. ](_images/f821a29478eb6281.png)

## 4. (RECOMMENDED) Change your default admin login credentials

In this step, we'll change the default login credentials for your IP304, as it's a security risk to keep factory defaults as your login credentials.

1. From your phone, tap the **Menu** button on your phone and select **Settings > Advanced Settings > Password > Phone Settings > Set Password**.
2. Enter your current password, your new password, and enter your new password again in the **Confirm** field to confirm it.
3. Click **Save** or the checkmark to save your changes.

   ![Password settings section. ](_images/5f62c51e9e92b0dd.png)

That's it! You're all set up to start using your Positron IP304 phone with Telnyx.

[Back to Top](#h_5644abe804)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* Positron IP phone comparison
* Positron's IP PBX brochure
* Device warranty information
* Positron sales and support
* User manuals for:

  + IP304
  + IP304C
  + IP408
  + IP410C
  + IP410G

---

---

Related Articles

[Fanvil H2U: Compact IP](https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip)[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[Fanvil H3W/H5W: WiFi IP](https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip)[Fanvil H5: Hotel IP](https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)

Did this answer your question?

😞😐😃

Table of contents
