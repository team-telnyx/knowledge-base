---
title: 'Telnyx Wireless IoT: Complete Guide'
summary: Plan, deploy, and operate Telnyx IoT SIM fleets — from ordering SIMs and
  configuring devices, to routing traffic with Private Wireless Gateways, enabling
  VoLTE voice, enforcing policies, monitoring usage, and troubleshooting connectivity.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/at-commands
- url: https://developers.telnyx.com/docs/iot-sim/bulk-sim-actions
- url: https://developers.telnyx.com/docs/iot-sim/call-forwarding-recording
- url: https://developers.telnyx.com/docs/iot-sim/connectivity-troubleshooting
- url: https://developers.telnyx.com/docs/iot-sim/cradlepoint-ibr200-cellular
- url: https://developers.telnyx.com/docs/iot-sim/data-usage-notifications
- url: https://developers.telnyx.com/docs/iot-sim/edge-deployment
- url: https://developers.telnyx.com/docs/iot-sim/get-started
- url: https://developers.telnyx.com/docs/iot-sim/glmifi-router
- url: https://developers.telnyx.com/docs/iot-sim/messaging-settings
- url: https://developers.telnyx.com/docs/iot-sim/mikrotik-wap-lte
- url: https://developers.telnyx.com/docs/iot-sim/mobile-phone-numbers
- url: https://developers.telnyx.com/docs/iot-sim/nordic-semiconductor
- url: https://developers.telnyx.com/docs/iot-sim/ordering-sims
- url: https://developers.telnyx.com/docs/iot-sim/ota-updates
- url: https://developers.telnyx.com/docs/iot-sim/particle-boron-lte-kit
- url: https://developers.telnyx.com/docs/iot-sim/pepwave-max-br1-mini-lte
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateway-how-to
- url: https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways
- url: https://developers.telnyx.com/docs/iot-sim/public-ips
- url: https://developers.telnyx.com/docs/iot-sim/sim-card-groups
- url: https://developers.telnyx.com/docs/iot-sim/sim-lifecycle
- url: https://developers.telnyx.com/docs/iot-sim/sim7600-a-rasp-pui-hat
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-cellular-iot-hat
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-rasp-pi-hat
- url: https://developers.telnyx.com/docs/iot-sim/traffic-policy-profiles
- url: https://developers.telnyx.com/docs/iot-sim/voice-enabled-iot
- url: https://developers.telnyx.com/docs/iot-sim/wireless-blocklists
- url: https://developers.telnyx.com/docs/iot-sim/wireless-detail-records
- url: https://developers.telnyx.com/docs/iot-sim/wireless-overview
updated_at: 2026-05-14T09:52:56Z
---

# Telnyx Wireless IoT: Complete Guide

*Part 2 of 2 — see also: [Part 1](telnyx-wireless-iot-complete-guide--part-1.md)*

Plan, deploy, and operate Telnyx IoT SIM fleets — from ordering SIMs and configuring devices, to routing traffic with Private Wireless Gateways, enabling VoLTE voice, enforcing policies, monitoring usage, and troubleshooting connectivity.

## AT commands and serial console tips
Use screen or minicom to send AT commands to modem ports (e.g., screen /dev/ttyUSB3). Common commands:
- AT — check modem responsiveness (OK)
- AT+COPS=? — list available networks (filters to SIM‑compatible carriers)
- AT+COPS=1,0,"Carrier Name" — manual PLMN selection
- AT+CCID — SIM ICCID
- AT+CREG? — network registration status
- AT+BANDS — manual band selection (advanced/testing)

Raspberry Pi notes: enable the serial port (raspi‑config → Interfacing Options → Serial), and use a Bluetooth keyboard/mouse if USB serial port enumeration is inconsistent. See [AT Commands](at-commands.md).

## Quick device setup references
All examples use APN data00.telnyx and require roaming enabled unless stated.
- Cradlepoint IBR200: create a Modem WAN profile, override APN to data00.telnyx, wait for first attach (can take up to 30 minutes). See [Cradlepoint IBR200 Cellular Router Setup Guide](cradlepoint-ibr200-cellular-router-setup-guide.md).
- Pepwave MAX BR1 Mini: update firmware, set Cellular Settings (Auto bands, Data Roaming: Any Countries), APN: Custom data00.telnyx. See [Pepwave Max BR1 Mini LTE Setup Guide](pepwave-max-br1-mini-lte-setup-guide.md).
- GL‑MiFi 4G Smart Router: log in at 192.168.8.1, set modem device and APN data00.telnyx. See [GL-MiFi 4G Smart Router Setup Guide](gl-mifi-4g-smart-router-setup-guide.md).
- Mikrotik wAP LTE Kit (US): update RouterOS, add APN profile (Telnyx, IPv4, Use Peer DNS, Default Route), allow roaming, insert SIM and verify registration. See [Mikrotik wAP LTE Kit - US Tutorial](mikrotik-wap-lte-kit-us-tutorial.md).
- Raspberry Pi SIM7600‑A HAT: install libqmi/udhcpc, set raw‑ip on wwan0, start network with data00.telnyx, acquire DHCP on wwan0. See [SIM7600-A Raspberry Pi 4G Hat Setup](sim7600-a-raspberry-pi-4g-hat-setup.md).
- Sixfab Cellular IoT HAT (BG96 LTE‑M/NB‑IoT): install Sixfab library and PPP installer; configure APN data00.telnyx; connect with pon/poff; check PPP0. See [Sixfab Cellular IoT HAT Setup](sixfab-cellular-iot-hat-setup.md).
- Sixfab 3G/4G Base HAT: run QMI script, set APN, use quectel‑CM to bring up data. See [Sixfab Raspberry Pi 3G/4G Hat](sixfab-raspberry-pi-3g-4g-hat.md).
- Nordic nRF9160 DK: update board and modem firmware with nRF Connect tools, insert Telnyx SIM, use LTE Link Monitor to attach automatically. See [Nordic Semiconductor nRF9160 DK Setup Guide](nordic-semiconductor-nrf9160-dk-setup-guide.md).
- Particle Boron LTE: enable third‑party SIM via custom firmware, set APN, and verify connection in Particle Console. See [Particle Boron LTE Kit Setup Guid](particle-boron-lte-kit-setup-guid.md).

## Where to go next
- Assign fleet policies: [SIM Card Groups](sim-card-groups.md), [Traffic Policy Profiles](traffic-policy-profiles.md), [Wireless Blocklists](wireless-blocklists.md), [Private Wireless Gateways](private-wireless-gateways.md).
- Expose devices inbound: [Public IPs](public-ips.md) or PWG + internet egress.
- Add voice and call features: [VoLTE](volte.md), [Mobile Phone Numbers](mobile-phone-numbers.md), [Call Forwarding, Recording & Screening](call-forwarding-recording-screening.md).
- Monitor and control usage: [Data Usage Notifications](data-usage-notifications.md), [Wireless Detail Records](wireless-detail-records.md), [OTA Updates](ota-updates.md).
- Run one‑off changes at scale: [Bulk Operations](bulk-operations.md).
