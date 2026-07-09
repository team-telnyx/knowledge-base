---
source_url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
scraped: 2026-07-08
content_hash: 3b217f8dcda4cc1ce92e979c87da493e275f46181a548436bafb888a7d4e6e9f
---

Asterisk: Configure an Asterisk IP trunk | Telnyx Help Center

[Skip to main content](#main-content)

# Asterisk: Configure an Asterisk IP trunk

This guide will walk you through configuring an Asterisk PBX IP Trunk with Telnyx.

C

Written by Customer Success

June 6, 2024

Table of contents

[Jump to Instructions](#h_e905b1451e)

[Asterisk](https://www.asterisk.org/) is an open source framework for building communications applications. Asterisk turns an ordinary computer into a communications server. Asterisk powers IP PBX systems, VoIP gateways, conference servers and other custom solutions. It is used by small businesses, large businesses, call centers, carriers and government agencies, worldwide.

There are two standard methods to connect an Asterisk box to Telnyx:

* Asterisk (SIP), to use the same standard Session Initiation Protocol used to connect to SIP phones
* Asterisk (PJSIP), to use the Open Source Embedded SIP protocol stack

|  |
| --- |
| ***Note:*** *Telnyx does not support IAX2 connections.* |

For more Asterisk documentation, see:

* [http://www.asteriskdocs.org](http://www.asteriskdocs.org/) is a free HTML book (the corresponding printed book is published conventionally by O'Reilly)
* [http://www.asterisk.org](https://www.asterisk.org/) is Asterisk's home site, operated by [Digium.com](https://www.sangoma.com/?source=digium_redirects_093021).

---

# Instructions for Configuring an Asterisk Trunk

**In this guide, you will:**

1. [Configure the Telnyx Mission Control Portal to work with your Asterisk trunk](#step-by-step-guide)
2. [Configure an Asterisk SIP trunk setup](#h_2c0331e737)
3. [Configure Asterisk to make and accept calls](#2-please-note-that-for-this-configuration-to-work-the-module-respjsipconfigwizardso-must-be-installed-and-loaded-available-from-asterisk-1320)
4. [Complete a basic PJSP configuration](#4-completing-the-basic-pjsip-configuration)
5. [Set up a dialplan](#5-setting-up-the-dialplan)

**Pre-Requisites:**

* [Download](http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz) and [install](https://docs.asterisk.org/) Asterisk version 18
* Make sure you have created an [IP authentication based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, [assigned this connection to a DID](https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection) and outbound profile in order to make and receive calls.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Asterisk/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Configuring the Telnyx Mission Control Panel

For step by step instructions on each of the requirements on the Telnyx Mission Control Portal, please follow this [guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).

## 2. Configuring Asterisk SIP Trunk Setup

Open up `/etc/asterisk/pjsip_wizard.conf` with your preferred editor, and edit the following rows:

```
[trunk_defaults]   
type = wizard   
  
[telnyx]   
endpoint/transport = 0.0.0.0-udp   
endpoint/allow = !all,ulaw,alaw,G729,G722   
endpoint/rewrite_contact = yes   
endpoint/dtmf_mode = rfc4733   
endpoint/context = from-pstn   
endpoint/force_rport = yes   
aor/qualify_frequency = 60   
sends_auth = no   
sends_registrations = no   
remote_hosts = sip.telnyx.com:5060
```

|  |
| --- |
| ***Note:*** *For this configuration to work, the module res\_pjsp\_config\_wizard.so must be installed and loaded. This is available through Asterisk 13.2.0.* |

## 3. Configure Asterisk to Make and Accept Calls

​​You will need to modify the `/etc/asterisk/pjsip_wizard.conf` in order to add the global configurations for the extensions, and specific ones for the sample.

In this example, we are setting up extension 1001 to make and accept calls. Parameters that reference `1001` and `password` can be customized for your requirements and map to the following fields:

```
[user_defaults](!)  
type = wizard   
accepts_registrations = yes   
sends_registrations = no   
accepts_auth = yes   
sends_auth = no   
endpoint/context = from-internal   
endpoint/allow = !all,ulaw,alaw,G729,G722   
endpoint/dtmf_mode = rfc4733   
endpoint/rewrite_contact = yes   
endpoint/force_rport = yes   
aor/max_contacts = 1   
aor/remove_existing = yes   
aor/minimum_expiration = 30   
  
1001   
endpoint/callerid = Bart <1001>   
inbound_auth/username = Bart   
inbound_auth/password = strong@pass123$
```

After creating the template, setting up a new phone is often as simple as setting up a username/password, as the Phone object inherits from the Wizard template. You won't even need to specify a type. See the following examples:

```
[Bart](user_defaults)   
hint_exten = 1001  
endpoint/callerid = Bart <1001>  
inbound_auth/username = Bart  
inbound_auth/password = strong@pass135$
```

```
[Lisa](user_defaults)   
hint_exten = 1001  
endpoint/callerid = Lisa <1001>  
endpoint/allow = !all,ulaw  
inbound_auth/username = Lisa  
inbound_auth/password = strong@pass246$  
has_phoneprov = yes ; defaults to no  
phoneprov/MAC = hereweGOaga1n ;must specify if has_phoneprov=yes  
phoneprov/PROFILE = profile1 ;must specify if has_phoneprov=yes
```

## 4. Completing the basic PJSIP configuration

Even though `pjsip_wizard.conf` is a great facilitator in setting up PJSIP endpoints, global configurations, or anything else that might be needed can still be added in `/etc/asterisk/pjsip.conf`. In the scope of our basic setup, add the lines below to `pjsip.conf` for installations behind NAT.

```
[global]   
type = global   
[transport-udp-nat]   
type = transport   
protocol = udp   
bind = 0.0.0.0:5060   
local_net = X.X.X.X/24   
external_media_address = X.X.X.X   
external_signaling_address = X.X.X.X   
allow_reload = no
```

* In case the PBX is not in a NATed network, you can safely remove the following parameters: **external\_media\_address** and **external\_signaling\_address**.
* With the above configurations added to the respective files, your PBX should be now registered to Telnyx, and the extension 1001 in your IP phone/softphone should be registered to your PBX.

## **5.** Setting Up the Dialplan

Asterisk makes use of the dialplans saved in `/etc/asterisk/extensions.conf` in order to route calls between endpoints, among other tasks. To allow our extension 1001 to call the world through Telnyx, as well as to send it any calls that arrive to the Telnyx DID assigned to the respective trunk, you need to open up extension.conf and add the following lines of code:

**extensions.conf**

```
[from-pstn]   
exten => _+1NXXXXXXXXX,1,Dial(PJSIP/1001)   
exten => _NXXXXXXXXX,1,Dial(PJSIP/1001)   
  
[from-internal]   
exten = _NXXNXXXXXX,1,Dial(PJSIP/+1${EXTEN}@telnyx)   
same = n,Hangup()   
  
exten = _X.,1,Dial(PJSIP/+${EXTEN}@telnyx)   
same = n,Hangup()
```

* `[from-pstn]` is the context that captures inbound calls to the PBX coming from Telnyx, and sends them to the extension 1001. The `[from-ptsn]` code block will capture every call towards CLDs in US national (10 digit) or +E164 and send it to the extension 1001.
* `[from-internal]` serves to route calls towards the world through Telnyx. The `[from-internal]` code block will capture calls towards US national numbers, convert to +E164 or towards any other number, prepend “+”, and send the call to Telnyx.

|  |
| --- |
| ***IMPORTANT:*** *If your IP-based connection uses a tech prefix to authenticate, this must be reflected in the dialplan!*    For example, if you have set the tech prefix "9999" in Telnyx, your `[from-internal]` block should look like this:  ``` [from-internal] exten = _NXXNXXXXXX,1,Dial(PJSIP/9999+1${EXTEN}@telnyx)  same = n,Hangup()  exten = _X.,1,Dial(PJSIP/9999+${EXTEN}@telnyx)  same = n,Hangup() ``` |

That's it! You've completed your Asterisk configuration and can now make and receive calls by using Telnyx as your SIP provider. !

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:

* Asterisk’s [help section](https://community.asterisk.org/) for extra support.

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[Configuring a Vicidial IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx)[Configuring an Asterisk Credentials Trunk](https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk)[Configuring a GoAutoDial PBX SIP Trunk](https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk)[FreePBX V15: IP Trunk - PJSIP](https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip)

Did this answer your question?

😞😐😃

Table of contents
