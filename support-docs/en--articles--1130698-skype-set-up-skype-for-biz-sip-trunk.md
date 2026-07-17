---
source_url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
title: "Skype: Set up Skype for Biz SIP Trunk"
description: "Learn how to configure a Skype for Business Server SIP Trunk with Telnyx. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 0dfe7f2b81bbf490e5e98ea38746a59589267cfa143edc01da3463aaf150281e
---







# Skype: Set up Skype for Biz SIP Trunk

Learn how to configure a Skype for Business Server SIP Trunk with Telnyx. See Telnyx guidance and requirements.

C




[Jump to instructions](#configure-skype-for-business-server-sip-trunk-with-telnyx)

[Skype for Business](https://www.microsoft.com/en-us/microsoft-365/previous-versions/skype-for-business-online) was an enterprise software application for instant messaging and videotelephony developed by Microsoft as part of the Microsoft Office suite. It is designed for use with the on-premises Skype for Business Server software, and a software as a service version offered as part of Office 365.

**Additional resources:**

* [Microsoft support](https://www.microsoft.com/en-us/microsoft-365/support)
* [Skype download](https://www.skype.com/en/get-skype/)
* [Skype for Business Topology documentation](https://learn.microsoft.com/en-us/skypeforbusiness/deploy/install/create-and-publish-new-topology)

---

## Instructions for configuring a Skype for Business Server SIP Trunk with Telnyx

In this activity you will:

1. [Connect Skype to a Telnyx SIP trunk](#h_dbdc6e3f53)
2. [Create a dial plan](#h_3dade4ab6f)
3. (Optional) [Deploy Cloud Connector Edition](#h_9363910e74)

**Pre-requisites:**

* Your Telnyx Portal must be correctly [set up and configured for use](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* Have your SIP Credentials (The username/password for your main SIP account or SIP sub-account)
* Have access to [Skype for Business Topology Builder](https://learn.microsoft.com/en-us/skypeforbusiness/deploy/install/create-and-publish-new-topology)
* You must allow this traffic on your firewall to work with Telnyx [SIP Trunk](https://telnyx.com/products/sip-trunks)

**Video Walkthroughs**

Setting up your Telnyx SIP portal account so you can make and receive calls:

## 1. Connect Skype to a Telnyx SIP trunk

In this section, you'll use Skype for Business Topology Builder to

1. Start Skype forBusiness Topology Builder:
2. Click **Start** and type *Skype for Business Server.* Then click on **Skype for Business Server Topology Builder**.
3. Navigate to Skype for **Business Server > [your site name] > Shared Components**.
4. Right-click the PSTN gateways node, and then click **New IP/PSTN Gateway**.
5. On the **Define New IP/PSTN Gateway** screen, type *sip.telnyx.com* and click **Next**.
6. On this screen, leave **IPv4 – Use allconfigured IP addresses** with its default value and click **Next**.
7. To define a root trunk for the PSTN gateway, provide the following values (***Note:*** *Be sure that the peer you're defining is running and using FQDN or an IP address you specified*):

   1. **Listening Port for IP/PTSN Gateway:** *5060*
   2. **SIP Transport Protocol:** *TCP*
   3. **Associated Mediation Server:** select the Mediation Server  pool to associate with the root trunk of this PSTN Gateway
   4. **Associated Mediation Server Port:** This will be the listening port that the mediation server will use for SIP messages from the gateway (*5068* by default).
8. Click **Finish**.
9. Right-click the **Skype for Business Server** node, and then click **Publish Topology**.

[Back to Top](#configure-skype-for-business-server-sip-trunk-with-telnyx)

## 2. Create a dial plan

In this section, you'll be creating a dial plan, a voice policy, call route, PSTN usage and trunk configuration.

|  |
| --- |
| ***Note:*** *We recommend that you create a custom configuration based on your location and your company policies. The script we're providing is just an example of a basic configuration. You should use this exact script only if you have a default environment with no voice settings.* |

|  |
| --- |
| ***IMPORTANT:*** *Before running this script, make sure you've defined a PSTN gateway in your topology for the selected site, and that you've backed upyour existing Enterprise Voice configuration* |

1. Copy and paste the text following these instructions, or your custom script into a text editor.

   ```
   Write-Host "Starting Telnyx Enterprise Voice example settings..."

   #Add PSTN UsageWrite-Host "Adding PSTN Usage..."Set-CsPstnUsage -Force -Usage @{add="US-Basic-PSTN-Usage"}  | Out-Null

   #Set Dial In Conference RegionWrite-Host "Setting Dial Plan..."Set-CsDialPlan -Identity "Global" -SimpleName "Global" -DialinConferencingRegion "US"  | Out-Null

   #Add Normalization RulesWrite-Host "Adding Normalization Rules..."New-CsVoiceNormalizationRule -Name 'US-National' -Parent Global -Pattern '^1?([2-9]\d\d[2-9]\d{6})\d*(\D+\d+)?$' -Translation '+1$1' -Priority 0 -Description "National number normalization for United States" -WarningAction:SilentlyContinue | Out-NullNew-CsVoiceNormalizationRule -Name 'US-Service' -Parent Global -Pattern '^([2-9]11)$' -Translation '$1' -Priority 1 -Description "Service number normalization for United States" -WarningAction:SilentlyContinue | Out-NullNew-CsVoiceNormalizationRule -Name 'US-International' -Parent Global -Pattern '^(?:\+|011)(1|7|2[07]|3[0-46]|39\d|4[013-9]|5[1-8]|6[0-6]|8[1246]|9[0-58]|2[1235689]\d|24[013-9]|242\d|3[578]\d|42\d|5[09]\d|6[789]\d|8[035789]\d|9[679]\d)(?:0)?(\d{6,14})(\D+\d+)?$' -Translation '+$1$2' -Priority 2 -Description "International number normalization for United States" -WarningAction:SilentlyContinue | Out-Null

   #Set Voice PolicyWrite-Host "Setting Voice Policy..."Set-CsVoicePolicy -Identity Global -AllowCallForwarding $true -AllowPSTNReRouting $true -AllowSimulRing $true -EnableBWPolicyOverride $false -EnableCallPark $true -EnableCallTransfer $true -EnableDelegation $true -EnableMaliciousCallTracing $true -EnableTeamCall $true -PstnUsages @{add="US-Basic-PSTN-Usage"}  | Out-Null

   #Add Voice RouteWrite-Host "Adding Voice Route..."New-CsVoiceRoute -Identity "US-Basic-Voice-Route" -NumberPattern ^+ -PstnGatewayList @{add="PstnGateway:sip.telnyx.com"} -PstnUsages @{add="US-Basic-PSTN-Usage"} -WarningAction:SilentlyContinue | Out-Null

   #Update Trunk ConfigurationWrite-Host "Updating Trunk Configuration..."Set-CsTrunkConfiguration -Identity Global -MaxEarlyDialogs 20 -SRTPMode "Optional" -ConcentratedTopology $true -EnableReferSupport $false  | Out-Null

   #Job is doneWrite-Host "Configuration is done!"
   ```
2. Save it with the extension .ps1
3. Open Skye for Business Management Shell and run the script you just created.

[Back to Top](#configure-skype-for-business-server-sip-trunk-with-telnyx)

## 3. (Optional) Deploy Cloud Connector Edition

If you need to deploy CCE (Cloud Connector Edition) you should follow the steps in the next article before proceeding:
​<https://technet.microsoft.com/en-us/library/mt605228.aspx>

1. Specify the following information in the .ini file:

   1. **Voice Gateway 1 Make and Model:** *Telnyx Telephony Engine*
   2. **Voice Gateway 1 Name:** *sip.telnyx.com*
   3. **Voice Gateway 1 IP Address:** *192.76.120.10*
   4. **Voice Gateway 1 Port #:**  *5060*
   5. **Voice Gateway 1 Protocol for SIP Traffic:** *TCP*
   6. **Enable REFER support:** *$false*
   7. Remove the section in the .ini file for the second gateway

That's it! You've finished configuring Skype for Business!

​

[Back to Top](#configure-skype-for-business-server-sip-trunk-with-telnyx)

---

## Additional Resources

## Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Microsoft support](https://www.microsoft.com/en-us/microsoft-365/support)
* [Skype download](https://www.skype.com/en/get-skype/)
* [Skype for Business Topology documentation](https://learn.microsoft.com/en-us/skypeforbusiness/deploy/install/create-and-publish-new-topology)

---

Related Articles

[Grandstream UCM6xxx: SIP Trunks](https://support.telnyx.com/en/articles/5748258-grandstream-ucm6xxx-sip-trunks)[Wildix: SIP Trunk Setup](https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[Grandstream GRP2612: SIP Trunk](https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)

Did this answer your question?

😞😐😃
