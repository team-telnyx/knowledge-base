---
source_url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
title: "Understanding Wireless Connectivity States (Telnyx API)"
description: "Detailed guide explaining the various connectivity state values, definitions, See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 15816c91a59c4e19aa16be70146a6f47812e93a1e3c9d073035efb291a6c8bc5
---







# Understanding Wireless Connectivity States (Telnyx API)

Detailed guide explaining the various connectivity state values, definitions, See Telnyx guidance and requirements.




## Understanding Wireless Connectivity States (Telnyx API)

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
