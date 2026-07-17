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

*Part 4 of 6 — see also: [Part 1](telnyx-phone-numbers-ordering-e911-and-number-management--part-1.md), [Part 2](telnyx-phone-numbers-ordering-e911-and-number-management--part-2.md), [Part 3](telnyx-phone-numbers-ordering-e911-and-number-management--part-3.md), [Part 5](telnyx-phone-numbers-ordering-e911-and-number-management--part-5.md), [Part 6](telnyx-phone-numbers-ordering-e911-and-number-management--part-6.md)*

This page consolidates Telnyx guidance on phone number ordering, including account verification restrictions, searching and buying numbers, requirement groups, working with the numbering team, E911 address registration and setup, testing E911 with 933, handling spam/scam-likely flags, and managing numbers through the My Numbers Page.

## Testing E911 Service

Use **933** to test that your Telnyx E911 configuration is returning the expected emergency address. 933 is the routine test path for E911 validation in the United States and Canada.

Do not place live 911 calls for routine testing. Live emergency calls should only be placed for an actual emergency or when specifically instructed by the appropriate authority or by Telnyx Support.

**Important:** Calls to 911 from a number that does not have emergency services enabled, does not have a registered emergency address, or does not present a valid E911-enabled caller ID may be treated as unregistered emergency calls and may incur an unregistered-call charge.

### Before You Test

Before dialing 933, confirm:

1. Emergency services are enabled on the Telnyx number you want to test.
2. An emergency address is saved for that number.
3. You are testing from the correct Telnyx number. The caller ID presented to Telnyx must be the Telnyx number with E911 enabled.
4. Your phone system routes 933 to Telnyx. If you use a PBX, SBC, UCaaS platform, or Microsoft Teams Direct Routing, make sure 933 is not being routed to another provider or blocked by your platform.

If you cannot enable emergency services, save the address, or route the test call correctly, contact [support@telnyx.com](mailto:support@telnyx.com) before placing emergency calls.

### Testing Regular Per-Number E911 with 933

1. From the device, PBX, or SIP endpoint that uses the E911-enabled Telnyx number, dial 933.
2. Listen to the automated readback.
3. Confirm that the address read back matches the emergency address you registered for that Telnyx number.
4. If the address is incorrect, update the emergency address in the Telnyx Portal and test again after the change is saved.

A successful 933 test confirms the address associated with the test call. It does not dispatch emergency services.

### Caller ID Requirements

For E911 and 933 testing, the caller ID presented to Telnyx must be the Telnyx number that has E911 enabled. For SIP customers, the outbound call should present the E911-enabled number in valid `+E.164` format, including the leading `+` and country code.

Example:

```
+12345678901
```

If your system sends the same number without the `+` and country code, Telnyx may not be able to match the call to the registered emergency address.

If you manage SIP headers directly, confirm that the SIP identity/caller ID your equipment sends to Telnyx contains the E911-enabled Telnyx number in `+E.164` format. If you are unsure which header your platform uses, check your PBX/SBC configuration or contact [support@telnyx.com](mailto:support@telnyx.com) with a recent failed 933 test example.

### PBX, SBC, UCaaS, and Microsoft Teams Direct Routing

Some calling platforms control caller ID, emergency routing, and location behavior before the call reaches Telnyx. Before testing:

- Confirm 933 and 911 are intentionally routed to Telnyx when Telnyx is your emergency provider for that number.
- Confirm the platform presents the Telnyx number with E911 enabled as the caller ID.
- Confirm any platform-specific emergency location settings are configured before placing test calls.
- For MLTS or multi-location deployments, confirm your internal emergency calling and notification obligations are handled in your own system configuration.

If 933 does not reach Telnyx or reads back an unexpected address, review the platform routing/caller ID settings first, then contact Telnyx Support if the issue continues.

### Testing Dynamic E911 or Location-Based E911

Regular per-number E911 and Dynamic E911 are different workflows. Dynamic E911 is used when the caller's location may change or when your application/platform sends location information dynamically, such as for nomadic, mobile, WebRTC, IoT, or MLTS use cases.

Before testing with 933, confirm that your Dynamic E911 configuration is active and that your application is sending the required dynamic location information for the call:

1. Confirm the dynamic emergency address or endpoint is fully configured and active.
2. Confirm that your application or SIP platform sends the expected dynamic location information for the call.
3. Dial 933 through the same call path that will be used for emergency calls.
4. Confirm the readback matches the expected dynamic location for that test.

If the call completes but the location is wrong, treat the test as failed. Correct the location configuration before relying on that call path for emergency calling.

For implementation details, see the [Dynamic E911 developer documentation](https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911).

### Limitations

- 933 testing is available for the United States and Canada E911 testing.
- For international emergency service availability and testing options, contact Telnyx Support or review Telnyx's supported emergency numbers guidance.
- During a 933 test, the service is primarily confirming the emergency address associated with the call. A 933 test is not the same as a live 911 call.
