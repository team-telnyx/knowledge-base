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

*Part 2 of 4 — see also: [Part 1](cisco-and-yeastar-sip-trunk-configuration-with-telnyx--part-1.md), [Part 3](cisco-and-yeastar-sip-trunk-configuration-with-telnyx--part-3.md), [Part 4](cisco-and-yeastar-sip-trunk-configuration-with-telnyx--part-4.md)*

This page consolidates Telnyx guidance for configuring SIP trunks on Cisco CUBE/CUCM, Cisco CME, and Yeastar P-Series and S-Series PBX platforms. It covers both IP-authentication and credentials-based authentication, including dial-peer setup, codec preferences, NAT traversal, inbound DID translation, and outbound/inbound routing.

## Cisco CME IP Trunk

[Cisco Unified Communications Manager Express (CME)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html) is a software-based entry-level telephony solution integrated directly into Cisco IOS, allowing small businesses or small enterprise branches to deploy and manage voice and data on a single platform. CME routers deliver key-system or hybrid PBX functionality with most standard telephony features plus many advanced features.

### Pre-requisites

- Your IP network is operational and you can access Cisco web.
- You have a valid Cisco.com account.
- You have access to a TFTP server for downloading files.
- Cisco router and all recommended services hardware for Cisco Unified CME is installed. See [Install Cisco Voice Services Hardware](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeplan.html#task_91761DDA380F4890A25367F04E782AC1).
- Recommended Cisco IOS IP Voice or higher image is downloaded to flash memory. See the [Cisco Unified CME and Cisco IOS Software Compatibility Matrix](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/requirements/guide/33matrix.html) and [Install Cisco IOS Software](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeplan.html#task_39FFFD89768947A9BE5D8E178ABA6146).
- Cisco IOS® Version 15.1(2)T and later.
- Enable a caller ID override in your Telnyx Mission Control Portal.
- Have already completed the main Cisco CME installation and telecommunication-applications deployment.

### Dial-peer configuration

The topology is **Telnyx <---> CUBE <---> CUCM**. In global configuration mode:

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

```
voice service voip
ip address trusted list
ipv4 192.76.120.10
ipv4 64.16.240.36 !Media IP address
```

### General SIP parameters

```
voice service voip
mode cme
allow connections sip to sip  ! Permit SIP to SIP calls
sip
bind all source-interface  !Bind control and media to an interface with an IP, if one is available
early-offer forced
midcall-signaling passthru
```

### Codec preference

```
voice class codec 1
codec preference 1 g711ulaw
codec preference 2 g711alaw
codec preference 3 g729br8
```

### NAT traversal

If your CUBE is behind a NAT and does not have a public IP, modify the IPs in the SIP messages to your public IP using SIP Profiles:

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

Apply globally or under the dial-peer config using `voice-class sip profiles 1`. Define a loopback interface with your public IP address (do not advertise it into your network):

```
interface loopback 0
ip address 50.249.214.241 255.255.255.0
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

For additional reference, see the [Cisco CME admin guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html) and [Cisco CME SIP trunking configuration example](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-manager-express/91535-cme-sip-trunking-config.html).

## Cisco CME Credentials Trunk

The credentials-based CME trunk uses the same dial-peer, allow-list, SIP parameters, codec, NAT traversal, and inbound translation configuration as the IP-authenticated CME trunk above, with the addition of a `sip-ua` block to register with `sip.telnyx.com` using the username and password configured in the Telnyx portal:

```
sip-ua
credentials username <connection_username> password <connection_password> realm sip.telnyx.com
authentication username <connection_username> password <connection_password> realm sip.telnyx.com
registrar dns:sip.telnyx.com
```

The pre-requisites, NAT traversal, codec preference, and inbound DID translation steps are identical to the IP-authenticated CME configuration.
