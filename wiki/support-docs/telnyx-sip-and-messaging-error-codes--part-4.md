---
title: Telnyx SIP and Messaging Error Codes
summary: A consolidated reference for Telnyx SIP response codes, the SIP 603+ carrier
  rejection standard, Voice Elements integration with Telnyx SIP, and Telnyx messaging
  error codes, including guidance on causes, workarounds, and best practices for reducing
  false-positive call blocking.
sources:
- url: https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections
- url: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
- url: https://support.telnyx.com/en/articles/6145484-voice-elements-telnyx-sip
- url: https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes
updated_at: 2026-08-05T13:34:42Z
---

# Telnyx SIP and Messaging Error Codes

*Part 4 of 4 — see also: [Part 1](telnyx-sip-and-messaging-error-codes--part-1.md), [Part 2](telnyx-sip-and-messaging-error-codes--part-2.md), [Part 3](telnyx-sip-and-messaging-error-codes--part-3.md)*

A consolidated reference for Telnyx SIP response codes, the SIP 603+ carrier rejection standard, Voice Elements integration with Telnyx SIP, and Telnyx messaging error codes, including guidance on causes, workarounds, and best practices for reducing false-positive call blocking.

## Telnyx Messaging Error Codes

Telnyx uses a structured set of messaging error codes to help identify the exact issue when a message attempt fails. These codes are grouped into categories: `1xxxx` (invalid request), `2xxxx` (account level), and `4xxxx` (delivery errors).

### Invalid Request Responses (1XXXX)

These error codes suggest that there might have been an issue with the message request's formatting, and as a result, they do not exit the Telnyx platform. Rectifying these is typically straightforward.

- **10001 — Inactive phone number**: The phone number specified in the request is not active. If you believe otherwise, consider contacting the recipient's carrier.
- **10002 — Invalid phone number**: The phone number mentioned in the request is invalid.
- **10003 — Invalid URL**: The provided URL is either invalid, improperly structured, or exceeds the length limit. URLs can be up to 2000 characters long.
- **10004 — Missing required parameter**: There's a missing required parameter. Refer to the error's source field to identify the missing information (for example, is the "to" number absent?).
- **10005 — Resource not found**: The desired resource or URL was not located. Ensure you're using the appropriate endpoint.
- **10006 — Invalid ID**: The supplied resource ID is not valid. Double-check if you have the necessary permissions to send SMS with your API key.
- **10007 — Unexpected error**: An unforeseen issue arose, potentially on Telnyx's side. Reattempt and check the status page for any extensive SMS problems on the platform.
- **10009 — Authentication failed**: The mandatory authentication headers were either incorrect or omitted. Make sure to include accurate API keys in your Authorization header.
- **10010 — Authorization failed**: You lack the permissions for the requested action on the given resources. This error is akin to 10009 and 10006. You might need to get in touch with your organization's owner for SMS sending permissions or for using specific features.
- **10011 — Too many requests**: Your requests have exceeded the limit. Ensure your API requests adhere to the prescribed rate. Monitor and control the rate of requests from your application to prevent surpassing the limits.
- **10015 — Bad Request**: The request was unsuccessful due to improper formatting. Make sure your messages align with the stipulated request format. Consult the API messaging guide for further details.
- **10016 — Phone number must be in +E.164 format**: The phone number should be in the +E.164 format.

### Account Level Errors (2XXXX)

These error codes point to potential issues with the account details provided or the account responsible for sending the SMS. It might be necessary to contact your organization's owner or Telnyx support for guidance.

- **20002 — API Key revoked**: The API Key specified in your authorization header isn't active. Visit the API Keys section in your Mission Control Portal to ensure the used API key is enabled.
- **20006 — Expired access token**: The given access token has expired. Check if your API v1 token remains valid. Migrating to API v2 is encouraged.
- **20012 — Account inactive**: Your request can't be processed because your account has been deactivated, possibly due to insufficient funds. Top up your account and try again.
- **20013 — Account blocked**: Your account is blocked. Should this appear to be a mistake, contact Telnyx support.
- **20014 — Account unverified & 20016 — Account not level 1 verified**: You need to validate your account using a mobile phone number to activate messaging.
- **20015 — Feature not enabled**: SMS functionality isn't activated for your account. Reach out to Telnyx customer support for more details.
- **20017 — Account not level 2 verified**: Your account hasn't achieved level 2 verification and therefore can't execute the desired action. Level 2 verification necessitates reaching out to Telnyx and is essential for sending messages using alphanumeric sender IDs.
- **20100 — Insufficient Funds**: Add the necessary funds to your account to dispatch your intended messages.

### Delivery Errors (4XXXX)

These error codes indicate there was an issue when delivering the sent SMS to your desired recipient. This information can be received from downstream and recipient carriers, so it is important to vet your use case and messaging content to ensure deliverability. The SMS Long Code Deliverability Best Practices article is a handy troubleshooting guide for many of these issues.

**Important key points:**

- Messages that fail due to the message failing off the Telnyx network will result in charges, as they have left the Telnyx network.
- Carriers can often block messaging from Toll-Free numbers if the messaging has not been registered. To get started with Toll-Free messaging, it is necessary to have your use case registered due to the high risk of fraud carriers face from this form of messaging. See the Toll-Free messaging article for instructions on how to achieve this.

#### General Delivery Errors

- **40001 — Not Routable**: The destination is either a landline or a non-routable wireless number and doesn't have messaging capabilities.
- **40002 — Blocked as spam — Temporary**: SPAM filter flagged the message. Temporarily halt sending and reassess your recipients to ensure their consent.
- **40003 — Blocked as spam — Permanent**: SPAM filter flagged the message, permanently blocking the originating number. Avoid this by ensuring recipients' consent. Contact Telnyx support if inaccurately flagged.
- **40004 — Rejected by destination**: The recipient's server declined the message. Seek assistance from Telnyx support or the recipient carrier.
- **40005 — Message expired during transmission**: The message wasn't delivered timely. If persistent, reach out to Telnyx support.
- **40006 — Recipient server unavailable**: The recipient's server is non-responsive. If the issue persists, contact Telnyx support.
- **40008 — Undeliverable**: The recipient carrier rejected the message due to various potential reasons.
- **40009 — Invalid message body**: The message body doesn't align with certain carrier rules, leading to rejection. Refer to Telnyx's Acceptable Use Policy.
- **40010 — Unregistered 10DLC Message**: The sending number is not attached to a 10DLC campaign.
- **40011 — Too many requests**: Exceeded the upstream rate limit, flagging the message as SPAM. Adjust your messaging rate as per your account's throughput.
- **40012 — Invalid messaging destination number**: The destination phone number was rejected by the carrier. Potential reasons include:
  - The number is unowned.
  - The number is deactivated.
  - The recipient lacks credit.
  - The recipient cannot receive short codes (for short code messaging only).
- **40013 — Invalid messaging source number**: Your source phone number was declined by the carrier. Ensure your number is correctly provisioned; if uncertain, contact Telnyx support.
- **40014 — Message expired in queue**: The message expired before being relayed by Telnyx. You won't be billed for this. This occurs if your messaging rate surpasses your available SMS throughput.
- **40015 — Blocked as spam — internal**: The message was flagged by Telnyx's internal SPAM filter. Adhere to the Acceptable Use Policy for Messaging.
- **40100 — Number not messaging enabled**: Ensure the number has messaging capabilities and an assigned messaging profile on the Telnyx platform.
- **40150 — Toll free number not in registry**: Ensure you register your toll-free number since it's not in the voice registry.
- **40151 — Message enablement pending with other provider**: The number is being enabled by another messaging provider.
- **40300 — Blocked due to STOP message**: You can't send messages to the destination since they've sent a STOP message to you. Make sure to vet your recipient list. Keywords triggering this block include:
  - CANCEL
  - END
  - QUIT
  - STOP (and its variants)
  - UNSUBSCRIBE
- **40301 — Unsupported message type for the 'to' address**: The requested destination doesn't support the type of message or sender.
- **40302 — Message too large**: SMS exceeding 140 bytes are divided into multiple parts. Depending on content, 34 to 153 characters fit in each segment.
- **40304 — Invalid combination of message content arguments**: SMS needs a body field; MMS requires either subject or media_urls. Check the support docs for message formatting.
- **40305 — Invalid 'from' address**: The sender must be a valid phone number, short code, or alphanumeric sender ID related to the active messaging profile. If you have enabled number pooling and skip unhealthy numbers on your messaging profile, this error can also occur because Telnyx will remove numbers from the pool if it detects that 75% or more of messages are being marked as spam.
- **40306 — Alpha sender not configured**: Update your profile to use an alphanumeric sender ID.
- **40308 — Invalid 'from' address for MMS**: Ensure the 'from' number can send MMS messages.
- **40309 — Invalid destination region**: Ensure the destination region is whitelisted in your messaging profile.
- **40310 — Invalid 'to' address**: The recipient address must be valid.
- **40311 — Invalid messaging profile secret**: Ensure the correct X-Profile-Secret header is provided.
- **40312 — Messaging profile is disabled**: Activate your messaging profile in the portal settings.
- **40313 — Missing messaging profile secret**: Ensure the X-Profile-Secret header is included.
- **40314 — Messaging disabled on account**: If not self-requested, contact Telnyx support.
- **40315 — Unhealthy 'from' address**: The sending number failed a health check due to low deliverability or high spam rates.
- **40316 — No content provided for message**: Provide the necessary fields for either SMS or MMS.
- **40317 — Invalid MMS content**: MMS can have up to 10 URLs and be under 1 MB. Refer to Telnyx's FAQ for MMS guidance.
- **40318 — Message queue full**: Monitor and adjust your message rate according to the throughput guide.
- **40319 — Incompatible message type for the 'to' address**: Ensure compatibility between the sender type and the recipient.
- **40320 — Temporarily unusable 'from' address**: Wait until the number's purchase is finalized for it to be usable.
- **40321 — No usable numbers on messaging profile**: If using number pooling, assign numbers to your messaging profile.
- **40322 — Blocked due to content**: Refer to the Acceptable Use Policy.
- **40328 — SMS exceeds recommended size**: For extended messages, consider sending as MMS.
- **40329 — Toll free number not yet verified**: A use case verification request has not yet been submitted for the number or the request is still pending. Submit a use case verification request for the toll free number or wait for approval on the request.

#### 10DLC Messaging Delivery Errors

These error codes indicate there was an issue when delivering the sent SMS using the 10DLC product.

- **40016 — T-Mobile 10DLC Sending Limit Reached**: 10DLC (10-Digit Long Code) is a system used by carriers like T-Mobile to manage and regulate A2P (Application-to-Person) SMS traffic. Each brand is assigned a certain throughput limit based on their brand score. This error indicates that you've exceeded the daily message sending limit set by T-Mobile for your brand. The count gets reset every day at midnight PST. Either wait for the count to reset at midnight PST or review the throughput limits related to your brand score in Telnyx's FAQ to understand the imposed restrictions.
- **40017 — AT&T 10DLC Spam Message Rejected**: AT&T has identified the content of your message as spam when sent via the 10DLC route. This could be due to various reasons such as the content resembling known spam patterns or the lack of proper opt-in from the message recipients. Review the content of your message to ensure it doesn't violate any spam guidelines. Make certain that you have appropriate permissions (opt-ins) from all recipients before sending messages.
- **40018 — AT&T 10DLC Sending Limit Reached**: Similar to the T-Mobile error, this indicates that you've reached AT&T's sending limit for your brand on the 10DLC route. AT&T's sending limit is given in message parts per minute. This error means that the total number of messages from this campaign has exceeded this limit for this given minute. This limit is influenced by the brand score assigned to your brand. Limit the amount of messages sent per minute by your campaign. Refer to Telnyx's FAQ to get a deeper understanding of the throughput limits based on your brand score.

See the [Frequently Asked Questions about 10DLC](https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc) for more information.
