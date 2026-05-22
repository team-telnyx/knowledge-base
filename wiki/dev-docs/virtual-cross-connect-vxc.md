---
title: Virtual Cross Connect (VXC)
summary: 'A concise guide to Telnyx Virtual Cross Connects (VXCs): where they’re available,
  how they’re priced, the core API, and the high-level steps to set up private connectivity
  to AWS Direct Connect, Google Cloud Interconnect, and Azure ExpressRoute.'
sources:
- url: https://developers.telnyx.com/docs/network/vxc/intro/index
- url: https://developers.telnyx.com/docs/network/vxc/api
- url: https://developers.telnyx.com/docs/network/vxc/aws/index
- url: https://developers.telnyx.com/docs/network/vxc/azure
- url: https://developers.telnyx.com/docs/network/vxc/cost
- url: https://developers.telnyx.com/docs/network/vxc/coverage
- url: https://developers.telnyx.com/docs/network/vxc/gcp
updated_at: 2026-05-20T09:18:09Z
---

# Virtual Cross Connect (VXC)

A concise guide to Telnyx Virtual Cross Connects (VXCs): where they’re available, how they’re priced, the core API, and the high-level steps to set up private connectivity to AWS Direct Connect, Google Cloud Interconnect, and Azure ExpressRoute.

## What you can do with a VXC
A Virtual Cross Connect (VXC) gives you private, high-performance connectivity between your Telnyx network and your cloud environment. Telnyx supports native integrations with AWS Direct Connect, Google Cloud Partner Interconnect, and Azure ExpressRoute.

## Coverage and availability
- Before building, confirm the service is offered at your desired location and bandwidth.
- See [VXC Coverage](vxc-coverage.md) for guidance; the Telnyx Coverage API is also documented at https://developers.telnyx.com/docs/network/coverage.

## Pricing
- You will be charged by Telnyx and by your cloud provider. Telnyx fees may change at Telnyx’s discretion under the general T&C, and Telnyx cannot advise on your cloud provider’s billing.
- Monthly Recurring Charge (USD) per VXC:
  - AWS and GCP: 50 Mbps $100; 100 Mbps $125; 200 Mbps $150; 300 Mbps $175; 400 Mbps $200; 500 Mbps $225; 1 Gbps $450
  - Azure: 50 Mbps $200; 100 Mbps $250; 200 Mbps $300; 300 Mbps $400; 400 Mbps $500; 500 Mbps $600; 1 Gbps $1000
- Details: [VXC Cost](vxc-cost.md)

## API overview
- Resource: /v2/virtual_cross_connects
- Required in every create request:
  - network_id: the Telnyx Network to associate to. If you don’t have one, create it first (guide: https://developers.telnyx.com/docs/network/networks).
  - name: a human-readable label.
- Other fields are cloud-provider specific (see below).
- Post-creation operations commonly used:
  - Enable data plane: PATCH primary_enabled = true (after the cloud side is ready/accepted).
  - Poll status with GET until provisioned (especially important for Azure before peering steps).
- Useful fields returned by the VXC object (used in cloud configuration): id, primary_cloud_ip, primary_telnyx_ip, primary_bgp_key.
- Full API notes: [VXC API](vxc-api.md)

## Provider-specific creation parameters
Use these at VXC creation time in addition to network_id and name. Choose bandwidth_mbps from options available in coverage.

- AWS (Direct Connect)
  - cloud_provider: aws
  - cloud_provider_region: AWS region (for example, eu-central-1)
  - primary_cloud_account_id: your AWS Account ID
  - bgp_asn: 64512 (Amazon default ASN)
  - bandwidth_mbps: available capacity per coverage

- Google Cloud (Partner Interconnect)
  - cloud_provider: gce
  - cloud_provider_region: a Google region with a nearby Telnyx PoP (for example, europe-west3)
  - primary_cloud_account_id: Google Partner Interconnect pairing key from your VLAN attachment (for example, xxxx/europe-west3/2)
  - bgp_asn: 16550 (Google)
  - bandwidth_mbps: available capacity per coverage

- Azure (ExpressRoute)
  - cloud_provider: azure
  - cloud_provider_region: the region/peering location used on the ExpressRoute circuit (for example, Frankfurt)
  - primary_cloud_account_id: the ExpressRoute Service Key
  - bgp_asn: 12076 (Azure)
  - bandwidth is selected on the ExpressRoute circuit (not in the VXC request)

Telnyx BGP ASN to use on the cloud side when prompted: 63440.

## AWS setup (Direct Connect)
High-level procedure. For detailed, step-by-step screenshots, see [AWS VXC Setup](aws-vxc-setup.md).

- In AWS (prerequisites):
  - Create a VPC in the intended region; create subnet(s) and optional Internet Gateway; set up route tables as needed.
  - Create a Virtual Private Gateway (VGW), note the AWS ASN (default 64512), and attach it to your VPC.
  - (Optional) Launch an EC2 instance in the VPC to validate connectivity later.
  - Note your AWS Account ID (you’ll use it in the VXC request).
- In Telnyx:
  - Create the VXC with cloud_provider=aws and the parameters above; record the returned VXC id. If the AWS-side connection isn’t accepted within 1 hour, Telnyx will delete the VXC and you must recreate it.
- In AWS:
  - Accept the new Direct Connect connection.
  - Create a Private Virtual Interface (VIF):
    - Type: Private; Owner: My AWS account; Gateway type: Virtual Private Gateway and select your VGW.
    - BGP Peer ASN: 63440 (Telnyx).
    - If available, use the VXC’s primary_telnyx_ip (Your router peer IP), primary_cloud_ip (Amazon router peer IP), and primary_bgp_key (BGP MD5 key).
- In Telnyx:
  - Enable the primary connection (set primary_enabled = true). AWS will show the connection as available.
- Validate:
  - From your EC2 instance, traceroute/ping a Telnyx-advertised prefix. Routes should traverse the VXC rather than the public Internet.

## Google Cloud setup (Partner Interconnect)
High-level procedure. For detailed, step-by-step screenshots, see [Google VXC Setup](google-vxc-setup.md).

- In Google Cloud (prerequisites):
  - Create a Partner Interconnect VLAN attachment:
    - Choose your VPC network and region (near a Telnyx PoP), MTU 8896.
    - Create or select a Cloud Router.
    - Capture the Partner pairing key (used as primary_cloud_account_id in the VXC request).
- In Telnyx:
  - Create the VXC with cloud_provider=gce and the parameters above; record the VXC id.
- In Google Cloud:
  - Activate the connection on the VLAN attachment:
    - Peer ASN: 63440 (Telnyx).
    - MD5 authentication: use the VXC’s primary_bgp_key.
- In Telnyx:
  - Update BGP peering details on the VXC with the Google-assigned IPs:
    - primary_cloud_ip = Google “Cloud Router BGP IP” (Remote IP).
    - primary_telnyx_ip = Google “BGP peer IP” (Local IP).
  - Enable the primary connection (primary_enabled = true).
- Validate:
  - Check advertised routes under VPC Networks → Routes and/or traceroute from a VM. Status should be Up on Google.

## Azure setup (ExpressRoute)
High-level procedure. For detailed, step-by-step screenshots, see [Azure VXC Setup](azure-vxc-setup.md).

- In Azure (prerequisites):
  - Create an ExpressRoute circuit:
    - Provider: Equinix; Port type: Provider.
    - Region/Peering location and Bandwidth: select values available in coverage.
    - SKU: Standard.
    - Provider status will show Not provisioned initially. Note the Service Key.
- In Telnyx:
  - Create the VXC with cloud_provider=azure using your ExpressRoute Service Key and region.
  - Wait until VXC status is provisioned, then enable the primary connection (primary_enabled = true).
- In Azure:
  - Configure Private Peering on the ExpressRoute circuit:
    - Peer ASN: 63440 (Telnyx).
    - Subnets: IPv4. Use /30s that include the VXC primary_cloud_ip (primary subnet) and the next /30 (secondary).
    - VLAN ID: any valid VLAN.
    - Shared key: use the VXC’s primary_bgp_key.
  - (For lab validation) Create a Virtual Network, add a Gateway Subnet, then deploy a Virtual Network Gateway (ExpressRoute, Standard) and connect it to the ExpressRoute circuit. Optionally deploy a VM in that VNet.
- Validate:
  - When the circuit, VNet, gateway, and connection are up, traceroute to sip.telnyx.com and sip.telnyx.eu from the VM. Next hop should match the ExpressRoute Private Peering path.

## Operational tips and status
- Acceptance windows: On AWS, you must accept the Direct Connect from your AWS account within 1 hour of VXC creation or the VXC is deleted.
- Bandwidth selection: Choose bandwidth_mbps values supported in your chosen region (see [VXC Coverage](vxc-coverage.md)).
- Enabling traffic: Don’t set primary_enabled = true until the cloud side is ready (for Azure, wait until the VXC status is provisioned; for AWS, enable after accepting the connection; for GCP, enable after configuring the VLAN attachment and MD5 key, and after setting the assigned BGP IPs on the VXC).
- Troubleshooting BGP:
  - Cloud-side Peer ASN is always Telnyx 63440.
  - If your cloud requires IP/MD5 details, use values returned by the VXC (primary_cloud_ip, primary_telnyx_ip, primary_bgp_key).
- Deep dives and screenshots: [AWS VXC Setup](aws-vxc-setup.md), [Google VXC Setup](google-vxc-setup.md), [Azure VXC Setup](azure-vxc-setup.md).
