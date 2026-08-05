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

*Part 1 of 6 — see also: [Part 2](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-2.md), [Part 3](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-3.md), [Part 4](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-4.md), [Part 5](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-5.md), [Part 6](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-6.md)*

Step-by-step guidance for connecting Thirdlane and 3CX (V18 and V20) IP-PBX systems to Telnyx as a SIP trunk provider, including trunk creation, inbound/outbound routing, extension setup, and SMS gateway configuration, along with notes on 3CX and Telnyx compatibility.

## Overview

This page consolidates Telnyx setup guides for two popular multi-tenant and Unified Communications PBX platforms: [Thirdlane PBX](https://www.thirdlane.com/products/thirdlane-pbx) and [3CX](https://www.3cx.com/). Both can be configured to make and receive calls (and, where supported, SMS) over the internet using Telnyx as the next-generation carrier.

Additional reference material:

- [Thirdlane user documentation](https://www.thirdlane.com/docs/platform/introduction)
- [Thirdlane support](https://www.thirdlane.com/support)
- [Thirdlane REST API](https://www.thirdlane.com/docs/platform/api)
- 3CX [help section](https://www.3cx.com/support/)
- Latest information on [3CX V20 Updates](https://www.3cx.com/blog/releases/)

## Pre-requisites (All Platforms)

Before configuring either PBX, complete the following in your Telnyx account:

- [Configure your Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).
- Set up a [SIP connection](https://portal.telnyx.com/#/app/connections) (credentials-based, IP-based, or FQDN-based) and assign it to a DID and an outbound voice profile.
- [Provision a DID from Telnyx](https://portal.telnyx.com/#/app/numbers/search-numbers) (see [Requesting numbers](https://support.telnyx.com/en/articles/3562148-requesting-numbers)).
- For SMS, create a [messaging profile](https://portal.telnyx.com/#/app/programmable-messaging/profiles) and assign it to your DIDs.
- Generate a Telnyx [API key](https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them) for messaging integrations.
