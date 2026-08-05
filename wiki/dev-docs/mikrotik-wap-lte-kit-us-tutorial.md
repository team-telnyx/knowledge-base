---
title: Mikrotik wAP LTE Kit - US Tutorial
summary: Step-by-step guide for configuring the Mikrotik wAP LTE Kit (US) router with
  a Telnyx SIM card, covering firmware update, APN configuration, and roaming setup.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/mikrotik-wap-lte
updated_at: 2026-08-05T13:46:59Z
---

# Mikrotik wAP LTE Kit - US Tutorial

Step-by-step guide for configuring the Mikrotik wAP LTE Kit (US) router with a Telnyx SIM card, covering firmware update, APN configuration, and roaming setup.

## Prerequisites

Before you begin, make sure you have the following:

1. An active Telnyx SIM card
2. Mikrotik LTE kit router
3. A computer
4. The latest RouterOS firmware, available from the [Mikrotik downloads page](https://mikrotik.com/product/wap_lte_kit_us#fndtn-downloads)

> **Note:** Insert the SIM card into the router only when instructed to do so.

## Part I: Firmware Update

Start by updating the RouterOS firmware to the latest version (6.48 as of the time of writing).

1. Remove the SIM card from the device.
2. Connect your computer to the device via either WiFi or the Ethernet interface and log into the default gateway at `192.168.88.1`. Use the default credentials:
   - **Username:** `admin`
   - **Password:** (blank)
3. Once logged in, you will see the admin console.

![Mikrotik RouterOS](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/capture.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=d6d41a980b5831fbfb9e56e81a619ef6)

4. Click **Files → Browse** and upload the `.npk` firmware file.

![Mikrotik Tutorial - Image 2](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/capture2.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=257eaf54f64fbb572fb9962f5bb83f8b)

5. Reboot the device by clicking **System → Reboot**. The device will apply the latest firmware automatically during the boot procedure.

## Part II: Router Configuration

With the firmware updated, configure the LTE interface to use the Telnyx APN.

1. Navigate to **Interface → LTE**.

![Mikrotik Router Configuration](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/capture3.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=45637f7123acc931c9706b7d9cadff59)

2. Click **LTE APNs → Add New** and enter the following values:
   - **Name:** `Telnyx`
   - **APN:** `data00.telnyx`
   - **IP Type:** `IPv4`
   - **Use Peer DNS:** Checked
   - **Add Default Route:** Checked
   - Leave all other settings at their default values.

![Mikrotik Router Settings](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/capture3.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=45637f7123acc931c9706b7d9cadff59)

3. Click **Apply**, then **OK**.
4. Return to the **LTE** tab under **Interfaces** and click on the LTE module. Apply the APN created above using the dropdown menu, then enable roaming by checking the **Allow Roaming** box.

![Roaming options Mikrotik](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/capture6-1-.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=f557928bdbaaeabddac3f019dbdae337)

5. Press **Apply**, then **OK**.

## Inserting the SIM and Verifying Connectivity

1. Insert the Telnyx SIM card into the router.
2. Wait approximately 45 seconds for the device to attach to the network.
3. Verify connectivity by going to **Interfaces → LTE**, clicking on the LTE module, and scrolling down to the **Registration Status** field. It should display "roaming".

![Roaming Mikrotik](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/capture5.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=fa3db95c0d8a0303cda78ae9f1373774)
