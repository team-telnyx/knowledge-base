---
title: Bulk Edit Numbers in Mission Control
summary: Learn how to manage Telnyx phone numbers at scale in Mission Control, including
  bulk editing voice settings (HD Voice, routing, CNAM, forwarding, recording, voicemail,
  expert config), assigning messaging profiles and tags, updating emergency services,
  and deleting numbers, plus quick context on DIDs and HD Voice requirements.
sources:
- url: https://support.telnyx.com/en/articles/2807846-bulk-edit-numbers-voice-settings
- url: https://support.telnyx.com/en/articles/2807910-bulk-edit-numbers-assigning-tags
- url: https://support.telnyx.com/en/articles/2819213-bulk-edit-numbers-emergency-services
- url: https://support.telnyx.com/en/articles/2819236-bulk-edit-numbers-delete-numbers
- url: https://support.telnyx.com/en/articles/2819238-bulk-edit-numbers-messaging-profile
- url: https://support.telnyx.com/en/articles/1130699-did-numbers-that-telnyx-offers
- url: https://support.telnyx.com/en/articles/1130702-where-can-i-buy-dids-in-the-us-canada
- url: https://support.telnyx.com/en/articles/1130704-what-is-a-did
- url: https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature
updated_at: 2026-05-20T15:38:55Z
---

# Bulk Edit Numbers in Mission Control

Learn how to manage Telnyx phone numbers at scale in Mission Control, including bulk editing voice settings (HD Voice, routing, CNAM, forwarding, recording, voicemail, expert config), assigning messaging profiles and tags, updating emergency services, and deleting numbers, plus quick context on DIDs and HD Voice requirements.

## Access and select numbers
- Go to Mission Control > Numbers. Open My Numbers (Manage Numbers).
- Select numbers via checkboxes. Use the header checkbox to select all visible on the page.
- Increase the row count (10–100) to expand selection before taking a bulk action.

## Bulk Actions overview
From the Bulk Actions menu you can:
- Edit Voice Settings
- Edit Messaging Profile
- Edit Tags
- Edit Emergency Settings
- Delete Numbers

A Bulk Edit window shows the numbers affected and the options you can change. Save to apply across all selected numbers.

## Edit Voice Settings in bulk
Within Bulk Edit Voice Settings you can set the following for all selected numbers:

### Routing & Billing
- SIP Connections / Applications: Assign one of your SIP Trunk Connections, or choose No Connection to remove an assignment.
- Billing Group: Associate or de-associate numbers with a billing group. See Billing Groups: https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups
- Voice Billing Method: Choose Channel Billing or Pay‑per‑minute Billing (billing increments). Channel Billing: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it. Increments: https://support.telnyx.com/en/articles/1130659-billing-increments

### HD Voice feature
- Toggle HD Voice for eligible numbers. To experience HD audio, ensure:
  - Calling party and called party (PSTN side) support wideband codecs and are on LTE/5G where applicable.
  - Supported carriers include: US (AT&T, T‑Mobile, Verizon), Germany (Outbox), Austria (Yuutel), Australia (all major carriers).
  - Your SIP Connection and your SIP device support OPUS, G.722, or AMR‑WB; enable these under SIP Trunking > SIP Connections > Inbound > Expert Settings.
  - The number is HD‑capable. You can search for HD numbers in Buy Numbers: https://portal.telnyx.com/#/numbers/buy-numbers
- Notes:
  - HD Voice is free (no MRC) and negotiated at call start; quality isn’t guaranteed on PSTN.
  - Many international, toll‑free, and some +1 long codes are not yet supported. A yellow banner indicates a number isn’t HD‑capable.
  - On codec mismatch, the call may transcode; HD→HD can remain HD, HD→narrowband will not be HD.
  - More details: https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature

### CNAM
- CNAM Listing: Enable/disable outbound CNAM listing.
- CNAM Caller ID Lookup: Enable/disable inbound caller ID name dips.
- Learn more: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam

### Forwarding
- Configure call forwarding target and mode (Always or On‑Failure) for all selected numbers.
- Learn more: https://support.telnyx.com/en/articles/1130657-call-forwarding

### Recording
- Enable call recording on selected numbers.
- Learn more: https://support.telnyx.com/en/articles/5377454-call-recording

### Voicemail
- Toggle voicemail and set a PIN for all selected numbers.
- Learn more: https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail

### Expert Config
- Enable options like Translated Number, Tech Prefix, T.38 FAX Gateway, Accept Any RTP Packets, RTP Auto Adjust.
- My Numbers reference: https://support.telnyx.com/en/articles/4349113-my-numbers-page

## Bulk assign a Messaging Profile
- Bulk Actions > Edit Messaging Profile. Choose a profile from the dropdown.
- Accept any message about MRC for assigning a profile, then Save to apply to all selected numbers.
- Guide: https://support.telnyx.com/en/articles/2819238-bulk-edit-numbers-messaging-profile

## Bulk assign or remove Tags
- Bulk Actions > Edit Tags. Select an existing tag or type a new tag name to create and apply in one step; Save.
- To remove, open Edit Tags, enter the tag name to remove, and Save.
- Guide: https://support.telnyx.com/en/articles/2807910-bulk-edit-numbers-assigning-tags

## Bulk edit Emergency Services
- Bulk Actions > Edit Emergency Settings.
- Choose status: Enable All, Disable All, or Unchanged.
- When enabling, pick a saved address or click New Address to add one, then Save to apply to all selected numbers.
- Important: Numbers that place emergency calls without a registered address incur a $100 penalty. Details: https://support.telnyx.com/en/articles/2819213-bulk-edit-numbers-emergency-services

## Bulk delete Numbers
- Bulk Actions > Delete Numbers. Review the list and confirm.
- This is irreversible. You may be able to repurchase deleted numbers within 15 days; after that they can return to the public pool.
- Guide: https://support.telnyx.com/en/articles/2819236-bulk-edit-numbers-delete-numbers

## About DIDs with Telnyx
- What is a DID? A virtual number (not tied to a POTS line) that becomes the phone number others use to reach you after configuration. https://support.telnyx.com/en/articles/1130704-what-is-a-did
- Types offered: US & Canada domestic, toll‑free, and international DIDs. https://support.telnyx.com/en/articles/1130699-did-numbers-that-telnyx-offers
- US/Canada coverage: Access to 15,000+ rate centers; numbers available in every US state and Canadian province. https://support.telnyx.com/en/articles/1130702-where-can-i-buy-dids-in-the-us-canada
- How to buy: Check Numbers Pricing (https://telnyx.com/pricing/numbers) and use Search & Buy Numbers in the portal: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
- International requirements: Tool: https://support.telnyx.com/en/articles/7003167-international-number-requirements-tool

## Tips and notes
- Selection scope: The header checkbox selects only numbers visible on the current page; raise the row count to include more before bulk editing.
- Messaging Profile charges: A notice appears when assigning a profile; accept to proceed.
- HD Voice: Free, codec‑dependent, and PSTN‑dependent; search for HD‑capable numbers when buying.
- Emergency Services: Always ensure addresses are registered/enabled on numbers that may dial emergency services to avoid penalties.
