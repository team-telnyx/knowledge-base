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

*Part 1 of 7 — see also: [Part 2](telnyx-sip-connections-failover-routing-and-integrations--part-2.md), [Part 3](telnyx-sip-connections-failover-routing-and-integrations--part-3.md), [Part 4](telnyx-sip-connections-failover-routing-and-integrations--part-4.md), [Part 5](telnyx-sip-connections-failover-routing-and-integrations--part-5.md), [Part 6](telnyx-sip-connections-failover-routing-and-integrations--part-6.md), [Part 7](telnyx-sip-connections-failover-routing-and-integrations--part-7.md)*

This page consolidates Telnyx SIP Connection configuration, failover, and retry behavior across IP/FQDN-based, credential-based, and UAC (SIP Attach) connection types. It covers AnchorSite® media routing, DID assignment, the Telnyx + Vapi integration (imported-number and BYO SIP trunk flows), and PBX setup guides for Bicom PBXware and sipXecs.

## Overview

Telnyx SIP Connections support several configuration models — IP/FQDN-based, credential-based, and UAC (User Agent Client) — each with its own failover, retry, and routing behavior. This page consolidates the configuration steps, failover logic, AnchorSite® media routing, and integration patterns (including Vapi and PBX systems such as Bicom PBXware and sipXecs) into a single reference.

## SIP Connection Failover (IP/FQDN-Based)

Failover can only be configured when multiple IP addresses or FQDNs are defined within a single SIP Connection.

To configure failover in the Mission Control Portal:

1. Navigate to [Voice → Connections](https://portal.telnyx.com/#/voice/connections) and click **Add SIP Connection**.
2. Enter a **Connection Name**, select **Type** as *IP* or *FQDN*, and click **Create**.
3. Click **Add IP** and add endpoints in order:
   - **First entry:** Primary IP/FQDN
   - **Second entry:** Secondary IP/FQDN (failover)
4. Use the dropdown to define the routing order: **Primary → Secondary → (optional) Tertiary**. Failover follows this sequence if a route becomes unreachable or fails.
5. Click **Next**, then **Done** to finalize the SIP Connection.

Failover is triggered when an endpoint is unreachable or fails to respond. Ensure all configured endpoints are properly provisioned and reachable, and regularly test failover behavior to confirm proper routing.

## Fail-over and Retry Concepts

Telnyx Mission Control SIP Connections allow multiple retries in case a call fails to connect. The fail-over and retry policy is designed to ensure calls always connect regardless of issues on either side.

Key concepts:

- **IP1:** Primary signaling IP address of the SIP region (e.g., for US SIP region: `192.76.120.10`).
- **IP2:** Secondary signaling IP address of the SIP region (e.g., for US SIP region: `64.16.250.10`).
- **Routes:** Each Connection can have multiple routes. For IP Auth connections each IP address is a route; for FQDN connections each FQDN is a route.
- **Route preferences:** If a Connection routing method is **Sequential**, each route can be set as Primary, Secondary, or Tertiary. Number-level settings override Connection settings. If the routing method is **Round Robin**, each route is attempted in random order.
- **Call Connected:** A call attempt is considered "connected" (not to be confused with "answered") if it gets one of the following results:
  - 486 Busy
  - 404 Not Found
  - 603 Declined
  - Call rings (180/183) but is not answered
  - Call is answered (200 OK)

To prevent retries on inbound calls, return a **603 Declined** response — this is the SIP response code Telnyx honors for not retrying.

### Inbound Call to Connection with Only One Route

1. Telnyx sends an attempt from IP1 to the single route of the Connection.
2. If the call attempt doesn't connect, Telnyx retries from IP2.

### Inbound Call to Connection with Multiple Routes

1. Telnyx sends a call attempt from IP1 to the first route of the Connection.
2. If the call attempt doesn't connect, Telnyx sends an attempt from IP1 to the second route.
3. If the call attempt doesn't connect, Telnyx sends an attempt from IP1 to the third route.
4. If the call attempt doesn't connect, Telnyx sends an attempt from IP2 to the first route.
5. If the call attempt doesn't connect, Telnyx sends an attempt from IP2 to the second route.
6. If the call attempt doesn't connect, Telnyx sends an attempt from IP2 to the third route.

### Inbound Call to Cred Auth Connection

Telnyx sends call attempts to Cred Auth Connections only from the IP that the SIP device registered to (either IP1 or IP2). The SIP device can be configured to register against:

1. An IP address (either IP1 or IP2)
2. An FQDN that points only to IP1 (for US SIP region: `sip-anycast1.telnyx.com`)
3. An FQDN that points only to IP2 (for US SIP region: `sip-anycast2.telnyx.com`)
4. An FQDN with SRV records that point to IP1 as primary and IP2 as secondary (`sip.telnyx.com`) — the SIP device may register to either IP1 or IP2 depending on its internal tests.

Call attempts to Cred Auth connections go through a KSS (SIP registrar) with 3 instances per US region:

1. Telnyx sends a call attempt from primary KSS and then through IP1/2 to the Cred Auth Connection.
2. If the call attempt doesn't connect, Telnyx sends a call attempt from secondary KSS and then through IP1/2.
3. If the call attempt doesn't connect, Telnyx sends a call attempt from tertiary KSS and then through IP1/2.

### Inbound Call with Call Forward On Failure

1. Telnyx sends a call attempt from IP1 to the first route of the Connection.
2. If the call attempt doesn't connect, Telnyx sends an attempt from IP1 to the second route.
3. If the call attempt doesn't connect, Telnyx sends an attempt from IP1 to the third route.
4. If the call attempt doesn't connect, Telnyx sends an attempt to the Call Forward PSTN Number through the first Termination Carrier in route.
5. If the call attempt doesn't connect, Telnyx sends an attempt to the Call Forward PSTN Number through the second Termination Carrier in route.
6. If the call attempt doesn't connect, Telnyx sends an attempt to the Call Forward PSTN Number through the "n" Termination Carrier in route (max 10 termination carriers).

### Inbound Call to Number with Call Forward Always

1. Telnyx sends a call attempt to the PSTN Number through the first Termination Carrier in route.
2. If the call attempt doesn't connect, Telnyx sends an attempt through the second Termination Carrier.
3. If the call attempt doesn't connect, Telnyx sends an attempt through the "n" Termination Carrier (max 10 termination carriers).

### Inbound Call to Connection with SRV Records

When an inbound call is routed to an FQDN Connection that uses SRV records, Telnyx honors the SRV records as long as no port is specified in the SIP URI. Telnyx performs an SRV lookup and routes the call based on the priority and weight returned by DNS. SRV records can be used for load balancing and failover across multiple SIP targets. If the first SRV target fails with a SIP 503 response, Telnyx attempts the next highest priority target in the SRV list.

If no SRV record exists, Telnyx falls back to an A-record lookup and uses the default SIP port (5060 for UDP/TCP or 5061 for TLS). If the domain cannot be resolved, the call fails with SIP 478 Unresolvable Destination.

> **Important:** If a port is included in the SIP URI, Telnyx bypasses SRV lookup and performs an A-record lookup instead. To use SRV failover, configure the FQDN without a port.

### Outbound Call to PSTN Number

1. Telnyx sends a call attempt to the PSTN Number through the first Termination Carrier in route.
2. If the call attempt doesn't connect, Telnyx sends an attempt through the second Termination Carrier.
3. If the call attempt doesn't connect, Telnyx sends an attempt through the "n" Termination Carrier (max 10 termination carriers).

### Configuring Primary and Secondary Proxies

- **Inbound:** Ensure SIP endpoints and network ACLs or failovers allow calls from both the primary and secondary Telnyx SIP proxy IPs.
- **Outbound:**
  - For IP addresses, use `192.76.120.10` as primary and `64.16.250.10` as secondary for the US region.
  - For FQDNs with A DNS record resolution, use `sip.telnyx.com` as the primary FQDN and `sip-anycast2.telnyx.com` as the failover for the US region.
  - For FQDNs with SRV DNS record resolution (recommended), use `sip.telnyx.com` for the US region — failover is automatically configured.
- For other regions (`sip.telnyx.eu`, `sip.telnyx.ca`, `sip.telnyx.com.au`, etc.), change the domain accordingly. See all available regions at [sip.telnyx.com](https://sip.telnyx.com/).
