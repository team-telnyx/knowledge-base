---
source_url: https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx
scraped: 2026-06-11
---

Polycom: Setup with Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# Polycom: Setup with Telnyx

Learn how to configure the Polycom VVX 300-series IP phone with your Telnyx account.

C

Written by Customer Success

June 6, 2024

Table of contents

[Jump to Instructions](#h_0a78797f6f)

[Polycom](https://www.poly.com/us/en/products/phones/vvx/vvx-301-311) phones sport a sleek and professional design with high-quality construction, making them an attractive desktop option capable of handling the demands of everyday use. Featuring Polycom's Acoustic Clarity Technology and HD Voice, Polycom Phones enable you to experience clear, crisp, room filling conversations that result in increased comprehension and productivity.

Standard features include programmable buttons, call waiting/forwarding/hold, call directory and of course speakerphone. With phones available for the smallest of businesses all the way up to the largest, Polycom Phones are a great choice for a SIP-based IP Phone.

Additional documentation and resources:

* [Polycom support](https://support.hp.com/us-en/poly)
* Polycom VVX 300-series IP phone user guide

---

# Instructions for Configuring your Polycom VVX 300-series IP phone

In this activity you will:

1. [Get your device's IP address and log into the web portal](#h_77cd006102)
2. [Configure NTP settings](#h_cec992e83c)
3. [Configure SIP settings](#h_19b5b25512)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create an [IP-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Download Elastix 4 ISO from [our dropbox.](https://www.dropbox.com/sh/rzrdrpu0ocumu95/AABJeNgKkOkDCYLkSrsIuD3Aa?dl=0) (V4 is no longer available through the provider)

  + Take note of any username/password combination you set during this activity. You'll need them at a later stage.

**Video walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Polycom VVX 300-series/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Get your device's IP address and log into the web portal

In this section, you'll obtain your device's IP address from your phone and use it to log into the Polycom web portal so you can begin configuration.

1. Connect the phone to a network with a DHCP server and wait for it to boot to the main interface. This typically takes about 1-2 minutes. Depending on the firmware version the phone has your IP *may be* displayed once it boots.
2. If your IP address doesn't display on boot, you can access the current IP information by pressing the Home (Button) and going to **Settings > Status > Network > TCP/IP Parameters.** You'll find the IP address here.
3. Note your IP address and open a web browser (Chrome/Firefox recommended) and type <https://<phone> IP Address> into the address bar and hit **Enter** on your keyboard.
4. If this is your first time logging in, and you have not yet changed the username and password, you can log in using the default password:

   1. **Password:** *456*
5. You'll be logged into the web portal and should see this:

   [![File:VVX311-Web-Conf-Util.png](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/398078855/9d52dee2152b116fe2e93866/800px-VVX311-Web-Conf-Util.png?expires=1781168400&signature=a7f7f5c53758b814a4c059080a939728961b3cd74d4047cf9bf7bae89706783a&req=dykvFs52lYRaFb4f3HP0gOOvvUR95Cg3UIKRNHvrNh106DBZURmdTAEwDba5%0A4zw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/398078855/9d52dee2152b116fe2e93866/800px-VVX311-Web-Conf-Util.png?expires=1781168400&signature=a7f7f5c53758b814a4c059080a939728961b3cd74d4047cf9bf7bae89706783a&req=dykvFs52lYRaFb4f3HP0gOOvvUR95Cg3UIKRNHvrNh106DBZURmdTAEwDba5%0A4zw%3D%0A)

[Back to Top](#h_0a78797f6f)

## **2. Configure NTP settings**

While not strictly required, it's a good idea to setup your backup NTP settings in case your DHCP server does not provide time service information.

1. From the top navigation, click on **Simple Setup** and expand the **Time Synchronization** section on the page. Provide the following:

   1. **Alternate SNTP Server:** *north-america.pool.ntp.org* for North America. For additional details, see [this link](https://www.ntppool.org/en/use.html).
   2. **Alternate Time Zone:** Enter your preferred time zone

      [![File:VVX311-NTP-Settings.png](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/398078857/f7a34b3717819ae2e542bcce/800px-VVX311-NTP-Settings.png?expires=1781168400&signature=939ffbc299db35b2ea1e7afebe01431b52745c650a98d017652e03d0072c26f1&req=dykvFs52lYRYFb4f3HP0gLtQn0G8G4bH%2BcAQMN57m9aBQvehYkPorARhDVq5%0A%2F8k%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/398078857/f7a34b3717819ae2e542bcce/800px-VVX311-NTP-Settings.png?expires=1781168400&signature=939ffbc299db35b2ea1e7afebe01431b52745c650a98d017652e03d0072c26f1&req=dykvFs52lYRYFb4f3HP0gLtQn0G8G4bH%2BcAQMN57m9aBQvehYkPorARhDVq5%0A%2F8k%3D%0A)

[Back to Top](#h_0a78797f6f)

## 3. Configure SIP settings

In this section, you'll configure your IP phone to connect to your Telnyx SIP trunk.

1. Begin the SIP configuration by clicking on **Settings > Lines** in the left-hand navigation to open the Line 1 configuration screen.

   [![File:VVX311-Lines-Menu.png](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/398078859/13b8b015b25a06d008ffc64f/214px-VVX311-Lines-Menu.png?expires=1781168400&signature=89d99b65b38c5dba2da178c9bfb905f3f94ab6d66f47760668e261f07a28b328&req=dykvFs52lYRWFb4f3HP0gKo0tQlhxsig7BxU8Vo2XuMK7dfRJfqOeIeODC3s%0AS7g%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/398078859/13b8b015b25a06d008ffc64f/214px-VVX311-Lines-Menu.png?expires=1781168400&signature=89d99b65b38c5dba2da178c9bfb905f3f94ab6d66f47760668e261f07a28b328&req=dykvFs52lYRWFb4f3HP0gKo0tQlhxsig7BxU8Vo2XuMK7dfRJfqOeIeODC3s%0AS7g%3D%0A)
2. Each line button you want to use will need to be configured individually but all should generally require the same settings. This example will show you what was required for this specific setup but your requirements may vary.
3. For each section listed below, you will need to enter this information (red highlighted sections):  
   ​  
   ​**Identification** section**:**

   1. Display Name: This is your outbound caller ID name.   
      ​  
      ​***Note:*** *Before configuring an outbound caller ID, you should be aware of some of the naming conventions standard for caller ID creation:*

      * *Your outbound Caller ID Name should be in **capital letters**. This will appears more clearly/visible on some devices.*
      * *You **must NOT use any special characters**, as they will not be displayed.*
      * *Some of regular **Canadian providers will not show more than 15 characters**. We suggest shrinking or adapt your caller ID.*
      * ***Spaces are allowed*** *in a caller id name.*
      * *Be familiar with [Telnyx's caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)*  
        ​
   2. **Address:** Your Telnyx account name
   3. **Label:** The name listed next to the line button on your phone
   4. **SRTP settings:** should all be set to *No*
   5. **Server Auto Discovery:** *Disabled*  
      ​

   **Server 1** section**:**

   1. **Address:** Your selected Telnyx SIP server FQDN or IP address
   2. **Port:** *5060*
   3. **Transport:***UDP Only*
   4. **Expires:** *300*, your value may depend on your gateway/router timeout values but this is typically fine
   5. **Subscription Expire(s):** *300*, same as **Expires**  
      ​

   **Message Center** section**:**

   1. **Callback Mode:** *Contact*
   2. **Callback Contact:** *\*97* to dial the assigned extension's VM box  
      ​

[Back to Top](#h_0a78797f6f)

## **4. Restart the phone and verify your settings**

To make sure that the settings take effect, we recommend that you restart the phone.

1. From your phone, go to **Utilities > Restart Phone.**
2. When prompted, click **Yes**.

Once your phone reboots, your display should show the phone online, the registration status section on VoIP's Control Panel should show registered and you should be able to make/receive calls with Telnyx as your SIP Provider!

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Polycom support](https://support.hp.com/us-en/poly)
* Polycom VVX 300-series IP phone user guide

---

Related Articles

[Yealink: Setup with Telnyx](https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx)[Flyingvoice: Telnyx Setup](https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)[Grandstream GXP: Telnyx Setup](https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup)[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)

Did this answer your question?

😞😐😃

Table of contents
