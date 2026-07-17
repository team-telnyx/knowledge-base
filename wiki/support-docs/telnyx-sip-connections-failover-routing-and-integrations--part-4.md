---
title: 'Telnyx SIP Connections: Failover, Routing, and Integrations'
summary: This page consolidates Telnyx SIP Connection configuration, failover, and
  retry behavior across IP/FQDN-based, credential-based, and UAC (SIP Attach) connection
  types. It covers AnchorSite® media routing, DID assignment, the Telnyx + Vapi integration
  (imported-number and BYO SIP trunk flows), and PBX setup guides for Bicom PBXware
  and sipXecs.
sources:
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
- url: https://support.telnyx.com/en/articles/6128008-sipxecs-pbx-setup-config
updated_at: 2026-07-17T09:07:44Z
---

# Telnyx SIP Connections: Failover, Routing, and Integrations

*Part 4 of 7 — see also: [Part 1](telnyx-sip-connections-failover-routing-and-integrations--part-1.md), [Part 2](telnyx-sip-connections-failover-routing-and-integrations--part-2.md), [Part 3](telnyx-sip-connections-failover-routing-and-integrations--part-3.md), [Part 5](telnyx-sip-connections-failover-routing-and-integrations--part-5.md), [Part 6](telnyx-sip-connections-failover-routing-and-integrations--part-6.md), [Part 7](telnyx-sip-connections-failover-routing-and-integrations--part-7.md)*

This page consolidates Telnyx SIP Connection configuration, failover, and retry behavior across IP/FQDN-based, credential-based, and UAC (SIP Attach) connection types. It covers AnchorSite® media routing, DID assignment, the Telnyx + Vapi integration (imported-number and BYO SIP trunk flows), and PBX setup guides for Bicom PBXware and sipXecs.

## Assigning DIDs to a SIP Connection

A DID is needed in order to receive inbound calls from the Telnyx network. You must assign a registered connection on a DID in order to receive inbound calls.

### Assigning a Single DID

1. Hover over the box beneath the **SIP Connection/App** header and click the pencil icon.
2. Select the connection you want to assign to the DID from the dropdown.

### Assigning Multiple DIDs

1. Select the check box to the left of the DIDs you want to edit.
2. Click the **Bulk update** button.
3. Paste all the numbers you want to update, click **Continue**, then **Edit Voice Settings**.
4. Select the desired SIP Connection in the connection field.
5. Click **Save**.

### DID Services

Telnyx offers seven services on DIDs:

- e911
- Call Forwarding
- Caller ID Name Listing
- Caller ID Name (Incoming)
- Inbound Call Recording
- HD Voice
- Inbound Call Screening
