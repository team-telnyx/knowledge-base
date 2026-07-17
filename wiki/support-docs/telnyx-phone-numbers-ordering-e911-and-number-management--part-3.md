---
title: 'Telnyx Phone Numbers: Ordering, E911, and Number Management'
summary: This page consolidates Telnyx guidance on phone number ordering, including
  account verification restrictions, searching and buying numbers, requirement groups,
  working with the numbering team, E911 address registration and setup, testing E911
  with 933, handling spam/scam-likely flags, and managing numbers through the My Numbers
  Page.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
- url: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
- url: https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
updated_at: 2026-07-17T09:01:25Z
---

# Telnyx Phone Numbers: Ordering, E911, and Number Management

*Part 3 of 6 — see also: [Part 1](telnyx-phone-numbers-ordering-e911-and-number-management--part-1.md), [Part 2](telnyx-phone-numbers-ordering-e911-and-number-management--part-2.md), [Part 4](telnyx-phone-numbers-ordering-e911-and-number-management--part-4.md), [Part 5](telnyx-phone-numbers-ordering-e911-and-number-management--part-5.md), [Part 6](telnyx-phone-numbers-ordering-e911-and-number-management--part-6.md)*

This page consolidates Telnyx guidance on phone number ordering, including account verification restrictions, searching and buying numbers, requirement groups, working with the numbering team, E911 address registration and setup, testing E911 with 933, handling spam/scam-likely flags, and managing numbers through the My Numbers Page.

## E911 Setup Guide

This guide explains how to enable regular E911 service for a Telnyx phone number in the Mission Control Portal. Regular E911 links one emergency service address to one Telnyx phone number. If your application needs to send a caller's location dynamically, review the Dynamic E911 section before using this setup.

### Regular E911 vs. Dynamic E911

| Setup type | Use this when | How is the location provided |
| --- | --- | --- |
| Regular per-number E911 | A Telnyx phone number should always route emergency calls using one fixed service address. | You assign an emergency address directly to the phone number in the Portal. |
| Dynamic E911 | The caller's location can change, such as nomadic, mobile, MLTS, WebRTC, IoT, or application-managed location use cases. | Location is provided dynamically through a separate Dynamic E911 workflow. |

Most customers with a fixed address should use the regular per-number E911 setup.

### Before You Begin

Make sure you have:

- A Telnyx phone number in your account
- The full emergency service address for that number
- Any suite, unit, floor, or room information that helps emergency responders locate the caller
- Permission to accept the monthly emergency services charge shown in the Portal

Do not use 911 to test emergency service. Use 933 after E911 is enabled and the number is ready.

### Enabling E911 for a Phone Number

1. Sign in to the Telnyx Mission Control Portal.
2. Go to **Phone Numbers** and select the phone number you want to configure.
3. Open the number's **Emergency** or **E911** settings (may appear as an ambulance icon).
4. Turn on emergency services for the number.
5. Select an existing emergency address, or choose **New Address** to add one.
6. Enter the emergency service address carefully, including suite, unit, floor, room, or other location details. If the Portal suggests or normalises the address, review and use the suggested version if correct. If the address is rejected or cannot be saved, contact [support@telnyx.com](mailto:support@telnyx.com) with the phone number, address, and a screenshot or exact error message.
7. Click **Save Changes**.
8. Review the monthly charge confirmation.
9. Click **Accept** to enable emergency services for the number.

After saving, confirm the Portal shows the number as ready or active for emergency service before relying on it for emergency calls. If the Portal shows a pending, failed, or error state, wait and refresh. If the status does not become ready/active, or if you are unsure, contact [support@telnyx.com](mailto:support@telnyx.com) before testing or relying on emergency calling.

### Testing with 933

After E911 is enabled and the number is ready/active, place a test call to **933**. The 933 test call should read back the emergency address associated with the phone number. Confirm that the readback matches the correct address for the caller.

When testing, ensure the outbound call presents the Telnyx phone number that has E911 enabled. For SIP customers managing identity headers, ensure the caller ID, From, P-Asserted-Identity, or any presented calling identity resolves to the E911-enabled Telnyx number.

### Emergency Call Notifications

Telnyx recommends setting up emergency call notifications so your team can be alerted if a number places an emergency call:

1. In the Mission Control Portal, go to the account notification settings.
2. Create or select the notification channel your team monitors, such as email or webhook.
3. Enable the emergency call or E911-related notification event for that channel.
4. Save your changes.
5. Confirm separately that your notification channel works as expected.

Notification setup is separate from E911 routing. A successful notification setup does not replace the 933 test call, and a successful 933 test does not confirm that your notification channel is working.

### API or Bulk Setup

The Portal workflow is recommended for most customers. If you manage numbers programmatically or need to update multiple numbers, use the Telnyx API documentation for address validation, phone number voice settings, and bulk phone number updates:

1. Validate or create an emergency-service address.
2. Assign that emergency address to the phone number's emergency settings.
3. Confirm the number's emergency status is active before relying on the number for emergency calling.
4. For multiple numbers, use the documented bulk phone number update workflow.

### Dynamic E911

Dynamic E911 is different from regular per-number E911. Use Dynamic E911 when the emergency location must be supplied dynamically, such as for nomadic users, mobile applications, MLTS environments, WebRTC applications, wearables, or IoT devices.

Dynamic E911 may require pre-provisioned dynamic emergency addresses or location information supplied during the emergency call. This is an advanced workflow and should not be mixed with the regular per-number setup unless your application is designed for it.

If you are unsure whether you need regular E911 or Dynamic E911, contact [support@telnyx.com](mailto:support@telnyx.com) with your use case before going live.
