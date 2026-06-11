---
source_url: https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx
scraped: 2026-06-11
---

MS Teams: Call2Teams & Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# MS Teams: Call2Teams & Telnyx

Learn how to set up and configure Call2Teams and connect Microsoft Teams to a PBX/SIP trunk.

C

Written by Customer Success

June 6, 2024

Table of contents

[Jump to Instructions](#h_8d2da11584)

[Microsoft Call2Teams](https://www.call2teams.com/)™ is an add-on for Office 365 that connects Microsoft Teams to any PBX or [SIP Trunk](https://telnyx.com/products/sip-trunks), allowing you to make and receive calls on any device using the Microsoft Teams App.

**Additional resources:**

* Features and benefits for the end user
* [Features and benefits for partners](https://www.call2teams.com/partners/)
* Call2Teams support (partner login required)

---

# Instructions for setting up and configuring Call2Teams to work with Telnyx

In this activity you will:

1. [Set up the Office 365 Tenant](#h_829aeeb8ab)
2. [Connect to Telnyx and create a SIP trunk](#h_829aeeb8ab)
3. [Assign a phone number to a team member](#h_927d8477c5)

**Pre-requisites**

* Your Telnyx Portal must be correctly [set up and configured for use](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* Have your SIP Credentials (The username/password for your main SIP account or SIP sub-account)
* Have [DID(s) available](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) to assign
* A PC running a Windows OS
* Create a temporary spare user license on Microsoft 365
* Global admin access to your Microsoft 365 tenant
* Create a Call2Teams subscription  
  ​

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

## 1. Set up the Office 365 tenant

In this section you will log into the Call2Teams portal and set up your

1. Once you've created your subscription to Call2Teams, you'll receive an email inviting you to the portal. When you click Accept Invitation, you'll need to use your Office 365 account to log in. Make sure this account is associated with the organization you're configuring Call2Teams for and that you have global-level; access.
2. Give Call2Teams permission to connect to your 365 account.

   1. You MUST check the **Connect on behalf of your organization** checkbox.

      [![Call2Teams portal.](https://downloads.intercomcdn.com/i/o/495511909/2f68422f897a20a8aaa22d03/3.png?expires=1781168400&signature=f5270b4e3f6e0f34533abff0ceb3e5b025a26092e8a323626e7363cfbc36fb3a&req=cCkiE8h%2FlIFWFb4f3HP0gLnDEvV4dh5o4l36t4WZmr0UF%2FaAUPFX3WlALUOq%0AkAM%3D%0A)](https://downloads.intercomcdn.com/i/o/495511909/2f68422f897a20a8aaa22d03/3.png?expires=1781168400&signature=f5270b4e3f6e0f34533abff0ceb3e5b025a26092e8a323626e7363cfbc36fb3a&req=cCkiE8h%2FlIFWFb4f3HP0gLnDEvV4dh5o4l36t4WZmr0UF%2FaAUPFX3WlALUOq%0AkAM%3D%0A)
3. Click **Accept**.

[Back to Top](#h_8d2da11584)

## 2. Connect to Telnyx and Create a SIP trunk

In this activity, you will set Telnyx as your SIP provider and create your first trunk that will be connected by Call2Teams to Microsoft Teams.

1. ### **From the Call2Teams admin portal, click on the "Service" tab in the top navigation.**
2. ### **From here, find the "Trunk" tab. Click on this, then click "Add New Trunk".**
3. ### **Here you will see a drop-down menu where you can select from a list of verified providers with pre-configured profiles that will set your trunk up for you.**

   1. As of the time of writing, Telnyx is not yet on this list, so you'll need to select **Custom** from this list. You'll get a message telling you that any Telnyx-specific support can't be handled by Microsoft at this time. Click the **Proceed with Unsupported Configuration** button.

      [![Service tab in the Call2Teams portal. ](https://downloads.intercomcdn.com/i/o/495519597/a0ef4940f0985276c0c0061c/5.png?expires=1781168400&signature=7d6a2f8c076a0473b05f2315c4491bdd7b2635c1d535044f4a1667e08cd36575&req=cCkiE8h3mIhYFb4f3HP0gC5fFDmFzXqyHdnwyulEzoAyuzbVRiWGbzlcsww0%0AR4Y%3D%0A)](https://downloads.intercomcdn.com/i/o/495519597/a0ef4940f0985276c0c0061c/5.png?expires=1781168400&signature=7d6a2f8c076a0473b05f2315c4491bdd7b2635c1d535044f4a1667e08cd36575&req=cCkiE8h3mIhYFb4f3HP0gC5fFDmFzXqyHdnwyulEzoAyuzbVRiWGbzlcsww0%0AR4Y%3D%0A)
4. ### **You'll now be able to enter your Telnyx account information. Provide the following:**

   * **Service Name**: *Telnyx Trunk 1*
   * **Country**: Your Country
   * **State/Province**: Your State/Province
   * **Range Start/Range End**: You'll use your Telnyx DIDs. Ensure that you add + plus your country code before entering your DID.

     + If you have more than one DID that you would like to add and they are not sequential, add each of these DIDs on both the **START Range** and the **Range END** fields.
     + You will need to add each DID separately by adding a new range by clicking on **+ Add Additional Range.**
   * **SIP Domain**: *sip.telnyx.com*
   * **Authenticate Type**: *Registration*
   * **Username**: Your Telnyx account/sub-account username
   * **Auth Username**: Your Telnyx account/sub-account username
   * **Password**: Your Telnyx account/sub-account password
   * **Expiry (seconds)**: If you want, click on the padlock, and enter *300*. You can also leave this blank.
   * **Protocol**: *UDP* or *TCP*.
   * **Encrypt Media**: *No*
   * **Propagate Refer:** *Yes*   
     ​  
     ​**Note:** Select *Yes* to propagate received SIP REFER messages from Microsoft upstream to this service.

     + If set to *No* then transfers are bridged out as new calls.On the 2nd Gen OneClick Teams connector you should select *Yes* if you have users in a Call Center, but otherwise select *No* as this will allow consultative transfers to work better.

   * **Propagate Refer**: *No*
   * **Outside Line Prefix**: Leave this option blank
   * **E164 Number Format**: *Localized*

   * **From Header**: *SIP Identifier*
   * **P-Asserted-Identity Header**: This will be the outbound caller ID Name. You can choose:

     + *Passthrough Caller Id:* This will be the caller ID given by the far end (e.g. Teams (The user extension name)),
     + *Trunk User Number:* To display the phone number assigned to the user in the portal

   * **E164 Number Translation** (The incoming number needs to be converted to E164 format)

     + **Outbound International Prefix**: *011*
     + **Outbound National Prefix**: Leave blank
     + **Inbound International Prefix**: Indicate
     + **Inbound National Prefix**: Leave blank

     [![Call2Teams portal for inputing Telnyx account information. ](https://downloads.intercomcdn.com/i/o/495524367/8090342e8242e61a4e34ed32/6.png?expires=1781168400&signature=fe4e7940ec5c1732aa3a4dc20bfd9deb2f3fef6d552d8602465600bc2f62dc36&req=cCkiE8t6nodYFb4f3HP0gFsTc10SyzfvmuA5W%2BAUxK%2BTaMY%2FO0CEY87gTHUE%0Atcw%3D%0A)](https://downloads.intercomcdn.com/i/o/495524367/8090342e8242e61a4e34ed32/6.png?expires=1781168400&signature=fe4e7940ec5c1732aa3a4dc20bfd9deb2f3fef6d552d8602465600bc2f62dc36&req=cCkiE8t6nodYFb4f3HP0gFsTc10SyzfvmuA5W%2BAUxK%2BTaMY%2FO0CEY87gTHUE%0Atcw%3D%0A)

     [![SIP domain section.](https://downloads.intercomcdn.com/i/o/495524654/62d78f7221be9b8cbb0842f6/7.png?expires=1781168400&signature=63d03fa90e029873aabf4a247bcfa7000757b0fa953d0897086368d4b8c3a75f&req=cCkiE8t6m4RbFb4f3HP0gLHshEzApOSDnSJyQtxtA%2FhsMFk7Z0RG8pFwHpxw%0AJxA%3D%0A)](https://downloads.intercomcdn.com/i/o/495524654/62d78f7221be9b8cbb0842f6/7.png?expires=1781168400&signature=63d03fa90e029873aabf4a247bcfa7000757b0fa953d0897086368d4b8c3a75f&req=cCkiE8t6m4RbFb4f3HP0gLHshEzApOSDnSJyQtxtA%2FhsMFk7Z0RG8pFwHpxw%0AJxA%3D%0A)

     [![Call2Teams portal for calling policy. ](https://downloads.intercomcdn.com/i/o/495532985/6131b586faae7550f6ad1a51/8.png?expires=1781168400&signature=b83707630aaa32326c924467c600d25d7ce1f72973f7e90ee01fe4b7eb636b56&req=cCkiE8p8lIlaFb4f3HP0gPumgv%2Fix7dRBlb%2FmE4mNyJXZWt4xnvyCbMubek0%0APFo%3D%0A)](https://downloads.intercomcdn.com/i/o/495532985/6131b586faae7550f6ad1a51/8.png?expires=1781168400&signature=b83707630aaa32326c924467c600d25d7ce1f72973f7e90ee01fe4b7eb636b56&req=cCkiE8p8lIlaFb4f3HP0gPumgv%2Fix7dRBlb%2FmE4mNyJXZWt4xnvyCbMubek0%0APFo%3D%0A)
5. ### **Click the "Add Trunk" button.**
6. ### **You'll now see your new trunk in your list. Click on the Trunk tab to see your list at any time. You can also monitor the health of your Trunk and ensure it's still up and running from this list.**

   [!["Add Trunk" button.](https://downloads.intercomcdn.com/i/o/495535703/5dd044ac8add41d52fe502a7/9.png?expires=1781168400&signature=07d8e6cfda31b601336be6fc19eec382f3876687fdf6744000d4dc8b5c849100&req=cCkiE8p7moFcFb4f3HP0gJ5IyLFC%2BDm9czEul5Q7RwDjA%2BBaYueByUlqGm52%0Ak9E%3D%0A)](https://downloads.intercomcdn.com/i/o/495535703/5dd044ac8add41d52fe502a7/9.png?expires=1781168400&signature=07d8e6cfda31b601336be6fc19eec382f3876687fdf6744000d4dc8b5c849100&req=cCkiE8p7moFcFb4f3HP0gJ5IyLFC%2BDm9czEul5Q7RwDjA%2BBaYueByUlqGm52%0Ak9E%3D%0A)

[Back to Top](#h_8d2da11584)

## 3. Associate a number with a team member

In this section, you'll add users to Call2Teams and associate numbers with them. These numbers will be the DIDs you entered in [section 2](#h_829aeeb8ab).

1. Click on the **Users** tab in the top navigation.
2. From this tab, click **Add New User** and provide the following information:

   1. **Select a User:** Select the user intended for the number.
   2. **PBX/Trunk:** Select a trunk you've created
   3. **Select a Trunk Number:** Select the DID intended for this user.

      [![Users tab. ](https://downloads.intercomcdn.com/i/o/495540921/411b5aa6e4a483ef2bbcc6d6/11.png?expires=1781168400&signature=725f08923b1d5cfa0c0e458aedee815fc9e55ec9b8e4dce98ec24445ebd1c544&req=cCkiE81%2BlINeFb4f3HP0gLr0mg60hv1hF3YawDnl%2FSLzzydd0v758JauQrgg%0Ahzg%3D%0A)](https://downloads.intercomcdn.com/i/o/495540921/411b5aa6e4a483ef2bbcc6d6/11.png?expires=1781168400&signature=725f08923b1d5cfa0c0e458aedee815fc9e55ec9b8e4dce98ec24445ebd1c544&req=cCkiE81%2BlINeFb4f3HP0gLr0mg60hv1hF3YawDnl%2FSLzzydd0v758JauQrgg%0Ahzg%3D%0A)
3. Click the **Add** button, followed by the **Sync Now** button in the upper right.

That's it! You've finished configuring Call2Teams, and can now start testing calls!  
​  
​

[Back to Top](#h_8d2da11584)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* Features and benefits for the end user
* [Features and benefits for partners](https://www.call2teams.com/partners/)
* Call2Teams support (partner login required)

---

---

Related Articles

[Configuring Telnyx with Microsoft Teams Direct Routing](https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing)[PBXes: Connecting a PBXes Trunk to Telnyx](https://support.telnyx.com/en/articles/5798240-pbxes-connecting-a-pbxes-trunk-to-telnyx)[Wildix: SIP Trunk Setup](https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup)[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)[BYOC: Telnyx & Genesys](https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys)

Did this answer your question?

😞😐😃

Table of contents
