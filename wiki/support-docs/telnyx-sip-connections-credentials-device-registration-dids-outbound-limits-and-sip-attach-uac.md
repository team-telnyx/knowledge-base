---
title: 'Telnyx SIP Connections: Credentials, Device Registration, DIDs, Outbound Limits,
  and SIP Attach (UAC)'
summary: 'A practical guide to managing Telnyx SIP connections in Mission Control:
  set and find credentials, understand device registration behavior, map DIDs for
  inbound service, manage concurrent outbound call limits, and configure SIP Attach
  using a UAC connection to register Telnyx to your PBX.'
sources:
- url: https://support.telnyx.com/en/articles/1130713-what-is-my-sip-account-connection-password
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
updated_at: 2026-05-14T11:43:00Z
---

# Telnyx SIP Connections: Credentials, Device Registration, DIDs, Outbound Limits, and SIP Attach (UAC)

A practical guide to managing Telnyx SIP connections in Mission Control: set and find credentials, understand device registration behavior, map DIDs for inbound service, manage concurrent outbound call limits, and configure SIP Attach using a UAC connection to register Telnyx to your PBX.

## Create and manage SIP credentials

When creating a SIP connection in Mission Control, choose credentials-based authentication to use a username/password. Telnyx generates a random pair you can change; using a strong, randomly generated password is recommended.

Where to find or change your SIP username/password:
- Log in to the Telnyx Portal: https://portal.telnyx.com
- Go to Voice → SIP Trunking
- Locate your SIP connection and click the pencil (edit) icon
- Open the Authentication and routing tab
- View, copy, or update the username and password as needed

## Registering devices on a credentials-based connection

A single credentials-based SIP connection can be registered to many devices over time, but only one device can be actively registered at any moment. If you register the same connection on a softphone after registering it on a desk phone, the softphone becomes active and the desk phone unregisters—calls will then ring the softphone only. Mission Control supports creating as many connections as you need; use separate connections if you require multiple simultaneously registered endpoints.

## Assigning DIDs to SIP connections and DID services

A DID must be assigned to a registered SIP connection to receive inbound PSTN calls.

Assign a single DID:
- In Numbers → Phone Numbers, under the SIP Connection/App column, click the pencil icon for the desired number
- Choose the target SIP connection from the dropdown

Bulk-assign multiple DIDs:
- Select the checkboxes for the numbers to update and click Bulk update
- Paste or confirm the list, Continue → Edit Voice Settings
- Choose the desired SIP connection and Save

DID features available include:
- e911 setup: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- Call Forwarding (bulk): https://intercom.help/telnyx/en/articles/2807944-bulk-edit-numbers-call-forwarding
- Caller ID Name (CNAM): https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- Inbound Call Recording (bulk): https://support.telnyx.com/en/articles/2807846-bulk-edit-numbers-voice-settings
- HD Voice: https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature
- Inbound Call Screening: https://support.telnyx.com/en/articles/8037040-inbound-call-screening

## Account-wide concurrent outbound call limits

New accounts start with a global limit of 2 concurrent outbound calls. After Level 2 verification, this increases to 10. Higher limits are available based on your use case; if you are Level 2 verified, email support@telnyx.com to request an increase (include context for requests over 100 channels).

If you reach the limit, Telnyx returns SIP: D1 — 403 User channel limit exceeded D1. This is enforced against the account’s global concurrent outbound limit associated with your Outbound Voice Profile: https://portal.telnyx.com/#/app/outbound-profiles

See SIP response codes: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes

## SIP Attach with UAC connections (Telnyx registers to your PBX)

### What SIP Attach/UAC is
SIP Attach lets Telnyx register as an extension on your PBX so Telnyx resources (e.g., AI Assistants, Call Control Apps, SIP-enabled apps) have a native presence on your internal phone system. It uses a UAC (User Agent Client) connection where Telnyx acts as the SIP client that registers to your PBX.

### How UAC differs from FQDN/IP connections
- FQDN/IP connections: Your PBX registers to Telnyx or is authenticated by IP; Telnyx is the server (UAS) and PBX is the client (UAC).
- UAC connections: Telnyx registers to your PBX as an extension; your PBX is the server (UAS) and Telnyx is the client (UAC).

This reverses registration direction and affects inbound routing behavior and PBX-side requirements.

### Prerequisites from your PBX
Gather from your PBX/admin:
- SIP username and password (extension credentials)
- SIP proxy address (e.g., pbx.example.com:5060)
- Transport protocol (UDP, TCP, or TLS)
- Auth username (if different), outbound proxy (if used), From User (if required)

Configure on your PBX:
- Create the SIP extension Telnyx will register as (e.g., 1001)
- Allowlist Telnyx signaling IPs so your PBX accepts REGISTER and INVITE from Telnyx

What you need on Telnyx:
- A Telnyx account and a resource (AI Assistant, Call Control App, or SIP-enabled application) to handle calls on this connection

### Create a UAC connection in Mission Control (Step 1)
- Voice → SIP Trunking → Create SIP Connection
- Select the UAC (User Agent Client) tile (Beta)
- Name the connection and click Next

### Configure Authentication and Routing (Step 2)
Step 2 has Internal UAC settings (Telnyx side) and External UAC settings (PBX side). Keep the directional model in mind:
- Telnyx → PBX uses the auto-generated SIP Subdomain
- PBX → Telnyx uses the Internal SIP URI you configure

Internal UAC settings (Telnyx side):
- SIP Subdomain (read-only): Auto-generated domain Telnyx uses when sending calls toward your PBX
- Receive SIP Subdomain calls: Controls acceptance of calls addressed to the subdomain and routes them to the Internal SIP URI
- Username/Password: Telnyx-side internal credentials
- Internal SIP URI: Where Telnyx delivers calls inbound to Telnyx on this connection (typically your AI Assistant or Call Control App’s SIP URI)

External UAC settings (PBX side):
- Username/Password: Your PBX extension’s SIP credentials
- Proxy: PBX SIP proxy (e.g., pbx.example.com:5060)
- Auth Username (optional), From User (optional), Outbound proxy (optional)
- Expiration (sec): Registration refresh interval
- Transport: UDP, TCP, or TLS (must match PBX)

Click Next to continue.

### Steps 3–6: Configuration, Inbound, Outbound, Numbers
Configure these as you would an FQDN connection:
- Configuration: Codecs, SRTP, and SIP options
- Inbound: Inbound call handling rules
- Outbound: Outbound routing rules
- Numbers (optional): Assign phone numbers to this connection

Note on inbound for UAC: Because Telnyx is a registered endpoint on your PBX, calls are addressed using the SIP subdomain and routed according to the Internal SIP URI you set in Step 2. Ensure the URI targets the correct Telnyx resource.

### Edit or delete a UAC connection
- Edit: Voice → SIP Trunking → SIP Connections → select your UAC connection → Edit. Updating External UAC settings (e.g., password, proxy, transport) triggers re-registration to your PBX.
- Delete: Voice → SIP Trunking → SIP Connections → select → Delete. Deleting deregisters immediately; any phone numbers assigned are unlinked—reassign them first to maintain inbound service.

### Troubleshooting UAC connections
Connection stuck in “Registering”:
- Confirm the PBX is reachable at the configured Proxy/port from the public internet (5060 UDP/TCP, 5061 TLS by default)
- Ensure firewalls allow SIP from Telnyx IPs
- Verify Transport matches the PBX (UDP/TCP/TLS)

Registration succeeds but calls don’t route:
- PBX: Check dial plan/routes to the registered extension; verify user/hunt group assignment
- Mission Control: Ensure Receive SIP Subdomain calls is set appropriately and the Internal SIP URI points to the correct Telnyx resource

Registration expires frequently:
- Increase Expiration (sec) in Step 2 (e.g., 3600 → 7200)
- Verify PBX min/max registration intervals; PBX may cap/override expiry

### Need help
If issues persist, email support@telnyx.com or open a ticket in Mission Control. Include the Connection ID and relevant PBX SIP logs for faster resolution.
