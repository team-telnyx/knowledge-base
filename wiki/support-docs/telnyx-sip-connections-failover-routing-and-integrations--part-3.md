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

*Part 3 of 7 — see also: [Part 1](telnyx-sip-connections-failover-routing-and-integrations--part-1.md), [Part 2](telnyx-sip-connections-failover-routing-and-integrations--part-2.md), [Part 4](telnyx-sip-connections-failover-routing-and-integrations--part-4.md), [Part 5](telnyx-sip-connections-failover-routing-and-integrations--part-5.md), [Part 6](telnyx-sip-connections-failover-routing-and-integrations--part-6.md), [Part 7](telnyx-sip-connections-failover-routing-and-integrations--part-7.md)*

This page consolidates Telnyx SIP Connection configuration, failover, and retry behavior across IP/FQDN-based, credential-based, and UAC (SIP Attach) connection types. It covers AnchorSite® media routing, DID assignment, the Telnyx + Vapi integration (imported-number and BYO SIP trunk flows), and PBX setup guides for Bicom PBXware and sipXecs.

## UAC (SIP Attach) Connections

SIP Attach lets Telnyx register as a SIP endpoint on your existing PBX or voice system, giving your Telnyx resource (such as an AI Assistant, Call Control Application, or SIP-enabled application) native PBX presence. Under the hood, SIP Attach is configured using a UAC (User Agent Client) Connection. With a UAC Connection, Telnyx registers to your PBX as an extension, so internal callers can reach the Telnyx resource without routing through the PSTN. This reduces latency and cost while making it easier to connect employee-facing voice agents, internal support flows, and other SIP-enabled Telnyx applications to your existing voice infrastructure.

### How UAC Differs from FQDN Connections

The SIP registration direction is reversed compared with traditional FQDN or IP-authenticated SIP connections:

- **FQDN / IP connections:** Your PBX registers to Telnyx, or Telnyx accepts calls from your PBX based on IP authentication. Telnyx is the server (UAS) and the PBX the client (UAC).
- **UAC connections:** Telnyx registers to your PBX as an extension. Your PBX is the server (UAS) and Telnyx the client (UAC).

This affects how inbound calls are routed and what you need to configure on the PBX side.

### Prerequisites

**From your PBX (customer side):**

- SIP username and password (credentials for the extension Telnyx will register as)
- SIP proxy address (where Telnyx sends SIP REGISTER requests, e.g., `pbx.example.com:5060`)
- Transport protocol (UDP, TCP, or TLS — must match your PBX)
- Auth username (if different from SIP username)
- Outbound proxy (if applicable)
- From User (if your PBX requires a specific caller identity in the SIP From header)

**On your PBX (customer side):**

1. Create a SIP extension that Telnyx will register as (e.g., extension 1001).
2. Allowlist Telnyx signaling IPs — your PBX must accept SIP REGISTER and INVITE requests from Telnyx's IP ranges. For SIP UAC registrations, Telnyx sends REGISTER requests from the Telnyx UAC IP for your selected region (see the UAC IP table below).

**On the Telnyx side:**

- A Telnyx account
- A Telnyx resource (such as a Call Control Application, AI Assistant, or SIP-enabled application) that will handle calls on this connection
- UAC Connections follow the same per-account connection limits as other SIP Connection types in the Mission Control Portal

### Step 1 — Select Connection Type

1. Navigate to **Voice → SIP Trunking → Create SIP Connection** in the Mission Control Portal.
2. Select the **UAC (User Agent Client)** tile (marked BETA).
3. Enter a Name for your connection (e.g., `PBX-uac`).
4. Click **Next**.

### Step 2 — Authentication and Routing

A UAC connection handles calls in two directions, and two different fields govern each direction:

- **Telnyx → PBX (outbound):** uses the auto-generated **SIP Subdomain**
- **PBX → Telnyx (inbound):** uses the **Internal SIP URI** you configure

**Internal UAC settings (Telnyx side):**

- **SIP Subdomain** (read-only): Auto-generated by Telnyx (e.g., `qqffqgf1rbok.sip.telnyx.com`). This is the address used for outbound calls from Telnyx to your PBX.
- **Receive SIP Subdomain calls** (required): Controls who can place calls to the subdomain. Defaults to **From Anyone**. When enabled, Telnyx accepts inbound SIP calls addressed to this subdomain and routes them to the Internal SIP URI below.
- **Username** (required): Internal SIP username (Telnyx-side identity).
- **Password** (required): Internal SIP password.
- **Internal SIP URI** (required): The Telnyx SIP URI that receives inbound calls from your PBX. For extension dialing, use the format `<extension>@<applicationFQDN>.sip.telnyx.com` (e.g., `1012@assistant-74907225-9ab8-40c8-96e2-311fd7099ca8.sip.telnyx.com`). This routes PBX extension 1012 to the AI Assistant application.

Because Telnyx registers *to* your PBX (rather than the other way around), inbound calls arrive via the SIP subdomain. The Internal SIP URI tells Telnyx where to deliver them, typically your AI Assistant or Call Control Application. If this is wrong, registration will succeed but calls won't route.

**External UAC settings (PBX side):**

- **Username** (required): SIP username for authenticating with your PBX.
- **Password** (required): SIP password for digest authentication.
- **Proxy** (required): SIP proxy address of your PBX (e.g., `pbx.example.com:5060`). Where Telnyx sends SIP REGISTER requests.
- **Auth Username** (optional): Separate username for digest auth, if your PBX uses one. Defaults to **Username**.
- **From User** (optional): User portion of the SIP From header in outbound requests. Defaults to **Username**.
- **Outbound proxy** (optional): SIP proxy for routing outbound requests through an intermediary, if required.
- **Expiration (sec)** (optional): Registration refresh interval. Telnyx re-registers at this interval.
- **Transport** (optional): UDP, TCP, or TLS. Must match your PBX configuration.

### Steps 3–6 — Configuration, Inbound, Outbound, Numbers

Configure these steps the same way you would for an FQDN connection:

- **Step 3 — Configuration:** Codec preferences, SRTP, and other SIP settings.
- **Step 4 — Inbound:** Inbound call routing and handling rules.
- **Step 5 — Outbound:** Outbound call routing rules.
- **Step 6 — Numbers:** Assign phone numbers to this connection (optional).

For IP-based and FQDN connections, inbound calls are routed based on source IP or resolved hostname. For a UAC connection, Telnyx is a registered endpoint on the PBX, so calls arrive via the **SIP subdomain** and are routed according to the **Internal SIP URI** set in Step 2. Make sure that URI points to the correct Telnyx resource.

To edit your configuration later, navigate to **Voice → SIP Trunking**, select your UAC connection, and go to the **UAC Settings (Beta)** tab.

### Registration Status

After creating or editing a UAC Connection, review the **Registration status** section to confirm whether Telnyx is registered to your external SIP registrar or PBX.

**SIP Registration Status values:**

- **registered:** Telnyx is currently registered to the external SIP registrar/PBX.
- **trying:** Telnyx is attempting or retrying SIP registration. Wait for the registration attempt to complete, then refresh the status.
- **failed:** The latest registration attempt failed. Check **Last registration response** for more information.
- **unregistering:** Telnyx is removing or unregistering the SIP registration.
- **connection_disabled:** The UAC Connection is disabled or suspended, so registration is not active.
- **unknown:** The registration state is unavailable or not classified.

The Registration status section also includes:

- **Registered:** Shows whether the UAC connection is currently registered. Shows **Yes** only when **SIP registration status** is *registered*.
- **Last registration response:** Shows the most recent SIP response Telnyx received from the external SIP registrar/PBX, such as *200 OK*.
- **Refresh:** Fetches the latest registration state. Use this after saving changes or updating PBX settings.
- **Show registration details:** Expands additional technical registration details, such as retry/failure counters, expiration timing, next scheduled action, uptime, and SIP URI/contact information.

After creating or updating a UAC Connection, registration status may take a few minutes to update while Telnyx picks up the configuration and attempts SIP registration.

### Editing or Deleting a UAC Connection

**Edit credentials or proxy settings:**

1. Navigate to **Voice Suite → SIP Trunking → SIP Connections** in the Mission Control Portal.
2. Select your UAC connection.
3. Click **Edit** to update any field in Step 2 — for example, changing the Password after a PBX credential rotation, updating the Proxy address after a network change, or adjusting the Expiration (sec) value.

**Disable a connection to force a fresh registration:**

If you need to force a fresh, clean SIP registration without deleting the connection, temporarily disable the UAC Connection and then re-enable it. Disabling the connection unregisters the SIP UAC from your PBX. When you re-enable the connection, Telnyx starts a new registration attempt using the current External UAC settings.

**Delete a connection:**

1. Navigate to **Voice Suite → SIP Trunking → SIP Connections** in the Mission Control Portal.
2. Select your UAC connection.
3. Click **Delete** and confirm.

Deleting a connection immediately deregisters from the PBX. Any phone numbers assigned to the connection will be unlinked — reassign them to another connection before deleting if you want to preserve inbound service.

### Telnyx UAC IP Addresses

Telnyx uses the following public Anycast IPs for both SIP signaling and RTP media on UAC (SIP Attach) connections. The IP depends on the SIP region selected in your UAC Connection settings.

- **US:** `192.76.120.14`
- **Europe:** `192.76.120.72`
- **Australia:** `192.76.120.73`
- **Canada:** `192.76.120.74`
- **Middle East:** `192.76.120.75`
- **Asia (Beta):** `192.76.120.76`

Allow-list the relevant IP(s) on your PBX/firewall for both SIP signaling (ports 5060/5061) and RTP media (ports 16384–32768 UDP).

### UAC Troubleshooting

Before troubleshooting call routing, check the **Registration status** section on the UAC Connection.

- If **SIP registration status** is *registered*, Telnyx is registered to the external SIP registrar/PBX. If calls still do not route, check the PBX dial plan and the Internal SIP URI configured in Telnyx.
- If the status is *trying*, Telnyx is attempting or retrying registration. Wait for the registration attempt to complete, then click **Refresh** to check the latest status. If the status remains *trying* for several minutes or changes to *failed*, review **Last registration response** and continue troubleshooting.
- If the status is *failed*, review **Last registration response** and check the SIP username, password, auth username, proxy, transport, and PBX registrar settings.
- If the status is *connection_disabled*, confirm the UAC Connection is enabled in UAC Connection details.
- After making changes, click **Refresh** to confirm the latest registration state.

**Connection stuck in "Registering":**

- Verify your PBX is reachable at the Proxy address from the public internet.
- Check that the port is correct (5060 for UDP/TCP, 5061 for TLS).
- Confirm no firewall is blocking SIP traffic from the Telnyx UAC IP.
- Verify the Transport setting in Step 2 matches what your PBX expects (UDP, TCP, or TLS).

**Registration succeeds but calls don't route:**

- On the PBX side: Verify your PBX dial plan routes calls to the registered extension correctly. Confirm the extension is assigned to the right user or hunt group.
- On the Telnyx Mission Control Portal: Confirm **Receive SIP Subdomain calls** is set correctly in Step 2. Verify your telephony resource (AI Assistant, Call Control Application) is correctly linked to this connection and the Internal SIP URI points to it.
- Verify the Internal SIP URI uses the correct extension-dialing format: `<extension>@<applicationFQDN>.sip.telnyx.com`. If this field is set to a generic SIP URI such as `assistant-<id>@sip.telnyx.com`, registration may succeed but calls from the PBX will not route to the intended Telnyx application.
- If media (audio) isn't flowing, confirm your firewall allows RTP from the same UAC IP (Telnyx uses the same IP for signaling and media on UAC connections).

**Registration expires frequently:**

If your PBX rate-limits registrations or you see frequent re-registration cycles:

1. Edit the connection in the Mission Control Portal.
2. Increase the **Expiration (sec)** value in Step 2 (e.g., from 3600 to 7200).
3. Check your PBX's minimum and maximum registration interval settings — some PBX systems override the requested expiry.
