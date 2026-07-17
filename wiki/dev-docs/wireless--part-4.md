---
title: Wireless
summary: Telnyx Wireless provides API-driven cellular connectivity for IoT and mobile
  devices. This page covers SIM and eSIM provisioning, lifecycle management, SIM Card
  Groups, bulk operations, data routing (public IPs, Private Wireless Gateways, Traffic
  Policy Profiles, Wireless Blocklists), data usage monitoring and notifications,
  Wireless Detail Records, OTA updates, VoLTE with mobile phone numbers and call features,
  IoT pricing, connectivity troubleshooting, AT commands, and step-by-step setup guides
  for a range of supported devices including Raspberry Pi HATs, Particle Boron, Nordic
  nRF9160, Cradlepoint IBR200, Pepwave Max BR1 Mini, GL-MiFi, and Mikrotik wAP LTE.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/at-commands/index
- url: https://developers.telnyx.com/docs/iot-sim/bulk-sim-actions/index
- url: https://developers.telnyx.com/docs/iot-sim/call-forwarding-recording
- url: https://developers.telnyx.com/docs/iot-sim/connectivity-troubleshooting/index
- url: https://developers.telnyx.com/docs/iot-sim/cradlepoint-ibr200-cellular/index
- url: https://developers.telnyx.com/docs/iot-sim/data-usage-notifications
- url: https://developers.telnyx.com/docs/iot-sim/edge-deployment/index
- url: https://developers.telnyx.com/docs/iot-sim/get-started/index
- url: https://developers.telnyx.com/docs/iot-sim/glmifi-router
- url: https://developers.telnyx.com/docs/iot-sim/iot-pricing
- url: https://developers.telnyx.com/docs/iot-sim/messaging-settings/index
- url: https://developers.telnyx.com/docs/iot-sim/mikrotik-wap-lte
- url: https://developers.telnyx.com/docs/iot-sim/mobile-phone-numbers/index
- url: https://developers.telnyx.com/docs/iot-sim/nordic-semiconductor
- url: https://developers.telnyx.com/docs/iot-sim/ordering-sims/index
- url: https://developers.telnyx.com/docs/iot-sim/ota-updates
- url: https://developers.telnyx.com/docs/iot-sim/particle-boron-lte-kit
- url: https://developers.telnyx.com/docs/iot-sim/pepwave-max-br1-mini-lte
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateway-how-to/index
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways
- url: https://developers.telnyx.com/docs/iot-sim/public-ips/index
- url: https://developers.telnyx.com/docs/iot-sim/sim-card-groups/index
- url: https://developers.telnyx.com/docs/iot-sim/sim-lifecycle
- url: https://developers.telnyx.com/docs/iot-sim/sim7600-a-rasp-pui-hat/index
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-cellular-iot-hat
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-rasp-pi-hat
- url: https://developers.telnyx.com/docs/iot-sim/traffic-policy-profiles
- url: https://developers.telnyx.com/docs/iot-sim/voice-enabled-iot/index
- url: https://developers.telnyx.com/docs/iot-sim/wireless-blocklists
- url: https://developers.telnyx.com/docs/iot-sim/wireless-detail-records
- url: https://developers.telnyx.com/docs/iot-sim/wireless-overview/index
updated_at: 2026-07-17T09:19:06Z
---

# Wireless

*Part 4 of 6 — see also: [Part 1](wireless--part-1.md), [Part 2](wireless--part-2.md), [Part 3](wireless--part-3.md), [Part 5](wireless--part-5.md), [Part 6](wireless--part-6.md)*

Telnyx Wireless provides API-driven cellular connectivity for IoT and mobile devices. This page covers SIM and eSIM provisioning, lifecycle management, SIM Card Groups, bulk operations, data routing (public IPs, Private Wireless Gateways, Traffic Policy Profiles, Wireless Blocklists), data usage monitoring and notifications, Wireless Detail Records, OTA updates, VoLTE with mobile phone numbers and call features, IoT pricing, connectivity troubleshooting, AT commands, and step-by-step setup guides for a range of supported devices including Raspberry Pi HATs, Particle Boron, Nordic nRF9160, Cradlepoint IBR200, Pepwave Max BR1 Mini, GL-MiFi, and Mikrotik wAP LTE.

## VoLTE

**Beta** — VoLTE is in beta. API reference and detailed configuration docs coming soon.

Add a real phone number to any eSIM-capable device. No second phone, no SIP client, no app — just a native cellular line with full API control.

### Mobile Phone Numbers

When you enable voice on a SIM, Telnyx assigns a Mobile Phone Number — a real +E.164 number. Inbound calls ring the device natively. Outbound calls show your number as caller ID.

**Enabling Voice**

Voice is enabled per-SIM via action endpoints, not by patching a field.

| Action | Endpoint |
| --- | --- |
| [Enable Voice](/api-reference/sim-cards/request-a-sim-card-enable) | `POST /sim_cards/{id}/actions/enable_voice` |
| [Disable Voice](/api-reference/sim-cards/request-a-sim-card-disable) | `POST /sim_cards/{id}/actions/disable_voice` |
| [Bulk Enable Voice](/api-reference/sim-cards/request-bulk-enabling-voice-on-sim-cards) | `POST /sim_cards/actions/bulk_enable_voice` |
| [Bulk Disable Voice](/api-reference/sim-cards/request-bulk-disabling-voice-on-sim-cards) | `POST /sim_cards/actions/bulk_disable_voice` |

`enable_voice` accepts an optional `connection_id` to associate with a Mobile Voice Connection.

**Mobile Phone Number**

Once voice is enabled, manage the assigned number via:

| Action | Endpoint |
| --- | --- |
| [List Numbers](/api-reference/mobile-phone-numbers/list-mobile-phone-numbers) | `GET /mobile_phone_numbers` |
| [Get Number](/api-reference/mobile-phone-numbers/retrieve-a-mobile-phone-number) | `GET /mobile_phone_numbers/{id}` |
| [Update Number](/api-reference/mobile-phone-numbers/update-a-mobile-phone-number) | `PATCH /mobile_phone_numbers/{id}` |

**Configurable Settings**

| Setting | Description |
| --- | --- |
| `call_forwarding` | Forward calls on no-answer, busy, or unconditional |
| `call_recording` | Record inbound, outbound, or both |
| `caller_id_name_enabled` | Enable CNAM lookup on outbound calls |
| `cnam_listing` | Register business name for inbound CNAM display |
| `noise_suppression` | AI noise reduction on calls |
| `inbound_call_screening` | Filter inbound calls before connecting |
| `connection_id` | Associate with a Mobile Voice Connection |
| `customer_reference` | Your own reference string |
| `tags` | Arbitrary tags for filtering |
| `inbound` / `outbound` | Routing configuration per direction |

**Mobile Voice Connection**

The voice application attached to a number — controls webhooks, API version, and routing.

| Action | Endpoint |
| --- | --- |
| [List Connections](/api-reference/mobile-phone-numbers/list-mobile-voice-connections) | `GET /mobile_voice_connections` |
| [Create Connection](/api-reference/mobile-phone-numbers/create-a-mobile-voice-connection) | `POST /mobile_voice_connections` |
| [Get Connection](/api-reference/mobile-phone-numbers/retrieve-a-mobile-voice-connection) | `GET /mobile_voice_connections/{id}` |
| [Update Connection](/api-reference/mobile-phone-numbers/update-a-mobile-voice-connection) | `PATCH /mobile_voice_connections/{id}` |
| [Delete Connection](/api-reference/mobile-phone-numbers/delete-a-mobile-voice-connection) | `DELETE /mobile_voice_connections/{id}` |

**Connection Settings**

| Setting | Description |
| --- | --- |
| `webhook_event_url` | Where call events are sent |
| `webhook_event_failover_url` | Backup URL if primary fails |
| `webhook_timeout_secs` | How long to wait for webhook response |
| `outbound` / `inbound` | Routing configuration per direction |
| `active` | Whether the connection is active |

### Call Forwarding, Recording & Screening

All settings below are configured via [`PATCH /mobile_phone_numbers/{id}`](/api-reference/mobile-phone-numbers/update-a-mobile-phone-number).

**Call Forwarding**

Set the `call_forwarding` object to route calls when the device is unavailable.

| Type | Behavior |
| --- | --- |
| `unconditional` | All calls forward immediately — device never rings |
| `no_answer` | Forward after timeout (device rings first) |
| `busy` | Forward when line is in use |

Forward to any number — landline, mobile, SIP connection, or Call Control application.

**Call Recording**

Set `call_recording` to record inbound, outbound, or both. Recordings are accessible through the standard Telnyx Recordings API — same storage, retrieval, and webhooks as Call Control recordings.

**Inbound Call Screening**

Inbound Call Screening automatically blocks or flags inbound calls based on caller reputation and SHAKEN/STIR attestation. The feature is free on any number.

Screening evaluates three factors:

| Factor | Description |
| --- | --- |
| **Number Reputation** | Cross-references caller identity against CallerAPI, Nomorobo, and YouMail databases |
| **Number Validation** | Checks whether the originating number is valid and exists |
| **SHAKEN/STIR Attestation** | Validates Caller ID authenticity — screens calls with Attestation C (unauthenticated) or Invalid (certificate error) |

**Handling modes**

| Mode | Behavior |
| --- | --- |
| **Flag** | Call connects but displays "SPAM LIKELY" in the From and P-Asserted-ID headers. A custom SIP header carries the screening status for your routing logic. |
| **Reject** | Call is blocked at the network level and never reaches your infrastructure. |

**Enabling call screening**

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Go to **My Numbers**, select a number, and click **Edit**.
3. Under the **Voice** tab, enable **Inbound Call Screening** and choose Flag or Reject.

You can also enable it via `PATCH /mobile_phone_numbers/{id}` by setting the `inbound_call_screening` field.

**Webhook integration**

Enable webhooks to receive the `call_screening_result` field in the `call.initiated` webhook payload.

Number reputation screening applies to US and Canada calls. SHAKEN/STIR screening applies to North America.

**Other Settings**

| Setting | Description |
| --- | --- |
| `noise_suppression` | AI noise reduction for loud environments |

**Example**

```
{
  "call_forwarding": {
    "forwarding_type": "no_answer",
    "forwarding_number": "+15551234567",
    "timeout_secs": 30
  },
  "call_recording": {
    "inbound": "enabled",
    "outbound": "disabled"
  },
  "noise_suppression": "enabled"
}
```

## Messaging

Coming soon.

## IoT Pricing

There are 3 components to Telnyx IoT pricing:

1. One time charge (OTC)
2. Monthly recurring charges (MRC)
3. Data usage

### One Time Charge

Each SIM card has a one time charge of $1. If the destination for the SIM card is outside of the U.S. mainland there is a $10 shipping charge. eSIMs have a one time charge of $0.70 and no shipping charge (eSIMs are delivered over-the-air). These costs are incurred upon ordering SIMs in the Mission Control Portal.

### Monthly Recurring Charges

Once a SIM is registered and showing up in your Mission Control Portal it will incur a monthly charge of $2/SIM.

This charge is reduced to $0.20/SIM for SIMs that are deactivated. You can deactivate a SIM by disabling them in the Portal or using [this endpoint](/api-reference/sim-cards/request-a-sim-card-disable).

### Data Usage

Data usage is billed on a tiered basis (upload and download) and the data rate is determined by the location in which the SIM is in use and the amount of data used across the account. Data usage on Telnyx SIMs is billed at a different rate depending on the country of usage - this is determined by the MCC that is being used by the SIM.

Each country that Telnyx Wireless operates in is mapped to a zone. Data usage is charged based on 9 zones and the amount of data consumed across the account.

[View a full cost breakdown](https://support.telnyx.com/en/articles/3296669-programmable-wireless-pricing) of data usage, mapping each country to their relevant zone.
