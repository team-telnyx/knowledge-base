---
title: Phone Numbers
summary: Overview of Telnyx phone numbers (DIDs), including available types, how to
  search and buy them, ordering restrictions based on account verification, international
  regulatory requirements, bulk management features, and number lookup capabilities.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
  content_hash: 2b12431fb031e0ce8377d07af5cb4896c19f274686dde559485ddf68fea370ad
- url: https://support.telnyx.com/en/articles/1130699-did-numbers-that-telnyx-offers
  content_hash: 6c3fa052b7f722aa6a7d85430b28191328ae1a9c9fa3bcbd0f1fdaba100a73d7
- url: https://support.telnyx.com/en/articles/1130702-where-can-i-buy-dids-in-the-us-canada
  content_hash: 5f537b58f0671121a74311273fd03537b581c23be7c4070b59f8847693e3888c
- url: https://support.telnyx.com/en/articles/1130704-what-is-a-did
  content_hash: d7cbbf347a4d213b2d604221442e2e1d38e43d689ed426380502e89e1eaafbd7
- url: https://support.telnyx.com/en/articles/1458084-global-number-types
  content_hash: 01713de0bcc2647e13d83af7a73e4ec5ed60ef1abf4f0ba71f8a5d2fefbd32b9
- url: https://support.telnyx.com/en/articles/2807846-bulk-edit-numbers-voice-settings
  content_hash: b98a504cc6da362f75e210369fbe1e955d53c874d7a03404513591f83d9af33e
- url: https://support.telnyx.com/en/articles/2807910-bulk-edit-numbers-assigning-tags
  content_hash: 30c8ef6520d82960c291d68d496a68b479851405c9f528a1603fccadb9dddbba
- url: https://support.telnyx.com/en/articles/2819236-bulk-edit-numbers-delete-numbers
  content_hash: 50c189f50f7424920ccd22c5222ec9f1ead3fb76aae89d3db20d68d74d198b45
- url: https://support.telnyx.com/en/articles/2819238-bulk-edit-numbers-messaging-profile
  content_hash: 0faec558eb098fc0e94e1706122f73b7ec9c6bb653dad85b8dbd32b36fe6d746
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
  content_hash: d70c77ae1b48589d08da567802e476adc7a43b3da171defb780f06d77104c17c
- url: https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide
  content_hash: 2516c8b50adbb448ce483f24d50c78ecd1c854575cf7f6e296ba84277634bc6d
- url: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
  content_hash: c8a90fcec1908f46824705b8c99813b1a18af1753649c2f6da683b7d962235b3
- url: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa
  content_hash: 0552e57b5b449e7e6b40672fccf90122d7442a1c8c4696543bf519a84879ec9f
- url: https://support.telnyx.com/en/articles/5469551-international-numbers-required-documents
  content_hash: b0aaaa3854726cf876b16f06f82886a74ce92a65090637ab67ba8f5e9bfa5ec2
- url: https://support.telnyx.com/en/articles/7003167-international-number-requirements-tool
  content_hash: 0daa53a8a43bac3e5f5211996b4d070f7046b798f596d12af6fd867b0a881fab
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
  content_hash: 91855e0ac86571e697084954333bff7475e2192e26f1050785f296d9cd6aa566
updated_at: 2026-06-11T11:44:58Z
---

# Phone Numbers

*Part 2 of 3 — see also: [Part 1](phone-numbers--part-1.md), [Part 3](phone-numbers--part-3.md)*

Overview of Telnyx phone numbers (DIDs), including available types, how to search and buy them, ordering restrictions based on account verification, international regulatory requirements, bulk management features, and number lookup capabilities.

## Requirement Groups

Requirement Groups let you pre-fill regulatory documentation once and reuse it across multiple orders, eliminating the need to re-upload the same documents each time.

Requirement Groups are optional in most countries but are **required** (since September 16, 2024) for ordering numbers in: Switzerland (CH), Denmark (DK), Italy (IT), Norway (NO), Portugal (PT), and Sweden (SE).

Each Requirement Group is valid only for a specific combination of **Country**, **phone number type**, and **order type**. For example, a Portugal local ordering group can only be used with Portugal local number orders.

### Creating and Using a Requirement Group

1. Navigate to the [Requirement Groups page](https://portal.telnyx.com/#/numbers/requirements/requirement-groups) and click **New Requirement Group**.
2. Specify the country, phone number type, and order type. Optionally add a customer reference.
3. Fill out all the displayed requirements and click **Submit**.
4. Go to the Buy Numbers page, search for matching numbers, and add them to your cart.
5. In the cart, select the appropriate Requirement Group from the **Requirement Groups** column for each number.
6. Place your order — the requirements are automatically attached and the order is submitted for review.

You can reuse each Requirement Group for as many orders as needed (as long as the country and number type match). For API integration, see the [developer guide](https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups).

## Managing Numbers

### My Numbers Page

The [My Numbers](https://portal.telnyx.com/#/numbers/my-numbers) page lists all procured numbers in purchase order by default. You can sort by order date, phone number, connection, and billing method. Display up to 100 numbers per page.

**Filters** include:

- **Connection or Application** — by SIP connection, Forward-only, or Call Control application
- **Number (partial or full)** — filter by digits
- **Status** — pending purchase, port status, emergency only, etc.
- **Billing Group** — filter by assigned billing group
- **Voice Billing Method** — pay-per-minute or channel billing
- **Tag** — custom tags for organization

**Export** — download a CSV of your numbers, optionally including any filters you have applied.

### Bulk Edit

Select numbers using checkboxes (or the select-all checkbox), then use the **Bulk Actions** dropdown. You can edit up to **100 numbers at a time**; for more, edit sequentially.

Available bulk actions:

- **Edit Voice Settings** — routing/billing, HD Voice, CNAM, forwarding, recording, voicemail, and expert config
- **Edit Messaging Profile** — assign or change the messaging profile (accepts MRC charges)
- **Edit Tags** — add existing tags, create new tags, or remove tags
- **Edit Emergency Services** — configure e911 settings
- **Delete Numbers** — permanently remove numbers

### Individual Number Settings

Click the pencil icon on a number to configure:

**General** — status, purchase date, active services.

**Number Management** — set tags; configure a porting PIN to prevent unauthorized port-out.

**Messaging** — assign a Messaging Profile; view SMS/MMS deliverability (domestic and international).

**Voice Settings:**

- **Routing** — assign a SIP Connection or Voice Application
- **Billing** — select billing group and voice billing method (Pay Per Minute or Channel Billing)
- **HD Voice** — use wideband audio codecs for enhanced PSTN call quality
- **Call Screening** — reject or flag suspicious calls (bad reputation or invalid/C-level Shaken-Stir attestation)
- **CNAM** — enable CNAM listings and Caller ID Name lookup
- **Call Forwarding** — set to Always or On-Failure
- **Inbound Call Recording** — WAV or MP3, single or dual channel; recordings available in the portal
- **Voicemail** — enable with PIN and notification email
- **Noise Suppression** — filters background noise; when enabled at the connection level it affects all associated numbers and supersedes individual number settings

**Advanced:**

- **Translated Number** — custom number translations in SIP headers (useful for ATAs requiring different INVITE/TO values)
- **Media Handling** — RTP Auto Adjust (enabled by default) and Accept Any RTP Packets
- **Tech Prefix** — prefix incoming calls with a tech prefix (IP/FQDN-based SIP Connections only). If both translated number and tech prefix are enabled, the SIP INVITE format is `prefix+translated+number`

### Emergency Services (e911)

Enable emergency services (incurs a monthly fee) and add an address for e911. When dialling 911, the local PSAP sees the caller ID and associated address.

**Warning:** Dialling 911 without emergency services enabled incurs a **$100 fee per call**. Ensure caller ID is sent in +E.164 format.

### Deleting and Restoring Numbers

Delete a number via the trash icon on the My Numbers page or in bulk via Bulk Actions. Monthly recurring charges stop upon deletion.

**Restoration:** You have **15 days** to repurchase deleted numbers. Search for them using Advanced Search (set Phone Number to "Contains" and enter the number). A prorated monthly recurring charge applies. If you cannot find a deleted number within the 15-day window, email [numbering@telnyx.com](mailto:numbering@telnyx.com).

After 15 days, deleted numbers enter an ageing state for another 2 weeks, after which they are released to the general inventory.

### Negative Balance Policy

If your account balance remains negative for more than 30 days:

1. Your numbers are removed and enter a 2-week hold period (only your account can find and buy them back via Search & Buy — adding balance alone is not sufficient).
2. After 2 weeks, numbers enter a 2-week ageing state.
3. After ageing, numbers are released and anyone can purchase them.

Contact [numbering@telnyx.com](mailto:numbering@telnyx.com) to retain numbers, and consider enabling [low balance notifications](https://support.telnyx.com/en/articles/4277896-notification-settings).

## Number Lookup

The Telnyx Number Lookup tool retrieves carrier details and CNAM data for any phone number. Access it at [portal.telnyx.com/#/lookup](https://portal.telnyx.com/#/lookup) or via the [Number Lookup API](https://developers.telnyx.com/docs/identity/number-lookup/quickstart).

### Prerequisites

- A Telnyx account with a positive balance (Number Lookup is unavailable if the balance is negative or zero)
- An API key (for API access)

### Lookup Types

| Lookup Type | Details | Cost |
|---|---|---|
| LRN | Local Routing Number (basic info) | $0.0015/query |
| MCC/MNC | Carrier codes (mobile only) | $0.0025/query |
| CNAM | Caller ID Name | $0.003/query |
| Inbound CNAM | Monthly per-number fee | $0.40/number/month |
| Outbound CNAM Listing | — | Free |

**Example costs:** A landline lookup with Carrier + Caller Name costs $0.0015 + $0.003 = $0.0045. A mobile lookup with the same costs $0.0015 + $0.0025 + $0.003 = $0.007.

View rates at [Telco Pricing](https://portal.telnyx.com/#/pricing/telco). For volume discounts, [contact sales](https://telnyx.com/contact-us).

### Limitations

- Access is restricted to Organization Owners only (no sub-accounts)
- US Toll-Free: RespOrg ID is not returned
- To view full LRN data, enable **Permitted NPAC User** in [Account Settings > Profile](https://portal.telnyx.com/#/account/general) (allow ~15 minutes to apply)
- Usage reports are not real-time; today's lookups appear tomorrow
