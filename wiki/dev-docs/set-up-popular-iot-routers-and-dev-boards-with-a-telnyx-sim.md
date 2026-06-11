---
title: Set up popular IoT routers and dev boards with a Telnyx SIM
summary: A single, consolidated guide to configure common routers, gateways, and development
  boards to connect over cellular using a Telnyx Wireless SIM, including required
  APN settings, default device logins, and essential troubleshooting tips.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/cradlepoint-ibr200-cellular/index
- url: https://developers.telnyx.com/docs/iot-sim/glmifi-router
- url: https://developers.telnyx.com/docs/iot-sim/mikrotik-wap-lte
- url: https://developers.telnyx.com/docs/iot-sim/nordic-semiconductor
- url: https://developers.telnyx.com/docs/iot-sim/particle-boron-lte-kit
- url: https://developers.telnyx.com/docs/iot-sim/pepwave-max-br1-mini-lte
- url: https://developers.telnyx.com/docs/iot-sim/sim7600-a-rasp-pui-hat/index
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-cellular-iot-hat
- url: https://developers.telnyx.com/docs/iot-sim/sixfab-rasp-pi-hat
updated_at: 2026-05-20T08:47:12Z
---

# Set up popular IoT routers and dev boards with a Telnyx SIM

A single, consolidated guide to configure common routers, gateways, and development boards to connect over cellular using a Telnyx Wireless SIM, including required APN settings, default device logins, and essential troubleshooting tips.

## Before you begin

- You need a Telnyx account and an active Telnyx Wireless SIM with a data plan.
- Use APN: data00.telnyx (leave username/password blank unless your device requires otherwise).
- SIM size varies by device (e.g., some routers use standard/mini; dev boards often use nano). Check your hardware label before inserting.
- Keep device firmware up to date for best compatibility.
- First network attach can take up to 30 minutes on a brand-new SIM or device. Subsequent attaches will be much faster.

## Cradlepoint IBR200 setup

- Insert a standard (mini) SIM. Power on.
- Browse to 192.168.0.1. Login: username admin; password is the device serial number on the bottom label.
- Go to Connection Manager → Add.
  - WAN Interface Profile: Name “Telnyx SIM”, Type “Modem”. Leave other options unchecked.
- Open the SIM/APN/Auth section:
  - SIM Card Lock: No PIN required
  - APN: Override → data00.telnyx
- Save and wait for registration. Verify status in Connection Manager. Note: first attach may take up to 30 minutes.
- NetCloud Essentials is required for full feature set, but basic connectivity works without it.

## Pepwave MAX BR1 Mini setup

- Insert a standard (mini) SIM in slot A or B. Power on.
- Connect via Wi‑Fi or Ethernet. Browse to 192.168.50.1. Login: admin / admin.
- Update firmware (System → Firmware) if prompted.
- Dashboard → WAN Connection Status → Details → Cellular Settings:
  - LTE/3G: Auto; Band Selection: Auto; Data Roaming: Checked (Any Countries)
  - APN: Custom → data00.telnyx (Username/Password blank)
- Save and Apply. Within ~2 minutes you should see “Connected” and an IP. Depending on region, the network/operator may display as Telecom Italia (I TIM).

## GL‑MiFi 4G Smart Router setup

- Insert the SIM with gold contacts facing up. Power on.
- Connect via Wi‑Fi/Ethernet. Browse to 192.168.8.1. Set an admin password when prompted (default is admin if not prompted).
- In Cellular Modem Overview, choose manual setup:
  - Device: /dev/cdc-wdm0
  - APN: data00.telnyx
- Apply and verify the overview shows an IP address and a Disconnect button. The status icon may show “I TIM” depending on the serving network.

## Mikrotik wAP LTE kit (US) setup

- Update RouterOS to the latest release (download the .npk from the Mikrotik site). Remove SIM, connect to 192.168.88.1, login admin (blank password), upload the .npk (Files → Browse), then System → Reboot.
- Configure LTE: Interfaces → LTE → LTE APNs → Add New:
  - Name: Telnyx; APN: data00.telnyx; IP Type: IPv4; Use Peer DNS: checked; Add Default Route: checked.
- Back in Interfaces → LTE, open the LTE modem, select the new APN, and enable Allow Roaming.
- Insert the SIM. After ~45 seconds, registration should show “roaming.” Verify the interface has an IP.

## Nordic nRF9160 DK setup

- Download latest board firmware and modem firmware, and install nRF Connect for Desktop with modules: LTE Link Monitor, Programmer, Trace Collector.
- Set the kit to debug mode. Connect via micro‑USB and power on.
- In Programmer, select device PCA10090, drag the board firmware zip, then Erase & write.
- Update the modem firmware via the Cellular Modem → Update modem action (select the mfw_nrf9160_*.zip).
- Insert a nano‑SIM. Open LTE Link Monitor, select PCA10090, wait for the automatic AT command sequence. The device should attach; verify in the Info pane.

## Particle Boron LTE kit setup

- Connect the LTE antenna and power the device. Use the Particle mobile app (Android/iOS) to add the device to your Particle account (the onboard eSIM activates during this flow).
- To use a Telnyx SIM, enable third‑party SIM via CLI:
  - Insert the Telnyx SIM.
  - Install Particle CLI on your computer.
  - Enter DFU mode: hold MODE, tap RESET, keep holding MODE until LED flashes yellow.
  - Connect via USB, then run:
    - particle update
    - particle flash --usb tinker
  - DFU again, then download TelnyxSIM.cpp, compile and flash:
    - particle compile boron
    - particle compile boron TelnyxSIM.cpp --saveTo firmware.bin
    - particle flash --usb firmware.bin
  - DFU again, then restore default app if desired:
    - particle flash --usb tinker
- Power cycle. The device will register using the Telnyx SIM (may take up to ~2 minutes). Verify in the Particle Console.

## Raspberry Pi: SIM7600‑A 4G HAT setup

- Update the Pi and reboot: sudo apt update -y; sudo apt dist-upgrade -y; sudo rpi-update.
- Install dependencies: sudo apt install libqmi-utils udhcpc
- Enable UART: sudo raspi-config → Interfacing Options → Serial → login shell “No” → reboot.
- Bring the modem online: sudo qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode=online
- Optional checks:
  - Operating mode: qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode
  - Signal: qmicli -d /dev/cdc-wdm0 --nas-get-signal-strength
  - Home network: qmicli -d /dev/cdc-wdm0 --nas-get-home-network
- Set raw‑ip and link up:
  - sudo ip link set wwan0 down
  - echo 'Y' | sudo tee /sys/class/net/wwan0/qmi/raw_ip
  - sudo ip link set wwan0 up
- Start data session with APN and obtain IP:
  - sudo qmicli --device=/dev/cdc-wdm0 --device-open-proxy --wds-start-network="ip-type=4,apn=data00.telnyx" --client-no-release-cid
  - sudo udhcpc -i wwan0
  - ip a s wwan0 (verify address)

## Raspberry Pi: Sixfab Cellular IoT HAT (BG96) setup

- Enable UART via sudo raspi-config (Interfacing Options → Serial → login shell “No”), then reboot.
- Install Sixfab library:
  - git clone https://github.com/sixfab/Sixfab_RPi_CellularIoT_Library.git
  - cd Sixfab_RPi_CellularIoT_Library && sudo python3 setup.py install
- Install PPP and set APN:
  - wget https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_install_standalone.sh
  - sudo chmod +x ppp_install_standalone.sh
  - sudo ./ppp_install_standalone.sh
  - Prompts: HAT = Cellular IoT HAT; APN = data00.telnyx; Username/Password = n; Port = ttyUSB3; Auto‑reconnect on boot = optional.
- Reboot. Connect/disconnect with:
  - Connect: sudo pon
  - Disconnect: sudo poff
- Troubleshooting highlights:
  - Ensure interface ppp0 appears (ifconfig). If missing, rerun the installer.
  - If ppp0 has no data, try ping 8.8.8.8, reboot, then ifconfig ppp0 down; ifconfig ppp0 up.
  - Rerun installer with blank APN then again with data00.telnyx if needed.
  - Verify antenna seating/compatibility and Pi power budget (≥12W for Pi 3, ≥15W for Pi 4). CAT‑M1 speeds are typically ~350 kbps.

## Raspberry Pi: Sixfab 3G/4G LTE Base HAT setup

- Update the Pi and headers, then reboot:
  - sudo apt update && sudo apt upgrade
  - sudo apt dist-upgrade
  - sudo apt install raspberrypi-kernel-headers
- Install QMI helper script:
  - wget https://raw.githubusercontent.com/sixfab/Sixfab_RPi_3G-4G-LTE_Base_Shield/master/tutorials/QMI_tutorial/qmi_install.sh
  - chmod +x qmi_install.sh
  - sudo ./qmi_install.sh (enter APN data00.telnyx when prompted)
- Reboot, then connect:
  - cd /files/quectel-CM
  - sudo ./quectel-CM -s data00.telnyx
- If connectivity is unstable, set auto‑reconnect:
  - wget https://raw.githubusercontent.com/sixfab/Sixfab_RPi_3G-4G-LTE_Base_Shield/master/tutorials/QMI_tutorial/install_auto_connect.sh
  - chmod +x install_auto_connect.sh
  - sudo ./install_auto_connect.sh (APN = data00.telnyx)
  - Verify: sudo systemctl status qmi_reconnect.service

## Verification and troubleshooting basics

- Confirm the APN is exactly data00.telnyx (no spaces/typos). Leave auth fields blank unless your device insists.
- Enable data roaming in router UIs where available.
- Allow up to 30 minutes for the very first network attach.
- Check for an assigned IP in the device UI or via interfaces (wwan0/ppp0) on Linux.
- Update device firmware and reboot if attach fails.
- Inspect antenna seating and use the correct antenna for your bands. Ensure adequate power supply, especially on Raspberry Pi builds.
- Basic network test: ping 8.8.8.8. If ICMP works but DNS doesn’t, ensure “Use Peer DNS” or equivalent is enabled, or manually set DNS.
