---
title: SIP Trunking on Telnyx
summary: Telnyx Elastic SIP Trunking provides elastic, programmable telephony over
  IP with multiple authentication methods, configurable outbound policies, call-quality
  features, and emergency calling support. This page consolidates the authentication
  options, configuration guides, caller ID and concurrency policies, advanced features,
  and emergency calling capabilities available on Telnyx SIP trunks.
sources:
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/credential-types/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/ip-authentication-token
- url: https://developers.telnyx.com/docs/voice/sip-trunking/authentication/tech-prefix
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/concurrent-limits
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/outbound-voice-profiles
- url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/p-charge-info-header
- url: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/external-transfers
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/jitter-buffer
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/noise-suppression/index
- url: https://developers.telnyx.com/docs/voice/sip-trunking/features/sip-uri-calling
updated_at: 2026-08-05T14:05:52Z
---

# SIP Trunking on Telnyx

*Part 5 of 5 — see also: [Part 1](sip-trunking-on-telnyx--part-1.md), [Part 2](sip-trunking-on-telnyx--part-2.md), [Part 3](sip-trunking-on-telnyx--part-3.md), [Part 4](sip-trunking-on-telnyx--part-4.md)*

Telnyx Elastic SIP Trunking provides elastic, programmable telephony over IP with multiple authentication methods, configurable outbound policies, call-quality features, and emergency calling support. This page consolidates the authentication options, configuration guides, caller ID and concurrency policies, advanced features, and emergency calling capabilities available on Telnyx SIP trunks.

## Dynamic E911

Dynamic E911 delivers location information to PSAPs during emergency calls. Two methods are available:

| Method | Use case | Location source |
| --- | --- | --- |
| API-based addresses | Fixed locations (offices, buildings) | Pre-provisioned via API |
| GPS coordinates | Mobile devices, wearables, IoT | PIDF-LO in SIP INVITE |

### API-based addresses

Pre-provision addresses and endpoints, then reference IDs in SIP headers during calls. Dynamically provisioning emergency endpoints may result in a delay before the associated address is fully available for routing. Telnyx recommends pre-provisioning a persistent emergency address rather than relying on just-in-time provisioning. In circumstances where an emergency call (e.g., 911) is initiated before a dynamically provisioned endpoint is fully activated, the call will be routed to a national emergency call center (PSAP).

**Create emergency address** — `POST /v2/dynamic_emergency_addresses`:

```
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

Response includes `id` (address UUID for endpoint association), `sip_geolocation_id` (include in `Geolocation` header), and `status` (`pending` during validation, `activated` when ready).

**Create emergency endpoint** — `POST /v2/dynamic_emergency_endpoints`:

```
{
  "dynamic_emergency_address_id": "uuid-from-address",
  "callback_number": "+13125550000",
  "caller_name": "Jane Doe"
}
```

Response includes `sip_from_id` (include in `From` or `P-Asserted-Identity` header).

**SIP INVITE format** — Include both IDs in emergency call INVITE:

```
INVITE sip:911@sip.telnyx.com SIP/2.0
From: <sip:{sip_from_id}@origin.example.com>
To: <sip:911@sip.telnyx.com>
Geolocation: {sip_geolocation_id}
```

Alternative using `P-Asserted-Identity`:

```
P-Asserted-Identity: <sip:{sip_from_id}@origin.example.com>
Geolocation: {sip_geolocation_id}
```

### GPS coordinates (PIDF-LO)

Pass real-time coordinates in PIDF-LO format for mobile devices, wearables, and IoT.

| Parameter | Range | Notes |
| --- | --- | --- |
| Latitude | -90 to +90 | Negative = South |
| Longitude | -180 to +180 | Negative = West |
| Precision | 6-8 decimal places | Meter-level accuracy |

**SIP INVITE format for PIDF-LO with GPS coordinates**:

```
INVITE sip:911@sip.telnyx.com SIP/2.0
From: <sip:+13125550100@sip.telnyx.com>
To: <sip:911@sip.telnyx.com>
Geolocation: <cid:location@example.com>
X-Latitude: latitude
X-Longitude: longitude
Content-Type: application/sdp
[SDP content]
```

**SIP INVITE format for PIDF-LO with MIME**:

```
INVITE sip:911@sip.telnyx.com SIP/2.0
From: <sip:+13125550100@sip.telnyx.com>
To: <sip:911@sip.telnyx.com>
Geolocation: <cid:location@example.com>
Content-Type: multipart/mixed;boundary=boundary1

--boundary1
Content-Type: application/sdp

[SDP content]

--boundary1
Content-Type: application/pidf+xml
Content-ID: <location@example.com>

<?xml version="1.0" encoding="UTF-8"?>
<presence xmlns="urn:ietf:params:xml:ns:pidf"
          xmlns:gp="urn:ietf:params:xml:ns:pidf:geopriv10"
          xmlns:gml="http://www.opengis.net/gml"
          xmlns:dm="urn:ietf:params:xml:ns:pidf:data-model"
          entity="sip:+13125550100@sip.telnyx.com">
  <dm:device id="device-001">
    <gp:geopriv>
      <gp:location-info>
        <gml:Point srsName="urn:ogc:def:crs:EPSG::4326">
          <gml:pos>41.8781 -87.6298</gml:pos>
        </gml:Point>
      </gp:location-info>
      <gp:usage-rules>
        <gp:retransmission-allowed>false</gp:retransmission-allowed>
      </gp:usage-rules>
    </gp:geopriv>
    <dm:timestamp>2024-01-15T10:30:00Z</dm:timestamp>
  </dm:device>
</presence>

--boundary1--
```

Telnyx currently supports LIS and ASSIST as PIDF-LO methods. Other methods are not supported.

**PIDF-LO requirements**:

| Element | Requirement |
| --- | --- |
| `<gml:pos>` | Latitude then longitude, space-separated |
| `srsName` | Must be `urn:ogc:def:crs:EPSG::4326` |
| `<dm:timestamp>` | ISO 8601 format |

### Testing

Use test number `933` to simulate emergency calls without dispatching services.

### Address field limits

| Field | Required | Max Length | PIDF-LO Element |
| --- | --- | --- | --- |
| house_number | No | 6 | HNO |
| house_suffix | No | 45 | HNS |
| street_pre_directional | No | 2 | PRD |
| street_name | Yes | 200 | RD |
| street_suffix | No | 45 | STS |
| street_post_directional | No | 2 | POD |
| extended_address | No | 60* | LOC |
| locality | Yes | 100 | A3 |
| administrative_area | Yes | 2 | A1 |
| postal_code | Yes | 10 | PC |
| country_code | Yes | 2 | country |
| caller_name | No | 50 | - |

*Common terms auto-abbreviated: APARTMENT→APT, FLOOR→FL, SUITE→STE, BUILDING→BLDG, ROOM→RM.
