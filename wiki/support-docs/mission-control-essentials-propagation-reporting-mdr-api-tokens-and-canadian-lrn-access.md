---
title: 'Mission Control Essentials: Propagation, Reporting, MDR, API Tokens, and Canadian
  LRN Access'
summary: A practical guide to operating in the Telnyx Mission Control Portal and API,
  covering configuration propagation timing, creating and securing API tokens, generating
  reports (including SMS MDR fundamentals), and the process and requirements for accessing
  Canadian LRN data.
sources:
- url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
- url: https://support.telnyx.com/en/articles/1130624-how-do-i-create-an-api-v1-token
- url: https://support.telnyx.com/en/articles/1130708-how-to-download-reports-at-telnyx
- url: https://support.telnyx.com/en/articles/1130611-understand-telnyx-sms-mdr-report-log
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
updated_at: 2026-05-14T11:41:00Z
---

# Mission Control Essentials: Propagation, Reporting, MDR, API Tokens, and Canadian LRN Access

A practical guide to operating in the Telnyx Mission Control Portal and API, covering configuration propagation timing, creating and securing API tokens, generating reports (including SMS MDR fundamentals), and the process and requirements for accessing Canadian LRN data.

## Configuration propagation across Mission Control and API
Telnyx runs a globally distributed infrastructure, so configuration updates made in the Mission Control Portal or via the API must propagate to all instances before they take full effect.

- Typical timing: minimum ~1 second, average ~1.5 seconds, maximum ~3 seconds
- Applies to all configuration updates, including: on-demand SIP credentials, call control settings, connection configurations, messaging profiles, and number settings
- Design guidance: pre-provision resources when possible and add a short delay before first use. For example, if you create new SIP credentials and register or place calls immediately, authentication may fail until propagation completes.

## API tokens: V2 recommended; creating a legacy V1 token when needed
- Use API V2 for new integrations. See: Create and Manage API V2 Keys (https://developers.telnyx.com/development/api-fundamentals/create-api-keys)
- API V1 tokens are only needed for legacy services such as reporting and debugging; use V2 for all other requests.

How to create an API V1 token in Mission Control:
1) Log in at https://portal.telnyx.com
2) Open your Profile icon > API Keys
3) Select API V1 Tokens > Create API Token > Create API v1 Token
4) Name the token and confirm Create API Token

Security notes:
- The full token is shown only once at creation. If lost, generate a new token.
- Store tokens in a secure password manager or secrets vault to prevent accidental exposure.

## Generating and filtering reports in Mission Control
Available report types include: Calls, Messaging, Voice API, Fax API, Wireless, WebRTC, and Real-Time Transcriptions.

How to generate report logs:
- Log in to the portal and go to Reporting
- Choose a Report Type and request a report for the desired time frame

Filters and scoping options:
- Time frame, CLI (originating number), CLD (destination number)
- Tags (set on numbers for inbound, or outbound voice profiles for outbound)
- Billing Groups
- Managed accounts: select which managed account to report on
- Record types: Completed, Incomplete, Errors
- Call type: Inbound, Outbound
- Scope by specific connection, application, or messaging profile

Usage reports:
- In Reporting, click Usage Reports to generate account usage summaries
- For a step-by-step guide, see Reporting: Usage Reports (https://support.telnyx.com/en/articles/4425016-reporting-usage-reports)

## Understanding SMS MDRs (Message Detail Records)
What is an MDR:
- For every sent or received message, Telnyx writes an MDR you can generate in the portal under Reports > Reporting.

Structure and retention:
- MDRs are stored as JSON objects and include an embedded body object.
- For privacy, a message’s body text is retained for up to 10 days; after that window, hash fields can be used to identify messages.

Status and delivery:
- Sent and received messages each have defined status value sets.
- The delivery_status field provides additional details about delivery confirmation (outbound) or delivery attempts (inbound).

Encoding (coding field):
- The coding field is an integer indicating the message encoding.
- Encoding is chosen based on message characters: GSM 7-bit when possible; otherwise UTF-16.

Message parts and billing:
- Long messages are split into parts; part size depends on encoding.
- Outbound messages have a maximum size of 10 parts.
- Billing and rate limiting apply per message part.
- rate = price per message part + carrier fee per part; cost = rate × number of parts.

## Accessing Canadian LRN data
Canadian LRN (Local Routing Number) data is regulated and requires approvals and minimum usage commitments.

Requirements and process:
1) Regulatory approval: Apply for Non-Member Access with the Canadian Local Number Portability Consortium (CNLPC). See https://clnpc.ca/non-member-access/ (available to contracted customers).
2) Associated costs: An annual fee of approximately $2,000 USD is paid directly to the CNLPC. Telnyx Number Lookup standard pricing applies for CA LRN lookups (no special pricing).
3) Usage requirements: Access is granted case-by-case. Telnyx applies a minimum monthly LRN lookup spend of about $225 (≈150,000 lookups at $0.0015 base price) to cover facilitation costs.

Activation:
- After meeting the above, provide proof of CNLPC approval to your Telnyx CSM or contact support@telnyx.com.

## Operational tips and best practices
- Account for propagation: Add a brief delay after configuration changes before first use; pre-create SIP credentials and update settings ahead of cutovers.
- Secure credentials: Prefer API V2; if you must use V1, store the token securely and plan for rotation since it’s only shown once.
- Plan reporting: Use filters (CLI/CLD, tags, billing groups, managed accounts) to focus reports and speed analysis; schedule reporting around operational needs.
- Preserve message context: If you need message bodies for audits, export within 10 days; rely on hashes thereafter.
- Control messaging costs: Mind encoding and length to minimize parts; remember outbound messages cap at 10 parts; billing and rate limits apply per part.
- LRN access readiness: Secure CNLPC approval early, budget for fees and minimum monthly spend, and coordinate activation with your CSM.
