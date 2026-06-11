---
source_url: https://support.telnyx.com/en/articles/6128008-sipxecs-pbx-setup-config
scraped: 2026-06-11
---

sipXecs PBX: Setup & Config | Telnyx Help Center

[Skip to main content](#main-content)

# sipXecs PBX: Setup & Config

Learn how to set up and configure the SIPfoundry sipXecs open source PBX to use Telnyx as the VoIP provider.

C

Written by Customer Success

June 6, 2024

Table of contents

[Jump to Instructions](#h_99d8568e05)

[SIPfoundry introduces sipXecs](http://www.sipfoundry.org/), the open source unified communications and collaboration project.

If you are looking for an all-software, open-source, modern communications PBX solution that scales to mid-size and large enterprise, . SIPfoundry is a community dedicated to the development of SIP- and XMPP-based communications solutions.

|  |
| --- |
| ***Note:*** *This guide explains how to install a single server system. This first server can be extended into a large cluster later using the admin UI.* |

**Additional documentation:**

* [sipXecs configuration guide](http://www.sipfoundry.org/Blogs/easy-guide-fast-start-for-sipxecs-admins)
* [sipXecs documentation](https://sipfoundry.atlassian.net/wiki/display/sipXecs/Home)
* [SIPfoundry support](http://www.sipfoundry.org/sipxecs-support-services)
* [sipXecs download](http://www.sipfoundry.org/sipxecs-software-download/)

---

# Instructions for setting up and configuring sipXecs with Telnyx as VoIP provider

In this activity you will:

1. [Install sipXecs on a computer or virtual server](#h_d763e4fbd8)
2. [Configure your first SIP trunk](#h_5706eac0e4)
3. [Log into the admin console and configure your superadmin account](#h_529dd5d385)
4. [Add phones to sipXecs](#h_28b2263b50)
5. [Add supported codecs](#h_a2d79f647a)

**Pre-requisites**

* Your Telnyx Portal must be correctly [set up and configured for use](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* Have your SIP Credentials (The username/password for your main SIP account or SIP sub-account)
* Have [DID(s) available](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) to assign.
* Installed/configured a computer or virtual server to use as a test server. Ensure it meets the minimum system requirements:

  + ### **Physical server:**

    - Dual or quad core CPU
    - 4 GB of RAM (minimum)
    - 40 GB hard drive (minimum),
    - 1 network card.
    - This machine’s hard drive will be wiped. Download and install a minimum version of CentOS 6 or RHEL 6 following the instructions provided by the operating system.
  + ### **Virtual machine:**

    - Clean VM from e.g. Google or Amazon. Avoid instances that have CPanel installed (such as VPS from Bluehost).
    - Two compute cores
    - 2 to 4 GB RAM
    - 16 GB storage, excluding storage for voicemail.
    - Start from a minimum image of CentOS 6 or RHEL 6.
* A network segment. Preferably use a separate routed network segment so that sipXecs can install and run its own DHCP server for phone auto-discovery and provisioning. If you can't do this, you'll have to manually configure sipXecs as the FTP server into each phone for it to download the configuration.
* Phone hardware of some kind:

  + ### **Desk phones:**

    [Polycom](https://www.google.com/aclk?sa=l&ai=DChcSEwiy_MD_5YT3AhUJpsgKHfy2DrsYABAkGgJxdQ&ae=2&sig=AOD64_0pnRV4Y7LLTJG_goJfMfcQXLwP0A&q&adurl&ved=2ahUKEwi7kbf_5YT3AhXdgnIEHdSMCXMQ0Qx6BAgEEAM) is the preferred phone but many other options exist
  + ### **Softphones:**

    [Counterpath Bria](https://www.google.com/aclk?sa=l&ai=DChcSEwigjdyL5oT3AhWGjMgKHTnOBzoYABACGgJxdQ&ae=2&sig=AOD64_2yjuu0KAFvBoU1dpL56y3X9BdfxQ&q&adurl&ved=2ahUKEwillNOL5oT3AhUbknIEHfBzCqQQ0Qx6BAgCEAM) is preferred but many other SIP softphones will work such as [Counterpath X-Lite](https://www.counterpath.com/x-lite/), [Linphone](https://www.linphone.org/), and [Jitsi](https://jitsi.org/)
  + ### **Mobile:**

    [Counterpath Bria](https://www.counterpath.com/softphone-clients/?utm_term=softphone%20for%20windows&utm_campaign=Search+-+USA+-+Direct+Sales+-+2020+-+NEW&utm_source=adwords&utm_medium=ppc&hsa_acc=2637421614&hsa_cam=9595061028&hsa_grp=100330646633&hsa_ad=504561969780&hsa_src=g&hsa_tgt=kwd-1582890290&hsa_kw=softphone%20for%20windows&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAjwur-SBhB6EiwA5sKtjkMtTT8t4qkhYd76XhN9q71dDDRfB0z10hDBMuGEbIMVpcb3G2bfuhoCNBwQAvD_BwE) smartphone and tablet app (iPhone and Android). Many other SIP mobile clients will work such as [CSipSimple](https://www.onsip.com/voip-resources/voip-reviews/csipsimple) or [SIPdroid](http://sipdroid.org/)
* (Optional) PTSN connectivity. Either via a PSTN gateway ([Audiocodes](https://www.audiocodes.com/) is the preferred brand) or with a [SIP trunk](https://telnyx.com/products/sip-trunks). There are several ITSP’s that work
* (Optional) Firewall for internet connectivity. For SIP trunking or connectivity to devices connected via the Internet you will want a firewall / SBC. sipXecs Canary and newer no longer includes a built-in SBC for SIP trunking. We recommend [Sangoma SBC](https://www.sangoma.com/products/network-connectivity/session-border-controllers/) for production deployments. Also, sipXecs includes native NAT traversal for remote devices connected via NAT. Additionally, [Ingate](https://www.ingate.com/), [Audiocodes](https://www.audiocodes.com/solutions-products/products/session-border-controllers-sbcs), or [ACME Packet](https://www.oracle.com/a/ocom/docs/industries/communications/comm-acme-packet-3900-ds.pdf) are all good choices for a professional SBC.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

## 1. Install sipXecs on your computer or virtual server

1. Log into your system as root or sudo to root.
2. You have several options for install.

   1. Install sipXecs by running the following script:

      ```
      bash -c "$(curl -L http://rpms.sipfoundry.org/canary-release/sipxecs-install)"
      ```
   2. Alternatively, you can also use the .repo file to install the software. Install the repo file into */etc/yum.repos.d*, then install the EPEL repository

      ```
      yum install -y epel-release
      ```

      and then run

      ```
      yum install sipxecs
      ```

      Once completed run the */usr/bin/sipxecs-setup* script.

[Back to Top](#h_99d8568e05)

## 2. Configure your first SIP trunk

In this section, you'll configure a Telnyx SIP trunk on sipXecs.

1. Run the */usr/bin/sipxecs-setup* configuration script. You'll need to provide the following information during setup:

   1. **IP Address:** Make sure you take note of this. You'll need it in the next section.
   2. **Configure network:** *No* (If your network is configured already)
   3. **First server:** *Yes*
   4. **Host name:** Choose the hostname you'd like to use (i.e.: *sipxecs*)
   5. **Domain:** *sip.telnyx.com*
   6. **SIP Domain:** *sip.telnyx.com*
   7. **SIP Realm:** Enter the name of the realm to which the SIP interface is connected

      [![The /usr/bin/sipxecs-setup configuration script.](https://downloads.intercomcdn.com/i/o/494272789/754b62840ea6d2e5fd1567c3/sipXecs-setup-script.png?expires=1781168400&signature=872ab0c84f0edee5e54b59febe17060b3cced18696a0b95fb38b304e61c61bd2&req=cCkjFM58molWFb4f3HP0gFUzTAJF2fGHc8gWOe4iZojzqANP209fiUIrarqk%0Amz8%3D%0A)](https://downloads.intercomcdn.com/i/o/494272789/754b62840ea6d2e5fd1567c3/sipXecs-setup-script.png?expires=1781168400&signature=872ab0c84f0edee5e54b59febe17060b3cced18696a0b95fb38b304e61c61bd2&req=cCkjFM58molWFb4f3HP0gFUzTAJF2fGHc8gWOe4iZojzqANP209fiUIrarqk%0Amz8%3D%0A)

[Back to Top](#h_99d8568e05)

## 3. Log into the admin console and configure the superadmin account

In this section, you'll log into the admin console and assign a password to the superadmin account. You'll use this account for all admin activities.

1. Open a browser and enter the IP address from [section 1](#h_5706eac0e4) and hit **Enter**. Your browser will present you with a certificate warning. Acknowledge this to go on to the login screen.
2. You will be asked to assign the password for the superadmin user. Once you do this, log in as the superadmin. You'll be taken to the admin console home page:

   [![The admin console.](https://downloads.intercomcdn.com/i/o/494282440/7c9d633b2fe08db511506cf4/adminhome.png?expires=1781168400&signature=09d9fa65958c44c81287dc0af2d01624b2ce7204838017d80314a144d71e5e1b&req=cCkjFMF8mYVfFb4f3HP0gIG8LQAwep%2BqxPrxXKx3jVGQq1k6QYZqF6nMnmpG%0AG%2Bk%3D%0A)](https://downloads.intercomcdn.com/i/o/494282440/7c9d633b2fe08db511506cf4/adminhome.png?expires=1781168400&signature=09d9fa65958c44c81287dc0af2d01624b2ce7204838017d80314a144d71e5e1b&req=cCkjFMF8mYVfFb4f3HP0gIG8LQAwep%2BqxPrxXKx3jVGQq1k6QYZqF6nMnmpG%0AG%2Bk%3D%0A)

|  |
| --- |
| ***Note:*** *You'll need to enable the services your organization will require. Most of these services are disabled by default when you first log in. Navigate to **System > Servers** and enable the settings you'll need.*    *You'll also need to add at least one user in order to start adding phones. Navigate to **Users > Users** and click on the **Add New User** link to add a new user.* |

[Back to Top](#h_99d8568e05)

## 4. Add phones to sipXecs

In this section, you'll add phone hardware or software to sipXecs and assign them to a user.

|  |
| --- |
| ***Note:*** *You can add a phone to sipXecs but in order to make calls with it, it must be assigned to a user.* |

1. In the admin portal, navigate to **Users > Users** and click on the user you want to assign a phone.
2. From the user screen, click on **Phones** in the lefthand menu.
3. If you configured sipXecs on an isolated subnet during installation, enabled the DHCP service, and enabled the Phone Auto-Provisioning service, then you are all set for auto-discovery of supported devices! Reset the configuration of a phone (if it's not new), and plug it into the network segment. It should automatically pick up a default configuration and come up with a provisional line configured and registered. If you did not configure these settings, skip to step 6.

   1. To find your auto-discovered devices, navigate to **Devices > Phones**.
4. Next, go to **Users > Phones** to provision a phone to a user and choose an existing but unassigned phone for the user by opening the **Add New Phone** dropdown dialogue and selecting the desired phone from the list.

   1. sipXecs now generates a configuration profile with default parameters that make sense for this particular user.
5. Plug the phone into the network and restart it. Make sure the phone has the sipXecs server configured as its FTP server if DHCP does not provide it and make sure the FTP service is enabled. The phone will now load the configuration profile.

   1. Make sure you press the **Send Profile** button to generate the phone profile.
6. You can also manually configure a phone. If your phone isn't in the **Add New Phone** dropdown, you will have to manually configure it by going to the phone’s configuration manager. The necessary parameters are typically:

   1. **Account Name:** A friendly name for the account that only you see
   2. **User ID:** The user’s numeric extension
   3. **Domain**: *sip.telnyx.com*
   4. **Password:** This is the TELNYX account or sub-account password
   5. **Display Name:** This will end up being the caller ID. Caller ID

      1. Name should be in capital letters. This will appears more clearly/visible on some devices.
      2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed.
      3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID.
   6. **Auth Name** The user’s numeric extension

[Back to Top](#h_99d8568e05)

## 5. Add supported codecs

sipXecs supports any codec so your only restriction will be to make sure you use a Telnyx-supported codec. The following is a list of codecs (both audio and video) that Telnyx supports:

**Audio:**

* ulaw(g711u)
* alaw(g711a)
* g722
* g729

**Video:**

* H264

That's it! You've finished configuring sipXecs, and can now start testing calls!

[Back to Top](#h_99d8568e05)

---

## Troubleshooting

**Q: *The phone I manually configured isn't working? What's wrong?***

**A:** If you cannot get it working with the information you provided in [section 4](#h_28b2263b50), you likely have some DNS issue. You can perform DNS tests going to **System > DNS** and then select **Advisor**.  
​  
​

[Back to Top](#h_99d8568e05)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [sipXecs configuration guide](http://www.sipfoundry.org/Blogs/easy-guide-fast-start-for-sipxecs-admins)
* [sipXecs documentation](https://sipfoundry.atlassian.net/wiki/display/sipXecs/Home)
* [SIPfoundry support](http://www.sipfoundry.org/sipxecs-support-services)
* [sipXecs download](http://www.sipfoundry.org/sipxecs-software-download/)

---

Related Articles

[How to configure a Thirdlane PBX](https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx)[Wildix: SIP Trunk Setup](https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup)[ScopTEL IP PBX](https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx)[Dinstar C60: Setup & Config](https://support.telnyx.com/en/articles/6128321-dinstar-c60-setup-config)[MicroSIP: Setup with Telnyx](https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx)

Did this answer your question?

😞😐😃

Table of contents
