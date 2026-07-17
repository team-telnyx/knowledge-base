---
source_url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
title: "FreeSWITCH: Credentials Trunk"
description: "Here we will explain how to configure a FreeSWITCH Credentials Trunk with Telnyx. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: fc5abd1292f0d8236346f697539169723a012c9e5d2ba0cf07cb7f87754a6b6e
---







# FreeSWITCH: Credentials Trunk

Here we will explain how to configure a FreeSWITCH Credentials Trunk with Telnyx. See Telnyx guidance and requirements.




[Jump to Instructions](#h_20180b055c)

[FreeSWITCH™](https://signalwire.com/freeswitch) is a scalable open source cross-platform telephony suite designed to route and interconnect popular communication protocols using audio, video, text or any other form of media. From a Raspberry PI to a multi-core server, FreeSWITCH can unlock the telecommunications potential of any device.

FreeSWITCH also provides a stable telephony platform on which many telephony applications can be developed using a wide range of free tools.

Additional documentation:

* Get in touch with FreeSWITCH here
* Check out their [help section](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/) for community or paid support.

---

## Instructions For Configuring a FreeSWITCH IP Trunk

**In this guide, you will:**

1. [Extension configuration for registering a SIP phone](#h_7aff4574d5)
2. [Create a SIP trunk](#h_16f056af1c)
3. [Create a dialplan](#h_66c3a7a543)
4. [Create an inbound trunk - DID](#h_bcac915da6)
5. [Configure your network](#h_f45e77e40e)

**Pre-Requisites**

* [Download](https://files.freeswitch.org/freeswitch-releases/) and [install](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Installation/) FreeSWITCH™
* [Configure the Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup#h_6b4b583ecb)
* Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive calls.

|  |
| --- |
| ***IMPORTANT:*** *FreeSWITCH™ v1.8 has been tagged End of Life. If you are on this version, you must upgrade.* |

## 1. Extension configuration for registering a SIP phone

You may register to one of the existing extensions; however it is recommended that you change the default password in the **directory/default/1000.xml** file:

```
<param name="password" value="abcd1234"/>
<!-- Replace abcd1234 with a strong password -->
```

## 2. Create the SIP trunk

Create a file under directory: **sip\_profiles/external** (i.e.: *sip\_profiles/external/telnyx.xml*)

|  |
| --- |
| ***Note:*** *If you have a linksys device (spa2102 spa5xx series), they will reject calls if ptime is not set to 20. Make sure you change that in the phone's configuration (rtp packet size 0.020 [from 0.030]) i.e.:* sip\_profiles/external/telnyx.xml *- telnyx.xml should contain the following:*    ``` <include>     <gateway name="telnyx">         <param name="realm" value="sip.telnyx.com"/>         <param name="username" value="freesuser"/>         <!-- Replace freesuser with your Telnyx Portal username -->         <param name="password" value="freespass"/>         <!-- Replace freepass with your Telnyx Portal password -->         <param name="register" value="true"/>     </gateway> </include> ``` |

## 3. Create a dialplan

File to edit: dialplan/default.xml - add the following to default.xml

```
<extension name="dial">
        <condition field="destination_number" expression="^(1{0,1}\d{10})$">
        <action application="set" data="effective_caller_id_number=13125489677"/>
        <!-- Replace 3125489677 with the DID you want as CID -->
        <action application="bridge" data="sofia/gateway/telnyx/$1"/>
        </condition>
</extension>
```

## 4. Create an inbound trunk - DID

Create a file under directory: dialplan/public/

ie. dialplan/public/3125489677.xml - 3125489677.xml is the DID you purchased at Telnyx Mission Control Portal and should contain the following:

```
<include>
    <extension name="public_did">
        <condition field="destination_number" expression="^(13125489677)$">
        <!-- Replace 13125489677 with the DID you purchased at the Telnyx Portal -->
            <action application="set" data="domain_name=$${domain}"/>
            <action application="transfer" data="1000 XML default"/>
        </condition>
    </extension>
</include>
```

## 5. Configure your network

If you want to use the same profile for communication both inside and outside your network, you will need to tell FreeSWITCH™ when it should use the local IP or the external IP.

The autonat: prefix toggles on the usage of the local-network-acl, if you prefix the IP like that it will activate the dynamic ability to tell when it should use ext-rtp-ip vs rtp-ip based on the acl match.

```
<param name="ext-sip-ip" value="autonat:$${external_sip_ip}"/>
```

|  |
| --- |
| ***Note:*** *In case FreeSWITCH fails to recognize your public IP you may "force" it to use a static Public IP by modifying sip\_profiles/external.xml as follows:*  ``` <param name="ext-rtp-ip" value="8.8.8.8"/> <param name="ext-sip-ip" value="8.8.8.8"/> <!-- Replace 8.8.8.8 with your public IP --> ``` |

[Back to Top](#h_20180b055c)

---

**Additional Resources**

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally you can:

* Get in touch with FreeSWITCH here
* Check out their [help section](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/) for community or paid support.

---

Related Articles

[Cisco: Configure a Cisco CME IP Trunk](https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk)[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[Configuring a Cisco CME Credentials Trunk](https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk)[FreeSWITCH: IP Trunk Setup](https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup)[Elastix 5: Credentials Trunk](https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk)

Did this answer your question?

😞😐😃
