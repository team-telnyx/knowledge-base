---
title: Trial Account Privileges & Limitations
summary: Capabilities, restrictions, and daily limits applied to Telnyx trial accounts.
sources:
  - url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/trial
    content_hash: 48e88fd009478cc04183ff22279d11c2253d5076d19f026edb7a23a56b403d66
updated_at: 2026-04-10T00:00:00Z
---

# Trial Account Privileges & Limitations

Capabilities, restrictions, and daily limits applied to Telnyx trial accounts.

## Testing credit

**USD \$5** in testing credit is provided.

## Access

* Full access except otherwise specified below.
* Telnyx reserves the right to modify limitations without notification.

## Numbers

### Verified numbers

* Limited to **1 verified number** at any one time.
* Limited to **10 changes** per **trial account lifetime**.
* Limited to **15 delivery attempts** regardless of conversion outcome per **trial account lifetime**.

### Number searching

* Full number display limited to **local numbers** of the account's country of origin.
* All other numbers will be shown redacted (e.g., +49351xxxxxxx).
* No access to other APIs or features in this category.

### Number reservation

* No access to APIs or features in this category.

### Number ordering

* Limited to **1 local number** of the account's country of origin per **trial account lifetime**.
* Successful number activation is subject to inventory availability, sufficient account balance, and local jurisdiction documentation rules.
* This number will be reclaimed within 30 days of purchase if the account has not upgraded.
* No port out is allowed on this number.
* No access to other APIs or features in this category.

### Number porting

* Limited to **50 portability check attempts** per **trial account lifetime**.
* No access to other APIs or features in this category.
* Users do not have proprietary rights to their trial telephone number, and Telnyx reserves the right to make reasonable changes to them with reasonable notice. Users cannot port out their trial number.

### Bundles

* No access to APIs or features in this category.

## Messaging

* Limited to **1 messaging profile** at any one time.
* **Outbound:** Limited to long code sending, destination limited to verified number, and capped at **100 messages a day**.
* **Inbound:** Limited to receiving from the verified number.
* No access to other APIs or features in this category.

## Verify

* Limited to **1 verified profile** at any one time.
* Only SMS is allowed.
* Destination limited to verified number.
* Limited to a max of **50 verifications a day**.
* No access to other APIs or features in this category.

## Voice

### General limits

* Limited to **1 instance per connection type** at any one time.
* Limited to **1 outbound voice profile** at any one time.
* **Outbound** limited to dialing only the verified phone number.
* **Inbound** limited to receiving from the verified phone number.
* Limited to **2 concurrent outbound calls** across all connection instances.
* Limited to a maximum of **10 minutes per call**.

### Programmable Voice

* All machine-generated voices are prepended with: “*This is an automated call generated on the Telnyx platform, please report any abuse to [fraud@telnyx.com](mailto:fraud@telnyx.com)*”.
* This applies to:
  * `/v2/calls`
  * `/v2/calls/:call_control_id/actions/transfer`
  * `/v2/calls/:call_control_id/actions/gather_using_audio`
  * `/v2/calls/:call_control_id/actions/gather_using_speak`
  * `/v2/calls/:call_control_id/actions/playback_start`
  * `/v2/calls/:call_control_id/actions/speak`
  * `/v2/calls/:call_control_id/actions/gather_using_ai`
  * `/v2/calls/:call_control_id/actions/ai_assistant_start`
  * TeXML verb `Play`
  * TeXML verb `Say`
  * TeXML verb `AIGather`
* Limited to a maximum of **100 outbound calls a day**.
* Limited to **10 outbound calls per hour**.

### Microsoft Operator Connect

* No access to APIs or features in this category.

### Microsoft Direct Routing

* No access to APIs or features in this category.

### Zoom Phone Provider Exchange

* No access to APIs or features in this category.

## LRN / Number Lookup

* No access to APIs or features in this category.

## Cloud Storage

* Limited to non-public policy or ACL on buckets or objects.
* Limited to **5 minutes of TTL** on pre-signed URLs.
* Limited to the documented free tier of used capacity across all buckets and regions.

## Wireless

* No access to physical SIM registration.
* No access to eSIM purchase.

## Account features

### Organizations and sub-users

* No access to APIs or features in this category.

### ManagED Accounts

* No access to APIs or features in this category.

### Payment methods

* Limited to credit cards.

### Billing groups

* No access to APIs or features in this category.

### API keys

* Limited to **1 API key** at any one time.
* No access to other APIs or features in this category.

### DDoS mitigation

* No access to APIs or features in this category.


## Related Pages

- [Paid Account Privileges & Limitations](../runbooks/paid-account-privileges-limitations.md)
- [Verified Account Privileges & Limitations](../runbooks/verified-account-privileges-limitations.md)
