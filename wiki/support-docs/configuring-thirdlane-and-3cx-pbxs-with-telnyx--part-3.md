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

*Part 3 of 6 — see also: [Part 1](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-1.md), [Part 2](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-2.md), [Part 4](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-4.md), [Part 5](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-5.md), [Part 6](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-6.md)*

Step-by-step guidance for connecting Thirdlane and 3CX (V18 and V20) IP-PBX systems to Telnyx as a SIP trunk provider, including trunk creation, inbound/outbound routing, extension setup, and SMS gateway configuration, along with notes on 3CX and Telnyx compatibility.

## 3CX and Telnyx Compatibility

> **Important:** Telnyx is no longer a supported vendor on 3CX. 3CX has decided to shut down support for third-party vendors altogether in some versions and only offers customers the option to connect with their supported vendors. Verify that your 3CX version supports third-party providers before proceeding.

Key compatibility points:

- **Existing 3CX customers with Telnyx SIP trunks** can maintain their setup through normal updates. If a trunk is deleted, it can be recreated using the 3CX generic template (depending on version).
- **3CX generic template compatibility:** Works with the Telnyx Messaging API and basic calls. Full compatibility with all call scenarios is not guaranteed and may require adjustments.
- **Availability:** The 3CX generic template is only available for 3CX dedicated and 3CX self-hosted systems. It is unavailable in Hosted by 3CX systems (FREE, PRO, ENT licenses) and in 3CX StartUP.
- **Messaging API configuration changes:** 3CX systems using Telnyx Messaging API configurations must be switched to the 3CX generic template. Customers who did not transition during the available period must now use the generic template to support Telnyx for Messaging API.
- **Continued support:** Existing Telnyx SIP trunks in previous 3CX versions will continue to function with future updates.
