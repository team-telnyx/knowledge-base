---
title: Configuring Thirdlane and 3CX PBXs with Telnyx
summary: This page covers how to configure Telnyx as a SIP provider for Thirdlane
  and 3CX (V18 and V20) PBX systems, including trunk creation, inbound/outbound routing,
  caller ID, SMS gateway setup, and compatibility considerations between 3CX and Telnyx.
sources:
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- url: https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx
- url: https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility
- url: https://support.telnyx.com/en/articles/8683996-3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update
updated_at: 2026-07-17T09:04:30Z
---

# Configuring Thirdlane and 3CX PBXs with Telnyx

*Part 6 of 6 — see also: [Part 1](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-1.md), [Part 2](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-2.md), [Part 3](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-3.md), [Part 4](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-4.md), [Part 5](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-5.md)*

This page covers how to configure Telnyx as a SIP provider for Thirdlane and 3CX (V18 and V20) PBX systems, including trunk creation, inbound/outbound routing, caller ID, SMS gateway setup, and compatibility considerations between 3CX and Telnyx.

## Additional Resources

- [Getting started with Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- [Thirdlane user documentation](https://www.thirdlane.com/docs/platform/introduction)
- [Thirdlane support](https://www.thirdlane.com/support)
- [Thirdlane REST API](https://www.thirdlane.com/docs/platform/api)
- [3CX help section](https://www.3cx.com/support/)
- [Latest 3CX V18 Updates](https://www.3cx.com/blog/releases/)
- [Latest 3CX V20 Updates](https://www.3cx.com/blog/releases/)
- [3CX V20 roadmap](https://www.3cx.com/blog/releases/v20-roadmap/)
- [3CX outbound rules overview](https://www.3cx.com/blog/voip-howto/outbound-rules-a-complete-example/)
- [Telnyx SIP connection types](https://support.telnyx.com/en/articles/4245868-sip-connection-types)
- [Telnyx SIP connection number formats](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats)
- [Telnyx caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)
- [Telnyx API keys](https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them)
- [Telnyx SIP signaling addresses](https://sip.telnyx.com/#signaling-addresses)
- [Telnyx media IP addresses](https://sip.telnyx.com/#media)

## Related Articles

- [Configuring an Elastix 4 PBX IP Trunk](configuring-an-elastix-4-pbx-ip-trunk.md)
- [Configuring an Elastix 4 PBX Trunk](configuring-an-elastix-4-pbx-trunk.md)
- [Elastix 5: FQDN Trunk Setup](elastix-5-fqdn-trunk-setup.md)
- [Xorcom PBX: SIP Trunk](xorcom-pbx-sip-trunk.md)
- [How to configure Yeastar P-series](how-to-configure-yeastar-p-series.md)
- [BYOC: Telnyx & Genesys](byoc-telnyx-genesys.md)
- [Does Telnyx support conference calls?](does-telnyx-support-conference-calls.md)
- [Configure Token Authentication Header (X-Telnyx-Token) in FreePBX](configure-token-authentication-header-x-telnyx-token-in-freepbx.md)
- [3CX: Configuring a 3CX V20 PBX 20.0 Update 5 (Build 20.0.5.551) (March 2025 Update)](3cx-configuring-a-3cx-v20-pbx-20-0-update-5-build-20-0-5-551-march-2025-update.md)
- [3CX: Configuring a 3CX V18 PBX](3cx-configuring-a-3cx-v18-pbx.md)
- [How to configure a Thirdlane PBX](how-to-configure-a-thirdlane-pbx.md)
