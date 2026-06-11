---
title: Telnyx Account Security, Fraud Prevention, and Compliance
summary: A practical guide to securing your Telnyx account, preventing fraud and abuse,
  responding to incidents, and understanding compliance topics including privacy,
  SOC reporting, and HIPAA considerations.
sources:
- url: https://support.telnyx.com/en/articles/3610162-prevent-telnyx-account-fraud
- url: https://support.telnyx.com/en/articles/4557103-telnyx-privacy-policy
- url: https://support.telnyx.com/en/articles/7020727-account-compromise-what-to-do
- url: https://support.telnyx.com/en/articles/7984661-how-to-reset-your-password
- url: https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com
- url: https://support.telnyx.com/en/articles/7915224-blocked-account-guidelines
- url: https://support.telnyx.com/en/articles/8648864-what-happens-with-my-numbers-after-my-account-gets-abolished-for-negative-balance
- url: https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications
- url: https://support.telnyx.com/en/articles/1130713-what-is-my-sip-account-connection-password
- url: https://support.telnyx.com/en/articles/3347891-hipaa-baas-and-the-conduit-exception
updated_at: 2026-05-20T14:44:49Z
---

# Telnyx Account Security, Fraud Prevention, and Compliance

A practical guide to securing your Telnyx account, preventing fraud and abuse, responding to incidents, and understanding compliance topics including privacy, SOC reporting, and HIPAA considerations.

## Fraud prevention controls in Mission Control
Strengthen your defenses using built-in limits and routing controls:
- Apply channel/concurrency limits on both SIP Connections and Outbound Profiles to cap simultaneous traffic.
- Use multiple Outbound Profiles per Connection for granular controls.
- Configure Outbound Profile safeguards: max daily spend, max destination rate, country/region allowlists and blacklists, and concurrent call caps (international plans support per-region or per-country allow/deny).
- Use a Tech Prefix to segment traffic when sharing a single IP across multiple clients.
- Restrict public web access to your PBX/VoIP system and routinely review access logs.

## Account security best practices
- Update your Telnyx Portal password on a 30–90 day cadence and enforce strong, unique passwords across your team.
- Rotate API keys regularly; remove old keys and update applications promptly.
- Rotate credentials for SIP credential-based connections on a schedule (can be automated via API).
- Enable 2FA (two-factor authentication) on your account to neutralize risks from compromised passwords. You can enable 2FA in the Portal’s Security settings.
- Configure Suspicious Outbound Voice Traffic notifications so alerts reach the right responders. Example patterns include bursts to the same prefix, multiple long-lived calls, and high-cost destinations. See Notification Settings for setup guidance.

## Incident response: steps after an account compromise
If you suspect unauthorized access, act immediately:
1. Change the compromised user’s Portal login password (Account General Settings).
2. Change credentials for all credential-auth SIP Connections, and update your PBX/phones accordingly. Verify every SIP Connection was created by you.
3. Review IP-authenticated Connections and remove any unknown IPs.
4. Regenerate Messaging Profile secrets (for v1 API) and update your applications.
5. Delete all active API Keys and generate new ones; update all dependent apps.
6. Audit call forwarding on all numbers to ensure no fraudulent forwarding is in place.
7. Review all Programmable Voice API and TeXML Applications; disable anything you didn’t create. Note: Disabling API keys stops Voice API traffic but not TeXML—remove unwanted TeXML apps too.
8. Enable 2FA if not already in place.

## Password management and recovery
- Password policy: at least 12 characters, one uppercase letter, and one punctuation/symbol.
- Reset via Sign-In: use “Forgot your password” on the Portal login page, follow the email link, and set a new password.
- Reset in-session: Account Settings → Security → Change Password (email verification code required), then enter current and new password.

## Managing SIP credentials
- When creating a credentials-based SIP Connection, a random username/password is generated; you can change it any time.
- Find/update: Voice → SIP Trunking → edit the Connection → Authentication and Routing tab. Use a strong, randomly generated password.

## TLS certificates for api.telnyx.com
- Telnyx uses Cloudflare Universal TLS to provide publicly trusted certificates. Most clients trust these by default via the OS/browser/JVM trust store.
- If your runtime does not use a standard trust store, import Cloudflare’s trusted CA bundle from the public repository (cfssl_trust) into your application’s trust store.
- Cloudflare may change issuing CAs (e.g., Baltimore CyberTrust Root). Including the Cloudflare trust bundle helps maintain continuity. For assistance, contact support@telnyx.com.

## Blocked or suspended accounts
- Telnyx anti-fraud/anti-spam systems may block accounts exhibiting suspicious activity. Specific trigger details aren’t shared to preserve control efficacy.
- If blocked in error, email support@telnyx.com for a manual review. Cooperate promptly and remediate any issues; persistent complaints (e.g., spam/scam/excessive calls) may result in permanent blocks.
- Porting away: for permanent blocks, Telnyx may grant temporary access to port numbers out and will waive port-out fees (email porting@telnyx.com).
- Refunds: request unused balance refunds at billing@telnyx.com.
- Process feedback (not an appeals channel): community@telnyx.com with subject “Feedback: [YOUR_TELNYX_ACCOUNT_EMAIL] [YOUR_TELNYX_CHAT/TICKET_ID] Blocked Account”.

## Negative balance abolishment and number recovery
- After one month with a negative balance, the account may be abolished and numbers removed.
- Number lifecycle after deletion:
  - Hold (≈2 weeks): only you can re-purchase the numbers via Search and Buy Numbers.
  - Aging (≈2 weeks): no one can purchase (regulatory recycling window).
  - Release: numbers become generally available to any customer.
- Adding balance alone doesn’t restore numbers—you must re-purchase them while on Hold. If numbers are Aging, contact numbering@telnyx.com (support@telnyx.com is 24/7; numbering is not).
- Prevent future issues: set up Auto-Recharge to cover monthly recurring charges (MRCs), and enable notifications (e.g., low balance, number deletions).

## Privacy policy and data rights
- Review Telnyx’s Privacy Policy to understand how personal data is collected and processed in line with GDPR.
- GDPR/CCPA: You can request to exercise data subject rights (access, correction, deletion, etc.). Telnyx typically responds within one month. Submit requests at https://telnyx.com/request-to-control-review-data.

## SOC compliance and accessing trust reports
- Telnyx undergoes independent audits and maintains SOC certifications:
  - SOC 2 Type I (control design at a point in time)
  - SOC 2 Type II (operational effectiveness over time)
  - SOC 3 (publicly shareable summary)
- Request SOC reports via the Trust Center: https://trust.telnyx.com (login and, if required, NDA).
- Controls commonly validated include governance and policies, risk management, RBAC and least privilege with MFA for elevated access, access reviews and offboarding, physical data center controls, continuous monitoring and incident response, change management and secure SDLC, and vendor security oversight.

## HIPAA, BAAs, and the conduit exception
- HIPAA may require a Business Associate Agreement (BAA) when vendors access, receive, transmit, or store PHI.
- Telecommunications services can fall under the HIPAA “conduit exception,” which generally removes the need for a BAA when acting merely as a conduit (temporary storage incidental to transmission is permitted under the exception).
- In general, Telnyx services fall within this conduit exception; Telnyx typically does not sign BAAs. For specific needs, contact sales@telnyx.com. This is not legal advice.

## Reporting abuse and learning about spoofing
- Report abuse: https://telnyx.com/report-abuse or email abuse@telnyx.com.
- Learn more about spoofing and STIR/SHAKEN:
  - What is spoofing and why it matters: https://telnyx.com/resources/what-is-spoofing-and-why-does-it-matter
  - SHAKEN/STIR explained: https://telnyx.com/resources/shaken-stir-explained
  - How Telnyx shuts down call fraud and phone scams: https://telnyx.com/resources/how-telnyx-shuts-down-call-fraud-phone-scams
  - Improve fraud protection in Mission Control: https://telnyx.com/resources/how-to-improve-fraud-protection-in-the-mission-control-portal
