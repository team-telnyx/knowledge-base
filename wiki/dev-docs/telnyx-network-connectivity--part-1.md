---
title: Telnyx Network Connectivity
summary: Telnyx provides private network connectivity through Virtual Cross Connects
  (VXC) to AWS, GCP, and Azure, enabling direct BGP-peered links between your cloud
  environment and the Telnyx network, as well as Wireguard-based VPN peer configuration
  for Linux, macOS, and Windows clients.
sources:
- url: https://developers.telnyx.com/docs/network/vxc/azure
  content_hash: cf592f8687461a1f46f07fe95241acb199d62bb40986b57932f83bde4c2b7aca
- url: https://developers.telnyx.com/docs/network/vxc/cost
  content_hash: b54d26125a828e8b063ad2bfbbd839ca57d6a2593148620f2b1fe4ba1c337c5b
- url: https://developers.telnyx.com/docs/network/vxc/coverage
  content_hash: bc793073a6b2f3ed535727b3b1fc28309839fec26ebd458952d90609c08615e5
- url: https://developers.telnyx.com/docs/network/vxc/gcp
  content_hash: c1f05cd32a55465f372db2b393b56448465c91771387dfa1b577eac3fe71cbe2
- url: https://developers.telnyx.com/docs/network/vxc/intro/index
  content_hash: 57114b3546b6bd95e02062bad9bb1459bd96112a29c91a9c3206db7384963b69
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/linux
  content_hash: 8417a3872274ccbd6530290a81396afc04002f67f744675f07c138615196a5ba
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/macos
  content_hash: 8e0eca1f8befece163b6381a971deb70cda8e882ab323ba86cb327ae6aa4cb15
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/windows
  content_hash: 08e66fcdc5bfcfa31a4af758e66b12964075a5b8fd3bd60e4aef2addcaf68b2b
updated_at: 2026-06-11T10:38:58Z
---

# Telnyx Network Connectivity

*Part 1 of 2 — see also: [Part 2](telnyx-network-connectivity--part-2.md)*

Telnyx provides private network connectivity through Virtual Cross Connects (VXC) to AWS, GCP, and Azure, enabling direct BGP-peered links between your cloud environment and the Telnyx network, as well as Wireguard-based VPN peer configuration for Linux, macOS, and Windows clients.

## Virtual Cross Connects (VXC)

VXC creates a private, dedicated link between a Telnyx network and your cloud provider environment. After choosing a provider, refer to the [coverage API](https://developers.telnyx.com/docs/network/coverage) to confirm availability in your desired region, then follow the provider-specific setup guide.

### VXC Coverage and Availability

Before provisioning, use the coverage API to ensure the desired region and bandwidth are offered. Available regions and bandwidths vary by provider.

### VXC Pricing

Both Telnyx and your cloud provider charge for VXC usage. Telnyx charges a monthly recurring fee (MRC) per instance; cloud-provider charges are separate and outside Telnyx's control.

**AWS and GCP** share the same pricing schedule:

| Bandwidth | Monthly Recurring Charge (USD) |
|---|---|
| 50 Mbps | 100 |
| 100 Mbps | 125 |
| 200 Mbps | 150 |
| 300 Mbps | 175 |
| 400 Mbps | 200 |
| 500 Mbps | 225 |
| 1 Gbps | 450 |

**Azure** pricing is higher:

| Bandwidth | Monthly Recurring Charge (USD) |
|---|---|
| 50 Mbps | 200 |
| 100 Mbps | 250 |
| 200 Mbps | 300 |
| 300 Mbps | 400 |
| 400 Mbps | 500 |
| 500 Mbps | 600 |
| 1 Gbps | 1000 |

### Azure VXC Setup

#### Prerequisites

**Create an ExpressRoute Circuit (Azure):**

| Parameter | Value |
|---|---|
| Region | Match an available region from the VXC coverage API |
| Port Type | Provider |
| Provider | Equinix |
| Peering location | Matching available region from the VXC coverage API |
| Bandwidth | Choose an available bandwidth from the VXC coverage API |
| SKU | Standard |

After creation, the "Provider status" should read **Not provisioned**. Copy the **Service key** — you will need it for the Telnyx VXC resource.

**Create a Telnyx Network:** If you do not already have a [network](telnyx-networks.md), follow the network creation guide first.

#### Procedure

1. **Create a VXC resource (Telnyx API):**

   ```
   POST /v2/virtual_cross_connects
   ```

   ```json
   {
       "network_id": "{{your network UUID}}",
       "name": "my-first-azure-vxc",
       "cloud_provider": "azure",
       "cloud_provider_region": "Frankfurt",
       "primary_cloud_account_id": "xxxxxx",
       "bgp_asn": 12076
   }
   ```

   | Parameter | Value |
   |---|---|
   | `cloud_provider` | `azure` |
   | `cloud_provider_region` | Matching region from the ExpressRoute circuit |
   | `primary_cloud_account_id` | Service key from the ExpressRoute circuit |
   | `bgp_asn` | Azure's BGP ASN: `12076` |

   Note the following from the response: `id`, `primary_cloud_ip`, `primary_bgp_key`.

2. **Enable the primary connection (Telnyx API):**

   ```
   PATCH /v2/virtual_cross_connects/:vxc_uuid
   ```

   ```json
   {
       "primary_enabled": true
   }
   ```

   Poll the VXC status via `GET /v2/virtual_cross_connects/:vxc_uuid` and confirm `status` is `provisioned` before proceeding.

3. **Configure Azure Private Peering (Azure portal):**

   The ExpressRoute "Provider status" must show **Provisioned** before this step.

   | Parameter | Value |
   |---|---|
   | Peer ASN | `63440` (Telnyx BGP ASN) |
   | Subnets | IPv4 |
   | IPv4 Primary subnet | The /30 block that includes `primary_cloud_ip` |
   | IPv4 Secondary subnet | The next /30 block |
   | VLAN ID | Any valid VLAN number |
   | Shared key | `primary_bgp_key` from the VXC response |
   | Public IP address | Create new |
   | Public IP address SKU | Standard |

   After saving, click **View route table** — you should see Telnyx IPs advertised. You may need to wait briefly before routes appear.

4. **(Optional) Create a Virtual Network, Gateway, and VM for testing:**

   - **Virtual Network:** Create in the same region; add a Gateway subnet with defaults.
   - **Virtual Network Gateway:** Set Gateway type to **Express Route**, SKU **Standard**, and attach the virtual network and a Standard public IP. Creation can take 20+ minutes.
   - **Virtual Machine:** Create in the same region and virtual network.
   - **Gateway Connection:** Add a connection of type **Express Route** linking the virtual network gateway and ExpressRoute circuit, with Routing weight `0`.

5. **Validate the connection:** SSH into the VM and run `traceroute sip.telnyx.com` (or `sip.telnyx.eu`). The next hop should match the Azure Private Peering configuration.

### GCP VXC Setup

#### Prerequisites

**Create a VLAN Attachment (Google Cloud Console):**

- Choose **Partner Interconnect Connection** → **Set up unencrypted Interconnect**.
- Select your VPC network and a region with a nearby Telnyx PoP.
- Set **MTU** to `8896`.
- Create or select a Cloud Router.

After creation, note the pairing key and Google-assigned BGP IPs.

**Create a Telnyx Network:** Follow the network creation guide if needed.

#### Procedure

1. **Create a VXC resource (Telnyx API):**

   ```
   POST /v2/virtual_cross_connects
   ```

   ```json
   {
       "network_id": "{{your network UUID}}",
       "name": "my-gcp-vxc",
       "cloud_provider": "gce",
       "cloud_provider_region": "europe-west3",
       "primary_cloud_account_id": "xxxx/europe-west3/2",
       "bgp_asn": 16550,
       "bandwidth_mbps": 50
   }
   ```

   Note the `id`, `primary_cloud_ip`, `primary_telnyx_ip`, and `primary_bgp_key` from the response.

2. **Activate the connection (Google Cloud Console):**

   Use the pairing key from the VLAN attachment. Set:
   - **Peer ASN:** `63440` (Telnyx)
   - **MD5 Authentication:** `primary_bgp_key` from the VXC response

3. **Update BGP peering (Telnyx API):**

   After activation the connection initially shows as "Down". Retrieve the Google-assigned BGP IPs and update the VXC:

   ```
   PATCH /v2/virtual_cross_connects/:vxc_uuid
   ```

   ```json
   {
       "primary_enabled": true,
       "primary_cloud_ip": "169.254.131.250/29",
       "primary_telnyx_ip": "169.254.131.249/29"
   }
   ```

   - `primary_cloud_ip` — the "Cloud Router BGP IP" / "Remote IP" shown in the Google troubleshooting page.
   - `primary_telnyx_ip` — the "BGP peer IP" / "Local IP" shown in the Google troubleshooting page.

   After this update, the Google-side status should change to **Up**.

4. **Validate the connection:** Under VPC networks, verify that routes advertised over the Cloud Router appear. You can also SSH into an instance and run `traceroute sip.telnyx.com` — the path should traverse the Telnyx network.
