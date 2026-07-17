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

*Part 6 of 6 — see also: [Part 1](wireless--part-1.md), [Part 2](wireless--part-2.md), [Part 3](wireless--part-3.md), [Part 4](wireless--part-4.md), [Part 5](wireless--part-5.md)*

Telnyx Wireless provides API-driven cellular connectivity for IoT and mobile devices. This page covers SIM and eSIM provisioning, lifecycle management, SIM Card Groups, bulk operations, data routing (public IPs, Private Wireless Gateways, Traffic Policy Profiles, Wireless Blocklists), data usage monitoring and notifications, Wireless Detail Records, OTA updates, VoLTE with mobile phone numbers and call features, IoT pricing, connectivity troubleshooting, AT commands, and step-by-step setup guides for a range of supported devices including Raspberry Pi HATs, Particle Boron, Nordic nRF9160, Cradlepoint IBR200, Pepwave Max BR1 Mini, GL-MiFi, and Mikrotik wAP LTE.

## Device Setup Guides

### SIM7600-A Raspberry Pi 4G HAT

The SIM7600A 4G HAT is a 4G communication and GNSS positioning module, which supports LTE CAT4 up to 150Mbps for downlink data transfer. It is pretty low power consumption and can be attached to a Raspberry Pi to empower connectivity for IoT applications. You can also connect this 4G module with a computer to surf the Internet. It has functionality for sending SMS, global positioning, and high speed internet connections via 4G.

**Prerequisites**

1. Sign up for a [free Telnyx Portal account](https://telnyx.com/sign-up "Sign Up") and purchase an active Telnyx SIM card with data plan. Check out the [SIMs & eSIMs](sims-esims.md) quickstart to get set up.
2. Raspberry Pi 3 Model B or Raspberry Pi 4 (this guide will use 4 but the steps are the same).
3. Internet connection for initial setup and configuration.

**Preparation steps**

First, update the Raspberry Pi:

- `sudo apt update -y`
- `sudo apt dist-upgrade -y`
- `sudo rpi-update`
- You may see a prompt like this. Press `Y` and press `enter`:
  ![Preparation steps for the SIM7600 Raspberry Pi 4G HAT setup](https://mintcdn.com/telnyx/33ANQJ-HKUTIlvR5u/img/capture.jpeg?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=b96b69bb05b2f9868bf1f7cdac90452b)

Once all of the steps are complete, reboot your Pi using `sudo reboot` command.

With the updates out of the way, install prerequisite software and libraries: *libqmi-utils* and *udhcpc*. Install them by running: `sudo apt install libqmi-utils && udhcpc`

*libqmi-utils* installs libraries that allow you to interact with Qualcomm-based modems. SIM7600 comes with a Qualcomm MDM9607 chipset. *udhcpc* is used for modem DHCP leasing. The cellular network gives a unique IP to the HAT and the Pi will have its own IP. This is used to solve IP addressing conflicts between the Pi and the HAT.

Now enable UART to communicate with the device. To do that, run `sudo raspi-config` and follow the prompts as shown in the [AT Commands](at-commands.md) section.

**Configuration of the SIM7600 module**

Next, configure the SIM7600A module. To turn on the module use the qmicli commands which are used to control Qualcomm devices. This command will activate the device: `sudo qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode='online'`

Verify that the module is online. These are sample commands you can send to the device:

- `qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode`
  - Response: Online or Offline
- `qmicli -d /dev/cdc-wdm0 --nas-get-signal-strength`
  - Response: Signal strength and signal quality values
- `qmicli -d /dev/cdc-wdm0 --nas-get-home-network`
  - Response: Carrier name or carrier PLMN

You should now see a WWAN0 interface in net-stats (`ifconfig`). Unless specified by user, WWAN0 is the default interface this device uses.

Configure the module to use raw-ip protocol with the following commands:

- `sudo ip link set wwan0 down`
- `echo 'Y' | sudo tee /sys/class/net/wwan0/qmi/raw_ip`
- `sudo ip link set wwan0 up`

And connecting to a mobile network:

```
sudo qmicli --device=/dev/cdc-wdm0 --device-open-proxy --wds-start-network="ip-type=4,apn=data00.telnyx" --client-no-release-cid
```

Finally, set the default route and IP using udhcpc: `sudo udhcpc -i wwan0`
And tell the udhcpc library to receive a DHCP lease from the network using WWAN0: `ip a s wwan0`

> The Telnyx SIM has access to all network types and many different operators. As a result, it can take them a while to attach to a network for the first time. Once it connects to a network, that network will be added to the list of priority operators so as to ensure a fast connection going forward. Please note that the first attach can take up to 30 minutes.

### Sixfab Raspberry Pi 3G/4G HAT

The Sixfab 3G/4G & LTE Base HAT grants your Raspberry Pi or 40-pin Pi compatible single-board-computer a super-simple interface bridge between mini PCIe cellular modems. If you're looking for a Raspberry Pi LTE HAT for IoT applications like location tracking or global device deployments this is a great device. This add-on also board allows you to create a remote controllable LTE Wi-Fi Hotspot, high-speed GPS tracking and more. From low-power consumption LTE-M to ultra-high-speed LTE-Advanced mini PCIe cards supported by this HAT. Both UART and USB communication with modules are available on the shield.

This guide assumes that you have a fresh installation of Raspbian OS.

**Instructions**

1. First, make sure the Raspberry Pi is up to date:

   ```
   sudo apt update && sudo apt upgrade
   sudo apt dist-upgrade
   sudo apt install raspberrypi-kernel-headers
   reboot
   ```
2. Next, obtain the required repository from the Sixfab quickstart script: `wget https://raw.githubusercontent.com/sixfab/Sixfab_RPi_3G-4G-LTE_Base_Shield/master/tutorials/QMI_tutorial/qmi_install.sh`
3. Take ownership of the script and install it. You may be prompted to enter an APN. Enter `data00.telnyx` as the APN:

   ```
   chmod +x qmi_install.sh
   sudo ./qmi_install.sh
   ```
4. Reboot your device and then get connected.
5. To get connected to the internet, navigate to: `cd /files/quectel-CM`
6. Then mark the device as "online":

   ```
   sudo ./quectel-CM -s internet
   ```

> The Telnyx SIM has access to all network types and many different operators. As a result, it can take them a while to attach to a network for the first time. Once it connects to a network, that network will be added to the list of priority operators so as to ensure a fast connection going forward. Please note that the first attach can take up to 30 minutes.

**Troubleshooting**

If the device doesn't connect to the internet, the device either doesn't know which APN to use or the Raspberry Pi has trouble communicating with the device. Set up auto-connect:

1. Make sure the sixfab hat is connected.
2. Obtain required repository: `wget https://raw.githubusercontent.com/sixfab/Sixfab_RPi_3G-4G-LTE_Base_Shield/master/tutorials/QMI_tutorial/install_auto_connect.sh`
3. Take ownership of the script and install:

   ```
   chmod +x install_auto_connect.sh
   sudo ./install_auto_connect.sh
   ```
4. Now, it will ask for an APN. Please make sure to double check the APN as a misspelling in this step may cause connectivity issues.
5. Verify that the module is active and online: `sudo systemctl status qmi_reconnect.service`

### Sixfab Cellular IoT HAT

Sixfab Raspberry Pi Cellular IoT HAT allows you to send or receive data over LTE-M cellular networks that the Telnyx SIM has access to without needing gateways. LTE-M (Cat M1) is a must-have for those looking to make the most of Low Power Wide Area Network (LPWAN) technology. Meanwhile, some countries already started to shut down 2G networks. The Quectel BG96, lies on the middle of the Raspberry Pi Cellular IoT HAT. It is an LTE Cat M1/Cat NB1/EGPRS module offering a maximum data rate of 375Kbps downlink and uplink with worldwide coverage. This LTE add-on for Raspberry Pi also supports GNSS and GPS for the need of building location, navigation, tracking, mapping and timing applications.

**Prerequisites**

1. A Telnyx Portal account and active Telnyx SIM card with data plan. Check out the [SIMs & eSIMs](sims-esims.md) quickstart to get set up.
2. Raspberry Pi 3 Model B or Raspberry Pi 4 (this guide will use 4 but the steps are the same).
3. Make sure both the firmware and software are up-to-date on your Pi.
4. Install the Sixfab IoT HAT on the Pi using the 40-pin connector and connect the HAT to the Pi's USB port.

**Instructions**

1. First, enable UART. This will allow you to communicate directly with the device using AT commands. Run `sudo raspi-config` and follow the prompts as shown in the [AT Commands](at-commands.md) section.
2. Retrieve necessary repository from Sixfab: `git clone https://github.com/sixfab/Sixfab_RPi_CellularIoT_Library.git`
3. Navigate to the directory, take ownership of the script, and begin the installation:

   ```
   cd Sixfab_RPi_CellularIoT_Library
   sudo python3 setup.py install
   ```
4. Activate the module and specify the APN:

   ```
   wget https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_install_standalone.sh
   sudo chmod +x ppp_install_standalone.sh
   sudo ./ppp_install_standalone.sh
   ```
5. Once the installation begins, you will be prompted several options. Select the options as follows:

   - Choose your HAT —> Cellular IoT HAT
   - What is your carrier APN? —> data00.telnyx
   - Does your carrier need an username or password? —> n
   - What is your device communication PORT? —> ttyUSB3
   - Would you like to reconnect automatically on boot? —> This step is optional. We will select "n" for this guide.

6. Once the Pi reboots, use the following commands to connect/disconnect from the internet. If you have selected "y" to the reconnect prompt during configuration, your HAT will automatically connect to the network.

   `sudo pon` to connect
   `sudo poff` to disconnect

> The Telnyx SIM has access to all network types and many different operators. As a result, it can take them a while to attach to a network for the first time. Once it connects to a network, that network will be added to the list of priority operators so as to ensure a fast connection going forward. Please note that the first attach can take up to 30 minutes.

**Troubleshooting**

If you have issues with network connectivity, check `ifconfig` to see if interface PPP0 is visible (it should be located at the very bottom). If you do not see this entry, repeat step 3 above. Sixfab's script is designed to skip items when there is an error or a part doesn't run properly.

If you see the PPP0 interface but there is no data connection please try the following steps.

1. Try pinging Google DNS at 8.8.8.8.
2. If this doesn't work, reboot the Pi and reset the interface:

   ```
   sudo reboot
   sudo ifconfig ppp0 down
   sudo ifconfig ppp0 up
   ```
3. If this step fails, run step 3 and 4 from the original setup again with a blank APN, then run the script again with the correct APN (`data00.telnyx`).
4. Check the antenna connection - main & GPS. An improperly seated connection will cause the device to reboot.
5. Check if the antenna supports your HAT model.
6. Check the Pi's power supply - the HAT itself uses 2 - 6 watts of power. Make sure you are using a sufficient power supply for your Pi. Raspberry Pi 3 requires at least 12W of power. Raspberry Pi 4 requires at least 15W of power.
7. Slow internet may cause issues in your setup too. The theoratical speed max for this HAT is about 350 Kbps range as this is the limitation of the CATM1 network. This is normal.

### Particle Boron LTE Kit

The Boron is a powerful LTE Cat M1 or 2G/3G enabled development kit that supports cellular networks and Bluetooth LE (BLE). It is based on the Nordic nRF52840 and has built-in battery charging circuitry so it's easy to connect a Li-Po and deploy your local network in minutes.

**Prerequisites**

1. A Telnyx Portal account and active Telnyx SIM card with data plan. Check out the [SIMs & eSIMs](sims-esims.md) quickstart to get set up.
2. An Android or iOS device with internet acccess.
3. The Particle Electron Boron device.
4. A computer with CLI.

**Instructions**

1. First, connect the LTE antenna to the port located in the front of the Particle Electron Boron device and connect the device to power. The device will automatically go into pairing mode.
2. Download and install the mobile application on your [Android](https://docs.particle.io/quickstart/boron/) or [iOS](https://apps.apple.com/us/app/particle-iot/id991459054) device.
3. Open the Particle Mobile Application and follow the on-screen instructions:
   - Click "Get Started".
   - Log into your Particle.io account or create an account.
   - Press the + button located at the top right of the page and select the device name (i.e. boron-ij3). Your device will now activate its eSIM and you'll be able to see the device by logging into console.particle.io. Particle.io offers a 3-month free trial with limited free data.
4. Now, let's enable third-party SIM capability on the device. To begin, insert the Telnyx SIM card into the device.
5. Set up CLI environment on your computer using this [Particle guide](https://docs.particle.io/tutorials/developer-tools/cli).
6. Place your device in DFU mode. This mode allows you to interact with the device using a computer.
7. Press and hold the "Mode" button then press the "Reset" button once. Keep holding the "Mode" button until the device flashes yellow.
8. Connect your device to the computer via the provided micro-USB cable. Then run the following commands in your CLI environment:
   - `particle update`
     - This command updates the device's firmware (1.5.2 as of this guide).
   - `particle flash --usb tinker`
     - The device, by default, receives commands from the Particle Cloud via a network connection.
     - This command allows your computer to control the device instead of the cloud.
9. Repeat Step 6 to place your device into DFU mode.
10. Download this file [TelnyxSIM](https://assets.ctfassets.net/4b49ta6b3nwj/2UDzHa6KD1Uf6OkKidxtxD/a620b9e24f5c0997be7e593ae39180ec/TelnyxSIM.cpp) and navigate to the saved location. Then, run the following commands:
    - `particle compile boron`
      - This command will compile the .cpp file into a binary file.
    - `particle compile boron TelnyxSIM.cpp --saveTo firmware.bin`
      - This command will create a firmware.bin file that you will tell the device to use the Telnyx SIM card.
    - `particle flash --usb firmware.bin`
      - This command will flash the firmware.bin on to the device. The device will start using the Telnyx SIM card next time it reboots.
11. Repeat Step 6 to place your device into DFU mode and run this command to give back your device its control:
    - `particle flash --usb tinker`
12. Once you connect your device into a power adapter, you'll connect to the Telnyx network. It may take up to 2 minutes to reflect network connectivity. You can also verify the connectivity by clicking on your device name in console.particle.io.

### Nordic Semiconductor nRF9160 DK

The nRF9160 DK is an affordable, pre-certified single-board development kit for evaluation and development on the nRF9160 SiP for LTE-M, NB-IoT and GPS.

**Updating the firmware of the nRF9160**

1. Download the latest board and SIP modem firmware for this device [here](https://www.nordicsemi.com/Products/Development-hardware/nrf9160-dk/download).
2. Once both firmwares are downloaded, open up your file manager and extract the board firmware. The zip file has the file name: `nrf9160dk_fw_0000-00-00_xxxxxxx.zip.` Do NOT extract the SIP modem firmware labeled `mfw_nrf9160_x.x.x.zip.`
3. Download and install the latest nRF Connect application for your operating system [here](https://www.nordicsemi.com/Products/Development-tools/nrf-connect-for-desktop/download#infotabs).
4. Once installed, open up the application and install the following modules:

   - LTE Link Monitor
   - Programmer
   - Trace Collector

5. Look at the front of the device and make sure it's in debug mode.
6. Connect the device to the computer via a microUSB cable and turn on the device using the power switch located at the bottom left corner of the device.
7. Open up the `Programmer` application and select the device denoted `PCA10090`.
8. Drag and drop the firmware file into the file memory layout box then select `Erase & write` to update the firmware. The left box will show patterns when the update is in progress. Once the update is complete, the left box will display a `Device is connected` message.
9. Now, update the modem firmware. Scroll the right toolbar to the bottom of the screen. Select `Update modem` under the Cellular Modem section and click on the SIP modem firmware that was downloaded in step 1. Then click `Write`.

   - The zip file has the following filename: `mfw_nrf9160_x.x.x.zip.`

10. Once the modem updates are complete, turn off the device by using the power switch located at the bottom left corner and disconnect the device from the computer.

**Connecting the nRF9160 device to your Telnyx SIM**

1. Insert your Telnyx SIM card into the nRF9160 device (this device uses nano-sim). Make sure to insert in the correct orientation as notated on the development kit.
2. Connect the nRF9160 device to the computer and power on the device.
3. Open up the nRF Connect application and launch `LTE Link Monitor`.
4. In the `Select Device` dropdown menu, select `PCA10090`. The LTE Link Monitor display will update and run preselected AT commands. Allow 10-15 seconds for it to complete and the device will automatically connect to the network. Verify connectivity in the information tab located on the right side of your display.

### Cradlepoint IBR200 Cellular Router

The compact, semi-ruggedized IBR200 LTE router is designed for secure, cloud-managed IoT networking. The IBR200 enables use of low-cost M2M/IoT data plans via the Telnyx Wireless SIM, and with NetCloud Perimeter, addresses the biggest gap in IoT: security. It comes with NetCloud Perimeter and advanced security for PCI-compliant networking of vulnerable IoT devices.

**Prerequisites**

1. A Telnyx Portal account and active Telnyx SIM card with data plan. Check out the [SIMs & eSIMs](sims-esims.md) quickstart to get set up.
2. The Cradlepoint IBR200 device.
3. A Netcloud Essentials Cloud subscription is required for full functionality of this Cradlepoint modem. Without this, many of its features will be disabled. This guide, however, will walk you through basic connectivity which does NOT require the subscription.

**Instructions**

1. First, insert the Telnyx SIM card into your Cradlepoint device. The device only accepts the standard SIM card (the largest size from your Telnyx SIM card kit).
2. Power on the device by connecting the device to its charging adapter.
3. Open up your preferred web browser and navigate to 192.168.0.1. This is the router's default gateway. You'll be prompted to log into the device. The default credentials are:
   - Username: admin
   - Password: the serial number located on the label at the bottom of the device.
4. Click on "Connection Manager" tab.
5. Click "Add".
6. In this step you'll specify the WAN Interface Profile. Configure the profile as shown below:
   - Profile name: Telnyx SIM
   - Type: Modem
   - Leave everything else unchecked
7. On the next page, click on "SIM/APN/Auth". In this step, you'll specify the APN to use with the Telnyx SIM Card. Configure the items as shown below:
   - SIM Card Lock: No Pin Required
   - Access Point Name (APN): Default Override
   - data00.telnyx
8. Once you hit "Save" it'll take a few minutes for your device to receive connection. You can verify connectivity by heading to "Connection Manager" tab.

> The Telnyx SIM has access to all network types and many different operators. As a result, it can take them a while to attach to a network for the first time. Once it connects to a network, that network will be added to the list of priority operators so as to ensure a fast connection going forward. Please note that the first attach can take up to 30 minutes.

### Pepwave Max BR1 Mini LTE

The Pepwave MAX BR1 Mini is the latest industrial-grade, 4G LTE router from Peplink. This capable router is heavy on features while keeping a lightweight, small footprint, suitable for installation just about anywhere. Whether the BR1 Mini is installed in a vehicle, used in M2M deployments, or will provide cellular backup or Out of Band Management to a home or office, it has great performance and works seamlessly with Telnyx Wireless SIMs.

**Prerequisites**

1. A Telnyx Portal account and active Telnyx SIM card with data plan. Check out the [SIMs & eSIMs](sims-esims.md) quickstart to get set up.
2. The Pepwave Max BRI Mini LTE Device.
3. A computer.
4. The latest firmware, which can be obtained [here](https://www.peplink.com/support/downloads).

**Instructions**

1. To start, insert the Telnyx SIM card into either SIM A or SIM B slot on the device and power on the device. The device only accepts the standard size SIM card (the largest SIM card included in the kit).
2. Connect to the device either via the WiFi credentials listed on the unit below the device or via the WAN/LAN Ethernet port located on the back of the device.
3. Navigate to `192.168.50.1`, this is the default gateway of the device. Now, log in, the default username and password are both `admin`.
4. Update the device firmware by navigating to `System`, then `Firmware`, and uploading the firmware file. This may take up to 8 minutes.
5. Once the update process is complete, you'll be directed to the `Dashboards` tab. Click on `Details` under WAN Connection Status. Then, scroll down to `Cellular Settings` and make modifications as shown below:
   - SIM Card: Specified in Step 1 of this guide
   - LTE/3G: Auto
   - Band Selection: Auto
   - Data Roaming: Checked, Any Countries
   - APN: Custom, data00.telnyx
   - Username: Leave blank
   - Password: Leave blank
6. Scroll down to the end of this page and press `Save and Apply`.
7. It'll take about 2 minutes to connect and you can verify connectivity by checking the `WAN Connection Status` under the `Dashboards` tab. This will show that you're connected to Telecom Italia Mobile.

### GL-MiFi 4G Smart Router

**Prerequisites**

1. A Telnyx Portal account and active Telnyx SIM card with data plan. Check out the [SIMs & eSIMs](sims-esims.md) quickstart to get set up.
2. GL-MiFi device.
3. A computer with a browser.

**Instructions**

1. First, insert the SIM card into the device. Look at the picture below for the proper placement of the SIM card, the gold chip should be facing up.
2. Power on the device and connect either via the Ethernet port or WiFi connection. The default WiFi credentials are located on a label at the bottom of the device.
3. Navigate to the device's default gateway at `192.168.8.1` and log into the device. You'll be prompted to set an admin password but if you don't see the prompt, the default password is `admin`.
4. Once you've logged in, click on `manual setup` located in the Cellular Modem Overview section. Enter the following details as shown below and click `Apply`.
   - Device: `/dev/cdc-wdm0`
   - APN: `data00.telnyx`
5. The device will now attach to the Telnyx network. You can verify the connectivity by checking the front page of the default gateway as shown below. You'll notice that the device now shows a `Disconnect` button as well as IP address and data usage.
6. To check your connectivity, you can also check the fourth icon on the left of the overview diagram. It will indicate `I TIM`.

### Mikrotik wAP LTE Kit - US

**Prerequisites**

1. An active Telnyx SIM card
2. Mikrotik LTE kit router
3. A computer
4. Latest routerOS firmware, which you can obtain [here.](https://mikrotik.com/product/wap_lte_kit_us#fndtn-downloads "Mikrotik Downloads")

**Setting Up Mikrotik wAP LTE kit**

Note: Please insert the SIM card into router only when instructed to do so.

**Part I: Firmware Update**

- We will begin by updating the routerOS firmware to the latest version (6.48 as of 2.4.21).
- Remove the SIM card from the device.
- Connect your computer to the device via either the WiFi or the Ethernet interface and log into the default gateway at 192.168.88.1. The default username and password are shown below.
  - Username: admin
  - Password: (blank)
- Once you log in, you will see the admin console.
- Click on Files → Browse and upload the .npk firmware file.
- Reboot the device by clicking System → Reboot.
  - The device will apply the latest firmware automatically during the booting procedure.

**Part II (Router Configuration)**

- Navigate to Interface → LTE.
- Click LTE APNs → Add New.
  - Name: Telnyx
  - APN: data00.telnyx
  - IP Type: IPv4
  - Use Peer DNS: Check
  - Add Default Route: Check
  - Leave all other settings as their default values.
- Click Apply then OK.
- Go back to the LTE tab under Interfaces and click on the LTE module. Apply the APN created above using the dropdown menu and enable roaming by checking the Allow Roaming box.
- Press Apply then OK.
- Insert the Telnyx SIM card. After roughly 45 seconds, the device will attach to the network. You can verify connectivity by going to Interfaces → LTE → Click on the LTE module then scroll down to registration status. It will display "roaming".

### Deploy a Cradlepoint edge device with an IoT SIM

In this tutorial, we are going to deploy a Cradlepoint IBR200 to the edge of our corporate network in Digital Ocean. We will then open the Cradlepoint device up for SSH access via a private IP address from within our network. For this tutorial, the SIM card in the Cradlepoint device will only have access to our corporate network in Digital Ocean and will not have access to the public internet directly.

There are 5 main steps in the setup of this deployment:

1. SIM card setup
2. Cloud VPN setup
3. Cradlepoint IBR200 setup
4. Private Wireless Gateway setup
5. Cradlepoint SSH configuration

To ensure that we have direct access to the Cradlepoint device via a private IP address in our corporate network, we are going to connect a Digital Ocean Droplet (a Linux server) to a VRF-defined network on the Telnyx MPLS backbone via a Wireguard client. We will then spin up a private packet gateway in the Telnyx mobile core just for this SIM card and add that packet gateway to the same VRF-defined network that the Wireguard client is connected to. We will finally configure the Cradlepoint device to accept SSH access and connect directly into our Cradlepoint CLI via the private IP address that the packet gateway gives the SIM on our VRF-defined network.

**SIM Card Setup**

Our first step is to order and register a Telnyx SIM card. SIM cards can be ordered in the mission Control portal and registered via the registration flow in the wireless section. You can learn more about registering a SIM card in our [SIMs & eSIMs](sims-esims.md) quickstart guide. When the SIM is inserted into the Cradlepoint device, the only custom configuration that is required to connect the SIM is to set the APN to `data00.telnyx`.

**Cloud VPN Setup**

Next, we will configure a Wireguard client in a Digital Ocean Droplet to connect into a Cloud VPN on the Telnyx MPLS backbone. Follow the steps in our Digital Ocean Ubuntu Server to Cloud VPN tutorial. When you can successfully ping the server endpoint on the Telnyx network, you can move to the next step.

**Cradlepoint IBR200 Setup**

Before we create and configure a Private Wireless Gateway we will connect our Telnyx SIM card to the internet in our Cradlepoint device. Follow the steps in our [Cradlepoint IBR200 Cellular Router](cradlepoint-ibr200-cellular-router.md) setup guide. When you can successfully access the public internet via a connected device to the Cradlepoint network, you can move to the next step.

**Private Wireless Gateway Setup**

A Private Wireless Gateway (PWG) must be associated with a Network resource in the portal. The PWG can be created in the [Private Wireless Gateways subsection](https://portal.telnyx.com/#/app/wireless/private-wireless-gateways) in the Wireless section of the portal. Click the Create PWG button, enter a name and select the Network resource that you used for your Cloud VPN from step 2.

The PWG may take up to 15 minutes to create. This is due to the number of automated network configurations that are required to deploy an entirely new Dockerized PGW instance into our wireless mobile core. When the PWG status changes to **provisioned**, we can associate our SIM Group. This can be done by navigating to the relevant SIM Group and setting the PWG to the one we just created. For the sake of this tutorial, it is best to associate a SIM group with just the SIM that you have inserted into your Cradlepoint device. By default, the SIMs in this SIM group will lose access to the public internet when added to the new PGW in our wireless mobile core.

Now that you have your SIM card associated with a new packet gateway via the PWG resource that you created on the same network as your Cloud VPN we can ping the IP of our SIM card from the Digital Ocean Droplet. Log into your Digital Ocean Ubuntu Server and ping the IP that your SIM is showing in the portal. The SIM card IP address can be viewed in the drill-down view for that SIM. When you have a successful ping working between your Digital Ocean server and SIM card in your Cradlepoint device, you can move on to the next step.

**Cradlepoint SSH Configuration**

The final step is to enable SSH access on your Cradlepoint device. This is done via the Administration page in the Cradlepoint configuration console. Connect to your Cradlepoint WiFi network and enter the LAN IP address or hostname of the router (assuming you are connecting from the LAN side) into a web browser's location field. By default, the LAN IP address is `192.168.0.1` and the router's hostname is `cp`:

Next, navigate to the **System** section on the left nav menu, and then select **Administration**. Select **Local Management** from the drop-down menu. Then check the **Enable SSH Server** entry box. To access the CLI from your corporate network, select **Remote Admin** from the **Administration** drop-down menu, and check **Allow Remote SSH Access**. Click **Save** *(if using Local Management)* or **Submit** *( if using Remote Admin)*.

*Allow Weak Cipher Support* is off by default. You may need to enable this depending on the SSH version and encryption algorithm that you are using on your server. It can be enabled by navigating to **System > Administration > Local Management > Allow Weak Cipher Support**.

Now that you have enabled SSH on the Cradlepoint device, you should be able to access the device from your Digital Ocean server. From your Linux server run:

```
ssh admin@[SIM_CARD_IP]
```

Enter the password that you used to access the Cradlepoint management console. You should now have access to the Cradlepoint CLI without any internet access.
