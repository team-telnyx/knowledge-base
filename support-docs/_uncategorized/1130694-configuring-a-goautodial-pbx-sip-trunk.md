---
source_url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
scraped: 2026-06-11
---

Configuring a GoAutoDial PBX SIP Trunk | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring a GoAutoDial PBX SIP Trunk

In this article we will walk you through configuring a GoAutoDial PBX user/pass trunk with Telnyx.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_45171fa155)

[GOautodial](https://goautodial.com/) is a free, enterprise-grade open source omni-channel contact center system designed and built for businesses of all sizes. It boasts inbound and outbound (predictive and preview), and blended dialing, WebRTC, real-time dashboard used to quickly track agent activities, reports, analytics, and more. It is REST-powered under the hood and was proudly built using trusted open-source tech.

Some more of the major GOautodial features include:

* Predictive, preview and manual dialing + inbound IVR and ACD
* Customer Relationship Manager (CRM)
* Ticketing system (under development)
* Instant messaging (under development)
* Social media (under development)

Additional documentation:

* [GOautodial documentation](https://goautodial.org/projects/goautodialce/wiki)
* [GOautodial forums](https://goautodial.org/projects/goautodialce/boards)
* [GOautodial github](https://goautodial.org/)
* [GOautodial system structure](https://goautodial.org/projects/goautodialce/wiki/GOautodial_System_Structure)
* [FAQ](https://goautodial.org/projects/goautodialce/wiki/FAQ)

---

# Instructions for Configuring GOautodial

In this activity you will:

1. [Configure a SIP trunk](#h_0548128ff3)
2. [Add account details and a dial plan](#h_88371e1982)
3. [Set up an outbound call campaign](#h_43c46e2528)
4. [Set up an inbound call campaign](#h_5748cafcf6)
5. [Import your list of call leads](#h_ae79f61a67)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* [Download](https://goautodial.org/projects/goautodialce/wiki/Goautodial_Getting_Started_Guidev4) and [install](https://goautodial.org/projects/goautodialce/wiki/Goautodial_Getting_Started_Guidev4) GOautodialer
* Work through GOautodialer's [Getting Started guide](https://goautodial.org/projects/goautodialce/wiki/Goautodial_Getting_Started_Guidev4) up to and including logging into the dashboard (You can stop here, as the steps that follow require Telnyx-specific settings)

**Video walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for GOautodial/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Configure a SIP trunk

The first section will walk you through configuring your Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks) with GOautodial.

1. Log into your GOautodial dashboard page and, in the left-hand navigation, find **Settings** and expand it.
2. Click on **Carriers** to open the Carriers page and then click the **+** sign in the lower right corner to add a new carrier.

   [![The GOautodial dashboard page. ](https://downloads.intercomcdn.com/i/o/441265515/b25a94115b3a584af297b0b4/Carrier1.png?expires=1781167500&signature=5a87ccaafd78d77ad65b13a6d9fcf17ada159db4d75696be4fe04f68744cd564&req=cCQmFM97mIBaFb4f3HP0gNSPYE%2F12haMiWnKtnMIXYqlSs8wQo9p49vcMYAt%0AsBA%3D%0A)](https://downloads.intercomcdn.com/i/o/441265515/b25a94115b3a584af297b0b4/Carrier1.png?expires=1781167500&signature=5a87ccaafd78d77ad65b13a6d9fcf17ada159db4d75696be4fe04f68744cd564&req=cCQmFM97mIBaFb4f3HP0gNSPYE%2F12haMiWnKtnMIXYqlSs8wQo9p49vcMYAt%0AsBA%3D%0A)
3. You will be asked to choose a carrier type. In this case, choose *Manual*.
4. In the Add New Carrier wizard, provide the following values:

   1. **Carrier ID:** *Telnyx*
   2. **Carrier Name:** *Telnyx*
   3. **Carrier Description:** You can use whatever makes the most sense to you. In this example, we simply named it *Telnyx Trunk*.
   4. **User Group:** *All User Groups*
   5. **Authentication:** *Registration* (As we are authenticating with a username and password)
   6. **Username:** Your Telnyx account username
   7. **Password:** Your Telnyx account password
   8. **Server IP/Host:** *sip.telnyx.com*
   9. **Dial Prefix:** The dial prefix setting will automatically dial a predefined number before every number you dial. For example: If your telephone system requires a 9 to dial an outside number, or a country-prefix to dial another country.
   10. **Codecs:** Set codec preferences here. Telnyx supports the following [audio codecs](https://telnyx.com/resources/codecs-affect-voip-sound-quality):

       1. ulaw(g711u)
       2. alaw(g711a)
       3. g722
       4. g729
   11. **DTMF Mode:** *RFC2833*
   12. **Protocol:** *SIP*
   13. **Port:** *5060* if you have not enabled TLS encryption. If you have, choose *5061*.
   14. **Active:** *Yes* (if you wish to activate the trunk now. Otherwise, you can activate it in the future by going back to your Carriers page and editing your trunk.

       [![Add New Carrier wizard page on GOautodial portal. ](https://downloads.intercomcdn.com/i/o/442399163/f2f42c688c60e6c8fae2495b/Carrier51.png?expires=1781167500&signature=737a643f3430e500dbb30ec6e62328778542cd5e0167893d6ca52ddc9892fed7&req=cCQlFcB3nIdcFb4f3HP0gBMs08nRIzwAxkFO4%2FxHfu9XuW1RYB3DPmPjkVq2%0AImg%3D%0A)](https://downloads.intercomcdn.com/i/o/442399163/f2f42c688c60e6c8fae2495b/Carrier51.png?expires=1781167500&signature=737a643f3430e500dbb30ec6e62328778542cd5e0167893d6ca52ddc9892fed7&req=cCQlFcB3nIdcFb4f3HP0gBMs08nRIzwAxkFO4%2FxHfu9XuW1RYB3DPmPjkVq2%0AImg%3D%0A)

       [![Goautodial DTMF entry point. ](https://downloads.intercomcdn.com/i/o/442400180/2b25abbac4f5708af0a2734c/Carrier4.png?expires=1781167500&signature=8ead84e8a61a3db6fc7377d8eebb3501d3fbac827363beeae4cf0c73a7602e08&req=cCQlEsl%2BnIlfFb4f3HP0gFI55FqwhppsJCEoHhn%2FwEyIFtUqa2nYG9XVuwyS%0AFXE%3D%0A)](https://downloads.intercomcdn.com/i/o/442400180/2b25abbac4f5708af0a2734c/Carrier4.png?expires=1781167500&signature=8ead84e8a61a3db6fc7377d8eebb3501d3fbac827363beeae4cf0c73a7602e08&req=cCQlEsl%2BnIlfFb4f3HP0gFI55FqwhppsJCEoHhn%2FwEyIFtUqa2nYG9XVuwyS%0AFXE%3D%0A)

[Back to Top](#h_45171fa155)

## 2. Add account details and dial plan

In this section, we use the advanced configuration option to add a dial plan.

1. Still on the **Carrier** page, with your newly created trunk open, click **Advance Configuration** and confirm or provide the following:

   1. **Account Entry:**

      ```
      Account Entry: [telnyx]  
      disallow=all  
      allow=ulaw  
      allow=alaw  
      type=friend  
      dtmfmode=rtc2833  
      qualify=yes  
      nat=yes  
      host=sip.telnyx.com  
      insecure=invite
      ```
   2. **Dialplan Entry:**

      ```
      exten => _X.,1,AGI(agi://127.0.0.1:4577/call_log)  
      exten => _NXXNXXXXXX.,1,Dial(SIP/${EXTEN}@telnyx)  
      exten => _1NXXNXXXXXX.,1,Dial(SIP/${EXTEN}@telnyx)  
      exten => _6468688074,1,Dial(SIP/8001@default)  
      exten => _16468688074,1,Dial(SIP/8001@default)
      ```

[Back to Top](#h_45171fa155)

## 3. Set up an outbound campaign

Today, manual cold calling is considered inefficient. Your call center's success is improved by setting up campaigns. Outbound campaigns effectively start conversations with leads, build brand awareness, and convert the target audience to loyal clients. It’s vital to create a detailed execution plan and hire the right reps to boost your dialing project’s effectiveness. In this section, you'll learn the mechanics of setting up your outbound campaign.

1. Log into your portal as an administrator. From the left-hand navigation, expand **Telephony** and click **Campaigns**.

   [![Portal for setting up an outbound campaign. ](https://downloads.intercomcdn.com/i/o/441349989/d34bc75052e2c35325a4ebca/Ocampaign1.png?expires=1781167500&signature=95d666d259af9c03faeea3063c44a640bd322497716563c9022a0f50d542e816&req=cCQmFc13lIlWFb4f3HP0gENnM1Uq6Hwmsnt1KKxum0lTv9OJ6AlW%2BM6xQ2ey%0A0%2F8%3D%0A)](https://downloads.intercomcdn.com/i/o/441349989/d34bc75052e2c35325a4ebca/Ocampaign1.png?expires=1781167500&signature=95d666d259af9c03faeea3063c44a640bd322497716563c9022a0f50d542e816&req=cCQmFc13lIlWFb4f3HP0gENnM1Uq6Hwmsnt1KKxum0lTv9OJ6AlW%2BM6xQ2ey%0A0%2F8%3D%0A)
2. Click the **+** to add a new campaign. When prompted for the **Campaign Type**, select *Outbound*.

   [![Portal for setting campaign types. ](https://downloads.intercomcdn.com/i/o/441350779/1f0a6609893404204283c92e/Ocampaign2.png?expires=1781167500&signature=238d1a5ff1c2d1d8c5fc11ad6f9bb3f9d8459592459a75585b301ee6918346a8&req=cCQmFcx%2BmoZWFb4f3HP0gAzGpTRxSYbuvJgtJ%2BSoG%2F7ZWOSKgJ224njqfVuu%0A%2FdA%3D%0A)](https://downloads.intercomcdn.com/i/o/441350779/1f0a6609893404204283c92e/Ocampaign2.png?expires=1781167500&signature=238d1a5ff1c2d1d8c5fc11ad6f9bb3f9d8459592459a75585b301ee6918346a8&req=cCQmFcx%2BmoZWFb4f3HP0gAzGpTRxSYbuvJgtJ%2BSoG%2F7ZWOSKgJ224njqfVuu%0A%2FdA%3D%0A)
3. Click the link in the **Campaign ID** column to check the campaign settings. you can also select or set preferred settings for your campaign. On the **Basic Settings** tab ensure that you set:

   1. **Dial Method:** You have some choices:

      1. *Manual, Auto\_Dial*
      2. *Predictive*
   2. **Auto Dial Level:** You have some choices:

      1. *Slow*
      2. *Normal*
      3. *Max*
      4. *High*
   3. **Carrier to use for this Campaign:** *Telnyx*. If this option isn't available, revisit section 1 to ensure that you have added Telnyx as a carrier.

      [![Campaign ID column in campaign setting portal. ](https://downloads.intercomcdn.com/i/o/441353889/0e9ba37be3b9125b0f039279/Ocampaign3.png?expires=1781167500&signature=4cb96843e913f8d175ce834e8a09e2aefcb548df71952d15aafb62b39b9ddde6&req=cCQmFcx9lYlWFb4f3HP0gITHEJyz2zIUbFpd1g4iw%2FKJuu8Y%2FBXmxAJdTTXl%0AhOw%3D%0A)](https://downloads.intercomcdn.com/i/o/441353889/0e9ba37be3b9125b0f039279/Ocampaign3.png?expires=1781167500&signature=4cb96843e913f8d175ce834e8a09e2aefcb548df71952d15aafb62b39b9ddde6&req=cCQmFcx9lYlWFb4f3HP0gITHEJyz2zIUbFpd1g4iw%2FKJuu8Y%2FBXmxAJdTTXl%0AhOw%3D%0A)
4. Click **Update** once done.  
   ​

[Back to Top](#h_45171fa155)

## 4. Set up an inbound campaign

Inbound marketing campaigns are concentrated efforts that align all of your marketing channels around a single message and goal. It starts with a marketing offer -- something valuable and relevant for your audience that you promote through your marketing channels. In this section, you'll learn the mechanics of setting up an inbound call campaign.

1. Log into your portal as an administrator. From the left-hand navigation, expand **Telephony** and click **Campaigns**.

   [![Inbound campaign settings portal. ](https://downloads.intercomcdn.com/i/o/441355653/4705ba7c070892d6cb25606c/Icampaign1.png?expires=1781167500&signature=bcf3a867e6b7c882529de79f8522777dba462c5548522178daa3d7c9f9ca15e6&req=cCQmFcx7m4RcFb4f3HP0gGO6HYkMN5njMuVuwlABZwc1D%2FjSSPt7RuJoaJJG%0AC%2Fg%3D%0A)](https://downloads.intercomcdn.com/i/o/441355653/4705ba7c070892d6cb25606c/Icampaign1.png?expires=1781167500&signature=bcf3a867e6b7c882529de79f8522777dba462c5548522178daa3d7c9f9ca15e6&req=cCQmFcx7m4RcFb4f3HP0gGO6HYkMN5njMuVuwlABZwc1D%2FjSSPt7RuJoaJJG%0AC%2Fg%3D%0A)
2. Click the **+** to add a new campaign. When prompted for the **Campaign Type**, select *Inbound*.

   [![Campaign types in inbound campaign settings. ](https://downloads.intercomcdn.com/i/o/441355900/0861e0ec0143dbe22c33b4c4/Icampaign2.png?expires=1781167500&signature=a7321d60d862ab50c260160d3fc34f86086338409ba1a9d2ba170ae6a8c588f5&req=cCQmFcx7lIFfFb4f3HP0gNjF2kiC0AiSobjju2azd1Uf44nExembMDT%2FrmI9%0ADx0%3D%0A)](https://downloads.intercomcdn.com/i/o/441355900/0861e0ec0143dbe22c33b4c4/Icampaign2.png?expires=1781167500&signature=a7321d60d862ab50c260160d3fc34f86086338409ba1a9d2ba170ae6a8c588f5&req=cCQmFcx7lIFfFb4f3HP0gNjF2kiC0AiSobjju2azd1Uf44nExembMDT%2FrmI9%0ADx0%3D%0A)
3. Complete the fields in the **Campaign Wizard > Inbound** and ensure that:

   1. **Call Route:** *Ingroup (default)*

      [![Campaign wizard to inbound page. ](https://downloads.intercomcdn.com/i/o/441356361/1e8b0d25b6493975de66491d/Icampaign3.png?expires=1781167500&signature=e7cdc54774e358c9f15b38dd136706b68e002093f5ab9ee313e2920c2f0ad627&req=cCQmFcx4nodeFb4f3HP0gIfEPE5yQZx5p64ni12Aty0Xw3iL%2FZK4gCVGUGvh%0Asjo%3D%0A)](https://downloads.intercomcdn.com/i/o/441356361/1e8b0d25b6493975de66491d/Icampaign3.png?expires=1781167500&signature=e7cdc54774e358c9f15b38dd136706b68e002093f5ab9ee313e2920c2f0ad627&req=cCQmFcx4nodeFb4f3HP0gIfEPE5yQZx5p64ni12Aty0Xw3iL%2FZK4gCVGUGvh%0Asjo%3D%0A)
4. Once your campaign has been created, return to the Campaigns screen (**Telephony > Campaigns**) and click the link in the **Campaign ID** column to check the campaign settings. On the **Basic Settings** tab ensure that you set:

   1. **Carrier to use for this Campaign:** *Telnyx*. If this option isn't available, revisit section 1 to ensure that you have added Telnyx as a carrier.

      [![Campaign carrier and ID settings. ](https://downloads.intercomcdn.com/i/o/441359107/16d6888b6565ad27564df32b/Icampaign4.png?expires=1781167500&signature=20b80fd442d1f6ab52c902e9d169b0b5dc228d25c34db062f9463657487ae4ed&req=cCQmFcx3nIFYFb4f3HP0gP3gqaNHgNEF%2B4Z2VHYhZzTfdPO%2Fxo%2FoPpJNG258%0AMUQ%3D%0A)](https://downloads.intercomcdn.com/i/o/441359107/16d6888b6565ad27564df32b/Icampaign4.png?expires=1781167500&signature=20b80fd442d1f6ab52c902e9d169b0b5dc228d25c34db062f9463657487ae4ed&req=cCQmFcx3nIFYFb4f3HP0gP3gqaNHgNEF%2B4Z2VHYhZzTfdPO%2Fxo%2FoPpJNG258%0AMUQ%3D%0A)
5. Now click on the **Advanced Settings** tab and ensure that:

   1. **INBOUND GROUPS:** Select all options that you'll require

      1. **AGENTDIRECT:** *Single Agent Direct Queue*
      2. **AGENTDIRECT\_CHAT:** *Single Agent Direct Queue for Chats*
   2. **Allowed Transfer Groups:** Select all options that you'll require

      1. **AGENTDIRECT:** *Single Agent Direct Queue*
      2. **AGENTDIRECT\_CHAT:** *Single Agent Direct Queue for Chats*

      [![Advanced Settings tab. ](https://downloads.intercomcdn.com/i/o/441361086/4290f3f5f0cec7d321979cd8/Icampaign5.png?expires=1781167500&signature=669822bdce1cfa98dc1b7de698a592105214437a45c2ae5d4f7d17c3ba35a3f0&req=cCQmFc9%2FnYlZFb4f3HP0gC%2FYvTIv%2Bv9DvO1GeCIMzDh7MuYZSRlxsm%2B8wlAP%0AaRQ%3D%0A)](https://downloads.intercomcdn.com/i/o/441361086/4290f3f5f0cec7d321979cd8/Icampaign5.png?expires=1781167500&signature=669822bdce1cfa98dc1b7de698a592105214437a45c2ae5d4f7d17c3ba35a3f0&req=cCQmFc9%2FnYlZFb4f3HP0gC%2FYvTIv%2Bv9DvO1GeCIMzDh7MuYZSRlxsm%2B8wlAP%0AaRQ%3D%0A)

|  |
| --- |
| ***Note:*** *Be sure to advise your agent to select always the ingroup on the **INBOUND CAMPAIGN** once they log in.*  [Inbound campaign icon interface.](https://downloads.intercomcdn.com/i/o/441361768/695af9b9562cacf4ce3e0dbc/Icampaign6.png?expires=1781167500&signature=e9f89c98f4c4884d6843c6d8892e4547551f49fcb14fb7ad8071a98b28394cad&req=cCQmFc9%2FmodXFb4f3HP0gHzCvfyf3mlnXfBp%2FJeS81PwsQvRXROgofb%2FTgX2%0AfJ8%3D%0A)  [Inbound campaign contact information.](https://downloads.intercomcdn.com/i/o/441361947/1af926bf52418dcdd4ec8fcc/Icampaign7.png?expires=1781167500&signature=e3f48fb28eb6a50a2d77b7ea9c58690c5f07fe51b76b63afc802531210a295ba&req=cCQmFc9%2FlIVYFb4f3HP0gOMDJwovM1hC2jzfZSNJ5wJtaIxx%2BS6JDkg04CDj%0A%2F10%3D%0A) |

[Back to Top](#h_45171fa155)

## 5. Import your list of call leads

Before your agents hit the phones, you'll need to make sure you've uploaded a properly formatted set of leads. This section will walk you through this activity.

1. Log into your GOautodial dashboard page and, in the left-hand navigation, find **Telephony** and expand it.
2. Click on **List** to open the List page and then click the **+** sign in the lower right corner to add a new list of leads.

   [![Interface for importing list of call leads. ](https://downloads.intercomcdn.com/i/o/441367036/054a0537796c007cf92549ee/golist1.png?expires=1781167500&signature=505eef35edf0e7ed693a963b6dca75500552b2521cb42bdff548fa6ca8ab7035&req=cCQmFc95nYJZFb4f3HP0gNeyy9P2E2ug6qLMDQVoKtP7yEq%2FWTvYL4KgixPK%0Ar2g%3D%0A)](https://downloads.intercomcdn.com/i/o/441367036/054a0537796c007cf92549ee/golist1.png?expires=1781167500&signature=505eef35edf0e7ed693a963b6dca75500552b2521cb42bdff548fa6ca8ab7035&req=cCQmFc95nYJZFb4f3HP0gNeyy9P2E2ug6qLMDQVoKtP7yEq%2FWTvYL4KgixPK%0Ar2g%3D%0A)
3. Now you'll upload a .csv file containing your leads. Make sure that you've followed the lead file format illustrated in the following image and save as .csv comma delimited. (To view this image in full size, right-click on the image and select **Open Image in New Tab** from the context menu.)

   [![.csv file containing leads. ](https://downloads.intercomcdn.com/i/o/441366060/73e42c70e11c4747d2cc9725/golist2.png?expires=1781167500&signature=4298ca603109c17eb8c42bc5cfb5befac2a334b2ca12f9196589f6751c84708b&req=cCQmFc94nYdfFb4f3HP0gJYQxIAlPeqGTnykIxcca4NgdDh1I490tK%2B%2Fo66%2B%0A6Sk%3D%0A)](https://downloads.intercomcdn.com/i/o/441366060/73e42c70e11c4747d2cc9725/golist2.png?expires=1781167500&signature=4298ca603109c17eb8c42bc5cfb5befac2a334b2ca12f9196589f6751c84708b&req=cCQmFc94nYdfFb4f3HP0gJYQxIAlPeqGTnykIxcca4NgdDh1I490tK%2B%2Fo66%2B%0A6Sk%3D%0A)
4. Lead status will be posted after you have successfully uploaded your lead file, Click **OK** once this upload is complete.

   [![Data processing completion interface. ](https://downloads.intercomcdn.com/i/o/441366727/b446d87de3e7485ca8aff090/golist3.png?expires=1781167500&signature=456b59b6a6e3e3adda30ffabe20d07247ad811c40f8921f0de37fa37e27e0dc5&req=cCQmFc94moNYFb4f3HP0gKQREUH3jrh2W4zRr8kUjVTDfXThGQ6VuFgS0e35%0AtIc%3D%0A)](https://downloads.intercomcdn.com/i/o/441366727/b446d87de3e7485ca8aff090/golist3.png?expires=1781167500&signature=456b59b6a6e3e3adda30ffabe20d07247ad811c40f8921f0de37fa37e27e0dc5&req=cCQmFc94moNYFb4f3HP0gKQREUH3jrh2W4zRr8kUjVTDfXThGQ6VuFgS0e35%0AtIc%3D%0A)

That's it! You've now completed the basic setup activities required to link GOautodial with Telnyx.

|  |
| --- |
| ***Note:*** *There are a number of other activities that do not involve Telnyx that you will want to complete in order to maximize your GOautodial experience. You can find those exercises [here](https://goautodial.org/projects/goautodialce/wiki/Version_4_HOWTOS).* |

[Back to Top](#h_45171fa155)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:

* [GOautodial documentation](https://goautodial.org/projects/goautodialce/wiki)
* [GOautodial forums](https://goautodial.org/projects/goautodialce/boards)
* [GOautodial github](https://goautodial.org/)
* [GOautodial system structure](https://goautodial.org/projects/goautodialce/wiki/GOautodial_System_Structure)
* [FAQ](https://goautodial.org/projects/goautodialce/wiki/FAQ)

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[Asterisk: Configure an Asterisk IP trunk](https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk)[How to configure a Thirdlane PBX](https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx)[Configuring a GOautodial PBX IP Trunk](https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk)[Configuring an Elastix 4 PBX Trunk](https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk)

Did this answer your question?

😞😐😃

Table of contents
