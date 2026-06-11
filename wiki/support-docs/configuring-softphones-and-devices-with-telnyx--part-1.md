---
title: Configuring Softphones and Devices with Telnyx
summary: A comprehensive guide to configuring a wide range of SIP softphones, team
  communication platforms, and hardware devices with Telnyx using credentials-based
  connections, covering common settings such as SIP domain, codecs, caller ID conventions,
  TLS/SRTP encryption, and device-specific setup steps.
sources:
- url: https://support.telnyx.com/en/articles/1130645-configuring-bria-solo-a-k-a-x-lite
  content_hash: 715c1767298dfd34f9de4aa7ccdc1fbbe3dff961c57a8c2026be07019deb4500
- url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
  content_hash: 94fa539b1fe2e4fa024745fa69ce40c63aa9053dbf037eecf031c128dc910ad0
- url: https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup
  content_hash: 09a46469b9366387ac4f7c53cdd9e92e47ad725ad980278285990b2d734636ac
- url: https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac
  content_hash: 07dff517a144626edb69478b062d07420323a364698a3eb2919754027bccfcc3
- url: https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux
  content_hash: 7edc2fa7abdd67cbd99f66ce6518e05e39e6a6b611ba5ea081dea2a144b37289
- url: https://support.telnyx.com/en/articles/5761112-acrobits-softphone
  content_hash: f2b2bbfaa9c4bb59034093ea8987a4233233c8a27cee580503ccebac41dd1e04
- url: https://support.telnyx.com/en/articles/5772825-counterpath-bria-teams-setup
  content_hash: 1687b49e78afc40ff34dfdbe8a54d89392c56be38d593126f732d13a938d005b
- url: https://support.telnyx.com/en/articles/5807979-konftel-300wx-telnyx-setup
  content_hash: ee9ad29b8d22624f13d9b9f8f41b4844ed0e1939a28a580f423d301e8a491a19
- url: https://support.telnyx.com/en/articles/5820183-plantronics-polycom-obi300-setup
  content_hash: 8ef74aceb7307a50d29f1d76291860422a5cb6d66121780f96ca1d64b24f2c2a
- url: https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx
  content_hash: 099c5f4bb532847138f710b1c676a9a24220a3d646540dfb1e8877d37d5ac5fd
- url: https://support.telnyx.com/en/articles/6133517-zoiper-communicator
  content_hash: d94de24a45beed31c1e5581dc3e5bad3e4b06195ffef6662f1ed2ce2f1170926
- url: https://support.telnyx.com/en/articles/6184748-grandstream-wave-lite-iphone
  content_hash: a585bed323d8201aa893f33e7394bd4c259483f5da8293f214486b62115d774e
- url: https://support.telnyx.com/en/articles/6184897-grandstream-wave-lite-android
  content_hash: c262c545cbf2f68d9663820d17994869b4607951a92f4287ba7edd3e9d396138
- url: https://support.telnyx.com/en/articles/6187273-grandstream-gds3710-wave-lite-android
  content_hash: d992630ed2dddf042bb062e72b4bfcac9b30c54ed2a8b1717a8a3320130e04c1
- url: https://support.telnyx.com/en/articles/6187411-grandstream-gds3710-wave-lite-ios
  content_hash: ed7c59987079659094e333f8345c6eff7710460dade2309723b7a10c8a957b32
- url: https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370
  content_hash: f75a754a6be7b66b4e892021cab6bf25785af6a4ab92b7982205bb1a2d62ab26
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
