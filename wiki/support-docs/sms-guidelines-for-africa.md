---
title: SMS Guidelines for Africa
summary: This page consolidates SMS guidelines for various African countries on the
  Telnyx platform, detailing Alphanumeric Sender ID support, registration requirements,
  and network-specific rules to ensure message delivery and compliance.
sources:
- url: https://support.telnyx.com/en/articles/6671488-guinea-sms-guidelines
  content_hash: 205932e02e5985f5c8b35c788ed7774ed6d53bdb6371d0303ceef4bbf72a5064
- url: https://support.telnyx.com/en/articles/6671725-guinea-bissau-sms-guidelines
  content_hash: 239bcd235cb0f342ebf6e3368a39c13830d4c6d42d0259669e3a6dc3e6a7980a
- url: https://support.telnyx.com/en/articles/6674813-lesotho-sms-guidelines
  content_hash: c73021e833fd5b8d2f5e6be9c4eb7ebeefa20fc1e96de3d7a3e44e999c7a6399
- url: https://support.telnyx.com/en/articles/6674974-liberia-sms-guidelines
  content_hash: e754eafed1bde005835327c57e1dc9f6a1a70b644a5ed8f92811b331c3501f78
- url: https://support.telnyx.com/en/articles/6677982-morocco-sms-guidelines
  content_hash: a3bd9e43a58ee400e76473feeb81be2d1de978b6e509de26318c5385cb19f7c8
- url: https://support.telnyx.com/en/articles/6679062-niger-sms-guidelines
  content_hash: f93684c7fc275ef752a5b3a5e50f7396b060750f9363986c6c15b4578d49ea86
- url: https://support.telnyx.com/en/articles/6680135-somalia-sms-guidelines
  content_hash: 0f62635395e54227d0641bd38785e00e0f8227111e61973f9e8e88c33ec18b49
- url: https://support.telnyx.com/en/articles/6680141-south-sudan-sms-guidelines
  content_hash: a055975919db0bd52fe66f5c9424c32bd943d85b148b91317ab97431cfde2f65
- url: https://support.telnyx.com/en/articles/6683295-tanzania-sms-guidelines
  content_hash: 7f022cda05d6c9731a085b802929c9ae65781a41872065c7a7eb093380f8f0f6
- url: https://support.telnyx.com/en/articles/6683385-tunisia-sms-guidelines
  content_hash: ba581492b544f86b9b8e41a452d01003945909db6a23377bca8dbebe4c272b2a
- url: https://support.telnyx.com/en/articles/6683501-zambia-sms-guidelines
  content_hash: 6f52c2c50a88d4bd4b86b9fbc59122d1ae715bd72b3571f4df0bfcaeaa0467f6
- url: https://support.telnyx.com/en/articles/6683504-zimbabwe-sms-guidelines
  content_hash: 3bd40e043db3398588ca622be71c55ac36e92536318b5cff81c5108339392a43
updated_at: 2026-06-11T11:22:53Z
---

# SMS Guidelines for Africa

This page consolidates SMS guidelines for various African countries on the Telnyx platform, detailing Alphanumeric Sender ID support, registration requirements, and network-specific rules to ensure message delivery and compliance.

## Alphanumeric Sender ID Support and Registration

Alphanumeric Sender IDs are generally supported across African destinations, but requirements vary by country and network. The use of generic Alpha Sender IDs is not recommended; Sender IDs should always be directly related to the message content.

### Mandatory Registration

In the following countries, Alphanumeric Sender ID registration is strictly required. Messages sent from unregistered Sender IDs will be rejected:

- **Morocco** (MCC 604, Dial Code 212)
- **Niger** (MCC 614, Dial Code 227)
- **Tanzania** (MCC 640, Dial Code 255)
- **Tunisia** (MCC 605, Dial Code 216)

### Conditional Network Registration

For certain countries, registration is only required when sending to specific mobile networks. Without registration to these networks, Alpha Senders will be overwritten to generic Sender IDs or messages will not deliver:

- **Guinea** (MCC 611, Dial Code 224): Network MTN (61104)
- **Guinea-Bissau** (MCC 632, Dial Code 245): Network MTN (63202)
- **Liberia** (MCC 618, Dial Code 231): Network Lonestar MTN (61801)
- **South Sudan** (MCC 659, Dial Code 211): Network MTN (65902)
- **Zambia** (MCC 645, Dial Code 260): Network MTN (65402)

### Traffic-Based Registration

- **Zimbabwe** (MCC 648, Dial Code 263): There is a distinction between local and international traffic. Registration is required for local traffic, but international traffic does not require registration.

### No Registration Required

- **Lesotho** (MCC 651, Dial Code 266): Alphanumeric Sender IDs are supported and maintained without registration. There are no content restrictions.
- **Somalia** (MCC 637, Dial Code 252): Alphanumeric Sender IDs are supported and maintained without registration.

## How to Register an Alphanumeric Sender ID

For countries requiring registration, you must submit a request to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com). Include the following details along with a copy of your Business Registration:

1. SenderID to be registered
2. Message/Content type
3. Message/Content example
4. Company name (and Brand name if different)
5. Website of brand or company
6. Company Country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested Alphanumeric Sender ID. If the relationship between your company/brand and the Sender ID is not clear, you must provide additional supporting documentation detailing your business case.

## Compliance and Best Practices

When sending SMS to these destinations, adhere to the following best practices and policies:

- **Consent:** Proof of opt-in consent should be obtained before sending any communications, particularly for marketing SMS.
- **Opt-Out:** Traffic should include clear opt-out options.
- **Acceptable Use:** Always refer to the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging).
