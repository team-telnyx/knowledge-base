---
source_url: https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro
scraped: 2026-06-11
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

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259110415/c8a7e84d020466ff8d92bd3b1b28/image.png?expires=1781167500&signature=792e7ce32a7495cdddff9c6f295fdb8d53c372de74fc0551a30693d9dec627dc&req=dSIiH8h%2FnYVeXPMW1HO4zWWUhF5UDjrLB992oFotEiWL9D5OBVlyn5vWhAJV%0AU8SVT4LRQ8Jdeau%2FLMI%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259110415/c8a7e84d020466ff8d92bd3b1b28/image.png?expires=1781167500&signature=792e7ce32a7495cdddff9c6f295fdb8d53c372de74fc0551a30693d9dec627dc&req=dSIiH8h%2FnYVeXPMW1HO4zWWUhF5UDjrLB992oFotEiWL9D5OBVlyn5vWhAJV%0AU8SVT4LRQ8Jdeau%2FLMI%3D%0A)

---

## **Setup Instructions for the UniFi LTE Pro**

### **Step 1: Insert the Telnyx SIM Card**

* Locate the Nano SIM card slot on your UniFi LTE Pro device.
* Insert the Nano SIM (smallest size from the Telnyx SIM card kit) into the slot.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259110857/d248a4bac595db730691cdb13c28/image.png?expires=1781167500&signature=2a45928c1b067be8ccfd746bfef5dd73d50a059dcd07247556c0b7f2cc132203&req=dSIiH8h%2FnYlaXvMW1HO4zf%2BgqmFo2btufHmkCFR4z0ZzcclyMmk7AglwsDkT%0AXXUXZJG%2FM%2Bj53rxvmIg%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259110857/d248a4bac595db730691cdb13c28/image.png?expires=1781167500&signature=2a45928c1b067be8ccfd746bfef5dd73d50a059dcd07247556c0b7f2cc132203&req=dSIiH8h%2FnYlaXvMW1HO4zf%2BgqmFo2btufHmkCFR4z0ZzcclyMmk7AglwsDkT%0AXXUXZJG%2FM%2Bj53rxvmIg%3D%0A)

### **Step 2: Power On the Device**

* Connect the UniFi LTE Pro to a PoE (802.3af) enabled Ubiquiti network switch to power it on.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259111287/181045e9f6a3f684442d386f1307/image.png?expires=1781167500&signature=525eb99dc35eb00e51d3e46dd182cba2fa03b28cc8e22bc0c058846bd8af0011&req=dSIiH8h%2FnINXXvMW1HO4zZim3pyvyWSJzH7v7zRoEmVsXBkAaLyXitfuvRwM%0A%2BRXv1%2B8YafER5qsDIKw%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259111287/181045e9f6a3f684442d386f1307/image.png?expires=1781167500&signature=525eb99dc35eb00e51d3e46dd182cba2fa03b28cc8e22bc0c058846bd8af0011&req=dSIiH8h%2FnINXXvMW1HO4zZim3pyvyWSJzH7v7zRoEmVsXBkAaLyXitfuvRwM%0A%2BRXv1%2B8YafER5qsDIKw%3D%0A)

### **Step 3: Access the UniFi Console**

1. Open your preferred web browser.
2. Navigate to <https://unifi.ui.com>.
3. Log in to your UniFi console.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259112916/3ec5d31eb33b30fb2963fa73721f/image.png?expires=1781167500&signature=3a0df58ef17ec3729f25bd42d25f03cf1f4363d21ae20c3aae47efb3f8d0b563&req=dSIiH8h%2Fn4heX%2FMW1HO4zdFxX0%2BVp11kHu8qjzrivfS2DgNtFx8GDEjzCaTj%0AOEcDOw85RkEdaEQmoyQ%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259112916/3ec5d31eb33b30fb2963fa73721f/image.png?expires=1781167500&signature=3a0df58ef17ec3729f25bd42d25f03cf1f4363d21ae20c3aae47efb3f8d0b563&req=dSIiH8h%2Fn4heX%2FMW1HO4zdFxX0%2BVp11kHu8qjzrivfS2DgNtFx8GDEjzCaTj%0AOEcDOw85RkEdaEQmoyQ%3D%0A)

### **Step 4: Adopt the Device**

* Locate the UniFi LTE Pro in your device list on the console.
* Click on the **Adopt** button to add the device to your network.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259114926/1a9467f86c97df1f9039500dc843/image.png?expires=1781167500&signature=75771e74f892928f349214e67cf194be1b1f55149804ce8d45c20b4c1cac9bf6&req=dSIiH8h%2FmYhdX%2FMW1HO4zfvqP5UqqbvYj%2FlupEd4h10%2BzQt5EkCCVaRofSXK%0AMqkXr0rfA6fNPq11NpE%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259114926/1a9467f86c97df1f9039500dc843/image.png?expires=1781167500&signature=75771e74f892928f349214e67cf194be1b1f55149804ce8d45c20b4c1cac9bf6&req=dSIiH8h%2FmYhdX%2FMW1HO4zfvqP5UqqbvYj%2FlupEd4h10%2BzQt5EkCCVaRofSXK%0AMqkXr0rfA6fNPq11NpE%3D%0A)

### **Step 5: Configure LTE Backup Settings**

1. After the device is successfully adopted, navigate to the **Settings** page.

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259116397/a3c4a5c43e6db114539b8be3ee69/image.png?expires=1781167500&signature=111b5c62cfc13d036bdc121fc0d9032708f1dc7d6e05ea0a270910e08ca39c30&req=dSIiH8h%2Fm4JWXvMW1HO4zUCZUdglnQgQu%2Fh1ksWP51W81MYQgSguPzhic2Uo%0AWT8D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259116397/a3c4a5c43e6db114539b8be3ee69/image.png?expires=1781167500&signature=111b5c62cfc13d036bdc121fc0d9032708f1dc7d6e05ea0a270910e08ca39c30&req=dSIiH8h%2Fm4JWXvMW1HO4zUCZUdglnQgQu%2Fh1ksWP51W81MYQgSguPzhic2Uo%0AWT8D%0A)
2. Select the **Internet** tab and click on the **LTE Backup** option.

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259117033/f3e9ef5a7c38824fa0155b9f6286/image.png?expires=1781167500&signature=0e0d8104933dc2b8471c8e6706d577a09b9a1c250d9bd0118fb321ace3211c09&req=dSIiH8h%2FmoFcWvMW1HO4zRzJ54RzMCOltq1PbVTmd2nQnGlKNY6pT3y0eGW0%0AMIlX%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259117033/f3e9ef5a7c38824fa0155b9f6286/image.png?expires=1781167500&signature=0e0d8104933dc2b8471c8e6706d577a09b9a1c250d9bd0118fb321ace3211c09&req=dSIiH8h%2FmoFcWvMW1HO4zRzJ54RzMCOltq1PbVTmd2nQnGlKNY6pT3y0eGW0%0AMIlX%0A)
3. A configuration window will appear on the right-hand side. Click **Settings** to proceed.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259118035/679620a9b67a68c187593fe2cec5/image.png?expires=1781167500&signature=9e939b3b61954b4e444eef26e43c36db12afd8c6e2cf1e336e49c0e270a18a47&req=dSIiH8h%2FlYFcXPMW1HO4zW9uTm8EhWh6Uw%2Fbnp8AABGoPcoaPbJNtLMlG6is%0AMVCQgbAqbdZSDRYZpvE%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259118035/679620a9b67a68c187593fe2cec5/image.png?expires=1781167500&signature=9e939b3b61954b4e444eef26e43c36db12afd8c6e2cf1e336e49c0e270a18a47&req=dSIiH8h%2FlYFcXPMW1HO4zW9uTm8EhWh6Uw%2Fbnp8AABGoPcoaPbJNtLMlG6is%0AMVCQgbAqbdZSDRYZpvE%3D%0A)

### **Step 6: Enter Telnyx APN Settings**

1. Input the Telnyx APN settings as follows:

   * **APN**: `data00.telnyx`
   * **Authentication Type**: Select **NONE**.
2. Click **Apply** to save the settings.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259118494/612d219be2ee038cda935964699f/image.png?expires=1781167500&signature=f3b7f25f1134328a0a5baca21e72ab94d0c07b52c9fef87769d10d9bdb965726&req=dSIiH8h%2FlYVWXfMW1HO4zckovP%2BX78rJqfLkQo2pdsVDEisDqckALM9YAqjc%0AaHM93RH1tUKsgaSD%2BO8%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259118494/612d219be2ee038cda935964699f/image.png?expires=1781167500&signature=f3b7f25f1134328a0a5baca21e72ab94d0c07b52c9fef87769d10d9bdb965726&req=dSIiH8h%2FlYVWXfMW1HO4zckovP%2BX78rJqfLkQo2pdsVDEisDqckALM9YAqjc%0AaHM93RH1tUKsgaSD%2BO8%3D%0A)

### **Step 7: Verify Connection Status**

* Go to the **Overview** tab.
* Confirm that the **Status** is listed as **Ready** and that **Connected** is set to **Yes**.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259119006/0a9b969a21798f11d1c5cace0c55/image.png?expires=1781167500&signature=c2937126e6016f777c190ffb5d7d4e00e8978de4102f151aaa06b3b2b64a67ab&req=dSIiH8h%2FlIFfX%2FMW1HO4zaGWoItWDiaQ9S%2FAsZGMxuWejtuMX6GvBseVDu8S%0AZOViYXX8P%2FNUYsyi9LU%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1259119006/0a9b969a21798f11d1c5cace0c55/image.png?expires=1781167500&signature=c2937126e6016f777c190ffb5d7d4e00e8978de4102f151aaa06b3b2b64a67ab&req=dSIiH8h%2FlIFfX%2FMW1HO4zaGWoItWDiaQ9S%2FAsZGMxuWejtuMX6GvBseVDu8S%0AZOViYXX8P%2FNUYsyi9LU%3D%0A)

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
