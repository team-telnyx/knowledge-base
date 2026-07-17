---
title: Telnyx Account Management
summary: This page covers Telnyx account management topics including verification
  frameworks (legacy Level 1/Level 2 and TPVE), account settings configuration, two-factor
  authentication setup, API key management, the Telnyx Verify API for application-based
  verification, fraud prevention best practices, account compromise response, blocked
  account guidelines, account cancellation, refund policy, and privacy policy.
sources:
- url: https://support.telnyx.com/en/articles/1130595-account-verification
- url: https://support.telnyx.com/en/articles/1130639-what-is-your-refund-policy
- url: https://support.telnyx.com/en/articles/1130689-how-do-i-cancel-my-account
- url: https://support.telnyx.com/en/articles/3610162-prevent-telnyx-account-fraud
- url: https://support.telnyx.com/en/articles/3739748-2fa-totp-setup
- url: https://support.telnyx.com/en/articles/4280610-how-to-setup-your-account-settings
- url: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
- url: https://support.telnyx.com/en/articles/4557103-telnyx-privacy-policy
- url: https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api
- url: https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy
- url: https://support.telnyx.com/en/articles/7020727-account-compromise-what-to-do
- url: https://support.telnyx.com/en/articles/7915224-blocked-account-guidelines
- url: https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status
- url: https://support.telnyx.com/en/collections/3968260-telnyx-identity-verification-tools
updated_at: 2026-07-17T09:01:50Z
---

# Telnyx Account Management

*Part 2 of 2 — see also: [Part 1](telnyx-account-management--part-1.md)*

This page covers Telnyx account management topics including verification frameworks (legacy Level 1/Level 2 and TPVE), account settings configuration, two-factor authentication setup, API key management, the Telnyx Verify API for application-based verification, fraud prevention best practices, account compromise response, blocked account guidelines, account cancellation, refund policy, and privacy policy.

## Telnyx Verify API

Telnyx Verify is a developer product for adding phone-based user verification to your own application. It is separate from Portal 2FA. To use it, you need a Telnyx account, an API key, a Verify Profile configured for the desired channel, and an application or backend that can call the Verify API. The API key should be kept secure and never placed in client-side code, public repositories, or screenshots.

A Verify Profile controls settings such as channel, message behavior, timeout, and optional webhook URLs. Profiles can be created and managed in the Telnyx Portal or via the Verify API.

To send a verification code, the request must include the user's phone number and the `verify_profile_id`. Other channels such as voice call or flash call can be used when enabled and configured.

To verify the submitted code, use the Verify API to submit the user's phone number, the code, and the same `verify_profile_id`. If the code is valid and not expired, the verification succeeds; otherwise, prompt the user to retry or request a new code.

Verify webhooks can be configured for real-time status updates by adding a webhook URL to the Verify Profile.

Production recommendations include rate limiting verification requests by user, phone number, IP address, and session; adding CAPTCHA or authenticated-session checks; using destination allowlists; setting reasonable code timeouts and retry limits; monitoring for unusual traffic patterns, SMS pumping, toll fraud, and repeated failed attempts; avoiding responses that reveal whether a phone number or account exists; and reviewing Verify Profile spend controls and alerting before launch.

The Verify API also supports delivering codes through voice call, flash call, PSD2-specific codes, and specifying the language for voice or SMS delivery.

## Account Security and Fraud Prevention

Telnyx recommends several measures to prevent fraud and secure accounts:

- Secure account passwords
- Review access logs regularly
- Restrict web access to PBX/VoIP systems
- Apply channel limit settings on connections and outbound profiles
- Use a Tech Prefix on connections to segment traffic when sharing an IP across multiple clients
- Use multiple outbound profiles per connection for granular control

Outbound profiles include a max daily spend limit, max destination rate limit, country blacklisting, concurrent call limits, and (for international plans) the ability to allow or disallow regions or countries.

### Best Practices

- **Update passwords** every 30, 60, or 90 days to restrict access for former employees.
- **Rotate API keys** by deleting old keys and generating new ones, especially when keys are shared across applications or teams.
- **Update SIP connection credentials** periodically, which can be automated via API requests.
- **Review notification settings for suspicious outbound voice traffic** – Telnyx sends email notifications for unusual patterns such as multiple concurrent or rapid calls to the same destination prefix, multiple ongoing calls to the same high-cost destination, or multiple long-lived concurrent calls.
- **Enable 2FA** to neutralize risks from compromised passwords.

Abuse can be reported via the [report abuse form](https://telnyx.com/report-abuse), by emailing [abuse@telnyx.com](mailto:abuse@telnyx.com), or through the chat widget.

## Account Compromise Response

If unauthorized access to a Telnyx account is suspected, take the following steps:

1. **Change the login password** for the compromised user under the [general settings](https://portal.telnyx.com/#/app/account/general).
2. **Change credentials for all credential-based SIP connections** in the [SIP Trunking](https://portal.telnyx.com/#/voice/connections) page, and update the credentials on the phone system.
3. **Check IP authentication connections** to ensure all listed IPs are legitimate and not added by an attacker.
4. **Regenerate the messaging profile secret** for any messaging profiles using v1 of the API, and update messaging applications with the new secret.
5. **Delete any active API keys** and generate new ones, updating applications with the new keys.
6. **Check forwarding on all numbers** to ensure no expensive forwarding destinations were set up by an attacker.
7. **Check all Programmable Voice API Applications and TeXML Applications** to confirm they are legitimate, since disabling the API key would not stop traffic through TeXML Applications.

If a bad actor gained access to a system but not the account, they may still have stolen SIP connection credentials, messaging profile secrets, or API keys, so these should be updated in the portal. Enabling 2FA is the single most powerful preventive measure.

## Blocked Account Guidelines

Telnyx has implemented anti-fraud and anti-spam systems that may occasionally suspend legitimate customers whose activities appear suspicious. Specific details about a block cannot be disclosed.

- **Case Review** – Contact [support@telnyx.com](mailto:support@telnyx.com) to request a manual review. If traffic or activity cannot be confirmed as following best practices and terms, Telnyx may advise finding an alternative vendor. If offending traffic can be identified and fixed, the account may be restored.
- **Cooperation and Compliance** – Cooperate with Telnyx during review and address issues promptly. Complaints from end-users about unsolicited messages, scam attempts, or excessive calls may result in a permanent block.
- **Porting Away** – If the decision is permanent, temporary access may be granted to port phone numbers away, with the port-out fee waived. Contact [porting@telnyx.com](mailto:porting@telnyx.com).
- **Requesting a Refund** – Unused funds can be refunded by emailing [billing@telnyx.com](mailto:billing@telnyx.com).
- **Feedback** – Send feedback to [community@telnyx.com](mailto:community@telnyx.com) with the subject line "Feedback: [YOUR_TELNYX_ACCOUNT_EMAIL] [YOUR_TELNYX_CHAT/TICKET_ID] Blocked Account."

## Account Cancellation

To remove a member from an organization, use the [Organization and Members](https://portal.telnyx.com/#/advanced-features/members) section. To cancel an account, email [support@telnyx.com](mailto:support@telnyx.com) with the Security Passphrase for the account.

The Security Passphrase is not the account login password. It can be found in the [Account Security](https://portal.telnyx.com/#/account/my-account/security) section. Cancellation can only be approved from the email address of the account owner.

To un-cancel or re-enable a cancelled account, email [support@telnyx.com](mailto:support@telnyx.com) from the email address to be activated again, or provide the email address of a cancelled sub-member if the requester is the organization owner.

## Refund Policy

Telnyx does not offer refunds for payments made using Bitcoin (BTC), and cannot refund payments that are 180 or more days old regardless of payment method. Any other funds in the account can be refunded by sending a request to [billing@telnyx.com](mailto:billing@telnyx.com). Because services are offered on a pay-as-you-go model, charges for services already used cannot be refunded.

## Privacy Policy

Telnyx's privacy policy provides information about how personal information is handled in line with the General Data Protection Regulation 2016/679. The full policy is available at [telnyx.com/privacy-policy](https://telnyx.com/privacy-policy). By supplying personal data through the website or via staff email addresses, users implicitly agree to the policy.

GDPR and CCPA rights requests must be responded to within one month. To exercise these rights, submit a request at [telnyx.com/request-to-control-review-data](https://telnyx.com/request-to-control-review-data).
