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

*Part 6 of 6 — see also: [Part 1](telnyx-phone-numbers-ordering-e911-and-number-management--part-1.md), [Part 2](telnyx-phone-numbers-ordering-e911-and-number-management--part-2.md), [Part 3](telnyx-phone-numbers-ordering-e911-and-number-management--part-3.md), [Part 4](telnyx-phone-numbers-ordering-e911-and-number-management--part-4.md), [Part 5](telnyx-phone-numbers-ordering-e911-and-number-management--part-5.md)*

This page consolidates Telnyx guidance on phone number ordering, including account verification restrictions, searching and buying numbers, requirement groups, working with the numbering team, E911 address registration and setup, testing E911 with 933, handling spam/scam-likely flags, and managing numbers through the My Numbers Page.

## My Numbers Page

The [My Numbers Page](my-numbers-page.md) in the Telnyx Portal provides an overview of all procured numbers along with options for managing them:

- List your procured numbers
- Number filters to help search and find specific numbers
- Bulk edit numbers to make bulk changes
- Number settings to provide information about and enable features for your numbers
- Enable Emergency Services (E911)
- Export/download a CSV file with a list of your numbers

Numbers display in the order they were purchased by default. You can sort by order date, phone number, connection, and billing method. Up to 100 numbers can be shown per page.

### Number Filters

Available filters include:

- **Connection or Application:** Filter by SIP connection, Forward-only numbers, or Call Control applications.
- **Number (Partial or Full):** Input any quantity of digits to filter.
- **Status:** Based on procurement status, including pending purchase, port status, and emergency only.
- **Billing group:** Filter by assigned billing group for reports and invoicing.
- **Voice Billing Method:** Normal billing by minutes or channel billing.
- **Tag:** Custom tags per number for filtering by name, organization, or other criteria.

### Export and Download CSV

When exporting numbers as CSV, you can export all numbers or include any applied filters. The export file automatically downloads through your browser once ready.

### Bulk Edit Numbers

Select multiple numbers and click the **Bulk Actions** drop-down menu to edit messaging profile, tags, voice settings, emergency settings, or delete multiple numbers. You can edit up to 100 numbers at a time; for more, edit sequentially.

### Number Settings

Each number has its own configurable services, accessed by clicking the pencil icon on the right.

**Settings:**

- **General:** Displays status, purchase date, and Active Services.
- **Number Management:** Set tags for multi-tenant environments and easy CDR report downloads.
- **Porting:** Set a PIN to verify porting requests and prevent unauthorized ports.
- **Delete Number:** Delete the selected number from your account.

**Messaging:**

- **Routing:** Assign a Messaging Profile to the selected number.
- **Deliverability:** Indicates if the number is capable of sending or receiving SMS/MMS domestically and internationally.

**Voice Settings:**

- **Routing:** Assign a SIP Connection or Voice Application to the selected number.
- **Billing:** Create or select a billing group and set the Voice Billing Method (Pay Per Minute or Channel Billing).

**Services:**

- **HD Voice:** Enables wideband audio codecs (when supported) to enhance PSTN call quality.
- **Call Screening:** Rejects or flags suspicious calls from PSTN based on originating number reputation or STIR/SHAKEN attestation level (invalid or C).
- **CNAM:** Enable and set CNAM Listings and Caller ID Name.
- **Call Forwarding:** Configure forwarding to another number, set to Always or On-Failure.
- **Inbound Call Recording:** Store recordings of received calls in WAV or MP3, single or dual channel.
- **VoiceMail:** Enable voicemail services with configurable PIN and notification email.
- **Noise Suppression:** Filters background noise for clearer communication. Enabling at the connection level affects all associated numbers and supersedes individual settings.

**Advanced:**

- **Translated Number:** Set up custom number translations in SIP headers, ideal for ATAs requiring a different value in the INVITE/TO header for inbound calls.
- **Media Handling:** Telnyx automatically detects your media IP address by monitoring RTP packets and adjusts if it differs from the announced pair. Disable by unselecting **Enable RTP Auto Adjust**. Extend behavior to the whole call duration by selecting **Accept any RTP packets**.
- **Enable Tech Prefix:** Differentiate between incoming numbers using a tech prefix. Works only with IP/FQDN-based SIP Connections, not SIP credentials-based Connections.

  Example: SIP Connection A has tech prefix 8888, SIP Connection B has tech prefix 1234. If SIP Connection A dials a number associated with SIP Connection B where B has tech prefix enabled, the incoming call will be prefixed with 1234+number. When disabled, the tech prefix will not be included.

  Note: If you have translated number enabled with a value of 4444 and tech prefix enabled, the resulting SIP INVITE would look like 1234+4444+number.

**Emergency Services:**

Set up emergency services for the number, which incurs a monthly fee. Once enabled, add an address for E911 services. When dialing 911 from this number, the local PSAP will see the caller's ID and the associated address.

### Important Notes

- If you dial 911 without having emergency services enabled on your DIDs, you will incur a $100 fee per call. Ensure the caller ID is sent out in `+E.164` format.
- If your account balance remains negative for more than 30 days, you will receive an email indicating your account has been abolished. Your phone numbers will be removed and enter a 2-week hold period during which only your account can buy them back. After the hold period, numbers enter a 2-week aging state, after which they are released and anyone can buy them. To retain numbers, contact [numbering@telnyx.com](mailto:numbering@telnyx.com). Consider enabling low balance notifications as a reminder to keep your balance positive.
