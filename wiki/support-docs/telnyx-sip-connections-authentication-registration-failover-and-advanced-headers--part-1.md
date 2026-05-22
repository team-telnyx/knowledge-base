---
title: 'Telnyx SIP Connections: Authentication, Registration, Failover, and Advanced
  Headers'
summary: A practical guide to Telnyx SIP connection types and telephony credentials,
  how registration and authentication work, options for multi-tenant identification
  (tech prefixes, tokens, headers), failover and SRV behavior, UAC (SIP Attach) connections,
  key limitations, and troubleshooting best practices.
sources:
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
updated_at: 2026-05-20T14:36:02Z
---

# Telnyx SIP Connections: Authentication, Registration, Failover, and Advanced Headers

*Part 1 of 2 — see also: [Part 2](telnyx-sip-connections-authentication-registration-failover-and-advanced-headers--part-2.md)*

A practical guide to Telnyx SIP connection types and telephony credentials, how registration and authentication work, options for multi-tenant identification (tech prefixes, tokens, headers), failover and SRV behavior, UAC (SIP Attach) connections, key limitations, and troubleshooting best practices.

## Connection types and when to use them
- Credentials connection: Use when your PBX/endpoints don’t have a static public IP. Telnyx authenticates with username/password. Outbound uses SIP 407 digest auth; inbound requires the device to be registered.
- IP-based connection: Use when your PBX has a static public IP. Telnyx trusts calls from listed IP(s). You can add multiple IPs and set routing method as Sequential or Round Robin.
- FQDN-based connection: Authenticate inbound by hostname (A/SRV). Outbound auth can be set to Credentials or IP. You can attach multiple inbound FQDNs and multiple outbound IPs.
- UAC (User Agent Client) connection a.k.a. SIP Attach: Telnyx registers to your PBX as an extension, giving Telnyx resources native PBX presence (useful for AI Assistants, Call Control apps, internal agents).

Reference setup details are available in the Mission Control Portal under Voice → SIP Trunking → Create SIP Connection.

## Telephony credential options
- SIP Connection Credentials: Username/password tied to a single SIP Connection. Choose strong, unique credentials.
- On-Demand Credentials (API-created): Programmatic per-user credentials for outbound calling and WebRTC. Inbound directly to these credentials isn’t supported; use your application to bridge inbound calls to logged-in agents. See API endpoint: https://developers.telnyx.com/api/connections/list-connections and Telephony Credentials endpoints.
- JSON Web Tokens (JWT): Short-lived tokens (24h) minted for On-Demand Credentials to enhance security for WebRTC/VoIP logins.

## SIP registration essentials
- Inbound to credential-based connections requires successful SIP registration; outbound does not require registration (it uses SIP 407 + digest auth).
- Typical registration flow: initial REGISTER → 401 Unauthorized challenge → REGISTER with credentials → 200 OK when successful. Incorrect creds will loop 401.
- Transport: UDP/TCP/TLS are dictated by the user agent. With TCP/TLS, Telnyx reuses the established TCP connection. If the Contact header’s IP:port differ from the source, Telnyx aliases the AOR and still reuses the TCP connection.
- Expiry: Use a relatively low registration expiry (around 180 seconds recommended) to keep the AOR fresh. If the expiry lapses without refresh, inbound will fail.
- Domains: Register to sip.telnyx.com (US) or regional FQDNs (sip.telnyx.ca, sip.telnyx.eu, sip.telnyx.com.au). The high-volume short-duration domain (siphv.telnyx.com) does not accept registration (SIP 405).
- SIP URI calling to credential-based connections: ensure your Contact header username matches the SIP Connection username, or your system may reject INVITEs.

## Multi-device and multi-tenant patterns
- A single credentials-based connection can be registered by many devices over time, but only one device is actively registered at any given moment. The last registration wins for inbound delivery. To avoid contention, use a PBX behind the connection, create multiple connections, or issue per-user On-Demand Credentials/WebRTC.
- For shared-IP multi-tenant deployments, use one or more of: Tech Prefix, X-Telnyx-Token, and/or P-Charge-Info to uniquely identify and segment traffic.

## Token and header-based identification
- X-Telnyx-Token header (for IP-auth connections):
  - Configure a unique token (12–48 chars; alphanumeric and dashes) on the IP-based SIP Connection, then include X-Telnyx-Token: <token> in the outbound INVITE.
  - INVITEs must originate from an IP associated with the target connection.
  - Example PBX implementation (FreePBX/Asterisk): use a predial hook (extensions_custom.conf) to set SIP header; verify via Asterisk console and SIP debug.
- P-Charge-Info header: Add P-Charge-Info: +E164Number to INVITEs so Telnyx identifies billing/DID properly. Scope the macro to the intended trunk if you have multiple trunks.

## Tech prefixes for IP-auth connections
- Assign a unique 4-digit tech prefix per IP-auth connection when multiple clients share the same IP.
- Dial by prepending the 4-digit prefix to the destination number (e.g., 123418005678912). Configure your PBX to automatically prepend.
- Omitting the prefix will lead to a SIP 407 and call rejection.
- You can also apply tech prefixes at the number level for granular routing/identification.
- If you encounter a Termination Endpoint assignment error when multiple connections share an IP, ensure uniqueness via tech prefix, token, or P-Charge-Info.

## Failover logic and retries
- Definitions (US region examples): IP1 = 192.76.120.10; IP2 = 64.16.250.10.
- When Telnyx considers an attempt “connected” (thus stops retrying): 486, 404, 603, ringing (180/183) without answer, or 200 OK.
- To stop inbound retries when you don’t want them, return SIP 603 Declined.
- Inbound to connection with one route: try from IP1; if not connected, retry from IP2.
- Inbound to connection with multiple routes (Sequential): IP1 tries route 1 → 2 → 3; then IP2 tries route 1 → 2 → 3.
- Inbound to credential-auth connection: Telnyx sends to the IP (IP1 or IP2) where the device registered, via one of three registrar (KSS) instances in order (primary → secondary → tertiary).
- Call Forward (On Failure / Always): Telnyx will attempt the configured PSTN target through termination carriers in order (up to 10), after exhausting connection routes (for On Failure) or immediately (Always).
- Outbound to PSTN: Telnyx cycles through termination carriers in route order until connected.

## Configuring IP/FQDN failover priority
- Add multiple IPs or FQDNs to a single SIP Connection and set priority (Primary/Secondary/Tertiary) with Sequential routing, or use Round Robin for distribution.
- Save and test regularly to validate failover behavior.

## SRV record behavior and DNS considerations
- For FQDN connections with SRV: Telnyx honors SRV priority/weight so you can load-balance and fail over across targets. If the top target returns 503, Telnyx proceeds to the next.
- If you include an explicit port in the SIP URI, SRV lookup is bypassed and A-record lookup is used instead.
- If no SRV exists, Telnyx falls back to A-record and default SIP ports (5060 UDP/TCP, 5061 TLS). Unresolvable domains fail with 478.

## UAC connections (SIP Attach) fundamentals
- Direction is reversed versus classic SIP trunks:
  - Telnyx → PBX (outbound from Telnyx): Uses the auto-generated SIP Subdomain (e.g., abc123.sip.telnyx.com).
  - PBX → Telnyx (inbound to Telnyx): Routed by the Internal SIP URI you configure on the connection.
- Internal UAC settings (Telnyx side):
  - SIP Subdomain (read-only), Receive SIP Subdomain calls toggle, Internal Username/Password, Internal SIP URI (target Telnyx resource such as an AI Assistant or Call Control app).
- External UAC settings (PBX side within the connection):
  - Username/Password, Proxy (pbx.example.com:5060), optional Auth Username/From User/Outbound proxy, Expiration, and Transport (UDP/TCP/TLS). Must match PBX.
- PBX requirements: Provision an extension for Telnyx, allowlist Telnyx signaling IPs, ensure dial plans route to/from that extension as intended.
- Troubleshooting:
  - “Registering” stuck: verify reachability/ports/firewalls and transport match.
  - Registration ok but calls fail: confirm Receive SIP Subdomain calls, Internal SIP URI target, and PBX dial plan to the registered extension.

## Inbound and outbound proxy recommendations
- US region:
  - IPs: Primary 192.76.120.10, Secondary 64.16.250.10.
  - FQDN: Prefer sip.telnyx.com with SRV (recommended). If using A-records, sip.telnyx.com primary and sip-anycast2.telnyx.com as failover.
- Use regional domains for other geographies (see https://sip.telnyx.com/).
