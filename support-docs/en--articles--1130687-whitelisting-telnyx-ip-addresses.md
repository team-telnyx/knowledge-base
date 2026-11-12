---
source_url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
title: "Whitelisting Telnyx IP Addresses"
description: "We will explain what Telnyx IP Addresses you will need to whitelist to ensure your service works properly. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 904ab9e1c14c0644f1060d23262095849620f8492183feca9423d502458eea01
---







# Whitelisting Telnyx IP Addresses

We will explain what Telnyx IP Addresses you will need to whitelist to ensure your service works properly. See Telnyx guidance and requirements.




## Whitelisting Telnyx IP Addresses

To ensure optimal performance of your Telnyx services, please whitelist the following IP addresses by region and purpose.
​

## SIP Signaling and Media Servers

If your network uses a firewall or access control list (ACL), allow the Telnyx SIP signaling and media IP addresses listed on the SIP Info page.

- [SIP signaling addresses and regional FQDNs](https://sip.telnyx.com/)
- [Media IP ranges and RTP ports](https://sip.telnyx.com/#media)

---

## Webhooks

Telnyx programmable services, including **TeXML**, **Fax**, **Messaging**, and **Call Control**, deliver webhooks from the following regional IPs.
​

**Note:** These IPs also apply to **WebSocket stream connections**, which are typically initiated using the **Dial** and **Start Stream** APIs. WebSocket traffic leverages the same delivery infrastructure as webhooks.

* **North America**

  + CH1 (US-Central): 192.76.120.128/29, 64.16.239.40/31, 64.16.239.49/32, 64.16.239.50/32, 64.16.239.67/32, 64.16.239.72/32, 64.16.239.73/32
  + DC2 (US-East): 192.76.120.136/29, 64.16.239.99/32, 64.16.239.100/32, 64.16.239.114/31
  + SV1 (US-West): 192.76.120.144/29, 64.16.239.2/31, 64.16.239.83/32, 64.16.239.84/32
  + TR1 (Toronto, CA): 192.76.120.160/29
* **Europe, Middle East, Africa (EMEA)**

  + LD6 (London, UK): 185.246.41.0/29
  + FR5 (Frankfurt, DE): 185.246.41.8/29
  + AM6 (Amsterdam, NL): 185.246.41.16/29
  + DX1 (Dubai, AE): 185.246.41.24/29
* **Asia-Pacific (APAC)**

  + SY1 (Sydney): 103.115.244.0/29
  + SG1 (Singapore): 103.115.244.8/29
  + MB2 (Mumbai): 103.115.244.32/29

---

## Network IP Address Assignments by Region

**AMER (North America)**

* **Main Pools:** 192.76.120.128/26 & 192.76.120.192/27

  + CH1 - US Central: 192.76.120.128/29
  + DC2 - US East: 192.76.120.136/29
  + SV1 - US West: 192.76.120.144/29
  + TR1 - Toronto: 192.76.120.160/29
* **Additional Egress IPs:**

  + CH1 - US Central: 64.16.239.40/31, 64.16.239.49/32, 64.16.239.50/32, 64.16.239.67/32, 64.16.239.72/32, 64.16.239.73/32
  + DC2 - US East: 64.16.239.99/32, 64.16.239.100/32, 64.16.239.114/31
  + SV1 - US West: 64.16.239.2/31, 64.16.239.83/32, 64.16.239.84/32

**EMEA (Europe, Middle East, Africa)**

* **Main Pool:** 185.246.41.0/26

  + LD6 - London: 185.246.41.0/29
  + FR5 - Frankfurt: 185.246.41.8/29
  + AM6 - Amsterdam: 185.246.41.16/29
  + DX1 - Dubai: 185.246.41.24/29

**APAC (Asia-Pacific)**

* **Main Pool:** 103.115.244.0/26

  + SY1 - Sydney: 103.115.244.0/29
  + SG1 - Singapore: 103.115.244.8/29
  + MB2 - Mumbai: 103.115.244.32/29
