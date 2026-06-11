---
source_url: https://support.telnyx.com/en/articles/5772825-counterpath-bria-teams-setup
scraped: 2026-06-11
---

CounterPath Bria Teams: Setup | Telnyx Help Center

[Skip to main content](#main-content)

# CounterPath Bria Teams: Setup

Elevate team connectivity with Bria Teams and Telnyx. This tutorial covers everything from linking accounts to configuring dial plans.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_246be6708b)

Bria Teams is a powerful and secure team-communication solution in which the team can connect via voice, messaging, online presence and screen share, using any or all of their devices while still streamlined into one application. Every tool you might need to keep your teams connected can be managed by one easy-to-use dashboard.

Additional documentation:

* [Bria Portal user documentation](https://docs.counterpath.com/docs/PortalUG/Resources/TitlePages/TeamsTitlePage.htm) (you can find your operating system from here)
* [Bria Solo user documentation](https://docs.counterpath.com/docs/PortalUG/clients/UserGuides/Desktop/quickStart/quickStartSolo.htm?Highlight=bria%20solo)
* [Bria Teams user documentation](https://docs.counterpath.com/docs/PortalUG/Resources/TitlePages/TeamsTitlePage.htm)
* [Counterpath support](https://support.counterpath.com/hc/en-us)

---

# Instructions for integrating your Bria Portal with Telnyx

In this document, you will:

1. [Link your Bria Teams account with Telnyx](#h_d1f4708790)
2. [(OPTIONAL) Configure security and encryption settings](#h_917bf7c44c)
3. [Configure a dial plan](#h_59017d026b)
4. [Configure audio and video codecs](#h_97fd196198)
5. [Link a team member to a SIP account profile](#h_28a0f9bd97)

|  |
| --- |
| ***Note:*** *Each team member added to Bria Teams will need a sub account, which you can set up in your Bria Teams dashboard at any time. However, for this example, we'll just use a team with one member for clarity.* |

**Pre-requisites and system requirements**

* Make sure your [Telnyx Mission Control Portal is set up properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* *Minimum* OS requirements:

  + Windows 10
  + Mac 10.13
  + Android 5.0
  + iOS 11
* Download and install the Bria Desktop client or Bria Mobile client

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Auth0/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Link your Bria Portal with Telnyx

In this step, you'll add Telnyx to your Bria Teams client through your Bria Teams portal.

1. From the Bria Portal, click **Voice and Video** in the top navigation.
2. Click on either

   1. [![phone icon. ](https://downloads.intercomcdn.com/i/o/426241284/dfe4ba7d74dc3a0de50eeb2d/addconfig.png?expires=1781168400&signature=bcc20c4ee0569106c8f033b98466eb12fafd97df912d62023f9d54dff78f0b22&req=cCIhFM1%2Fn4lbFb4f3HP0gDb9SG%2BxNFJin9SitFdXWGz059HDKTJcmsU28LQS%0AD%2B8%3D%0A)](https://downloads.intercomcdn.com/i/o/426241284/dfe4ba7d74dc3a0de50eeb2d/addconfig.png?expires=1781168400&signature=bcc20c4ee0569106c8f033b98466eb12fafd97df912d62023f9d54dff78f0b22&req=cCIhFM1%2Fn4lbFb4f3HP0gDb9SG%2BxNFJin9SitFdXWGz059HDKTJcmsU28LQS%0AD%2B8%3D%0A)
   2. [![Button with "Add Voice Configuration" command. ](https://downloads.intercomcdn.com/i/o/426241437/526f90a42c4ceace9202b792/addconfig2.png?expires=1781168400&signature=51b50d7a45672940e914dd0ccc5cfd460c56a318ef7beafffe12d435c4246dc2&req=cCIhFM1%2FmYJYFb4f3HP0gExuL85uzolN31Yrwh9y0v93uaPHD9uuoQjr6mIc%0A5Go%3D%0A)](https://downloads.intercomcdn.com/i/o/426241437/526f90a42c4ceace9202b792/addconfig2.png?expires=1781168400&signature=51b50d7a45672940e914dd0ccc5cfd460c56a318ef7beafffe12d435c4246dc2&req=cCIhFM1%2FmYJYFb4f3HP0gExuL85uzolN31Yrwh9y0v93uaPHD9uuoQjr6mIc%0A5Go%3D%0A)
3. The Add Service screen will give you two options. Currently, Telnyx is not on the pre-configured list of providers, so you'll need to add it manually. To add Telnyx, click on **Configure SIP Settings**.

   [![Add voice service section. ](https://downloads.intercomcdn.com/i/o/426252230/78729092680ae1cb99281cea/addvoice.png?expires=1781168400&signature=c4658059825f8f8a0b7f6fdfccf969671b9706416226ca749048b2005500783d&req=cCIhFMx8n4JfFb4f3HP0gCOTQzCf3AwRbBQMLCS67Q%2BGwVsRqVlNASYbsL2r%0ACp0%3D%0A)](https://downloads.intercomcdn.com/i/o/426252230/78729092680ae1cb99281cea/addvoice.png?expires=1781168400&signature=c4658059825f8f8a0b7f6fdfccf969671b9706416226ca749048b2005500783d&req=cCIhFMx8n4JfFb4f3HP0gCOTQzCf3AwRbBQMLCS67Q%2BGwVsRqVlNASYbsL2r%0ACp0%3D%0A)
4. The **New Voice Configuration** screen will appear. Here you will add server details that will apply to every entity (such as people or SIP connections) that you will add to your portal in the future. Fill in the following:

   1. **Service Label**: Only for your own purposes, for easy association
   2. **Domain**: *sip.telnyx.com*
   3. **Port**: *5060*
   4. **Register with domain and receive calls**: [CHECKED]
   5. **Transport**: *Automatic*
   6. **Keep Alive**: *Enabled*
   7. **Voicemail**: Voicemail Number: *\*97*
   8. **Service Options**: [CHECKED] This voice service requires an authorization username for each voice account.
   9. **Firewall Method:** *Stun* (This is optional, but you can use this if you want to specify it)
   10. **Firewall Server URL:** *stun.telnyx.com:3478*
   11. **Username:** Telnyx firewall username (Reach out to support for more information)
   12. **Password:** Telnyx firewall password (Reach out to support for more information)

   [![New Voice Configuration settings. ](https://downloads.intercomcdn.com/i/o/426332000/aa842547d52160f8dd74c9cd/adjustedAddSIP.png?expires=1781168400&signature=e6348133b489e322011596810e579108c54aeed074d98749a7e66fceafb919cd&req=cCIhFcp8nYFfFb4f3HP0gL38DanSYHd5xGF4GcKWRqF1duVVJkpFAST9thON%0AMwQ%3D%0A)](https://downloads.intercomcdn.com/i/o/426332000/aa842547d52160f8dd74c9cd/adjustedAddSIP.png?expires=1781168400&signature=e6348133b489e322011596810e579108c54aeed074d98749a7e66fceafb919cd&req=cCIhFcp8nYFfFb4f3HP0gL38DanSYHd5xGF4GcKWRqF1duVVJkpFAST9thON%0AMwQ%3D%0A)
5. Click **Save And Close**.

   1. Unless you have already configured voice accounts, in which case, click **Assign Voice Accounts From this configuration to team members** and skip to section x.
6. You can test your setup from your Bria Portal client on your computer or mobile device. On the computer, click the arrow beside **Auto Select**. On mobile, go to Bria **Settings** > **Accounts**. You should see both accounts with a green icon.

[Back to Top](#h_246be6708b)

## 2. (OPTIONAL) Configure security and encryption settings

This section is optional, but you will want to follow it if you want to encrypt call traffic. If you're not sure, or want to know more about the benefits of encrypting traffic, contact support for more information.

1. If you haven't already, you'll need to adjust your SIP settings to support TLS encryption. To do this, go to the Bria Portal, click **Voice and Video** in the top navigation.
2. Find the voice service you want to encrypt and click the **Edit Configuration** button.

   [![Voice Service #1 settings tab. ](https://downloads.intercomcdn.com/i/o/426333089/c4814a35b925285d6d4bd32d/Screen+Shot+2021-11-29+at+13.51.12.png?expires=1781168400&signature=64df31760529fcbf406482b215df52577825da0a4b886693358e10073de6dcc5&req=cCIhFcp9nYlWFb4f3HP0gMYrt%2BsCP%2FSGHxAmaKhob6VeNHeimN%2BKtPghbvNW%0A8IY%3D%0A)](https://downloads.intercomcdn.com/i/o/426333089/c4814a35b925285d6d4bd32d/Screen+Shot+2021-11-29+at+13.51.12.png?expires=1781168400&signature=64df31760529fcbf406482b215df52577825da0a4b886693358e10073de6dcc5&req=cCIhFcp9nYlWFb4f3HP0gMYrt%2BsCP%2FSGHxAmaKhob6VeNHeimN%2BKtPghbvNW%0A8IY%3D%0A)
3. Make the following changes:

   1. **Port:** *5061*
   2. **Transport:** *TLS*
   3. **SRTP:** *Enabled*
   4. **Register with Domain and Receive Calls:** [checked]

   [![Voice Configuration editing. ](https://downloads.intercomcdn.com/i/o/426335856/439617af0e8d4e581d971b5c/tls.png?expires=1781168400&signature=0450ded5069581b924290cc761928fc2cfe4d35b0b15cbd4cca2e787eed3774b&req=cCIhFcp7lYRZFb4f3HP0gOG2ctSFN1f3TuNQ31cIVyvZFvdMny8OkVkSoNe9%0AmD8%3D%0A)](https://downloads.intercomcdn.com/i/o/426335856/439617af0e8d4e581d971b5c/tls.png?expires=1781168400&signature=0450ded5069581b924290cc761928fc2cfe4d35b0b15cbd4cca2e787eed3774b&req=cCIhFcp7lYRZFb4f3HP0gOG2ctSFN1f3TuNQ31cIVyvZFvdMny8OkVkSoNe9%0AmD8%3D%0A)

[Back to Top](#h_246be6708b)

## 3. Configure a dial plan

In this step, you will configure a dial plan in Bria Portal. For example, you may want to configure your system to require all outgoing callers to dial 9 before dialing out.

(add a concept article or tooltip explaining dial plan - should contain something like...

{a dial plan can be used to modify how your calls are placed. For example, a dial plan can change any number that starts with “+1613” to “613”. A dial plan is used for any combination of the following reasons:

* To modify (transform) the input (the number to be dialed), such as to add the “9” required to obtain an outside line from a PBX.
* To select the account to use to place a call, if users have more than one account. For example, to use Account 1 to dial a number starting with 61, and use Account 2 to dial a number starting with 64.}

Bria has [their own dial plan syntax](https://docs.counterpath.com/docs/PortalUG/clients/UserGuides/Desktop/calls/deskDialPlan.htm).

[Back to Top](#h_246be6708b)

## 4. Configuring audio and video codecs

In this step, you will configure your audio and video codecs and even set them in order of preference. This configuration will apply to all the custom SIP accounts you configured in step 1.

1. Open your Bria Portal client or the Bria Portal web app and click **Settings and Preferences** in the top navigation.

   [![Settings and Preferences on the Bria Portal.  ](https://downloads.intercomcdn.com/i/o/426318013/2f77014530790cb5fdb53322/settingsandpreferences.png?expires=1781168400&signature=c4091c543d8e8aa5468723b55a64c7e6594b3b030b7ecad8495d0ddd8defbc3f&req=cCIhFch2nYBcFb4f3HP0gMUbIFcLLs0xmrcqHucJM0w89kn%2FzFPQyV1xvGwT%0ASR0%3D%0A)](https://downloads.intercomcdn.com/i/o/426318013/2f77014530790cb5fdb53322/settingsandpreferences.png?expires=1781168400&signature=c4091c543d8e8aa5468723b55a64c7e6594b3b030b7ecad8495d0ddd8defbc3f&req=cCIhFch2nYBcFb4f3HP0gMUbIFcLLs0xmrcqHucJM0w89kn%2FzFPQyV1xvGwT%0ASR0%3D%0A)
2. Click the **Configure** **Codecs** button to open the Codec Settings page.
3. In the **Codecs** section, click the gear icon.

   [![Codecs settings. ](https://downloads.intercomcdn.com/i/o/426321144/b26e483e1d432ce22efdf7e8/Screen+Shot+2021-11-29+at+13.27.png?expires=1781168400&signature=c73f8b81bfda351cfcb6e2fb22fc1fbeaf340457c665069b8b4ff17c25fc3b66&req=cCIhFct%2FnIVbFb4f3HP0gIfs%2BuMPlnjJ8RPxR0hzUGq5TVkthy27IaK7Mt0A%0AX38%3D%0A)](https://downloads.intercomcdn.com/i/o/426321144/b26e483e1d432ce22efdf7e8/Screen+Shot+2021-11-29+at+13.27.png?expires=1781168400&signature=c73f8b81bfda351cfcb6e2fb22fc1fbeaf340457c665069b8b4ff17c25fc3b66&req=cCIhFct%2FnIVbFb4f3HP0gIfs%2BuMPlnjJ8RPxR0hzUGq5TVkthy27IaK7Mt0A%0AX38%3D%0A)
4. On this screen, you can choose, and prioritize, the codecs you'll use for audio and video. Note that the following codecs are supported by Telnyx:

   1. ulaw(g711u)
   2. alaw(g711a)
   3. g722
   4. g729

   [![Audio and Video codec settings. ](https://downloads.intercomcdn.com/i/o/426324190/d1b08bc871f3f705a39111dd/Screen+Shot+2021-11-29+at+13.35.27.png?expires=1781168400&signature=7cd91e0809ac5d3949c0daefbdc1127598401ccf8b5fc91511c46a9db7f787df&req=cCIhFct6nIhfFb4f3HP0gP%2BTeHg9IWDXLg8CA%2B2hXmBZHE4P0joBkBZm3MIZ%0AEN4%3D%0A)](https://downloads.intercomcdn.com/i/o/426324190/d1b08bc871f3f705a39111dd/Screen+Shot+2021-11-29+at+13.35.27.png?expires=1781168400&signature=7cd91e0809ac5d3949c0daefbdc1127598401ccf8b5fc91511c46a9db7f787df&req=cCIhFct6nIhfFb4f3HP0gP%2BTeHg9IWDXLg8CA%2B2hXmBZHE4P0joBkBZm3MIZ%0AEN4%3D%0A)

[Back to Top](#h_246be6708b)

## 5. Link a team member to an account and SIP profile

In this section, you'll learn how to associate a team member with the SIP profile you added in step 1.

1. Click on the **Team Members** tab in the top navigation menu.

   [![Team Members settings. ](https://downloads.intercomcdn.com/i/o/426340091/ccc12a033ddc74b5b1623d95/teammembers.png?expires=1781168400&signature=f65dc712dc0d7b62cc843e24a291e9b462cabdd45414e5e3b0bacf7f8b6f757c&req=cCIhFc1%2BnYheFb4f3HP0gGkwRUACXpJJIsNT8Sm%2BV8nc1iVtdO3IozPRcf3P%0AaR8%3D%0A)](https://downloads.intercomcdn.com/i/o/426340091/ccc12a033ddc74b5b1623d95/teammembers.png?expires=1781168400&signature=f65dc712dc0d7b62cc843e24a291e9b462cabdd45414e5e3b0bacf7f8b6f757c&req=cCIhFc1%2BnYheFb4f3HP0gGkwRUACXpJJIsNT8Sm%2BV8nc1iVtdO3IozPRcf3P%0AaR8%3D%0A)

   ​
2. If you have already added team members and are familiar with this step, skip to step 4. Otherwise, from the left-hand navigation, click the button next to **team members**.

   [![Team members settings. ](https://downloads.intercomcdn.com/i/o/426784845/7abdb984c1bf750a57569af7/add3.png?expires=1781168400&signature=71929afb4c094e1d37af70d34c09e083855922ef87170491b68aafb379201b40&req=cCIhEcF6lYVaFb4f3HP0gKiwrJtCl8tetfp6fm86ochkXv7oif14H5AvY0kA%0ARKQ%3D%0A)](https://downloads.intercomcdn.com/i/o/426784845/7abdb984c1bf750a57569af7/add3.png?expires=1781168400&signature=71929afb4c094e1d37af70d34c09e083855922ef87170491b68aafb379201b40&req=cCIhEcF6lYVaFb4f3HP0gKiwrJtCl8tetfp6fm86ochkXv7oif14H5AvY0kA%0ARKQ%3D%0A)
3. Enter the email address of the new team member. Their invite will be sent here. If you want to assign them to a SIP profile, click the phone button next to the email field and go on to step 4. Otherwise, click **Add Members And Invite** if you are finished. You can also add additional team members with the **+ Add Member** button.

   [![Build your team settings. ](https://downloads.intercomcdn.com/i/o/426770020/5af0ed20cb24aa6bf9ede06b/newTeamMember.png?expires=1781168400&signature=0d0e12ec737bc3200ed6a86645081d719683276ca83304215f1006ac3792800f&req=cCIhEc5%2BnYNfFb4f3HP0gFPI0W%2BGhdqyHxNNCweBzX3CrQ7WcN7s7fIN9WYQ%0AFfk%3D%0A)](https://downloads.intercomcdn.com/i/o/426770020/5af0ed20cb24aa6bf9ede06b/newTeamMember.png?expires=1781168400&signature=0d0e12ec737bc3200ed6a86645081d719683276ca83304215f1006ac3792800f&req=cCIhEc5%2BnYNfFb4f3HP0gFPI0W%2BGhdqyHxNNCweBzX3CrQ7WcN7s7fIN9WYQ%0AFfk%3D%0A)
4. To assign a team member to a SIP profile, you'll need to provide the following:

   1. **VOICE SERVICE:** If you have multiple voice services, you can select the one you wish to assign to your new team member. If you only have one voice service set up, the wizard will default to this.
   2. **SIP USERNAME/CALL EXTENSION**: The team member's Telnyx username
   3. **SIP/VOICE PASSWORD**: The team member's Telnyx password
   4. **CALL DISPLAY**: Is your Outbound Caller ID Name. *(**Note**: We suggest entering it in capital letters, and no longer than 15 characters, without special characters such as dots, commas or apostrophe.)*

   [![Member addition settings. ](https://downloads.intercomcdn.com/i/o/426785544/b96d493e7205defe594bd31c/Screen+Shot+2021-11-30+at+08.02.22.png?expires=1781168400&signature=9e756940e2c801aae0d2e24849229195303b4f5894bd19204aab3f6fc8a75ed8&req=cCIhEcF7mIVbFb4f3HP0gAeZU5Hoeb5UzqyYc9X40egpsotp9BxIGKnZvVBF%0AKtA%3D%0A)](https://downloads.intercomcdn.com/i/o/426785544/b96d493e7205defe594bd31c/Screen+Shot+2021-11-30+at+08.02.22.png?expires=1781168400&signature=9e756940e2c801aae0d2e24849229195303b4f5894bd19204aab3f6fc8a75ed8&req=cCIhEcF7mIVbFb4f3HP0gAeZU5Hoeb5UzqyYc9X40egpsotp9BxIGKnZvVBF%0AKtA%3D%0A)

   Some additional considerations for your call display name:

   1. Call ID name should be in CAPITAL LETTERS. This is easier to read on some devices.
   2. No special characters will be displayed. Don't use them.
   3. Max 15 characters
   4. Spaces are allowed

When you create a new member with his email address, they will receive a link in order to download and install the softphone. Then they will need to follow the instructions. A new password will need to be created by them using the email address that you used to create the member.

That's it, you've now linked Bria Teams to Telnyx and your fellow teammates to Telnyx!

[Back to Top](#h_246be6708b)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, check out:

* [Bria Portal user documentation](https://docs.counterpath.com/docs/PortalUG/Resources/TitlePages/TeamsTitlePage.htm) (you can find your operating system from here)
* [Bria Solo user documentation](https://docs.counterpath.com/docs/PortalUG/clients/UserGuides/Desktop/quickStart/quickStartSolo.htm?Highlight=bria%20solo)
* [Bria Teams user documentation](https://docs.counterpath.com/docs/PortalUG/Resources/TitlePages/TeamsTitlePage.htm)
* [Counterpath support](https://support.counterpath.com/hc/en-us)

---

Related Articles

[Configuring a Cisco CUBE/CUCM IP Trunk](https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk)[Cisco: Configure a Cisco CME IP Trunk](https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk)[Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)[Grandstream GXP: Telnyx Setup](https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup)[Audiocodes 400HD](https://support.telnyx.com/en/articles/5819923-audiocodes-400hd)

Did this answer your question?

😞😐😃

Table of contents
