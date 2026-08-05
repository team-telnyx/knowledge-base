---
title: Cisco and Yeastar SIP Trunk Configuration with Telnyx
summary: This page consolidates Telnyx guidance for configuring SIP trunks on Cisco
  CUBE/CUCM, Cisco CME, and Yeastar P-Series and S-Series PBX platforms. It covers
  both IP-authentication and credentials-based authentication, including dial-peer
  setup, codec preferences, NAT traversal, inbound DID translation, and outbound/inbound
  routing.
sources:
- url: https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk
- url: https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk
- url: https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk
- url: https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
- url: https://support.telnyx.com/en/articles/1130675-what-kind-of-equipment-do-you-use
- url: https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series
- url: https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip
updated_at: 2026-08-05T13:27:08Z
---

# Cisco and Yeastar SIP Trunk Configuration with Telnyx

*Part 1 of 4 — see also: [Part 2](cisco-and-yeastar-sip-trunk-configuration-with-telnyx--part-2.md), [Part 3](cisco-and-yeastar-sip-trunk-configuration-with-telnyx--part-3.md), [Part 4](cisco-and-yeastar-sip-trunk-configuration-with-telnyx--part-4.md)*

This page consolidates Telnyx guidance for configuring SIP trunks on Cisco CUBE/CUCM, Cisco CME, and Yeastar P-Series and S-Series PBX platforms. It covers both IP-authentication and credentials-based authentication, including dial-peer setup, codec preferences, NAT traversal, inbound DID translation, and outbound/inbound routing.

## Overview

Telnyx supports SIP trunking with a variety of enterprise and SMB telephony platforms. This page consolidates configuration guidance for Cisco Unified Border Element (CUBE) with Cisco Unified Communications Manager (CUCM), Cisco Unified Communications Manager Express (CME), and Yeastar P-Series and S-Series PBX systems. Two authentication models are supported throughout: IP authentication (peer trunk) and credentials-based authentication (register trunk).

For background on Telnyx's underlying network, see [What kind of equipment do you use?](what-kind-of-equipment-do-you-use.md) — Telnyx uses Cisco ASR routers for core and edge, Juniper QFX5100 for aggregation, and Brocade Vyatta with virtualized routing platforms for Cloud CE routing.

## Cisco CUBE/CUCM IP Trunk

[Cisco Unified Border Element (CUBE)](https://www.cisco.com/c/en/us/products/unified-communications/unified-border-element/index.html) provides secure voice and video connectivity from the enterprise IP network to a Telnyx [SIP trunk](https://telnyx.com/products/sip-trunks). CUBE performs session control, security, interworking, and demarcation, and can scale to up to 64,000 sessions with box-to-box and in-box redundancy.

### Pre-requisites

- Cisco recommends that your system *does not* have Domain Name System (DNS) configuration.
- CUCM Version 8.6 through Version 12.x. Note that all CUCM versions below 11.x have reached end of life/end of support, and 11.x versions are no longer being sold.
- Cisco IOS® Version 15.1(2)T and later.
- Enable either a valid caller ID or a caller ID override in your Telnyx Mission Control Portal. To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection.
- Have already completed the main CISCO/CUCM installation and telecommunication-applications deployment.

### Dial-peer configuration

The topology is **Telnyx <---> CUBE <---> CUCM**. Configure a dial-peer to Telnyx in global configuration mode:

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

Available only in some versions of Cisco IOS. In global configuration mode:

```
voice service voip
ip address trusted list
ipv4 192.76.120.10
ipv4 64.16.240.36
ipv4 172.0.0.0 !Private IP address of CUCM
```

### General SIP parameters

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

### Codec preference

In global configuration mode:

```
voice class codec 1
codec preference 1 g711ulaw
codec preference 2 g711alaw
codec preference 3 g729br8
```

### NAT traversal

If your CUBE is behind a NAT and does not have an interface with a public IP, modify the IPs in the SIP messages to your public IP using SIP Profiles. In global configuration mode:

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

It is also advisable to define a loopback interface and configure it with your public IP address. Do not advertise this into your network, as it may cause other problems. In global configuration mode:

```
interface loopback 0
ip address 1.2.3.4 255.255.255.0
```

### Inbound calling

Use translation rules and profiles to translate DIDs to extensions. Create a voice translation rule (the example below translates 13125489677 to 3005):

```
voice translation-rule 100
rule 1 /13125489677/ /3005/   !  Several rules can be defined. In this case, 3005 is an extension on CUCM
```

Create a translation profile using the rule:

```
voice translation-profile 100
translate called 100
```

Apply the translation profile to the dial-peer:

```
translation-profile incoming 100
```

### Dial-peer towards CUCM

In global configuration mode:

```
dial-peer voice 300 voip
destination-pattern 3...           !Matches 3XXX numbers, as translated by the translation profile
session protocol sipv2
session target ipv4:172.16.8.10
dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
```

For additional reference, see the [Cisco CUBE/CUCM integration documentation](https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/117300-configure-cube-00.html).

## Cisco CUBE/CUCM SIP Trunk (Credentials)

The credentials-based variant of the CUBE/CUCM integration uses the same dial-peer, allow-list, SIP parameters, codec, NAT traversal, and inbound translation configuration as the IP-authenticated trunk above, with the following differences:

- The `session target` should be set to `sip.telnyx.com` rather than an IP address.
- The `mode border-element` and `sip-profiles 1` lines are still required under `voice service voip`.
- A `sip-ua` block must be added to register with `sip.telnyx.com` using the username and password configured in the Telnyx portal:

```
sip-ua
credentials username <connection_username> password <connection_password> realm sip.telnyx.com
authentication username <connection_username> password <connection_password> realm sip.telnyx.com
registrar dns:sip.telnyx.com
```

The pre-requisites, NAT traversal, codec preference, and inbound DID translation steps are identical to the IP-authenticated CUBE/CUCM configuration.
