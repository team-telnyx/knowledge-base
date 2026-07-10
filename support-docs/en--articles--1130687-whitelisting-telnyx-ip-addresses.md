---
source_url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
scraped: 2026-07-08
content_hash: 38e9951445c88d8ef3718a7d3d37b463289803d20106b238f44cb02c0ad1e7c2
---

Whitelisting Telnyx IP Addresses | Telnyx Help Center

[Skip to main content](#main-content)

# Whitelisting Telnyx IP Addresses

We will explain what Telnyx IP Addresses you will need to whitelist to ensure your service works properly.

Written by Telnyx Sales

March 25, 2025

Table of contents

## Whitelisting Telnyx IP Addresses

To ensure optimal performance of your Telnyx services, please whitelist the following IP addresses by region and purpose.  
​

## SIP Signaling and Media Servers

If your network uses a firewall or ACL, add both our media and SIP signaling IP addresses to your firewall’s whitelist.

For the most up-to-date IP addresses, refer to: [Telnyx IP Addresses](https://sip.telnyx.com).

---

## Webhooks

Telnyx programmable services, including **TeXML**, **Fax**, **Messaging**, and **Call Control**, deliver webhooks from the following regional IPs.  
​

**Note:** These IPs also apply to **WebSocket stream connections**, which are typically initiated using the **Dial** and **Start Stream** APIs. WebSocket traffic leverages the same delivery infrastructure as webhooks.

* **US**

  + CH1 (US-Central): 192.76.120.128/29
  + DC2 (US-East): 192.76.120.136/29
  + SV1 (US-West): 192.76.120.144/29
* **Europe**

  + LD6 (London, UK): 185.246.41.0/29
  + FR5 (Frankfurt, DE): 185.246.41.8/29
  + AM6 (Amsterdam, NL): 185.246.41.16/29
* **Asia-Pacific (APAC)**

  + SY1 (Sydney): 103.115.244.0/29
  + SG1 (Singapore): 103.115.244.8/29

---

## Network IP Address Assignments by Region

**AMER (North America)**

* **Main Pools:** 192.76.120.128/26 & 192.76.120.192/27

  + CH1 - US Central: 192.76.120.128/29
  + DC2 - US East: 192.76.120.136/29
  + SV1 - US West: 192.76.120.144/29
  + TR1 - Toronto: 192.76.120.160/29

**EMEA (Europe, Middle East, Africa)**

* **Main Pool:** 185.246.41.0/26

  + LD6 - London: 185.246.41.0/29
  + FR5 - Frankfurt: 185.246.41.8/29
  + AM6 - Amsterdam: 185.246.41.16/29

**APAC (Asia-Pacific)**

* **Main Pool:** 103.115.244.0/26

  + SY1 - Sydney: 103.115.244.0/29
  + SG1 - Singapore: 103.115.244.8/29

---

## Media IP Addresses

To ensure uninterrupted media delivery, whitelist the following media IP ranges:

* **36.255.198.128/25**
* **50.114.136.128/25**
* **50.114.144.0/21**
* **64.16.226.0/24**
* **64.16.227.0/24**
* **64.16.228.0/24**
* **64.16.229.0/24**
* **64.16.230.0/24**
* **64.16.248.0/24**
* **64.16.249.0/24**
* **103.115.244.128/25**
* **185.246.41.128/25**

---

## Region-Specific SIP FQDNs and IP Addresses

For location-specific SIP connections, whitelist the following FQDNs and IPs:

|  |  |  |  |
| --- | --- | --- | --- |
| Region | FQDN | Primary IP Address | Secondary IP Address |
| US | sip.telnyx.com | 192.76.120.10 | 64.16.250.10 |
| Europe | sip.telnyx.eu | 185.246.41.140 | 185.246.41.141 |
| Australia | sip.telnyx.com.au | 103.115.244.145 | 103.115.244.146 |
| Canada | sip.telnyx.ca | 192.76.120.31 | 64.16.250.13 |

For the latest and most accurate IP address information, visit [Telnyx IP Addresses](https://sip.telnyx.com).

---

Related Articles

[Configuring an AVAYA IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx)[Configuring a Vicidial IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx)[Configuring Grandstream GXP16XX with Telnyx](https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx)[Ip Authentication with X-Telnyx-Token](https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token)[Whitelisting Telnyx Media IP Addresses](https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses)

Did this answer your question?

😞😐😃

Table of contents
