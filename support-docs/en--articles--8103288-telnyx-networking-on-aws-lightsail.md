---
source_url: https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail
scraped: 2026-06-11
---

Telnyx Networking on AWS Lightsail | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx Networking on AWS Lightsail

This guide provides a step-by-step process to deploy a Lightsail Virtual Private Server (VPS) on Amazon AWS and configure Telnyx to it

Written by Telnyx Engineering

December 11, 2023

Table of contents

# AWS Lightsail and the Telnyx Network

Here's an overview of what we will be going over:

* Deploying a Ubuntu 20.04 Lightsail VPS (or your preffered distribution)
* Installing WireGuard on the VPS
* Configuring WireGuard with Telnyx on the VPS

## Step 1: Configuring for Telnyx

Reference the introduction to Telnyx Networking section located here: [Telnyx Configuration](https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing)

Copy and take note of the Peer Configuration file along with the private key that you got assigned from the above tutorial, it should look like the following:

[![Peer Configuration file. ](https://downloads.intercomcdn.com/i/o/779406840/c9bd1538ae6d5dbea52f740d/peer_conf.png?expires=1781168400&signature=ecfba5f5e81aefbd874e28146be277f7e4e95964e4a92a11163a86769c6db927&req=cycuEsl4lYVfFb4f3HP0gKiuyJL9hNmCzZHm7hb8TAnafDlmK7zZ1YosGpYs%0AVPt1R98YeoA%2FNvzeKQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779406840/c9bd1538ae6d5dbea52f740d/peer_conf.png?expires=1781168400&signature=ecfba5f5e81aefbd874e28146be277f7e4e95964e4a92a11163a86769c6db927&req=cycuEsl4lYVfFb4f3HP0gKiuyJL9hNmCzZHm7hb8TAnafDlmK7zZ1YosGpYs%0AVPt1R98YeoA%2FNvzeKQ%3D%3D%0A)

## Step 2: Deploy an Amazon Lightsail VPS

Log in to Amazon Lightsail and click on "Create instance."

[![Amazon Lightsail. ](https://downloads.intercomcdn.com/i/o/779527855/9af1f615fcc0b3f41b2a5436/aws1.png?expires=1781168400&signature=ab93f7682e5cad7b58b52776e52e227a809f540235f359676eb7a65c3f87123b&req=cycuE8t5lYRaFb4f3HP0gOvHK8I9NqSWLxI3sMDvpNvjEOrCNfOiaCyGYZFv%0A9dCqdQM3lcjEf6DTWQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779527855/9af1f615fcc0b3f41b2a5436/aws1.png?expires=1781168400&signature=ab93f7682e5cad7b58b52776e52e227a809f540235f359676eb7a65c3f87123b&req=cycuE8t5lYRaFb4f3HP0gOvHK8I9NqSWLxI3sMDvpNvjEOrCNfOiaCyGYZFv%0A9dCqdQM3lcjEf6DTWQ%3D%3D%0A)

Choose a location by clicking on "Change AWS Region and Availability Zone."

[![Amazon Lightsail for location settings. ](https://downloads.intercomcdn.com/i/o/779527942/7d5442bc30d842100f86480b/aws2.png?expires=1781168400&signature=dc88f945b13c218a0b5f8d2655decf111728a66acd631f25df7e434d1a6fea67&req=cycuE8t5lIVdFb4f3HP0gIrBl15p1uK1mX9i3dIK6OEqPgz7bOEIbCcEDQzR%0ACuLf51nZKQCCwhAp1Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779527942/7d5442bc30d842100f86480b/aws2.png?expires=1781168400&signature=dc88f945b13c218a0b5f8d2655decf111728a66acd631f25df7e434d1a6fea67&req=cycuE8t5lIVdFb4f3HP0gIrBl15p1uK1mX9i3dIK6OEqPgz7bOEIbCcEDQzR%0ACuLf51nZKQCCwhAp1Q%3D%3D%0A)

Select "Linux/Unix" and choose "Ubuntu 20.04 LTS" as the operating system.

Give the instance a name and click "Create instance."

Take note of the public IP address of the instance as you will need it later for SSH connection and configuring the WireGuard VPN client.

Note: Telnyx Networking and Edge Routing works on any distro that supports WireGuard; as such a good place to start and reference is the [WireGuard installation site](<https://www.wireguard.com/install/>).

## **Step 3: Configuring Networking**

Now that your instance is running, you need to make some changes to the firewall rules to allow WireGuard clients to connect to the server.  
Click on the instance name and go to the "Networking" section.

[![Amazon Lightsail for configuring networking. ](https://downloads.intercomcdn.com/i/o/779529288/071ae5601ae335a26c0460ba/aws4.png?expires=1781168400&signature=67acb07798cabafb9e2939a7b147df102928ba2083e052fdc55958ef095bf6c9&req=cycuE8t3n4lXFb4f3HP0gD6xeFY4gCUzT2NQjgrIhOtFZG%2FcHES3XGujJ%2F%2BK%0A65o0FAcsd6jkTCS08g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779529288/071ae5601ae335a26c0460ba/aws4.png?expires=1781168400&signature=67acb07798cabafb9e2939a7b147df102928ba2083e052fdc55958ef095bf6c9&req=cycuE8t3n4lXFb4f3HP0gD6xeFY4gCUzT2NQjgrIhOtFZG%2FcHES3XGujJ%2F%2BK%0A65o0FAcsd6jkTCS08g%3D%3D%0A)

Delete the HTTP rule (since it's not a web server) by clicking on the recycle bin icon next to the HTTP rule.  
Click

* "Add rule,"
* select "Custom,"
* choose "UDP,"
* assign port 51820
* click "Create."

This port will be used by the WireGuard service to connect to clients.

> Note: Disabling IPv6 is optional and depends on your usage preferences.

## **Step 4: Connecting to the VPS Instance with SSH**

Now it's time to establish an SSH connection to your VPS instance.

Navigate to the "Account" section, then click on "SSH keys.

[![Amazon Lightsail for Account section. ](https://downloads.intercomcdn.com/i/o/779530709/c37221546e38f49ba037d9e1/aws5.png?expires=1781168400&signature=6470c44326ead77dd030ed5d88d65c271c971b6b327db41cf49ead859e318656&req=cycuE8p%2BmoFWFb4f3HP0gKWzMX1Re2llA2vv%2Fs0cvnmGQeTkBzE3Pjh8zxrS%0AE1eCHNCyMw%2FUmFL%2FGg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779530709/c37221546e38f49ba037d9e1/aws5.png?expires=1781168400&signature=6470c44326ead77dd030ed5d88d65c271c971b6b327db41cf49ead859e318656&req=cycuE8p%2BmoFWFb4f3HP0gKWzMX1Re2llA2vv%2Fs0cvnmGQeTkBzE3Pjh8zxrS%0AE1eCHNCyMw%2FUmFL%2FGg%3D%3D%0A)

Download the key assigned to your instance and save it on your computer.

Open a Terminal session (Unix-like operating systems) or Putty (Windows).

Make the key readable only by the current user:

```
chmod 600 ~/Desktop/vpn.cer
```

Connect to the VPS instance using the public IP address and the certificate path:

```
ssh -i ~/Desktop/vpn.cer ubuntu@[PUBLIC_IP_ADDRESS]
```

## **Step 5: Enabling Port Forwarding**

After connecting to the server, the next step is to enable port forwarding so that client traffic can access the internet.

Enable port forwarding by creating a file called `"10-wireguard.conf"` in the `"/etc/sysctl.d"` directory:

```
sudo vim /etc/sysctl.d/10-wireguard.conf
```

Add the following contents to the file:

```
net.ipv4.ip_forward=1
```

To enable port forwarding immediately, run the command:   
​

```
sudo sysctl -p /etc/sysctl.d/10-wireguard.conf
```

## **Step 6: Installing WireGuard and Generating Keys**

Install WireGuard by running:

```
sudo apt update && sudo apt install wireguard -y
```

Generate the server and client keys using the following commands:

```
cd /etc/wireguard/  
wg genkey | tee server.key | wg pubkey > server.pub  
wg genkey | tee client.key | wg pubkey > client.pub
```

A list of files should now be created

```
/etc/wireguard# ls -ltotal 16  
-rw------- 1 root root 45 Jun 29 10:32 client.key  
-rw------- 1 root root 45 Jun 29 10:32 client.pub  
-rw------- 1 root root 45 Jun 29 10:32 server.key  
-rw------- 1 root root 45 Jun 29 10:32 server.pub
```

> Make sure to keep track of these files as they will be used if you want to connect multiple peers or manage this server remotely from a different WireGuard Client

## **Step 7: Creating the WireGuard Server Configuration**

We now need to create the config file for the WireGuard service before we start it  
​

```
sudo vim wg0.conf
```

We can now copy/paste our configuration files we got from Step 1 inside here, from the Telnyx portal:

[![Wireguard config files. ](https://downloads.intercomcdn.com/i/o/779535799/2fdfa94d1fdb55aaa303f9f3/peer_conf.png?expires=1781168400&signature=f907f9258489c67e25063d2e8a19d6ddb2e6d1386a9bb9b33d104cb02acdf7c8&req=cycuE8p7mohWFb4f3HP0gMa2alYgIgm6ZVI1WAdydUzEPinwI%2B5IBn97guOe%0A4z%2F%2FPhHcl7lYkQIZIQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779535799/2fdfa94d1fdb55aaa303f9f3/peer_conf.png?expires=1781168400&signature=f907f9258489c67e25063d2e8a19d6ddb2e6d1386a9bb9b33d104cb02acdf7c8&req=cycuE8p7mohWFb4f3HP0gMa2alYgIgm6ZVI1WAdydUzEPinwI%2B5IBn97guOe%0A4z%2F%2FPhHcl7lYkQIZIQ%3D%3D%0A)

To enable the service when the server boots, simply run:  
​

```
sudo systemctl enable wg-quick@wg0
```

To start the service now run:

```
sudo systemctl start wg-quick@wg0
```

## **Step 8: Test**

We can test to see if it's working by checking the [portal](https://portal.telnyx.com/#/app/networking/cloudvpn/) and seeing the last seen status change:

[![Mission control portal. ](https://downloads.intercomcdn.com/i/o/779537516/f77f922eae46183f2d7d6951/test.png?expires=1781168400&signature=520dac66e7625f5955036be1920fe5ce8791b63d4cf8f5349df61cc33f9905d9&req=cycuE8p5mIBZFb4f3HP0gJe%2Fp%2F5J%2Fq4VJpLqLwvik1g%2Fjd89xFFh7tIDfttB%0AxGNNvLY9mYhj5pXzoA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779537516/f77f922eae46183f2d7d6951/test.png?expires=1781168400&signature=520dac66e7625f5955036be1920fe5ce8791b63d4cf8f5349df61cc33f9905d9&req=cycuE8p5mIBZFb4f3HP0gJe%2Fp%2F5J%2Fq4VJpLqLwvik1g%2Fjd89xFFh7tIDfttB%0AxGNNvLY9mYhj5pXzoA%3D%3D%0A)

or you can curl/trace into your server to confirm the Global IP that is configured to it.

Example Response:

​

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

## **Next Steps**

Congratulations! You have successfully connected an AWS Lightsail VPS instance to the Telnyx Edge Routing Network to the configured IP in your portal.

If you have any further questions or would like to see more tutorials, feel free to reach out to our support team or our external Slack channel for help!  
​

---

Related Articles

[Telnyx Networking on Ubuntu](https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu)[Telnyx Networking on AWS VPC](https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc)[Telnyx Networking on Azure Linux VMs](https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms)[Telnyx Networking on Android/iOS](https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios)[Telnyx Networking on Oracle VMs](https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms)

Did this answer your question?

😞😐😃

Table of contents
