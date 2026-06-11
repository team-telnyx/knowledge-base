---
title: Telnyx Platform Guide
summary: A comprehensive reference for the Telnyx communications platform, covering
  account management, SIP trunking, voice calling, phone number provisioning and porting,
  messaging, webhooks, device configuration, regulatory compliance, and troubleshooting
  — synthesised from official Telnyx documentation.
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
- url: https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier
- url: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
- url: https://support.telnyx.com/en/articles/1130703-can-i-call-toll-free-with-my-telnyx-number
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
- url: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- url: https://support.telnyx.com/en/articles/1311073-spain-did-requirements
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support
- url: https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections
- url: https://support.telnyx.com/en/articles/2906030-port-out-tracking
- url: https://support.telnyx.com/en/articles/2950523-grandstream-ip-auth-setup
- url: https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
- url: https://support.telnyx.com/en/articles/3269600-how-to-set-up-a-telnyx-sim-card
- url: https://support.telnyx.com/en/articles/3505912-australia-did-requirements
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
- url: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
- url: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
- url: https://support.telnyx.com/en/articles/4353862-creating-postman-collection-from-openapi
- url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
- url: https://support.telnyx.com/en/articles/4951492-managed-accounts
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
- url: https://support.telnyx.com/en/articles/5120062-portugal-number-porting
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
- url: https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup
- url: https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx
- url: https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx
- url: https://support.telnyx.com/en/articles/5386351-automating-ports-with-programmatic-api
- url: https://support.telnyx.com/en/articles/5466658-jamaica-did-requirements
- url: https://support.telnyx.com/en/articles/5466851-north-macedonia-did-requirements
- url: https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
- url: https://support.telnyx.com/en/articles/5807457-nch-express-talk
- url: https://support.telnyx.com/en/articles/5820047-find-gb-numbers-on-telnyx-portal
- url: https://support.telnyx.com/en/articles/6122586-ubiquiti-trunk-unifi-talk-auth
- url: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id
- url: https://support.telnyx.com/en/articles/6531682-philippines-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545167-poland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6545173-south-africa-sms-guidelines
- url: https://support.telnyx.com/en/articles/6592454-american-samoa-sms-guidelines
- url: https://support.telnyx.com/en/articles/6596425-bhutan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6661387-cook-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6665126-cuba-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670750-falkland-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670819-french-polynesia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670896-grenada-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674331-haiti-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674453-israel-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674794-kyrgyzstan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674807-lebanon-sms-guidelines
- url: https://support.telnyx.com/en/articles/6674989-libya-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675252-malta-sms-guidelines
- url: https://support.telnyx.com/en/articles/6675683-martinique-sms-guidelines
- url: https://support.telnyx.com/en/articles/6677919-mauritius-sms-guidelines
- url: https://support.telnyx.com/en/articles/6678010-myanmar-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679129-norfolk-island-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679378-reunion-sms-guidelines
- url: https://support.telnyx.com/en/articles/6679451-samoa-sms-guidelines
- url: https://support.telnyx.com/en/articles/6680225-sudan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683365-tonga-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683429-tuvalu-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683454-uzbekistan-sms-guidelines
- url: https://support.telnyx.com/en/articles/6683459-vanuatu-sms-guidelines
- url: https://support.telnyx.com/en/articles/6837118-elevateai-proof-of-concept-setup-guide
- url: https://support.telnyx.com/en/articles/6974437-updates-to-global-conversational-rate-deck
- url: https://support.telnyx.com/en/articles/7885470-chiro8000-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
- url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
- url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
- url: https://support.telnyx.com/en/articles/8520014-qatar-did-requirements
- url: https://support.telnyx.com/en/collections/12044103-regulatory
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
- url: https://support.telnyx.com/en/collections/133103-telnyx-sms-guide
- url: https://support.telnyx.com/en/collections/19623087-ai-assistant
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
- url: https://support.telnyx.com/en/collections/3968237-telnyx-sip-trunking-configurations
- url: https://support.telnyx.com/en/collections/3968260-telnyx-identity-verification-tools
updated_at: 2026-06-11T11:48:37Z
---

# Telnyx Platform Guide

*Part 1 of 4 — see also: [Part 2](telnyx-platform-guide--part-2.md), [Part 3](telnyx-platform-guide--part-3.md), [Part 4](telnyx-platform-guide--part-4.md)*

A comprehensive reference for the Telnyx communications platform, covering account management, SIP trunking, voice calling, phone number provisioning and porting, messaging, webhooks, device configuration, regulatory compliance, and troubleshooting — synthesised from official Telnyx documentation.

## Account Setup & Access

### API Keys

Telnyx uses API keys (v2) and API tokens (v1) to authenticate requests. Create and manage them from the Mission Control Portal under **Account Settings → API Keys**.

- **API v2 keys** are used as bearer tokens. They are visible only at creation time, so store them securely. You can set expiration dates, temporarily disable keys, and add up to 10 tags per key.
- **API v1 tokens** require two headers in requests: `x-api-user` (your account email) and `x-api-token` (your token).

### Managed Accounts

Managed Accounts are sub-accounts created from a manager account, allowing advanced control over pricing, reporting, administration, and billing. They are available on Starter, Growth, and Enterprise commit plans (not Pay-as-you-go). Key features:

- Managed Accounts inherit pricing from the manager account; pricing is hidden from the sub-account.
- Each managed account has its own balance, payment methods, and invoices.
- Rollup Billing writes spend records to the manager account.
- The default limit is 1,000 managed sub-accounts per manager account.
- Existing Telnyx accounts cannot be migrated under a manager account.

Managed Accounts are for managing customer accounts, not for separating production/staging environments. For environment separation, create two entirely separate Telnyx accounts.

### Addresses

The Addresses section (under **Numbers → Compliance → Emergency Addresses**) stores addresses used for E911 and regulatory requirements. Addresses can be added manually or via built-in search. Deleting an address that is associated with a DID for E911 will invalidate that DID's E911 service.

### Access Control List

The legacy Access Control List (ACL) feature has been deprecated and is no longer active.

## Single Sign-On (SAML)

Telnyx supports SAML-based SSO with several identity providers. The general process involves: creating an SSO app in your IdP, obtaining an Organization in the Telnyx portal, configuring the Single Sign-On settings, and enabling SSO.

Supported providers include:

- **OneLogin** — Uses the SAML Test Connector (Advanced). Provide the IdP Metadata URL.
- **Okta** — Uses the SAML Service Provider app. After importing IdP settings, manually fill in the IdP Entity ID field.
- **LastPass** — Add an unlisted SSO app. Manually enter configuration values (IdP Certificate Fingerprint, Entity ID, SSO Target URL).
- **Azure AD** — Use the Microsoft Extra SAML Toolkit enterprise application. After importing, manually enter the Thumbprint in the IdP Certificate Fingerprint field.
- **Auth0** — Enable the SAML2 Web App addon. Download the IdP metadata and configure the application callback URL.
- **GSuite** — Add a custom SAML app. Manually enter the SSO URL, Entity ID, and SHA-256 fingerprint.

Once SSO is enabled, users have 72 hours to continue using username/password before SSO becomes mandatory.

## IP Whitelisting & Network Configuration

### Signaling and Media IPs

If your network uses a firewall or ACL, whitelist both Telnyx's SIP signaling and media IP addresses. For the most up-to-date lists, visit [sip.telnyx.com](https://sip.telnyx.com).

**Region-Specific SIP FQDNs and IPs:**

| Region | FQDN | Primary IP | Secondary IP |
|--------|------|------------|--------------|
| US | sip.telnyx.com | 192.76.120.10 | 64.16.250.10 |
| Europe | sip.telnyx.eu | 185.246.41.140 | 185.246.41.141 |
| Australia | sip.telnyx.com.au | 103.115.244.145 | 103.115.244.146 |
| Canada | sip.telnyx.ca | 192.76.120.31 | 64.16.250.13 |

**Media IP Ranges:**

- 36.255.198.128/25
- 50.114.136.128/25
- 50.114.144.0/21
- 64.16.226.0/24
- 64.16.227.0/24
- 64.16.228.0/24
- 64.16.229.0/24
- 64.16.230.0/24
- 64.16.248.0/24
- 64.16.249.0/24
- 103.115.244.128/25
- 185.246.41.128/25

**Network IP Assignments by Region:**

- **AMER:** Main pools 192.76.120.128/26 & 192.76.120.192/27 (CH1, DC2, SV1, TR1)
- **EMEA:** Main pool 185.246.41.0/26 (LD6, FR5, AM6)
- **APAC:** Main pool 103.115.244.0/26 (SY1, SG1)

### Webhook IPs

Webhooks (including WebSocket stream connections) are delivered from regional IPs:

- **US:** CH1 192.76.120.128/29, DC2 192.76.120.136/29, SV1 192.76.120.144/29
- **Europe:** LD6 185.246.41.0/29, FR5 185.246.41.8/29, AM6 185.246.41.16/29
- **APAC:** SY1 103.115.244.0/29, SG1 103.115.244.8/29

## SIP Connections & Trunking

### Connection Types

Telnyx offers several SIP connection types:

- **IP-based** — Authenticated by source IP address.
- **FQDN** — Authenticated by resolved hostname. Your PBX registers to Telnyx.
- **Credentials** — Authenticated by username/password.
- **UAC (User Agent Client)** — Telnyx registers to your PBX as an extension (beta). The registration direction is reversed compared to traditional connections: Telnyx is the client (UAC) and your PBX is the server (UAS).

### UAC Connections (SIP Attach)

UAC Connections let Telnyx register as a SIP endpoint on your existing PBX. This gives Telnyx resources (AI Assistants, Call Control Applications) native PBX presence, reducing latency and cost.

Key configuration fields:

- **SIP Subdomain** (auto-generated) — Used for outbound calls from Telnyx to your PBX.
- **Internal SIP URI** — Receives inbound calls from your PBX; typically points to an AI Assistant or Call Control Application.
- **External UAC settings** — Username, password, proxy, transport, and expiration for registering to your PBX.

For UAC registrations, Telnyx sends REGISTER requests from IP **192.76.120.14**. Allowlist this IP on your PBX/firewall.

Check the Registration status section on the connection for registration state (registered, trying, failed, unregistering, connection_disabled, unknown).

### AnchorSite Settings

The AnchorSite setting determines which media server Telnyx uses to route media packets. Options:

- **Latency** (default) — Telnyx proactively pings your connection to determine the optimal Point of Presence.
- **Manual selection** — Choose a specific PoP. Note that if you don't whitelist all media IPs, failover during maintenance or outages may be limited.

For IP/FQDN connections, whitelist media IPs so latency checks work. For credential connections, include the SIP username in the contact header of the first INVITE (or add `X-Telnyx-Username: <username>`).

### FIPS Support

Telnyx supports FIPS-140-2/FIPS-140-3 on its SIP proxy infrastructure via OpenSSL FIPS mode. This restricts TLS to 1.2+, prohibits CHACHA20-POLY1305, and enforces minimum key-length requirements. Note that SIP Digest authentication (which uses MD5) is not FIPS-compliant; customers with formal FIPS requirements must validate their end-to-end configuration.

### Custom SIP Headers for FreePBX

**P-Charge-Info:** Add a billing number to SIP INVITEs. Edit `/etc/asterisk/extensions_custom.conf` and add a `macro-dialout-trunk-predial-hook` macro that calls `func-set-sipheader` with the DID in E.164 format.

**X-Telnyx-Token:** Add token-based authentication. Use the same macro pattern to inject the `X-Telnyx-Token` header with the token from the Mission Control Portal.
