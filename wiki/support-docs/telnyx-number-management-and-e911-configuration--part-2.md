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

*Part 2 of 4 — see also: [Part 1](telnyx-number-management-and-e911-configuration--part-1.md), [Part 3](telnyx-number-management-and-e911-configuration--part-3.md), [Part 4](telnyx-number-management-and-e911-configuration--part-4.md)*

This page consolidates Telnyx Mission Control guidance for managing phone numbers, configuring E911 emergency services, registering emergency addresses, testing emergency calling, and using bulk edit tools for voice, messaging, tags, and emergency settings.

## Testing E911 with 933

The [How do I test E911 service?](how-do-i-test-e911-service.md) article describes how to validate E911 configuration. Use `933` to test that your Telnyx E911 configuration is returning the expected emergency address. `933` is the routine test path for E911 validation in the United States and Canada.

Do not place live `911` calls for routine testing. Live emergency calls should only be placed for an actual emergency or when you have been specifically instructed to do so by the appropriate authority or by Telnyx Support.

> **Important:** Calls to `911` from a number that does not have emergency services enabled, does not have a registered emergency address, or does not present a valid E911-enabled caller ID may be treated as unregistered emergency calls and may incur an unregistered-call charge.

### Before you test

Before dialing `933`, confirm the following in your Telnyx account and calling platform:

1. **Emergency services are enabled** on the Telnyx number you want to test.
2. **An emergency address is saved** for that number.
3. **You are testing from the correct Telnyx number.** The caller ID presented to Telnyx must be the Telnyx number with E911 enabled.
4. **Your phone system routes `933` to Telnyx.** If you use a PBX, SBC, UCaaS platform, or Microsoft Teams Direct Routing, make sure `933` is not being routed to another provider or blocked by your platform.

If you cannot enable emergency services, save the address, or route the test call correctly, contact [support@telnyx.com](mailto:support@telnyx.com) before placing emergency calls.

### Test regular per-number E911 with 933

1. From the device, PBX, or SIP endpoint that uses the E911-enabled Telnyx number, dial `933`.
2. Listen to the automated readback.
3. Confirm that the address read back matches the emergency address you registered for that Telnyx number.
4. If the address is incorrect, update the emergency address in the Telnyx Portal and test again after the change is saved.

A successful `933` test confirms the address associated with the test call. It does not dispatch emergency services.

### Caller ID requirements

For E911 and `933` testing, the caller ID presented to Telnyx must be the Telnyx number that has E911 enabled. For SIP customers, this means your outbound call should present the E911-enabled number in a valid `+E.164` format, including the leading `+` and country code.

Example:

```
+12345678901
```

If your system sends the same number without the `+` and country code, Telnyx may not be able to match the call to the registered emergency address. If you manage SIP headers directly, confirm that the SIP identity/caller ID your equipment sends to Telnyx contains the E911-enabled Telnyx number in `+E.164` format. If you are not sure which header your platform uses, check your PBX/SBC configuration or contact [support@telnyx.com](mailto:support@telnyx.com) with a recent failed `933` test example.

### PBX, SBC, UCaaS, and Microsoft Teams Direct Routing

Some calling platforms control caller ID, emergency routing, and location behavior before the call reaches Telnyx. Before testing:

- Confirm `933` and `911` are intentionally routed to Telnyx when Telnyx is your emergency provider for that number.
- Confirm the platform presents the Telnyx number with E911 enabled as the caller ID.
- Confirm any platform-specific emergency location settings are configured before placing test calls.
- For MLTS or multi-location deployments, confirm your internal emergency calling and notification obligations are handled in your own system configuration.

If `933` does not reach Telnyx or reads back an unexpected address, review the platform routing/caller ID settings first, then contact Telnyx Support if the issue continues.

### Advanced: testing Dynamic E911 or location-based E911

Regular per-number E911 and Dynamic E911 are different workflows. If you use Dynamic E911, do not rely only on the regular per-number checks above. Before testing with `933`, confirm that your Dynamic E911 configuration is active and that your application is sending the required dynamic location information for the call.

For Dynamic E911 testing:

1. Confirm the dynamic emergency address or endpoint is fully configured and active.
2. Confirm that your application or SIP platform sends the expected dynamic location information for the call.
3. Dial `933` through the same call path that will be used for emergency calls.
4. Confirm the readback matches the expected dynamic location for that test.

If the call completes but the location is wrong, treat the test as failed. Correct the location configuration before relying on that call path for emergency calling. For implementation details, see Telnyx's [Dynamic E911 developer documentation](https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911).

### Limitations

- `933` testing is available for the United States and Canada E911 testing.
- For international emergency service availability and testing options, contact Telnyx Support or review Telnyx's supported emergency numbers guidance.
- During a `933` test, the service is primarily confirming the emergency address associated with the call. A `933` test is not the same as a live `911` call.
