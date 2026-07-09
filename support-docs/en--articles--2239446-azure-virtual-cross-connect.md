---
source_url: https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect
scraped: 2026-07-08
content_hash: 372d70edce629f978700499923aa4c376c77bb78589b4121fd1ce1a5acc03c35
---

Azure: Virtual Cross Connect | Telnyx Help Center

[Skip to main content](#main-content)

# Azure: Virtual Cross Connect

This document will provide instructions and guidelines for integrating an Azure VPC environment with the Telnyx network backbone.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_c4436070ec)

This document will provide instructions, technical details and guidelines for integrating a [Microsoft Azure Cloud](https://azure.microsoft.com/en-us/) environment with the Telnyx network backbone. A virtual cross connect (VXC) is a private and direct connection between cloud providers that is faster and safer than a traditional public internet connection. Using this strategy allows you to bypass the internet and gain direct and private access to Telnyx, thereby eliminating hops and reducing the risk of packet loss and jitter. You’ll also benefit from the additional security of direct interconnection.

Additional documentation:

* [Microsoft Azure technical documentation](https://learn.microsoft.com/en-us/)

---

# Instructions for integrating Azure VPC with Telnyx

In this activity you will:

1. [Prepare your Microsoft account for an Azure Express Route](#h_1dd7eadf26)
2. [Set up a VXC in your Telnyx Mission Control Portal](#h_d1bbf97e8d)
3. [Turn up routing and NAT configuration](#h_ac858b4624)

**Pre-requisites**

* Have a Microsoft Azure cloud environment

**Video Walkthrough**

Coming soon! Check back frequently as we are updating our documentation.

## 1. Prepare Microsoft account for Azure Express Route.

1. ### **Log into your [Azure Portal](https://portal.azure.com/#home).**

   ![The Azure portal interface. ](_images/afe3599b4c90ce84.png)
2. ### **Perform a search for *express route* and click on *Express Route Circuits.***

   ![An open search tab for express route circuits. ](_images/473d679738f44aa7.png)
3. ### **Click on Add -> Provider. This provider *must* be *Equinix*, *do \*NOT\** select *Allow Classic Operations*. Rename other fields at your discretion.**

   ![Provider addition tab. ](_images/04bdee9281839c58.png)

   ![Microsoft Azure dashboard. ](_images/a886509000445920.png)
4. ### **Click OK.**
5. ### **Once the deployment completes, you will see your newly-provisioned Azure Express Route.**

   ![Newly-provisioned Azure express route.](_images/1e223319babbed1a.png)

[Back to Top](#h_c4436070ec)

## 2. Set up the VXC in your Telnyx Mission Control Portal

1. ### **Log into your [Telnyx Mission Control Portal](https://portal.telnyx.com).**
2. ### **Click on "Networking" in the left-hand menu**

   ![Telnyx Mission Control Portal. ](_images/ce72b790e3013644.png)
3. ### **Click on the "Create New Network" button on the top-right.**

   !["Create New Network" button. ](_images/aba0e7768d0e3e8c.png)
4. ### **Give your network a name and click on the "Create Network" button**

   !["Create Network" button. ](_images/4fae7e1732e14348.png)
5. ### **Once the Network is Created, Next step is to add the site. Click on the "Add a Site" button.**

   !["Add a site" button. ](_images/9a18ec397d061afe.png)
6. ### **Choose the Telnyx Backbone Network you want to peer with.**

   ![Telnyx Backbone Network selection table. ](_images/16177156943b6a23.png)
7. ### **Add the VXC, by clicking on "Create VXC".**

   !["Create VXC" add button. ](_images/7bcf4a962b2792c9.png)
8. ### **Create an Azure Express Route.**

   #### Note that in order to complete this section, Stage 1 needs to have been completed.

   ![Azure Express Route creation portal. ](_images/5bc7392afdc7fb42.png)

   ​
9. ### **Key in Azure Service Key and Microsoft Azure ASN. Typically it is 12076**

   ![Azure Service Key and Microsoft Azure ASN credentials input. ](_images/3ff1230ce0a8f6e8.png)

   #### **You can see a sample Service Key and ASN Displayed Below**

   ![Sample Service Key and ASN display. ](_images/46792623108fd182.png)
10. ### **Now create your VXC and submit it to Telnyx Network team.**

    ![VXC creation portal and submission button. ](_images/23933c5d9b4429ba.png)

    #### Connection acceptance will be TELNYX Network Team.

    ![Routing and NAT configuration interface. ](_images/ddeefdc918a0304c.png)

|  |
| --- |
| ***IMPORTANT:*** *Do NOT Enable Routing status via the slider, this step has to be coordinated in sync with Telnyx Network Team, as enabling this without Backend configuration may blackhole your voice traffic.* |

[Back to Top](#h_c4436070ec)

## 3. Turning up Routing and NAT configuration

1. Arrange a Maintenance activity and co-ordinate with TELNYX Network engineering to turn on the Routing. Please [contact our Support Team](https://telnyx.com/contact-us) to assist with this.   
   ​  
   ​***Note:*** *This activity has to be co-ordinate with the Network team to complete Back-end configuration during the Maintenance window.*
2. Once you enable the circuit using the Routing Status slider, you should see a routing table in Express Route similar to the following:

   ![Routing and NAT configuration interface. ](_images/d1b96d106ae67bb7.png)

### **Once enabled with Routing, you'll see Telnyx public ranges via Express Route Circuit. This will ensure that these are preferred over the Internet Routing Table.**

![Routing table display. ](_images/e5a1be5db1b8f53b.png)

That's it, you've now integrated your Google VPC and Telnyx though VXC.

[Back to Top](#h_c4436070ec)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, see:

* [Microsoft Azure technical documentation](https://learn.microsoft.com/en-us/)

---

Related Articles

[AWS: Virtual Cross Connect Setup](https://support.telnyx.com/en/articles/1371411-aws-virtual-cross-connect-setup)[Google VPC: Telnyx Integration](https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration)[Configuring Telnyx with Microsoft Teams Direct Routing](https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing)[Azure AD: SAML Identity Setup](https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup)[Telnyx Networking on Azure Linux VMs](https://support.telnyx.com/en/articles/8104343-telnyx-networking-on-azure-linux-vms)

Did this answer your question?

😞😐😃

Table of contents
