---
source_url: https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration
scraped: 2026-06-11
---

Google VPC: Telnyx Integration | Telnyx Help Center

[Skip to main content](#main-content)

# Google VPC: Telnyx Integration

This document will provide instructions and guidelines for integrating a Google Cloud environment with the Telnyx network backbone.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_691dca3fcb)

This document will provide instructions, technical details and guidelines for integrating a [Google Cloud](https://cloud.google.com/) environment with the Telnyx network backbone. A virtual cross connect (VXC) is a private and direct connection between cloud providers that is faster and safer than a traditional public internet connection. Using this strategy allows you to bypass the internet and gain direct and private access to Telnyx, thereby eliminating hops and reducing the risk of packet loss and jitter. You’ll also benefit from the additional security of direct interconnection.

|  |
| --- |
| ***Note:*** *To protect against man in the middle attacks, we always recommend that you* [encrypt both signaling and media with TLS & Z/SRTP](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication). |

Further documentation:

* [Google VPC documentation](https://cloud.google.com/vpc#section-4)
* [VLAN attachments documentation](https://cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)

---

# Instructions for integrating Google VPC with Telnyx

In this activity you will:

1. [Create a GCP Partner Interconnect and VLAN attachments](#1-create-a-gpc-partner-interconnect-and-vlan-attachments)
2. [Provide Telnyx with your VXC preferences](#2-provide-telnyx-with-vxc-preferences)
3. [Activate the Virtual Cross Connect in Google Cloud Console](#h_4971b62ecb)
4. [Complete your order in Telnyx](#h_64718b336b)

**Pre-requisites**

* GCP Virtual Private Cloud (VPC) network
* For optimal performance, your VPC needs to be located in the same region where you plan to build a Virtual Cross Connect (VXC)

**Video Walkthrough**

Coming soon! Check back frequently as we are updating our documentation.

## 1. Create a GPC Partner Interconnect and VLAN attachments

In this step, you'll create a GPC partner interconnect, which will connect your Google Cloud VPC to the Telnyx network. You will then create VLAN attachments which are connections between your local routers and Google Cloud's routers used by your partner interconnect.

1. Open the [Google Cloud Platform VPC](https://console.cloud.google.com/hybrid/interconnects/).
2. Choose **Interconnect Type -> Partner Interconnect**

   [![Google Cloud Platform VPC interface. ](https://downloads.intercomcdn.com/i/o/83697968/552f2d00abef6c13cdb815b3/Screen+Shot+2018-11-01+at+2.07.09+PM.png?expires=1781167500&signature=744771ee6c8824145af3e2a7ce10c01ef6c67d575b0d4dc506c262842fe79d3c&req=fCMhH853m4kTWLcX3D%2B5hi2NL4w5t9HBEsULJGsktcz%2BZaMZRHIna7iIu374%0Aag%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/83697968/552f2d00abef6c13cdb815b3/Screen+Shot+2018-11-01+at+2.07.09+PM.png?expires=1781167500&signature=744771ee6c8824145af3e2a7ce10c01ef6c67d575b0d4dc506c262842fe79d3c&req=fCMhH853m4kTWLcX3D%2B5hi2NL4w5t9HBEsULJGsktcz%2BZaMZRHIna7iIu374%0Aag%3D%3D%0A)
3. Under **Add Partner VLAN Attachment -> Check your connection**, choose *I already have a service provider.*

   [![Partner VLAN Attachment Addition. ](https://downloads.intercomcdn.com/i/o/83698234/2c56400b164de46b8668e321/Screen+Shot+2018-11-01+at+2.09.15+PM.png?expires=1781167500&signature=5cf3b0ad488635f6185c245d77250351a15425942b624cf7abfc4327a8c9f654&req=fCMhH8F8noUTWLcX3D%2B5hkudgesnSVz5oaC%2BuV3XvITDFJeVeVhB4Vqfdg6H%0A8A%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/83698234/2c56400b164de46b8668e321/Screen+Shot+2018-11-01+at+2.09.15+PM.png?expires=1781167500&signature=5cf3b0ad488635f6185c245d77250351a15425942b624cf7abfc4327a8c9f654&req=fCMhH8F8noUTWLcX3D%2B5hkudgesnSVz5oaC%2BuV3XvITDFJeVeVhB4Vqfdg6H%0A8A%3D%3D%0A)
4. Under **Add VLAN attachments**, fill in the following:

   1. **Redundancy:** Telnyx recommends selecting *Create a redundant pair of VLAN attachments**.*** See pricing for each Virtual Cross Connect [here](https://telnyx.com).Note that a redundant pair of VLAN attachments requires two VXCs.**)**
   2. **VPC network:** *default*
   3. **Region:**  The region should be the same region where you’re running the software application.
   4. **Cloud Router:**  The router will be created in the same region as your VPC Network.
   5. **Name the VLAN attachment(s):** Consider a naming convention similar to us-east-4-vlan-attachment-1 (i.e.: country-region-etc)

      [![VLAN attachment naming portal. ](https://downloads.intercomcdn.com/i/o/83698842/15239166fdc526c86e7df4db/Screen+Shot+2018-11-01+at+2.12.57+PM.png?expires=1781167500&signature=064080adc6afaa6f090c7db9eb3dd6fd2f07609aa4f38a44652fc33a149bed47&req=fCMhH8F2mYMTWLcX3D%2B5huLdtCqTbbiOmWvgQMAnrYUAfGkir469v44%2BW9HI%0AZw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/83698842/15239166fdc526c86e7df4db/Screen+Shot+2018-11-01+at+2.12.57+PM.png?expires=1781167500&signature=064080adc6afaa6f090c7db9eb3dd6fd2f07609aa4f38a44652fc33a149bed47&req=fCMhH8F2mYMTWLcX3D%2B5huLdtCqTbbiOmWvgQMAnrYUAfGkir469v44%2BW9HI%0AZw%3D%3D%0A)
5. Click **Create**.
6. Now select **OK** to connect your VPC networks.
7. Click on VLAN Attachment Detail and copy your pairing key(s). You will need them

[Back to Top](#h_691dca3fcb)

## 2. Provide Telnyx with VXC Preferences

In this step, you'll let Telnyx know your VXC preferences for a network and a site. The network uses virtual routing and forwarding technology to provide you with a unique routing table within Telnyx's routers. A site is a Telnyx Point of Presence (PoP) where we house our network gear.

1. Log into your Telnyx Mission Control Portal.
2. Go to the **Networking** section.
3. Click **Create New Network** to create a new one.

   1. If you have one you want to use, click **View Details** for this network.
4. Find the **Site Detail** section of your network and click **Add Site(s)**, then **Create VXC** to create a new site.

   1. If you have a site you want to use, click **Create VXC** on an existing site.

   Note that you should select sites that are local to your Google Cloud region(s). See a [list of Telnyx sites and their corresponding local Google Cloud regions](https://telnyx.com/).
5. Select **Google Cloud** as your Cloud Provider.
6. Click **Next.**
7. Select Bandwidth Speed.
8. Click **Next.**
9. Input your **Google Pairing Key** for you primary VLAN attachment. (i.e., the last number of the pairing key should be "1")  You can retrieve this from <https://console.cloud.google.com/hybrid/interconnects,> and by viewing **VLAN Attachment Detail.**They key will be in the format *<random>/<vlan-attachment-region>/<edge-availability-domain*>
10. If you created a redundant link, click **Secondary Link** and input your **Google Pairing Key** from the secondary **VLAN Attachment** (i.e., the last number of the pairing key should be "2")
11. Review **New Virtual Cross Connect (VXC) Request.**Click **Create VXC.**

[Back to Top](#h_691dca3fcb)

## 3.  Activate the Virtual Cross Connect in Google Cloud

Now that everything is configured, let's activate your VXC in Google Cloud.

1. Open the Google Cloud Platform VPC at <https://console.cloud.google.com/hybrid/interconnects/>.
2. For each VLAN Attachment under Actions, Click **Activate.** (This option may take up to 5 minutes to appear.)  ThenClick **Accept**

   [![Google Cloud Platform VPC. ](https://downloads.intercomcdn.com/i/o/83722725/52d3c429ecefbae24d95648e/Screen+Shot+2018-11-01+at+4.52.46+PM.png?expires=1781167500&signature=f41becd158ffa8da800e0e3c5fdb42b3af3a0bc9c35f78b2e87475f568b05190&req=fCMgFMt5n4QTWLcX3D%2B5hg4F%2Fa4gMxyI1nymOtN5uONws6iPoKTo9Z58uCr%2B%0AyQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/83722725/52d3c429ecefbae24d95648e/Screen+Shot+2018-11-01+at+4.52.46+PM.png?expires=1781167500&signature=f41becd158ffa8da800e0e3c5fdb42b3af3a0bc9c35f78b2e87475f568b05190&req=fCMgFMt5n4QTWLcX3D%2B5hg4F%2Fa4gMxyI1nymOtN5uONws6iPoKTo9Z58uCr%2B%0AyQ%3D%3D%0A)
3. For each VLAN Attachment under Actions, Click **Configure [BGP](https://telnyx.com/resources/what-is-bgp).**

   [![Google Cloud Platform VPC VLAN attachment configuration. ](https://downloads.intercomcdn.com/i/o/84423042/639f7e5968eba9b8a5081d1a/Screen+Shot+2018-11-06+at+4.41.51+PM.png?expires=1781167500&signature=92c2c7d3c6a5f15bba5a3608f5540e033d93fbe3b5c0ea83c0e6642ccb70b173&req=fCQjFMp%2BmYMTWLcX3D%2B5hu8hxuNHli0S%2Bv0XB0ffrfDCNTlGwa%2FD71x1Dajw%0AFQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/84423042/639f7e5968eba9b8a5081d1a/Screen+Shot+2018-11-06+at+4.41.51+PM.png?expires=1781167500&signature=92c2c7d3c6a5f15bba5a3608f5540e033d93fbe3b5c0ea83c0e6642ccb70b173&req=fCQjFMp%2BmYMTWLcX3D%2B5hu8hxuNHli0S%2Bv0XB0ffrfDCNTlGwa%2FD71x1Dajw%0AFQ%3D%3D%0A)
4. In EDIT BGP session, in the **Peer ASN** field, input **63440**.   Click **Save and Continue.**

   [![EDIT BGP session tab, in the Peer ASN field. ](https://downloads.intercomcdn.com/i/o/84424452/cbfef0d317b4d9b61aba7c3e/Screen+Shot+2018-11-06+at+4.40.55+PM.png?expires=1781167500&signature=47cbcf82d661000961a68bb32fbc79c4dde652e9ff1e5ae5ac2914af2076f46e&req=fCQjFM16mIMTWLcX3D%2B5huE51cZ%2BtXrTLKZyGkkfywVWMFslCc%2BUTt0TVYJ6%0AjA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/84424452/cbfef0d317b4d9b61aba7c3e/Screen+Shot+2018-11-06+at+4.40.55+PM.png?expires=1781167500&signature=47cbcf82d661000961a68bb32fbc79c4dde652e9ff1e5ae5ac2914af2076f46e&req=fCQjFM16mIMTWLcX3D%2B5huE51cZ%2BtXrTLKZyGkkfywVWMFslCc%2BUTt0TVYJ6%0AjA%3D%3D%0A)
5. Click **Refresh.**Status should say **Up.**

   [![Refreshed EDIT BGP session tab, in the Peer ASN field. ](https://downloads.intercomcdn.com/i/o/84423667/1736f39055fb9041a4e80c6d/Screen+Shot+2018-11-06+at+4.46.51+PM.png?expires=1781167500&signature=9a030e3c85e71fdeb0a1f6b144713bb3d3fc2313bd485e82bf4b7e7209de0cf0&req=fCQjFMp4m4YTWLcX3D%2B5hhHnIAwUnfeF%2BOq9VZVdsyto5LXc9925QyRcyjF%2F%0APA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/84423667/1736f39055fb9041a4e80c6d/Screen+Shot+2018-11-06+at+4.46.51+PM.png?expires=1781167500&signature=9a030e3c85e71fdeb0a1f6b144713bb3d3fc2313bd485e82bf4b7e7209de0cf0&req=fCQjFMp4m4YTWLcX3D%2B5hhHnIAwUnfeF%2BOq9VZVdsyto5LXc9925QyRcyjF%2F%0APA%3D%3D%0A)
6. Copy the **Cloud Router IP** for each VLAN Attachment.  You will need this in the next step.

   [![Refreshed EDIT BGP session tab, in the Peer ASN field. ](https://downloads.intercomcdn.com/i/o/84424344/0026049065e4a8aa832d6e04/Screen+Shot+2018-11-06+at+4.52.49+PM.png?expires=1781167500&signature=0567074679d72b420dddceb990a5715b0bccb602a407ee90d34a7df5b8e9766b&req=fCQjFM19mYUTWLcX3D%2B5hmzut47QLy2PHVC1qafybO%2BJGKkgTpqo6nZV%2Bps5%0AnQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/84424344/0026049065e4a8aa832d6e04/Screen+Shot+2018-11-06+at+4.52.49+PM.png?expires=1781167500&signature=0567074679d72b420dddceb990a5715b0bccb602a407ee90d34a7df5b8e9766b&req=fCQjFM19mYUTWLcX3D%2B5hmzut47QLy2PHVC1qafybO%2BJGKkgTpqo6nZV%2Bps5%0AnQ%3D%3D%0A)

[Back to Top](#h_691dca3fcb)

## 4.  Complete your Order in Telnyx

1. Copy the **Cloud Router IP** for the first VLAN Attachment.  Click **Save.**If you have a redundant link, copy the **Cloud Router IP** for the second VLAN Attachment.  Click **Save.**

   [![Cloud router IP portal. ](https://downloads.intercomcdn.com/i/o/84634563/c382b56aa01c8d755f313548/Screen+Shot+2018-11-07+at+4.36.57+PM.png?expires=1781167500&signature=e3321ae5579b4b008afca76052a6186915e31f6ff8958054ef1a10362f823f51&req=fCQhFc17m4ITWLcX3D%2B5hkRtKOTjLXbB0b5ePTkKImmNI2wLGIE79Foci4m1%0AEQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/84634563/c382b56aa01c8d755f313548/Screen+Shot+2018-11-07+at+4.36.57+PM.png?expires=1781167500&signature=e3321ae5579b4b008afca76052a6186915e31f6ff8958054ef1a10362f823f51&req=fCQhFc17m4ITWLcX3D%2B5hkRtKOTjLXbB0b5ePTkKImmNI2wLGIE79Foci4m1%0AEQ%3D%3D%0A)
2. Telnyx will approve your request (this may take up to 3 hours).  Order Status will change from **Pending** to **Active** to **Complete.**Once an **Order Status** is complete, the BGP session between Telnyx and Google Cloud will be active.
3. To receive traffic from Telnyx, your cloud hosts must have public IP addresses configured. Consult your Telnyx representative before clicking 'Enable' if you need assistance.
4. Under routing status, click the button to enable.  Doing this will transition packet delivery from your Cloud Provider's Internet transit to the private Virtual Cross Connect resulting in a brief traffic disruption.  
   ​

   [![Routing status enable button. ](https://downloads.intercomcdn.com/i/o/84635287/315b29497959fb5ee217d49d/Screen+Shot+2018-11-07+at+4.38.54+PM.png?expires=1781167500&signature=56a33390d2917f15c7bf0235c03d00ede082235410141213f7b128f68bd4f549&req=fCQhFcx8lYYTWLcX3D%2B5hnKcvMPonXcY0lrcc2n32yOuEVDn91IqOKBVQ4TD%0ASA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/84635287/315b29497959fb5ee217d49d/Screen+Shot+2018-11-07+at+4.38.54+PM.png?expires=1781167500&signature=56a33390d2917f15c7bf0235c03d00ede082235410141213f7b128f68bd4f549&req=fCQhFcx8lYYTWLcX3D%2B5hnKcvMPonXcY0lrcc2n32yOuEVDn91IqOKBVQ4TD%0ASA%3D%3D%0A)

That's it, you've now integrated your Google VPC and Telnyx though VXC.

[Back to Top](#h_691dca3fcb)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, see:

* [Google VPC documentation](https://cloud.google.com/vpc#section-4)
* [VLAN attachments documentation](https://cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)

---

Related Articles

[AWS: Virtual Cross Connect Setup](https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup)[Azure: Virtual Cross Connect](https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect)[Use ExpanDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage)[Intro to Telnyx Edge Router](https://support.telnyx.com/en/articles/8126141-intro-to-telnyx-edge-router)[BYOC: Telnyx & Genesys](https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys)

Did this answer your question?

😞😐😃

Table of contents
