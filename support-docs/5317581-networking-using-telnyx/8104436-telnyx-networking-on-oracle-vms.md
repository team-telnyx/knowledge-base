---
source_url: https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms
scraped: 2026-06-11
---

Telnyx Networking on Oracle VMs | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx Networking on Oracle VMs

Guide to set up Telnyx Edge Routing on Oracle VMs using WireGuard for secure connectivity.

Written by Telnyx Engineering

December 13, 2023

Table of contents

# Step 1: Telnyx Configuration with Oracle VMs

Reference the introduction to Telnyx Networking section located here: [Telnyx Configuration](https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing)

Copy and take note of the Peer Configuration file along with the private key that you got assigned from the above tutorial, it should look like the following:

[![Peer Configuration file interface. ](https://downloads.intercomcdn.com/i/o/779406840/c9bd1538ae6d5dbea52f740d/peer_conf.png?expires=1781168400&signature=ecfba5f5e81aefbd874e28146be277f7e4e95964e4a92a11163a86769c6db927&req=cycuEsl4lYVfFb4f3HP0gKiuyJL9hNmCzZHm7hb8TAnafDlmK7zZ1YosGpYs%0AVPt1R98YeoA%2FNvzeKQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779406840/c9bd1538ae6d5dbea52f740d/peer_conf.png?expires=1781168400&signature=ecfba5f5e81aefbd874e28146be277f7e4e95964e4a92a11163a86769c6db927&req=cycuEsl4lYVfFb4f3HP0gKiuyJL9hNmCzZHm7hb8TAnafDlmK7zZ1YosGpYs%0AVPt1R98YeoA%2FNvzeKQ%3D%3D%0A)

## **Step 2: Create your Oracle Cloud Compute Instance**

You should now go through and create your own Oracle Cloud VM Instance. A good overview and guide on how to do so can be found here written by n00.

It will guide you through the setup process as well as the installation of WireGuard which is what we will use to configure the Telnyx networking instance.

## **Step 3: Configuring WireGuard with Telnyx**

We will first need to create a configuration file in the `/etc/wireguard` folder called `wg0.conf`. This is where we will place the configuration instructions that we generated from Step 1.

```
[Interface]  
PrivateKey = private key for this machine  
Address = IP address for WireGuard interface  
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE  
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE  
ListenPort = 51280  
  
[Peer]  
PublicKey = public key for peer machine  
AllowedIPs = IP address for peer WireGuard interface, additional CIDRs  
PersistentKeepalive = 1
```

**Notes on Step 3**

If you have chosen an interface name different from wg0, please ensure that you modify the PostUp and PostDown lines accordingly. It's important to note that this configuration utilizes Network Address Translation (NAT) to present the VPN traffic as if it originates from the VPN instance within the VPC. This eliminates the need to disable source/destination checks or update routing tables.

Considering that my client devices are situated behind a NAT, I have included the PersistentKeepalive setting. While it may not be necessary for everyone, I anticipate that many individuals will find it beneficial.

Regarding the notation **additional CIDRs** mentioned earlier, if you desire other IP addresses from the peer's network to route through this connection, specify those addresses/networks here. This becomes particularly significant in the "client" side configuration, where you consolidate all traffic for a VPC (or a group of VPCs) through a single WireGuard node.

## **Step 4:**

**Additional Oracle NAT and Routing Configuration**

If you've tried setting up WireGuard with Oracle Cloud before, you'll probably notice after setup that your WireGuard instance will not function due to server blocking on their side. This is due to Oracle specific configuration issues in relation to how they set up their NAT settings. To get around this and be able to connect, we will need to create and add-on two scripts. We can do so with the following steps:

## Step 4.1

**We need to update our `wg0.conf` file with the following:**

```
PostUp = /etc/wireguard/helper/add-nat-routing.sh  
PostDown = /etc/wireguard/helper/remove-nat-routing.sh
```

## Step 4.2

**We will create the following two above scripts in the `/etc/wireguard/helper/` directory with execute permissions:**

## Script 1

- add-nat-routing.sh

```
#!/bin/bash  
IPT="/sbin/iptables"  
IPT6="/sbin/ip6tables"  
  
IN_FACE="ens3" # NIC connected to the internet  
WG_FACE="wg0" # WG NIC  
SUB_NET="10.66.66.0/24" # WG IPv4 sub/net aka CIDR  
WG_PORT="59075" # WG udp port  
SUB_NET_6="fd42:42:42::/64" # WG IPv6 sub/net  
  
## IPv4 ##  
$IPT -t nat -I POSTROUTING 1 -s $SUB_NET -o $IN_FACE -j MASQUERADE  
$IPT -I INPUT 1 -i $WG_FACE -j ACCEPT  
$IPT -I FORWARD 1 -i $IN_FACE -o $WG_FACE -j ACCEPT  
$IPT -I FORWARD 1 -i $WG_FACE -o $IN_FACE -j ACCEPT  
$IPT -I INPUT 1 -i $IN_FACE -p udp --dport $WG_PORT -j ACCEPT  
  
## IPv6 (Uncomment) ##  
$IPT6 -t nat -I POSTROUTING 1 -s $SUB_NET_6 -o $IN_FACE -j MASQUERADE  
$IPT6 -I INPUT 1 -i $WG_FACE -j ACCEPT  
$IPT6 -I FORWARD 1 -i $IN_FACE -o $WG_FACE -j ACCEPT  
$IPT6 -I FORWARD 1 -i $WG_FACE -o $IN_FACE -j ACCEPT
```

## Script 2

- remove-nat-routing.sh

```
#!/bin/bash  
IPT="/sbin/iptables"  
IPT6="/sbin/ip6tables"  
  
IN_FACE="ens3" # NIC connected to the internet  
WG_FACE="wg0" # WG NIC  
SUB_NET="10.66.66.0/24" # WG IPv4 sub/net aka CIDR  
WG_PORT="59075" # WG udp port  
SUB_NET_6="fd42:42:42::/64" # WG IPv6 sub/net  
  
# IPv4 rules #  
$IPT -t nat -D POSTROUTING -s $SUB_NET -o $IN_FACE -j MASQUERADE  
$IPT -D INPUT -i $WG_FACE -j ACCEPT  
$IPT -D FORWARD -i $IN_FACE -o $WG_FACE -j ACCEPT  
$IPT -D FORWARD -i $WG_FACE -o $IN_FACE -j ACCEPT  
$IPT -D INPUT -i $IN_FACE -p udp --dport $WG_PORT -j ACCEPT  
  
# IPv6 rules (uncomment) #$IPT6 -t nat -D POSTROUTING -s $SUB_NET_6 -o $IN_FACE -j MASQUERADE  
$IPT6 -D INPUT -i $WG_FACE -j ACCEPT  
$IPT6 -D FORWARD -i $IN_FACE -o $WG_FACE -j ACCEPT  
$IPT6 -D FORWARD -i $WG_FACE -o $IN_FACE -j ACCEPT
```

The first script will ensure that the traffic running from the VPN is correctly routed through the network on the Oracle Cloud servers while the second script correctly disables the routing configuration when the service is stopped.

A more detailed writeup of the above can be [found here written elegantly by Vadim Smirnov.](https://www.ntkernel.com/setting-up-wireguard-on-oracle-cloud-overcoming-nat-and-routing-challenges/)

## **Step 5: Test**

We can test to see if it's working by checking the [portal](https://portal.telnyx.com/#/app/networking/cloudvpn/) and seeing the last seen status change:

[![Mission control portal properties section.](https://downloads.intercomcdn.com/i/o/779537516/f77f922eae46183f2d7d6951/test.png?expires=1781168400&signature=520dac66e7625f5955036be1920fe5ce8791b63d4cf8f5349df61cc33f9905d9&req=cycuE8p5mIBZFb4f3HP0gJe%2Fp%2F5J%2Fq4VJpLqLwvik1g%2Fjd89xFFh7tIDfttB%0AxGNNvLY9mYhj5pXzoA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779537516/f77f922eae46183f2d7d6951/test.png?expires=1781168400&signature=520dac66e7625f5955036be1920fe5ce8791b63d4cf8f5349df61cc33f9905d9&req=cycuE8p5mIBZFb4f3HP0gJe%2Fp%2F5J%2Fq4VJpLqLwvik1g%2Fjd89xFFh7tIDfttB%0AxGNNvLY9mYhj5pXzoA%3D%3D%0A)

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

Congratulations! You have successfully connected an Oracle Cloud VM instance to the Telnyx Edge Routing Network to the configured IP in your portal.

If you have any further questions or would like to see more tutorials, feel free to reach out to our support team or our external Slack channel for help!

---

Related Articles

[Telnyx Networking on AWS Lightsail](https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail)[Telnyx Networking on Ubuntu](https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu)[Telnyx Networking on AWS VPC](https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc)[Telnyx Networking on Azure Linux VMs](https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms)[Telnyx Networking on Android/iOS](https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios)

Did this answer your question?

😞😐😃

Table of contents
