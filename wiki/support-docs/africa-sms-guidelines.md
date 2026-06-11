---
title: Africa SMS Guidelines
summary: SMS guidelines for African countries on the Telnyx platform, including sender
  ID registration requirements, content restrictions, and compliance recommendations
  for Algeria, Benin, Botswana, Burundi, Cape Verde, Central African Republic, Chad,
  Comoros, Djibouti, and Eritrea.
sources:
- url: https://support.telnyx.com/en/articles/6592441-algeria-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596235-benin-sms-guidelines
- url: https://support.telnyx.com/en/articles/6600928-botswana-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601042-burundi-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601074-cape-verde-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601081-central-african-republic-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601133-chad-sms-guidelines
- url: https://support.telnyx.com/en/articles/6601152-comoros-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665699-djibouti-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670452-eritrea-sms-guidelines
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
