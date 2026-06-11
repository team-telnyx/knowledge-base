---
title: Telnyx Networking
summary: Telnyx Networking provides private, direct cloud interconnections via Virtual
  Cross Connects (VXCs) and global edge routing via WireGuard-based Cloud VPN. It
  supports AWS, Azure, Google Cloud, and Megaport for dedicated backbone connectivity,
  and offers Global Edge Router for BGP-anycast failover across 25+ points of presence
  with platform-specific WireGuard guides for VMs, mobile devices, and firewalls.
sources:
- url: https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup
  content_hash: 38e8fb4b062ccf333a01a85a5c55cf64f2a1ce8797170dd06db9a09bca43e0c4
- url: https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect
  content_hash: 81d586d17af9f2151be09fe3f9289dbf02e7e4d2f7cce377254f924862d1dab0
- url: https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration
  content_hash: 726d23e81b11439d8039430039f438f3503381e9c4b88908f52211bfe4fac4e3
- url: https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx
  content_hash: 137fa43047fbd7d22d781b409a0e2a2f4e387aa94a2488b9a518216f906c661e
- url: https://support.telnyx.com/en/articles/8002565-how-to-configure-global-edge-router-with-telnyx
  content_hash: 4b3912e5814e8f4b2dbdc10c3384690d65381edc57c55b911479a2ebdb2e8c54
- url: https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing
  content_hash: 2373069f1cef6255f3f94a0f33b392d1203ec69ff2e4d094023d76d0a7d43c10
- url: https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail
  content_hash: c37bb3e5d49609b5635ede08b2a2c669160584424a75cc36e4a4c8075b36c10d
- url: https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu
  content_hash: b538845e2550e649d97c28739b2be8b6debe089aeffcdf227abdbf3dd639a43e
- url: https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc
  content_hash: b0f1c9dc3d23558e86f3c597cdd2f145310ebe46847582ce216344f006211aac
- url: https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms
  content_hash: 2f499dc9b50c9eebb60bb8ac8698ab06cb039f5328292ed78ac9660a23753a17
- url: https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios
  content_hash: ef6618967bf0d5287c1ff2e058d8044aa93fb5fa777ede9f83164b663117aff8
- url: https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms
  content_hash: fe7493e7086d57112ec02adfe56ec3c410defb86328adbad1fb63a472707d948
- url: https://support.telnyx.com/en/articles/8126141-intro-to-telnyx-edge-router
  content_hash: 3e9f78a1f33849dd29e047c5fb0f6c2e549d80e10ad1904e74dc4fe60719a306
- url: https://support.telnyx.com/en/articles/8174793-round-robin-routing
  content_hash: 469c54c3c55c87e20370fc3fb2b6b1e02871b93ee3bf1fd9c072ab1585951dad
- url: https://support.telnyx.com/en/articles/8201852-telnyx-networking-on-pfsense
  content_hash: c6bb4e02ed9f4a7193d32bed3c1d18687c43ffd311fddb57cece9f865b3b245e
- url: https://support.telnyx.com/en/collections/5317581-networking-using-telnyx
  content_hash: ecb3d37aecd93e9912ae01c3a43a967b45c015bcf792ebe7e0e38c0f5ee06878
updated_at: 2026-06-11T11:41:32Z
---

# Telnyx Networking

*Part 2 of 4 — see also: [Part 1](telnyx-networking--part-1.md), [Part 3](telnyx-networking--part-3.md), [Part 4](telnyx-networking--part-4.md)*

Telnyx Networking provides private, direct cloud interconnections via Virtual Cross Connects (VXCs) and global edge routing via WireGuard-based Cloud VPN. It supports AWS, Azure, Google Cloud, and Megaport for dedicated backbone connectivity, and offers Global Edge Router for BGP-anycast failover across 25+ points of presence with platform-specific WireGuard guides for VMs, mobile devices, and firewalls.

## Virtual Cross Connects

A Virtual Cross Connect (VXC) is a private, direct connection between a cloud provider and the Telnyx network backbone. VXCs are faster and safer than traditional public internet connections because they eliminate hops and reduce the risk of packet loss and jitter. Each VXC is managed through the Telnyx Mission Control Portal under the **Networking** section.

A **Network** in the Telnyx context uses virtual routing and forwarding (VRF) technology to provide a unique routing table within Telnyx's routers. A **Site** is a Telnyx Point of Presence (PoP) where Telnyx houses its network gear. When creating a VXC, select sites that are local to your cloud region for optimal performance.

### AWS Direct Connect VXC

Integrating an AWS VPC with Telnyx through a VXC uses AWS Direct Connect. The process involves five steps.

**Pre-requisites:** An AWS VPC must already exist, and you need the 12-digit AWS account number, AWS region, bandwidth speed, and a network name.

**Step 1 — Provide Telnyx with VXC preferences:** In the Mission Control Portal, navigate to **Networking > Create a New VXC** and provide the 12-digit AWS account number, AWS region, bandwidth speed, and network name. Telnyx will create 1 or 2 Direct Connect connections (2 if a redundant backup link was requested). This takes 1–3 days to complete. Preferences cannot be changed without creating a new VXC.

**Step 2 — Create a Virtual Private Gateway (VGW):** Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/), go to **Virtual Private Gateways > Create Virtual Private Gateway**, name the gateway, use the default ASN, and create it. Then select the VGW, click **Actions > Attach to VPC**, and attach it to your destination VPC.

**Step 3 — Accept pending Direct Connect connections:** Open the [AWS Direct Connect console](https://console.aws.amazon.com/directconnect/), navigate to **Connections**, and accept each pending connection by selecting the consent checkbox and clicking **Accept Connection**. Each connection should then show as available.

**Step 4 — Create a virtual interface for each circuit:** For each accepted connection, select **Actions > Create Virtual Interface**. Fill out the form as follows:
- **Public or Private:** Private
- **Virtual Interface Name:** Use the connection ID
- **Your router peer IP:** The Telnyx IP from the support email
- **Amazon router peer IP:** The customer IP from the Telnyx support email
- **BGP ASN:** From the Telnyx support email
- **BGP Authentication Key:** From the Telnyx support email

If a redundant backup link was requested, repeat for the second connection.

**Step 5 — Enable route propagation for VPC route tables:** Open the AWS Direct Connect console, click the **Route Propagate** tab, choose **Edit**, select the **Propagate** checkbox next to your VGW, and click **Save**. The routing table will display Telnyx prefixes routing to the VGW. When visible, the integration is complete and IP reachability can be tested.

For further reference, see the [AWS Direct Connect user guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) and [Direct Connect virtual interfaces guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html).

### Azure ExpressRoute VXC

Integrating an Azure cloud environment with Telnyx uses Azure ExpressRoute.

**Pre-requisite:** A Microsoft Azure cloud environment must exist.

**Step 1 — Prepare the Microsoft account for Azure ExpressRoute:** Log into the [Azure Portal](https://portal.azure.com/#home), search for *ExpressRoute*, click **ExpressRoute Circuits**, then click **Add > Provider**. The provider **must** be **Equinix**. Do **NOT** select *Allow Classic Operations*. Rename other fields at your discretion, click **OK**, and wait for deployment to complete.

**Step 2 — Set up the VXC in the Telnyx Mission Control Portal:** Log into the [Mission Control Portal](https://portal.telnyx.com), click **Networking**, then **Create New Network**. Name the network and click **Create Network**. Click **Add a Site**, choose the Telnyx Backbone Network to peer with, and click **Create VXC**. Select **Azure Express Route**, enter the **Azure Service Key** and **Microsoft Azure ASN** (typically 12076), then submit the VXC to the Telnyx Network team.

> **IMPORTANT:** Do NOT enable the Routing Status slider until coordinated with the Telnyx Network Team. Enabling routing without backend configuration may blackhole your voice traffic.

**Step 3 — Turn up routing and NAT configuration:** Arrange a maintenance window with Telnyx Network Engineering to complete backend configuration. [Contact Telnyx Support](https://telnyx.com/contact-us) to coordinate. Once the circuit is enabled using the Routing Status slider, the Azure ExpressRoute routing table will display Telnyx public ranges, ensuring they are preferred over internet routing.

### Google Cloud Partner Interconnect VXC

Integrating a Google Cloud VPC with Telnyx uses GCP Partner Interconnect and VLAN attachments.

**Pre-requisites:** A GCP VPC network must exist, ideally in the same region where the VXC will be built.

**Step 1 — Create a GCP Partner Interconnect and VLAN attachments:** Open the [Google Cloud Platform VPC](https://console.cloud.google.com/hybrid/interconnects/), choose **Partner Interconnect**, and under **Add Partner VLAN Attachment**, select *I already have a service provider*. Fill in:
- **Redundancy:** Telnyx recommends selecting *Create a redundant pair of VLAN attachments* (requires two VXCs)
- **VPC network:** default
- **Region:** same region as your software application
- **Cloud Router:** created in the same region as the VPC
- **Name:** use a naming convention such as `us-east-4-vlan-attachment-1`

Click **Create**, then **OK**. Open the VLAN Attachment Detail and copy the pairing key(s).

**Step 2 — Provide Telnyx with VXC preferences:** In the Mission Control Portal, go to **Networking > Create New Network** (or view an existing one). In the **Site Detail** section, click **Add Site(s) > Create VXC**. Select **Google Cloud**, choose bandwidth speed, input the **Google Pairing Key** for the primary VLAN attachment (the last number should be "1"), and if redundant, input the secondary pairing key. Click **Create VXC**.

**Step 3 — Activate the VXC in Google Cloud:** Open the GCP VPC console. For each VLAN attachment, click **Activate** under Actions (may take up to 5 minutes to appear), then **Accept**. Configure BGP: click **Configure BGP**, set **Peer ASN** to **63440**, and click **Save and Continue**. Click **Refresh** — status should say **Up**. Copy the **Cloud Router IP** for each VLAN attachment.

**Step 4 — Complete the order in Telnyx:** In the Mission Control Portal, paste the **Cloud Router IP** for each VLAN attachment and click **Save**. Telnyx will approve the request (up to 3 hours); the Order Status will change from **Pending** to **Active** to **Complete**. Once complete, the BGP session is active. To receive traffic, cloud hosts must have public IP addresses configured. Under routing status, click **Enable** — this transitions packet delivery from internet transit to the private VXC, causing a brief traffic disruption. Consult your Telnyx representative before enabling if you need assistance.

For further reference, see [Google VPC documentation](https://cloud.google.com/vpc#section-4) and [VLAN attachments documentation](https://cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments).

### Megaport Configuration

Megaport is a Network as a Service provider that enables dedicated access to cloud providers. The Telnyx–Megaport integration uses a service key provided by Telnyx.

**Pre-requisites:** The Mission Control Portal must be configured, TLS encryption is recommended, and Megaport ports must be live on both ends.

**Step 1 — Create a connection in the Megaport portal:** Log into Megaport, click **+ Connection**, then **Enter Service Key**. Provide the **Megaport Service Key ID** (obtained from Telnyx Support). Confirm the auto-filled details:
- **Name:** a descriptive connection name
- **Rate limit:** a network traffic cap
- **Preferred A-End VLAN:** a unique VLAN ID (2–4093); if unspecified, Megaport assigns one

Click **Next**, then **Add VXC**. View your cart and click **Order** — this sends an email to Telnyx for approval. Once Telnyx approves, the VXC between Megaport and Telnyx is created.

For further reference, see [Megaport documentation](https://docs.megaport.com/) and [Megaport support](https://docs.megaport.com/support/contact/).
