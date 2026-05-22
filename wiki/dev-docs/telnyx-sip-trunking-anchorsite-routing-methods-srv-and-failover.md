---
title: 'Telnyx SIP trunking: AnchorSite, routing methods, SRV, and failover'
summary: A practical guide to controlling where Telnyx anchors media (AnchorSite),
  how inbound routing and retries behave, how to use DNS SRV for resilient signaling,
  and which SIP responses influence failover—plus configuration tips and examples.
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/anchorsite-configuration
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/failover-and-retries/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/round-robin-routing/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/srv-records
- url: https://developers.telnyx.com/docs/voice/sip-trunking/troubleshooting/response-codes/index
updated_at: 2026-05-20T09:49:55Z
---

# Telnyx SIP trunking: AnchorSite, routing methods, SRV, and failover

A practical guide to controlling where Telnyx anchors media (AnchorSite), how inbound routing and retries behave, how to use DNS SRV for resilient signaling, and which SIP responses influence failover—plus configuration tips and examples.

## AnchorSite overview
AnchorSite determines which Telnyx Point of Presence (PoP) anchors RTP media for your SIP calls. It operates per SIP Connection and can be chosen automatically by latency or pinned manually for predictable routing.

## AnchorSite modes and requirements
- Latency mode (automatic): Telnyx probes ICMP latency to your SIP endpoint and anchors media in the lowest-latency PoP.
  - If you use IP/FQDN authentication: allow ICMP ping from Telnyx media IPs through your firewalls.
  - If you use credential authentication: include your SIP Connection username so Telnyx can correlate the endpoint during probing. Either include it in the Contact header or in an X-Telnyx-Username header, for example:

    Contact: <sip:user@192.0.2.10:5060>
    X-Telnyx-Username: connection_username

  - TeXML: latency is measured to the public IP of your webhook URL; the best PoP for that address is selected.

- Manual mode (explicit PoP): Pin media to a specific PoP for deterministic behavior. Available PoPs include:
  - Chicago, IL (North America Central)
  - Ashburn, VA (North America East)
  - San Jose, CA (North America West)
  - Toronto, Canada; Montreal, Canada; Vancouver, Canada
  - London, UK; Amsterdam, Netherlands; Frankfurt, Germany
  - Sydney, Australia

## Configure AnchorSite
- Portal: In the Telnyx Portal, edit your SIP IP Connection and use the AnchorSite Override dropdown to select Latency or a specific PoP.
- API (key fields):
  - anchorsite_override: "latency" to enable latency mode, or a PoP name (e.g., "Chicago, IL") to pin manually.

## Signaling and media failover model
- Separation of roles: AnchorSite selects the media PoP, while SIP signaling enters Telnyx via geo-redundant regional signaling IPs (two per region). Always prefer the regional FQDNs (for example, sip.telnyx.com for US, sip-eu.telnyx.com for Europe, sip-ca.telnyx.com for Canada, sip-au.telnyx.com for Australia) to pick up the current IPs automatically.
- Single-route behavior: Telnyx sends the SIP INVITE from the region’s primary signaling IP; if it fails, Telnyx retries from the secondary IP.
- Multi-route behavior: When you configure multiple target routes on a SIP Connection, Telnyx attempts all routes via the primary signaling IP in your configured order; if all fail, it retries all routes via the secondary signaling IP. Route order follows your default routing method (sequential or round-robin).
- Credential-auth specifics: With registered/credential connections, Telnyx routes via the registered KSS instance and applies multiple internal failover layers automatically.
- Call forward on failure: Optional feature that, after all SIP routes fail, forwards calls to PSTN termination via up to 10 downstream carriers.

## Routing methods: sequential vs round-robin
- Sequential (default): Tries your routes in order. Combined with Telnyx’s signaling IP redundancy, this yields simple, predictable failover.
- Round-robin (inbound distribution): Distributes incoming calls evenly across all configured IPs, cycling through them regardless of current call load, for example:

  Call 1 → IP 1
  Call 2 → IP 2
  Call 3 → IP 3
  Call 4 → IP 1 (repeats)

  - Failover: If the selected IP fails, Telnyx tries the remaining IPs in sequence; each IP serves as a backup for the others.
  - Limitations: Distribution is count-based, not load-aware; an IP with many active calls still receives new calls at the same rate as others.
  - Use cases: Simple HA across PBX instances where equal distribution is sufficient.
- API (key fields):
  - default_routing_method: "sequential" or "round-robin".

## Resilient SIP with DNS SRV records
DNS SRV records provide transport-aware, port-aware routing that resolves to multiple Telnyx signaling IPs with priority and weight controls, enabling client-side load sharing and automatic failover.

- SRV record format (RFC 2782):

  _service._protocol.domain TTL IN SRV priority weight port target

  Example (UDP 5060 to US region):

  _sip._udp.example.com. 3600 IN SRV 10 10 5060 sip.telnyx.com.

- TLS signaling example (TCP 5061):

  _sip._tcp.example.com. 3600 IN SRV 10 10 5061 sip.telnyx.com.

- Multi‑region redundancy example (US primary, EU secondary):

  _sip._udp.example.com. 3600 IN SRV 10 50 5060 sip.telnyx.com.
  _sip._udp.example.com. 3600 IN SRV 20 50 5060 sip-eu.telnyx.com.

- Regional FQDNs: sip.telnyx.com (US), sip-eu.telnyx.com (Europe), sip-ca.telnyx.com (Canada), sip-au.telnyx.com (Australia). Query these FQDNs to obtain the current IPs.
- Why SRV over A records:
  - Multiple IPs per target with priority and weight
  - Port and transport embedded in DNS
  - Better failover behavior without manual IP juggling
- Verification:
  - dig _sip._udp.example.com SRV
  - dig sip.telnyx.com A
- Troubleshooting tips:
  - Ensure the SRV target has a trailing dot (e.g., sip.telnyx.com.) in many DNS UIs
  - Some PBXs require SRV lookups to be explicitly enabled and must be configured with your domain, not a raw IP
  - For balanced distribution, use equal weights; note some SIP stacks cache the first resolved IP

## SIP response codes that influence failover
Telnyx triggers retries/failover on specific SIP outcomes:
- Triggers failover: 408 (Request Timeout), 480 (Temporarily Unavailable), 503 (Service Unavailable), 504 (Server Timeout), and transport/network errors.
- Does not trigger failover (treated as connected or final by design): 180 (Ringing), 200 (OK/answered), 404 (Not Found), 486 (Busy Here), 603 (Decline).
- Telnyx diagnostic codes you may encounter during routing/media setup:
  - PE1–PE6 with 503: no routes found (check destination/routing)
  - B3 with 488: SRTP/SDP mismatch (align media encryption and codec settings)
  - See [SIP Response Codes](sip-response-codes.md) for the full catalog of D‑, P‑, R‑, PE‑, T‑, and B‑series codes and resolutions.

## Putting it together: key configuration fields
- AnchorSite (media):
  - anchorsite_override = "latency" for automatic, or set to a PoP name (e.g., "Chicago, IL") for manual.
- Routing method (signaling/route order):
  - default_routing_method = "sequential" or "round-robin".
- Forward on failure:
  - call_forwarding.forwarding_type = "on_failure" to send failed calls to PSTN after all SIP routes are exhausted.

## Best practices
- Prefer SRV-based domains (sip.telnyx.com, etc.) over hardcoded IPs; let DNS provide current, redundant targets.
- If using AnchorSite latency mode, ensure ICMP is permitted to your SIP endpoint and include the SIP Connection username (Contact or X-Telnyx-Username) for credential-auth flows.
- Keep firewall rules updated for Telnyx media and signaling; AnchorSite optimizes media, while signaling may enter via different regional IPs.
- Test and observe failover: use dig to verify SRV, and monitor which response codes appear when calls reroute.
- Round-robin is simple and even, but not load-aware; use it when equal distribution (not dynamic load shedding) is acceptable.
