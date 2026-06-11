---
title: Configuring PBX SIP Trunks with Telnyx
summary: A consolidated guide for connecting enterprise PBX systems—including Cisco
  CUBE/CUCM, Cisco CME, Avaya, and Skype for Business—to Telnyx SIP trunks using either
  IP or credential-based authentication, covering dial-peer setup, codec preferences,
  NAT traversal, inbound routing, and platform-specific configuration steps.
sources:
- url: https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk
  content_hash: 1641534c34fa540edb01d95e3810d1502907eabbb59045687ec24538b110abd5
- url: https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk
  content_hash: d456c5aa82ab5d1ad33033bd6f9e7f5dff364be03ae17781308423938ed6244f
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
  content_hash: 3ffae37ef3a030f05481c2fe063d574bbf1b807f7e82b1534ca750432e9ad3eb
- url: https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk
  content_hash: 6f178599aeb8ccbb3f197b4673b694938ff87948e8efa6d86cf8fb63fb204eb7
- url: https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
  content_hash: 5684e2b733e7a9c3bf6c2eb157b2d50911a9c9199e79eac6952644941bddfe95
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
  content_hash: d292910b69b74f080522cfb140011099cc87881acf7c7add67a069e9c896efd4
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
  content_hash: 579305b4e90eaf859351c0077e8a7158f84e20d2012faf66abbfbf53639ab7fb
updated_at: 2026-06-11T11:24:50Z
---

# Configuring PBX SIP Trunks with Telnyx

*Part 1 of 2 — see also: [Part 2](configuring-pbx-sip-trunks-with-telnyx--part-2.md)*

A consolidated guide for connecting enterprise PBX systems—including Cisco CUBE/CUCM, Cisco CME, Avaya, and Skype for Business—to Telnyx SIP trunks using either IP or credential-based authentication, covering dial-peer setup, codec preferences, NAT traversal, inbound routing, and platform-specific configuration steps.

## Prerequisites and Common Requirements

Before configuring any PBX with Telnyx, ensure the following are in place:

- Your [Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) is set up and configured.
- A DID number is [provisioned from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) ([how to request numbers](https://support.telnyx.com/en/articles/3562148-requesting-numbers)).
- **Caller ID requirement:** To make outbound calls, Telnyx requires either a valid caller ID from your device or a caller ID override enabled on your SIP connection. See the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) for details on enabling an override from the portal.
- The PBX installation and telecommunication applications deployment are already completed.
- Cisco IOS Version 15.1(2)T or later is required for all Cisco configurations.

---

## Cisco CUBE/CUCM

[Cisco Unified Border Element (CUBE)](https://www.cisco.com/c/en/us/products/unified-communications/unified-border-element/index.html) provides secure voice and video connectivity from the enterprise IP network to a Telnyx SIP trunk. CUBE performs session control, security, interworking, and demarcation, and can scale to up to 64,000 sessions with box-to-box and in-box redundancy.

The topology is: **Telnyx ←→ CUBE ←→ CUCM**

CUCM versions 8.6 through 12.x are supported, though Cisco recommends the system does **not** have DNS configuration. Note that CUCM versions below 11.x [have reached end of life/end of support](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html), and 11.x versions are no longer being sold.

### Dial-Peer to Telnyx

*In global configuration mode:*

```
dial-peer voice 100 voip        ! 100 is an arbitrary number
 translation-profile incoming 100  ! Used to translate DID to extension
 destination-pattern 1[2-9]..[2-9]...... ! General pattern for outgoing 11-digit calling
 session protocol sipv2
 voice-class sip profiles 1   ! Refers to a pre-configured SIP Profile
 session target ipv4:192.76.120.10  ! Or replace with sip.telnyx.com
 incoming called-number 1[2-9]..[2-9]......
 dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
 voice-class codec 1       ! Refers to a pre-configured ordered list of codecs
```

### Allow-List SIP IPs

> **Note:** Only available in some versions of Cisco IOS.

*In global configuration mode:*

```
voice service voip
 ip address trusted list
 ipv4 192.76.120.10
 ipv4 64.16.240.36
 ipv4 172.0.0.0  ! Private IP address of CUCM
```

### General SIP Parameters

*In global configuration mode:*

```
voice service voip
 mode border-element  ! Required for CUBE mode
 allow connections sip to sip
 sip
  early-offer forced
  midcall-signaling passthru
  sip-profiles 1
```

### Codec Preference

*In global configuration mode:*

```
voice class codec 1
 codec preference 1 g711ulaw
 codec preference 2 g711alaw
 codec preference 3 g729br8
```

### NAT Traversal

If the CUBE is behind a NAT without a public IP interface, use SIP Profiles to replace the private IP with the public IP in SIP messages:

*In global configuration mode:*

```
voice class sip-profiles 1
 response ANY sip-header Contact modify "172.x.y.z" "1.2.3.4"
 request ANY sip-header Contact modify "172.x.y.z" "1.2.3.4"
 response ANY sdp-header Audio-Connection-Info modify "172.x.y.z" "1.2.3.4"
 response ANY sdp-header Connection-Info modify "172.x.y.z" "1.2.3.4"
 response ANY sdp-header Session-Owner modify "172.x.y.z" "1.2.3.4"
 request ANY sdp-header Audio-Connection-Info modify "172.x.y.z" "1.2.3.4"
 request ANY sdp-header Connection-Info modify "172.x.y.z" "1.2.3.4"
 request ANY sdp-header Session-Owner modify "172.x.y.z" "1.2.3.4"
```

Apply globally (`sip profiles #`) or under the dial-peer (`voice-class sip profiles 1`).

It is also advisable to define a loopback interface with the public IP (do not advertise it into your network):

```
interface loopback 0
 ip address 1.2.3.4 255.255.255.0
```

### Inbound Calling and DID Translation

Use translation rules and profiles to map DIDs to extensions. For example, translating `13125489677` to extension `3005`:

```
voice translation-rule 100
 rule 1 /13125489677/ /3005/

voice translation-profile 100
 translate called 100
```

Apply to the dial-peer:

```
translation-profile incoming 100
```

### Dial-Peer Towards CUCM

*In global configuration mode:*

```
dial-peer voice 300 voip
 destination-pattern 3...            ! Matches 3XXX numbers
 session protocol sipv2
 session target ipv4:172.16.8.10
 dtmf-relay rtp-nte cisco-rtp sip-kpml sip-notify
```

### Credential (Username/Password) Authentication

When using credentials authentication instead of IP authentication, register with `sip.telnyx.com` using the username and password from the Telnyx portal:

```
sip-ua
 credentials username <connection_username> password <connection_password> realm sip.telnyx.com
 authentication username <connection_username> password <connection_password> realm sip.telnyx.com
 registrar dns:sip.telnyx.com
```

For further reference, see the [Cisco CUBE/CUCM integration documentation](https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/117300-configure-cube-00.html).

---

## Cisco CME

[Cisco Unified Communications Manager Express (CME)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html) is a software-based entry-level telephony solution integrated into Cisco IOS, allowing small businesses or enterprise branches to deploy voice and data on a single platform.

The topology is: **Telnyx ←→ CME**

Additional prerequisites for CME include a valid Cisco.com account, access to a TFTP server, and the recommended Cisco IOS IP Voice image downloaded to flash memory.

### Dial-Peer to Telnyx

The dial-peer configuration is identical to the CUBE dial-peer shown above.

### Allow-List SIP IPs

```
voice service voip
 ip address trusted list
 ipv4 192.76.120.10
 ipv4 64.16.240.36  ! Media IP address
```

### General SIP Parameters

*In global configuration mode:*

```
voice service voip
 mode cme  ! CME mode instead of border-element
 allow connections sip to sip
 sip
  bind all source-interface  ! Bind control and media to an interface with an IP
  early-offer forced
  midcall-signaling passthru
```

### Codec Preference and NAT Traversal

Codec preference and NAT traversal configurations are the same as for CUBE/CUCM (see above).

### Inbound Calling and DID Translation

The translation rule and profile configuration is identical to the CUBE/CUCM inbound calling section.

### Credential (Username/Password) Authentication

When using credentials authentication, configure SIP UA registration as described in the CUBE/CUCM credential section above. This step is **not** needed when using IP authentication.

For further reference, see the [Cisco CME admin guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html) and the [Cisco CME SIP trunking configuration example](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-manager-express/91535-cme-sip-trunking-config.html).

---
