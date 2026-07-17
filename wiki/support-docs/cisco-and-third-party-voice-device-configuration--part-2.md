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

*Part 2 of 4 — see also: [Part 1](cisco-and-third-party-voice-device-configuration--part-1.md), [Part 3](cisco-and-third-party-voice-device-configuration--part-3.md), [Part 4](cisco-and-third-party-voice-device-configuration--part-4.md)*

This page consolidates Telnyx configuration guides for Cisco CUBE/CUCM IP and SIP trunks, Cisco CME IP and credentials trunks, the Cisco SPA112/122 ATA, and the BuddyTalk BT110/BT120 speakerphone. It also documents the deprecation of the Telnyx Access Control List feature and the Accessible Canada Act (ACA) feedback process.

## Cisco CME IP Trunk

[Cisco Unified Communications Manager Express (CME)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html) is a software-based entry-level telephony solution integrated directly into Cisco IOS, allowing small businesses or small enterprise branches to deploy and manage voice and data on a single platform. CME routers deliver key-system or hybrid PBX functionality, providing standard telephony features as well as many advanced features not available with traditional telephony solutions.

### Pre-requisites

- Your IP network is operational and you can access Cisco web.
- You have a valid Cisco.com account.
- You have access to a TFTP server for downloading files.
- Cisco router and all recommended services hardware for Cisco Unified CME is installed.
- Recommended Cisco IOS IP Voice or higher image is downloaded to flash memory in the router.
- Cisco IOS® Version 15.1(2)T and later.
- Enable a caller ID override in your Telnyx Mission Control Portal.
- Have already completed the main Cisco CME installation and telecommunication-applications deployment.

### Dial-Peer Configuration

The setup layout is **Telnyx <---> CUBE <---> CUCM**.

In global configuration mode:

```
dial-peer voice 100 voip        ! 100 is an arbitrary number  
translation-profile incoming 100  ! Used to translate DIDs to extensions  
destination-pattern 1[2-9]..[2-9]...... !general pattern for an outgoing 11 digit calling  
session protocol sipv2  
voice-class sip profiles 1   ! Refers to pre-configured sip profile. Used to modify headers  
session target ipv4:192.76.120.10  ! or replace with sip.telnyx.com  
incoming called-number 1[2-9]..[2-9]......  !Pattern-match for incoming DIDs  
dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify  
voice-class codec 1      ! 1 Refers to a pre-configured ordered list of codecs
```

### Allow-list SIP IPs

In some versions of IOS, you can whitelist SIP IPs as follows:

In global configuration mode:

```
voice service voip  
ip address trusted list  
ipv4 192.76.120.10  
ipv4 64.16.240.36 !Media IP address
```

### Specify General SIP Parameters

In global configuration mode:

```
voice service voip  
mode cme  
allow connections sip to sip  ! Permit SIP to SIP calls  
sip  
bind all source-interface  !Bind control and medial to an interface with an IP, if one is available  
early-offer forced  
midcall-signaling passthru
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

If your CUBE is behind a NAT and does not have a public IP, modify the IPs in the SIP messages to your public IP using SIP Profiles:

In global configuration mode:

```
voice class sip-profiles 1  
response ANY sip-header Contact modify "172.x.y.z" "1.2.3.4" !1.2.3.4 Public IP; 172.x.y.z Private IP of the CME  
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

It is also advisable to define a loopback interface and configure it with your public IP address. Do not advertise this into your network.

In global configuration mode:

```
interface loopback 0  
ip address 50.249.214.241 255.255.255.0
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

## Cisco CME Credentials Trunk

This guide covers the same CME topology but uses credential (username/password) authentication instead of IP authentication. The pre-requisites and most configuration steps are identical to the CME IP trunk configuration above, with the following addition:

### Required for Username/Password Authentication

Configure registration with sip.telnyx.com using the username and password set up on portal.telnyx.com:

In global configuration mode:

```
sip-ua  
credentials username <connection_username> password <connection_password> realm sip.telnyx.com  
authentication username <connection_username> password <connection_password> realm sip.telnyx.com   
registrar dns:sip.telnyx.com
```
