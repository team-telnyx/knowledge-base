---
source_url: https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms
scraped: 2026-06-11
---

Telnyx Networking on Azure Linux VMs | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx Networking on Azure Linux VMs

Setup and deploy the Telnyx Networking product on Azure Linux Virtual Machines

Written by Telnyx Engineering

December 11, 2023

Table of contents

# Azure Linux VMs and the Telnyx Network

## Step 1: Telnyx Configuration with Azure Linux VMs

Reference the introduction to Telnyx Networking section located here: [Telnyx Configuration](https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing)

Copy and take note of the Peer Configuration file along with the private key that you got assigned from the above tutorial, it should look like the following:

[![Peer Configuration file. ](https://downloads.intercomcdn.com/i/o/779406840/c9bd1538ae6d5dbea52f740d/peer_conf.png?expires=1781168400&signature=ecfba5f5e81aefbd874e28146be277f7e4e95964e4a92a11163a86769c6db927&req=cycuEsl4lYVfFb4f3HP0gKiuyJL9hNmCzZHm7hb8TAnafDlmK7zZ1YosGpYs%0AVPt1R98YeoA%2FNvzeKQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779406840/c9bd1538ae6d5dbea52f740d/peer_conf.png?expires=1781168400&signature=ecfba5f5e81aefbd874e28146be277f7e4e95964e4a92a11163a86769c6db927&req=cycuEsl4lYVfFb4f3HP0gKiuyJL9hNmCzZHm7hb8TAnafDlmK7zZ1YosGpYs%0AVPt1R98YeoA%2FNvzeKQ%3D%3D%0A)

## **Step 2: Create an Azure Linux VM and SSH in**

Head over to the [Azure Portal](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Compute%2FVirtualMachines) to create a Linux VM of your choosing. Edge router runs on WireGuard in the background which makes it easily compatible with most Linux distributions offered by the Azure Marketplace.

​[SSH](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/ssh-from-windows) into your Azure VM instance.

## **Step 3: Setting up WireGuard for Telnyx**

While SSH'ed into your VM, install WireGuard on your machine.  
​

```
sudo apt update$ sudo apt install wireguard
```

> Note: You can utilize [WireGuard Manager](https://github.com/complexorganizations/wireguard-manager) to make the setup process for your WireGuard installation more straightforward with step by step guides to setting up your parameters, but it is not necessary

After installation, we should now have the WireGuard folder that is located at `/etc/wireguard`, where we need to configure the `wg0.conf` file.

Let's open the conf file:

```
sudo vi /etc/wireguard/wg0.conf
```

and copy/paste the information that we got from Step 1

[![Peer Configuration file](https://downloads.intercomcdn.com/i/o/779581774/06035971cb76591d0df0b253/peer_conf_term.png?expires=1781168400&signature=6a825ee729264d1b1054b2bc4eed35598b7c5b81570c499877bf4a2355b7d999&req=cycuE8F%2FmoZbFb4f3HP0gAXXxnmz3LqOo%2F%2FAhfZ24eZmo2sZ8aeYUccBXBXJ%0AMt2zUPCKzkQEZUkFhA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779581774/06035971cb76591d0df0b253/peer_conf_term.png?expires=1781168400&signature=6a825ee729264d1b1054b2bc4eed35598b7c5b81570c499877bf4a2355b7d999&req=cycuE8F%2FmoZbFb4f3HP0gAXXxnmz3LqOo%2F%2FAhfZ24eZmo2sZ8aeYUccBXBXJ%0AMt2zUPCKzkQEZUkFhA%3D%3D%0A)

Save and quit:

```
:wq
```

## **Step 4: Test**

We can now run the VPN by simply inputting:

```
sudo wg-quick up wg0
```

[![Peer Configuration file.](https://downloads.intercomcdn.com/i/o/779584950/1f90652e81f2c48950263bfa/vpn_start.png?expires=1781168400&signature=7ffd6d0361313677e1674c89d91bdc66bac88ce849b94e0d88c25a48f664975d&req=cycuE8F6lIRfFb4f3HP0gIIl%2FBDWc3exRJGDCXXIXAU0R3fMxmZWQ0p%2BBxjA%0AjUKx0pOY1BDsGPrq2A%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779584950/1f90652e81f2c48950263bfa/vpn_start.png?expires=1781168400&signature=7ffd6d0361313677e1674c89d91bdc66bac88ce849b94e0d88c25a48f664975d&req=cycuE8F6lIRfFb4f3HP0gIIl%2FBDWc3exRJGDCXXIXAU0R3fMxmZWQ0p%2BBxjA%0AjUKx0pOY1BDsGPrq2A%3D%3D%0A)

We can test to see if it's working by checking the [portal](https://portal.telnyx.com/#/app/networking/cloudvpn/) and seeing the last seen status change:

[![Mission control portal. ](https://downloads.intercomcdn.com/i/o/779537516/f77f922eae46183f2d7d6951/test.png?expires=1781168400&signature=520dac66e7625f5955036be1920fe5ce8791b63d4cf8f5349df61cc33f9905d9&req=cycuE8p5mIBZFb4f3HP0gJe%2Fp%2F5J%2Fq4VJpLqLwvik1g%2Fjd89xFFh7tIDfttB%0AxGNNvLY9mYhj5pXzoA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779537516/f77f922eae46183f2d7d6951/test.png?expires=1781168400&signature=520dac66e7625f5955036be1920fe5ce8791b63d4cf8f5349df61cc33f9905d9&req=cycuE8p5mIBZFb4f3HP0gJe%2Fp%2F5J%2Fq4VJpLqLwvik1g%2Fjd89xFFh7tIDfttB%0AxGNNvLY9mYhj5pXzoA%3D%3D%0A)

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

Congratulations! You have successfully connected an Azure Linux VM instance to the Telnyx Edge Routing Network to the configured IP in your portal.

If you have any further questions or would like to see more tutorials, feel free to reach out to our support team or our external Slack channel for help!

---

Related Articles

[Telnyx Networking on AWS Lightsail](https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail)[Telnyx Networking on Ubuntu](https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu)[Telnyx Networking on AWS VPC](https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc)[Telnyx Networking on Android/iOS](https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios)[Telnyx Networking on Oracle VMs](https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms)

Did this answer your question?

😞😐😃

Table of contents
