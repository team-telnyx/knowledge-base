---
title: E911 and Emergency Services with Telnyx
summary: How to register emergency addresses, enable and test E911, understand Dynamic
  E911, and place global emergency calls with Telnyx—including routing behavior, caller
  ID rules, supported codes, penalties, and Australia’s IPND requirements.
sources:
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
  content_hash: 7d21374d76b24794f1c22315d58d2dd2d7868d1bc4b41919c6931bed9b8292e8
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
  content_hash: c88cf64651660251bbb7c78d5fc2076fa6d575dc0270a71edc0f2d1b9f8aada7
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
  content_hash: 34e57629d424492a20b673d6f3d2fc4f56fd611b327d4e68d553f53c04547d4e
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
  content_hash: c0939fb1efca8761c74f918b506bdb9a47783d31999fc81ec3a577cc1c7c7db9
- url: https://support.telnyx.com/en/articles/4567969-united-states-n11-codes
  content_hash: 20c33fabf18a5c41cfc49b63290a8b2b021345fc481a9d60823f54781c5a3a08
- url: https://support.telnyx.com/en/articles/8712528-dialing-emergency-services
  content_hash: a99ff63bc88f0020ceded16ae5f0f4810ebb6a0b0142d2ffb850a568816bef0f
- url: https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers
  content_hash: cb95db9a1d4b7efd8c0e2a2a6203e548f01a093152051f6d98c1287b0cdc5f64
- url: https://support.telnyx.com/en/articles/9039036-emergency-services-and-ipnd-in-australia
  content_hash: 99dd825a73f5094d28a7f3562840fe554512529d6edad42e92b92a9a1418cb7d
updated_at: 2026-05-20T15:35:05Z
---

# E911 and Emergency Services with Telnyx

How to register emergency addresses, enable and test E911, understand Dynamic E911, and place global emergency calls with Telnyx—including routing behavior, caller ID rules, supported codes, penalties, and Australia’s IPND requirements.

## Understanding Telnyx E911 Options
- Regular (per-number) E911: link one fixed emergency service address to one Telnyx phone number. Use this for fixed-location lines.
- Dynamic E911: supply the caller’s location at call time for nomadic, mobile, MLTS, WebRTC, or IoT scenarios. Do not mix Dynamic E911 with per‑number E911 unless your application is designed for it.

## Manage and Register Emergency Addresses in the Portal
- In Mission Control, open Numbers and find the Emergency Addresses page (you can also use the direct link: https://portal.telnyx.com/#/numbers/emergency-addresses).
- Click Add Address and provide contact name or business name, then either:
  - Use Search for an address (auto-complete), or
  - Enter details manually (country, state/province/region, city, ZIP/postal code, street, extended address such as unit/suite/floor/room).
- Saved addresses appear in a list you can filter and manage. Deleting an address that’s assigned to a DID disables E911 for that DID until a new address is assigned.

Note: Calls to 911 without an enabled emergency address are treated as unregistered and may incur a $100 charge per call in the US.

## Enable E911 on a Telnyx Phone Number
1. Sign in to Mission Control.
2. Go to Phone Numbers and open the number’s settings (look for the Emergency/E911 tab or ambulance icon).
3. Enable emergency services for the number.
4. Select an existing emergency address or add a new one.
5. Carefully review/accept any normalised address suggestions.
6. Save changes and accept the monthly emergency services charge.
7. Confirm the number shows Ready/Active for emergency service before relying on it.
- If status remains pending/failed, refresh and, if needed, contact help@telnyx.com with the number, address, and any error/screenshot.

## Verify Configuration with 933 (Test Line)
- After E911 is enabled and shows Ready/Active, place a test call to 933 (US/Canada only).
- The system reads back the emergency address associated with the calling number. Confirm it matches.
- Do not place live 911 calls for routine testing.

## Caller ID and SIP Identity Requirements
- The caller ID you present to Telnyx must be the Telnyx number that has E911 enabled.
- Present the number in +E.164 format (for example, +12345678901). Omitting + and country code can prevent proper address matching.
- If you manage SIP headers, ensure the E911-enabled number is presented consistently (e.g., From, P-Asserted-Identity).

## Platform Routing Considerations (PBX, SBC, UCaaS, Teams)
- Ensure 933 and 911 route to Telnyx when Telnyx is your emergency provider.
- Confirm the platform presents the E911-enabled Telnyx number as caller ID.
- Configure any platform-specific emergency location features (especially for MLTS/multi-site) and your own internal notification/trace obligations.

## Set Up Emergency Call Notifications
- In Mission Control, configure account notifications (email, webhook, etc.) and enable the emergency-call event.
- Test your notification channel separately—notification setup does not validate E911 routing, and a successful 933 test does not validate notifications.

## Advanced Workflows: API, Bulk, and Dynamic E911
- API/bulk: validate or create the emergency address, assign it to each number’s emergency settings, then confirm each number’s emergency status is Active before relying on it.
- Dynamic E911: ensure your application supplies the dynamic location for the call. Test over the exact call path with 933 and verify the readback. Developer guide: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911

## Global Emergency Dialing Behavior and Number Format
- Telnyx determines the destination country for an emergency call by the caller ID’s country. Example: dialing 911 with a Canadian caller ID routes to Canada; with a Mexican caller ID, to Mexico.
- Always dial the local emergency code by itself (no + sign or country code). For example, dial 911, not +1911 or 1911.
- If your connection uses a tech prefix, you may prepend it (e.g., 1234911) but do not add any country code.
- Emergency dialing is permitted by regulation and cannot be disabled. However, using a caller ID without a registered emergency address can result in fines (e.g., $100 per unregistered 911 call in the US). Localization settings on your SIP connection do not affect emergency routing.

## United States N11 and Special Codes Support
- Supported through Telnyx outbound: 711 (TRS), 811 (One Call), 911 (Emergency), and 988 (call and text, Suicide & Crisis Lifeline).
- Not supported for outbound: 211, 311, 411, 511. 611 not offered as a Telnyx service.
- Caller ID validation is not enforced for most N11 outbound calls; 911 calls without a valid E911-enabled caller ID are treated as unregistered and may incur a $100 charge per call.

## Australia: 000/112 and IPND Requirements
- 000 is the primary emergency number; 112 is also supported on mobile phones. Calls to 000/112 are free and can be made even from inactive or SIM-less mobiles. For more, see http://www.triplezero.gov.au.
- IPND: Telnyx uploads your Public Number Customer Data (name, service address, phone numbers, and directory preferences) to the Integrated Public Number Database. This enables accurate emergency response and lawful access by authorised agencies.
- Keep your service address and directory preferences current—contact support@telnyx.com to view, update, or opt out of directory listings.

## Penalties, Availability, and Limitations
- Unregistered 911 calls (US) may incur a $100 fee per call. Register and enable E911 on every number that might place emergency calls.
- 933 testing is available for the US and Canada only.
- Supported emergency numbers vary by country. Review coverage before going live.

## Troubleshooting and When to Contact Telnyx Support
Contact help@telnyx.com if:
- The Portal rejects an address, or a number stays pending/not Active.
- 933 reads back the wrong address or the call presents the wrong caller ID.
- You’re implementing Dynamic E911, MLTS, WebRTC, mobile, or IoT emergency workflows.
Include: the Telnyx number, date/time/timezone of the test, presented caller ID, expected vs. actual readback, address used, platform routing details, and screenshots/error messages.

## References and Further Reading
- E911 Setup Guide: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- How to test E911 service (933): https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- Addresses overview in Mission Control: https://support.telnyx.com/en/articles/4294429-addresses-overview
- Dialing Emergency Services (global behavior and format): https://support.telnyx.com/en/articles/8712528-dialing-emergency-services
- Supported Emergency Numbers by country: https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers
- US N11 Codes support: https://support.telnyx.com/en/articles/4567969-united-states-n11-codes
- Australia IPND and 000/112: https://support.telnyx.com/en/articles/9039036-emergency-services-and-ipnd-in-australia
- Global coverage: https://telnyx.com/global-coverage
