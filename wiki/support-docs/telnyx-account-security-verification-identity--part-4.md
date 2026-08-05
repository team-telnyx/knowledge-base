---
title: Telnyx Account Security, Verification & Identity
summary: This page consolidates Telnyx guidance on account verification (legacy Level
  1/Level 2 and the newer Trial-Paid-Verified-Enterprise framework), Mission Control
  Portal two-factor authentication, the Telnyx Verify API for embedding 2FA in your
  own applications, fraud prevention and account compromise recovery, blocked account
  guidelines, refunds, TLS/SSL certificate handling, and webhook certificate authority
  errors.
sources:
- url: https://support.telnyx.com/en/articles/1130595-account-verification
- url: https://support.telnyx.com/en/articles/1130639-what-is-your-refund-policy
- url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
- url: https://support.telnyx.com/en/articles/3610162-prevent-telnyx-account-fraud
- url: https://support.telnyx.com/en/articles/3739748-2fa-totp-setup
- url: https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api
- url: https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy
- url: https://support.telnyx.com/en/articles/7020727-account-compromise-what-to-do
- url: https://support.telnyx.com/en/articles/7915224-blocked-account-guidelines
- url: https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com
- url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
- url: https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status
- url: https://support.telnyx.com/en/collections/3968260-telnyx-identity-verification-tools
updated_at: 2026-08-05T13:26:47Z
---

# Telnyx Account Security, Verification & Identity

*Part 4 of 5 — see also: [Part 1](telnyx-account-security-verification-identity--part-1.md), [Part 2](telnyx-account-security-verification-identity--part-2.md), [Part 3](telnyx-account-security-verification-identity--part-3.md), [Part 5](telnyx-account-security-verification-identity--part-5.md)*

This page consolidates Telnyx guidance on account verification (legacy Level 1/Level 2 and the newer Trial-Paid-Verified-Enterprise framework), Mission Control Portal two-factor authentication, the Telnyx Verify API for embedding 2FA in your own applications, fraud prevention and account compromise recovery, blocked account guidelines, refunds, TLS/SSL certificate handling, and webhook certificate authority errors.

## Account Compromise Recovery

If you suspect that someone has accessed your Telnyx account without your permission, take these steps to protect your account and prevent future unauthorized access:

- **Change the login password** for the compromised user in your organization under the [general settings](https://portal.telnyx.com/#/app/account/general) of the account.
- **Change credentials for all credential authentication-based SIP connections** in the [SIP Trunking](https://portal.telnyx.com/#/voice/connections) page. Update the credentials on your phone system as well. Make sure all SIP connections in your account were set up by you and not the bad actor.
- **Check the configuration of all your [IP authentication connections](https://portal.telnyx.com/#/voice/connections)** to make sure all the IPs are yours and not ones set up by the bad actor.
- **Regenerate the [messaging profile](https://portal.telnyx.com/#/app/programmable-messaging/profiles) secret** for any messaging profiles using v1 of the API. Update your messaging applications with the new secret.
- **Delete any [API keys](https://portal.telnyx.com/#/app/api-keys)** that were active when the bad actor accessed your account, then generate new API keys for your applications.
- **Check forwarding on [all numbers](https://portal.telnyx.com/#/app/numbers/my-numbers)** in your account to make sure the bad actor has not set up forwarding to expensive numbers.
- **Check all your [Programmable Voice API Applications](https://portal.telnyx.com/#/app/call-control/applications) and [TeXML Applications](https://portal.telnyx.com/#/app/call-control/texml)** to make sure they are actually yours and not applications configured by the bad actor. Disabling the API key would prevent traffic through Voice API Applications but not TeXML Applications.

The single most powerful thing you can do to prevent this from happening in the future is enabling two-factor authentication. If a bad actor has gained access to your system but not your account, they can still have stolen the credentials for your SIP connection, the messaging profile secret, or the API keys, so make sure to update them in your Mission Control Portal.

For more information on other options to prevent fraud on your account, see [Prevent Telnyx Account Fraud](prevent-telnyx-account-fraud.md).

## Blocked Account Guidelines

Telnyx has implemented anti-fraud and anti-spam systems to protect customers and the global community. Occasionally, legitimate customers may get suspended by these security measures if their activities appear suspicious. Specific details about an account's block cannot be disclosed, as it would compromise the effectiveness of the security measures.

### Case Review

If you believe you have been blocked in error, contact the support team at [support@telnyx.com](mailto:support@telnyx.com). Telnyx will manually review your case to determine whether the block can be lifted. If Telnyx is unable to confirm that your traffic or activity follows best practices and the terms and conditions, Telnyx may advise you to find an alternative vendor for all or some of the related traffic. If the offending traffic or behavior can be identified and fixed, there is a possibility of restoring your account. Not all requests may be reviewed, or there may be a delay in processing.

### Cooperation and Compliance

It is essential to cooperate with Telnyx during the review process and address any identified issues promptly. If Telnyx receives complaints from end-users regarding your account's traffic or activity (such as unsolicited messages, scam attempts, or excessive calls), it may result in a permanent block. Avoid contacting individuals who have not requested to be contacted, especially multiple times.

### Porting Away

If the decision is made to permanently part ways, Telnyx may grant temporary access to port your phone numbers away. Telnyx will waive the port-out fee for blocked accounts. Message [porting@telnyx.com](mailto:porting@telnyx.com).

### Requesting a Refund

If Telnyx has decided to keep the block permanently and you have unused funds in your account, you may request a refund by emailing [billing@telnyx.com](mailto:billing@telnyx.com).

### Feedback and Suggestions

Send feedback or suggestions regarding the block review process to [community@telnyx.com](mailto:community@telnyx.com) with the subject line "Feedback: [YOUR_TELNYX_ACCOUNT_EMAIL] [YOUR_TELNYX_CHAT/TICKET_ID] Blocked Account". This is not a channel to appeal your account status and you may not receive any response.

## Refund Policy

Telnyx does not offer refunds for payments made using Bitcoin (BTC). Additionally, Telnyx is unable to refund payments that are 180 or more days old, regardless of the payment method used.

Any funds left in your account that do not match the above criteria can be refunded. Send a request to [billing@telnyx.com](mailto:billing@telnyx.com).

### Pay-as-you-go Refund Policy

Telnyx offers services via a pay-as-you-go model, so charges billed for services already used cannot be refunded.
