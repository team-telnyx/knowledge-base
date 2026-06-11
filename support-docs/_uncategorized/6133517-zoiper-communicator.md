---
source_url: https://support.telnyx.com/en/articles/6133517-zoiper-communicator
scraped: 2026-06-11
---

Zoiper Communicator | Telnyx Help Center

[Skip to main content](#main-content)

# Zoiper Communicator

Maximize your online communication with the Zoiper Communicator IAX & SIP softphone, a free, multi-functional tool.

C

Written by Customer Success

June 6, 2024

Table of contents

[Jump to Instructions](#h_9def290ce2)

[Zoiper Communicator](https://digitalvoice.ca/softphone_zoiper_dl.php) IAX & SIP softphone is a free converged Internet communication tool combining high-quality voice and video calls, fax, instant messaging and presence through a contact-centric intuitive interface. The [Zoiper](https://support.telnyx.com/en/articles/6133517-zoiper-communicator) Service is embedded in your Zoiper Communicator and assures free advanced Zoiper-to-Zoiper communication.

|  |
| --- |
| ***Note:*** *You can choose not to use the Zoiper service with Zoiper Communicator. Simply choose "I don't want to use this service" from the interface on initial startup. You can also just not log into the service on startup as well.* |

|  |
| --- |
| ***Note:*** *Zoiper does not advertise or offer Zoiper Communicator at this time, however it is still available for use via the link above.* |

Additional Resources:

* [Zoiper help](https://www.zoiper.com/en/support/questions)  
  ​

---

# Instructions for Configuring Zoiper Communicator

In this activity you will:

1. [Add Telnyx as your SIP provider and create a trunk](#h_04c5d08d3f)  
   ​

**Pre-requisites**

* Your Telnyx Portal must be correctly [set up and configured for use](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* Have your SIP Credentials (The username/password for your main SIP account or SIP sub-account)
* Have [DID(s) available](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) to assign
* A PC running a Windows OS
* [Download](https://digitalvoice.ca/softphone_zoiper_dl.php) and install Zoiper Communicator  
  ​

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *We are trying to find a Zoiper Communicator video and have it available soon! Check back frequently as we are updating our documentation.* |

## 1. Add Telnyx as your SIP provider and create a trunk

In this section, you'll configure your first [SIP trunk](https://telnyx.com/products/sip-trunks) on your Zoiper Communicator softphone.

1. Start Zoiper Communicator and select **Settings**.
2. Select **Create New Account**.

   [![Settings section of the Zoiper Communicator. ](https://downloads.intercomcdn.com/i/o/495452076/ab7e565669225ff76afcc3a4/1.png?expires=1781168400&signature=329637cfa7aebe12638cd2ed176816d281c7d9cbd24d90284485ffb4506a1e73&req=cCkiEsx8nYZZFb4f3HP0gGVfQQlA4YV07KM8sUQub1M77J7oaI2Tu5ook%2FIg%0ALEw%3D%0A)](https://downloads.intercomcdn.com/i/o/495452076/ab7e565669225ff76afcc3a4/1.png?expires=1781168400&signature=329637cfa7aebe12638cd2ed176816d281c7d9cbd24d90284485ffb4506a1e73&req=cCkiEsx8nYZZFb4f3HP0gGVfQQlA4YV07KM8sUQub1M77J7oaI2Tu5ook%2FIg%0ALEw%3D%0A)
3. Enter a name for your new account and click **OK**.

   [![Account name entry section of the Zoiper Communicator. ](https://downloads.intercomcdn.com/i/o/495460429/89d17d7617464179aac78711/2.png?expires=1781168400&signature=61ec183d8f1ca86a910461d9ee751d339cefc1a3b102ed4dffcd55895b922e8a&req=cCkiEs9%2BmYNWFb4f3HP0gGz17%2FO0NPEVX1m9FUxTYg0TDMMCGSlNCXNLOWDW%0A%2B14%3D%0A)](https://downloads.intercomcdn.com/i/o/495460429/89d17d7617464179aac78711/2.png?expires=1781168400&signature=61ec183d8f1ca86a910461d9ee751d339cefc1a3b102ed4dffcd55895b922e8a&req=cCkiEs9%2BmYNWFb4f3HP0gGz17%2FO0NPEVX1m9FUxTYg0TDMMCGSlNCXNLOWDW%0A%2B14%3D%0A)
4. On the **SIP Account Options** page, provide the following information:

   1. **Domain:** *sip.telnyx.com*
   2. **Username:** Your main Telnyx account or sub-account username
   3. **Password:** Your main Telnyx account or sub-account password
   4. **Caller ID Name:** Choose whatever name you prefer. Note the following caller ID naming conventions:

      1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.

      [![SIP Account Options page.](https://downloads.intercomcdn.com/i/o/495462090/3fcdf949bd101efa778000a3/3.png?expires=1781168400&signature=0ec6693378d6c39b148107f202bce1cb95d78b7ebfa18f5aa811efbdb00c4647&req=cCkiEs98nYhfFb4f3HP0gI6PC4wb0oHRgca49z4SCNSfq4gfxr6BopriNLNo%0Aptg%3D%0A)](https://downloads.intercomcdn.com/i/o/495462090/3fcdf949bd101efa778000a3/3.png?expires=1781168400&signature=0ec6693378d6c39b148107f202bce1cb95d78b7ebfa18f5aa811efbdb00c4647&req=cCkiEs98nYhfFb4f3HP0gI6PC4wb0oHRgca49z4SCNSfq4gfxr6BopriNLNo%0Aptg%3D%0A)
5. Click **OK** to complete the setup.

   [![SIP Account Options page to complete setup. ](https://downloads.intercomcdn.com/i/o/495462488/6546e6ea6c3f335c4bf17765/4.png?expires=1781168400&signature=da9b1367ee84fddebe754da43a43427e97167a28ead561d2c763018b035f66e2&req=cCkiEs98mYlXFb4f3HP0gCcIp0FHhQJH4AN%2Fmd%2BHCDdBBBlOOAseCrIRsTBv%0AfP4%3D%0A)](https://downloads.intercomcdn.com/i/o/495462488/6546e6ea6c3f335c4bf17765/4.png?expires=1781168400&signature=da9b1367ee84fddebe754da43a43427e97167a28ead561d2c763018b035f66e2&req=cCkiEs98mYlXFb4f3HP0gCcIp0FHhQJH4AN%2Fmd%2BHCDdBBBlOOAseCrIRsTBv%0AfP4%3D%0A)

That's it! You've finished configuring your Zoiper Communicator softphone, and can now start testing calls!  
​

[Back to Top](#h_9def290ce2)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Zoiper help](https://www.zoiper.com/en/support/questions)

---

Related Articles

[SIP URI Calling](https://support.telnyx.com/en/articles/2925713-sip-uri-calling)[Zoiper 5 Pro: Telnyx Setup](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup)[Dinstar C60: Setup & Config](https://support.telnyx.com/en/articles/6128321-dinstar-c60-setup-config)[MicroSIP: Setup with Telnyx](https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx)[MS Teams: Call2Teams & Telnyx](https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx)

Did this answer your question?

😞😐😃

Table of contents
