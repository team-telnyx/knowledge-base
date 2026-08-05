---
title: Configuring Thirdlane and 3CX PBXs with Telnyx
summary: Step-by-step guidance for connecting Thirdlane and 3CX (V18 and V20) IP-PBX
  systems to Telnyx as a SIP trunk provider, including trunk creation, inbound/outbound
  routing, extension setup, and SMS gateway configuration, along with notes on 3CX
  and Telnyx compatibility.
sources:
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
- url: https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility
- url: https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update
updated_at: 2026-08-05T13:29:24Z
---

# Configuring Thirdlane and 3CX PBXs with Telnyx

*Part 6 of 6 — see also: [Part 1](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-1.md), [Part 2](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-2.md), [Part 3](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-3.md), [Part 4](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-4.md), [Part 5](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-5.md)*

Step-by-step guidance for connecting Thirdlane and 3CX (V18 and V20) IP-PBX systems to Telnyx as a SIP trunk provider, including trunk creation, inbound/outbound routing, extension setup, and SMS gateway configuration, along with notes on 3CX and Telnyx compatibility.

## Additional Resources

- [Getting started with Telnyx Mission Control](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- [Telnyx SIP connection types](https://support.telnyx.com/en/articles/4245868-sip-connection-types)
- [Telnyx SIP connection number formats](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats)
- [Telnyx caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)
- [Telnyx API keys and how to use them](https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them)
- [Requesting numbers from Telnyx](https://support.telnyx.com/en/articles/3562148-requesting-numbers)
- [Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)
- [Configuring an Elastix 4 PBX Trunk](https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk)
- [Elastix 5: FQDN Trunk Setup](https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup)
- [Xorcom PBX: SIP Trunk](https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk)
- [How to configure Yeastar P-series](https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series)
- [BYOC: Telnyx & Genesys](https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys)
- [Configure Token Authentication Header (X-Telnyx-Token) in FreePBX](https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx)
- [Does Telnyx support conference calls?](https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls)
