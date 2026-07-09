---
source_url: https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu
scraped: 2026-07-08
content_hash: fef16392bbc3c0966a76c3c57be921953e7774fa9d5c8b0e2064b1de00a27454
---

Telnyx Networking on Ubuntu | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx Networking on Ubuntu

Tutorial on connecting a Digital Ocean Ubuntu Server to Telnyx's Cloud VPN via WireGuard.

Written by Telnyx Engineering

October 30, 2023

Table of contents

In this tutorial, you’ll learn how you can connect a Digital Ocean Ubuntu Server via WireGuard to a [Cloud VPN](https://telnyx.com/products/cloud-vpn) interface on the Telnyx network.

# Setting up Telnyx Networking with Digital Ocean (Ubuntu)

​**Pre-requisites**

Before following these steps, you'll need to create a Telnyx Account, grab your API key and create a **Network.** Head to our Networking Quickstart Guide to get started!

You'll also need to [create a Digital Ocean Ubuntu Server](https://docs.digitalocean.com/products/droplets/how-to/create/) and [run extra setup steps for greater security](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04).

---

## **Step 1: Install Wireguard on the Server**

Log onto your Digital Ocean Ubuntu Server and execute the following command:  
​

```
sudo apt install wireguard
```

## **Step 2: Generate public and private keys**

In this step you will use the WireGuard key generation tool to create the public and private keys needed to communicate with the Cloud VPN server on the Telnyx network.

```
wg genkey | tee privatekey | wg pubkey > publickey
```

Print both keys to screen as you will need both of them soon.

```
cat privatekey
```

```
cat publickey
```

> **Note:**The `private\_key` will be needed later to build the Cloud VPN peer configuration. The `public\_key` will be used when creating the Cloud VPN peer

## **Step 3: Create a Cloud VPN Interface**

Create a Cloud VPN Interface associated with the Network that you created in the Networking Quickstart Guide. This network interface is configured on the Telnyx network and acts as a tunnel interface.

​**Create a Cloud VPN Interface with the Telnyx API**

```
curl -X POST \  
 --header "Content-Type: application/json" \  
--header "Accept: application/json" \  
 --header "Authorization: Bearer YOUR_API_KEY" \  
--data '{  
 "network_id": "7c3c05f4-7d53-4edb-9224-371c6d659cd4",  
 "region_code": "ashburn-va",  
 "name": "WG_net01_VA_interface01"  
 }' \  
 https://api.telnyx.com/v2/wireguard_interface
```

**Example Response**

```
{  
"data": {  
"status": "provisioning",  
"network_id": "7c3c05f4-7d53-4edb-9224-371c6d659cd4",  
"id": "9122b687-30aa-47a6-8f64-2b8681476ec2",  
"updated_at": "2022-06-13T09:50:54.117345Z",  
"created_at": "2022-06-13T09:50:53.627044Z",  
"region_code": "ashburn-va",  
"public_key": "4sHgXncx9tgswHmQvxq8B8O8iJ1AuJjLNmT9Qfs/VV0=",  
"name": "WG_net01_VA_interface01",  
"region": {  
"code": "ashburn-va",  
"name": "Ashburn",  
"record_type": "region"  
 },  
"record_type": "wireguard_interface",  
"endpoint": "64.16.243.3:5034",  
"server_ip_address": "172.27.1.17/29"  
 }  
}
```

> **Note:** The 'server\_ip\_address' is the private ip of the Cloud VPN interface and will be used later to test the connectivity between the added peer and the interface

## **Step 4: Create a Cloud VPN Peer**

Create a Cloud VPN Peer associated with the Cloud VPN Interface. This adds a peer to the server configuration created on the Cloud VPN server on the Telnyx network. Input your `public_key` generated on the Digital Ocean Ubuntu server in step 2

​**Create a Cloud VPN Peer with the Telnyx API**

```
curl -X POST \  
 --header "Content-Type: application/json" \  
--header "Accept: application/json" \  
 --header "Authorization: Bearer YOUR_API_KEY" \  
--data '{  
 "wireguard_interface_id": "9122b687-30aa-47a6-8f64-2b8681476ec2",  
 "name": "ubuntu_peer01"  
 “public_key”: "ToEvvyKC/zI+Q3AipAUs7Zl3CvEkOzMXNtf4YTf8UH4="  
 }' \  
 https://api.telnyx.com/v2/wireguard_peers
```

**Example Response**

```
{  
"data": {  
"updated_at": "2022-06-13T09:56:23.601577Z",  
"id": "e4916505-a638-4b1d-b076-3142e7f1516a",  
"wireguard_interface_id": "9122b687-30aa-47a6-8f64-2b8681476ec2",  
"created_at": "2022-06-13T09:56:23.601577Z",  
"public_key": "ToEvvyKC/zI+Q3AipAUs7Zl3CvEkOzMXNtf4YTf8UH4=",  
"name": "ubuntu_peer01",  
"last_seen": null,  
"record_type": "wireguard_peer"  
 }  
}
```

## **Step 5: Retrieve your configuration for the Cloud VPN Peer**

You will now need to save the peer configuration file in the `/etc/wireguard` directory on the Digital Ocean Ubuntu server. The peer configuration can be retrieved via API. You will need to add the private key to the configuration file. Give the configuration a meaningful name e.g. `wg0.conf` or `wg_ubuntu.conf`. It must have `.conf` as the file extension.

​**Cloud VPN Peer Configuration Template**

```
[Interface]  
Address = <server_private_ip_address>  
PrivateKey = <contents-of-client-privatekey>  
  
[Peer]PublicKey = <contents-of-server-publickey>Endpoint = <server-public-ip>:<port>AllowedIPs = <ip/cidr>
```

**Retrieve Configuration for the Cloud VPN Peer with the Telnyx API**  
​

```
curl -X GET \  
 --header "Content-Type: application/json" \  
--header "Accept: application/json" \  
 --header "Authorization: Bearer YOUR_API_KEY" \  
https://api.telnyx.com/v2/19783d68-c893-4954-bfbf-815d9ab9b0f6/Config
```

​**Example Response**

```
{  
[Interface]  
PrivateKey = <! INSERT PEER PRIVATE KEY HERE !>  
Address = 172.27.1.18/32  
  
[Peer]PublicKey = ToEvvyKC/zI+Q3AipAUs7Zl3CvEkOzMXNtf4YTf8UH4=AllowedIPs = 172.27.1.16/29Endpoint = 64.16.243.3:5034PersistentKeepalive = 25}
```

## **Step 6: Bring up WireGuard Interface on your peer**

In this step you will bring up the WireGuard VPN interface on the peer. The command must contain the name of the peer configuration file you created on the Digital Ocean Ubuntu server in Step 5, without the file extension, `.conf`.

​**Bring up the Wireguard Interface on your peer**

Use the following command

```
sudo wg-quick up wg0
```

​**Example Response**

```
root@ubuntu-s-1vcpu-1gb-lon1-01:~# wg-quick up wg0  
[#] ip link add wg0 type wireguard  
[#] wg setconf wg0 /dev/fd/63  
[#] ip -4 address add 172.27.255.60/29 dev wg0  
[#] ip link set mtu 1420 up dev wg0
```

## **Step 7: Test Connection**

Test that a connection was established between your peer and the Telnyx network.  
Use the following command to show the current peer configuration

```
sudo wg show
```

**Example Response**

```
root@ubuntu-s-1vcpu-1gb-lon1-01:~# wg show  
interface: wg0  
public key: ToEvvyKC/zI+Q3AipAUs7Zl3CvEkOzMXNtf4YTf8UH4=  
private key: (hidden)  
listening port: 45111  
peer: qF4EqlZq+5JL2IKYY8ij49daYyfKVhevJrcDxdqC8GU= endpoint: 203.0.113.0:51871 allowed ips: 198.51.100.0/29 latest handshake: 2 minutes, 12 seconds ago transfer: 10.20 KiB received, 5.05 KiB sent
```

**Test Connection**

```
bash$ ping <server_ip_address>
```

> **Note:** The 'server\_ip\_address' is the private ip of the Cloud VPN interface and can be found in the response of the Cloud VPN Interface create endpoint in Step 3

​**Example Response**

```
root@ubuntu-s-1vcpu-1gb-lon1-01:~# ping 172.27.1.17  
PING 172.27.1.17 (172.27.1.17) 56(84) bytes of data.  
64 bytes from 172.27.1.17: icmp_seq=1 ttl=64 time=145 ms  
64 bytes from 172.27.1.17: icmp_seq=2 ttl=64 time=144 ms  
64 bytes from 172.27.1.17: icmp_seq=3 ttl=64 time=144 ms  
64 bytes from 172.27.1.17: icmp_seq=4 ttl=64 time=144 ms  
64 bytes from 172.27.1.17: icmp_seq=5 ttl=64 time=144 ms  
64 bytes from 172.27.1.17: icmp_seq=6 ttl=64 time=144 ms
```

## **Next Steps**

Congratulations! You have successfully connected your Digital Ocean Ubuntu Server to a Cloud VPN server running in the Telnyx network.  
​

By repeating the steps in this tutorial for multiple peers, you'll be able to link apps, devices and services together across the Telnyx backbone for low latency, secure communications across the globe.  
​

If you have any further questions or would like to see more tutorials, feel free to reach out to our support team or our external Slack channel for help!

---

Related Articles

[Telnyx Networking on AWS Lightsail](https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail)[Telnyx Networking on AWS VPC](https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc)[Telnyx Networking on Azure Linux VMs](https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms)[Telnyx Networking on Android/iOS](https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios)[Telnyx Networking on Oracle VMs](https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms)

Did this answer your question?

😞😐😃

Table of contents
