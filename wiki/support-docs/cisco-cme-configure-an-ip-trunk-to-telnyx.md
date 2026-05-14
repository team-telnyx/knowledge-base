---
title: 'Cisco CME: Configure an IP Trunk to Telnyx'
summary: How to configure a Cisco Call Manager Express (CME) SIP/IP trunk to Telnyx
  using IP authentication, including dial-peer setup, SIP service parameters, codec
  preferences, NAT handling with SIP Profiles, and inbound DID translation.
sources:
- url: https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk
  content_hash: 3806a4300cffd35bf8a51cdb444a548f0b0ce5b53e6bb6a8aba19b5061ce78b5
updated_at: 2026-05-14T11:45:08Z
---

# Cisco CME: Configure an IP Trunk to Telnyx

How to configure a Cisco Call Manager Express (CME) SIP/IP trunk to Telnyx using IP authentication, including dial-peer setup, SIP service parameters, codec preferences, NAT handling with SIP Profiles, and inbound DID translation.

## Overview
Cisco Unified Communications Manager Express (CME) is a software-based telephony solution integrated into Cisco IOS. This guide shows a sample configuration to connect CME to Telnyx over an IP-authenticated SIP trunk, covering outbound and inbound call handling.

## Prerequisites
- Operational IP network with access to Cisco device management.
- Cisco.com account and access to a TFTP server (for general CME deployments).
- Cisco router with recommended voice services hardware for CME and a compatible IOS image (IOS 15.1(2)T or later recommended). See Cisco’s compatibility and installation guides for details.
- A Telnyx Mission Control Portal account and a SIP trunk/connection set up for IP authentication.
- Caller ID requirement: Telnyx requires either a valid caller ID from your device or an outbound caller ID override enabled on your SIP connection.
- CME installation and application deployment already completed.

Additional background:
- Cisco CME admin guide: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html
- Cisco CME SIP trunking example: https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-manager-express/91535-cme-sip-trunking-config.html

## Reference topology
Telnyx <—> CUBE <—> CUCM/CME

## Configure the Telnyx dial peer
In global configuration mode, define a VoIP dial peer toward Telnyx. Adjust destination patterns and targets as appropriate for your deployment.

```
dial-peer voice 100 voip                  ! 100 is an arbitrary identifier
 translation-profile incoming 100         ! Translate inbound DIDs to extensions
 destination-pattern 1[2-9]..[2-9]......  ! General 11-digit NANPA outbound pattern
 session protocol sipv2
 voice-class sip profiles 1               ! Apply pre-configured SIP Profile (see NAT section)
 session target ipv4:192.76.120.10        ! Or replace with sip.telnyx.com
 incoming called-number 1[2-9]..[2-9]...... ! Match inbound DIDs
 dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
 voice-class codec 1                      ! Apply ordered codec list (defined below)
```

## Optionally trust Telnyx signaling/media IPs
Some IOS versions support whitelisting trusted SIP/media IPs:

```
voice service voip
 ip address trusted list
  ipv4 192.76.120.10
  ipv4 64.16.240.36     ! Media IP address
```

## Set global SIP service parameters
Enable SIP-to-SIP connections and recommended behaviors. Bind to the interface carrying your signaling and media.

```
voice service voip
 mode cme
 allow connections sip to sip
 sip
  bind all source-interface               ! Bind control/media to the interface with an IP
  early-offer forced
  midcall-signaling passthru
```

Note: Replace the bind target with the specific interface used for SIP signaling in your environment.

## Define codec preferences
Create an ordered codec preference list and reference it in your dial peer.

```
voice class codec 1
 codec preference 1 g711ulaw
 codec preference 2 g711alaw
 codec preference 3 g729br8
```

## Handle NAT with SIP Profiles
If your CUBE/CME is behind NAT (no public IP on the signaling interface), rewrite private addresses in SIP headers and SDP using a SIP Profile. Replace placeholders with your actual private and public IPs.

```
voice class sip-profiles 1
 response ANY sip-header Contact               modify "172.x.y.z" "1.2.3.4"  ! 1.2.3.4 = Public IP; 172.x.y.z = Private IP
 request  ANY sip-header Contact               modify "172.x.y.z" "1.2.3.4"
 response ANY sdp-header Audio-Connection-Info modify "172.x.y.z" "1.2.3.4"
 response ANY sdp-header Connection-Info       modify "172.x.y.z" "1.2.3.4"
 response ANY sdp-header Session-Owner         modify "172.x.y.z" "1.2.3.4"
 request  ANY sdp-header Audio-Connection-Info modify "172.x.y.z" "1.2.3.4"
 request  ANY sdp-header Connection-Info       modify "172.x.y.z" "1.2.3.4"
 request  ANY sdp-header Session-Owner         modify "172.x.y.z" "1.2.3.4"
```

Apply the profile globally (as shown in the dial peer via voice-class sip profiles 1) or per dial peer as needed.

## Optional: Assign a public loopback IP
Defining a loopback interface with your public IP can help in NAT scenarios. Do not advertise this IP inside your network.

```
interface loopback 0
 ip address 50.249.214.241 255.255.255.0
```

## Map inbound DIDs to extensions
Translate inbound DIDs to internal extensions using translation rules and profiles, then apply to the Telnyx dial peer (already shown via translation-profile incoming 100).

```
voice translation-rule 100
 rule 1 /13125489677/ /3005/         ! Example: map DID 13125489677 to extension 3005

voice translation-profile 100
 translate called 100
```

Attach to the inbound side of the Telnyx dial peer:

```
translation-profile incoming 100
```

## Finish
Once the dial peer, SIP service parameters, codec list, and (if needed) NAT SIP Profile are in place, your Cisco CUBE/CUCM/CME should be able to place and receive calls via the Telnyx IP trunk using the defined patterns and translations.

## Additional resources
- Get started with a Mission Control account: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- Cisco CME admin guide: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html
- Cisco CME SIP trunking configuration example: https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-manager-express/91535-cme-sip-trunking-config.html
