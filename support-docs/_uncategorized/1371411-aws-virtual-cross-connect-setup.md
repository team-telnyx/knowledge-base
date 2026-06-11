---
source_url: https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup
scraped: 2026-06-11
---

AWS: Virtual Cross Connect Setup | Telnyx Help Center

[Skip to main content](#main-content)

# AWS: Virtual Cross Connect Setup

Learn how to integrate an AWS VPC environment with the Telnyx network backbone.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_d0dad697c3)

A virtual cross connect (VXC) is a private and direct connection between cloud providers that is faster and safer than a traditional public internet connection. Using this strategy allows you to bypass the internet and gain direct and private access to Telnyx, thereby eliminating hops and reducing the risk of packet loss and jitter. You’ll also benefit from the additional security of direct interconnection.

|  |
| --- |
| ***Note:*** *To protect against man in the middle attacks, we always recommend that you* [encrypt both signaling and media with TLS & Z/SRTP](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication). |

Further documentation:

* Amazon AWS [Direct Connect user guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
* Amazon AWS [Direct Connect virtual interfaces user guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html)
* Amazon AWS [Virtual Private Cloud](https://docs.aws.amazon.com/vpc/)

---

# Instructions for integrating Telnyx and AWS through a VXC

In this document, you will:

1. [Provide Telnyx with VXC preferences](#h_fcf7710367)
2. [Create a Virtual Private Gateway (VGW)](#h_36d0c85d12)
3. [Accept pending Direct Connect connections](#h_1bea825e20)
4. [Create a virtual interface for each circuit](#h_89c79af892)
5. [Enable route propagation for VPC route tables](#h_c7aa419f27)

​**Pre-Requisites**

* Have set up an AWS Virtual Private Cloud (VPC)
* Have the following information ready:

  + 12-digit AWS VPC account number
  + AWS region
  + Bandwidth speed between you and your VPC
  + Network name

**Video Walkthrough**

Coming soon! Check back frequently as we are updating our documentation.

## 1. Provide Telnyx with VXC preferences

In this step, you'll provide Telnyx with the information we need to provision Direct Connect connections that you'll then be able to accept in your AWS console.

1. Log into your Telnyx Mission Control Portal.
2. Navigate to the **Networking** section.
3. Click on **Create a New VXC** and provide the following values in the new VXC form:

   1. the 12-digit AWS account number associated with your VPC
   2. AWS region
   3. Bandwidth speed
   4. Network name

After receiving the request, Telnyx will create 1 or 2 Direct Connect connections that you can accept from your AWS console.

|  |
| --- |
| ***Note:*** *This request will take 1-3 days for Telnyx to complete. Once you submit your preferences to Telnyx, you will not be able to change them without creating a new VXC. You can complete step 2 now, but step 3 cannot be completed until Telnyx finishes this task.* |

[Back to Top](#h_d0dad697c3)

## 2. Create a Virtual Private Gateway (VGW)

In this task, you'll set up a VGW, which is an intermediary between AWS Direct Connect and your AWS VPC. You will need to create 1 VGW in order to complete this setup.

First, create the VGW:

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/).
2. Click on Virtual **Private Gateways > Create Virtual Private Gateway**.
3. Name your gateway.
4. Use the default ASN.
5. Choose **Create Virtual Private Gateway**.

Next, associate the new VFG with your destination AWS VPC.

1. From your [Amazon VPC console](https://console.aws.amazon.com/vpc/), select the VWG you just created.
2. Click on the **Actions** button and choose **Attach to VPC**.
3. Select your VPC from the list and choose **Yes, Attach**.
4. You should see the following:

   [![Amazon VPC console. ](https://downloads.intercomcdn.com/i/o/421128975/175063190953c9b410a909b5/Create_a_Virtual_Private_Gateway_in_AWS.png?expires=1781167500&signature=70da99f95ab6d6fcde1fdc19864eac602ea3d2a25bd2b7da01da27564eebddf4&req=cCImF8t2lIZaFb4f3HP0gI7wrrx3Pk8MflCuem9MQ%2FhUu3Jp0m4aSfkV%2FCCq%0AG8s%3D%0A)](https://downloads.intercomcdn.com/i/o/421128975/175063190953c9b410a909b5/Create_a_Virtual_Private_Gateway_in_AWS.png?expires=1781167500&signature=70da99f95ab6d6fcde1fdc19864eac602ea3d2a25bd2b7da01da27564eebddf4&req=cCImF8t2lIZaFb4f3HP0gI7wrrx3Pk8MflCuem9MQ%2FhUu3Jp0m4aSfkV%2FCCq%0AG8s%3D%0A)

[Back to Top](#h_d0dad697c3)

## 3. Accepting pending Direct Connect connections

Once Telnyx finishes creating your new VGWs, they'll be waiting for permission to accept Direct Connect connections. In this step, you'll log into your AWS account. You should find your VGWs waiting for your authorization.

|  |
| --- |
| ***Note:*** *If you requested a backup link, you'll see 2 pending connections in this step. If you didn't, you'll see 1.* |

1. Open your [AWS Direct Connect console](https://console.aws.amazon.com/directconnect/).
2. Click **Connections** in the navigation pane.
3. You should see either 1 or 2 connections waiting for acceptance.

   [![AWS direct connect console. ](https://downloads.intercomcdn.com/i/o/421147102/ad3c7bc97c5b2a3a4b53592c/connections.png?expires=1781167500&signature=fdebec98635b6bf33006c81545211561ad5ffb800fc64c19dc92be5cb9c7fcb3&req=cCImF815nIFdFb4f3HP0gECVnTT19FSK2zyAa4pO9pzKqowpUzxsHf2BzCf4%0AnF0%3D%0A)](https://downloads.intercomcdn.com/i/o/421147102/ad3c7bc97c5b2a3a4b53592c/connections.png?expires=1781167500&signature=fdebec98635b6bf33006c81545211561ad5ffb800fc64c19dc92be5cb9c7fcb3&req=cCImF815nIFdFb4f3HP0gECVnTT19FSK2zyAa4pO9pzKqowpUzxsHf2BzCf4%0AnF0%3D%0A)
4. For each connection in this list, expand each connection and select **I understand that Direct Connect port charges apply once I click Accept Connection**, and then choose **Accept Connection**.

   [![AWS direct connect console consent input. ](https://downloads.intercomcdn.com/i/o/41102606/eb2db453a23681724f01af4c/VXC+Image+3.PNG?expires=1781167500&signature=a3163e083eb22e6bedcf97ff97f10fc1c61fe68abf0846a7bca8ae1d2869ab09&req=cCEmFst4nYcTWLcX3D%2B5hmFhBSJ23EM1P1NXhGk2faeSInkNJ45a4QOZvDtH%0A8A%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/41102606/eb2db453a23681724f01af4c/VXC+Image+3.PNG?expires=1781167500&signature=a3163e083eb22e6bedcf97ff97f10fc1c61fe68abf0846a7bca8ae1d2869ab09&req=cCEmFst4nYcTWLcX3D%2B5hmFhBSJ23EM1P1NXhGk2faeSInkNJ45a4QOZvDtH%0A8A%3D%3D%0A)
5. Once the connections are completed, your output should show each connection as available.

   [![AWS direct connect output display. ](https://downloads.intercomcdn.com/i/o/41102671/92d7d66392f60d2e4095d9ad/VXC+Image+4.PNG?expires=1781167500&signature=52545a604b70575661aa1726dcb0bd3ece1fdee2a4ce4ea71aa690d54b094961&req=cCEmFst4moATWLcX3D%2B5hnXKUiRUv18lYRmCEPlJcRsLaqiEZYYYWTT%2F%2Fo%2B2%0AXw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/41102671/92d7d66392f60d2e4095d9ad/VXC+Image+4.PNG?expires=1781167500&signature=52545a604b70575661aa1726dcb0bd3ece1fdee2a4ce4ea71aa690d54b094961&req=cCEmFst4moATWLcX3D%2B5hnXKUiRUv18lYRmCEPlJcRsLaqiEZYYYWTT%2F%2Fo%2B2%0AXw%3D%3D%0A)

[Back to Top](#h_d0dad697c3)

## 4. Create a virtual interface for each circuit

In this step, you will be creating a private virtual interface. These are used to access a VPC using a private IP address. This is where all Layer 3 addressing and [BGP](https://telnyx.com/resources/what-is-bgp) (border gateway protocol) details will be completed.

|  |
| --- |
| ***Note:*** *Some of the information you'll need to supply in this step will have been provided to you in the Telnyx support email that should have come along with your new VGW(s). If you did not receive this, or you can't locate it, just reach out to Telnyx support and we'll sort it out for you!* |

1. Open your [AWS Direct Connect console](https://console.aws.amazon.com/directconnect/).
2. Click on **Connections** in the navigation pane.
3. Select the first connection on the list (that you configured in step 3) and choose **Actions > Create Virtual Interface**.
4. Fill out the form with the following information:

   1. **Public or Private:** Private
   2. **Virtual Interface Name:** Use the connection ID
   3. **Your router peer IP:** Use the Telnyx IP that was provided in the telnyx support email
   4. **Amazon router peer IP:** Use the customer IP that was provided in the Telnyx support email
   5. **BGP ASN:** You can find this in the Telnyx support email
   6. **BGP Authentication Key:** You can find this in the Telnyx support email

   [![AWS direct connect console for creating virtual interface. ](https://downloads.intercomcdn.com/i/o/421162025/1361d2d799fa65a42a670334/Create_a_Virtual_Interface_Per_Circuit_Screenshot.png?expires=1781167500&signature=5c791479e5eadb9a4269ba338d3364de65173b36e924a9fa35a825938696a8aa&req=cCImF898nYNaFb4f3HP0gMhtaq%2FzlqmNcIk3NkQ%2F%2F1x7B9Fy%2FY%2BfSebc8dkN%0Ax4Q%3D%0A)](https://downloads.intercomcdn.com/i/o/421162025/1361d2d799fa65a42a670334/Create_a_Virtual_Interface_Per_Circuit_Screenshot.png?expires=1781167500&signature=5c791479e5eadb9a4269ba338d3364de65173b36e924a9fa35a825938696a8aa&req=cCImF898nYNaFb4f3HP0gMhtaq%2FzlqmNcIk3NkQ%2F%2F1x7B9Fy%2FY%2BfSebc8dkN%0Ax4Q%3D%0A)
5. If you requested a redundant backup link, repeat steps 3 through 5 in this step for that connection as well.

[Back to Top](#h_d0dad697c3)

## 5. Enable route propagation for VPC route tables

Now that you have created virtual interfaces (Step 4), BGP sessions will form with Telnyx and routing will be in place on these connections. In this step, you'll ensure that route propagation is enabled for the VGW, which will allow it to automatically propagate routes to the route tables so you don't have to do it manually.

1. Open your [AWS Direct Connect console](https://console.aws.amazon.com/directconnect/).
2. Click the **Route Propagate** tab.
3. Choose **Edit**.
4. Select the **Propagate** checkbox next to your VGW.

Hit **Save**. The routing table should now display Telnyx prefixes routing to the VGW. When these are visible in the routing table, integration between Telnyx and AWS is complete and you can test IP reachability.

[![AWS direct connect console for route propagate tab. ](https://downloads.intercomcdn.com/i/o/421168543/06579115dd9a6a84ff3895f6/Routes_Tab_Screenshot.png?expires=1781167500&signature=b1be8f9781240d7e7309a40158feac0a746f02c3571a81c5641609bc48fdd5c0&req=cCImF892mIVcFb4f3HP0gHIPXUCTU3Y4I3Y1NsXmzP0o7WWD5VYrVvoz45oV%0Avm4saMSGhpJCafj69g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/421168543/06579115dd9a6a84ff3895f6/Routes_Tab_Screenshot.png?expires=1781167500&signature=b1be8f9781240d7e7309a40158feac0a746f02c3571a81c5641609bc48fdd5c0&req=cCImF892mIVcFb4f3HP0gHIPXUCTU3Y4I3Y1NsXmzP0o7WWD5VYrVvoz45oV%0Avm4saMSGhpJCafj69g%3D%3D%0A)

That's it, you've now integrated your AWS VPC and Telnyx though VXC.

[Back to Top](#h_d0dad697c3)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, see:

* Amazon AWS [Direct Connect user guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
* Amazon AWS [Direct Connect virtual interfaces user guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html)
* Amazon AWS [Virtual Private Cloud](https://docs.aws.amazon.com/vpc/)

---

Related Articles

[Azure: Virtual Cross Connect](https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect)[Google VPC: Telnyx Integration](https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration)[Megaport Configuration with TELNYX](https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx)[Telnyx Networking on AWS Lightsail](https://support.telnyx.com/en/articles/8103288-telnyx-networking-on-aws-lightsail)[Telnyx Networking on AWS VPC](https://support.telnyx.com/en/articles/8104309-telnyx-networking-on-aws-vpc)

Did this answer your question?

😞😐😃

Table of contents
