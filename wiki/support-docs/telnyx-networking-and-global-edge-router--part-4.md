---
title: Telnyx Networking and Global Edge Router
summary: This page covers Telnyx's network equipment, the Global Edge Router product
  (including its WireGuard-based architecture, benefits, multi-cloud use cases, and
  pricing), and step-by-step setup guides for connecting the Edge Router to AWS Lightsail,
  AWS VPC, Azure Linux VMs, Oracle VMs, pfSense, and Android/iOS devices. It also
  includes instructions for setting up the Telnyx side of the configuration via the
  Mission Control portal or API, verifying connectivity, and creating a Postman collection
  from the Telnyx OpenAPI specification.
sources:
- url: https://support.telnyx.com/en/articles/1130675-what-kind-of-equipment-do-you-use
- url: https://support.telnyx.com/en/articles/4353862-creating-postman-collection-from-openapi
- url: https://support.telnyx.com/en/articles/8002565-how-to-configure-global-edge-router-with-telnyx
- url: https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing
- url: https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail
- url: https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc
- url: https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms
- url: https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios
- url: https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms
- url: https://support.telnyx.com/en/articles/8126141-intro-to-telnyx-edge-router
- url: https://support.telnyx.com/en/articles/8201852-telnyx-networking-on-pfsense
- url: https://support.telnyx.com/en/collections/5317581-networking-using-telnyx
updated_at: 2026-07-17T09:06:19Z
---

# Telnyx Networking and Global Edge Router

*Part 4 of 4 — see also: [Part 1](telnyx-networking-and-global-edge-router--part-1.md), [Part 2](telnyx-networking-and-global-edge-router--part-2.md), [Part 3](telnyx-networking-and-global-edge-router--part-3.md)*

This page covers Telnyx's network equipment, the Global Edge Router product (including its WireGuard-based architecture, benefits, multi-cloud use cases, and pricing), and step-by-step setup guides for connecting the Edge Router to AWS Lightsail, AWS VPC, Azure Linux VMs, Oracle VMs, pfSense, and Android/iOS devices. It also includes instructions for setting up the Telnyx side of the configuration via the Mission Control portal or API, verifying connectivity, and creating a Postman collection from the Telnyx OpenAPI specification.

## Verifying Connectivity

After deploying on any platform, you can verify the connection by checking the [Mission Control portal](https://portal.telnyx.com/#/app/networking/cloudvpn/) to see the last seen status change, or by curling/tracing into your server to confirm the Global IP configured to it. Example response:

```
root@MacBook-Pro % ping 172.27.1.17
PING 172.27.1.17 (172.27.1.17): 56 data bytes
64 bytes from 172.27.1.17: icmp_seq=0 ttl=53 time=184.512 ms
64 bytes from 172.27.1.17: icmp_seq=1 ttl=53 time=183.202 ms
64 bytes from 172.27.1.17: icmp_seq=2 ttl=53 time=183.365 ms
64 bytes from 172.27.1.17: icmp_seq=3 ttl=53 time=183.040 ms
64 bytes from 172.27.1.17: icmp_seq=4 ttl=53 time=183.310 ms
64 bytes from 172.27.1.17: icmp_seq=5 ttl=53 time=183.980 ms
64 bytes from 172.27.1.17: icmp_seq=6 ttl=53 time=183.457 ms
64 bytes from 172.27.1.17: icmp_seq=7 ttl=53 time=183.097 ms
^C
--- 172.27.1.17 ping statistics ---
8 packets transmitted, 8 packets received, 0.0% loss
round-trip min/avg/max/stddev = 183.040/183.495/184.512/0.471 ms
```

## Creating a Postman Collection from the Telnyx OpenAPI

To get all of Telnyx API v2 into Postman in a few clicks:

1. Navigate to <https://github.com/team-telnyx/openapi/tree/master/openapi>.
2. From Postman, import the JSON via the raw link in GitHub or a downloaded file.

   ![Postman collection page.](_images/b71bba14c6559120.png)

   Use the default settings.

   ![Default settings page on Postman.](_images/0be23cb33799271b.png)

3. Add your API token to the collection.

   ![Authentication section interface on Postman.](_images/0aede94b05f80fbc.png)

   ![Authentication interface on Postman.](_images/d424884077d5f5ee.png)

4. Use the API.

   ![An array of API codes on Postman.](_images/b2c03189e6c2e560.png)

## Related Articles

- [Intro to Telnyx Edge Router](intro-to-telnyx-edge-router.md)
- [How to configure Global Edge Router with Telnyx](how-to-configure-global-edge-router-with-telnyx.md)
- [Global IP & Edge Routing](global-ip-edge-routing.md)
- [Telnyx Networking on AWS Lightsail](telnyx-networking-on-aws-lightsail.md)
- [Telnyx Networking on AWS VPC](telnyx-networking-on-aws-vpc.md)
- [Telnyx Networking on Azure Linux VMs](telnyx-networking-on-azure-linux-vms.md)
- [Telnyx Networking on Android/iOS](telnyx-networking-on-android-ios.md)
- [Telnyx Networking on Oracle VMs](telnyx-networking-on-oracle-vms.md)
- [Telnyx Networking on PfSense](telnyx-networking-on-pfsense.md)
- [Creating Postman Collection from OpenAPI](creating-postman-collection-from-openapi.md)
- [What kind of equipment do you use?](what-kind-of-equipment-do-you-use.md)

## Support and Feedback

For questions or feedback, message [community@telnyx.com](mailto:community@telnyx.com) and include the link to the article you are referencing along with any concerns or comments. 24/7 world-class support is available by phone at +18889809750 ext 2, by email at [support@telnyx.com](mailto:support@telnyx.com), or via chat by clicking the chat bubble in the bottom right of your [Mission Control Portal](https://portal.telnyx.com/) account. For discussion purposes, you can also join the Telnyx Slack at <https://joinslack.telnyx.com/>.
