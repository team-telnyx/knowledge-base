---
source_url: https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing
scraped: 2026-06-11
---

Configuring Telnyx with Microsoft Teams Direct Routing | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring Telnyx with Microsoft Teams Direct Routing

Unlock seamless integration: Set up Microsoft Teams Direct Routing with Telnyx. Dive in now!

C

Written by Customer Success

February 20, 2026

Table of contents

[Jump to Instructions](#h_73f0b860c1)

[Direct Routing](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-plan) with [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) allows businesses to connect external phone lines to Microsoft Teams and use Teams as an office phone system instead of a legacy PBX system. This means you can maintain your existing [SIP trunks](https://telnyx.com/products/sip-trunks) and PSTN connectivity -- retaining control over your numbers and realizing cost savings over the MS Teams Calling Plans.

This article will guide you on how to use Telnyx as a PSTN provider for Microsoft Teams Direct Routing. Once set up is complete, Telnyx customers will be able to use numbers purchased from Telnyx to send and receive calls via the PSTN from the same Teams account.

Additional resources:

* [Microsoft Teams Direct Routing documentation](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-plan)
* [Microsoft support](https://support.microsoft.com/en-US)

---

# Instructions for configuring Telnyx with Microsoft Teams Direct Routing

|  |
| --- |
| ***Note:*** *This integration is carried out via the [Telnyx MS Teams SBC](https://telnyx.com/resources/integrated-sbc-direct-routing), which interconnects Microsoft Teams with the Telnyx telephony platform. Telnyx SBC uses the base domain mstsbc.telnyx.tech, and Telnyx customers will be able to interconnect using a subdomain of mstsbc.telnyx.tech and a token for authentication.* |

In this activity you will:

1. [Add a SIP connection in Telnyx](#h_f21691d342)
2. [Assign a number to the Telnyx SBC Connection](#h_ddd7742f7e)
3. [Add your SIP Connection to your Outbound Voice Profile](#h_ddd7742f7e)
4. [Add a subdomain to the customer tenant in Microsoft](#h_ac2ea5e081)
5. [Activate the subdomain](#h_1c9c29c5f4)
6. [Add the Telnyx SBC in Direct Routing](#h_70157d551b)
7. [Create voice routes](#h_a2f1949f03)
8. [Enroll the SBC](#h_8a68f47b55)
9. [Add the PTSN usage records](#h_2db33bd935)
10. [Configure voice routing policies and apply dial plan](#h_6f3d53fce8)
11. [Assign dial plan and voice routing policies](#h_a6bb824e85)
12. [Assign Telnyx DID to on-premises PSTN connectivity](#h_9aa246fcc1)
13. [Make some test calls with Microsoft Teams](#h_dea56744cd)

## **Pre-requisites**

* You'll need a Telnyx account with a purchased number. Learn how to set up your account [here](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).
* Assign a **Microsoft Teams E5** license to each user who will be making and receiving calls to the PSTN
* Make sure you can sign in to the Microsoft 365 admin center as a Global Administrator.

  + To validate the role you have, please sign in to the Microsoft 365 admin center (<https://portal.office.com>) and go to **Users → Active Users**. Click your user and under **Account → Roles** click **Manage roles.** Verify that you have a Global Administrator role applied to your account.

    [![Microsoft 365 admin center portal. ](https://downloads.intercomcdn.com/i/o/350367801/9b1fb848bdb655bc1c5cb7c9/image.png?expires=1781168400&signature=c6badecaec516379bfbbd3afd770410bca2deb427e7ca500988912dc8a53a5d8&req=dyUnFc95lYFeFb4f3HP0gFuxNQcIf8aQ2CW5gemgNZtZqpjx8vVEAExNsHjC%0Aap4%3D%0A)](https://downloads.intercomcdn.com/i/o/350367801/9b1fb848bdb655bc1c5cb7c9/image.png?expires=1781168400&signature=c6badecaec516379bfbbd3afd770410bca2deb427e7ca500988912dc8a53a5d8&req=dyUnFc95lYFeFb4f3HP0gFuxNQcIf8aQ2CW5gemgNZtZqpjx8vVEAExNsHjC%0Aap4%3D%0A)

    [![Administration roles management settings. ](https://downloads.intercomcdn.com/i/o/350368826/21185ec0bb0c8384b8fb5698/image.png?expires=1781168400&signature=3d09fa70b8d862b70aed31de8955b4f879e62553d6ecb5dce44b82410974292c&req=dyUnFc92lYNZFb4f3HP0gGaW55Oe%2FqExOrb9%2BQwCFTrZD8Kh18zTXKqTAC55%0A5MU%3D%0A)](https://downloads.intercomcdn.com/i/o/350368826/21185ec0bb0c8384b8fb5698/image.png?expires=1781168400&signature=3d09fa70b8d862b70aed31de8955b4f879e62553d6ecb5dce44b82410974292c&req=dyUnFc92lYNZFb4f3HP0gGaW55Oe%2FqExOrb9%2BQwCFTrZD8Kh18zTXKqTAC55%0A5MU%3D%0A)
* Procure a Microsoft license. You can find different license options in the table below. You'll need one of these base plans and an add-on if necessary:

|  |  |
| --- | --- |
| **BASE PLAN** | **ADD ON REQUIRED FOR DIRECT ROUTING** |
| Microsoft Business Basic / Standard / Premium | Microsoft 365 Business Voice without Calling Plan |
| Microsoft Office 365 Enterprise E1 / E3 / F3 / A1 / A3 | Phone System |
| Microsoft Office 365 Enterprise E5 | No add on required |

## 1. Add a SIP connection in Telnyx

Once you have set up your Telnyx account, you will have to set up a new connection for the Telnyx SBC on the [SIP Connections page](https://portal.telnyx.com/#/app/connections).

1. Click on the **Create SIP Connection** button and choose a name for your connection. You should see options that will allow you to choose a SIP Connection Type on the next page. For this connection, we must choose **MS Teams Direct Routing SBC.**

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892351247/b090d25dd4475a210775576d2bbc/image.png?expires=1781168400&signature=aca37e1de845ec464f99f33e474dd0a7884a70f09c46c34a8226405798ac02cb&req=dSguFMp7nINbXvMW1HO4zVqFVumSLlaq9om1CF7cOm3QmrO6EnHLKUVPtZqW%0Ald4a%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892351247/b090d25dd4475a210775576d2bbc/image.png?expires=1781168400&signature=aca37e1de845ec464f99f33e474dd0a7884a70f09c46c34a8226405798ac02cb&req=dSguFMp7nINbXvMW1HO4zVqFVumSLlaq9om1CF7cOm3QmrO6EnHLKUVPtZqW%0Ald4a%0A)
2. You will want to take note of the auto-generated subdomain that appears as it will be needed at different stages of the setup.
3. Click **Next** and follow the guide to set up your **Authentication and Routing** details on the following page, followed by your **Configuration** details.

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892380993/16be5d09b003590be7fa9e585518/image.png?expires=1781168400&signature=518b9e8af7d72e76adcdd94c6ff039ba212820667ad3aaac91029473f89ea9cb&req=dSguFMp2nYhWWvMW1HO4zWNu9g5hI9VpAOTH1Bkp0tlgS1CvOhNkOl1ovfhM%0AD9IX%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892380993/16be5d09b003590be7fa9e585518/image.png?expires=1781168400&signature=518b9e8af7d72e76adcdd94c6ff039ba212820667ad3aaac91029473f89ea9cb&req=dSguFMp2nYhWWvMW1HO4zWNu9g5hI9VpAOTH1Bkp0tlgS1CvOhNkOl1ovfhM%0AD9IX%0A)

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892394069/4247303aa630656dc4310a0d6d15/image.png?expires=1781168400&signature=ccde998527365a9052a232c8cae4b4330ed7627b23f7264292eceee7132ea51c&req=dSguFMp3mYFZUPMW1HO4zS8Cf8BbN0zGf6r9Yo6kJJsRQVLPsS8CoO99yJEg%0ApMiW%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892394069/4247303aa630656dc4310a0d6d15/image.png?expires=1781168400&signature=ccde998527365a9052a232c8cae4b4330ed7627b23f7264292eceee7132ea51c&req=dSguFMp3mYFZUPMW1HO4zS8Cf8BbN0zGf6r9Yo6kJJsRQVLPsS8CoO99yJEg%0ApMiW%0A)
4. Scroll down and Click **Next**.

[Back to Top](#h_73f0b860c1)

## 2. Set up Inbound and Outbound details

Now, you will set up **Inbound** and **Outbound** details for the SIP Connection. You will also be able to assign it an Outbound Voice Profile.

For the Inbound settings, there are a variety of options you may configure to your preference and for the Outbound settings, it is critical to keep in mind the details of the Outbound profile being assigned. You can see these from the Voice>Settings> Outbound profiles page.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892399645/9eda9d01349c8627f6c8a48795b7/image.png?expires=1781168400&signature=8e3a8a8c9b5221bda9c30299a29fde9805b6ea2b0b4e05750ba3c7afd93a9677&req=dSguFMp3lIdbXPMW1HO4zXKv1kNNOvZ7JEBA46AkX5C6qYk6iPM7CERJhKer%0AR%2BCaETdQ7mezhW9bW7g%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892399645/9eda9d01349c8627f6c8a48795b7/image.png?expires=1781168400&signature=8e3a8a8c9b5221bda9c30299a29fde9805b6ea2b0b4e05750ba3c7afd93a9677&req=dSguFMp3lIdbXPMW1HO4zXKv1kNNOvZ7JEBA46AkX5C6qYk6iPM7CERJhKer%0AR%2BCaETdQ7mezhW9bW7g%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892410755/ab92d8d279c9ff7fc77abe0b3b2b/image.png?expires=1781168400&signature=8bcd3d96c1f65f9ba9c9da925a8cdee8b000b7cccec95bb0282ba376f4a1ad4a&req=dSguFM1%2FnYZaXPMW1HO4ze3AzPRRgPKmmh660T5J86%2FdvvEgNZQagQW0pzQ2%0Anry4YlxTQkv3fQsKC64%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892410755/ab92d8d279c9ff7fc77abe0b3b2b/image.png?expires=1781168400&signature=8bcd3d96c1f65f9ba9c9da925a8cdee8b000b7cccec95bb0282ba376f4a1ad4a&req=dSguFM1%2FnYZaXPMW1HO4ze3AzPRRgPKmmh660T5J86%2FdvvEgNZQagQW0pzQ2%0Anry4YlxTQkv3fQsKC64%3D%0A)

Click **Next.**

[Back to Top](#h_73f0b860c1)

## 3. Assign a number to the Telnyx SBC Connection

You are now required to assign a Number to the MS Teams connection you just created.

1. If you have not done so already as part of your [pre-requisite activities](#h_bb9a5a60b7), you'll need to purchase a number from Telnyx.
2. Once you have a number, navigate to the Numbers section and assign the number to your connection.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892415657/3d93c66995652ce9003b158eda7d/image.png?expires=1781168400&signature=be661be7e2e7a408c1486bd23312d79af32b45aa0fcbc9b28598abe00f4edbeb&req=dSguFM1%2FmIdaXvMW1HO4zcxiP%2FJ0FwCOxkiwhM2%2BvGGViKu6TpIhlNHxeEzA%0AvM1wwQUst1afC7YDjus%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892415657/3d93c66995652ce9003b158eda7d/image.png?expires=1781168400&signature=be661be7e2e7a408c1486bd23312d79af32b45aa0fcbc9b28598abe00f4edbeb&req=dSguFM1%2FmIdaXvMW1HO4zcxiP%2FJ0FwCOxkiwhM2%2BvGGViKu6TpIhlNHxeEzA%0AvM1wwQUst1afC7YDjus%3D%0A)

Alternatively, navigate to the Numbers page in the Telnyx Mission Control Portal and assign your MS Teams connection to the desired DID, as shown below.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892515541/2ea9359e5a86a9f4e7d42e948a76/image.png?expires=1781168400&signature=0f0c7e70ee8546cea3623531f6c21b65689c53a29aa3bc0aed1b129d13fa2d6e&req=dSguFMx%2FmIRbWPMW1HO4zTIIp4cJBGc5XsF19tglEfxcZwxRuXCfw1evatTO%0AY0mT0JGWHIMBDhxxPu4%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1892515541/2ea9359e5a86a9f4e7d42e948a76/image.png?expires=1781168400&signature=0f0c7e70ee8546cea3623531f6c21b65689c53a29aa3bc0aed1b129d13fa2d6e&req=dSguFMx%2FmIRbWPMW1HO4zTIIp4cJBGc5XsF19tglEfxcZwxRuXCfw1evatTO%0AY0mT0JGWHIMBDhxxPu4%3D%0A)

Click **Complete.**

[Back to Top](#h_73f0b860c1)

## **4.** Add a subdomain to the customer tenant in Microsoft

Now that your Mission Control Portal is set up and ready to go, you’ll need to add a subdomain in the Microsoft admin portal before setting up Direct Routing in Microsoft Teams.

In order to do this, you'll need to make sure you have a Microsoft License and are signed into your Microsoft 365 Admin Center as a global administrator, as outlined in your [pre-requisite activities](#h_bb9a5a60b7). Once you have the correct licensure and account privileges, you can continue here.

1. Perform a search for *Domains* within the Microsoft 365 admin center search bar at the top of your screen.
2. Click the **Add Domain** option at the top left and add the auto generated subdomain that corresponds to the SIP Connection we created in [Section 1](#h_f21691d342).

   [![Microsoft 365 Domain Adding center.  ](https://downloads.intercomcdn.com/i/o/350371249/8aef35c0e71697611f4bc093/image.png?expires=1781168400&signature=1140dfab97d742cd893c4108f3cbe765790638a28ba197b8a752f265afdd8d42&req=dyUnFc5%2Fn4VWFb4f3HP0gI%2F9Brn54EX14UIl%2Fl0DAtMOcf367LRilw%2FBTrgP%0AnW8%3D%0A)](https://downloads.intercomcdn.com/i/o/350371249/8aef35c0e71697611f4bc093/image.png?expires=1781168400&signature=1140dfab97d742cd893c4108f3cbe765790638a28ba197b8a752f265afdd8d42&req=dyUnFc5%2Fn4VWFb4f3HP0gI%2F9Brn54EX14UIl%2Fl0DAtMOcf367LRilw%2FBTrgP%0AnW8%3D%0A)
3. Click **Use This Domain** and verify the domain on the following page. Select the **Add a TXT record instead** option**.**

   [![A screenshot showing a domain verification steps.](https://downloads.intercomcdn.com/i/o/350371625/9abfa6e55434c2b537ff1748/image.png?expires=1781168400&signature=53ca71dc29812f66c3a5e9de7ef529339b14785d97db64d229229cfc6b0d1a00&req=dyUnFc5%2Fm4NaFb4f3HP0gB%2B18gHqCDFJzIg%2Bttk7Y7KumF3fh%2FkMRx%2Bxc2ka%0Am%2BY%3D%0A)](https://downloads.intercomcdn.com/i/o/350371625/9abfa6e55434c2b537ff1748/image.png?expires=1781168400&signature=53ca71dc29812f66c3a5e9de7ef529339b14785d97db64d229229cfc6b0d1a00&req=dyUnFc5%2Fm4NaFb4f3HP0gB%2B18gHqCDFJzIg%2Bttk7Y7KumF3fh%2FkMRx%2Bxc2ka%0Am%2BY%3D%0A)
4. Click **Next** and take note of the TXT value displayed.

   [![Information required to verify the domain.](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691815/8d1e523c2fe992599b57f1c8/Information_required_to_verify_the_domain..png?expires=1781168400&signature=cd69b113743f13133472f6bf976ca16e537356c55671f6cacdf00ac6801d6d1e&req=dyQlEMB%2FlYBaFb4f3HP0gJCrH2%2FFuaiViNImMru2PRxam5nWrnTXz72kjK9y%0Av%2B4%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691815/8d1e523c2fe992599b57f1c8/Information_required_to_verify_the_domain..png?expires=1781168400&signature=cd69b113743f13133472f6bf976ca16e537356c55671f6cacdf00ac6801d6d1e&req=dyQlEMB%2FlYBaFb4f3HP0gJCrH2%2FFuaiViNImMru2PRxam5nWrnTXz72kjK9y%0Av%2B4%3D%0A)
5. Navigate back to your MS Teams SBC SIP Connection settings in your Telnyx Mission Control Portal.
6. Navigate to the **Domain Validation** header in the top right corner of the window and paste the TXT Value from MS Teams into the **TXT Value** text box.   
   ​  
   ​***Note:*** *The TXT Name and TLL fields should match the fields shown in the MS 365 admin center, hence why they cannot be edited.*  
   ​*Also, Any user who tries to set the `txt_name` on a MS DR connection to `*.mstsbc.telnyx.tech` will get an error that says*

   ```
   txt_name should not include the '.mstsbc.telnyx.tech' suffix. Use only the identifier portion (e.g. '1234abc' instead of '1234abc.mstsbc.telnyx.tech')
   ```

   [![MS Teams settings in the SIP Connections tab.](https://downloads.intercomcdn.com/i/o/342482514/6100f09ef71d1575de679114/image.png?expires=1781168400&signature=e78df32ee20141b38f25879e3583a2e7e1960b9ad15f8468c64137f3ff86f7d6&req=dyQlEsF8mIBbFb4f3HP0gENei5Ce4ETMaScNcUy5XgAUq%2BUMuuubLw%2Bvh9qi%0Aad0%3D%0A)](https://downloads.intercomcdn.com/i/o/342482514/6100f09ef71d1575de679114/image.png?expires=1781168400&signature=e78df32ee20141b38f25879e3583a2e7e1960b9ad15f8468c64137f3ff86f7d6&req=dyQlEsF8mIBbFb4f3HP0gENei5Ce4ETMaScNcUy5XgAUq%2BUMuuubLw%2Bvh9qi%0Aad0%3D%0A)
7. Click **Save All Changes**.
8. Once you have saved your changes, navigate back to Microsoft 365 admin center and click on the **Verify** button at the bottom.
9. On the next page, select **More Options**.
10. Select **Skip and do this later** and click **Next**.

    [![Check the ‘Skip and do this later’.](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691820/e32adc33fdfabc6f1ef736a2/Check_the____Skip_and_do_this_later___..png?expires=1781168400&signature=863b2a68639c26ad80e6bf3bd8cbce5352602b0e20377e8942bc3c2647e91cb3&req=dyQlEMB%2FlYNfFb4f3HP0gPE9Mq0nZW%2BKnGHekL9ldtRIMv%2BbJ%2FOhN0IViBrf%0AobM%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691820/e32adc33fdfabc6f1ef736a2/Check_the____Skip_and_do_this_later___..png?expires=1781168400&signature=863b2a68639c26ad80e6bf3bd8cbce5352602b0e20377e8942bc3c2647e91cb3&req=dyQlEMB%2FlYNfFb4f3HP0gPE9Mq0nZW%2BKnGHekL9ldtRIMv%2BbJ%2FOhN0IViBrf%0AobM%3D%0A)
11. After this you will be prompted that setup has been complete.

    [![Domain setup is complete](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691822/951024d26b2b5981a80bdf9c/Domain_setup_is_complete.png?expires=1781168400&signature=8650b3841a8d4ecb6dd142d1769cac3f546cb7da11f64a671ec7bb5a86a8c63b&req=dyQlEMB%2FlYNdFb4f3HP0gLfe0XxxmxYyY0NeTiU3TKNt947FlFb%2Fc8P4%2B9%2FJ%0Av%2Fw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691822/951024d26b2b5981a80bdf9c/Domain_setup_is_complete.png?expires=1781168400&signature=8650b3841a8d4ecb6dd142d1769cac3f546cb7da11f64a671ec7bb5a86a8c63b&req=dyQlEMB%2FlYNdFb4f3HP0gLfe0XxxmxYyY0NeTiU3TKNt947FlFb%2Fc8P4%2B9%2FJ%0Av%2Fw%3D%0A)

[Back to Top](#h_73f0b860c1)

## 5. Activate the subdomain

After you have registered a domain name, you’ll need to activate it by adding at least one user and assigning the domain that matches the subdomain that was automatically generated when the SIP Connection was created in [Section 1](#h_f21691d342).

1. From Microsoft 365 Admin Center, navigate to **Users → Active Users → Add a user**.

   [![Microsoft 365 Admin Center](https://downloads.intercomcdn.com/i/o/350373745/f944323f92c6fb0fbf0cafe4/image.png?expires=1781168400&signature=4eaf2027886e806fe3de75c8968309fc3b4f6ce9404b94516ccb2a4691f3f431&req=dyUnFc59moVaFb4f3HP0gJ%2BHZJLihbXvuyIIf%2BvqKsKEicPiuW1JE%2BvJAqy4%0A4%2FE%3D%0A)](https://downloads.intercomcdn.com/i/o/350373745/f944323f92c6fb0fbf0cafe4/image.png?expires=1781168400&signature=4eaf2027886e806fe3de75c8968309fc3b4f6ce9404b94516ccb2a4691f3f431&req=dyUnFc59moVaFb4f3HP0gJ%2BHZJLihbXvuyIIf%2BvqKsKEicPiuW1JE%2BvJAqy4%0A4%2FE%3D%0A)
2. Next, fill in the User details:

   1. **Domain:** Select the Telnyx subdomain (i.e. *yyyy.mstsbc.telnyx.tech*)
   2. Assign E5 license under "Product Licenses".
3. Click **Add.**   
   ​  
   ​***Note*** *that you can remove the E5 license from this user once you're able to add this domain to Direct Routing.*

   [![Activating the subdomain](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691826/28bcfa808b752854e8fb1399/Activating_the_subdomain.png?expires=1781168400&signature=a18e70df811c5076f98bb3dc8d2e27f7c7e420eafef09b258f8a2445af12ee9c&req=dyQlEMB%2FlYNZFb4f3HP0gLOV201OfDpgLOIeQ1LPp5vVGzx3anepY0WSSm52%0AYTw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691826/28bcfa808b752854e8fb1399/Activating_the_subdomain.png?expires=1781168400&signature=a18e70df811c5076f98bb3dc8d2e27f7c7e420eafef09b258f8a2445af12ee9c&req=dyQlEMB%2FlYNZFb4f3HP0gLOV201OfDpgLOIeQ1LPp5vVGzx3anepY0WSSm52%0AYTw%3D%0A)

[Back to Top](#h_73f0b860c1)

## 6. Add the Telnyx SBC in Direct Routing

Next, we'll need to set up the Telnyx SBC subdomain in the Microsoft Teams admin center. To do this, you’ll have to have a Microsoft Teams E5 license assigned to each user who will be making and receiving calls to the PSTN. Keep in mind that the changes on the MS Teams admin portal may take up to 24 hours to take effect.

1. In the left tab of the Microsoft Teams admin center, navigate to **Voice → Direct Routing**.
2. Click the **SBCs** tab.

   [![Direct Routing in the Microsoft Teams admin center.](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691827/83a679be4c2e280dba6d0fea/Direct_Routing_in_the_Microsoft_Teams_admin_center..png?expires=1781168400&signature=1f6103c3323b117fc1617ad3dc5c98e629609f0e827efc7e280cc365a7f2ab4c&req=dyQlEMB%2FlYNYFb4f3HP0gGGYS59fdjvWcXL5Hx8oKi7I0LfpAF7wa3UQkh50%0A9jc%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691827/83a679be4c2e280dba6d0fea/Direct_Routing_in_the_Microsoft_Teams_admin_center..png?expires=1781168400&signature=1f6103c3323b117fc1617ad3dc5c98e629609f0e827efc7e280cc365a7f2ab4c&req=dyQlEMB%2FlYNYFb4f3HP0gGGYS59fdjvWcXL5Hx8oKi7I0LfpAF7wa3UQkh50%0A9jc%3D%0A)
3. Click **Add** and enter the subdomain that was automatically generated in your SIP Connection from [Section 4](#h_ac2ea5e081).
4. Provide the following information:

   1. **Enabled:** Toggle on
   2. **SIP Signaling port:** *5061*
   3. **Send SIP options:** Toggle on
   4. **Forward P-Asserted-Identity (PAI) header:** Toggle on if you would like anonymous calls to connect.

      [![Direct Routing and SBC settings. ](https://downloads.intercomcdn.com/i/o/424925253/19f66687178fe4f2b8a95e76/Enter_SBC_settings_in_Microsoft_Teams_1.png?expires=1781168400&signature=1871c6e4068de14d3ee9729295d4db1fca372e20611b406031e3a32ac64714d5&req=cCIjH8t7n4RcFb4f3HP0gKSFH71wpEVqqh6%2BOoHiiVCs%2FEBXek6qDBdRXMAG%0AnW4%3D%0A)](https://downloads.intercomcdn.com/i/o/424925253/19f66687178fe4f2b8a95e76/Enter_SBC_settings_in_Microsoft_Teams_1.png?expires=1781168400&signature=1871c6e4068de14d3ee9729295d4db1fca372e20611b406031e3a32ac64714d5&req=cCIjH8t7n4RcFb4f3HP0gKSFH71wpEVqqh6%2BOoHiiVCs%2FEBXek6qDBdRXMAG%0AnW4%3D%0A)
5. Click **Save**.
6. Upon successful settings changes, your connection should resemble the example below:

   [![Sample Connection](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691834/c0a20860f2125e62622f3726/Screenshot_from_2021-05-10_09-49-45.png?expires=1781168400&signature=54b29bf430c556e466945898d1fd0ca843611b101d390211cc9ec688af1e1b8b&req=dyQlEMB%2FlYJbFb4f3HP0gHT0%2F8Bpir6LiRwUDAL9hES9gWC8kacQwtKKPyIo%0Aavw%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691834/c0a20860f2125e62622f3726/Screenshot_from_2021-05-10_09-49-45.png?expires=1781168400&signature=54b29bf430c556e466945898d1fd0ca843611b101d390211cc9ec688af1e1b8b&req=dyQlEMB%2FlYJbFb4f3HP0gHT0%2F8Bpir6LiRwUDAL9hES9gWC8kacQwtKKPyIo%0Aavw%3D%0A)

[Back to Top](#h_73f0b860c1)

## 7. Create voice routes

Now you’ll need to create a pass-through voice route.

1. In the left-hand navigation of you 365 admin portal, navigate to **Voice → Direct Routing**.
2. When on the Directing Routing page, select the **Voice routes** tab.
3. Click **Add,** and enter a name and description for your voice route.
4. Set the priority and specify the dialed number pattern as per Telnyx's number plan.  
   ​  
   ​**For US numbers:**

   1. prepend:*1*; match pattern: *NXXNXXXXXX*
   2. prepend: blank; match pattern: *1NXXNXXXXXX*

   **For International numbers:**

   1. prepend: Country Dialing prefix; match pattern: *NXXNXXXXXX*
   2. prepend: blank; match pattern: (Country Dialing prefix)*NXXNXXXXXX*

   [![Creating Voice Routes in Microsoft Teams](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691841/fcf8c262b4cf4102324f6f25/Creating_Voice_Routes_in_Microsoft_Teams.png?expires=1781168400&signature=1b72983009bbd72b5674e2a4b18d0087162e2fbf4c3a941e39618837dd7d540e&req=dyQlEMB%2FlYVeFb4f3HP0gJ97tJ5%2BWDnIHewMtLhCkP0dCd%2FC8cNIdmoOEUej%0A%2BU0%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691841/fcf8c262b4cf4102324f6f25/Creating_Voice_Routes_in_Microsoft_Teams.png?expires=1781168400&signature=1b72983009bbd72b5674e2a4b18d0087162e2fbf4c3a941e39618837dd7d540e&req=dyQlEMB%2FlYVeFb4f3HP0gJ97tJ5%2BWDnIHewMtLhCkP0dCd%2FC8cNIdmoOEUej%0A%2BU0%3D%0A)

[Back to Top](#h_73f0b860c1)

## 8. Enroll the SBC

In this section, we will enroll the SBC with the voice route.

1. From the **Direct Routing** page, navigate to **SBCs enrolled**.
2. Click **Add SBCs**.
3. Select the SBCs you want to enroll.
4. Click **Apply**.

[Back to Top](#h_73f0b860c1)

## 9. Add the PTSN usage records

In this section, you will add Public Switched Telephone Network (PSTN) usage records, which specify a class of call (such as internal, local, or long distance) that can be made by a user or group of users in an organization.

1. From your Microsoft 365 admin portal, use the left-hand navigation to navigate to **Voice → Direct Routing** and find the **PSTN usage records** section.
2. Click **Add PSTN usage**.
3. Select the PSTN records you want to add.

   [![Enrolling SBC’s and adding PSTN usage records in Microsoft Teams.](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/382898348/0f347cf1d01d63ce0779e395/Screenshot_from_2021-08-16_10-44-51.png?expires=1781168400&signature=eac4f89b4ead242a9c487bb7b2ce722ed84d2d23a8ae04a57337d5b553ef05ea&req=dyglHsB2noVXFb4f3HP0gOBpm9mweJvRoYHawMy3PVIFjwLlRkxcp2jXg0bq%0AOgI%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/382898348/0f347cf1d01d63ce0779e395/Screenshot_from_2021-08-16_10-44-51.png?expires=1781168400&signature=eac4f89b4ead242a9c487bb7b2ce722ed84d2d23a8ae04a57337d5b553ef05ea&req=dyglHsB2noVXFb4f3HP0gOBpm9mweJvRoYHawMy3PVIFjwLlRkxcp2jXg0bq%0AOgI%3D%0A)

   ​***Note:*** *This example includes “^(.\*)$”, which allows you to dial any destination. We recommend using a different pattern if you want to include restrictions.*  
   ​
4. Click **Apply**.
5. From the left-hand navigation, under **Voice**, click **Voice Routing Policies.**
6. In the **PSTN usage records** section, click **Add PSTN** usage.
7. Select *Telnyx*.

   [![Adding PSTN Usage Records](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691854/bebd3035ea550e77efed2941/Adding_PSTN_Usage_Records.png?expires=1781168400&signature=5a91adbf2eb2a05292d1c944e112321cee7c7d162b8673f26ce2c8ca485edc4e&req=dyQlEMB%2FlYRbFb4f3HP0gILOaLiFMAH6y%2Byp%2BsTyklPLDe7erVGhAPzAyJIh%0ACSE%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691854/bebd3035ea550e77efed2941/Adding_PSTN_Usage_Records.png?expires=1781168400&signature=5a91adbf2eb2a05292d1c944e112321cee7c7d162b8673f26ce2c8ca485edc4e&req=dyQlEMB%2FlYRbFb4f3HP0gILOaLiFMAH6y%2Byp%2BsTyklPLDe7erVGhAPzAyJIh%0ACSE%3D%0A)
8. Click **Save**.

[Back to Top](#h_73f0b860c1)

## 10. Configure voice routing policies

1. From the left-hand navigation of the 365 admin portal, under **Voice**, click **Voice Routing Policies.**
2. Click **Add**.
3. Type **TELNYX** as the name and add a description.

   [![Adding Voice Routing Policies in Microsoft Teams](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691850/3cc84754c807e04157f11adc/Adding_Voice_Routing_Policies_in_Microsoft_Teams.png?expires=1781168400&signature=14ec70163b21f7bb700118fe75cf0053f90a8b63c36acf72b6e5f6d6230b20f2&req=dyQlEMB%2FlYRfFb4f3HP0gCBIDzttCsPWsPCcLNOXLCfboGY0i%2Bk%2BjIVKpox4%0Aplg%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691850/3cc84754c807e04157f11adc/Adding_Voice_Routing_Policies_in_Microsoft_Teams.png?expires=1781168400&signature=14ec70163b21f7bb700118fe75cf0053f90a8b63c36acf72b6e5f6d6230b20f2&req=dyQlEMB%2FlYRfFb4f3HP0gCBIDzttCsPWsPCcLNOXLCfboGY0i%2Bk%2BjIVKpox4%0Aplg%3D%0A)

[Back to Top](#h_73f0b860c1)

## 11. Assign Dialplan and Voice routing policies

1. From the left-hand navigation of the 365 admin portal, click **Users**.
2. Click the **Policies** tab.
3. Select **Edit** and assign the following:

   1. **Dial Plan:** *Telnyx*
   2. **Voice Routing Policy:** *Telnyx*

      [![Assigning the Telnyx dial plan and voice routing policy in Microsoft Teams.](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691855/89cfc9d143c1c038b7f35a00/Assigning_the_Telnyx_dial_plan_and_voice_routing_policy_in_Microsoft_Teams..png?expires=1781168400&signature=c911a7fb52390d0348ca07255d102ef6504e2aa66aa5a30360ded0401a5d6637&req=dyQlEMB%2FlYRaFb4f3HP0gDr%2BCeznPd3yO%2BmzVqleogwvPu7cqvsQaVJF1ONm%0AOUU%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/342691855/89cfc9d143c1c038b7f35a00/Assigning_the_Telnyx_dial_plan_and_voice_routing_policy_in_Microsoft_Teams..png?expires=1781168400&signature=c911a7fb52390d0348ca07255d102ef6504e2aa66aa5a30360ded0401a5d6637&req=dyQlEMB%2FlYRaFb4f3HP0gDr%2BCeznPd3yO%2BmzVqleogwvPu7cqvsQaVJF1ONm%0AOUU%3D%0A)
4. Click **Apply**.

[Back to Top](#h_73f0b860c1)

## 12. Assign Telnyx DID to on-premises PSTN connectivity

Finally, provision a user with an on-premises phone number. You need to go to [admin.teams.microsoft.com](http://admin.teams.microsoft.com/) > **Manage** **Users . Click on the intended user**

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1274811337/7cc209f1d7e4f1f81b2a5dc99abb/image.png?expires=1781168400&signature=4f06dd5c6ba14b9c7d74896a9731ce6d71478af5315e58db104856eae59a8b0b&req=dSIgEsF%2FnIJcXvMW1HO4ze860SoNRT%2FHUgqhtuZpIcoHxO57dkx86hJlbRVu%0AKVW7l566Wgh4C1ksqlU%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1274811337/7cc209f1d7e4f1f81b2a5dc99abb/image.png?expires=1781168400&signature=4f06dd5c6ba14b9c7d74896a9731ce6d71478af5315e58db104856eae59a8b0b&req=dSIgEsF%2FnIJcXvMW1HO4ze860SoNRT%2FHUgqhtuZpIcoHxO57dkx86hJlbRVu%0AKVW7l566Wgh4C1ksqlU%3D%0A)

Under Account ,   
- Enable the toggle `Enterprise Voice`  
- Click on `Assign a primary phone number`

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1274812770/c80ab08fd5fbf1d2332eca90a1b2/image.png?expires=1781168400&signature=eaea2dbc4b902260614ca43b7895f342dc6a9e07be72cbed0a4e1db8ec9f39c6&req=dSIgEsF%2Fn4ZYWfMW1HO4zXSlwZQ9jqwECww52oWZLQOSp%2BASBJRuOq5kfLBE%0Au3lV%2FKNV9tT2uNmiTS0%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1274812770/c80ab08fd5fbf1d2332eca90a1b2/image.png?expires=1781168400&signature=eaea2dbc4b902260614ca43b7895f342dc6a9e07be72cbed0a4e1db8ec9f39c6&req=dSIgEsF%2Fn4ZYWfMW1HO4zXSlwZQ9jqwECww52oWZLQOSp%2BASBJRuOq5kfLBE%0Au3lV%2FKNV9tT2uNmiTS0%3D%0A)

A New prompt will open to the side. Add the phone number and click on Apply.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1274813744/ee2f7f42c9607a0da403a44c1855/image.png?expires=1781168400&signature=80a6988f1bee5e1275cae24cf31d9b3dd378512f5f989447d1b3bf7715d2eacb&req=dSIgEsF%2FnoZbXfMW1HO4zfeiFKBiWjxqLoSfu2dceO5hkPHqHNdKWUQhixxu%0Ai74a1B08SxIje0y4RoU%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1274813744/ee2f7f42c9607a0da403a44c1855/image.png?expires=1781168400&signature=80a6988f1bee5e1275cae24cf31d9b3dd378512f5f989447d1b3bf7715d2eacb&req=dSIgEsF%2FnoZbXfMW1HO4zfeiFKBiWjxqLoSfu2dceO5hkPHqHNdKWUQhixxu%0Ai74a1B08SxIje0y4RoU%3D%0A)

[Back to Top](#h_73f0b860c1)

## **13. Make some test calls with Microsoft Teams**

Your setup for Microsoft Teams Direct Routing should now be complete. The last step is to make both inbound & outbound test calls from Microsoft Teams to verify the service has been set up correctly.

1. Call a PSTN number from the Microsoft Teams client. You'll want to confirm that the call connects through Telnyx and that there is two-way audio.
2. Call a Telnyx DID that is assigned to both your new Microsoft Teams SIP Connection and one of your Microsoft Teams users from the PSTN (i.e. a cell phone). Confirm that the call is received in Microsoft Teams and that two-way audio is functioning correctly.
3. Check the CDRs from the **Reporting** section of your [Telnyx Mission Control Portal](https://portal.telnyx.com/) to validate that both calls went through correctly.

If you encounter any issues during these tests, please contact us at [support@telnyx.com](mailto:support@telnyx.com) with a note of the number dialled and the date/time. We'll do our best to help you resolve the issue.  
​  
This concludes your set up of Microsoft Teams Direct Routing with Telnyx.

Happy Calling!

[Back to Top](#h_73f0b860c1)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Microsoft Teams Direct Routing documentation](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-plan)
* [Microsoft support](https://support.microsoft.com/en-US)

---

Related Articles

[Skype: Set up Skype for Biz SIP Trunk](https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk)[MS Teams: Call2Teams & Telnyx](https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx)[TLS & SIP Warnings for Teams](https://support.telnyx.com/en/articles/7048813-tls-sip-warnings-for-teams)[Operator Connect Guide - Microsoft Teams](https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams)[How to Configure a SIP Trunk](https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk)

Did this answer your question?

😞😐😃

Table of contents
