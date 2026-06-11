---
title: Africa SMS Guidelines
summary: SMS guidelines for African countries on the Telnyx platform, including sender
  ID registration requirements, content restrictions, and compliance recommendations
  for Algeria, Benin, Botswana, Burundi, Cape Verde, Central African Republic, Chad,
  Comoros, Djibouti, and Eritrea.
sources:
- url: https://support.telnyx.com/en/articles/6592441-algeria-sms-guidelines
  content_hash: bf3b5f614ac27060c43aea5f541632359fc8539f3ebdf8b3feb8f74515d3f6e6
- url: https://support.telnyx.com/en/articles/6596235-benin-sms-guidelines
  content_hash: 04beff42a89e11abeb42fa9044f23eaa0079cf177e61003a8a506acea03a0e7a
- url: https://support.telnyx.com/en/articles/6600928-botswana-sms-guidelines
  content_hash: daff80eda87dbab9f7c66d2ed1d5ac6c11d8b83f3056152c1873f82971603684
- url: https://support.telnyx.com/en/articles/6601042-burundi-sms-guidelines
  content_hash: f8901823f2394c50a084a23b6a3e4bc097da0864a9e9f2c8a641a48f25bca848
- url: https://support.telnyx.com/en/articles/6601074-cape-verde-sms-guidelines
  content_hash: 60161c5ea369c04c599034455463beda2bcaf0ea3b8e1e2d915d99963a7d47f3
- url: https://support.telnyx.com/en/articles/6601081-central-african-republic-sms-guidelines
  content_hash: 61a2dd903e4f78a66c336d5302b230a883b07131242bba02708aa743877393ad
- url: https://support.telnyx.com/en/articles/6601133-chad-sms-guidelines
  content_hash: f551f19ccbc0370fb32a4d2e07092ee929438e1eaeaead6aef7dc8237b20b212
- url: https://support.telnyx.com/en/articles/6601152-comoros-sms-guidelines
  content_hash: 6f3f024dea74c0717fed05707933772ef1d85d40e42afd3a1d1ce9969611cb24
- url: https://support.telnyx.com/en/articles/6665699-djibouti-sms-guidelines
  content_hash: e6be029da119bedf3d0361f024ce309fabcc57483f11cfd0f49de25465209e44
- url: https://support.telnyx.com/en/articles/6670452-eritrea-sms-guidelines
  content_hash: 8f459d1d6e9237a5c63a0c3509009a67bd041fcaaee14abf993eb9d626316e75
updated_at: 2026-06-11T11:23:31Z
---

# Africa SMS Guidelines

SMS guidelines for African countries on the Telnyx platform, including sender ID registration requirements, content restrictions, and compliance recommendations for Algeria, Benin, Botswana, Burundi, Cape Verde, Central African Republic, Chad, Comoros, Djibouti, and Eritrea.

## Country Reference

| Country | MCC | Dial Code | Sender ID Registration | Content Restrictions | Generic Alpha Sender IDs |
|---|---|---|---|---|---|
| Algeria | 603 | 213 | Required | - | - |
| Benin | 616 | 229 | Required for MTN (61603) | - | Not recommended |
| Botswana | 652 | 267 | Not possible | - | Not recommended (may be rejected/blocked) |
| Burundi | 642 | 257 | Required | - | - |
| Cape Verde | 625 | 238 | Not required | None | - |
| Central African Republic | 623 | 236 | Not required | None | - |
| Chad | 622 | 235 | Required | - | - |
| Comoros | 654 | 269 | Required | - | - |
| Djibouti | 253\* | 638\* | Not required | None | Not recommended |
| Eritrea | 657 | 291 | Not required | Religious, political, or adult traffic prohibited | Not recommended |

\* *Note: The MCC and Dial Code for Djibouti appear swapped in the source documentation. The actual MCC is 638 and the Dial Code is 253.*

## Alphanumeric Sender ID Registration

For countries where registration is required (Algeria, Burundi, Chad, and Comoros), all messages from unregistered Sender IDs will be rejected. To register an Alphanumeric Sender ID, provide the following details along with a copy of your Business Registration to [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com):

1. SenderID to be registered
2. Message/Content type
3. Message/Content example
4. Company name (and Brand name if different)
5. Website of brand or company
6. Company Country of origin
7. Expected volumes per month
8. Email linked to your Telnyx account

Companies must have a valid business case for the requested Alphanumeric Sender ID. If the relationship between your company/brand and the requested Sender ID is not clear, you must provide additional supporting documentation detailing your business case.

For Benin, Alphanumeric Sender IDs are supported but registration is specifically required for the MTN network (61603). Without registration to this network, Alpha Senders will be overwritten to generic Alpha Sender IDs or will not deliver.

## Content and Usage Recommendations

- **Generic Alpha Sender IDs:** The use of generic Alpha Sender IDs is not recommended in Benin, Botswana, Djibouti, and Eritrea. Alphanumeric Sender IDs should be directly related to the message content. In Botswana, generic Alpha Sender IDs can be rejected or blocked by local operators.
- **Opt-In Consent:** For countries requiring Sender ID registration (Algeria, Burundi, Chad, and Comoros), consent (Proof for Opt-in) should be obtained before sending any communications, such as Marketing SMS. Traffic should also include clear Opt-Out options.
- **Content Restrictions:** Religious, political, or adult traffic is prohibited in Eritrea. Cape Verde, Central African Republic, and Djibouti have no content restrictions.
- **Acceptable Use:** Always refer to the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging).
