---
title: Dynamic E911
summary: Dynamic E911 delivers location information to PSAPs during emergency calls.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911/index
    content_hash: f23de3f489e2ca22db6b93ba6cd9b94daa8b73b01d11c8f98afccb7d5a2813c4
updated_at: 2026-04-10T00:00:00Z
---

# Dynamic E911

Dynamic E911 delivers location information to PSAPs during emergency calls. Two methods available:

| Method              | Use case                             | Location source         |
| ------------------- | ------------------------------------ | ----------------------- |
| API-based addresses | Fixed locations (offices, buildings) | Pre-provisioned via API |
| GPS coordinates     | Mobile devices, wearables, IoT       | PIDF-LO in SIP INVITE   |

## API-based addresses

Pre-provision addresses and endpoints, then reference IDs in SIP headers during calls.

### Create emergency address

[POST /v2/dynamic\_emergency\_addresses](https://developers.telnyx.com/api-reference/dynamic-emergency-addresses/create-a-dynamic-emergency-address)

```json theme={null}
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

Response includes:

* `id` - Address UUID for endpoint association
* `sip_geolocation_id` - Include in `Geolocation` header
* `status` - `pending` during validation, `activated` when ready

### Create emergency endpoint

[POST /v2/dynamic\_emergency\_endpoints](https://developers.telnyx.com/api-reference/dynamic-emergency-endpoints/create-a-dynamic-emergency-endpoint)

```json theme={null}
{
  "dynamic_emergency_address_id": "uuid-from-address",
  "callback_number": "+13125550000",
  "caller_name": "Jane Doe"
}
```

Response includes:

* `sip_from_id` - Include in `From` or `P-Asserted-Identity` header

### SIP INVITE format

Include both IDs in emergency call INVITE:

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

## GPS coordinates (PIDF-LO)

Pass real-time coordinates in PIDF-LO format for mobile devices, wearables, and IoT.

### Coordinate format

| Parameter | Range              | Notes                |
| --------- | ------------------ | -------------------- |
| Latitude  | -90 to +90         | Negative = South     |
| Longitude | -180 to +180       | Negative = West      |
| Precision | 6-8 decimal places | Meter-level accuracy |

### SIP INVITE with PIDF-LO

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

### PIDF-LO requirements

| Element          | Requirement                              |
| ---------------- | ---------------------------------------- |
| `<gml:pos>`      | Latitude then longitude, space-separated |
| `srsName`        | Must be `urn:ogc:def:crs:EPSG::4326`     |
| `<dm:timestamp>` | ISO 8601 format                          |

## Testing

Use test number `933` to simulate emergency calls without dispatching services.

## Address field limits

| Field                     | Required | Max Length | PIDF-LO Element |
| ------------------------- | -------- | ---------- | --------------- |
| house\_number             | No       | 6          | HNO             |
| house\_suffix             | No       | 45         | HNS             |
| street\_pre\_directional  | No       | 2          | PRD             |
| street\_name              | Yes      | 200        | RD              |
| street\_suffix            | No       | 45         | STS             |
| street\_post\_directional | No       | 2          | POD             |
| extended\_address         | No       | 60\*       | LOC             |
| locality                  | Yes      | 100        | A3              |
| administrative\_area      | Yes      | 2          | A1              |
| postal\_code              | Yes      | 10         | PC              |
| country\_code             | Yes      | 2          | country         |
| caller\_name              | No       | 50         | -               |

\*Common terms auto-abbreviated: APARTMENT→APT, FLOOR→FL, SUITE→STE, BUILDING→BLDG, ROOM→RM


## Related Pages

- [Dynamic Variables](../runbooks/dynamic-variables.md)
