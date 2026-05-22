---
title: Telnyx Reporting, Webhooks, Encryption, and Tools
summary: A practical guide to generating and downloading reports in the Mission Control
  Portal, using v2 Usage Reports and On‑Demand analysis, understanding Monthly Charges,
  configuring reliable webhooks with signature rotation and troubleshooting, enabling
  SIP TLS/SRTP encryption, importing the Telnyx API into Postman, and checking real‑time
  service status.
sources:
- url: https://support.telnyx.com/en/articles/1130708-how-to-download-reports-at-telnyx
  content_hash: 0f35c9bf7083fb546b98190052a688b6f6f87889e2752bb962cccb148de4e39a
- url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
  content_hash: 00f11df1724e443c1d6e7373b3f3ea724f99b62d392479c8efe459e89b888938
- url: https://support.telnyx.com/en/articles/4305547-reporting-overview
  content_hash: a25611b1e1a462919feee8456354bd75997205c7f499fa034b97ed9dc8649e9e
- url: https://support.telnyx.com/en/articles/4424926-reporting-detail-requests
  content_hash: eff252a706a539dfebfac4cead414df4c6e027496577b8a63a9b1f09e4c7e586
- url: https://support.telnyx.com/en/articles/4425016-reporting-usage-reports
  content_hash: 61dbc45e36d200ef1ff93ab93d36dbbb87396cdc8c72704724a4d903011a4d9c
- url: https://support.telnyx.com/en/articles/4425088-reporting-monthly-charges
  content_hash: 263f50d473bf7199f9f6067e3667a3587d6615322797506af86d17a485b276cc
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
  content_hash: e33247a2589d864d204e0854667008828740be9dd634ffedb02a0308f37963aa
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
  content_hash: 671427431321f3803e233727f6691a2dd69040e2c643b73f6fc09162faeb19f9
- url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
  content_hash: 33f2a911f356445a83cfd50c5edc338ef9247777c8cbf29a8763ed2b29a74989
- url: https://support.telnyx.com/en/articles/4353862-creating-postman-collection-from-openapi
  content_hash: 78e45bf4324642352293f1e27e1ae3a1012520bb40702147e9477a48de23b694
- url: https://support.telnyx.com/en/articles/6707731-telnyx-status-page
  content_hash: 87d9aab8a08bc6109a8b1bc46f2a0a73ecf006958996406773a3240e864dd672
updated_at: 2026-05-20T15:40:32Z
---

# Telnyx Reporting, Webhooks, Encryption, and Tools

A practical guide to generating and downloading reports in the Mission Control Portal, using v2 Usage Reports and On‑Demand analysis, understanding Monthly Charges, configuring reliable webhooks with signature rotation and troubleshooting, enabling SIP TLS/SRTP encryption, importing the Telnyx API into Postman, and checking real‑time service status.

## Find and Navigate the Reporting Area
- Sign in to the Mission Control Portal and open Reporting: https://portal.telnyx.com/
- In Reporting you’ll find:
  - Detail Records
  - Usage Reports
  - Monthly Charges
  - Message Deliverability
  - Outbound Declined Calls
  - On-Demand Reports

## Detail Records (CDR/MDR and more)
Generate granular logs for these products: Calls, Messaging, Voice API (Call Control), Fax API, Wireless, WebRTC, and Real-Time Transcriptions.
- Where: Reporting > Detail Records (https://portal.telnyx.com/#/reporting/detailed-records)
- Key options:
  - Report Type: Calls, Messaging, Call Control, Fax API, Wireless, WebRTC, Real-Time Transcriptions
  - Time range: Start and End time (start required; end defaults to now)
  - Filters: CLD (destination), CLI (originating), Tags (on numbers or profiles), Billing Groups; choose specific Connections/Applications/Messaging Profiles
  - Record Types: Completed, Incomplete, Errors, or All
  - Call/Message Direction: Inbound, Outbound, or Both
  - Metadata: choose up to dozens of columns; all included by default
- Generate and download:
  - Click Generate Detailed Report; monitor status under Download Report
  - If a link shows Expired, click the refresh icon to regenerate
  - View created time, covered time range, and applied filters
- Tips:
  - Managed accounts: pick the specific managed account before generating

## Usage Reports (Aggregated v2)
Analyze aggregated usage across products with flexible dimensions, metrics, and filters.
- Where: Reporting > Usage Reports (https://portal.telnyx.com/#/app/reporting/usage-reports)
- Scope: Calls, Messaging, Telco Data, Real-Time Transcription, and more (e.g., SIP Trunking, Call Control, Media Storage)
- Timespan:
  - Custom: set explicit start/end
  - Month: pick a calendar month
- Advanced filters:
  - Dimensions, Metrics, and Filters to group and slice results
  - Breakdowns for calls by direction, product, country, and connection
- Messaging note: usage is calculated per message part; detail CSVs include a parts column for each message

## Monthly Charges (MRC)
Review billed monthly recurring charges and account movements.
- Where: Reporting > Monthly Charges (https://portal.telnyx.com/#/app/reporting/monthly-charges)
- Billing cycle: MRCs post at the start of each month and deduct from your balance
- Views:
  - Summary: rollup of the month
  - Breakdown by number: DID-specific items (e.g., DID MRC, CNAM MRC)
- Sections you’ll see after generating:
  - Numbers, Features, Additional Services, Credit (funds added), Ledger Adjustments, Ending Balance
- Number types commonly billed:
  - Local DIDs, Vanity DIDs, Toll-Free DIDs (Telnyx is an independent RespOrg)
- Example number features that may incur charges:
  - Bundle Pricing, Channels, CNAM, Emergency Services, HD Voice, Inbound Call Screening, SMS
- Additional services examples:
  - Port-Outs (incl. vanity), Unregistered E911 Calls
- Credits and adjustments:
  - Payments, Promo Redemptions, Referral Credit, Ledger Adjustments (refunds)

## Message Deliverability and Outbound Reputation
- Message Deliverability dashboard: filter by Direction (Inbound/Outbound), Type (SMS/MMS), and Product (Toll-Free, Short Code, Long Code, Alphanumeric) to assess profile health
- Outbound Declined Calls: view numbers receiving 603/608 declines for reputation management

## On-Demand Reports (Natural Language)
Create ad-hoc charts from your v2 Usage Report data by describing what you need in plain English; save and re-run for relative timespans.
- Examples: “Daily wireless spend for the last 10 days”, “Number of messages by direction as a pie chart”, “Weekly total calls in February”
- Where: Reporting > On-Demand Reports in the Portal

## Webhooks: Configuration, Delivery, and Security
Set up real-time notifications for messaging, voice, and fax.
- Configure webhook URLs on SIP Connections or Applications (voice, fax, messaging). For messaging, you can also provide webhooks in the send request body; precedence is: request body > profile > no webhook
- Requirements and networking:
  - Expose a publicly reachable HTTP(S) endpoint; HTTPS strongly recommended
  - Webhooks originate from the anchorsite region for your traffic; consider anchorsite settings and whitelist Telnyx IP ranges if you use ACLs/firewalls
- Delivery behavior:
  - Telnyx sends status updates (e.g., message.received, message.finalized) according to the URL hierarchy above
  - MMS media URLs are accessible for 30 days after receipt
- Responding and retries:
  - Acknowledge with 2xx quickly; 3xx and other codes are treated as failures
  - If no 2xx within ~2000 ms, Telnyx retries once per URL
  - Use a failover webhook URL for resilience
  - Debug in the Portal: Debugging > Webhook; timeouts display response code 0; inspect request/response details
- Signature verification (API v2):
  - Telnyx signs events using a private key; verify with the account’s public key (Portal: Account Settings > Keys & Credentials > Public Key)
  - Headers include telnyx-signature-ed25519 and telnyx-timestamp; the signature is computed over a string composed of timestamp, a pipe (|), and the JSON payload, then Base64-encoded before signing
  - Use official SDK helpers where available to verify signatures
- Rotating the webhook signing public key:
  - Create a new inactive key: POST https://api.telnyx.com/v2/inactive_key (auth required)
  - Activate it when ready: POST https://api.telnyx.com/v2/inactive_key/{id}/activate
  - Notes: only one inactive key per organization; activation can take up to ~60 minutes, during which both keys may be accepted
- Troubleshooting CA errors:
  - If primary webhook fails with “certificate authority isn’t recognized” and traffic falls back to failover: ensure your server certificate is signed by a recognized CA, or temporarily use HTTP (HTTPS recommended once CA is correct)

## SIP Encryption (TLS/SRTP)
Secure SIP signaling and RTP media when your equipment supports it.
- Defaults: calls are not encrypted by default
- Outbound calls: configure your device to use TLS (signaling) and SRTP (media); no additional Portal changes required
- Inbound calls: enable TLS and SRTP on the Connection in the Portal (Real-Time Communications > Voice > SIP Trunking > Connection settings). For IP/FQDN connections, enable inbound TLS and SRTP there
- Network path: Telnyx’s private network helps minimize public internet exposure by carrying media over Telnyx fiber wherever possible
- More details: TLS/SRTP feature overview at Telnyx docs

## Using Postman with Telnyx API v2
Quickly load the full API into Postman using the OpenAPI spec.
- Steps:
  1) Go to the Telnyx OpenAPI repository: https://github.com/team-telnyx/openapi/tree/master/openapi
  2) In Postman, Import via the raw JSON URL (or download and import)
  3) Add your API token to the collection’s Authorization
  4) Start calling endpoints

## Service Status and Notifications
- Check live incidents and maintenance at https://status.telnyx.com/
- Subscribe to updates via your preferred channels

## Handy Portal Shortcuts
- Detail Records: https://portal.telnyx.com/#/reporting/detailed-records
- Usage Reports: https://portal.telnyx.com/#/app/reporting/usage-reports
- Monthly Charges: https://portal.telnyx.com/#/app/reporting/monthly-charges
- Connections (enable TLS/SRTP): https://portal.telnyx.com/#/voice/connections
- Debugging > Webhook: https://portal.telnyx.com/#/app/debugging/webhook?enableAlerts=true
- Account Public Key: https://portal.telnyx.com/#/app/account/public-key
