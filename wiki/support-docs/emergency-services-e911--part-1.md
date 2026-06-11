---
title: Emergency Services (E911)
summary: Covers how to register emergency addresses, enable and test E911 on Telnyx
  numbers, dial emergency services globally, and handle advanced scenarios like Dynamic
  E911 and Microsoft Teams integration.
sources:
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/2819213-bulk-edit-numbers-emergency-services
- url: https://support.telnyx.com/en/articles/8712528-dialing-emergency-services
- url: https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers
- url: https://support.telnyx.com/en/articles/9039036-emergency-services-and-ipnd-in-australia
- url: https://support.telnyx.com/en/articles/9718403-microsoft-teams-emergency-call-routing
updated_at: 2026-06-11T11:37:16Z
---

# Emergency Services (E911)

*Part 1 of 2 — see also: [Part 2](emergency-services-e911--part-2.md)*

Covers how to register emergency addresses, enable and test E911 on Telnyx numbers, dial emergency services globally, and handle advanced scenarios like Dynamic E911 and Microsoft Teams integration.

## Regular E911 vs. Dynamic E911

| Setup type | Use this when | How the location is provided |
|---|---|---|
| Regular per-number E911 | A Telnyx phone number should always route emergency calls using one fixed service address. | You assign an emergency address directly to the phone number in the Portal. |
| Dynamic E911 | The caller's location can change — nomadic, mobile, MLTS, WebRTC, IoT, or application-managed location use cases. | Location is provided dynamically through a separate Dynamic E911 workflow. |

Most customers with a fixed address should use regular per-number E911. Dynamic E911 should not be mixed with the regular per-number setup unless your application is specifically designed for it.

## Register Emergency Addresses

1. In the Telnyx Mission Control Portal, go to **Real-Time Communications → Numbers → My Numbers**.
2. Click the **Emergency Address** sub-tab.
3. Click **Add Address**.
4. Fill out the form:
   - First Name, Last Name, or Business Name.
   - You can auto-search for the address by typing in the "search for an address" field.
   - Or manually enter: Country, State/Province/Region, City, ZIP/Postal Code, Street Address, and Extended Address.
5. Save the address.

> **Warning:** Failure to register an address and enable emergency services on numbers that make emergency calls will result in those calls being considered unregistered, incurring a penalty of **$100 per call** (US). Other countries may also impose fines.

## Enable E911 for a Phone Number

### Prerequisites

- A Telnyx phone number in your account.
- The full emergency service address for that number.
- Any suite, unit, floor, or room information that helps emergency responders locate the caller.
- Permission to accept the monthly emergency services charge shown in the Portal.

### Steps

1. Sign in to the Mission Control Portal.
2. Go to **Phone Numbers** and select the number to configure.
3. Open the number's **Emergency** or **E911** settings (may appear as an ambulance icon).
4. Turn on emergency services.
5. Select an existing emergency address or choose **New Address** to add one.
6. Enter the address carefully, including suite/unit/floor/room details. If the Portal suggests a normalised version, review it and use it if correct.
7. Click **Save Changes**.
8. Review the monthly charge confirmation and click **Accept**.

After saving, confirm that the Portal shows the number as **ready** or **active** for emergency service. If the status is pending, failed, or in error, wait and refresh. If it does not resolve, contact [support@telnyx.com](mailto:support@telnyx.com) before relying on the number for emergency calls.

### If the address is rejected

If the address cannot be saved, contact [support@telnyx.com](mailto:support@telnyx.com) and include the phone number, address, and a screenshot or exact error message.

## Bulk Edit Emergency Settings

To assign an emergency address to multiple numbers at once:

1. Go to **Numbers → My Numbers** in the Portal.
2. Select numbers using the checkboxes. You can select all numbers on the page using the top checkbox.
3. Expand the row count (10–100) to display more numbers per page.
4. Open the **Bulk Actions** dropdown and select **Edit Emergency Settings**.
5. Choose **Enable All**, **Disable All**, or **Unchanged** for the emergency settings status.
6. If enabling, select an existing address or click **New Address** to add one.
7. Save. Emergency service will be enabled for all selected numbers.

## Test E911 with 933

Do **not** place live 911 calls for routine testing. Use **933**, the E911 address-verification test number for the United States and Canada.

### Before testing

Confirm the following:

1. Emergency services are **enabled** on the Telnyx number.
2. An emergency address is **saved** for that number.
3. You are calling from the correct Telnyx number — the caller ID presented to Telnyx must be the E911-enabled number.
4. Your phone system routes 933 to Telnyx (not to another provider or blocked by your PBX/SBC/UCaaS platform).

### Test procedure

1. From the device or SIP endpoint using the E911-enabled number, dial **933**.
2. Listen to the automated readback.
3. Confirm the address read back matches the registered emergency address.
4. If incorrect, update the address in the Portal and re-test after saving.

A successful 933 test confirms the address associated with the call. It does **not** dispatch emergency services.

### Caller ID requirements

- The caller ID presented to Telnyx must be the E911-enabled Telnyx number in valid **+E.164** format (e.g., `+12345678901`), including the leading `+` and country code.
- For SIP customers, ensure the SIP identity/caller ID (From, P-Asserted-Identity, etc.) contains the E911-enabled number in +E.164 format.
- If your system sends the number without the `+` and country code, Telnyx may not match the call to the registered emergency address.

### PBX / SBC / UCaaS / Microsoft Teams Direct Routing

Before testing, confirm:

- 933 and 911 are intentionally routed to Telnyx when Telnyx is your emergency provider.
- The platform presents the E911-enabled Telnyx number as the caller ID.
- Any platform-specific emergency location settings are configured.
- For MLTS or multi-location deployments, confirm your internal emergency-calling and notification obligations are handled in your own system.

## Enable Emergency Call Notifications

Telnyx recommends setting up notifications so your team is alerted when a number places an emergency call:

1. Go to account notification settings in the Mission Control Portal.
2. Create or select a notification channel (email, webhook, etc.).
3. Enable the emergency call or E911 notification event for that channel.
4. Save your changes.
5. Confirm separately that the notification channel works as expected.

Notification setup is independent of E911 routing. A successful notification setup does not replace the 933 test, and a successful 933 test does not confirm your notification channel is working.

## Dialing Emergency Services

### Country routing

Telnyx uses the **caller ID** of each call to determine which country's emergency services to route to. For example, dialling 911 with a Canadian caller ID routes to Canada; dialling 911 with a Mexican caller ID routes to Mexico. The SIP connection's "Localization Settings" do **not** affect emergency-service dialling.

### Number format

Emergency numbers are local numbers that do not support +E.164 or E.164 international formats. **Always dial the local emergency number by itself without a `+` sign or country code.**

- ✅ Correct: `911`
- ❌ Incorrect: `+1911` or `1911` (these will fail with an invalid-number error)

You may use a tech prefix. For example, if your connection uses tech prefix `1234`, dial `1234911`.

### Registering an address is mandatory

In some countries, calling emergency services from a number without a registered emergency address can result in a fine (e.g., $100 per call in the US). Per regulation, Telnyx will always allow calls to emergency services regardless of whether the caller ID has a registered address. You cannot disable dialling to emergency numbers.
