---
title: 'Mission Control Portal: Account Setup, Tools, and Support'
summary: A concise guide to creating and configuring your Telnyx Mission Control Portal
  account, organizing users and permissions, enabling security and notifications,
  using dashboards and debugging tools, requesting features or reporting bugs, contacting
  support, and understanding freemium, SSO, and configuration propagation.
sources:
- url: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- url: https://support.telnyx.com/en/articles/1189141-get-started-with-organizations
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
- url: https://support.telnyx.com/en/articles/4277896-notification-settings
- url: https://support.telnyx.com/en/articles/4280610-how-to-setup-your-account-settings
- url: https://support.telnyx.com/en/articles/4283783-feature-requests
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
- url: https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools
- url: https://support.telnyx.com/en/articles/4307059-telnyx-dashboards
- url: https://support.telnyx.com/en/articles/4404409-resources-on-your-account
- url: https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
- url: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
- url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
updated_at: 2026-05-20T14:42:57Z
---

# Mission Control Portal: Account Setup, Tools, and Support

*Part 1 of 2 — see also: [Part 2](mission-control-portal-account-setup-tools-and-support--part-2.md)*

A concise guide to creating and configuring your Telnyx Mission Control Portal account, organizing users and permissions, enabling security and notifications, using dashboards and debugging tools, requesting features or reporting bugs, contacting support, and understanding freemium, SSO, and configuration propagation.

## Sign Up, Verification, and Freemium
- Sign up at https://telnyx.com/sign-up using SSO (Gmail/Microsoft) or the form. A business email is required; some free email providers are blocked. You may be prompted for KYC verification.
- Verify your email (and one-time phone code if requested), then complete the use‑case survey to be guided to relevant tools.
- Currency: new accounts (since Oct 18, 2022) are USD-only.
- Freemium accounts: designed for Telnyx AI products; include $25 in AI credits and one US local number, magic‑link sign‑in (no password needed), and no top‑ups. Non‑AI products are unavailable. Upgrade in the Portal (profile icon → Account Level → Upgrade) via LinkedIn or GitHub. After approval, Freemium becomes a standard trial with all products and a $5 full‑credit replacing the $25 AI credit. Each LinkedIn/GitHub can verify only one Telnyx account. If both methods are rejected, contact Support.

## First-Time Setup Checklist
To make/receive calls and messages after sign-up:
- Level 1 Verification: required to assign connections/profiles. Manage at https://portal.telnyx.com/#/app/account/verifications.
- Connection Setup: create a SIP Connection (Credentials, IP Address, or FQDN authentication) to register to sip.telnyx.com. See connection types at https://support.telnyx.com/en/articles/4245868-sip-connection-types.
- DIDs: buy numbers and assign them to your connection for inbound calling. Number search: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers. Assigning guide: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection.
- Outbound Voice Profile: required for outbound calling; create and assign to your connection. Overview: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles.
- Payments: add a payment method to top up for numbers, calls, and messaging (https://portal.telnyx.com/#/app/billing/payment). Billing overview: https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups.
- Propagation tip: most configuration changes propagate globally within ~1–3 seconds. When creating credentials or updating settings, add a brief delay before first use to avoid transient failures.

## Organizations and Access Control
- An organization groups users under one owner account with a single balance and payment method. Create/manage at https://portal.telnyx.com/#/app/advanced-features/organizations (Level 1 required).
- Invitations: invite users who do not already have a Telnyx account. Limits: 10 invites/hour (incl. deleted/revoked), max 10 open invites, resend up to 5 times with 5‑minute cooldown. Revoking prevents joining via that invite.
- Groups & permissions: assign sub‑members to permission groups (category‑level permissions such as Account, Connections, Numbers, Outbound, Reporting, Porting, Managed Accounts, Networking, Messaging, Organization Management, Wireless, ACL, Call Recording). Users receive the union of permissions across groups. Initial release supports category permissions only.
- Ownership limits: sub‑accounts don’t “own” resources (numbers, connections, outbound profiles) and can’t add their own payment info. Some areas may show limited results during V2 migration; for advanced tasks sub‑members may need to use the organization owner’s API key. Verification and SSO pages are owner‑only.
- Can’t invite an existing Telnyx user; they must work with support to free their email first. To remove access to a joined user, remove them from groups and ask support to block the user if necessary (support@telnyx.com).

## Account Settings and Security
- Account profile: manage personal/org details and redeem promo codes at https://portal.telnyx.com/#/account/general.
- Data storage location: choose once among United States, Germany, Australia to align with regulations (https://telnyx.com/data-privacy).
- Access Control IPs: whitelist SIP signaling/media IPs to prevent security blocks.
- Security: change email/password; enable magic‑link sign‑in; configure Two‑Factor Authentication (TOTP app or SMS); set a Support security paraphrase; reference your Account Verification ID and rotating numeric security codes for support interactions. 2FA guide: https://support.telnyx.com/en/articles/3739748-2fa-totp-setup.

## Single Sign-On (SSO)
- Prerequisite: create an Organization.
- Configure SAML IdP (Auth0, Azure AD, Okta, Google Workspace, OneLogin, LastPass) under My Account → Single Sign‑On in the Portal. Enter IdP details, save, then enable SSO. Users get a 72‑hour grace period to switch from username/password. Sign in via the SSO tab at https://portal.telnyx.com/#/login/sign-in.

## Notifications
- Access at https://portal.telnyx.com/#/app/advanced-features/notifications.
- Low Balance Notifications: set threshold and reminder cadence (emails sent to owner by default).
- Event Notifications: configure channels (Email, SMS, Voice, Webhook) per event using Notification Profiles, Channels, and Settings. Supported events include: new invoice available (email), number order complete (webhook), low available credit, port in/out updates, SIM status change, SIM data usage threshold, and suspicious outbound voice traffic (e.g., bursts to high‑cost destinations or concurrent long‑lived calls).

## Debugging and Troubleshooting Tools
- SIP Call Flow Tool: filter calls (last 3 days) by number, billed duration, direction, tags, and SIP result code; view ladder diagrams. Response codes: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes.
- Programmatic Voice (Call Control/TeXML/Fax) Flow: search via Call Session ID and inspect webhooks per event.
- Web Dialer: place/receive test calls without a PBX. Requires a Credentials Connection and a DID assigned to it; optional caller ID name for testing.
- Webhook Deliveries: search by delivery ID, filter by time/status/name (e.g., call.initiated), inspect payloads, and analyze failures.
- QoS Reports: with RTCP capture enabled on the SIP Connection, view MOS (1–4.5), interarrival jitter, packets lost, and packet counts per RTP stream in a timeline.

## Dashboards and Analytics
- Access the Dashboard at https://portal.telnyx.com/#/reports/dashboard (voice and SMS trends). Time ranges: 24h, 7d, 30d.
- Voice: number of calls, connection rate, max concurrent calls, outbound peak CPS, peak inbound concurrent channels, abandoned calls percentage, and live active calls (in/outbound). Conversational calls only (no HVSD at this time).
- Messaging: number of messages; usage/spend by country (toggle countries in legend). Messaging dashboard: https://portal.telnyx.com/#/messaging/reports/dashboard.

## Feature Requests and Bug Reports
- Feature requests: in the Portal, click the ? icon → Feature Request. Submit your idea, importance, and email. You can view planned/underway/consideration items and indicate impact.
- Bug reports: email support@telnyx.com and include clear reproduction steps, screenshots/videos, console/network logs (save HAR for backend issues). The Portal UI sits atop the public API; browser dev tools are invaluable.
- Vulnerability Disclosure: security reports to security@telnyx.com (scope: Telnyx‑owned apps/APIs/infrastructure). Include description, reproduction steps, PoC, and demonstrated impact. Follow rules (no accessing others’ data, no DoS, test only your accounts, embargo until remediation). Safe harbor applies; rewards may be offered at Telnyx’s discretion.
