---
source_url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
scraped: 2026-06-11
---

Understanding Wireless Connectivity States (Telnyx API) | Telnyx Help Center

[Skip to main content](#main-content)

# Understanding Wireless Connectivity States (Telnyx API)

Detailed guide explaining the various connectivity state values, definitions, and triggers for Telnyx Wireless Connectivity Logs API.

Written by Telnyx Engineering

November 5, 2025

Table of contents

# Understanding Wireless Connectivity States (Telnyx API)

When using the [Telnyx Wireless Connectivity Logs API](https://developers.telnyx.com/api/wireless/get-wireless-connectivity-logs), you might encounter different `state` values representing the status of your wireless SIM sessions. Below is a detailed explanation of each state, including their definitions and trigger points.

## Possible State Values & Definitions:

## 1. **Opened**

* **Definition:** This state occurs when a SIM initiates a new session to connect to a wireless network.
* **Trigger Points:** Occurs immediately after an attached event when a device starts transmitting or receiving data.

## 2. **Attached**

* **Definition:** Represents a SIM successfully connecting to the local carrier network. Once attached, the SIM receives an IP address, enabling data sessions.
* **Trigger Points:** Occurs when the SIM successfully registers with the cellular network and can start exchanging data.

## 3. **Closed**

* **Definition:** Indicates the data session has ended.
* **Trigger Points:** Can occur due to:

  + Loss of network coverage.
  + Device intentionally stopping the session (e.g., IoT device scheduled sessions).
  + Device switching off or entering airplane mode.
  + Device disconnecting from the cellular network upon connecting to Wi-Fi.

## 4. **Provisioned**

* **Definition:** A newly provisioned SIM remains in this state until it first attaches to a cellular network. It may also appear if the SIM has been transferred from a regular SIM group to a private wireless gateway SIM group.
* **Trigger Points:** Occurs upon initial provisioning or after specific account/SIM group changes.

##

---

## Frequently Asked Questions (FAQs)

## **Q1. What triggers the state 'Closed'?**

* The state 'Closed' triggers when:

  + Network connectivity is lost.
  + Device intentionally terminates a data session.
  + Device is switched off, placed in airplane mode, or moves to Wi-Fi connectivity.

## **Q2. How can I identify if a device is out of network coverage?**

* Currently, the API does not explicitly identify devices that lose coverage. However, a lack of "Attached" events indicates the device has not connected to the network. A standard successful connection cycle should be:

  + **Attached → Opened → Closed**

## **Q3. What does 'our API' refer to?**

* "Our API" refers specifically to the Telnyx Wireless Connectivity Logs API:

  + [Telnyx Wireless Connectivity Logs API](https://developers.telnyx.com/api/wireless/get-wireless-connectivity-logs)

---

For more detailed technical information, please visit the [Telnyx API documentation](https://developers.telnyx.com/api/wireless/get-wireless-connectivity-logs).

---

Related Articles

[SIM Reporting & Analytics](https://support.telnyx.com/en/articles/3679913-sim-reporting-analytics)[SIM Setup and Configuration](https://support.telnyx.com/en/articles/4298710-sim-setup-and-configuration)[SIM Connectivity Logs](https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs)[Using Telnyx SIM with Ubiquiti UniFi LTE Pro](https://support.telnyx.com/en/articles/10164784-using-telnyx-sim-with-ubiquiti-unifi-lte-pro)[Using Telnyx SIM with InRouter300 Series Cellular Routers](https://support.telnyx.com/en/articles/10511105-using-telnyx-sim-with-inrouter300-series-cellular-routers)

Did this answer your question?

😞😐😃

Table of contents
