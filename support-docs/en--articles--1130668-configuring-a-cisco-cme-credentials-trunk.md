---
source_url: https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk
title: "Configuring a Cisco CME Credentials Trunk"
description: "In this article we will explain how you can configure a Cisco Call Manager Express User/Pass Trunk with Telnyx. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 6f178599aeb8ccbb3f197b4673b694938ff87948e8efa6d86cf8fb63fb204eb7
---







# Configuring a Cisco CME Credentials Trunk

In this article we will explain how you can configure a Cisco Call Manager Express User/Pass Trunk with Telnyx. See Telnyx guidance and requirements.




[Jump to Instructions](#h_a1ef61df3c)

[Cisco Unified Communications Manager Express (CME)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html) is a feature-rich and software-based entry-level telephony solution that is integrated directly into Cisco IOS, allowing small-businesses or small enterprise branches to deploy and manage voice and data on a single platform.

Cisco CME routers to deliver key-system or hybrid PBX functionality, providing almost all standard telephony features, as well as many advanced features not available with traditional telephony solutions.

Additional documentation:

* [Cisco CME admin guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html)
* [Cisco CME SIP trunking configuration example](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-manager-express/91535-cme-sip-trunking-config.html)

---

## Instructions for configuring a CME credentials trunk

This guide will help you establish a connection between Cisco CME, and your Telnyx Mission Control Portal by showing you a sample trunk configuration using **credential (username/password) authentication.** This assumes you've already completed the installation and telecommunication-applications deployment, per the pre-requisites.

In this activity you will:

1. [Set up a Telnyx SIP trunk](#h_807a945dc2)
2. [Configure a dial-peer to Telnyx](#h_bf6b119d16)

**Pre-requisites**

* Your IP network is operational and you can access Cisco web.
* You have a valid Cisco.com account.
* You have access to a TFTP server for downloading files.
* Cisco router and all recommended services hardware for Cisco Unified CME is installed. For installation information, see [Install Cisco Voice Services Hardware](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeplan.html#task_91761DDA380F4890A25367F04E782AC1)
* Recommended Cisco IOS IP Voice or higher image is downloaded to flash memory in the router. To determine which Cisco IOS software release supports the recommended Cisco Unified CME version, see [Cisco Unified CME and Cisco IOS Software Compatibility Matrix](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/requirements/guide/33matrix.html). For installation information, see [Install Cisco IOS Software](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeplan.html#task_39FFFD89768947A9BE5D8E178ABA6146)
* Cisco IOS**®** Version 15.1(2)T and later
* [Enable a caller ID override in your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)

  + *To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection.*
* Have already made the main Cisco CME installation and telecommunication-applications deployment.

**Video walkthrough**

Setting up your Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks):

|  |
| --- |
| ***Note:*** *Video walkthrough for Cisco CME configuration coming soon. Check back as we update our docs.* |

## 1. Configure a Dial-Peer to Telnyx

This is the layout of our set-up:

### **Telnyx<--->CUBE<--->CUCM**

#### Dial-peer configuration

*In global configuration mode*

```
dial-peer voice 100 voip        ! 100 is an arbitrary number
translation-profile incoming 100  ! Used to translate DIDs to extensions
destination-pattern 1[2-9]..[2-9]...... !general pattern for an outgoing 11 digit calling
session protocol sipv2
voice-class sip profiles 1   ! Refers to pre-configured sip profile. Used to modify headers
session target ipv4:192.76.120.10  ! or replace with sip.telnyx.com
incoming called-number 1[2-9]..[2-9]......  !Pattern-match for incoming DIDs
dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
voice-class codec 1      ! 1 Refers to a pre-configured ordered list of codecs
```

#### **Allow-list SIP IPs:**

|  |
| --- |
| ***Note:*** *This is only available in some versions of Cisco IOS* |

*In global configuration mode*

```
voice service voip
ip address trusted list
ipv4 192.76.120.10
ipv4 64.16.240.36 !Media IP address
```

#### **Specify general SIP parameters:**

*In global configuration mode*

```
voice service voip
mode cme
allow connections sip to sip  ! Permit SIP to SIP calls
sip
bind all source-interface  !Bind control and medial to an interface with a IP, if one is available
early-offer forced
midcall-signaling passthru
```

#### **Configure codec preference:**

*In global configuration mode*

```
voice class codec 1
codec preference 1 g711ulaw
codec preference 2 g711alaw
codec preference 3 g729br8
```

#### **NAT Traversal**

If your CUBE is behind a NAT and does not have a public IP, you need to modify the IPs in the SIP messages to your public IP using SIP Profiles as shown below:

*In global configuration mode*

```
voice class sip-profiles 1
response ANY sip-header Contact modify "172.x.y.z" "1.2.3.4" !1.2.3.4 Public IP; 172.x.y.z Private IP of the CME
request ANY sip-header Contact modify "172.x.y.z" "1.2.3.4"
response ANY sdp-header Audio-Connection-Info modify "172.x.y.z" "1.2.3.4"
response ANY sdp-header Connection-Info modify "172.x.y.z" "1.2.3.4"
response ANY sdp-header Session-Owner modify "172.x.y.z" "1.2.3.4"
request ANY sdp-header Audio-Connectio (Not needed if using IP authentication):n-Info modify "172.x.y.z" "1.2.3.4"
request ANY sdp-header Connection-Info modify "172.x.y.z" "1.2.3.4"
request ANY sdp-header Session-Owner modify "172.x.y.z" "1.2.3.4"
```

This can then be applied either globally to the general sip config or under the dial-peer config using:

```
voice-class sip profiles 1
```

Additionally, it is advisable to define a loopback interface and configure it with your public IP address. Do not advertise this into your network though, as it may cause other problems.

*In global configuration mode*

```
interface loopback 0
ip address 50.249.214.241 255.255.255.0
```

#### **Inbound calling:**

Use translation rules and translation profiles to translate your DIDs to extensions.

Create a voice translation rule. For example, the rule below translates 13125489677 to 3005

*In global configuration mode*

```
voice translation-rule 100 (Not needed if using IP authentication):
rule 1 /13125489677/ /3005/   !  Several rules can be defined. In this case, 3005 is an extension on CUCM
```

Create a translation profile using the rule created:

*In global configuration mode*

```
voice translation-profile 100
translate called 100
```

Apply the translation profile to the dial-peer:

```
translation-profile incoming 100
```

**Required for username/password (credentials) authentication** *(Not needed if using IP authentication):*

Configure registration with sip.telnyx.com using username and password set up on portal.telnyx.com as follows:

*In global configuration mode*

```
sip-ua
credentials username <connection_username> password <connection_password> realm sip.telnyx.com
authentication username <connection_username> password <connection_password> realm sip.telnyx.com
registrar dns:sip.telnyx.com
```

|  |
| --- |
| ***Note:*** *To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection. Please view our [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for information on enabling a caller ID override from within the Telnyx portal.* |

That's it, you've now completed the configuration of your Cisco CUBE/CUCM SIP Trunk

[Back to Top](#h_a1ef61df3c)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Cisco CME admin guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html)
* [Cisco CME SIP trunking configuration example](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-manager-express/91535-cme-sip-trunking-config.html)

---

Related Articles

[Configuring a Cisco CUBE/CUCM IP Trunk](https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk)[Cisco: Configure a Cisco CME IP Trunk](https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk)[Configuring an AVAYA IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx)[Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)[FreeSWITCH: Credentials Trunk](https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk)

Did this answer your question?

😞😐😃
