---
source_url: https://support.telnyx.com/en/articles/8201852-telnyx-networking-on-pfsense
scraped: 2026-06-11
---

Telnyx Networking on PfSense | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx Networking on PfSense

Guide on setting up Telnyx networking on pfSense. Ensure seamless connectivity!

Written by Telnyx Engineering

December 11, 2023

Table of contents

# PfSense with the Telnyx Network

## Step 1: Telnyx Configuration with PfSense

Reference the introduction to Telnyx Networking section located here: [Telnyx Configuration](https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing)

Copy and take note of the Peer Configuration file along with the private key that you got assigned from the above tutorial, it should look like the following:

[![Peer Configuration file. ](https://downloads.intercomcdn.com/i/o/779406840/c9bd1538ae6d5dbea52f740d/peer_conf.png?expires=1781168400&signature=ecfba5f5e81aefbd874e28146be277f7e4e95964e4a92a11163a86769c6db927&req=cycuEsl4lYVfFb4f3HP0gKiuyJL9hNmCzZHm7hb8TAnafDlmK7zZ1YosGpYs%0AVPt1R98YeoA%2FNvzeKQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779406840/c9bd1538ae6d5dbea52f740d/peer_conf.png?expires=1781168400&signature=ecfba5f5e81aefbd874e28146be277f7e4e95964e4a92a11163a86769c6db927&req=cycuEsl4lYVfFb4f3HP0gKiuyJL9hNmCzZHm7hb8TAnafDlmK7zZ1YosGpYs%0AVPt1R98YeoA%2FNvzeKQ%3D%3D%0A)

## Step 1.5 Telnyx Setup using API

We can also utilize direct API calls to set up everything from above

1. Create a new Network

```
curl --request POST \  
  --url https://api.telnyx.com/v2/networks \  
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>' \  
  --header 'Content-Type: application/json' \  
  --data '{  
    "name": "Test Network"  
}'
```

2. Create a Wireguard Interface

```
curl -i -X POST \  
  https://api.telnyx.com/v2/wireguard_interfaces \  
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \  
  -H 'Content-Type: application/json' \  
  -d '{  
    "network_id": "<NETWORK_ID_HERE>",  
    "name": "test interface",  
    "region_code": "ashburn-va"  
  }'
```

3. Create a Wireguard Peer

```
curl -i -X POST \  
  https://api.telnyx.com/v2/wireguard_peers \  
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \  
  -H 'Content-Type: application/json' \  
  -d '{  
    "wireguard_interface_id": "<WIREGUARD_INTERFACE_ID_HERE>"  
  }'
```

Note: At this current stage, only ports 80/443 are supported and are looking into broadening this to encompass more ports.

## Step 2. PfSense Configuration

1. Ensure you have the Wireguard package installed
2. Setup Wireguard on Pfsense

   1. Navigate to VPN -> Wireguard
   2. Add a new Tunnel

      1. Give the tunnel a descriptive name, like telnyx\_wg.
      2. Paste the Private Key from **Telnyx Setup: 3. Create a Wireguard Peer** into Private Key for the Interface Keys.
   3. Add a new Peer

      1. Uncheck the Dynamic Endpoint
      2. Paste the Endpoint from **Telnyx Setup: 3. Create a Wireguard Peer** into Endpoint.
      3. Paste the Public Key from **Telnyx Setup: 3. Create a Wireguard Peer** into Public Key
      4. Paste the allowed IPs from **Telnyx Setup: 3. Create a Wireguard Peer** into Allowed IPs
3. Setup the Interface for Wireguard

   1. Navigate to Interface -> Assignments
   2. Add a new interface with the Wireguard tunnel (ie, telnyx\_wg)
   3. Click on the Interface to edit it

      1. Set IPv4 Configuration Type to Static IPv4
      2. Under Static IPv4 Configuration, set the IPv4 Address to the Interface Address found in **Telnyx Setup: 3. Create a Wireguard Peer**
      3. Select /16 for the subnet mask.

## Step 3. Setting up 1:1 NAT and outbound NAT

You will need two NAT configs:

* The 1:1 NAT so that when traffic ingresses through your Wireguard peer, it will route to your service VM
* Outbound NAT so that your service VM can send the traffic back to your pfsense instance without needing to know about the route to the Wireguard interface, and your pfsense instance can send the traffic back to the Wireguard gateway

1. Create a 1:1 NAT mapping with the following:

   1. Interface: the Wireguard tunnel interface
   2. External subnet: Wireguard tunnel Interface address
   3. Internal IP: the IP address of the machine you are hosting your machine on

[![Wireguard firewall interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/797880632/dae3859e0ec59e140ed78375/-MX7QTShgaTyq0y7fitEmx7nWuG6dWKDRfzpRx_ipElLZO9LggH7DhJeoIvecIMQXM_izK4HaImVTAdfw5iUZ_uSHS2i12idNlBhFFJR3EFHPfXcEHe_v5Vhw7fePVBIdDJ49SB5sk6x2Yo6h8WDYUM?expires=1781168400&signature=ada51f0c02f406a229de34e9f5f19246779e1eff9cb6a4e39a006e05e373543d&req=cykgHsF%2Bm4JdFb4f3HP0gDXmOMhkl91JPMoBMR9mA5CAVVtOtvzLFSNVyj5d%0APs3u%2Bn%2B1qLQXLwCjmw%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/797880632/dae3859e0ec59e140ed78375/-MX7QTShgaTyq0y7fitEmx7nWuG6dWKDRfzpRx_ipElLZO9LggH7DhJeoIvecIMQXM_izK4HaImVTAdfw5iUZ_uSHS2i12idNlBhFFJR3EFHPfXcEHe_v5Vhw7fePVBIdDJ49SB5sk6x2Yo6h8WDYUM?expires=1781168400&signature=ada51f0c02f406a229de34e9f5f19246779e1eff9cb6a4e39a006e05e373543d&req=cykgHsF%2Bm4JdFb4f3HP0gDXmOMhkl91JPMoBMR9mA5CAVVtOtvzLFSNVyj5d%0APs3u%2Bn%2B1qLQXLwCjmw%3D%3D%0A)

2. Create an Outbound NAT with the following:

1. Interface: WAN interface (or whichever interface your VM is also listening on)
2. Address Family: IPv4 + IPv6
3. Protocol: any (restrict as you would like)
4. Source: Any (restrict as you would like)
5. Destination: specify the IP address of your VM on the Interface
6. Translation

   1. Address: Interface Address

[![Advanced Outbound NAT Entry. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/797880648/179702c4b4cb10c04c019461/0CkqvSYQeprQ0zoDQAkDR86nG44mr8EY3Y7pY9MDmqJaxCRafWixxdM2dH9uq5oruq7Hg4ZCcXj7uK5OcrS673YpCS2Ceq9yK_4OSd5WrsQ97PtQScLofFRQqq8HGA5kZVrVPo5X0f6AEEW3b8cOK2c?expires=1781168400&signature=125aa93c1ce00d26b2bd93ba2f34e38658e97a672b0b3926a03bd0605ef82c68&req=cykgHsF%2Bm4VXFb4f3HP0gCDh8yrMSoYWgj08M01GJztsjn4aCeN8cg95TvyO%0AtFodeey1aQ4Ci3hzVg%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/797880648/179702c4b4cb10c04c019461/0CkqvSYQeprQ0zoDQAkDR86nG44mr8EY3Y7pY9MDmqJaxCRafWixxdM2dH9uq5oruq7Hg4ZCcXj7uK5OcrS673YpCS2Ceq9yK_4OSd5WrsQ97PtQScLofFRQqq8HGA5kZVrVPo5X0f6AEEW3b8cOK2c?expires=1781168400&signature=125aa93c1ce00d26b2bd93ba2f34e38658e97a672b0b3926a03bd0605ef82c68&req=cykgHsF%2Bm4VXFb4f3HP0gCDh8yrMSoYWgj08M01GJztsjn4aCeN8cg95TvyO%0AtFodeey1aQ4Ci3hzVg%3D%3D%0A)

---

Related Articles

[How to configure Global Edge Router with Telnyx](https://support.telnyx.com/en/articles/8002565-how-to-configure-global-edge-router-with-telnyx)[Telnyx Networking on Ubuntu](https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu)[Telnyx Networking on AWS VPC](https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc)[Telnyx Networking on Azure Linux VMs](https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms)[Telnyx Networking on Oracle VMs](https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms)

Did this answer your question?

😞😐😃

Table of contents
