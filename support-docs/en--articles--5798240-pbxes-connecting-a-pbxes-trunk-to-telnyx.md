---
source_url: https://support.telnyx.com/en/articles/5798240-pbxes-connecting-a-pbxes-trunk-to-telnyx
scraped: 2026-07-08
content_hash: 42a3b23294002ae7f4e3bb3ed3be410677ac19a4ee974eb3cbb1b6915b7652a1
---

PBXes: Connecting a PBXes Trunk to Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# PBXes: Connecting a PBXes Trunk to Telnyx

Connect your PBXes SIP trunk to Telnyx effortlessly. Step-by-step instructions for inbound and outbound routing configurations.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_67de6d5252)

[PBXes.org](https://www1.pbxes.com/iptel_virtuelle-telefonanlage.html) (if you wish to read the page in English, right-click on the page and select **Translate to English** from the menu) is a German PBX provider that provides full operational service across all aspects of telephone system operation, from installation to updates, and even data backup are carried out by PBXes. They additionally provide a clear, easily calculable cost overview.

Additional documentation:

* [PBXes premium account options](https://www1.pbxes.com/shop.php)
* [PBXes user documentation](https://www1.pbxes.com/community.php?display=wiki) (if you wish to read the page in English, right-click on the page and select **Translate to English** from the menu)
* [PBXes user forum](https://www1.pbxes.com/community.php?display=forum)

---

# Instructions for configuring PBXes to work with Telnyx

In this activity you will:

1. [Add a SIP trunk to PBXes and connect the trunk to Telnyx](#h_f2eb8d4bd3)
2. [Configure inbound routing](#h_dbbcb8a282)
3. [Configure outbound routing](#h_4ea0789da1)

|  |
| --- |
| ***Note:*** *PBXes website (pbxes.org) is in German. We will provide all English instructions in this guide. If you wish to read PBXes' own site in English, right-click on the current page and select* **Translate to English***from the right-click menu.*    *This guide only covers the basics of connecting the trunk with Telnyx and placing outgoing calls.* |

**Pre-requisites**

* Ensure your [Telnyx Mission Control Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Provision a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) ([How do I do this?](https://support.telnyx.com/en/articles/3562148-requesting-numbers))
* Create either

  + A [free PBXes account](https://www1.pbxes.com/config.php) (You will be able to upgrade to one of the [Premium account](https://www1.pbxes.com/shop.php) options later if you decide to.)

**Video walkthrough**

Setting up your Telnyx Mission Control Portal so you can make/receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Thirdlane PBX/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Add a SIP trunk to PBXes and connect the trunk to Telnyx

In this step, you will create a [SIP trunk](https://telnyx.com/products/sip-trunks) in your PBXes online portal and connect the SIP trunk to Telnyx.

1. Log into your pbxes.com web portal using the login dialogue on the top-right of the page.
2. Expand **Trunks** in the left-hand menu and click on **Add Trunk.**
3. On the **Add a Trunk** page, click **Add SIP Trunk**.
4. On the **Add SIP Trunk** page, find the **General Settings** section and provide the following:

   1. **Trunk Name:** This can be whatever makes sense to you.
   2. **Language:** Choose your language
   3. **DTMF mode:** *Auto* or you can choose a [specific configuration](https://app.intercom.com/a/apps/ltcafuzd/articles/articles/1130710/show)
   4. **audio-bypass:** Your choice. [Need help choosing?](https://app.intercom.com/a/apps/ltcafuzd/articles/articles/1130722/show)
   5. **sendrpid:** *No* (This field defines whether a Remote-Party-ID SIP header should be sent. This typically defaults to NO.)
5. Now find the Account section and provide the following:

   1. **username:** Your Telnyx SIP account username
   2. **password:** Your Telnyx SIP account password
   3. **SIP server or proxy:** *sip.telnyx.com*
   4. **domain:** *sip.telnyx.com*
   5. **register:** *Yes (inbound and outbound calls)*

   ![PBXes online portal.](_images/91d34846a0763b4e.png)

[Back to Top](#h_67de6d5252)

## 2. Configure inbound routing

In this step, you'll create an inbound routing dial rule and an outbound routing dial rule.

1. Log into your pbxes.com web portal using the login dialogue on the top-right of the page.
2. Expand **Inbound Routing** in the left-hand menu and click on **Add Route.**
3. In the **Options** section, you can choose an Outbound Caller ID if you wish.   
   ​  
   ​***Note*** *the following Caller ID naming conventions:*

   1. Call ID name should be in CAPITAL LETTERS. This is easier to read on some devices.
   2. No special characters will be displayed. Don't use them. Spaces are allowed.
   3. Max 15 characters (Many Canadian carriers truncate a caller ID longer than 15 characters)
4. In the **Dial Rules** section make sure that:

   1. **Dial Rules:** The basic *1+NXXNXXXXXX* will apply to the pattern in the outbound route

   ![inbound routing dial rule section. ](_images/490642a7d43514c6.png)

[Back to Top](#h_67de6d5252)

## 3. Configure outbound routing

In this step, you'll create an outbound routing dial rule and an outbound routing dial rule.

1. Log into your pbxes.com web portal using the login dialogue on the top-right of the page.
2. Expand **Outbound Routing** in the left-hand menu and click on **Add Route.**
3. In the **Add Route** section, enter the following details:

   1. **Route Name:** *Telnyx\_out* or something similar that makes sense to you
   2. **Trunk Sequence:** You should see *SIP/Telnyx* as an option in the dropdown. Select this.
4. In the **Set Destination** section, enter the following details:

   1. **Custom Dial Patterns:** *NXXNXXXXXX* (this is the basic pattern)

   ![outbound routing dial rule section.](_images/b7ec3a8d02272793.png)

That's it, you've now configured a PBXes SIP trunk with Telnyx.

[Back to Top](#h_67de6d5252)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, check out:

* [PBXes premium account options](https://www1.pbxes.com/shop.php)
* [PBXes user documentation](https://www1.pbxes.com/community.php?display=wiki) (if you wish to read the page in English, right-click on the page and select **Translate to English** from the menu)
* [PBXes user forum](https://www1.pbxes.com/community.php?display=forum)

---

Related Articles

[FreePBX Trunk Settings With Telnyx](https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx)[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Xorcom PBX: SIP Trunk](https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk)[BYOC: Telnyx & Genesys](https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys)

Did this answer your question?

😞😐😃

Table of contents
