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

*Part 3 of 6 — see also: [Part 1](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-1.md), [Part 2](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-2.md), [Part 4](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-4.md), [Part 5](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-5.md), [Part 6](configuring-thirdlane-and-3cx-pbxs-with-telnyx--part-6.md)*

This page covers how to configure Telnyx as a SIP provider for Thirdlane and 3CX (V18 and V20) PBX systems, including trunk creation, inbound/outbound routing, caller ID, SMS gateway setup, and compatibility considerations between 3CX and Telnyx.

## 3CX and Telnyx Compatibility

[3CX](https://www.3cx.com/) is an open-standards IP PBX offering complete Unified Communications out of the box, suitable for any business size or industry.

### Compatibility Notes

- **Existing 3CX customers with Telnyx SIP trunks** can maintain their setup if they update their systems normally. If the SIP trunk is deleted, it can be recreated using the 3CX generic template depending on the 3CX version.
- **3CX generic template compatibility:** The 3CX generic template works with the Telnyx Messaging API and basic calls. Full compatibility with all call scenarios is not guaranteed and may require adjustments.
- **Availability:** The 3CX generic template is only available for 3CX dedicated and 3CX self-hosted systems. It is unavailable in Hosted by 3CX systems (FREE, PRO, ENT licenses) and in 3CX StartUP.
- **Messaging API configuration changes:** 3CX systems using Telnyx Messaging API configurations must be switched to the 3CX generic template. Customers who did not transition during the available period must now use the 3CX generic template to support Telnyx for Messaging API.
- **Continued support:** Existing Telnyx SIP trunks in previous 3CX versions will continue to function with future updates.

> **Important:** Telnyx is no longer a supported carrier on 3CX. 3CX has decided to shut down support for third-party carriers altogether in some of their versions and to only offer customers the option to connect with their supported carriers. Ensure that your 3CX version supports third-party vendors (providers not officially supported by 3CX) before proceeding.
