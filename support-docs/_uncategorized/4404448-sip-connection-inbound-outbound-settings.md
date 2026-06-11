---
source_url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
scraped: 2026-06-11
---

SIP Connection: Inbound & Outbound Settings | Telnyx Help Center

[Skip to main content](#main-content)

# SIP Connection: Inbound & Outbound Settings

Master inbound and outbound voice configurations with Telnyx's comprehensive guideline materials.

Written by Dillin

April 29, 2026

Table of contents

# **SIP Settings**

We provide our customers with the ability to enable certain features on their SIP Connection, to allow for more control on your inbound or outbound calls.

If you are looking for a detailed overview of the basic settings, please review this [article](https://support.telnyx.com/en/articles/4245868-sip-connection-types) for more information.

## **Inbound SIP Settings**

The settings available are as follows:

* ### **Number Format (DNIS / ANI)**

  This setting controls the number format in the FROM/TO and INVITE URI - described in further detail [here](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats). Useful for when your system only supports a particular number format on inbound rules.
* ## **SIP Transport Protocol**

  This setting is only available on **IP Auth, FQDN Auth or MS Teams Auth type SIP Connections** and allows you to set which transport protocol you wish to use for SIP signalling. More details on this can be found here: <https://sip.telnyx.com/>.
* ## **SIP Region**

  This setting is only available on **IP Auth, FQDN Auth or MS Teams Auth type SIP Connections** and allows you to set the Telnyx region which SIP signalling will be sent to your system from. More details on this can be found here: <https://sip.telnyx.com/>.
* ## **No Ringback Timeout**

  This setting controls how long Telnyx will wait for your SIP 180/183 response before terminating the call. By default, this timeout is set to 5 seconds. (The time frame cannot be set to less than 1 second, or more than 2 minutes.)
* ## **No Answer Timeout**

  This setting controls how long Telnyx will wait for your SIP 200 OK response before terminating the call. By default, this timeout is set to 5 seconds. (The time frame cannot be set to less than 1 second, or more than 10 minutes.)
* ## **SIP Subdomain**

  This setting is only available on **IP Auth, FQDN Auth or MS Teams Auth type SIP Connections** and allows you to set a SIP subdomain which can receive calls. (Leaving this empty will disable SIP subdomain calls.)
* ## **Receive SIP Subdomain Calls**

  This setting is only available on **IP Auth, FQDN Auth or MS Teams Auth type SIP Connections** and allows Telnyx to process calls with a defined subdomain that you set. For example, your sip:[test1234@client123.sip.telnyx.com](mailto:username@sip.telnyx.com) is dialed, where **client123** is the subdomain. SIP Subdomain calls can be received to all Telnyx SIP Proxies. This setting can also be set to be allowed from anyone (public internet), or just from your other account connections.
* ## **Channel Limit**

  This setting controls how many concurrent calls are allowed at any one time. By default, there is no limit specified meaning if you receive X amount of calls to DID's associated with this SIP Connection, we will process all requests.
* ## **Receive SIP URI Calls**

  This setting is only available on **credential type SIP Connections** and allows Telnyx to process calls where your sip:[username@sip.telnyx.com](mailto:username@sip.telnyx.com) is dialed. This can be disabled, set to be allowed from anyone, or just from your connections.
* ## **Encrypted Media**

  This setting allows for the media of your inbound calls to be encrypted with SRTP. When enabled, Telnyx will send the SIP INVITE to your connection with crypto media attributes in order to establish end-to-end media encryption between our media servers and your phone system.
* ## **Default Ringback Setting**

  Telnyx will not send anything. However, we will relay any messages and/or early media sent from the called party to the PSTN inbound carrier.
* ## **Generate Ringback Tone (183)**

  This setting means that Telnyx will reply with an instant 183 message with SDP and start sending early media carrying a US ringback tone to the PSTN inbound carrier. If the called party starts sending early media then Telnyx will stop generating the ringback tone and start passing what the called party sends to the PSTN inbound carrier.
* ## **Enable Instant Ringback (180)**

  Telnyx will reply with an instant 180 Ringing message and the PSTN inbound carrier is expected to generate a ringback tone on their side. If the called party starts sending early media then Telnyx will start passing that to the PSTN inbound carrier.
* ## **Offered Audio / Video Codecs**

  This setting allows you to enable the codecs which you prefer to be used and in order of preference.
* ## **Enable SIP Compact Headers**

  This setting, when enabled, means that Telnyx will send the SIP INVITE to your Connection with the SIP headers [compacted](https://www.cs.columbia.edu/sip/compact.html). Ideal for reducing Bandwidth consumption.

* ## **Enable Prack**

  This setting, when enabled, will allow for an acknowledgment system for your provisional 1XX responses. Each time you send back a 1XX, we will send back a SIP PRACK acknowledgment. By default, the setting is not enabled.
* ## **Receive ISUP Headers into SIP Headers**

  Sometimes our inbound PSTN carriers can send SS7 PSTN ISUP information as mime content type in the body of the SIP INVITE. By default, we pass this information along but if your system has difficulty parsing ISUP headers, you can enable this feature to ensure the ISUP is converted into the appropriate SIP Headers instead.
* ## **Enable Shaken/Stir Header**

  By default this is unselected. Select yes if you want receive attestation information in the webhooks for incoming calls.
* ## **Enable 3rd Party Call Control**

  Specifically for Cisco UCM devices but useful in cases where the SIP INVITE doesn't include a SDP (late media negotiation).  
  ​
* ## Enable Simultaneous Ringing

  Activate this feature to allow multiple SIP devices registered under the same **credentials** authenticated SIP connection to ring at the same time. This ensures that your customers never miss a call, whichever device they're closest to will ring simultaneously, increasing responsiveness and availability. Click Save to finish.

  [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333603031/7e912c052f457ff40f857e3530ea/image.png?expires=1781167500&signature=803aa7908b9451ba522511f589cf00abbbcb88d40fc9ee432e903d255e4094a2&req=diMkFc9%2BnoFcWPMW1HO4zcHEcStPMHP54zMeyx%2BWMJ5UlDB40EpDoXpRCbPO%0AKTKI%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333603031/7e912c052f457ff40f857e3530ea/image.png?expires=1781167500&signature=803aa7908b9451ba522511f589cf00abbbcb88d40fc9ee432e903d255e4094a2&req=diMkFc9%2BnoFcWPMW1HO4zcHEcStPMHP54zMeyx%2BWMJ5UlDB40EpDoXpRCbPO%0AKTKI%0A)

## **Outbound SIP Settings**

The settings available are as follows:

* ## **Outbound Voice Profile**

  The user can choose which outbound profile the SIP Connection can be associated with.
* ## **Localization Country**

  This setting, when enabled, will allow the user to dial out with the associated exit code of that country and allow the user to dial local numbers of that country also, without having the include the exit + country code. When a country is not specified, Telnyx will attempt to validate the dialed numbers as US and if that validation fails, a 404 invalid destination response is returned.
* ## **Channel Limit for Outbound Calls**

  When specified, Telnyx will honour the channel limit and not process any more concurrent outbound calls beyond that. The user will receive a 403 channel limit reached response.
* ## **Caller ID Override**

  Users have a choice of always overriding the caller ID for all outbound calls, overriding the caller ID for normal calls or overriding the caller ID for emergency calls. Example, if you have "Emergency Only" enabled with the caller ID you prefer, and a caller dials 911, we'll make sure to convert the caller ID provided in your SIP INVITE to the one defined your SIP Connection.
* ## **(FAX Settings) T.38 Re-invite Initiated By**

  Specifically for fax machines sending outbound faxes. By default this is set to Telnyx. However, users can choose "Customer" to initiate the SIP reINVITE for T.38 depending on their use case, or "Disabled".
* ## **Encrypted Media**

  This setting allows for the media of your outbound calls to be encrypted with **SRTP**. When enabled, Telnyx expects to receive your SIP INVITE from your connection with crypto media attributes in order to establish end-to-end media encryption between our media servers and your phone system.
* ## **Default Ringback Settings**

  Any 18x messages and/or early media (if any) Telnyx receives from the PSTN Term Carrier will be passed to the calling party agent.
* ## **Enable Instant Ringback (180)**

  Telnyx will reply with an instant 180 message and the calling party agent is expected to generate a ringback tone on its side. If the PSTN Term Carrier starts sending early media then Telnyx will start passing it to the calling party agent.
* ## **Generate Ringback Tone (183)**

  Telnyx will reply with an instant 183 message with SDP and start sending early media carrying a US ringback tone to the calling party agent. If The PSTN Term Carrier starts sending early media then Telnyx will stop generating the ringback tone and start passing it to the calling party agent.

---

Related Articles

[Configuring a GoAutoDial PBX SIP Trunk](https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk)[Skype: Set up Skype for Biz SIP Trunk](https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk)[SIP URI Calling](https://support.telnyx.com/en/articles/2925713-sip-uri-calling)[SIP Connection: Fail-over and Retries](https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries)[Xorcom PBX: SIP Trunk](https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk)

Did this answer your question?

😞😐😃

Table of contents
