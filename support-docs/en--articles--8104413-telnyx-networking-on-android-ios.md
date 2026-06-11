---
source_url: https://support.telnyx.com/en/articles/8104413-telnyx-networking-on-android-ios
scraped: 2026-06-11
---

Telnyx Networking on Android/iOS | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx Networking on Android/iOS

Global Edge Router setup using the WireGuard App for the iOS and Android mobile platforms

Written by Telnyx Engineering

April 30, 2026

Table of contents

WireGuard has native client installations for both [Android](https://play.google.com/store/apps/details?id=com.wireguard.android) and [iOS](https://apps.apple.com/us/app/wireguard/id1441195209?ls=1) that we can use to test or monitor our Telnyx Edge instances.

# Android/iOS and the Telnyx Network

This is probably the easiest way to test out the service with a simple and effortless 3 steps to follow.

## Step 1: Telnyx Configuration for Android/iOS

Reference the introduction to Telnyx Networking section located here: [Telnyx Configuration](https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing)

Copy and take note of the Peer Configuration file along with the private key that you got assigned from the above tutorial, it should look like the following:

[![Peer Configuration file. ](https://downloads.intercomcdn.com/i/o/779406840/c9bd1538ae6d5dbea52f740d/peer_conf.png?expires=1781168400&signature=ecfba5f5e81aefbd874e28146be277f7e4e95964e4a92a11163a86769c6db927&req=cycuEsl4lYVfFb4f3HP0gKiuyJL9hNmCzZHm7hb8TAnafDlmK7zZ1YosGpYs%0AVPt1R98YeoA%2FNvzeKQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779406840/c9bd1538ae6d5dbea52f740d/peer_conf.png?expires=1781168400&signature=ecfba5f5e81aefbd874e28146be277f7e4e95964e4a92a11163a86769c6db927&req=cycuEsl4lYVfFb4f3HP0gKiuyJL9hNmCzZHm7hb8TAnafDlmK7zZ1YosGpYs%0AVPt1R98YeoA%2FNvzeKQ%3D%3D%0A)

## **Step 2: WireGuard Setup for Android/iOS**

Install the client on your preferred platform; [Android](https://play.google.com/store/apps/details?id=com.wireguard.android) or [iOS](https://apps.apple.com/us/app/wireguard/id1441195209?ls=1)

On the top right, there will be a + button for us to add a peer. Click on it.  
Here we can add the configuration settings that we generated from Step 1.

The interface should look like the following for Android and iOS respectively:

[![WireGuard section. ](https://downloads.intercomcdn.com/i/o/779592362/e99851c6d6d1e32a52d6509d/android.png?expires=1781168400&signature=00b40057fba9ee8ffb1e634d86e387fc55a7e5aae27a48a152913cf67afe8251&req=cycuE8B8noddFb4f3HP0gJwqEjbMslp2yewUHaNBRbHJ6GcnZ2%2BKZZzhWDwW%0AgNCA5fa4PZFGFsv5YQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779592362/e99851c6d6d1e32a52d6509d/android.png?expires=1781168400&signature=00b40057fba9ee8ffb1e634d86e387fc55a7e5aae27a48a152913cf67afe8251&req=cycuE8B8noddFb4f3HP0gJwqEjbMslp2yewUHaNBRbHJ6GcnZ2%2BKZZzhWDwW%0AgNCA5fa4PZFGFsv5YQ%3D%3D%0A)

[![Edit configuration section.](https://downloads.intercomcdn.com/i/o/779592267/cda77efe70c1f6b1fbef2948/ios.png?expires=1781168400&signature=97f9f622bb250c1944f04290f5fc58da0a5eb015185986d64b996c623a32b955&req=cycuE8B8n4dYFb4f3HP0gDeR0aCwHpoa1fktaiMZDEvXoY%2B78EcOylS7qbQh%0AEnr4ouNBd%2BS6ewnCHg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/779592267/cda77efe70c1f6b1fbef2948/ios.png?expires=1781168400&signature=97f9f622bb250c1944f04290f5fc58da0a5eb015185986d64b996c623a32b955&req=cycuE8B8n4dYFb4f3HP0gDeR0aCwHpoa1fktaiMZDEvXoY%2B78EcOylS7qbQh%0AEnr4ouNBd%2BS6ewnCHg%3D%3D%0A)

## **Step 3: Test**

We can test to see if it's working by checking the [portal](https://portal.telnyx.com/#/app/networking/cloudvpn/) and seeing the last seen status change:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2338094233/da6cf10dc989554219f661e0ea83/image+%284%29.png?expires=1781168400&signature=a82aad54283c0a67bec1255cd364981bad27affc70f10d87fa7ccfa63e1253a1&req=diMkHsl3mYNcWvMW1HO4zesKbLuhHpcvaihD6E2UCNFFDdB4MfP9Tg5fPH6h%0Aaxq7VxUvo1PwPQ2zUf4%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2338094233/da6cf10dc989554219f661e0ea83/image+%284%29.png?expires=1781168400&signature=a82aad54283c0a67bec1255cd364981bad27affc70f10d87fa7ccfa63e1253a1&req=diMkHsl3mYNcWvMW1HO4zesKbLuhHpcvaihD6E2UCNFFDdB4MfP9Tg5fPH6h%0Aaxq7VxUvo1PwPQ2zUf4%3D%0A)

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

Congratulations! You have successfully connected an Android and/or iOS instance to the Telnyx Edge Routing Network to the configured IP in your portal.

If you have any further questions or would like to see more tutorials, feel free to reach out to our support team or our external Slack channel for help!

---

Related Articles

[Telnyx Networking on AWS Lightsail](https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail)[Telnyx Networking on Ubuntu](https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu)[Telnyx Networking on AWS VPC](https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc)[Telnyx Networking on Azure Linux VMs](https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms)[Telnyx Networking on Oracle VMs](https://support.telnyx.com/en/articles/8104436-telnyx-networking-on-oracle-vms)

Did this answer your question?

😞😐😃

Table of contents
