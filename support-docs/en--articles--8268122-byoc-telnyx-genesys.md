---
source_url: https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys
scraped: 2026-06-11
---

BYOC: Telnyx & Genesys | Telnyx Help Center

[Skip to main content](#main-content)

# BYOC: Telnyx & Genesys

This guide provides instructions and technical details for the configuration of SIP trunk connectivity between Genesys Cloud and Telnyx.

Written by Karl Hulse

December 11, 2023

Table of contents

# Genesys and Telnyx BYOC

Before you get started you'll have to have the following set up:

1. Have created an account with Telnyx
2. Completed L2 verification
3. Purchased a number to be used for voice calls.

## Creating a SIP connection

In the Telnyx Mission Control Portal navigate to the "Voice” tab on the left side menu and select "S[IP Trunking](https://telnyx.com/products/sip-trunks)". Click on the “Add SIP Connection” button.

[![Genesys Cloud &amp; Telnyx SIP Set up](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980659/e7696e0fbb283f0524976019/Genesys_1.png?expires=1781168400&signature=c1b994ef1444902fa58dfe08b61133b3f811746a3e678d3cc298bb3ca4e2b7ee&req=fCAuH8F%2Bm4RWFb4f3HP0gPtSVpRBcuH0GgG%2F5J9D%2BwncjPb8t7R5IRwdQlFn%0A3zSG7DzglmImdv2hdg%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980659/e7696e0fbb283f0524976019/Genesys_1.png?expires=1781168400&signature=c1b994ef1444902fa58dfe08b61133b3f811746a3e678d3cc298bb3ca4e2b7ee&req=fCAuH8F%2Bm4RWFb4f3HP0gPtSVpRBcuH0GgG%2F5J9D%2BwncjPb8t7R5IRwdQlFn%0A3zSG7DzglmImdv2hdg%3D%3D%0A)

## ***Image 1 - Creating a SIP Trunk in Mission Control***

Name your SIP connection to make it easy to find.

[![Genesys Cloud &amp; Telnyx Connection Type](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980662/a078ac01aa1ceee1ca5c3810/Genesys_2.png?expires=1781168400&signature=140edfe395f4a4745cee6cfc61a3d38f2f99170dc0564d576b16db138f7c43e5&req=fCAuH8F%2Bm4ddFb4f3HP0gIDSghRpXaVNZmHS8FQgu9MCUV7GPwybDfzifKaN%0Aj%2BxLi5%2FQCV5sCz%2FJjw%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980662/a078ac01aa1ceee1ca5c3810/Genesys_2.png?expires=1781168400&signature=140edfe395f4a4745cee6cfc61a3d38f2f99170dc0564d576b16db138f7c43e5&req=fCAuH8F%2Bm4ddFb4f3HP0gIDSghRpXaVNZmHS8FQgu9MCUV7GPwybDfzifKaN%0Aj%2BxLi5%2FQCV5sCz%2FJjw%3D%3D%0A)

## *Naming your connection*

Choose “FQDN” as the SIP connection type and provide SIP URI to your Genesys Cloud organization. The domain should match the region of your Genesys Cloud deployment. Click the “have FQDN” button to update the FQDN setting.

In the “Outbound” section of the SIP connection settings, choose “Credentials” and provider user name and a password to be used for a digest authentication. Click “Save & Finish Editing” button to save your SIP Connection.

[![Genesys Cloud &amp; Telnyx FQDN Connections](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980665/405184877224f9d550db28d2/Genesys_3.png?expires=1781168400&signature=5d77c50c973611ec9bd1c291a5fb6c84cb80f536a986ca62d69eb8e1ac13945e&req=fCAuH8F%2Bm4daFb4f3HP0gJi4NvEOoSzsrSVCvQDpsym0z4Cp3KBiCxA3CbLw%0AjWU8DzmC34gmBrASpQ%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980665/405184877224f9d550db28d2/Genesys_3.png?expires=1781168400&signature=5d77c50c973611ec9bd1c291a5fb6c84cb80f536a986ca62d69eb8e1ac13945e&req=fCAuH8F%2Bm4daFb4f3HP0gJi4NvEOoSzsrSVCvQDpsym0z4Cp3KBiCxA3CbLw%0AjWU8DzmC34gmBrASpQ%3D%3D%0A)

## ***Image 2 - Choosing a FQDN Connection type***

##

## **Creating an Outbound Voice Profile**

Navigate to the “Outbound Voice Profiles” tab in the "Voice" section. Click the “Add New Profile” button.

[![Genesys Cloud &amp; Telnyx Outbound Voice Profile Setup](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980674/f4ba20caac58613b3627a808/Genesys_4.png?expires=1781168400&signature=81ed4cf11453fc4cfc652498fa7928dc4e38a508fc3c65df8f92929c6bf05256&req=fCAuH8F%2Bm4ZbFb4f3HP0gIx5BqR5%2BLsGzxfuJIeIf1GaszvczT5rbF3QGIt%2F%0A0MUwutXyQuxDGszSqA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980674/f4ba20caac58613b3627a808/Genesys_4.png?expires=1781168400&signature=81ed4cf11453fc4cfc652498fa7928dc4e38a508fc3c65df8f92929c6bf05256&req=fCAuH8F%2Bm4ZbFb4f3HP0gIx5BqR5%2BLsGzxfuJIeIf1GaszvczT5rbF3QGIt%2F%0A0MUwutXyQuxDGszSqA%3D%3D%0A)

## **Image 3 - Setting up your Outbound Voice Profile**

Provide a name for your new Outbound Voice Profile and click "Create".  
​

[![Genesys Cloud &amp; Telnyx Naming your OVP](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980680/46122cb51a49b8973b787c7b/Genesys_5.png?expires=1781168400&signature=9dc0a4facd5e5bd65718ea78f1d97c32113fa740c983be9fe62111134d71f5a4&req=fCAuH8F%2Bm4lfFb4f3HP0gA%2BvdpkQh8Qr72uM7K3RdQClPY6qTpCw81ByBBB1%0AFdVQOgokieOscdeNlg%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980680/46122cb51a49b8973b787c7b/Genesys_5.png?expires=1781168400&signature=9dc0a4facd5e5bd65718ea78f1d97c32113fa740c983be9fe62111134d71f5a4&req=fCAuH8F%2Bm4lfFb4f3HP0gA%2BvdpkQh8Qr72uM7K3RdQClPY6qTpCw81ByBBB1%0AFdVQOgokieOscdeNlg%3D%3D%0A)

## **Image 4 - Naming your Outbound Voice Profile**

You can select individual countries or regions to be allowed for the voice calls. Once you have chosen where to allow calls to/ from click the “Save” button to confirm your configuration.

[![Outbound voice profile section. ](https://downloads.intercomcdn.com/i/o/809953551/b53871b415e438f8a3531102/image.png?expires=1781168400&signature=4ac9e432d457d30faa63ee8ca47e5162660324198aebc5831d8d6af3adc998d2&req=fCAuH8x9mIReFb4f3HP0gIeu%2BpoJHm%2BsUPuIaoiBkQqQrRxBfpRGuHutX9yt%0AqK63mSrwznFdjpYtdg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/809953551/b53871b415e438f8a3531102/image.png?expires=1781168400&signature=4ac9e432d457d30faa63ee8ca47e5162660324198aebc5831d8d6af3adc998d2&req=fCAuH8x9mIReFb4f3HP0gIeu%2BpoJHm%2BsUPuIaoiBkQqQrRxBfpRGuHutX9yt%0AqK63mSrwznFdjpYtdg%3D%3D%0A)

## **Image 5 - Outbound Voice Profile Settings**

Return to your SIP Connection and edit the configuration. Select “Outbound” tab and select your newly created Outbound Voice Profile from a dropdown list.

​

[![Genesys Cloud &amp; Telnyx SIP Connection Options](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980691/0634ad841e26725e82af9048/Genesys_7.png?expires=1781168400&signature=688619b7899ef45b28121404361f4987fcb1209b7812ae1af9789994335446d6&req=fCAuH8F%2Bm4heFb4f3HP0gLquV0EmiKfH9bSPYlOF1D2hOYdMbK5OdsMlEcSA%0AV%2BmJCTxzIeg0lW4dWg%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980691/0634ad841e26725e82af9048/Genesys_7.png?expires=1781168400&signature=688619b7899ef45b28121404361f4987fcb1209b7812ae1af9789994335446d6&req=fCAuH8F%2Bm4heFb4f3HP0gLquV0EmiKfH9bSPYlOF1D2hOYdMbK5OdsMlEcSA%0AV%2BmJCTxzIeg0lW4dWg%3D%3D%0A)

## **Image 6 - Add your Outbound Voice Profile to your SIP Connection**

Next, switch to the “Inbound” tab of your SIP connection. Adjust DNIS and ANI numbers format to your Genesys Cloud configuration and save the updated configuration.

[![SIP connection settings for Genesys Cloud. ](https://downloads.intercomcdn.com/i/o/809959715/a3875da1ed3189a22756766e/image.png?expires=1781168400&signature=775effbeb3604bcf5cc15073b1718a82529f03798c01ec259f314107e2366df8&req=fCAuH8x3moBaFb4f3HP0gHAFTXZQLsvmr%2BY%2BRO9lPLahHW4zrwT1BywjznXV%0AI%2B9j2kkEqcXTEtwGGA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/809959715/a3875da1ed3189a22756766e/image.png?expires=1781168400&signature=775effbeb3604bcf5cc15073b1718a82529f03798c01ec259f314107e2366df8&req=fCAuH8x3moBaFb4f3HP0gHAFTXZQLsvmr%2BY%2BRO9lPLahHW4zrwT1BywjznXV%0AI%2B9j2kkEqcXTEtwGGA%3D%3D%0A)

## **Image 7 - Inbound SIP Connection Settings**

## **Number Configuration**

On the left-side menu, select the “Numbers” section and navigate to “My Numbers” tab. For your number purchased select a configured SIP Connection from a dropdown list.

[![Mission control portal for Number Configuration. ](https://downloads.intercomcdn.com/i/o/809964118/dbfa5a0e6417ed6591d2bdcf/image.png?expires=1781168400&signature=b7f4aa3ac41ffac512b1c493b8e98d3561c8b02a7f1506c755861d0e8b66a0b7&req=fCAuH896nIBXFb4f3HP0gH2NVpc7gvPPhmS%2FJcvb7xLbP4xX5UGRB4y3vnxJ%0AnaP5Z47UuQBXyk98vw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/809964118/dbfa5a0e6417ed6591d2bdcf/image.png?expires=1781168400&signature=b7f4aa3ac41ffac512b1c493b8e98d3561c8b02a7f1506c755861d0e8b66a0b7&req=fCAuH896nIBXFb4f3HP0gH2NVpc7gvPPhmS%2FJcvb7xLbP4xX5UGRB4y3vnxJ%0AnaP5Z47UuQBXyk98vw%3D%3D%0A)

## **Image 8 - Navigating To My Numbers**

Note that you can assign the same SIP connection to multiple numbers.

##

## **Configuration in Genesys Cloud**

Follow the steps below to create a SIP connection to Genesys Cloud organization.

Before you get started you need to ensure that:

1. The BYOC option is enabled in your Genesys Cloud organization
2. You have admin rights to setup Trunks
3. You have a number purchased and added to "[DID Numbers](https://telnyx.com/resources/sip-did)" and routed correctly (for example to the Architect flow)

For assistance, refer to Genesys Resource Center on [help.mypurecloud.com](https://help.mypurecloud.com/) for all details about Genesys Cloud configuration.

## **Create a SIP Trunk**

Go to the Admin options and select "Trunks". Provide a name for your SIP trunk and choose “BYOC Carrier” a SIP trunk type.

[![Genesys Cloud &amp; Telnyx Creating a SIP Trunk](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980699/b003e9648c65bd0241216699/Genesys_10.png?expires=1781168400&signature=63b85864f6016868cc7ac86ca7c7eae1e195c11aeb4398f0b1b15467d9ffc14a&req=fCAuH8F%2Bm4hWFb4f3HP0gPR7%2FcKRCQFnt3SQlk9VfkS6YTaoW50FV3VzQr0Y%0Aw9ddbCS2Sqt6wULrVw%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980699/b003e9648c65bd0241216699/Genesys_10.png?expires=1781168400&signature=63b85864f6016868cc7ac86ca7c7eae1e195c11aeb4398f0b1b15467d9ffc14a&req=fCAuH8F%2Bm4hWFb4f3HP0gPR7%2FcKRCQFnt3SQlk9VfkS6YTaoW50FV3VzQr0Y%0Aw9ddbCS2Sqt6wULrVw%3D%3D%0A)

## **Image 9 - Creating a SIP Trunk in Genesys Cloud**

Select "Generic BYOC Carrier" as a subtype.

[![Genesys Cloud &amp; Telnyx Selecting BYOC](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980708/f4be7a2f727ef0f84f5c6226/Genesys_11.png?expires=1781168400&signature=eca17cb79b0db11b9c35dab5b1bfe548c8552731d7a0c8e19cad3d412f1fac85&req=fCAuH8F%2BmoFXFb4f3HP0gN1EXP8swEpmKNbEx12xsw56z884AdST2AC%2F6aOI%0ACQYAQ1DYgUbwITIZUQ%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980708/f4be7a2f727ef0f84f5c6226/Genesys_11.png?expires=1781168400&signature=eca17cb79b0db11b9c35dab5b1bfe548c8552731d7a0c8e19cad3d412f1fac85&req=fCAuH8F%2BmoFXFb4f3HP0gN1EXP8swEpmKNbEx12xsw56z884AdST2AC%2F6aOI%0ACQYAQ1DYgUbwITIZUQ%3D%3D%0A)

## **Image 10 - Selecting Generic BYOC Carrier**

Provide a name for your SIP Trunk and your Inbound SIP Termination Identifier. This name should match the one configured in the Telnyx SIP Connection for FQDN option.

[![Genesys Cloud &amp; Telnyx Name your connection](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980710/55d280aa99f1671ac35571eb/Genesys_12.png?expires=1781168400&signature=e996c272ec7eecd9ad88e195c7fa1d69977922b5bceaf12f9732b0233ae4b9e9&req=fCAuH8F%2BmoBfFb4f3HP0gGJabMViK%2BPphZ0k8TjU9%2FNUNnHrQLx9An3IPSZx%0ASQJakOsA0dCrEnubjg%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980710/55d280aa99f1671ac35571eb/Genesys_12.png?expires=1781168400&signature=e996c272ec7eecd9ad88e195c7fa1d69977922b5bceaf12f9732b0233ae4b9e9&req=fCAuH8F%2BmoBfFb4f3HP0gGJabMViK%2BPphZ0k8TjU9%2FNUNnHrQLx9An3IPSZx%0ASQJakOsA0dCrEnubjg%3D%3D%0A)

## **Image 11 - Naming your connection**

Provide Telnyx SIP interface URL in the “SIP Servers and Proxies” based on your chosen region like sip.telnyx.com, sip.telnyx.eu etc.

Enable “Digest Authentication” and provide in “Realm” field the same URL as used for SIP proxy.

Provide the “User Name” and “Password” which was configured in Telnyx SIP Connection . Setup “Caller ID” with a number purchased in Telnyx platform.

##

[![Genesys Cloud &amp; Telnyx Settings](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980715/8c9a9e304b23458fe28ecdff/Genesys_13.png?expires=1781168400&signature=683f6fdf6f3a7a9f9c35ebca4fafd5e02b708734844d0c8e4b75115c38c51047&req=fCAuH8F%2BmoBaFb4f3HP0gN8122nq0rfUqK5YYDmX4FKzc1BLB5cDriDKvfw2%0AIQKvtpCt6wRBuGAg1w%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980715/8c9a9e304b23458fe28ecdff/Genesys_13.png?expires=1781168400&signature=683f6fdf6f3a7a9f9c35ebca4fafd5e02b708734844d0c8e4b75115c38c51047&req=fCAuH8F%2BmoBaFb4f3HP0gN8122nq0rfUqK5YYDmX4FKzc1BLB5cDriDKvfw2%0AIQKvtpCt6wRBuGAg1w%3D%3D%0A)

## **Image 12 - Manage your connection settings**

In the "SIP Access Control" Section, provide the IP addresses of your chosen Telnyx SIP endpoints (addresses are provided on sip.telnyx.com)  
​

[![SIP Access Control](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980720/028175c5561698ef24a58e14/Genesys_18_.png?expires=1781168400&signature=addba9d6a2f4fc14412f90bf12e4440bd953798a323fd5780af48bb8602815d8&req=fCAuH8F%2BmoNfFb4f3HP0gPEv28ebDH8p5XFXZl%2BWLQ8QuvO1pOEtBhxdn03y%0A%2BSBP0g8%2BGDmR%2BOuogA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980720/028175c5561698ef24a58e14/Genesys_18_.png?expires=1781168400&signature=addba9d6a2f4fc14412f90bf12e4440bd953798a323fd5780af48bb8602815d8&req=fCAuH8F%2BmoNfFb4f3HP0gPEv28ebDH8p5XFXZl%2BWLQ8QuvO1pOEtBhxdn03y%0A%2BSBP0g8%2BGDmR%2BOuogA%3D%3D%0A)

## **Image 13 - Add SIP Addresses**

Under the 'External Trunk Configuration' section expand the Protocol menu.

Scroll down to the 'Outbound' configuration and add a custom SIP header “X-Telnyx-Username” with the same value as set for a Digest Authentication.

[![Genesys - Adding External Trunk Connections](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980727/81631db3807b46085e39b30c/Genesys_19.png?expires=1781168400&signature=6786debd822abdffa1a5399934153ac570f83b1f65f56c2f7aa9b95631ffe141&req=fCAuH8F%2BmoNYFb4f3HP0gFXT6gNSQeLvsEO5G8am7EIzvFQEfrmGb4p4E%2B8A%0Av9filKsyuP5iUkfn3w%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980727/81631db3807b46085e39b30c/Genesys_19.png?expires=1781168400&signature=6786debd822abdffa1a5399934153ac570f83b1f65f56c2f7aa9b95631ffe141&req=fCAuH8F%2BmoNYFb4f3HP0gFXT6gNSQeLvsEO5G8am7EIzvFQEfrmGb4p4E%2B8A%0Av9filKsyuP5iUkfn3w%3D%3D%0A)

## **Image 14 - External Trunk Configuration**

[![Outbound Settings](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980734/09415558f3fcb93ed090e79b/Gensys_20.png?expires=1781168400&signature=872a21ff0309b41b742ec210a058d8d797cf8025598e18462ebf0954ac31b950&req=fCAuH8F%2BmoJbFb4f3HP0gCFf%2BqRhLvQlus7LSNPSpSRg24TevDjDkJNt3ZcT%0Am3y9npGvjIzMmwTsUA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-1.com/i/o/809980734/09415558f3fcb93ed090e79b/Gensys_20.png?expires=1781168400&signature=872a21ff0309b41b742ec210a058d8d797cf8025598e18462ebf0954ac31b950&req=fCAuH8F%2BmoJbFb4f3HP0gCFf%2BqRhLvQlus7LSNPSpSRg24TevDjDkJNt3ZcT%0Am3y9npGvjIzMmwTsUA%3D%3D%0A)

## **Image 15 - Outbound Trunk Settings**

## **Troubleshooting**

Debugging tools are available in the Telnyx Mission Control Portal where you can troubleshoot any issues with your SIP trunk communication checking SIP call flows, QoS stats and communication to a defined webhooks.

To find and use the debugging tools:

1. Navigate to the “Debugging” menu under “Reporting” in the sidebar
2. Select “SIP Call Flow Tool” in the top bar
3. Specify your search criteria and press “Search CDRs” button
4. From the list of listed calls select a one with “Call Data Debugging” button.

[![Mission Control Debugging Tools Overview section. ](https://downloads.intercomcdn.com/i/o/809976497/0c31069011a0a7f09556fd86/image.png?expires=1781168400&signature=65cb84918539fca906fdab86477cec196acc0b5df3bb16c3fcfc34d6ceb0385f&req=fCAuH854mYhYFb4f3HP0gA6xcKxKiNOlekjdqI%2BJoF88IKQWTgqOWfl%2FFDGR%0AO60cMVQvKMhcc6SxjQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/809976497/0c31069011a0a7f09556fd86/image.png?expires=1781168400&signature=65cb84918539fca906fdab86477cec196acc0b5df3bb16c3fcfc34d6ceb0385f&req=fCAuH854mYhYFb4f3HP0gA6xcKxKiNOlekjdqI%2BJoF88IKQWTgqOWfl%2FFDGR%0AO60cMVQvKMhcc6SxjQ%3D%3D%0A)

## **Image 16 - Mission Control Debugging Tools Overview**

This enables you to review a SIP Call Flow with the detailed data for each SIP Request:  
​  
​

## **Image 17 - Call Flow Debugging**

You can also check "Session Info" on the next tab or export PCAP data on the "Export" tab for sharing with your team.

[![Call Flow Debugging section. ](https://downloads.intercomcdn.com/i/o/809978736/23a967e8927fec1853fec956/image.png?expires=1781168400&signature=4e35437a2f6c712fa5357d40936c7838c14a012a4ed9484e3533c55506557b2a&req=fCAuH852moJZFb4f3HP0gEEVCoIA18Fx61oG67gJAQk5Qb8y%2BpndcY6P%2F0qa%0AWcR9hQS8ON%2FaNyHoaQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/809978736/23a967e8927fec1853fec956/image.png?expires=1781168400&signature=4e35437a2f6c712fa5357d40936c7838c14a012a4ed9484e3533c55506557b2a&req=fCAuH852moJZFb4f3HP0gEEVCoIA18Fx61oG67gJAQk5Qb8y%2BpndcY6P%2F0qa%0AWcR9hQS8ON%2FaNyHoaQ%3D%3D%0A)

## **Image 18 - PCAP Inspection**

---

Related Articles

[Skype: Set up Skype for Biz SIP Trunk](https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk)[Yeastar S-Series: Telnyx SIP](https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip)[PBXes: Connecting a PBXes Trunk to Telnyx](https://support.telnyx.com/en/articles/5798240-pbxes-connecting-a-pbxes-trunk-to-telnyx)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[How to Configure a SIP Trunk](https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk)

Did this answer your question?

😞😐😃

Table of contents
