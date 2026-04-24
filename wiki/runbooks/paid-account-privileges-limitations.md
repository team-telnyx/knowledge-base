---
title: Paid Account Privileges & Limitations
summary: Capabilities and restrictions applied to paid Telnyx accounts.
sources:
  - url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/paid
    content_hash: 6109b411086832d106461dde8133fdf6e79e53b2e434c83c3a45db0c2bcb49a3
updated_at: 2026-04-10T00:00:00Z
---

# Paid Account Privileges & Limitations

Capabilities and restrictions applied to paid Telnyx accounts.

## Access

* Full access except otherwise specified below.
* Telnyx reserves the right to modify limitations without notification.

## Numbers

### Number searching

* No access to number blocks.

### Number ordering

* Limited to local numbers whose country code matches the account's country of origin.

### Number porting

* No access to LRN migration.

## Messaging

* No access to 10DLC.
* No access to Toll-Free verification.
* No access to hosted messaging.

## Voice

### General limits

* Limited set of outbound destination country codes.
* Limited to **5 concurrent outbound calls** across all connection types.

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

## Cloud Storage

* Limited to non-public policy or ACL on buckets or objects.
* Limited to **5 minutes of TTL** on pre-signed URLs.

## Account features

### ManagED Accounts

* No access to APIs or features in this category.

### Payment methods

* Credit card
* PayPal

### DDoS mitigation

* No access to APIs or features in this category.


## Related Pages

- [Trial Account Privileges & Limitations](../runbooks/trial-account-privileges-limitations.md)
- [Verified Account Privileges & Limitations](../runbooks/verified-account-privileges-limitations.md)
