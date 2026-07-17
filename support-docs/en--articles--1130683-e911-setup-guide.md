---
source_url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
title: "E911 Setup Guide"
description: "In this article we will explain how to setup E911 with the Telnyx Mission Control Portal. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 34094d20e6df8cd15d9cfe7115423459a3a9ff299acc13726a6a90be64c4fd37
---







# E911 Setup Guide

In this article we will explain how to setup E911 with the Telnyx Mission Control Portal. See Telnyx guidance and requirements.




## E911 Setup Guide

This guide explains how to enable regular E911 service for a Telnyx phone number in the Mission Control Portal.

Regular E911 links one emergency service address to one Telnyx phone number. If your application needs to send a caller's location dynamically, review the Dynamic E911 section before using this setup.

## Regular E911 vs. Dynamic E911

|  |  |  |
| --- | --- | --- |
| Setup type | Use this when | How is the location provided |
| Regular per-number E911 | A Telnyx phone number should always route emergency calls using one fixed service address. | You assign an emergency address directly to the phone number in the Portal. |
| Dynamic E911 | The caller's location can change, such as nomadic, mobile, MLTS, WebRTC, IoT, or application-managed location use cases. | Location is provided dynamically through a separate Dynamic E911 workflow. |

Most customers with a fixed address should use the regular per-number E911 setup below.

## Before you begin

Make sure you have:

* A Telnyx phone number in your account.
* The full emergency service address for that number.
* Any suite, unit, floor, or room information that helps emergency responders locate the caller.
* Permission to accept the monthly emergency services charge shown in the Portal.

Do not use 911 to test emergency service. Use 933 after E911 is enabled and the number is ready.

## Enable E911 for a Telnyx phone number

1. Sign in to the Telnyx Mission Control Portal.
2. Go to **Phone Numbers** and select the phone number you want to configure.
3. Open the number's **Emergency** or **E911** settings.

   * In some Portal views, this may appear as an ambulance icon on the number.
4. Turn on emergency services for the number.
5. Select an existing emergency address, or choose **New Address** to add one.
6. Enter the emergency service address carefully.

   * Include suite, unit, floor, room, or other location details when applicable.
   * If the Portal suggests or normalises the address, review the suggested version and use it if it is correct.
   * If the address is rejected or cannot be saved, contact [support@telnyx.com](mailto:support@telnyx.com) and include the phone number, address, and a screenshot or exact error message.
7. Click **Save Changes**.
8. Review the monthly charge confirmation.
9. Click **Accept** to enable emergency services for the number.

After the change is saved, confirm that the Portal shows the number as ready or active for emergency service before relying on it for emergency calls.

If the Portal shows a pending, failed, or error state, wait and refresh the number settings. If the status does not become ready/active, or if you are not sure whether the number is ready, contact [support@telnyx.com](mailto:support@telnyx.com) before testing or relying on emergency calling.

## Test with 933

After E911 is enabled and the number is ready/active, place a test call to **933**.

The 933 test call should read back the emergency address associated with the phone number. Confirm that the readback matches the correct address for the caller.

When testing, make sure the outbound call presents the Telnyx phone number that has E911 enabled.

Advanced SIP note: if you manage SIP identity headers, ensure the caller ID, From, P-Asserted-Identity, or any presented calling identity resolves to the E911-enabled Telnyx number.

## Enable emergency call notifications

Telnyx recommends setting up emergency call notifications, so your team can be alerted if a number places an emergency call.

1. In the Mission Control Portal, go to the account notification settings.
2. Create or select the notification channel your team monitors, such as email or webhook, depending on the options available in your account.
3. Enable the emergency call or E911-related notification event for that channel.
4. Save your changes.
5. Confirm separately that your notification channel works as expected.

Notification setup is separate from E911 routing. A successful notification setup does not replace the 933 test call, and a successful 933 test does not confirm that your notification channel is working.

## Advanced: API or bulk setup

The Portal workflow is recommended for most customers.

If you manage numbers programmatically or need to update multiple numbers, use the Telnyx API documentation for address validation, phone number voice settings, and bulk phone number updates. At a high level, API users should:

1. Validate or create an emergency-service address.
2. Assign that emergency address to the phone number's emergency settings.
3. Confirm the number's emergency status is active before relying on the number for emergency calling.
4. For multiple numbers, use the documented bulk phone number update workflow.

## Advanced: Dynamic E911

Dynamic E911 is different from regular per-number E911.

Use Dynamic E911 when the emergency location must be supplied dynamically, such as for nomadic users, mobile applications, MLTS environments, WebRTC applications, wearables, or IoT devices.

Dynamic E911 may require pre-provisioned dynamic emergency addresses or location information supplied during the emergency call. This is an advanced workflow and should not be mixed with the regular per-number setup unless your application is designed for it.

If you are unsure whether you need regular E911 or Dynamic E911, contact [support@telnyx.com](mailto:support@telnyx.com) with your use case before going live.

## If activation gets complicated

Contact [support@telnyx.com](mailto:support@telnyx.com) if:

* The Portal rejects the emergency address.
* The number remains pending or does not show as ready/active.
* The 933 readback is incorrect.
* The call does not present the E911-enabled Telnyx number.
* You are configuring Dynamic E911, MLTS, WebRTC, mobile, IoT, or another advanced emergency-calling workflow.

Include the Telnyx phone number, the emergency service address, the approximate time of the test or attempted setup, and any screenshot or exact error message from the Portal.

---

Related Articles

[Configuring Grandstream GXP16XX with Telnyx](https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx)[How do I test E911 service?](https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service)[2FA / TOTP Setup](https://support.telnyx.com/en/articles/3739748-2fa-totp-setup)[My Numbers Page](https://support.telnyx.com/en/articles/4349113-my-numbers-page)[Grandstream HT802: Telnyx Setup](https://support.telnyx.com/en/articles/5725071-grandstream-ht802-telnyx-setup)

Did this answer your question?

😞😐😃
