---
source_url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
scraped: 2026-06-11
---

FreeSWITCH: IP Trunk Setup | Telnyx Help Center

[Skip to main content](#main-content)

# FreeSWITCH: IP Trunk Setup

In this article we will walk you through configuring a FreeSWITCH IP Trunk with Telnyx.

Written by Dillin

November 22, 2025

Table of contents

[Jump to Instructions](#h_ae423994db)

[FreeSWITCH™](https://signalwire.com/freeswitch) is a scalable open source cross-platform telephony suite designed to route and interconnect popular communication protocols using audio, video, text or any other form of media. From a Raspberry PI to a multi-core server, FreeSWITCH can unlock the telecommunications potential of any device.

FreeSWITCH also provides a stable telephony platform on which many telephony applications can be developed using a wide range of free tools.

Additional documentation:

* Get in touch with FreeSWITCH here
* Check out their [help section](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/) for community or paid support.

---

# Instructions For Configuring a FreeSWITCH IP Trunk

**In this guide, you will:**

1. [Extension configuration for registering a SIP phone](#h_4876db4804)
2. [Create a SIP trunk](#h_b93eaf5074)
3. [Create an inbound trunk - DID](#h_7714f1cd5d)
4. [Create a dialplan](#h_2fc6c12cb3)
5. [Configure your network](#h_b3c7464524)

**Pre-Requisites**

* [Download](https://files.freeswitch.org/freeswitch-releases/) and [install](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Installation/) FreeSWITCH™
* [Configure the Telnyx Mission Control Portal](#h_6b4b583ecb)
* Create an [IP connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive calls.

|  |
| --- |
| ***IMPORTANT:*** *FreeSWITCH™ v1.8 has been tagged End of Life. If you are on this version, you must upgrade.* |

## 1. Configuring the Telnyx Mission Control Panel

For step-by-step instructions on each of the requirements on the Telnyx Mission Control Portal, please follow this [guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).

Once you've configured your Telnyx account, you can now proceed to setup FreePBX V13 following the guide below.

## 2. Update default credentials

Your new FreeSWITCH instance is preconfigured with default credentials that ***must*** be changed to prevent unauthorized users from registering with your instance and making calls.

1. Open vars.xml:  
   ​`root@ip­172­31­54­222:/# cd /usr/local/freeswitch/conf root@ip­172­31­54­222:/usr/local/freeswitch/conf# vi vars.xml`
2. Find the line that begins with `<X-PRE-PROCESS cmd="set" data="default_password="`
3. Change the default password.

## 3. Update the external SIP profile

1. Navigate to sip\_profiles/external.xml

   ```
   ...# cd sip_profiles  
   .../sip_profiles# vi external.xml
   ```
2. Uncomment the following lines:

   ```
   <param name="ext-rtp-ip" value="$${external_rtp_ip}"/>  
   <param name="ext-sip-ip" value="$${external_sip_ip}"/>
   ```

## 4. Create the SIP Trunk and build it to Telnyx

There are multiple ways that this can be accomplished, but the easiest way is to build your own gateway under the external SIP profile.

1. Navigate to the sip\_profiles/telnyx.xml

   ```
   .../sip_profiles# cd external  
   .../sip_profiles/external# vi telnyx.xml
   ```
2. You'll see something like this:

   ```
   <include>  
   <gateway name="telnyx">  
   <param name="proxy" value="sip.telnyx.com"/>  
   <param name="register" value="false"/>  
   <param name="caller-id-in-from" value="true"/> <!--Most gateways seem to want this-->  
   <param name="username" value="not-used"/>  
   <param name="password" value="not-used"/>  
   </gateway>  
   </include>
   ```

## 5. Create a Dialplan

Note that this is a sample dialplan, as each dialplan is typically unique. For more defailed information about setting up a FreeSWITCH dialplan, see FreeSWITCH's documentation.

1. Navigate to /user/local/freeswitch/conf/dialplan/public
2. Remove the files located here and create a new inbound dialplan xml. Here is an example of what this will look like:

   ```
   <include>  
     <extension name="public_did">  
       <condition field="destination_number" expression="^(1{0,1}\d{10})$">  
         <action application="set" data="effective_caller_id_number=13125489677"/>                 
         <!-- Replace 3125489677 with the DID you want as CID -->   
         <action application="bridge" data="sofia/gateway/telnyx/$1"/>  
       </condition>  
     </extension>  
     
     <extension name="local.com">  
       <condition field="destination_number" expression="^(\d{7})$">  
         <action application="set"  
   data="effective_caller_id_number=${outbound_caller_id_number}"/>  
         <action application="set"  
   data="effective_caller_id_name=${outbound_caller_id_name}"/>  
         <action application="bridge"  
   data="sofia/gateway/telnyx/+1${default_areacode}$1"/>  
       </condition>  
     </extension>  
     
     <extension name="domestic.com">  
       <condition field="destination_number" expression="^(\d{11})$">  
         <action application="set"  
   data="effective_caller_id_number=${outbound_caller_id_number}"/>  
         <action application="set"  
   data="effective_caller_id_name=${outbound_caller_id_name}"/>  
         <action application="bridge" data="sofia/gateway/telnyx/+$1"/>  
       </condition>  
     </extension>  
     
     <extension name="international.com">  
       <condition field="destination_number" expression="^(011\d+)$">  
         <action application="set"  
   data="effective_caller_id_number=${outbound_caller_id_number}"/>  
         <action application="set"  
   data="effective_caller_id_name=${outbound_caller_id_name}"/>  
         <action application="bridge" data="sofia/gateway/telnyx/+$1"/>  
       </condition>  
     </extension>  
   </include>
   ```

## 6. Network configuration

If you want to use the same profile for communication both inside and outside your network, you will need to tell FreeSWITCH™ when it should use the local IP or the external IP.

The autonat: prefix toggles on the usage of the local-network-acl, if you prefix the IP like that it will activate the dynamic ability to tell when it should use ext-rtp-ip vs rtp-ip based on the acl match.

```
<param name="ext-sip-ip" value="autonat:$${external_sip_ip}"/>
```

***Note:*** In case FreeSWITCH fails to recognize your public IP you may "force" it to use a static Public IP by modifying sip\_profiles/external.xml as follows:

```
<param name="ext-rtp-ip" value="8.8.8.8"/>  
<param name="ext-sip-ip" value="8.8.8.8"/>  
<!-- Replace 8.8.8.8 with your public IP -->
```

[Back to Top](#h_ae423994db)

---

**Additional Resources**

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally you can:

* Get in touch with FreeSWITCH here
* Check out their [help section](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/) for community or paid support.

---

Related Articles

[Configuring a Cisco CUBE/CUCM IP Trunk](https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk)[Cisco: Configure a Cisco CME IP Trunk](https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk)[Configuring an AVAYA IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx)[Asterisk: Configure an Asterisk IP trunk](https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk)[FreeSWITCH: Credentials Trunk](https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk)

Did this answer your question?

😞😐😃

Table of contents
