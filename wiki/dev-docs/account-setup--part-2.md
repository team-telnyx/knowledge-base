---
title: Account Setup
summary: Walks through creating a Telnyx account, the trust and safety checks applied
  at signup, the Pretrial–Trial–Paid–Verified–Enterprise (PTPVE) account framework,
  the privileges and limitations at each level, data locality options, and how to
  upgrade between levels.
sources:
- url: https://developers.telnyx.com/docs/account-setup/account-upgrade
- url: https://developers.telnyx.com/docs/account-setup/create-account
- url: https://developers.telnyx.com/docs/account-setup/data-locality
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/index
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/paid
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/pretrial
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/trial
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/verified
- url: https://developers.telnyx.com/docs/account-setup/signup
- url: https://developers.telnyx.com/docs/account-setup/using-trial-account
updated_at: 2026-08-05T13:38:21Z
---

# Account Setup

*Part 2 of 3 — see also: [Part 1](account-setup--part-1.md), [Part 3](account-setup--part-3.md)*

Walks through creating a Telnyx account, the trust and safety checks applied at signup, the Pretrial–Trial–Paid–Verified–Enterprise (PTPVE) account framework, the privileges and limitations at each level, data locality options, and how to upgrade between levels.

## Trial account

Trial accounts are intended for hands-on testing of Voice, Messaging, and Verify against a verified phone number.

### Testing credit

- **USD $5** in testing credit is provided.

### Access

- Full access except where noted below.
- Telnyx reserves the right to modify limitations without notification.

### Numbers

- **Verified numbers** — Limited to **1 verified number** at any one time, **10 changes** per trial account lifetime, and **15 delivery attempts** regardless of conversion outcome per trial account lifetime.
- **Searching** — Full number display limited to local numbers of the account's country of origin. All other numbers are shown redacted (e.g., `+49351xxxxxxx`). No access to other APIs or features in this category.
- **Reservation** — No access.
- **Ordering** — Limited to **1 local number** of the account's country of origin per trial account lifetime. Successful activation depends on inventory availability, sufficient account balance, and local jurisdiction documentation rules. The number is reclaimed within 30 days of purchase if the account has not upgraded. No port out is allowed. No access to other APIs or features in this category.
- **Porting** — Limited to **50 portability check attempts** per trial account lifetime. Users do not have proprietary rights to their trial telephone number, and Telnyx reserves the right to make reasonable changes with reasonable notice. Users cannot port out their trial number.
- **Bundles** — No access.

### Messaging

- Limited to **1 messaging profile** at any one time.
- **Outbound** — Long code sending only, destination limited to the verified number, capped at **100 messages a day**.
- **Inbound** — Limited to receiving from the verified number.
- No access to other APIs or features in this category.

### Verify

- Limited to **1 verified profile** at any one time.
- Only SMS is allowed.
- Destination limited to the verified number.
- Limited to a max of **50 verifications a day**.
- No access to other APIs or features in this category.

### Voice

- **General limits** — Limited to **1 instance per connection type** and **1 outbound voice profile** at any one time. Outbound calls are limited to dialing only the verified phone number; inbound calls are limited to receiving from the verified phone number. Limited to **2 concurrent outbound calls** across all connection instances and a maximum of **10 minutes per call**.
- **Programmable Voice** — All machine-generated voices are prepended with: *"This is an automated call generated on the Telnyx platform, please report any abuse to [fraud@telnyx.com](mailto:fraud@telnyx.com)"*. This applies to the same endpoints and TeXML verbs listed for pretrial accounts. Limited to a maximum of **100 outbound calls a day** and **10 outbound calls per hour**.
- **Microsoft Operator Connect, Microsoft Direct Routing, Zoom Phone Provider Exchange** — No access.

### LRN / Number Lookup

- No access.

### Cloud Storage

- Limited to non-public policy or ACL on buckets or objects.
- Limited to **5 minutes of TTL** on pre-signed URLs.
- Limited to the documented free tier of used capacity across all buckets and regions.

### Wireless

- No access to physical SIM registration.
- No access to eSIM purchase.

### Account features

- **Organizations and sub-users** — No access.
- **ManagED Accounts** — No access.
- **Payment methods** — Limited to credit cards.
- **Billing groups** — No access.
- **API keys** — Limited to **1 API key** at any one time. No access to other APIs or features in this category.
- **DDoS mitigation** — No access.

## Paid account

Paid accounts unlock production usage with broader access, but a few restrictions remain.

### Access

- Full access except where noted below.
- Telnyx reserves the right to modify limitations without notification.

### Numbers

- **Searching** — No access to number blocks.
- **Ordering** — Limited to local numbers whose country code matches the account's country of origin.
- **Porting** — No access to LRN migration.

### Messaging

- No access to 10DLC.
- No access to Toll-Free verification.
- No access to hosted messaging.

### Voice

- **General limits** — Limited set of outbound destination country codes. Limited to **5 concurrent outbound calls** across all connection types.
- **Programmable Voice** — All machine-generated voices are prepended with: *"This is an automated call generated on the Telnyx platform, please report any abuse to [fraud@telnyx.com](mailto:fraud@telnyx.com)"*. This applies to the same endpoints and TeXML verbs listed for pretrial accounts. Limited to a maximum of **100 outbound calls a day** and **10 outbound calls per hour**.

### Cloud Storage

- Limited to non-public policy or ACL on buckets or objects.
- Limited to **5 minutes of TTL** on pre-signed URLs.

### Account features

- **ManagED Accounts** — No access.
- **Payment methods** — Credit card, PayPal.
- **DDoS mitigation** — No access.

## Verified account

Verified accounts are the highest self-serve tier in the PTPVE framework.

### Access

- Full access except where noted below.
- Telnyx reserves the right to modify limitations without notification.

### Numbers

- **Searching** — No access to number blocks.
- **Ordering** — No access to number blocks.
- **Porting** — No access to LRN migration.

### Account features

- **ManagED Accounts** — No access.
- **Payment methods** — Credit card, PayPal, BTC.
- **DDoS mitigation** — No access.

Qualification by the Telnyx sales team is required to upgrade to the enterprise level and gain access to the features above. [Contact Telnyx](https://telnyx.com/contact-us) to start the process.

## Using your trial account

Follow this process to make the most of your trial credit and stay within trial limitations.

1. **Verify a phone number.** A [verified number](https://portal.telnyx.com/#/numbers/verified-numbers) is essential to test Voice and Messaging. Use a mobile phone number that you control. Trial accounts have limits on delivery attempts and the number of changes allowed; once the allowance is depleted, [upgrade your account](https://developers.telnyx.com/docs/account-setup/account-upgrade).
2. **Search for and purchase a phone number.** Search results show only local (to the signup origin) numbers in full E.164; other results appear partially redacted. A successful purchase depends on inventory availability, sufficient account balance, and local jurisdiction [documentation rules](https://portal.telnyx.com/#/numbers/requirements). Only **one** phone number order is allowed during the trial, regardless of the outcome.
3. **Test calling workflows.** Use one of the following tutorials to place calls:
   - [SIP Trunking](https://developers.telnyx.com/docs/voice/sip-trunking/get-started)
   - [Programmable Voice](https://developers.telnyx.com/docs/voice/programmable-voice/get-started)
   - [TeXML](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup)

   Regardless of how the call is created, the destination is limited to the verified phone number from Step 1, and inbound calls must also originate from that number. See [Trial Account Privileges & Limitations](trial-account-privileges-limitations.md) for the full voice limits.
4. **Test messaging workflows.** Use the [Send Message](https://developers.telnyx.com/docs/messaging/messages/send-message) tutorial to send SMS. Outbound messages must target the verified phone number you configured, and inbound messages must also originate from that number. See [Trial Account Privileges & Limitations](trial-account-privileges-limitations.md) for the full messaging limits.
