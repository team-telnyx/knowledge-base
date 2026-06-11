---
title: SIP Trunking
summary: Telnyx SIP Trunking provides carrier-grade voice connectivity using SIP Connections
  for inbound traffic and Outbound Voice Profiles for outbound routing, with features
  including dynamic E911, noise suppression, jitter buffering, SIP URI calling, external
  transfers, and configurable routing with automatic failover.
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/external-transfers
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/jitter-buffer
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/noise-suppression/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/sip-uri-calling
- url: https://developers.telnyx.com/docs/voice/sip-trunking/get-started/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/livekit-configuration-guide
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/ip-whitelisting/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/srv-records
- url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/stun-turn-servers
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/anchorsite-configuration
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/failover-and-retries/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/routing/round-robin-routing/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/troubleshooting/response-codes/index
updated_at: 2026-06-11T10:45:55Z
---

# SIP Trunking

*Part 3 of 3 — see also: [Part 1](sip-trunking--part-1.md), [Part 2](sip-trunking--part-2.md)*

Telnyx SIP Trunking provides carrier-grade voice connectivity using SIP Connections for inbound traffic and Outbound Voice Profiles for outbound routing, with features including dynamic E911, noise suppression, jitter buffering, SIP URI calling, external transfers, and configurable routing with automatic failover.

## Dynamic E911 Emergency Calling

Dynamic E911 delivers location information to PSAPs during emergency calls. Two methods are available:

| Method | Use case | Location source |
| --- | --- | --- |
| API-based addresses | Fixed locations (offices, buildings) | Pre-provisioned via API |
| GPS coordinates (PIDF-LO) | Mobile devices, wearables, IoT | PIDF-LO in SIP INVITE |

### API-Based Addresses

Pre-provision addresses and endpoints, then reference IDs in SIP headers during calls. Telnyx recommends pre-provisioning a persistent emergency address rather than relying on just-in-time provisioning, as dynamically provisioned endpoints may have a delay before activation. If an emergency call is initiated before a dynamically provisioned endpoint is fully activated, the call will be routed to a national emergency call center.

**1. Create emergency address** — `POST /v2/dynamic_emergency_addresses`:

```json
{
  "house_number": "1901",
  "street_pre_directional": "W",
  "street_name": "MADISON",
  "street_suffix": "ST",
  "locality": "CHICAGO",
  "administrative_area": "IL",
  "postal_code": "60612",
  "country_code": "US"
}
```

Response includes `id` (address UUID), `sip_geolocation_id` (for `Geolocation` header), and `status` (`pending` during validation, `activated` when ready).

**2. Create emergency endpoint** — `POST /v2/dynamic_emergency_endpoints`:

```json
{
  "dynamic_emergency_address_id": "uuid-from-address",
  "callback_number": "+13125550000",
  "caller_name": "Jane Doe"
}
```

Response includes `sip_from_id` (for `From` or `P-Asserted-Identity` header).

**3. SIP INVITE format:**

```
From: <sip:{sip_from_id}@origin.example.com>
Geolocation: {sip_geolocation_id}
```

Or using `P-Asserted-Identity`:

```
P-Asserted-Identity: <sip:{sip_from_id}@origin.example.com>
Geolocation: {sip_geolocation_id}
```

### GPS Coordinates (PIDF-LO)

Pass real-time coordinates in PIDF-LO format for mobile devices, wearables, and IoT. Latitude ranges from -90 to +90 (negative = South); longitude from -180 to +180 (negative = West). Use 6–8 decimal places for meter-level accuracy.

**Simple format with custom headers:**

```
Geolocation: <cid:location@example.com>
X-Latitude: latitude
X-Longitude: longitude
```

**Full MIME multipart format** uses `Content-Type: application/pidf+xml` with a `<presence>` element containing a `<gml:Point>` with `srsName="urn:ogc:def:crs:EPSG::4326"`. The `<gml:pos>` element contains latitude then longitude, space-separated. The `<dm:timestamp>` must be in ISO 8601 format.

Telnyx currently supports LIS and ASSIST as PIDF-LO methods. Other methods are not supported.

### Address Field Limits

| Field | Required | Max Length |
| --- | --- | --- |
| house_number | No | 6 |
| house_suffix | No | 45 |
| street_pre_directional | No | 2 |
| street_name | Yes | 200 |
| street_suffix | No | 45 |
| street_post_directional | No | 2 |
| extended_address | No | 60 |
| locality | Yes | 100 |
| administrative_area | Yes | 2 |
| postal_code | Yes | 10 |
| country_code | Yes | 2 |
| caller_name | No | 50 |

Common terms in `extended_address` are auto-abbreviated: APARTMENT→APT, FLOOR→FL, SUITE→STE, BUILDING→BLDG, ROOM→RM.

### Testing E911

Use test number `933` to simulate emergency calls without dispatching services.

## LiveKit Integration

To configure a SIP trunk between Telnyx and LiveKit:

**In Telnyx Mission Control Portal:**

1. Create an FQDN SIP Connection using the SIP URI from your LiveKit project settings.
2. Configure outbound calls authentication with credentials (username and password for LiveKit outbound trunk).
3. Assign an Outbound Voice Profile.
4. Assign phone numbers to the connection.

Optionally, configure a Programmable Voice Application for advanced features (call recording, IVR, TTS/STT, conversational AI) by creating an app with a webhook URL and inbound subdomain.

**In LiveKit:**

1. Create an inbound SIP trunk with the Telnyx phone number.
2. Create a dispatch rule to route incoming calls to a LiveKit room.
3. Create an outbound SIP trunk pointing to `sip.telnyx.com` with the Telnyx credentials. For Voice App integration, use the app subdomain instead and leave credentials blank.
4. **Set the `X-Telnyx-Username` custom header** to ensure calls are authenticated against your specific FQDN connection. This prevents accidental IP-based matches in shared cloud environments. Use LiveKit's `headers_to_attributes` mapping:

```json
{
  "trunk": {
    "name": "My outbound trunk",
    "address": "sip.telnyx.com",
    "numbers": ["+15555555555"],
    "authUsername": "<your_telnyx_username>",
    "authPassword": "<your_telnyx_password>",
    "headers_to_attributes": {
      "X-Telnyx-Username": "authUsername"
    }
  }
}
```

The header value must exactly match the username configured for credential authentication on the Telnyx FQDN connection.

## Troubleshooting

### SIP Response Codes

Telnyx uses custom response codes to diagnose call failures:

**D-Series (4XX — account/connection/profile issues):**

- **D1X:** Account & connection issues — concurrent call limits, disabled connections, inactive accounts
- **D2X:** Profile & channel limits — profile limits exceeded, missing destinations, rate limits
- **D3X:** Connection & URI issues — concurrent limits, invalid SIP URIs, invalid caller ID format, missing outbound voice profile (D38)
- **D4X:** Routing & destination issues — no route available, forbidden prefixes, SIP REFER not allowed (D42)
- **D5X:** Channel billing & verification — billing limits, unverified numbers, HD voice disabled
- **D6X:** Account tier restrictions — tier requires verified numbers, port pending, regulatory pending
- **D7–D9X:** No outbound profile (D7), missing E911 caller ID (D8), international rate limit (D9)

**P-Series (protocol violations):**

- Invalid Request-URI (P01), CANCEL without INVITE (P02), REGISTER with To tag (P04), CPS/message size limits (P05–P06), Contact header length violations (P14–P16, P51), empty destination (P18), registration failures (P29), username validation (P81–P83), hop count exceeded (P93)

**R-Series (registration & authentication):**

- Empty authentication username (R14), invalid/short/mismatched username (R16–R18), multiple Contact addresses (R47), user not registered (RG1)

**Routing & media codes:**

- **PE-Series (503):** No routes found
- **TV1 (503):** Downstream carrier termination issue
- **TM1 (403):** No rates for destination prefix
- **B3 (488):** SRTP mismatch — encrypted media expected

**488 Not Acceptable Media** can result from: private IP in SDP (use public IP), T.38 fax mismatch, IPv6 addresses (use IPv4), unsupported codecs (use G.711, G.722, G.729, or Opus), or SDP encryption conflicts.

### Debugging Tools

The Mission Control Portal provides a SIP Call Flow Tool under **Reporting → Debugging**. Search CDRs by criteria, then inspect individual calls for SIP message flows, QoS stats, session info, and PCAP exports.

### Common Troubleshooting Checks

- **SIP URI calls fail:** Verify the feature is enabled, username starts with a non-numeric character, access control permits the source, endpoint is registered, and firewall allows SIP traffic.
- **External transfers fail:** Verify an active inbound call exists, Diversion header is present with the correct Telnyx number, outbound profile allows the destination, and destination is in E.164 format.
- **One-way audio:** Verify STUN server is reachable, UDP port 3478 is allowed outbound, and RTP media ports are open bidirectionally.
- **SRV records not resolving:** Verify trailing dot on target FQDN, check TTL expiration, and confirm DNS propagation.
- **PBX not using SRV:** Enable SRV lookup, configure PBX to use domain not IP, and check PBX logs for DNS query behavior.
