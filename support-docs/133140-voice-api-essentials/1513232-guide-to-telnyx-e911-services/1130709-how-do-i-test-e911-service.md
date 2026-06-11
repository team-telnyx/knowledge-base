---
source_url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
scraped: 2026-06-11
---

How do I test E911 service? | Telnyx Help Center

[Skip to main content](#main-content)

# How do I test E911 service?

Do you need to test e911 services with Telnyx. It's easy, just follow these simple instructions.

Written by Telnyx Sales

Updated over 3 weeks ago

Table of contents

**Please note: Not registering an address or enabling emergency services for numbers used for emergency calls will result in those calls being considered unregistered, incurring a $100 penalty.**

# How do I test E911 service?

Use `933` to test that your Telnyx E911 configuration is returning the expected emergency address. `933` is the routine test path for E911 validation in the United States and Canada.

Do not place live `911` calls for routine testing. Live emergency calls should only be placed for an actual emergency or when you have been specifically instructed to do so by the appropriate authority or by Telnyx Support.

*Important*: Calls to `911` from a number that does not have emergency services enabled, does not have a registered emergency address, or does not present a valid E911-enabled caller ID may be treated as unregistered emergency calls and may incur an unregistered-call charge.

---

## Before you test

Before dialing `933`, confirm the following in your Telnyx account and calling platform:

1. **Emergency services are enabled** on the Telnyx number you want to test.
2. **An emergency address is saved** for that number.
3. **You are testing from the correct Telnyx number.** The caller ID presented to Telnyx must be the Telnyx number with E911 enabled.
4. **Your phone system routes `933` to Telnyx.** If you use a PBX, SBC, UCaaS platform, or Microsoft Teams Direct Routing, make sure `933` is not being routed to another provider or blocked by your platform.

If you cannot enable emergency services, save the address, or route the test call correctly, contact [`support@telnyx.com`](mailto:support@telnyx.com) before placing emergency calls.

## Test regular per-number E911 with 933

Use this section if your Telnyx number has a fixed emergency address assigned to it in the Telnyx Portal.

1. From the device, PBX, or SIP endpoint that uses the E911-enabled Telnyx number, dial `933`.
2. Listen to the automated readback.
3. Confirm that the address read back matches the emergency address you registered for that Telnyx number.
4. If the address is incorrect, update the emergency address in the Telnyx Portal and test again after the change is saved.

A successful `933` test confirms the address associated with the test call. It does not dispatch emergency services.

## Caller ID requirements

For E911 and `933` testing, the caller ID presented to Telnyx must be the Telnyx number that has E911 enabled.

For SIP customers, this means your outbound call should present the E911-enabled number in a valid `+E.164` format, including the leading `+` and country code.

Example:

```
+12345678901
```

If your system sends the same number without the `+` and country code, Telnyx may not be able to match the call to the registered emergency address.

If you manage SIP headers directly, confirm that the SIP identity/caller ID your equipment sends to Telnyx contains the E911-enabled Telnyx number in `+E.164` format. If you are not sure which header your platform uses, check your PBX/SBC configuration or contact [`support@telnyx.com`](mailto:support@telnyx.com) with a recent failed `933` test example.

## If you use a PBX, SBC, UCaaS platform, or Microsoft Teams Direct Routing

Some calling platforms control caller ID, emergency routing, and location behavior before the call reaches Telnyx. Before testing:

* Confirm `933` and `911` are intentionally routed to Telnyx when Telnyx is your emergency provider for that number.
* Confirm the platform presents the Telnyx number with E911 enabled as the caller ID.
* Confirm any platform-specific emergency location settings are configured before placing test calls.
* For MLTS or multi-location deployments, confirm your internal emergency calling and notification obligations are handled in your own system configuration.

If `933` does not reach Telnyx or reads back an unexpected address, review the platform routing/caller ID settings first, then contact Telnyx Support if the issue continues.

## Advanced: testing Dynamic E911 or location-based E911

Regular per-number E911 and Dynamic E911 are different workflows.

* **Regular per-number E911** assigns a fixed emergency address to a Telnyx number.
* **Dynamic E911** is used when the caller's location may change or when your application/platform sends location information dynamically, such as for nomadic, mobile, WebRTC, IoT, or MLTS use cases.

If you use Dynamic E911, do not rely only on the regular per-number checks above.

Before testing with `933`, confirm that your Dynamic E911 configuration is active and that your application is sending the required dynamic location information for the call.

For Dynamic E911 testing:

1. Confirm the dynamic emergency address or endpoint is fully configured and active.
2. Confirm that your application or SIP platform sends the expected dynamic location information for the call.
3. Dial `933` through the same call path that will be used for emergency calls.
4. Confirm the readback matches the expected dynamic location for that test.

If the call completes but the location is wrong, treat the test as failed. Correct the location configuration before relying on that call path for emergency calling.

For implementation details, see Telnyx's Dynamic E911 developer documentation: [`https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911`](https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911).

## Limitations

* `933` testing is available for the United States and Canada E911 testing.
* For international emergency service availability and testing options, contact Telnyx Support or review Telnyx's supported emergency numbers guidance.
* During a `933` test, the service is primarily confirming the emergency address associated with the call. A `933` test is not the same as a live `911` call.

## Need help?

Contact [`support@telnyx.com`](mailto:support@telnyx.com) and include:

* The Telnyx number you tested.
* The date and time of the `933` test, including the timezone.
* The caller ID your system presented to Telnyx.
* The address you expected to hear.
* The address or message that was actually read back.
* Any relevant PBX/SBC/UCaaS routing details.

---

Related Articles

[E911 Setup Guide](https://support.telnyx.com/en/articles/1130683-e911-setup-guide)[Grandstream UMC6202: Auth Setup](https://support.telnyx.com/en/articles/1295514-grandstream-umc6202-auth-setup)[Grandstream: IP Auth Setup](https://support.telnyx.com/en/articles/2950523-grandstream-ip-auth-setup)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[Dialing Emergency Services](https://support.telnyx.com/en/articles/8712528-dialing-emergency-services)

Did this answer your question?

😞😐😃

Table of contents
