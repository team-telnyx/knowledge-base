---
title: Emergency Services (E911)
summary: Covers how to register emergency addresses, enable and test E911 on Telnyx
  numbers, dial emergency services globally, and handle advanced scenarios like Dynamic
  E911 and Microsoft Teams integration.
sources:
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/2819213-bulk-edit-numbers-emergency-services
- url: https://support.telnyx.com/en/articles/8712528-dialing-emergency-services
- url: https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers
- url: https://support.telnyx.com/en/articles/9039036-emergency-services-and-ipnd-in-australia
- url: https://support.telnyx.com/en/articles/9718403-microsoft-teams-emergency-call-routing
updated_at: 2026-06-11T11:37:16Z
---

# Emergency Services (E911)

*Part 2 of 2 — see also: [Part 1](emergency-services-e911--part-1.md)*

Covers how to register emergency addresses, enable and test E911 on Telnyx numbers, dial emergency services globally, and handle advanced scenarios like Dynamic E911 and Microsoft Teams integration.

## Supported Emergency Numbers

Telnyx supports emergency numbers across many countries. Below is a summary of key numbers; see the [full list on the Telnyx Help Center](https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers) for complete details.

| Country | Emergency Number(s) |
|---|---|
| United States | 911 (Emergency), 933 (E911 test), 711 (TRS), 811, 988 |
| Canada | 911 |
| United Kingdom | 999, 112 (Emergency), 101, 111, 105, 119 |
| Australia | 000, 112 (Emergency) |
| Germany | 112, 110 |
| France | 112, 15, 17, 18 |
| Mexico | 911, 070–089 |
| Brazil | 190–193, 197 |
| Netherlands | 112 |
| Ireland | 112, 999 |
| New Zealand | 111 |
| Singapore | 999, 995 |

933 testing is available for the United States and Canada only. For international emergency-service testing options, contact Telnyx Support.

## Emergency Services and IPND in Australia

Australia's primary emergency number is **000**. Emergency calls can be made without charge, even if the mobile service is suspended, disconnected, or out of credit. Calls to 000 are answered by a Telstra Emergency Call Service Operator who transfers the call to the required Emergency Service Organisation (Police, Fire, or Ambulance).

**112** is Australia's secondary emergency service number, recognised globally for mobile phones, with the same functionality as 000. Mobile phones sold in Australia since 2002 recognise 000 as the emergency number; international roamers or phones purchased overseas can dial either 000 or 112.

### Integrated Public Number Database (IPND)

Telnyx uploads your name, address, and telephone numbers to the IPND. The IPND stores Public Number Customer Data (PNCD) — telephone number, name, service address, and directory-related information — used to assist in emergency services and law enforcement.

Data users with IPND access include Directory Related Service Providers, Emergency Call Service Operators, and Enforcement Agencies.

Because IPND data is used for emergency dispatch:

- Keep Telnyx updated with any contact-data changes (e.g., a new service address) so IPND can be updated accordingly.
- If the address you provided is not the physical address from which you are calling, contact the support team with the correct contact name and telephone number.
- To view your phone number's IPND status, update it, or opt out of directory listings, contact [support@telnyx.com](mailto:support@telnyx.com) or use the chat function.

For more information, visit [www.triplezero.gov.au](http://www.triplezero.gov.au).

## Dynamic E911

Dynamic E911 is used when the emergency location must be supplied dynamically — for nomadic users, mobile applications, MLTS environments, WebRTC applications, wearables, or IoT devices. It may require pre-provisioned dynamic emergency addresses or location information supplied during the emergency call.

### Testing Dynamic E911

Before testing with 933:

1. Confirm the dynamic emergency address or endpoint is fully configured and active.
2. Confirm your application or SIP platform sends the expected dynamic location information.
3. Dial 933 through the same call path used for emergency calls.
4. Confirm the readback matches the expected dynamic location.

If the location is wrong, treat the test as failed. Correct the configuration before relying on that call path for emergency calling. For implementation details, see the [Dynamic E911 developer documentation](https://developers.telnyx.com/docs/voice/sip-trunking/emergency-calling-dynamic-e911).

If you are unsure whether you need regular or Dynamic E911, contact [support@telnyx.com](mailto:support@telnyx.com) with your use case before going live.

## Microsoft Teams Emergency Call Routing

Microsoft Teams uses **Dynamic Location Routing** to ensure emergency calls are directed to the correct Public Safety Answering Point (PSAP) based on the caller's current position.

### PIDF-LO in SIP INVITE

Location data is embedded in the SIP INVITE using **PIDF-LO** (Presence Information Data Format Location Object), a standardised XML protocol. When an emergency call is placed, Microsoft Teams includes emergency address details within the SIP INVITE MIME part. Telnyx processes this information to route the call to the appropriate PSAP.

The PIDF-LO data includes:

- **Geodetic location** — latitude and longitude coordinates (e.g., `33.38075 -111.75344`).
- **Civic address** — country, state (A1), city (A3), street (RD), house number (HNO), postal code (PC), and other fields.
- **Method** — the source of the location data (e.g., `LIS` or `ASSIST`).
- **Confidence** — reliability indicator (e.g., `low`, `normal`).

Example PIDF-LO XML excerpt:

```xml
<presence xmlns="urn:ietf:params:xml:ns:pidf" entity="-">
  <tuple id="tuple0">
    <status>
      <geopriv xmlns="urn:ietf:params:xml:ns:pidf:geopriv10">
        <location-info>
          <Point srsName="urn:ogc:def:crs:EPSG::4326" xmlns="http://www.opengis.net/gml">
            <pos>33.38075 -111.75344</pos>
          </Point>
          <civicAddress xmlns="urn:ietf:params:xml:ns:pidf:geopriv10:civicAddr">
            <country>US</country>
            <A1>AZ</A1>
            <A3>Mesa</A3>
            <RD>South Val Vista Drive</RD>
            <HNO>1939</HNO>
            <PC>85204</PC>
          </civicAddress>
        </location-info>
        <method>ASSIST</method>
      </geopriv>
    </status>
  </tuple>
</presence>
```

For more on configuring Microsoft Teams with Telnyx, see [Microsoft Teams Direct Routing](microsoft-teams-direct-routing.md) and the [Microsoft Dynamic Emergency Calling documentation](https://learn.microsoft.com/en-us/microsoftteams/configure-dynamic-emergency-calling).

## API and Bulk Programmatic Setup

The Portal workflow is recommended for most customers. For programmatic or bulk management:

1. Validate or create an emergency-service address via the Telnyx API.
2. Assign the emergency address to the phone number's emergency settings.
3. Confirm the number's emergency status is active before relying on it for emergency calling.
4. For multiple numbers, use the documented bulk phone number update workflow.

## Troubleshooting

Contact [support@telnyx.com](mailto:support@telnyx.com) if:

- The Portal rejects the emergency address.
- The number remains pending or does not show as ready/active.
- The 933 readback is incorrect.
- The call does not present the E911-enabled Telnyx number.
- You are configuring Dynamic E911, MLTS, WebRTC, mobile, IoT, or another advanced workflow.

When contacting support, include:

- The Telnyx phone number.
- The emergency service address.
- The approximate date/time (with timezone) of the test or attempted setup.
- The caller ID your system presented to Telnyx.
- The address you expected vs. the address that was read back.
- Any screenshot or exact error message from the Portal.
- Relevant PBX/SBC/UCaaS routing details.
