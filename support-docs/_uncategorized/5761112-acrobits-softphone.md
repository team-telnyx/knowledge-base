---
source_url: https://support.telnyx.com/en/articles/5761112-acrobits-softphone
scraped: 2026-06-11
---

Acrobits Softphone | Telnyx Help Center

[Skip to main content](#main-content)

# Acrobits Softphone

Learn how to configure Acrobits Softphone or Acrobits Groundwire to use Telnyx for voice calling.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_2e5fde5343)

|  |
| --- |
| ***IMPORTANT:*** *Acrobits softphone apps can only be used for voice calling, as SIP/Simple, which is required to enable SMS/MMS on Acrobits, is currently not supported by Telnyx.* |

Make voice & video calls, send texts, share files, and more—all within [Acrobits](https://acrobits.net/). Acrobits allows you to build your own customized [UCaaS](https://telnyx.com/resources/ucaas) solution that exactly fits your needs. Cloud Softphone lets you design, build, and deploy your suite in mere days, sometimes less than 24 hours. And if your needs change, don't worry! You can add and remove over 100+ available premium features whenever you need. And you only pay for what you use. And if security is your concern, don't worry. Acrobits uses the same encryption stack being used by the European Parliament.

You can use the [Acrobits Groundwire or Acrobits Softphone](https://acrobits.net/sip-client-ios-android/) apps on iOS and Android.

**Additional resources:**

* [Acrobits official site](https://acrobits.net/)
* [Acrobits pricing and demo options](https://acrobits.net/cloud-softphone/pricing/)
* [What can I do with Acrobits?](https://acrobits.net/features/)
* [Build your own low-code app with cloud softphone](https://acrobits.net/cloud-softphone/)
* [Acrobits SDK](https://acrobits.net/acrobits-sdk/)

---

# Instructions for configuring Acrobits to work with Telnyx

|  |
| --- |
| ***Note:*** *Because of all the possible customizations you can do within Acrobits, this guide will cover the basic configuration only. See the additional documentation above to get started with customizing your Acrobits solution.* |

In this document, you will:

1. [Connect Acrobits to Telnyx](#h_4cabf36690)
2. OPTIONAL: [Set up a display name to work with your outbound caller ID](#h_e2d545f3bc)

**Pre-requisites and hardware requirements**

* Ensure your [Telnyx Portal is configured correctly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* Ensure you meet the [hardware requirements](https://acrobits.net/cloud-softphone/pricing/) necessary to run Acrobits
* [Add key and repository to Debian](https://acrobits.net/cloud-softphone/pricing/)
* [Configure SIPIS](https://acrobits.net/cloud-softphone/pricing/)
* [Setting up HTTPS registration](https://acrobits.net/cloud-softphone/pricing/)
* [Configure your firewall](https://acrobits.net/cloud-softphone/pricing/)
* Ensure that any other SIPIS settings in [this document](https://doc.acrobits.net/sipis/index.html) are configured the way you need them to be

**Video Walkthrough**

Coming soon! Check back frequently as we are updating our documentation.  
​

## 1. Connect Acrobits with Telnyx

In this step, you will sync your Acrobits softphone app with your Telnyx account.

1. Run the Acrobits app (either Acrobits Softphone or Acrobits Groundwire).
2. Tap on the settings gear at the top-right of the screen. From settings, select **SIP Accounts**
3. Tap on **New SIP Account**.
4. You will be presented with a list of providers. If, for whatever reason, you don't find Telnyx in this list, please contact Telnyx support to let us know, and simply add us manually. Don't worry, you'll be adding server details in the next step, so Acrobits will be able to connect to us regardless.
5. Regardless of whether you are able to select Telnyx from the list or need to add it manually, you will need to enter your server information. Enter the following:

   1. **Title:** A title for your connection. We recommend using *Telnyx*.
   2. **Username:** Your Telnyx account username
   3. **Password:** Your Telnyx account password
   4. **Domain:** *sip.telnyx.com*

      [![Telnyx new account settings. ](https://downloads.intercomcdn.com/i/o/424122538/78f31e595351bc77e8cfd479/200px-Acrobits_2.png?expires=1781168400&signature=216b8135aa3aef65060796ba184e43f2b7834a4363dfad4ca62336253746dd29&req=cCIjF8t8mIJXFb4f3HP0gItsT0BKnnNYVpr5nptbRpVrRMdAtyEeUqSMW4Qo%0AeYA%3D%0A)](https://downloads.intercomcdn.com/i/o/424122538/78f31e595351bc77e8cfd479/200px-Acrobits_2.png?expires=1781168400&signature=216b8135aa3aef65060796ba184e43f2b7834a4363dfad4ca62336253746dd29&req=cCIjF8t8mIJXFb4f3HP0gItsT0BKnnNYVpr5nptbRpVrRMdAtyEeUqSMW4Qo%0AeYA%3D%0A)
6. Click **Save**.

And that's it! You'll be able to start making calls through Telnyx using Acrobits!

[Back to Top](#h_2e5fde5343)

## 2. OPTIONAL: Set up a display name for your outbound caller ID

You can set set up a caller ID display name that will appear on outbound calls from the advanced settings in your Acrobits app. However, there are a few considerations and requirements you'll need to be aware of when choosing a caller ID name:

* Your outbound Caller ID Name should be in **capital letters**. This will appears more clearly/visible on some devices.
* You **must NOT use any special characters**, as they will not be displayed.
* Some of regular **Canadian providers will not show more than 15 characters**. We suggest shrinking or adapt your caller ID.
* **Spaces are allowed** in a caller id name.

That's it, you've now completed the configuration of your VitalPBX and can now make and receive calls by using Telnyx as the SIP provider.

[Back to Top](#h_2e5fde5343)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, check out:

* [Acrobits official site](https://acrobits.net/)
* [Acrobits pricing and demo options](https://acrobits.net/cloud-softphone/pricing/)
* [What can I do with Acrobits?](https://acrobits.net/features/)
* [Build your own low-code app with cloud softphone](https://acrobits.net/cloud-softphone/)
* [Acrobits SDK](https://acrobits.net/acrobits-sdk/)

---

Related Articles

[Configuring Linphone with Telnyx](https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx)[BuddyTalk BT110/BT120](https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120)[MicroSIP: Setup with Telnyx](https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx)[Grandstream Wave Lite (iPhone)](https://support.telnyx.com/en/articles/6184748-grandstream-wave-lite-iphone)[Grandstream Wave Lite (Android)](https://support.telnyx.com/en/articles/6184897-grandstream-wave-lite-android)

Did this answer your question?

😞😐😃

Table of contents
