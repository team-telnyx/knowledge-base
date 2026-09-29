---
title: "SIP Connection Failover Guide (IP/FQDN-Based)"
summary: "This guide explains how to configure failover for SIP Connections using IP or FQDN-based authentication in the Telnyx… See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--1176364-sip-connection-failover-guide-ip-fqdn-based.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--1176364-sip-connection-failover-guide-ip-fqdn-based.md -->

# SIP Connection Failover Guide (IP/FQDN-Based)

This guide explains how to configure failover for SIP Connections using IP or FQDN-based authentication in the Telnyx… See Telnyx guidance and requirements.




##

* **Note:** Failover can only be configured when multiple IP addresses or FQDNs are defined within a single SIP Connection.

---

## Step-by-Step Configuration

## 1. Create a SIP Connection

* Navigate to: <https://portal.telnyx.com/#/voice/connections>
* Click **“Add SIP Connection”**
* Enter a **Connection Name**
* Select **Type**: *IP* or *FQDN*
* Click **Create**

## 2. Configure IP/FQDN Addresses

* Click **“Add IP”**
* Add your endpoints in order:

  + **First entry:** Primary IP/FQDN
  + **Second entry:** Secondary IP/FQDN (failover)

## 3. Set Failover Priority

* Use the dropdown to define the routing order:

  + **Primary → Secondary → (optional) Tertiary**

Failover will follow this sequence if a route becomes unreachable or fails.
​

## 4. Save the Connection

* Click **“Next”**, then **“Done”** to finalize the SIP Connection

---

## Result

Your SIP Connection is now configured with failover. Calls will automatically route to backup endpoints if the primary endpoint fails.

---

## Additional Notes

* Failover is triggered when an endpoint is unreachable or fails to respond
* Ensure all configured endpoints are properly provisioned and reachable
* Regularly test failover behavior to confirm proper routing
