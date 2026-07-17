---
title: Telnyx DID Numbers
summary: This page covers Telnyx's DID (Direct Inward Dial) number offerings, including
  domestic long-code, toll-free, and international number types, along with guidance
  on purchasing, requesting unavailable numbers, and finding GB numbers on the portal.
  It also explains how to bulk edit number settings (voice, tags, emergency services,
  messaging profile, and deletion) in Mission Control, and provides reference tables
  for US N11 codes, international toll-free prefixes, and supported emergency numbers
  by country, including dialing rules and address registration requirements.
sources:
- url: https://support.telnyx.com/en/articles/1130699-did-numbers-that-telnyx-offers
- url: https://support.telnyx.com/en/articles/1130702-where-can-i-buy-dids-in-the-us-canada
- url: https://support.telnyx.com/en/articles/1130703-can-i-call-toll-free-with-my-telnyx-number
- url: https://support.telnyx.com/en/articles/1130704-what-is-a-did
- url: https://support.telnyx.com/en/articles/1458084-global-number-types
- url: https://support.telnyx.com/en/articles/2807846-bulk-edit-numbers-voice-settings
- url: https://support.telnyx.com/en/articles/2807910-bulk-edit-numbers-assigning-tags
- url: https://support.telnyx.com/en/articles/2819213-bulk-edit-numbers-emergency-services
- url: https://support.telnyx.com/en/articles/2819236-bulk-edit-numbers-delete-numbers
- url: https://support.telnyx.com/en/articles/2819238-bulk-edit-numbers-messaging-profile
- url: https://support.telnyx.com/en/articles/3562148-requesting-numbers
- url: https://support.telnyx.com/en/articles/4567969-united-states-n11-codes
- url: https://support.telnyx.com/en/articles/5820047-find-gb-numbers-on-telnyx-portal
- url: https://support.telnyx.com/en/articles/8712528-dialing-emergency-services
- url: https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers
updated_at: 2026-07-17T09:06:28Z
---

# Telnyx DID Numbers

*Part 2 of 3 — see also: [Part 1](telnyx-did-numbers--part-1.md), [Part 3](telnyx-did-numbers--part-3.md)*

This page covers Telnyx's DID (Direct Inward Dial) number offerings, including domestic long-code, toll-free, and international number types, along with guidance on purchasing, requesting unavailable numbers, and finding GB numbers on the portal. It also explains how to bulk edit number settings (voice, tags, emergency services, messaging profile, and deletion) in Mission Control, and provides reference tables for US N11 codes, international toll-free prefixes, and supported emergency numbers by country, including dialing rules and address registration requirements.

## Requesting Numbers Not Available in the Portal

If no phone number results are returned from a search request, an Advanced Order can be submitted directly from the account. Telnyx also offers contiguous blocks in increments of 10, 25, 50, and 100.

When clicking "Request Number," a form appears to specify the phone numbers desired. The Number Operations team uses these details to acquire the numbers on the customer's behalf. Each Advanced Order has a unique ID for tracking and can be viewed via the portal or the Advanced Order API.

The Number Operations team reviews requests within 3-5 business days. Requests are best effort, and Telnyx cannot guarantee fulfillment. If the team can fulfill the request, a number order is placed on the account. If regulatory requirements apply, the order remains in a "pending" state until the required information is provided.

### FAQ

**Q: I want to receive notifications for my advanced orders. Is that possible?**

A: Yes. Webhook and/or email notifications can be set up for advanced order events. See the developer guide's "Notifications" section and the notification settings support article for details.

**Q: Why am I being asked for regulatory requirements? How do I provide those?**

A: In some cases, the Number Operations team needs regulatory requirements in advance to secure the requested phone numbers. To provide them: (1) create a requirement group for the phone numbers being requested, (2) fill in the requirement group, and (3) update the Advanced Order with that requirement group.

## Bulk Editing Numbers in Mission Control

Telnyx Mission Control allows bulk editing of number settings. The general workflow is:

1. Log in to Mission Control and click **NUMBERS** on the top left.
2. Click the **MY NUMBERS** tab.
3. Select numbers using the checkboxes in front of each number.
4. Optionally, select all numbers on the page using the checkbox above the top number. The row count can be expanded to display 10-100 numbers per page.
5. Click the **Bulk Actions** dropdown and select the desired edit option.

### Bulk Edit Voice Settings

After selecting numbers and choosing **Edit Voice Settings** from the Bulk Actions dropdown, a **Bulk Edit Voice Settings** window opens with the following tabs:

- **Routing/Billing:** Configure SIP Connections/Applications, Billing Group, and Voice Billing Method (Channel Billing or Pay-per-minute Billing).
- **CNAM:** Enable/disable CNAM listing and CNAM caller ID lookup.
- **Forwarding:** Set call forwarding (On-Failure/Always) for inbound calls.
- **Recording:** Set call recording (On-Failure/Always) for inbound calls.
- **Voicemail:** Toggle voicemail and set a PIN.
- **Expert Config:** Enable Translated Number, Tech Prefix, T.38 FAX gateway, Accept any RTP Packets, and RTP Auto Adjust settings.

### Bulk Edit Tags

After selecting numbers and choosing **Edit Tags** from the Bulk Actions dropdown, a window appears to select an existing tag or create a new tag (e.g., "test-tag"). Tags can also be removed in bulk by entering the tag name to remove.

### Bulk Edit Emergency Services

**NOTE:** Failure to register an address and enable emergency services on numbers that make emergency calls is considered unregistered and incurs a $100 penalty.

After selecting numbers and choosing **Edit Emergency Settings** from the Bulk Actions dropdown, a window opens to choose **Enable All**, **Disable All**, or **Unchanged** for emergency settings status. When choosing **Enable All**, an existing saved address can be selected or a new address added via the "New Address" button.

### Bulk Edit Messaging Profile

After selecting numbers and choosing **Edit Messaging Profile** from the Bulk Actions dropdown, a window opens to select the desired messaging profile from a dropdown menu. Upon selection, a message regarding the MRC charge for assigning a messaging profile to a number is displayed. The charges must be accepted before saving.

### Bulk Delete Numbers

After selecting numbers and choosing **Delete Numbers** from the Bulk Actions dropdown, a window opens displaying the numbers to be deleted. Clicking the red **Delete Numbers** button permanently deletes the numbers from the account.

**Note:** This is an irreversible action. If numbers are deleted from the portal and recovery is desired, they can be repurchased within 15 days from the deletion date. After this period, the number becomes available in the number pool for others to purchase.

## US N11 Codes

N11 codes provide three-digit dialing access to special services. In the United States, the FCC administers N11 codes and recognizes 211, 311, 511, 711, 811, and 911 as nationally assigned.

| N11 Code | Description | Supported |
| --- | --- | --- |
| 211 | Community Information and Referral Services | No |
| 311 | Non-Emergency Police and Other Governmental Services | No |
| 411 | Local Directory Assistance | No |
| 511 | Traffic and Transportation Information (US); Provision of Weather and Traveller Information Services (Canada) | No |
| 611 | Repair Service |  |
| 711 | Telecommunications Relay Service (TRS) | Yes |
| 811 | Access to One Call Services to Protect Pipeline and Utilities from Excavation Damage (US) | Yes |
| 911 | Emergency | Yes |
| 988 (call and text) | National Suicide Prevention Lifeline | Yes |

For N11 outbound calls, no caller ID (CLI) validations are enforced. However, for 911, if an invalid CLI or a CLI without an emergency address is used, the call is classified as unregistered at a cost of $100 per call.

## Dialing Emergency Services

Telnyx offers PSTN replacement for several countries, including the ability to dial emergency services in each of those countries. The complete global coverage is available on the Telnyx website.

### Determining the Country for Emergency Dialing

Telnyx uses the caller ID of each call to determine which country's emergency number to dial. For example, dialing 911 with a Canadian caller ID sends the call to Canada, while dialing 911 with a Mexican caller ID sends the call to Mexico. This allows a single connection to be set up with numbers from different countries while still being able to dial each country's emergency services.

The "Localization Settings" in the outbound section of SIP connection settings do not affect dialing into Emergency Services; they are only used for normal local calling.

### Number Format for Emergency Dialing

Emergency service numbers are local numbers not available for international dialing and do not support +E.164 or E.164 international formats. Always dial the local emergency number by itself without a + sign or country code. Dialing +1911 or 1911 will fail with an invalid number error; the proper way is to dial just 911. A tech prefix can be used so long as nothing else is included (e.g., with tech prefix 1234, dial 1234911).

### Registering an Emergency Address

In some countries, calling emergency services from a number without a registered Emergency Service Address can result in fines. In the US, the fine is $100 per call. Ensure an address is registered for Emergency Services on all numbers used to dial Emergency Services. Per regulation, calls to Emergency Services are always allowed regardless of whether the caller ID has a registered address. For security reasons, dialing to Emergency Numbers cannot be disabled.
