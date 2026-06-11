---
source_url: https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers
scraped: 2026-06-11
---

Using Telnyx SIM with Teltonika 4G/LTE Routers | Telnyx Help Center

[Skip to main content](#main-content)

# Using Telnyx SIM with Teltonika 4G/LTE Routers

Configuring Teltonika 4G/LTE Routers involves several key steps to ensure optimal performance and connectivity

S

Written by Shubham

June 9, 2025

Table of contents

Teltonika LTE routers are widely used in IoT, industrial, and remote networking applications. Setting up a Telnyx SIM on a Teltonika router ensures a secure and reliable cellular connection. This guide provides step-by-step instructions to configure a Teltonika LTE router with a Telnyx SIM—and adds robust failover recovery with auto-reboot, plus RMS cloud integration for managing large SIM fleets.

[![4G Teltonika Trb 140 Lte Router, For Industrial at ₹ 12000/piece in Chennai  | ID: 2848977683188](https://downloads.intercomcdn.com/i/o/ltcafuzd/1373051870/070673890c0637d5e18069b0c8b7/pri-gateway-500x500.png?expires=1781167500&signature=367cb719d71748afb1414d0ec587c5957987d66bc3f421053e8a5b3eb9509fe0&req=dSMgFcl7nIlYWfMW1HO4zYQPGUrKvv83zzUf010yuTet0MZ3j4RRpJxSC5j5%0AdOoGDAt76kfo8SxfRu0%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1373051870/070673890c0637d5e18069b0c8b7/pri-gateway-500x500.png?expires=1781167500&signature=367cb719d71748afb1414d0ec587c5957987d66bc3f421053e8a5b3eb9509fe0&req=dSMgFcl7nIlYWfMW1HO4zYQPGUrKvv83zzUf010yuTet0MZ3j4RRpJxSC5j5%0AdOoGDAt76kfo8SxfRu0%3D%0A)

## 1. Initial Setup

**Insert the SIM Card:**

* Power off the router.
* Insert your active Telnyx SIM into the designated SIM slot.
* Ensure the SIM is securely seated to prevent connectivity issues.

**Connect to Power and Computer:**

* Power on the router using the included adapter.
* Use an Ethernet cable to connect the router’s LAN port to your computer.

---

## 2. Accessing the Web Interface

**Default IP Address:**

* Open a browser and enter: `http://192.168.2.1`

**Login Credentials:**

* **Username:** `admin`
* **Password:** (printed on the router label)

⚠️ On first login, you may be prompted to change the password.

---

## 3. Configuring APN Settings for Telnyx

**Navigate to:** `Network > Interfaces`

**Edit Mobile Interface:**

* Click the pencil icon next to `mob1s1a1` (mobile interface).
* Uncheck **Auto APN**.
* Enter the following:

  + **APN:** `data00.telnyx`
  + **Username/Password:** leave blank unless instructed.

**Save Changes:**

* Click **Save & Apply**.

[![Editing Auto APN - Teltonika Networks Wiki](https://downloads.intercomcdn.com/i/o/ltcafuzd/1373066573/fda63feeaa05aafef7d6c7db350d/1004px-Custom_APN_v2.png?expires=1781167500&signature=3f3ff1ab2f949c3bc7512f8f2488ab9efd992237a83ebb7c21f81efd260433c2&req=dSMgFcl4m4RYWvMW1HO4zcqWAJJkcGu886y3ffSDx8KHCenSYjdv%2FKKNtlyg%0AtDlmkwXD9Z8eJFy0lvI%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1373066573/fda63feeaa05aafef7d6c7db350d/1004px-Custom_APN_v2.png?expires=1781167500&signature=3f3ff1ab2f949c3bc7512f8f2488ab9efd992237a83ebb7c21f81efd260433c2&req=dSMgFcl4m4RYWvMW1HO4zcqWAJJkcGu886y3ffSDx8KHCenSYjdv%2FKKNtlyg%0AtDlmkwXD9Z8eJFy0lvI%3D%0A)

## 4. Verifying Connectivity

**Check Status:**

* Go to `Status > Network Information`.
* Confirm:

  + **Connected** status
  + **Assigned IP address**
  + **Signal strength** is within usable range

---

## 5. Configuring Auto-Reboot for Network Recovery (Recommended)

To ensure the modem recovers from service interruptions or poor network connectivity, configure the **auto-reboot watchdog** feature:

**Navigate to:** `System > Auto Reboot`

**Enable Watchdog Monitoring:**

* Enable **Auto Reboot**.
* Set **Reboot Conditions**:

  + Select **Ping Reboot**
  + Enter reliable targets like `8.8.8.8` and `1.1.1.1`
* Set **Ping Interval** and **Retry Count**:

  + E.g., ping every 60 seconds, reboot after 3 failures
* Optional: Enable **Scheduled Reboot** (e.g., daily at 3 AM)

**Apply Settings:**

* Click **Save & Apply**

🔁 This helps the modem recover automatically from outages without manual intervention—especially critical for remote or unattended deployments.

---

## 6. Optional: Teltonika RMS for Centralized Fleet Management

If you’re deploying many Teltonika routers with Telnyx SIMs, using **Teltonika RMS** (Remote Management System) is highly recommended.

## What is RMS?

A **cloud-based management platform** by Teltonika that enables:

* Real-time monitoring of devices and SIMs
* Remote firmware/configuration updates
* Command-line access for remote diagnostics
* Batch operations (e.g., set auto-reboot across 100+ routers)
* VPN tunnel setup and firewall configurations
* Alerts and logs for connection drops or reboot events

## Benefits for Telnyx SIM Users:

* Central dashboard to **track usage, signal, uptime**
* Minimize truck rolls with **remote troubleshooting**
* Set up **auto-reboot and APN settings** for all routers
* Monitor health of every modem in the field with automated alerts

## How to Start:

* Sign up at rms.teltonika-networks.com
* Register each device using the unique **RMS code** found in the web UI (`System > RMS`)
* Apply configuration templates or execute remote CLI scripts

💡 Telnyx customers managing LTE modems at scale will benefit immensely from RMS observability, bulk configuration, and failover automation.

---

## 7. Firmware & Security

* **Update Firmware**: `System > Firmware` – check for latest updates
* **Firewall**: Customize via `Network > Firewall`
* **VPN Support**: Available under `VPN` (OpenVPN, WireGuard, IPsec)

---

## 8. Backing Up Configuration

* Go to `System > Backup`
* Click **Generate** and download the backup for disaster recovery

---

## 9. Troubleshooting Tips

**No Internet:**

* Ensure SIM is active and APN is correct
* Confirm signal reception is sufficient
* Verify auto-reboot is configured in case of prolonged disconnection

**Weak Signal:**

* Move router to a better location
* Use external antennas to improve signal gain

---

Related Articles

[Using Telnyx SIM with Ubiquiti UniFi LTE Pro](https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro)[Using Telnyx SIM with InRouter300 Series Cellular Routers](https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers)

Did this answer your question?

😞😐😃

Table of contents
