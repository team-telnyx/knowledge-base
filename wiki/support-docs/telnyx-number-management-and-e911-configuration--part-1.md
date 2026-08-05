---
title: Telnyx Number Management and E911 Configuration
summary: This page consolidates Telnyx Mission Control guidance for managing phone
  numbers, configuring E911 emergency services, registering emergency addresses, testing
  emergency calling, and using bulk edit tools for voice, messaging, tags, and emergency
  settings.
sources:
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
- url: https://support.telnyx.com/en/articles/2807846-bulk-edit-numbers-voice-settings
- url: https://support.telnyx.com/en/articles/2807910-bulk-edit-numbers-assigning-tags
- url: https://support.telnyx.com/en/articles/2819213-bulk-edit-numbers-emergency-services
- url: https://support.telnyx.com/en/articles/2819236-bulk-edit-numbers-delete-numbers
- url: https://support.telnyx.com/en/articles/2819238-bulk-edit-numbers-messaging-profile
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
- url: https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide
- url: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa
updated_at: 2026-08-05T13:30:13Z
---

# Telnyx Number Management and E911 Configuration

*Part 1 of 4 — see also: [Part 2](telnyx-number-management-and-e911-configuration--part-2.md), [Part 3](telnyx-number-management-and-e911-configuration--part-3.md), [Part 4](telnyx-number-management-and-e911-configuration--part-4.md)*

This page consolidates Telnyx Mission Control guidance for managing phone numbers, configuring E911 emergency services, registering emergency addresses, testing emergency calling, and using bulk edit tools for voice, messaging, tags, and emergency settings.

## Overview

Telnyx Mission Control provides a centralized portal for procuring, configuring, and managing phone numbers. The [My Numbers Page](my-numbers-page.md) lists all procured numbers and exposes per-number settings, filters, bulk edit actions, and CSV export. From this page you can configure routing, billing, voice features, messaging profiles, tags, and emergency services for individual numbers or in bulk.

## Registering E911 Addresses

Before enabling emergency services on a number, you must register an emergency service address. In the portal, navigate to **Real-Time Communications → Numbers → My Numbers → Emergency Address**, then click **Add Address**. The address form accepts a first name, last name, or business name, and either an autocomplete address search or manual entry of country, state/province/region, city, ZIP/postal code, street address, and extended address.

The [Addresses Overview](addresses-overview.md) section of the portal stores addresses used both for E911 emergency services and for number ordering regulatory requirements. From **Numbers → Compliance → Emergency Addresses**, you can add, filter, and delete addresses. Deleting an address that is associated with a DID for E911 will render that DID non-viable for E911.

> **NOTE:** Failure to register an address and enable emergency services on numbers that make emergency calls is considered unregistered and incurs a $100 penalty per call.

## Enabling E911 on a Phone Number

The [E911 Setup Guide](e911-setup-guide.md) walks through enabling regular per-number E911 in the Mission Control Portal. Regular E911 links one emergency service address to one Telnyx phone number. If your application needs to send a caller's location dynamically, review the Dynamic E911 section before using this setup.

### Regular E911 vs. Dynamic E911

| Setup type | Use this when | How is the location provided |
| --- | --- | --- |
| Regular per-number E911 | A Telnyx phone number should always route emergency calls using one fixed service address. | You assign an emergency address directly to the phone number in the Portal. |
| Dynamic E911 | The caller's location can change, such as nomadic, mobile, MLTS, WebRTC, IoT, or application-managed location use cases. | Location is provided dynamically through a separate Dynamic E911 workflow. |

Most customers with a fixed address should use the regular per-number E911 setup.

### Before you begin

Make sure you have:

- A Telnyx phone number in your account.
- The full emergency service address for that number.
- Any suite, unit, floor, or room information that helps emergency responders locate the caller.
- Permission to accept the monthly emergency services charge shown in the Portal.

Do not use 911 to test emergency service. Use 933 after E911 is enabled and the number is ready.

### Enable E911 for a Telnyx phone number

1. Sign in to the Telnyx Mission Control Portal.
2. Go to **Phone Numbers** and select the phone number you want to configure.
3. Open the number's **Emergency** or **E911** settings. In some Portal views, this may appear as an ambulance icon on the number.
4. Turn on emergency services for the number.
5. Select an existing emergency address, or choose **New Address** to add one.
6. Enter the emergency service address carefully. Include suite, unit, floor, room, or other location details when applicable. If the Portal suggests or normalises the address, review the suggested version and use it if it is correct. If the address is rejected or cannot be saved, contact [support@telnyx.com](mailto:support@telnyx.com) and include the phone number, address, and a screenshot or exact error message.
7. Click **Save Changes**.
8. Review the monthly charge confirmation.
9. Click **Accept** to enable emergency services for the number.

After the change is saved, confirm that the Portal shows the number as ready or active for emergency service before relying on it for emergency calls. If the Portal shows a pending, failed, or error state, wait and refresh the number settings. If the status does not become ready/active, or if you are not sure whether the number is ready, contact [support@telnyx.com](mailto:support@telnyx.com) before testing or relying on emergency calling.

### Enable emergency call notifications

Telnyx recommends setting up emergency call notifications so your team can be alerted if a number places an emergency call.

1. In the Mission Control Portal, go to the account notification settings.
2. Create or select the notification channel your team monitors, such as email or webhook, depending on the options available in your account.
3. Enable the emergency call or E911-related notification event for that channel.
4. Save your changes.
5. Confirm separately that your notification channel works as expected.

Notification setup is separate from E911 routing. A successful notification setup does not replace the 933 test call, and a successful 933 test does not confirm that your notification channel is working.

### Advanced: API or bulk setup

The Portal workflow is recommended for most customers. If you manage numbers programmatically or need to update multiple numbers, use the Telnyx API documentation for address validation, phone number voice settings, and bulk phone number updates. At a high level, API users should:

1. Validate or create an emergency-service address.
2. Assign that emergency address to the phone number's emergency settings.
3. Confirm the number's emergency status is active before relying on the number for emergency calling.
4. For multiple numbers, use the documented bulk phone number update workflow.

### Advanced: Dynamic E911

Dynamic E911 is different from regular per-number E911. Use Dynamic E911 when the emergency location must be supplied dynamically, such as for nomadic users, mobile applications, MLTS environments, WebRTC applications, wearables, or IoT devices. Dynamic E911 may require pre-provisioned dynamic emergency addresses or location information supplied during the emergency call. This is an advanced workflow and should not be mixed with the regular per-number setup unless your application is designed for it. If you are unsure whether you need regular E911 or Dynamic E911, contact [support@telnyx.com](mailto:support@telnyx.com) with your use case before going live.
