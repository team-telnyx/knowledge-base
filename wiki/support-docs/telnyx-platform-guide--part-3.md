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

*Part 3 of 4 — see also: [Part 1](telnyx-platform-guide--part-1.md), [Part 2](telnyx-platform-guide--part-2.md), [Part 4](telnyx-platform-guide--part-4.md)*

A comprehensive reference for the Telnyx communications platform, covering account management, SIP trunking, voice calling, phone number provisioning and porting, messaging, webhooks, device configuration, regulatory compliance, and troubleshooting — synthesised from official Telnyx documentation.

## Messaging

### SMS Traffic Types

- **A2P (Application-to-Person)** — Used for domestic messaging and one-way campaigns. Does not support international messaging.
- **P2P (Person-to-Person)** — Ideal for two-way communication; supports international messaging.

### Alphanumeric Sender IDs

Alphanumeric Sender ID handling varies by destination. Some countries maintain the ID without registration, some require registration, and some overwrite it to ensure delivery. Registration requires Level 2 account verification. Contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) for registration requests.

### Country-Specific SMS Guidelines

Guidelines vary significantly:

- **US/Canada (10DLC):** Must register brands and campaigns with the Campaign Registry.
- **Philippines:** Alphanumeric registration required; generic alpha Sender IDs not allowed.
- **Israel:** No registration required; religious, gambling, political, or adult traffic prohibited.
- **Mauritius:** Supported except toward Orange Mauritius; religious, political, or adult traffic prohibited.
- **South Africa:** All alphanumeric Sender IDs overwritten to random local long code.
- **Cuba:** Registration required; up to 6 months provisioning time; mixed letter-number Sender IDs not supported.
- **Bhutan, Lebanon, Libya, Myanmar, Uzbekistan:** Registration required; messages from unregistered IDs rejected.

### MMS

MMS is currently supported within the US and Canada only. Key details:

- Supported file types: text/plain, text/vcard, image/jpeg, image/png, image/gif, video/3gpp, video/mp4.
- Maximum single attachment: 1 MB (ideally 900 KB for encoding overhead).
- Maximum total message: 1 MB with up to 10 media URLs.
- **MMS Fallback** — Automatically converts MMS to SMS with media URLs listed in the body if the destination doesn't support MMS.
- **MMS Transcoding** — Resizes images/videos to meet carrier size requirements; animated GIFs are not resized.
- Toll-free MMS rate limit: 1,200 messages/minute.
- Account-wide messaging rate: 15 messages/second.
- Media files cached for 1 hour; change the URL to invalidate cache.
- To secure media, whitelist IPs 192.76.120.192 and 192.76.120.193.

### Acceptable Use Policy

Prohibited content and behaviors include:

- Sending unsolicited messages (valid opt-in required; purchased lists don't qualify).
- Inappropriate content (sexual, firearms, alcohol/tobacco/drugs, high-risk financial, gambling, etc.).
- Not honouring unsubscribe requests (STOP/UNSUBSCRIBE; must remove within 24 hours).
- High-frequency messaging (no more than 10 messages to a recipient in 24 hours without two-way communication or explicit opt-in).
- Misrepresenting identity (spoofing).
- Fraud or phishing.

Customers must comply with CAN-SPAM (US), CASL (Canada), and CTIA Messaging Principles.

## Webhooks

Webhooks deliver real-time event data. Requirements:

- A publicly accessible HTTP server (HTTPS recommended).
- Return a `2xx` status code to acknowledge receipt.
- Timeout threshold: 2,000 milliseconds; failed deliveries are retried once.
- Configure a failover URL as backup.

### Webhook Signing

Telnyx signs webhook events using public key encryption (API v2). The public key is available in the portal under **Account Settings → Keys & Credentials → Public Key**. Verify signatures using the `telnyx-signature-ed25519` and `telnyx-timestamp` headers.

### Rotating the Public Key

1. Create an inactive key: `POST /v2/inactive_key`
2. Activate it: `POST /v2/inactive_key/{id}/activate`

Only one inactive key can exist per organization. Activation takes up to 60 minutes to propagate; both old and new keys may be active during this period.

### CA Error

If webhooks fail with a certificate authority error and traffic goes to the failover URL, your server's SSL certificate must be signed by a known CA, or use HTTP instead of HTTPS.

## Device & PBX Configuration

### Grandstream UMC6202 (IP Auth)

1. Log into the web UI (default password: `admin` or printed on the unit sticker).
2. Add a SIP trunk pointing to `192.76.120.10`.
3. Create inbound routes with patterns directing to extensions.
4. Create outbound routes with privilege levels matching your Telnyx outbound profile.
5. Configure outbound caller ID (capitals, no special characters, max 15 characters for Canadian providers).

### Yealink T Series (Credentials)

Configure via keypad or web interface. Enter the Telnyx credentials-based connection username and password. Set the SIP server to `sip.telnyx.com`.

### Polycom VVX 300-series (IP Auth)

1. Access the web UI (default password: `456`).
2. Configure NTP settings.
3. Under Lines, set the server address to your Telnyx SIP server, port 5060, UDP transport.

### Ubiquiti UniFi Talk (Credentials Auth)

1. Add a third-party SIP provider in Talk settings with custom fields: proxy, realm, username, password, register, sip_cid_type, retry_seconds, expire-seconds.
2. Import DIDs in E.164 format (with `+` prefix).
3. Add IP address range `192.76.120.10/32`.
4. Assign numbers to users.

### NCH Express Talk

Configure via **File → Options → Lines**: set server to `sip.telnyx.com`, enter SIP account credentials.

## SIM Cards

1. Order a SIM from Telnyx and register it at the [SIM registration page](https://portal.telnyx.com/#/app/wireless/register-sims).
2. Insert into device and configure APN: Name `Telnyx`, APN `data00.telnyx`.
3. Enable data roaming.
4. Reboot the device if needed.

## Billing & Pricing

### Rate Sheets and LRN

Call rates are based on the Location Routing Number (LRN), not always the dialled number. Use the Number Lookup tool in the portal to find a number's LRN prefix and determine the correct rate.

### Global Conversational Rate Deck

Rate changes affect origination type classifications (Local, EEA, Non-surcharged, Surcharged), prefixes, and pricing. Notifications are sent 3 days before changes take effect.

- **Local origination** — Call to country X from a number of country X purchased on Telnyx.
- **EEA origination** — Call to EEA country from another EEA number.
- **Non-surcharged** — Call to country X from a number of a predefined country Z.
- **Surcharged** — None of the above apply.

### Canadian LRN Data

Canadian LRN data requires regulatory approval from the Canadian Local Number Portability Consortium (CNLPC). Annual fee ~$2,000 USD. Telnyx applies a minimum lookup requirement (~$225/month) on a case-by-case basis.

## Regulatory Compliance

### Texas Mini-TCPA (SB 140)

Effective September 1, 2025, Texas SB 140 expands the state's telemarketing framework to include text messages:

- Text solicitations are now regulated the same as telemarketing calls.
- Quiet hours apply to texts: Mon–Sat 9am–9pm, Sunday 12pm–9pm (recipient's local time).
- Businesses based in Texas or marketing to Texas residents must register with the Texas Secretary of State ($200 filing fee + $10,000 security deposit).
- Failure to register: civil penalties up to $5,000 per violation.
- Expanded private right of action for violations.
- Multiple exemptions apply (former customers, securities brokers, publicly traded corporations, licensed insurance, banks, utilities, newspapers, schools, nonprofits, etc.).

### FCC Requirements

- **SIP 603+** — Standardized notification for analytics-based call blocking.
- **Do-Not-Originate (DNO)** — Requirements effective December 15, 2025.
- **Reassigned Numbers Database** — Tracks permanently disconnected numbers.
- **STIR/SHAKEN** — Telnyx implements STIR/SHAKEN; using numbers you own results in A attestation.
