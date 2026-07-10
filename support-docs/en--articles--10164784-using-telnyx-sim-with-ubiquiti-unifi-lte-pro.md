---
source_url: https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro
scraped: 2026-07-08
content_hash: d345ef29c538bbc71d0d1c8f17af0d7a34aad7ace8f20d7c07b271a26bd484f0
---

Using Telnyx SIM with Ubiquiti UniFi LTE Pro | Telnyx Help Center

[Skip to main content](#main-content)

# Using Telnyx SIM with Ubiquiti UniFi LTE Pro

A step-by-step guide to setting up the Ubiquiti UniFi LTE Pro with a Telnyx SIM card for reliable cellular backup connectivity.

Written by Telnyx Engineering

November 20, 2024

Table of contents

# Ubiquiti UniFi LTE Pro Setup Guide

The Ubiquiti UniFi LTE Pro provides reliable backup cellular internet connectivity to ensure your UniFi WAN network remains operational. The Pro model supports 4G LTE and WCDMA bands and is compatible with the EU, US, and CA regions. It includes a Nano SIM card slot, which allows for the insertion of a Telnyx SIM card.

This guide will walk you through the setup process for configuring the Ubiquiti UniFi LTE Pro with a Telnyx SIM card.

![](_images/3cbf5191f4fcd719.png)

---

## **Setup Instructions for the UniFi LTE Pro**

### **Step 1: Insert the Telnyx SIM Card**

* Locate the Nano SIM card slot on your UniFi LTE Pro device.
* Insert the Nano SIM (smallest size from the Telnyx SIM card kit) into the slot.

![](_images/104a49a49e8e8704.png)

### **Step 2: Power On the Device**

* Connect the UniFi LTE Pro to a PoE (802.3af) enabled Ubiquiti network switch to power it on.

![](_images/f862e805db3d1d11.png)

### **Step 3: Access the UniFi Console**

1. Open your preferred web browser.
2. Navigate to <https://unifi.ui.com>.
3. Log in to your UniFi console.

![](_images/67b599cf6f9f7ce4.png)

### **Step 4: Adopt the Device**

* Locate the UniFi LTE Pro in your device list on the console.
* Click on the **Adopt** button to add the device to your network.

![](_images/0e682c4d08bd1f2b.png)

### **Step 5: Configure LTE Backup Settings**

1. After the device is successfully adopted, navigate to the **Settings** page.

   ![](_images/6c209094af1dc26e.png)
2. Select the **Internet** tab and click on the **LTE Backup** option.

   ![](_images/08ffe08918bd5bce.png)
3. A configuration window will appear on the right-hand side. Click **Settings** to proceed.

![](_images/cbb5d8a2dea3007e.png)

### **Step 6: Enter Telnyx APN Settings**

1. Input the Telnyx APN settings as follows:

   * **APN**: `data00.telnyx`
   * **Authentication Type**: Select **NONE**.
2. Click **Apply** to save the settings.

![](_images/3322fb6e93aa6f1c.png)

### **Step 7: Verify Connection Status**

* Go to the **Overview** tab.
* Confirm that the **Status** is listed as **Ready** and that **Connected** is set to **Yes**.

![](_images/ea63d97edc1df0f2.png)

---

## **Important Notes**

### **First-Time Network Attachment**

* Telnyx SIM cards support multiple network types and operators. During the first connection attempt, it may take up to 30 minutes for the device to attach to a network.
* Once connected, the network will be added to the list of priority operators for faster future connections.

### **Device Restart or Re-provisioning**

* If the device is restarted or re-provisioned, it may enter SIM-Activation mode. To resolve this, execute the following command in the UniFi CLI:

  ```
  qmicli -p -d /dev/cdc-wdm0 --wds-set-autoconnect-settings=enabled
  ```

---

Related Articles

[How to set up a Telnyx SIM Card](https://support.telnyx.com/en/articles/3269600-how-to-set-up-a-telnyx-sim-card)[SIM Setup and Configuration](https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration)[SIM Connectivity Logs](https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs)[Using Telnyx SIM with InRouter300 Series Cellular Routers](https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers)[Using Telnyx SIM with Teltonika 4G/LTE Routers](https://support.telnyx.com/en/articles/10511646-using-telnyx-sim-with-teltonika-4g-lte-routers)

Did this answer your question?

😞😐😃

Table of contents
