---
title: SIP Connections
summary: A consolidated reference for configuring Telnyx SIP Connections in the Mission
  Control Portal, covering connection types (Credentials, IP, FQDN, UAC), authentication
  and routing, inbound and outbound settings, number formats, SIP URI calling, AnchorSite®
  media anchoring, webhooks, advanced options, and DID assignment.
sources:
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
- url: https://support.telnyx.com/en/articles/1130713-what-is-my-sip-account-connection-password
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
updated_at: 2026-08-05T13:31:54Z
---

# SIP Connections

*Part 2 of 5 — see also: [Part 1](sip-connections--part-1.md), [Part 3](sip-connections--part-3.md), [Part 4](sip-connections--part-4.md), [Part 5](sip-connections--part-5.md)*

A consolidated reference for configuring Telnyx SIP Connections in the Mission Control Portal, covering connection types (Credentials, IP, FQDN, UAC), authentication and routing, inbound and outbound settings, number formats, SIP URI calling, AnchorSite® media anchoring, webhooks, advanced options, and DID assignment.

## Connection Types

Telnyx offers four authentication types for registering your switch to the Telnyx network. As a rule of thumb, use a **credential-based** connection if you have a dynamic public IP address, and an **IP-based** connection if you have a static IP address.

- **Credentials** — username/password authentication, ideal for dynamic IPs and WebRTC clients.
- **IP Address** — static IP authentication with optional multiple IPs and routing methods (Sequential or Round Robin).
- **FQDN** — Fully Qualified Domain Name authentication with separate inbound and outbound settings; outbound calls can use Credentials or IP Address authentication.
- **UAC (User Agent Client)** — Telnyx registers as a SIP endpoint on your existing PBX, used for SIP Attach.

### Credentials Connection Setup

1. Click **Create SIP Connection** at the SIP Connections tab.
2. Enter a name for the connection.
3. Select **Credentials** as the Connection Type. A username and password are auto-generated; you can change them in the Authentication & Routing section. A strong password is highly recommended.
4. Click **Next** to save the user details.

After creation, view or update the username and password under **SIP Connection → Authentication and routing**.

### IP Address Connection Setup

1. Click **Create SIP Connection**.
2. Enter a name.
3. Select **IP Address** as the Connection Type.
4. Enter an IP address and port, then click **Add IP address**. Multiple IPs can be added with a chosen routing method (Sequential or Round Robin).

If you do not have a static IP address, it will change and you will be unable to receive or make calls.

### FQDN Connection Setup

1. Click **Create SIP Connection**.
2. Enter a name.
3. Select **FQDN** as the Connection Type.
4. Click **Add FQDN**, choose the FQDN type (typically **A**), and enter the Fully Qualified Domain Name.
5. For outbound calls authentication, choose either **Credentials** or **IP Address**.

You can assign multiple FQDN addresses on the inbound section and multiple IP addresses on the outbound section to a single FQDN-registered connection, and change routing priority and method in the connection settings.

### UAC (SIP Attach) Connection

SIP Attach lets Telnyx register as a SIP endpoint on your existing PBX or voice system, giving Telnyx resources (such as an AI Assistant, Call Control Application, or SIP-enabled application) native PBX presence. With a UAC Connection, Telnyx registers to your PBX as an extension so internal callers can reach the Telnyx resource without routing through the PSTN.

The key directional difference is:

- **FQDN / IP connections:** Your PBX registers to Telnyx, or Telnyx accepts calls from your PBX based on IP authentication. Telnyx is the server (UAS) and the PBX the client (UAC).
- **UAC connections:** Telnyx registers to your PBX as an extension. Your PBX is the server (UAS) and Telnyx the client (UAC).

#### Before You Start

Collect the following from your PBX administrator:

- SIP username and password for the extension Telnyx will register as
- SIP proxy address (e.g., `pbx.example.com:5060`)
- Transport protocol (UDP, TCP, or TLS) — must match your PBX
- Auth username (if different from the SIP username)
- Outbound proxy (if applicable)
- From User (if your PBX requires a specific caller identity in the SIP From header)

On your PBX, create a SIP extension that Telnyx will register as and allowlist Telnyx signaling IPs. For SIP UAC registrations, Telnyx sends REGISTER requests from the Telnyx UAC IP for your selected region.

#### Configuration Steps

1. **Step 1 — Select Connection Type:** Navigate to Voice → SIP Trunking → Create SIP Connection, select the **UAC (User Agent Client)** tile (marked BETA), enter a name, and click **Next**.
2. **Step 2 — Authentication and Routing:** Configure Internal UAC settings (Telnyx side) and External UAC settings (PBX side).
3. **Steps 3–6:** Configure codec preferences, SRTP, inbound routing, outbound routing, and (optionally) assign phone numbers — the same as for an FQDN connection.

A UAC connection handles calls in two directions:

- **Telnyx → PBX (outbound):** uses the auto-generated **SIP Subdomain**.
- **PBX → Telnyx (inbound):** uses the **Internal SIP URI** you configure.

**Internal UAC settings (Telnyx side):**

- **SIP Subdomain** (read-only) — auto-generated (e.g., `qqffqgf1rbok.sip.telnyx.com`); used for outbound calls from Telnyx to your PBX.
- **Receive SIP Subdomain calls** — controls who can place calls to the subdomain. Defaults to **From Anyone**.
- **Username** — internal SIP username (Telnyx-side identity).
- **Password** — internal SIP password.
- **Internal SIP URI** — the Telnyx SIP URI that receives inbound calls from your PBX. For extension dialing, use the format `<extension>@<applicationFQDN>.sip.telnyx.com` (e.g., `1012@assistant-74907225-9ab8-40c8-96e2-311fd7099ca8.sip.telnyx.com`).

**External UAC settings (PBX side):**

- **Username** — SIP username for authenticating with your PBX.
- **Password** — SIP password for digest authentication.
- **Proxy** — SIP proxy address of your PBX (e.g., `pbx.example.com:5060`).
- **Auth Username** — separate username for digest auth, if your PBX uses one. Defaults to **Username**.
- **From User** — user portion of the SIP From header in outbound requests. Defaults to **Username**.
- **Outbound proxy** — SIP proxy for routing outbound requests through an intermediary, if required.
- **Expiration (sec)** — registration refresh interval.
- **Transport** — UDP, TCP, or TLS. Must match your PBX configuration.

For UAC connections, inbound calls arrive via the SIP subdomain and are routed according to the Internal SIP URI. To edit later, navigate to **Voice → SIP Trunking**, select the UAC connection, and open the **UAC Settings (Beta)** tab.

#### Registration Status

After creating or editing a UAC Connection, review the **Registration status** section to confirm whether Telnyx is registered to your external SIP registrar or PBX.

- **registered** — Telnyx is currently registered.
- **trying** — Telnyx is attempting or retrying registration.
- **failed** — the latest attempt failed; check **Last registration response**.
- **unregistering** — Telnyx is removing the SIP registration.
- **connection_disabled** — the UAC Connection is disabled or suspended.
- **unknown** — the registration state is unavailable or not classified.

The section also shows **Registered** (Yes only when status is *registered*), **Last registration response**, a **Refresh** button, and **Show registration details** (retry/failure counters, expiration timing, next scheduled action, uptime, and SIP URI/contact information). Status may take a few minutes to update after configuration changes.

#### Editing and Deleting a UAC Connection

To edit credentials or proxy settings, navigate to Voice Suite → SIP Trunking → SIP Connections, select the UAC connection, and click **Edit**. To force a fresh registration without deleting the connection, temporarily disable the UAC Connection and then re-enable it. To delete, select the connection and click **Delete** and confirm. Deleting immediately deregisters from the PBX and unlinks any assigned phone numbers.

#### Telnyx UAC IP Addresses

Telnyx uses the following public Anycast IPs for both SIP signaling and RTP media on UAC connections. The IP depends on the SIP region selected in your UAC Connection settings.

- **US:** 192.76.120.14
- **Europe:** 192.76.120.72
- **Australia:** 192.76.120.73
- **Canada:** 192.76.120.74
- **Middle East:** 192.76.120.75
- **Asia (Beta):** 192.76.120.76

Allow-list the relevant IP(s) on your PBX/firewall for both SIP signaling (ports 5060/5061) and RTP media (ports 16384–32768 UDP).
