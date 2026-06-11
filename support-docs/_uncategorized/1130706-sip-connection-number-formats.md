---
source_url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
scraped: 2026-06-11
---

SIP Connection: Number Formats | Telnyx Help Center

[Skip to main content](#main-content)

# SIP Connection: Number Formats

Here we will talk about SIP connections and ANI/DNIS number format control!

Written by Dillin

Updated over 3 weeks ago

Table of contents

This article describes the number formatting functionality available on the inbound settings of your SIP Connections.

## **Configuring Number Formats**

The SIP connections section is located on the left pane when signed into your account. This section allows you to whitelist the different SIP connections of your phone systems. They can be assigned to [DID's](https://portal.telnyx.com/#/voice/my-numbers) to allow for inbound calling and assigned to [Outbound Voice Profiles](https://portal.telnyx.com/#/outbound-profiles) for allowing outbound calling.   
​  
Click on this button below and it will directly get you to the SIP Connections section.

[SIP Connections](https://portal.telnyx.com/#/voice/connections)

## **Guide to Creating a SIP Connection**

You can create a SIP Connection by clicking the "Create SIP Connection" button on the right side of the web page.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333360720/5499142c60510e6054b25a4913dd/image.png?expires=1781167500&signature=712ae842e9a0e2904cce8863c9f9970c762a111c011f1105b279ddcbb066c650&req=diMkFcp4nYZdWfMW1HO4zf35a2cutkaUvs0969fDA%2BbmDi4X%2BxHB4dMIGMIS%0AtBuWEID9p3qXJnRv5%2FQ%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333360720/5499142c60510e6054b25a4913dd/image.png?expires=1781167500&signature=712ae842e9a0e2904cce8863c9f9970c762a111c011f1105b279ddcbb066c650&req=diMkFcp4nYZdWfMW1HO4zf35a2cutkaUvs0969fDA%2BbmDi4X%2BxHB4dMIGMIS%0AtBuWEID9p3qXJnRv5%2FQ%3D%0A)

If you already have a SIP connection, go straight ahead and click the settings icon on the right side of your SIP connection, then navigate to the "Inbound" tab.

## **Inbound**

You'll now see a settings section appear with the number format functionality we're interested in, specifically DNIS (dialed number) and ANI (originating number). By default, E164 is the selected option, you may want to consider changing this depending on what your phone system expects, based on the inbound rules.

1. **Dialed Number Information Service** (DNIS) is designed to allow the recipient of a telephone call the know the phone number originally dialed for an incoming phone call.
2. **Automatic number identification (ANI)** is a feature of a telecommunications network for automatically determining the origination telephone number on toll calls for billing purposes.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333378580/5d273bfa339fabca28670b75f262/image.png?expires=1781167500&signature=5564c3b4faed3a36468453f74dbd0cbfab5a9d1cf36f3872756a38e4fe7d1f5e&req=diMkFcp5lYRXWfMW1HO4zSb8GKxYJFlLczH2A8aV66CDuSp%2B78CyceYv3oqc%0A5fqRpfFO8mLzimEDj5Y%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333378580/5d273bfa339fabca28670b75f262/image.png?expires=1781167500&signature=5564c3b4faed3a36468453f74dbd0cbfab5a9d1cf36f3872756a38e4fe7d1f5e&req=diMkFcp5lYRXWfMW1HO4zSb8GKxYJFlLczH2A8aV66CDuSp%2B78CyceYv3oqc%0A5fqRpfFO8mLzimEDj5Y%3D%0A)

Some phone systems prefer to accept specific number formats on their inbound calls, we describe the different number formats below which are configurable from the drop-down menus.   
​

* **+E.164** - When selected, Telnyx will include, in the SIP INVITE, the number with the + included in front of the country code.  
  ​
* **E.164** - When selected, Telnyx will include, in the SIP INVITE, the number without the + included in front of the country code.   
  ​
* **National (10 digits)** - When selected, Telnyx will include, in the SIP INVITE, the local 10 digit format of the country.  
  ​
* **SIP Username** - When selected, Telnyx will include, in the SIP INVITE, the username of the SIP Connection. This is only available for credential authentication based connections and only for the DNIS.  
  ​
* **+E.164 / National (10 digits)** - This option is only available to configure on the ANI. Depending on the callers number and country of origin, will depend on what Telnyx sends.   
  ​  
  ​**Example:** If the dialed number is US based and the origin number is also US based, then the SIP INVITE will contain 10 digit ANI number format. However, if the dialed number is US based but the origin is not US based but International, then Telnyx will send the ANI as +E.164 number format.   
  ​
* **E.164 / National (10 digits)** - This option is only available to configure on the ANI. Depending on the callers number and country of origin, will depend on what Telnyx sends.   
  ​  
  ​**Example:** If the dialed number is US based and the origin number is also US based, then the SIP INVITE will contain 10 digit ANI number format. However, if the dialed number is US based but the origin is not US based but International, then Telnyx will send the ANI as E.164 number format.

​**ANI Number Format Options**  
​

[![Number format (ANI) interface.](https://downloads.intercomcdn.com/i/o/230309627/f4083c6e1eefdad934dbc68e/Screenshot+from+2020-07-25+00-29-41.png?expires=1781167500&signature=42eb0cba8b4d030271dd7fa5bab907ce9c0089ad3ba01d317cddc5b9774209c8&req=diMnFcl3m4NYFb4f3HP0gOJoV02NmxTw22tilzkq7DlN9lsKdh84mF39HA8%2F%0AxDwD8s4kxBAKB%2FF8Jg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/230309627/f4083c6e1eefdad934dbc68e/Screenshot+from+2020-07-25+00-29-41.png?expires=1781167500&signature=42eb0cba8b4d030271dd7fa5bab907ce9c0089ad3ba01d317cddc5b9774209c8&req=diMnFcl3m4NYFb4f3HP0gOJoV02NmxTw22tilzkq7DlN9lsKdh84mF39HA8%2F%0AxDwD8s4kxBAKB%2FF8Jg%3D%3D%0A)

**DNIS Number Format Options**

[![Number format (DNIS) options interface.](https://downloads.intercomcdn.com/i/o/230309682/5f2e01a84228059a753d107f/Screenshot+from+2020-07-25+00-29-25.png?expires=1781167500&signature=dcbd544b0e1b2aef68980a1d8e71008dac8b7517c763625bac87a295a2783d4b&req=diMnFcl3m4ldFb4f3HP0gHG8U4en2SAIobbIHTRCkospSnEV8hLPTsROA6lR%0AYoD94H5%2F%2BaBwHnznhA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/230309682/5f2e01a84228059a753d107f/Screenshot+from+2020-07-25+00-29-25.png?expires=1781167500&signature=dcbd544b0e1b2aef68980a1d8e71008dac8b7517c763625bac87a295a2783d4b&req=diMnFcl3m4ldFb4f3HP0gHG8U4en2SAIobbIHTRCkospSnEV8hLPTsROA6lR%0AYoD94H5%2F%2BaBwHnznhA%3D%3D%0A)

## **Outbound**

When making outbound calls through Telnyx, we support all number format types. In particular, we allow for the use of localization. This feature, when enabled with the country of interest, will allow the user to dial out with the associated exit code of that country and allow the user to dial local numbers of that country also, without having the include the exit + country code.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333381224/52070e38ba7771ecf32d960065fa/image.png?expires=1781167500&signature=3f3c34a65f3541f8405333ef070a53e162d60cf66e81a9d722e85c570afbc64e&req=diMkFcp2nINdXfMW1HO4zeCwAez5hpJJp%2F3KoKOAOvFx4h7BxD9NA1XlA0XS%0ATPnna0I7NM%2FB2Lf%2BohM%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2333381224/52070e38ba7771ecf32d960065fa/image.png?expires=1781167500&signature=3f3c34a65f3541f8405333ef070a53e162d60cf66e81a9d722e85c570afbc64e&req=diMkFcp2nINdXfMW1HO4zeCwAez5hpJJp%2F3KoKOAOvFx4h7BxD9NA1XlA0XS%0ATPnna0I7NM%2FB2Lf%2BohM%3D%0A)

## **Special Note on SIP Connections**

With Telnyx, if you choose to build a [WebRTC](https://portal.telnyx.com/#/debugging/web-dialer) application, you can create a credential authentication based connection. Once created, you will be provided with, or can edit yourself, a username and password.   
​  
You can then specify the DNIS number format as the ***SIP Username*** such that when inbound calls arrive to our network toward your DID's associated with the SIP Connection, we'll send the username of the SIP Connection in the SIP INVITE.

Lastly, don't forget to select the ***VP8/9*** codecs in the advanced settings of the inbound section of the SIP Connection. This allows Telnyx to send the SIP INVITE to your WebRTC application with these codecs in the media parameters, which are ideal for video!

---

Related Articles

[SIP URI Calling](https://support.telnyx.com/en/articles/2925713-sip-uri-calling)[Caller ID Number Policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)[SIP Connection: Inbound & Outbound Settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)

Did this answer your question?

😞😐😃

Table of contents
