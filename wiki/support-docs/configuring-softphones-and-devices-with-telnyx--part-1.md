---
title: Configuring Softphones and Devices with Telnyx
summary: A comprehensive guide to configuring a wide range of SIP softphones, team
  communication platforms, and hardware devices with Telnyx using credentials-based
  connections, covering common settings such as SIP domain, codecs, caller ID conventions,
  TLS/SRTP encryption, and device-specific setup steps.
sources:
- url: https://support.telnyx.com/en/articles/1130645-configuring-bria-solo-a-k-a-x-lite
- url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
- url: https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup
- url: https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac
- url: https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux
- url: https://support.telnyx.com/en/articles/5761112-acrobits-softphone
- url: https://support.telnyx.com/en/articles/5772825-counterpath-bria-teams-setup
- url: https://support.telnyx.com/en/articles/5807979-konftel-300wx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5820183-plantronics-polycom-obi300-setup
- url: https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/6133517-zoiper-communicator
- url: https://support.telnyx.com/en/articles/6184748-grandstream-wave-lite-iphone
- url: https://support.telnyx.com/en/articles/6184897-grandstream-wave-lite-android
- url: https://support.telnyx.com/en/articles/6187273-grandstream-gds3710-wave-lite-android
- url: https://support.telnyx.com/en/articles/6187411-grandstream-gds3710-wave-lite-ios
- url: https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370
updated_at: 2026-06-11T11:29:23Z
---

# Configuring Softphones and Devices with Telnyx

*Part 1 of 3 — see also: [Part 2](configuring-softphones-and-devices-with-telnyx--part-2.md), [Part 3](configuring-softphones-and-devices-with-telnyx--part-3.md)*

A comprehensive guide to configuring a wide range of SIP softphones, team communication platforms, and hardware devices with Telnyx using credentials-based connections, covering common settings such as SIP domain, codecs, caller ID conventions, TLS/SRTP encryption, and device-specific setup steps.

## Prerequisites

Before configuring any softphone or device with Telnyx, ensure the following:

- Your [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) account is properly configured.
- You have created a **credentials-based SIP connection** in the Portal and noted its username and password.
- The connection is assigned to a **DID** (phone number) and an **outbound voice profile** so you can make and receive calls.
- For encrypted traffic, enable TLS on your SIP connection in the Telnyx Portal. If "Encrypted SIP Traffic" is enabled on the Portal but your device sends UDP/TCP or plain RTP, the call will be rejected with error code 488.

## Common SIP Settings

All Telnyx-compatible softphones and devices share these core parameters:

| Parameter | Unencrypted | Encrypted (TLS/SRTP) |
|---|---|---|
| SIP Domain / Server | sip.telnyx.com | sip.telnyx.com |
| SIP Port | 5060 | 5061 |
| Transport | UDP or TCP | TLS |
| Registration Expiry | 300 seconds | 300 seconds |
| STUN Server | stun.telnyx.com:3478 | stun.telnyx.com:3478 |
| Outbound Proxy | sip.telnyx.com | sip.telnyx.com |

For SIP server addresses outside the USA, consult the [Telnyx signaling addresses table](https://sip.telnyx.com/#signaling-addresses).

## Supported Audio and Video Codecs

Telnyx supports the following codecs. Configure them in order of preference on your device:

**Audio:**
- ulaw (G.711u)
- alaw (G.711a)
- G.722
- G.729

**Video:**
- H.264

## Caller ID Conventions

Telnyx enforces a strict caller ID policy. When setting the Display Name / Caller ID Name field on any softphone or device:

- Use **capital letters** for better visibility on receiving devices.
- **Do not use special characters** (dots, commas, apostrophes, etc.) — they will not be displayed.
- **Spaces are allowed.**
- Some Canadian providers truncate the name after **15 characters**; keep names concise.
- The caller ID number must be a Telnyx number on your account or a previously verified number. See the [caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) and [verified numbers](https://support.telnyx.com/en/articles/6988813-verified-numbers) for details.

If you receive a **403 error** about an invalid caller ID, the softphone may not be passing the caller ID in the required header. As a workaround, configure a **caller ID override** in the outbound section of your SIP connection settings in the Telnyx Portal.
