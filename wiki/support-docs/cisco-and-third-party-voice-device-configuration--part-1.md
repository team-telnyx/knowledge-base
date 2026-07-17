---
title: Cisco and Third-Party Voice Device Configuration
summary: This page consolidates Telnyx configuration guides for Cisco CUBE/CUCM IP
  and SIP trunks, Cisco CME IP and credentials trunks, the Cisco SPA112/122 ATA, and
  the BuddyTalk BT110/BT120 speakerphone. It also documents the deprecation of the
  Telnyx Access Control List feature and the Accessible Canada Act (ACA) feedback
  process.
sources:
- url: https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk
- url: https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
- url: https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk
- url: https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
- url: https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120
- url: https://support.telnyx.com/en/articles/6228388-aca-feedback-process
updated_at: 2026-07-17T09:02:19Z
---

# Cisco and Third-Party Voice Device Configuration

*Part 1 of 4 — see also: [Part 2](cisco-and-third-party-voice-device-configuration--part-2.md), [Part 3](cisco-and-third-party-voice-device-configuration--part-3.md), [Part 4](cisco-and-third-party-voice-device-configuration--part-4.md)*

This page consolidates Telnyx configuration guides for Cisco CUBE/CUCM IP and SIP trunks, Cisco CME IP and credentials trunks, the Cisco SPA112/122 ATA, and the BuddyTalk BT110/BT120 speakerphone. It also documents the deprecation of the Telnyx Access Control List feature and the Accessible Canada Act (ACA) feedback process.

## Overview

This page consolidates Telnyx configuration guides for several Cisco and third-party voice devices, along with related operational notes. It covers Cisco CUBE/CUCM IP and SIP trunks, Cisco CME IP and credentials trunks, the Cisco SPA112/122 ATA, and the BuddyTalk BT110/BT120 speakerphone. It also documents the deprecation of the Telnyx Access Control List feature and the Accessible Canada Act (ACA) feedback process.

## Cisco CUBE/CUCM IP Trunk

[Cisco Unified Border Element (CUBE)](https://www.cisco.com/c/en/us/products/unified-communications/unified-border-element/index.html) provides secure voice and video connectivity from the enterprise IP network to a Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks). CUBE performs session control, security, interworking, and demarcation, and can be deployed virtually on Cisco servers or integrated into a Cisco router. It supports multiple services on the same routing platform and can scale to up to 64,000 sessions with box-to-box and in-box redundancy.

### Pre-requisites

- Cisco recommends that your system *does not* have Domain Name System (DNS) configuration.
- CUCM Version 8.6 through Version 12.x. Note that all CUCM versions below 11.x have reached end of life/end of support, and 11.x versions are no longer being sold.
- Cisco IOS® Version 15.1(2)T and later.
- Enable either a valid caller ID or a caller ID override in your Telnyx Mission Control Portal. To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection.
- Have already completed the main CISCO/CUCM installation and telecommunication-applications deployment.

### Configure a Dial-Peer to Telnyx

The setup layout is **Telnyx <---> CUBE <---> CUCM**.

In global configuration mode:

```
dial-peer voice 100 voip        ! 100 is an arbitrary number  
translation-profile incoming 100  ! Used to translate DID to extension  
destination-pattern 1[2-9]..[2-9]...... !general pattern for an outgoing 11 digit calling  
session protocol sipv2  
voice-class sip profiles 1   ! Refers to a pre-configured SIP Profile, used to modify headers in SIP Messages  
session target ipv4:192.76.120.10  ! or replace with sip.telnyx.com  
incoming called-number 1[2-9]..[2-9]......   
dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify  
voice-class codec 1      ! 1 Refers to a pre-configured ordered list of codecs
```

### Allow-list SIP IPs

> Note: This is only available in some versions of Cisco IOS.

In global configuration mode:

```
voice service voip  
ip address trusted list  
ipv4 192.76.120.10  
ipv4 64.16.240.36  
ipv4 172.0.0.0 !Private IP address of CUCM
```

### Specify General SIP Parameters

In global configuration mode:

```
voice service voip  
mode border-element  ! Required if operating in CUBE mode, as opposed to CME  
allow connections sip to sip  ! Permit SIP to SIP calls  
sip  
early-offer forced  
midcall-signaling passthru  
sip-profiles 1   ! Refers to pre-configured sip profile
```

### Configure Codec Preference

In global configuration mode:

```
voice class codec 1  
codec preference 1 g711ulaw  
codec preference 2 g711alaw  
codec preference 3 g729br8
```

### NAT Traversal

If your CUBE is behind a NAT and does not have an interface with a public IP, modify the IPs in the SIP messages to your public IP using SIP Profiles:

In global configuration mode:

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

Apply either globally to the general SIP config or under the dial-peer config using:

```
voice-class sip profiles 1
```

It is also advisable to define a loopback interface and configure it with your public IP address. Do not advertise this into your network, as it may cause other problems.

In global configuration mode:

```
interface loopback 0  
ip address 1.2.3.4 255.255.255.0
```

### Inbound Calling

Use translation rules and translation profiles to translate your DIDs to extensions. The rule below translates 13125489677 to 3005.

In global configuration mode:

```
voice translation-rule 100  
rule 1 /13125489677/ /3005/   !  Several rules can be defined. In this case, 3005 is an extension on CUCM
```

Create a translation profile using the rule created:

In global configuration mode:

```
voice translation-profile 100  
translate called 100
```

Apply the translation profile to the dial-peer:

```
translation-profile incoming 100
```

### Configure the Dial-Peer Towards CUCM

In global configuration mode:

```
dial-peer voice 300 voip  
destination-pattern 3...           !Matches 3XXX numbers, as translated by the translation profile  
session protocol sipv2  
session target ipv4:172.16.8.10  
dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
```

> Note: To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection. See the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for information on enabling a caller ID override from within the Telnyx portal.

## Cisco CUBE/CUCM SIP Trunk (Username/Password Authentication)

This guide covers the same CUBE/CUCM topology but uses username/password authentication instead of IP authentication. The pre-requisites and most configuration steps are identical to the IP trunk configuration above, with the following differences:

- The dial-peer `session target` uses `sip.telnyx.com` rather than an IP address.
- The allow-list SIP IPs block does not include the CUCM private IP.
- The general SIP parameters block does not include `sip-profiles 1`.

### Required for Username/Password Authentication

Configure registration with sip.telnyx.com using the username and password set up on portal.telnyx.com:

In global configuration mode:

```
sip-ua  
credentials username <connection_username> password <connection_password> realm sip.telnyx.com  
authentication username <connection_username> password <connection_password> realm sip.telnyx.com   
registrar dns:sip.telnyx.com
```
