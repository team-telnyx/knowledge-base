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

*Part 2 of 4 — see also: [Part 1](telnyx-platform-guide--part-1.md), [Part 3](telnyx-platform-guide--part-3.md), [Part 4](telnyx-platform-guide--part-4.md)*

A comprehensive reference for the Telnyx communications platform, covering account management, SIP trunking, voice calling, phone number provisioning and porting, messaging, webhooks, device configuration, regulatory compliance, and troubleshooting — synthesised from official Telnyx documentation.

## Voice Calls

### Outbound Voice Profiles

Outbound Voice Profiles manage service plans, billing methods, and traffic types for outbound voice. Key settings:

- **International Allowed Destinations** — Whitelist countries/regions for international calling.
- **Channel Limit** — Limit concurrent outbound calls.
- **Max Destination Rate** — Reject calls to destinations exceeding a per-minute rate.
- **Daily Spend Limit Per Connection** — Cap daily outbound spend per connection (resets at 00:00 UTC).
- **Call Recording** — Enable recording for all or specific ANIs, in WAV or MP3, single or double channel.

If multiple SIP connections share the same IP, use a tech prefix or `X-Telnyx-Token` header to uniquely identify each connection for outbound profile assignment.

### Channel Billing

Channel billing lets you pay a flat fee for unlimited inbound minutes instead of per-minute billing. Each channel supports one concurrent inbound call. Channels can be shared across multiple numbers, and you can have more channels than numbers. Channel billing applies only to standard DIDs (not toll-free or international DIDs).

### Audio and Codecs

Telnyx uses SDP (Session Description Protocol) in SIP INVITEs to negotiate media parameters. Supported codecs include G.711 (PCMU/PCMA), G.722, G.729, and telephone-event (DTMF).

- **DTMF:** Works reliably only with G.711. Use outband DTMF (RFC 2833) with any codec.
- **Fax:** Works only with G.711 mu-law and A-law. Use T.38 for best reliability.
- **ptime:** Telnyx specifies 20ms; other values may cause audio quality issues.

### SIP 603+ Carrier Rejections

SIP 603+ is a standardized format for analytics-based call blocking on IP networks (FCC 25-15). It uses status code 603 with reason phrase "Network Blocked" and includes additional metadata such as a redress URL. To reduce rejections:

- Use caller IDs you own (for STIR/SHAKEN A attestation).
- Configure accurate CNAM and register with the [Free Caller Registry](https://freecallerregistry.com/fcr/).
- Maintain healthy traffic patterns (no sudden spikes, low abandoned-call rates).
- Warm up new numbers gradually.

### Spam/Scam Likely

If your number is flagged as "Spam Likely":

1. Register with the FCR at [freecallerregistry.com](https://www.freecallerregistry.com/fcr/).
2. Add CNAM listing in the portal.
3. Allow time for the number to age with healthy calling patterns.
4. Push to the specific carrier flagging calls via [USTelecom contacts](https://www.ustelecom.org/the-industry-traceback-group-itg/call-labeling-and-blocking-points-of-contact/).

SIP 608 indicates call blocking due to suspected fraud by the terminating carrier.

### Abandoned Call Surcharge

If more than 20% of your outbound calls are dropped by the originator during the ringing/setup process, a surcharge of $0.005 per abandoned call applies. Calls to disconnected numbers also count as abandoned. Track abandoned call percentages via the dashboard pie chart or usage reports.

### Toll-Free Calling

You can call toll-free numbers from your Telnyx number. US and Canada share prefixes: 800, 833, 844, 855, 866, 877, 888. International toll-free numbers have country-specific prefixes and dialing rules.

## Phone Numbers

### DID Setup

DIDs (Direct Inward Dial numbers) must be assigned to a SIP connection to receive inbound calls. Assign single DIDs via the pencil icon under the SIP Connection/App column, or use bulk update for multiple numbers.

DID services include: e911, Call Forwarding, Caller ID Name (CNAM), Inbound Call Recording, HD Voice, and Inbound Call Screening.

### Number Types

- **Local** — Area-code-specific numbers.
- **Toll-Free** — Free for callers; available in many countries.
- **National** — Non-geographic numbers within a country.
- **Mobile** — In some countries, mobile numbers support SMS.
- **Shared Cost** — Caller and recipient share the cost (e.g., Australian 1300 numbers).

### Country-Specific DID Requirements

Regulatory requirements vary by country and number type. Examples:

- **Spain:** Local/toll-free require local ID or passport, Spanish DNI/NIE, and proof of address matching the area code. National numbers require local ID/passport and proof of address in Spain. End-users must be physically present in Spain. ~72-hour activation time.
- **Australia:** Local numbers require personal or business identity and an Australian address. Toll-free require worldwide address. Mobile numbers have specific purchaser/service activator requirements.
- **Jamaica:** Requires signed LOI (within 1 month). Toll-free requires company name. Worldwide address accepted.
- **North Macedonia:** Toll-free available; requires business registration certificate or personal ID. Worldwide address accepted.
- **Qatar:** Toll-free available; requires recently signed LOI (within the month). ~72-hour activation.

For most orders, "local" identity means issued by the purchase country. EU customers may use valid passport/national ID from any EU member state.

### Finding GB Numbers

GB local, national, and toll-free numbers are not SMS-supported; only mobile numbers support SMS. Search for local numbers by region/city name.

## Number Porting

### Customer Service Records (CSRs)

A CSR is a copy of how your telephone records appear in your carrier's database. It contains line charges, service location, billing address, features, and more. Having your CSR before starting the porting process is the best way to speed up porting. Most delays are caused by submitting incorrect data.

Carriers match on: business name, zip/postal code of the service address, and account number or BTN/ATN. Canadian carriers are generally not willing to provide CSRs to other carriers.

### Port-In Process

Run a portability check, initiate a porting order, upload supporting documents (via the Documents API for automation), provide end-user information and activation settings, and confirm the order.

### Port-Out Tracking

Port-out requests are tracked in the Mission Control Portal. You can accept or reject requests. Rejections require a valid reason; invalid reasons may result in the port being approved automatically. If a port-out is not acknowledged, it is auto-approved. The gaining carrier has a 10-day grace period after the FOC date to complete the port.

### Country-Specific Porting

- **Portugal:** Requires LOA with local address (wet signature), latest invoice, passport/ID, power of attorney, CVP (portability validation code), TAX ID/VAT, and proof of address. Possible ~3-hour outage during porting.
