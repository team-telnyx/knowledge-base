---
source_url: https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx
scraped: 2026-06-11
---

Yealink: Setup with Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# Yealink: Setup with Telnyx

In this guide we will walk you through configuring a Yealink T Series IP phone with Telnyx.

C

Written by Customer Success

October 23, 2023

Table of contents

[Jump to Instructions](#h_860d1e8063)

[YeaLink](https://www.yealink.com/en) provides video and voice communication technology solutions for your business needs. This article guides you on how to configure your T series IP-based hardphones which are SIP compatible, for making and receiving calls over the internet through a next generation carrier like Telnyx!

Additional documentation:

* [Yealink Knowledge Base](https://support.yealink.com/en/portal/knowledge)
* [Yealink equipment maintenance](https://ams.yealink.com/search/index)
* [Yealink license application](https://license.yealink.com/)
* [Yealink support](https://support.yealink.com/en/portal/home)

---

# Instructions for Configuring your Yealink IP phone

In this activity you will:

1. [Provision your Yealink phone](#h_50399089c4)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Connect your Yealink phone to an ethernet port to establish an internet connection

**Video walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Yealink/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Provision your Yealink phone

When provisioning a Yealink phone manually, there are two methods:

* Using the phone’s keypad
* Using the phone’s web interface

We will provide instructions for both methods.   
​  
​**Using the phone's keypad**

1. From your phone handset, press the **Menu** button.
2. Navigate to **Advanced.**
3. Enter the password. Unless you've changed it, it will be the default password: **admin**
4. Navigate to **Accounts.**
5. Select an empty line and fill in the following fields:

   1. **Activation**: set this to *Enabled*.
   2. **Label**: Enter the name you would like to see on the screen of your Yealink phone (i.e. *John Doe*)
   3. **Register Name**: Your Telnyx account username
   4. **User name:** Your Telnyx account username

**Using the phone's web interface**

1. First, retrieve the phone's IP address:

   1. Press **Home/Menu** button on the phone.
   2. Navigate to **Status.**
   3. On screen you should see your phones IP address(on screen as: IPv4).
   4. Enter the IP address in your web browser's address bar.
2. You'll need to log into the web portal. Out of the box, the default credentials are:

   1. **Username:** *admin*
   2. **Password:** *admin*

      [![Telnyx web portal. ](https://downloads.intercomcdn.com/i/o/128648676/ccfc8ad4d78a135d3e118536/image.png?expires=1781167500&signature=c1d106308d142d5622e93f58a024a70f2767d6b589fe1237fdb6d3bb7160968d&req=dSIvEM12m4ZZFb4f3HP0gLVsA%2F7vy58MVtopt%2BSV6JDWSB3rCdqobSgoV2%2F3%0AARA%3D%0A)](https://downloads.intercomcdn.com/i/o/128648676/ccfc8ad4d78a135d3e118536/image.png?expires=1781167500&signature=c1d106308d142d5622e93f58a024a70f2767d6b589fe1237fdb6d3bb7160968d&req=dSIvEM12m4ZZFb4f3HP0gLVsA%2F7vy58MVtopt%2BSV6JDWSB3rCdqobSgoV2%2F3%0AARA%3D%0A)
3. From the menu, click on **Account**, find **Account 1**, and provide the following information:

   1. **Activation**: *Enabled*
   2. **Label**: Enter the name you would like to see on the screen of your Yealink phone (i.e. *John Doe*)
   3. **Register Name**: Enter the username from your credentials-based Telnyx connection
   4. **User name:** Enter the username from your credentials-based Telnyx connection
   5. **Password:** Enter the password from your credentials based connection.
   6. **Display Name:** It is shown as the caller ID when placing the outbound calls  
      ​  
      ​***Note:*** *Before configuring an outbound caller ID, you should be aware of some of the naming conventions standard for caller ID creation:*

      * *Your outbound Caller ID Name should be in **capital letters**. This will appears more clearly/visible on some devices.*
      * *You **must NOT use any special characters**, as they will not be displayed.*
      * *Some of regular **Canadian providers will not show more than 15 characters**. We suggest shrinking or adapt your caller ID.*
      * ***Spaces are allowed*** *in a caller id name.*
      * *Be familiar with [Telnyx's caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)*

      [![Yealink web settings dashboard. ](https://downloads.intercomcdn.com/i/o/128649807/fccdd77a3e7cf2b7d69144d0/image.png?expires=1781167500&signature=446a7e456eade7579f3c6c868d61e596c88b6e196d6630bf3cdcf071e5a7127b&req=dSIvEM13lYFYFb4f3HP0gBs%2B9Xund4umkq6d7f2TS7xUD9ZRgGCcBLs7yfyF%0AT1w%3D%0A)](https://downloads.intercomcdn.com/i/o/128649807/fccdd77a3e7cf2b7d69144d0/image.png?expires=1781167500&signature=446a7e456eade7579f3c6c868d61e596c88b6e196d6630bf3cdcf071e5a7127b&req=dSIvEM13lYFYFb4f3HP0gBs%2B9Xund4umkq6d7f2TS7xUD9ZRgGCcBLs7yfyF%0AT1w%3D%0A)

That's it, you've now completed the configuration of your Yealink IP phone and can now make and receive calls by using Telnyx as the SIP provider.

##

[Back to Top](#h_860d1e8063)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:

* [Yealink Knowledge Base](https://support.yealink.com/en/portal/knowledge)
* [Yealink equipment maintenance](https://ams.yealink.com/search/index)
* [Yealink license application](https://license.yealink.com/)
* [Yealink support](https://support.yealink.com/en/portal/home)

---

Related Articles

[Configuring a Vicidial IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx)[Configuring Linphone with Telnyx](https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx)[Polycom: Setup with Telnyx](https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx)[Flyingvoice: Telnyx Setup](https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)

Did this answer your question?

😞😐😃

Table of contents
