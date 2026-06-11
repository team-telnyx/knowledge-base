---
source_url: https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk
scraped: 2026-06-11
---

Configuring a Cisco CUBE/CUCM IP Trunk | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring a Cisco CUBE/CUCM IP Trunk

In this article we will walk you through configuring a Cisco CUBE/CUCM IP Trunk on the Telnyx network.

Written by Telnyx Sales

June 6, 2024

Table of contents

[Jump to Instructions](#h_901aa18804)

[Cisco Unified Border Element (CUBE)](https://www.cisco.com/c/en/us/products/unified-communications/unified-border-element/index.html) provides highly secure voice and video connectivity from the enterprise IP network to a Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks). CUBE performs session control, security, interworking, and demarcation. You can deploy virtually on Cisco servers or integrate into a Cisco router. Cisco CUBE also provides multiple services on the same routing platform, and can scale to up to 64,000 sessions with box-to-box and in-box redundancy.

Additional documentation:

* [Cisco CUBE/CUCM integration documentation](https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/117300-configure-cube-00.html)

---

# Instructions for integrating a Cisco CUBE with a Telnyx CUCM SIP trunk

This guide will help you establish a connection between your CISCO/CUCM server, and your Telnyx Mission Control Portal by showing you a sample trunk configuration. This assumes you've already completed the installation and telecommunication-applications deployment, per the pre-requisites.

In this activity you will

1. [Set up your Telnyx SIP trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk#h_a276b2d188)
2. [Configure a dial-peer to Telnyx](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk#h_788d3ac82c)

**Pre-requisites**

* Cisco recommends that your system *does not* have Domain Name System (DNS) configuration
* CUCM Version 8.6 through Version 12.x

  + Note that all CUCM versions below 11.x [have reached end of life/end of support](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html). And [11.x versions are no longer being sold](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html)
* Cisco IOS**®** Version 15.1(2)T and later
* [Enable either a valid caller ID or a caller ID override in your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)

  + *To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection.*
* Have already made the main CISCO/CUCM installation and telecommunication-applications deployment.

**Video Wakthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Cisco CUBE to CUCM integration coming soon. Check back as we update our docs.* |

## 1. Configure a Dial-Peer to Telnyx

This is the layout of our set-up:

### **Telnyx<--->CUBE<--->CUCM**

### **Configure a Dial-Peer to Telnyx as follows:**

*In global configuration mode*

```
dial-peer voice 100 voip        ! 100 is an arbitrary number  
translation-profile incoming 100  ! Used to translate DID to extension  
destination-pattern 1[2-9]..[2-9]...... !general pattern for an outgoing 11 digit calling  
session protocol sipv2  
voice-class sip profiles 1   ! Refers to a pre-configured SIP Profile, used to modify headers in SIP Messages  
session target ipv4:192.76.120.10  ! or replace with sip.telnyx.com  
incoming called-number 1[2-9]..[2-9]......   
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
ipv4 64.16.240.36  
ipv4 172.0.0.0 !Private IP address of CUCM
```

###

#### **Specify general SIP parameters:**

*In global configuration mode*

```
voice service voip  
mode border-element  ! Required if operating in CUBE mode, as opposed to CME  
allow connections sip to sip  ! Permit SIP to SIP calls  
sip  
early-offer forced  
midcall-signaling passthru  
sip-profiles 1   ! Refers to pre-configured sip profile
```

#### **Configure codec preference:**

*In global configuration mode*

```
voice class codec 1  
codec preference 1 g711ulaw  
codec preference 2 g711alaw  
codec preference 3 g729br8
```

#### **NAT Traversal:**

If your CUBE is behind a NAT and does not have an interface with a public IP, you need to modify the IPs in the SIP messages to your public IP using SIP Profiles as follows:

*In global configuration mode*

```
voice class sip-profiles 1  
response ANY sip-header Contact modify "172.x.y.z" "1.2.3.4" !1.2.3.4 Public IP; 172.x.y.z Private IP of the CUBE  
request ANY sip-header Contact modify "172.x.y.z" "1.2.3.4"   
response ANY sdp-header Audio-Connection-Info modify "172.x.y.z" "1.2.3.4"  
response ANY sdp-header Connection-Info modify "172.x.y.z" "1.2.3.4"  
response ANY sdp-header Session-Owner modify "172.x.y.z" "1.2.3.4"  
request ANY sdp-header Audio-Connection-Info modify "172.x.y.z" "1.2.3.4"  
request ANY sdp-header Connection-Info modify "172.x.y.z" "1.2.3.4"  
request ANY sdp-header Session-Owner modify "172.x.y.z" "1.2.3.4"
```

This can then be applied either globally to the general sip config (sip profiles #) or under the dial-peer config using:

```
voice-class sip profiles 1
```

Additionally, it is advisable to define a loopback interface and configure it with your public IP address. Do not advertise this into your network though, as it may cause other problems.

*In global configuration mode*

```
interface loopback 0  
ip address 1.2.3.4 255.255.255.0
```

#### **Inbound calling:**

Use translation rules and translation profiles to translate your DIDs to extensions.  
​

Create a voice translation rule. For example, the rule below translates 13125489677 to 3005

*In global configuration mode*

```
voice translation-rule 100  
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

#### **Configure the dial-peer towards CUCM**

*In global configuration mode*

```
dial-peer voice 300 voip  
destination-pattern 3...           !Matches 3XXX numbers, as translated by the translation profile  
session protocol sipv2  
session target ipv4:172.16.8.10  
dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
```

|  |
| --- |
| ***Note:*** *To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection. Please view our [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for information on enabling a caller ID override from within the Telnyx portal.* |

That's it, you've now completed the configuration of your Cisco CUBE/CUCM SIP Trunk

[Back to Top](#h_901aa18804)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Cisco CUBE/CUCM integration documentation](https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/117300-configure-cube-00.html)

---

Related Articles

[Cisco: Configure a Cisco CME IP Trunk](https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk)[Configuring an AVAYA IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx)[Configuring a Cisco CME Credentials Trunk](https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk)[Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)[Cisco: 68xx/88xx Setup](https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup)

Did this answer your question?

😞😐😃

Table of contents
