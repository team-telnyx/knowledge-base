---
source_url: https://support.telnyx.com/en/articles/6122586-ubiquiti-trunk-unifi-talk-auth
scraped: 2026-06-11
---

Ubiquiti Trunk: Unifi Talk - Auth | Telnyx Help Center

[Skip to main content](#main-content)

# Ubiquiti Trunk: Unifi Talk - Auth

Learn how to configure a Telnyx Trunk with credentials-based authentication with Ubiquiti Unifi Talk PBX.

C

Written by Customer Success

June 6, 2024

Table of contents

[Jump to Instructions](#h_5f24533bc0)

The [UniFi Talk PBX](https://help.ui.com/hc/en-us/articles/1500005593742), provided by [Ubquiti](https://www.ui.com/), is a subscription-based VoIP phone solution that is the ideal plug-and-play setup for small to medium sized businesses.

|  |
| --- |
| ***Note:*** *Unifi Talk (which we will refer to from here as simply Talk) has specific hardware requirements. Only other Talk devices are compatible with the Talk application. See the pre-requisites section of this document for more information.* |

**Additional documentation:**

* [UniFi Talk FAQ](https://www.ui.com/new-integrations/managed-voip)
* [UniFi Talk community](https://community.ui.com/)
* [UniFi Talk support](https://help.ui.com/hc/en-us)
* [Talk device firmware](https://www.ui.com/download/)
* [UniFi Console quick-start guide](https://dl.ui.com/qig/udm-pro/#index)

---

# Instructions for configuring Unifi Talk PBX with your Telnyx Account

In this activity you will:

1. [Add a Telnyx SIP Trunk to your Talk application](#h_3d13fdf38a)
2. [Authorize international outgoing calls](#h_6f64f584a2)
3. [Configure phone numbers](#h_d36f908dd0)
4. [Set the IP address range](#h_ff9d76ba01)
5. [Assign a phone number to a user](#h_3f90ca2597)

**Pre-requisites**

* Your Telnyx Portal must be correctly [set up and configured for use](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* Have your SIP Credentials (The username/password for your main SIP account or SIP sub-account)
* Have [DID(s) available](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) to assign.
* You must have a [UniFi Console](https://ui.com/cloud-gateways) set up and configured: [A Dream Machine Pro](https://store.ui.com/us/en/products/udm-pro) or [Cloud Keygen 2 Plus](https://store.ui.com/us/en/products/uck-g2-plus) is required in order for the Talk application to work.

  + If you want to store call recordings, you will also need a hard disk drive, but this is not required for the Talk application to run correctly.
* PoE switches are required to power and connect your Talk device. UniFi offers their own [in-house option.](https://ui.com/switching/#compare)
* A [Talk device](https://www.ui.com/new-integrations/managed-voip). Only Talk devices will work with the Talk application.
* Your Talk application must be [set up and up to date](https://help.ui.com/hc/en-us/articles/1500005593742) before you continue

  + Ensure you can log into Talk UI
* Make sure to have completed [all firmware updates](https://www.ui.com/download/) or other updates on your endpoint(s) (IP Phone)

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

Setting up a third-party SIP provider with UniFi Talk (in this case, it is VoIP.ms)

## 1. Add a Telnyx SIP trunk to your Talk application

In this section, you'll configure Telnyx as your SIP provider within your Talk application.

1. From your Unifi Talk dashboard, click on the settings icon in the right-hand navigation.

   [![Settings section on the Unifi Talk dashboard. ](https://downloads.intercomcdn.com/i/o/529816287/873482bb33eef9e7a6ed4cd3/arrow.png?expires=1781168400&signature=44de5c225fbc4ea5da76defbb2f05dee7c8565a3aca5844714f7026dbf5d0dd7&req=cSIuHsh4n4lYFb4f3HP0gH5Wy0FqY%2F72aL7nfCPD0gItTDUAAi4j1YBaoDLN%0AzPk%3D%0A)](https://downloads.intercomcdn.com/i/o/529816287/873482bb33eef9e7a6ed4cd3/arrow.png?expires=1781168400&signature=44de5c225fbc4ea5da76defbb2f05dee7c8565a3aca5844714f7026dbf5d0dd7&req=cSIuHsh4n4lYFb4f3HP0gH5Wy0FqY%2F72aL7nfCPD0gItTDUAAi4j1YBaoDLN%0AzPk%3D%0A)
2. Under Unifi Talk settings click **System Settings**.

   [![System settings section on the Unifi Talk dashboard. ](https://downloads.intercomcdn.com/i/o/493633141/22bf0848c9974d0a05318269/600px-VoIPms_Unifi-Talk_Setting_System-Settings.png?expires=1781168400&signature=d4ed524c6f0197ea66e9dead756f3e93c675964fd87eeb43b697ecb5a35cbecf&req=cCkkEMp9nIVeFb4f3HP0gOPBGNtQQSAA3cpq3jp67jodI%2BB4X2kGoT13gNnH%0AAzw%3D%0A)](https://downloads.intercomcdn.com/i/o/493633141/22bf0848c9974d0a05318269/600px-VoIPms_Unifi-Talk_Setting_System-Settings.png?expires=1781168400&signature=d4ed524c6f0197ea66e9dead756f3e93c675964fd87eeb43b697ecb5a35cbecf&req=cCkkEMp9nIVeFb4f3HP0gOPBGNtQQSAA3cpq3jp67jodI%2BB4X2kGoT13gNnH%0AAzw%3D%0A)
3. Find the **Third Party SIP Setup** section and click on **Add Third Party SIP Provider**.
4. You can enter the provider name here (ie: *Telnyx*).

   [![Third Party SIP Setup on the Unifi Talk dashboard. ](https://downloads.intercomcdn.com/i/o/493636520/947c1fc5e22e022748a1103d/2.png?expires=1781168400&signature=cea6871011d7ff0355d47e1b093729c174ee262858314c5e95a5337c85705b23&req=cCkkEMp4mINfFb4f3HP0gGj%2FamXIMB5mlFEL3nyyqPDQpM7WYrcCl6019HLb%0A%2BE4%3D%0A)](https://downloads.intercomcdn.com/i/o/493636520/947c1fc5e22e022748a1103d/2.png?expires=1781168400&signature=cea6871011d7ff0355d47e1b093729c174ee262858314c5e95a5337c85705b23&req=cCkkEMp4mINfFb4f3HP0gGj%2FamXIMB5mlFEL3nyyqPDQpM7WYrcCl6019HLb%0A%2BE4%3D%0A)
5. Now we need to add a few custom fields, both the field names AND their corresponding values. Click the **Add Fields** button. You'll get a popup screen with a **+** which you can use to add new fields. Add the following information, *making sure to type the field names exactly as they're written below*:

   1. *proxy*
   2. *realm*
   3. *username*
   4. *password*
   5. *register*
   6. *sip\_cid\_type*
   7. *retry\_seconds*
   8. *expire-seconds*
6. Click on **Done** when you're finished.
7. Now you can add values to the fields you just created. In each field, provide the following:

   1. **proxy**: *sip.telnyx.com*
   2. **realm**: *sip.telnyx.com*
   3. **username**: Your Telnyx account or sub-account username
   4. **password**: Your Telnyx account or sub-account password
   5. **register**: *true*
   6. **sip\_cid\_type**: *rpd*
   7. **retry\_seconds**: *30*
   8. **expire-seconds**: *120*

[Back to Top](#h_5f24533bc0)

## 2. Authorize international outgoing calls

If you want your users to be able to dial out to other countries, you'll need to authorize those. (If you do not want your users making international calls, you can go onto section 3.

1. From the **System Settings** config, click the **Select Countries** button. Make sure your Telnyx account allows for international calling, or this will not work.

   [![System Settings configuration for Countries' selection. ](https://downloads.intercomcdn.com/i/o/493703204/ed267f9641efc01de1b4abf1/3.png?expires=1781168400&signature=c20a90e357822ba97fa383cb170881ec4fb5dafa3a1c262b345d9be799c51b6f&req=cCkkEcl9n4FbFb4f3HP0gJu7uoG16dc3zxYScCalvt%2BT4kmqUIb77wOB0AQO%0ALMA%3D%0A)](https://downloads.intercomcdn.com/i/o/493703204/ed267f9641efc01de1b4abf1/3.png?expires=1781168400&signature=c20a90e357822ba97fa383cb170881ec4fb5dafa3a1c262b345d9be799c51b6f&req=cCkkEcl9n4FbFb4f3HP0gJu7uoG16dc3zxYScCalvt%2BT4kmqUIb77wOB0AQO%0ALMA%3D%0A)
2. Click **Save**.

[Back to Top](#h_5f24533bc0)

## 3. Configure phone numbers

In this section, you'll be importing phone numbers into Talk. You have the option of importing them either manually by entering them one by one, or auto-importing them from a list in a text file.

1. From the **System Settings** config, open the **[DID Numbers](https://telnyx.com/resources/sip-did)** section.
2. To manually import numbers, enter each of your Telnyx DIDs that you provisioned as part of your [pre-requisite activities](#h_429a5653b5) into **Input Numbers** field in E164 format (ie: +1XXXXXXXXXX).

   1. You ***MUST*** provide the + at the beginning of your number string, otherwise you may get parsing errors.

      [![DID Numbers section on the System settings. ](https://downloads.intercomcdn.com/i/o/493709011/5240ef4ae2d233906bb0c765/4.png?expires=1781168400&signature=57d46956db347568751ca485c43028b7748fa0810cf5ab49a39542448b1980e1&req=cCkkEcl3nYBeFb4f3HP0gPATGeUIss8fzseQ2xDLMBs7Wx6fHjMcMUrvUvZS%0Afm4%3D%0A)](https://downloads.intercomcdn.com/i/o/493709011/5240ef4ae2d233906bb0c765/4.png?expires=1781168400&signature=57d46956db347568751ca485c43028b7748fa0810cf5ab49a39542448b1980e1&req=cCkkEcl3nYBeFb4f3HP0gPATGeUIss8fzseQ2xDLMBs7Wx6fHjMcMUrvUvZS%0Afm4%3D%0A)
3. To auto-import numbers from a text file, click the **Import Numbers with .TXT File** button.

   1. There ***MUST*** be the + at the beginning of each number string, otherwise you may get parsing errors.
   2. Make sure each number is on a separate line.

[Back to Top](#h_5f24533bc0)

## 4 Set the IP address range

In this section, you will set the range of ACL IP addresses that you will get from Telnyx. If you do not have these, please reach out to support.

1. From the **System Settings** config, click the **IP Address Range** option.
2. Click the **Add IP Address Range** button on the right.

   1. **CIDR Network Address**: *192.76.120.10* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).) Leave */32* as it is.
3. Click the **Add** button.

   [![IP Address Range option on the System Settings Configuration domain.](https://downloads.intercomcdn.com/i/o/529851091/b8dbfecff27e170ec4c9d81f/5.png?expires=1781168400&signature=a25d6cbffd29323e0ca9a86d35c4b44106c12fcdeab7eaf0619d8d5eb1f0b62e&req=cSIuHsx%2FnYheFb4f3HP0gJVCXm%2Bw%2FBTHR6VptDK6nVilB36oF6ZyT8p1nYHM%0A4R8%3D%0A)](https://downloads.intercomcdn.com/i/o/529851091/b8dbfecff27e170ec4c9d81f/5.png?expires=1781168400&signature=a25d6cbffd29323e0ca9a86d35c4b44106c12fcdeab7eaf0619d8d5eb1f0b62e&req=cSIuHsx%2FnYheFb4f3HP0gJVCXm%2Bw%2FBTHR6VptDK6nVilB36oF6ZyT8p1nYHM%0A4R8%3D%0A)

[Back to Top](#h_5f24533bc0)

## 5. Assign a phone number to a user

In this section, you'll assign a phone number to each user in your setup. These phone numbers are the DIDs you acquired as part of your [pre-requisite activities](#h_429a5653b5).

1. Go to the left-hand navigation and click on the users icon.

   [![Users icon. ](https://downloads.intercomcdn.com/i/o/494203956/661bc73d8589ad45779d6d55/6.png?expires=1781168400&signature=56312eb8e2824349eadfd931836631a39ed1172c529207772f29d1794cdd7105&req=cCkjFMl9lIRZFb4f3HP0gBrJbOh41CYfDz4grvFX2iAqvEK8BLmfGXi5YRLZ%0AbKU%3D%0A)](https://downloads.intercomcdn.com/i/o/494203956/661bc73d8589ad45779d6d55/6.png?expires=1781168400&signature=56312eb8e2824349eadfd931836631a39ed1172c529207772f29d1794cdd7105&req=cCkjFMl9lIRZFb4f3HP0gBrJbOh41CYfDz4grvFX2iAqvEK8BLmfGXi5YRLZ%0AbKU%3D%0A)
2. Find the user you want to assign a number and click the **Edit** button at the far right of their row.

   [![Edit button. ](https://downloads.intercomcdn.com/i/o/494204829/4ee97b17c3d28ee49ee4a826/7.png?expires=1781168400&signature=3130da73ce0b7d95893dc06bae3aa44306489c878d1cd317ae1430fb9d472620&req=cCkjFMl6lYNWFb4f3HP0gC2NUqobc4AhdXMm11yLFv8MOnJMTTzYMfKmlZaH%0AhDU%3D%0A)](https://downloads.intercomcdn.com/i/o/494204829/4ee97b17c3d28ee49ee4a826/7.png?expires=1781168400&signature=3130da73ce0b7d95893dc06bae3aa44306489c878d1cd317ae1430fb9d472620&req=cCkjFMl6lYNWFb4f3HP0gC2NUqobc4AhdXMm11yLFv8MOnJMTTzYMfKmlZaH%0AhDU%3D%0A)
3. A user edit popup will appear. Click the **Manage** dropdown

   [![Manage dropdown on the user edit popup. ](https://downloads.intercomcdn.com/i/o/494205685/df76a87d5cb9d3cbaaa9c94b/8.png?expires=1781168400&signature=185ee77491723c11fdc373e63711d46225992470b39809361164b70b56e82bf4&req=cCkjFMl7m4laFb4f3HP0gNHnRIoXzoKctuGYDm5G9ifdUGESJgrBvNrksafx%0A130%3D%0A)](https://downloads.intercomcdn.com/i/o/494205685/df76a87d5cb9d3cbaaa9c94b/8.png?expires=1781168400&signature=185ee77491723c11fdc373e63711d46225992470b39809361164b70b56e82bf4&req=cCkjFMl7m4laFb4f3HP0gNHnRIoXzoKctuGYDm5G9ifdUGESJgrBvNrksafx%0A130%3D%0A)
4. Find the **Change Number** section. Here you'll see all the DIDs you added in [section 3](#h_fd88a3a609). Any numbers that have not yet been assigned to a user will say "Unassigned" next to them.

   [![Change Number section. ](https://downloads.intercomcdn.com/i/o/494206900/5080625a4446ce5f5f22b350/9.png?expires=1781168400&signature=f4387fa49518535cf812f71e7916e050315e4c32c224913ea072088448015c2b&req=cCkjFMl4lIFfFb4f3HP0gKmt4kjH%2FPUY%2F9RXPdMPRxsNVocB1FwIuIZVU3TD%0AUXo%3D%0A)](https://downloads.intercomcdn.com/i/o/494206900/5080625a4446ce5f5f22b350/9.png?expires=1781168400&signature=f4387fa49518535cf812f71e7916e050315e4c32c224913ea072088448015c2b&req=cCkjFMl4lIFfFb4f3HP0gKmt4kjH%2FPUY%2F9RXPdMPRxsNVocB1FwIuIZVU3TD%0AUXo%3D%0A)

That's it! You've finished configuring Unifi Talk, and can now start testing calls from your Talk device!

[Back to Top](#h_5f24533bc0)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [UniFi Talk FAQ](https://www.ui.com/new-integrations/managed-voip)
* [UniFi Talk community](https://community.ui.com/)
* [UniFi Talk support](https://help.ui.com/hc/en-us)
* [Talk device firmware](https://www.ui.com/download/)
* [UniFi Console quick-start guide](https://dl.ui.com/qig/udm-pro/#index)

---

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[Configuring an Elastix 4 PBX Trunk](https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk)[FreeSWITCH: Credentials Trunk](https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk)[Elastix 5: FQDN Trunk Setup](https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup)[Ubiquiti Trunk: Unifi Talk - IP Auth](https://support.telnyx.com/en/articles/6303467-ubiquiti-trunk-unifi-talk-ip-auth)

Did this answer your question?

😞😐😃

Table of contents
