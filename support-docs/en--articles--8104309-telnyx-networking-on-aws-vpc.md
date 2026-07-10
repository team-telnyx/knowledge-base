---
source_url: https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc
scraped: 2026-07-08
content_hash: 2fc6e99c6b5cc4736be40b1b4f492f1fbc086cb2818c04484729184ef5d616d0
---

Telnyx Networking on AWS VPC | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx Networking on AWS VPC

A step-by-step process to deploy a Virtual Private Server (VPS) on Amazon AWS and configure Telnyx Edge Routing to it.

Written by Telnyx Engineering

December 11, 2023

Table of contents

# AWS VPC and Telnyx Networking

An overview of what we will be going over:

* Installing any necessary packages/software
* Generating WireGuard private and public keys
* Modifying the AWS environment to allow WireGuard traffic
* Setting up the WireGuard interface with Telnyx- Activating the VPN

## **Step 1: Telnyx Configuration for AWS VPC**

Reference the configuration section [located here](https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing).

Copy and take note of the Peer Configuration file along with the private key that you got assigned from the above tutorial, it should look like the following:

![Peer Configuration file. ](_images/dc7326bcccc84de3.png)

## Step 2: Install WireGuard

Telnyx Edge Routing supports any distribution that supports WireGuard; as such a good place to start and reference is the [WireGuard installation](https://www.wireguard.com/install/).  
​  
Referencing the Ubuntu installation, simply run

```
apt install wireguard-tools
```

WireGuard utilizes UDP port 51280 as the listening port for the interface. If you are going to route traffic through the EC2 instance, you'll need to turn off the source/destination check for the VPN instance. You can easily accomplish this with the AWS CLI by running:

```
aws ec2 modify-instance-attribute --no-source-dest-check --instance-id <instance-id>
```

We are ready to configure our instance!

## **Step 3: Configuring Telnyx with WireGuard**

```
We will first need to create a configuration file in the /etc/wireguar` folder called wg0.conf. This is where we will place the configuration instructions that we generated from Step 1:  
[Interface]  
PrivateKey = <private key for this machine>  
Address = <IP address for WireGuard interface>  
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE  
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE  
ListenPort = 51280  
[Peer]PublicKey = <public key for peer machine>AllowedIPs = <IP address for peer WireGuard interface>, <additional CIDRs>PersistentKeepalive = 1
```

Replace the above with your specific configuration

> Note: - If you have chosen an interface name different from wg0, please ensure that you modify the PostUp and PostDown lines accordingly. It's important to note that this configuration utilizes Network Address Translation (NAT) to present the VPN traffic as if it originates from the VPN instance within the VPC. This eliminates the need to disable source/destination checks or update routing tables.

> Note: - Considering that my client devices are situated behind a NAT, I have included the PersistentKeepalive setting. While it may not be necessary for everyone, I anticipate that many individuals will find it beneficial.

> Note: - Regarding the notation <additional CIDRs> mentioned earlier, if you desire other IP addresses from the peer's network to route through this connection, specify those addresses/networks here. This becomes particularly significant in the "client" side configuration, where you consolidate all traffic for a VPC (or a group of VPCs) through a single WireGuard node.

## **Step 4: Test**

We can test to see if it's working by checking the [portal](https://portal.telnyx.com/#/app/networking/cloudvpn/) and seeing the last seen status change:

![Mission control portal. ](_images/a4693ab904e2e821.png)

or you can curl/trace into your server to confirm the Global IP that is configured to it.

Example Response:

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
8 packets transmitted, 8 packets received, 0.0% packet loss  
round-trip min/avg/max/stddev = 183.040/183.495/184.512/0.471 ms
```

**Next Steps**

Congratulations! You have succesfully connected an AWS VPS instance to the Telnyx Edge Routing Network to the configured IP in your portal.

If you have any further questions or would like to see more tutorials, feel free to reach out to our support team or our external Slack channel for help!

---

Related Articles

[Telnyx Networking on AWS Lightsail](https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail)[Telnyx Networking on Ubuntu](https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu)[Telnyx Networking on Azure Linux VMs](https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms)[Telnyx Networking on Android/iOS](https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios)[Telnyx Networking on Oracle VMs](https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms)

Did this answer your question?

😞😐😃

Table of contents
