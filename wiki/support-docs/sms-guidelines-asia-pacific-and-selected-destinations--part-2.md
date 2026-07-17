---
title: 'SMS Guidelines: Asia-Pacific and Selected Destinations'
summary: Consolidated Telnyx SMS guidelines for Australia, Philippines, Ireland, China,
  Hong Kong, India, Macao, Malaysia, Mauritius, Mozambique, Nepal, New Caledonia,
  Singapore, Taiwan, and Trinidad & Tobago, covering MCC/dial codes, Alphanumeric
  Sender ID registration and overwrite rules, content restrictions, and links to the
  Acceptable Use Policy for Messaging.
sources:
- url: https://support.telnyx.com/en/articles/6531656-australia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6531682-philippines-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545161-ireland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601144-china-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674367-hong-kong-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674383-india-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675024-macao-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675110-malaysia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677919-mauritius-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677999-mozambique-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678903-nepal-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679031-new-caledonia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680103-singapore-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683277-taiwan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683379-trinidad-tobago-sms-guidelines
updated_at: 2026-07-17T09:11:00Z
---

# SMS Guidelines: Asia-Pacific and Selected Destinations

*Part 2 of 2 — see also: [Part 1](sms-guidelines-asia-pacific-and-selected-destinations--part-1.md)*

Consolidated Telnyx SMS guidelines for Australia, Philippines, Ireland, China, Hong Kong, India, Macao, Malaysia, Mauritius, Mozambique, Nepal, New Caledonia, Singapore, Taiwan, and Trinidad & Tobago, covering MCC/dial codes, Alphanumeric Sender ID registration and overwrite rules, content restrictions, and links to the Acceptable Use Policy for Messaging.

## Nepal

- **MCC:** 429
- **Dial code:** 977

Alphanumeric Sender IDs are supported. For Network Ncell (42902), Alphanumeric Sender IDs are only supported with registration. Without registration to this network, Alpha Senders will be overwritten to Generic Alpha Sender IDs or will not deliver. The use of generic Alpha Sender IDs is not recommended; Alpha Senders should be directly related to the message content.

## New Caledonia

- **MCC:** 546
- **Dial code:** 687

Alphanumeric Sender IDs are supported and will be maintained; no registration is required. There are no restrictions with regards to content towards this destination.

## Singapore

- **MCC:** 525
- **Dial code:** 65

Mandatory registration of [Alphanumeric Sender IDs](https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id) has been implemented by the Infocomm Media Development Authority (IMDA) since 31 January 2023. From this date until 31 July 2023, all submissions with unregistered Alphanumeric Sender IDs were flagged and overwritten with "Likely-SCAM". After 31 July 2023, messages with unregistered Alphanumeric Sender IDs are blocked.

Registration involves fees and must first be completed directly with the regulator, SGNIC. Users can register directly via the [SGNIC SMS Sender ID Registry portal](https://smsregistry.sg/web/login). Note that users will need a Singapore Unique Entity Number (UEN) to complete the process. More information is available on the [SGNIC FAQ](https://www.sgnic.sg/faq/sms-sender-id-registry). After this step is completed, reach out to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for advice on the next steps.

**Additional recommendations:** Religious, gambling, political, or adult traffic is prohibited.

## Taiwan

- **MCC:** 466
- **Dial code:** 886

All Alphanumeric Sender IDs will be overwritten to a random Local Long Code to ensure delivery.

## Trinidad & Tobago

- **MCC:** 374
- **Dial code:** 1868

Alphanumeric Sender IDs are supported; no registration is required. Occasionally, an Alphanumeric Sender ID might be overwritten to a Random Long Code to ensure delivery towards Network Bmobile (37412).

## Contact and Policy References

For more information on Alpha Sender ID registration, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com). Always refer to the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md) when sending traffic to any of these destinations.
