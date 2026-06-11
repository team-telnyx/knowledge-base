---
source_url: https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx
scraped: 2026-06-11
---

Megaport Configuration with TELNYX | Telnyx Help Center

[Skip to main content](#main-content)

# Megaport Configuration with TELNYX

In this article we will explain how to configure Megaport with Telnyx.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_931a5218c3)

[Megaport](https://www.megaport.com/) is a global leading Network as a Service provider transforming the way businesses connect to AWS Cloud <https://www.megaport.com/services/amazon-web-services/>. Our SDN and easy-to-use Portal enable users to provision instant and dedicated access to AWS Direct Connect across hundreds of global locations.

Additional resources:

* [Megaport documentation](https://docs.megaport.com/)
* [Megaport support](https://docs.megaport.com/support/contact/)
* [Megaport resource center](https://www.megaport.com/resources/)

---

# Instructions for configuring Megaport with Telnyx

In this activity you will:

1. [Create a connection between Telnyx and your Megaport portal](#h_2463bf030a)

**Pre-requisites:**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Megaport ports must be live on both ends

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Megaport/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Create a connection between Telnyx and the Megaport portal

In this section, you'll set up a configuration from the customer side to connect Telnyx to your Megaport portal. This needs to be done in order to use the service key provided by Telnyx.

1. Log into your Megaport portal account.
2. Click **+ Connection**.
3. Click **Enter Service Key**.

   [![Telnyx and the Megaport portal connection portal. ](https://downloads.intercomcdn.com/i/o/119817756/a90ee85232186da5446dfb5e/11.png?expires=1781167500&signature=f908bbbf6aa013db2b62dfdad1617dcdb930ddefd309452b062864e840c833af&req=dSEuHsh5moRZFb4f3HP0gCYEDZzcifANLchrFV79NZ%2FhLkOLUnUAW03ykc5M%0AU0E%3D%0A)](https://downloads.intercomcdn.com/i/o/119817756/a90ee85232186da5446dfb5e/11.png?expires=1781167500&signature=f908bbbf6aa013db2b62dfdad1617dcdb930ddefd309452b062864e840c833af&req=dSEuHsh5moRZFb4f3HP0gCYEDZzcifANLchrFV79NZ%2FhLkOLUnUAW03ykc5M%0AU0E%3D%0A)

   [![Telnyx and the Megaport portal connection portal. ](https://downloads.intercomcdn.com/i/o/119817788/e3e32a2bf37a6dfe168f0fcf/12.png?expires=1781167500&signature=307e9d932577d1290fd149fbb5ec05f91d1c97f293268b907cf4c85def19c800&req=dSEuHsh5molXFb4f3HP0gJmJEqwIqVXygh5ILIYUDwQgwWiXQGoxswk79A6G%0AMdU%3D%0A)](https://downloads.intercomcdn.com/i/o/119817788/e3e32a2bf37a6dfe168f0fcf/12.png?expires=1781167500&signature=307e9d932577d1290fd149fbb5ec05f91d1c97f293268b907cf4c85def19c800&req=dSEuHsh5molXFb4f3HP0gJmJEqwIqVXygh5ILIYUDwQgwWiXQGoxswk79A6G%0AMdU%3D%0A)
4. Provide the following information:

   1. **Megaport Service Key ID:** Enter the service key provided by Telnyx. The data from this key will populate. If you did not receive a service key, or are unsure, contact Telnyx Support.

      [![Megaport service key ID credentials input tab. ](https://downloads.intercomcdn.com/i/o/119817839/7ab5cf6d43b1e076210aac95/13.png?expires=1781167500&signature=b1ff2101d18dfcd1135d90802ab11f302e2321c2d5119bb913fd65269f440fcf&req=dSEuHsh5lYJWFb4f3HP0gFdtdzfNtFFtEtRrQPzhVHAC3Py4sTjLCgnl%2B5cf%0ABY4%3D%0A)](https://downloads.intercomcdn.com/i/o/119817839/7ab5cf6d43b1e076210aac95/13.png?expires=1781167500&signature=b1ff2101d18dfcd1135d90802ab11f302e2321c2d5119bb913fd65269f440fcf&req=dSEuHsh5lYJWFb4f3HP0gFdtdzfNtFFtEtRrQPzhVHAC3Py4sTjLCgnl%2B5cf%0ABY4%3D%0A)
5. Once you've entered your service key, you'll notice that the details have updated on your screen.

   [![Megaport service key ID credentials input tab. ](https://downloads.intercomcdn.com/i/o/119817870/6be69a1c4039814429ef5643/14.png?expires=1781167500&signature=ce6939a825a21b6911e95ec68e2c1c39de3a333fe4123d7094d1d6797406352f&req=dSEuHsh5lYZfFb4f3HP0gPoNZcKqfA3I7weB6WLfK7FYrfEaFpSRoMdUFOJj%0Aiow%3D%0A)](https://downloads.intercomcdn.com/i/o/119817870/6be69a1c4039814429ef5643/14.png?expires=1781167500&signature=ce6939a825a21b6911e95ec68e2c1c39de3a333fe4123d7094d1d6797406352f&req=dSEuHsh5lYZfFb4f3HP0gPoNZcKqfA3I7weB6WLfK7FYrfEaFpSRoMdUFOJj%0Aiow%3D%0A)
6. Click **Next**.
7. You'll be taken to a form where you'll need to confirm the following auto-filled details:

   1. **Name your connection:** You can name this anything you like. We recommend something that can help you easily identify your connection and its purpose.
   2. **Rate limit:** This limits network traffic and puts a cap on how often someone can repeat an action within a certain timeframe – for instance, trying to log in to an account. Rate limiting can help stop certain kinds of malicious bot activity.
   3. **Preferred A-End VLAN:** Each VXC is delivered as a separate VLAN on your Port. This must be a unique VLAN ID on this Port and can range from 2 to 4093. If you specify a VLAN ID that is already in use, the system displays the next available VLAN number. The VLAN ID must be unique to proceed with the order. If you don’t specify a value, Megaport will assign one.

      [![Preferred A-End VLAN tab. ](https://downloads.intercomcdn.com/i/o/119818303/1744cb98be32ee6e1fcb1020/16.png?expires=1781167500&signature=d53d27ba94f30264c1a1956c7c434fd51186b7901f29acb0f07fd9e29b514836&req=dSEuHsh2noFcFb4f3HP0gO4EauhtdmPZotBO35AZcFfpf1hNVfTPWh8I75zy%0A0Bw%3D%0A)](https://downloads.intercomcdn.com/i/o/119818303/1744cb98be32ee6e1fcb1020/16.png?expires=1781167500&signature=d53d27ba94f30264c1a1956c7c434fd51186b7901f29acb0f07fd9e29b514836&req=dSEuHsh2noFcFb4f3HP0gO4EauhtdmPZotBO35AZcFfpf1hNVfTPWh8I75zy%0A0Bw%3D%0A)
8. Click **Next**.
9. Once you've confirmed all your details, click **Add VXC** to update your ordering cart.

   [![VXC addition tab. ](https://downloads.intercomcdn.com/i/o/119818449/ba4867401742ec1ee96ea898/17.png?expires=1781167500&signature=488c1c97006a0c26bf4a02e771b8f39f137ca88656cb1346a2fba5431a36ab20&req=dSEuHsh2mYVWFb4f3HP0gJ35Qk%2F5y6uIeMFnOhZ4ezxW8z3%2BtWhhRNeTgOeY%0A%2F7M%3D%0A)](https://downloads.intercomcdn.com/i/o/119818449/ba4867401742ec1ee96ea898/17.png?expires=1781167500&signature=488c1c97006a0c26bf4a02e771b8f39f137ca88656cb1346a2fba5431a36ab20&req=dSEuHsh2mYVWFb4f3HP0gJ35Qk%2F5y6uIeMFnOhZ4ezxW8z3%2BtWhhRNeTgOeY%0A%2F7M%3D%0A)
10. When you're ready, view your cart and click on **Order**. This will send an email to Telnyx for approval. Once Telnyx approves your connection, this creates the VXC between your Megaport setup and Telnyx.

    [![Megaport configured services portal. ](https://downloads.intercomcdn.com/i/o/119818494/e66b2f502dd2f39afd7a99c8/18.png?expires=1781167500&signature=24d31afd239492339b9cdccf807f57abf977e5d8cd9d6b9750ae3d7a0af25491&req=dSEuHsh2mYhbFb4f3HP0gMmBiBUnMLMYwwWTHAyw3xLPTPv7hRFWrVcIdwQa%0AIko%3D%0A)](https://downloads.intercomcdn.com/i/o/119818494/e66b2f502dd2f39afd7a99c8/18.png?expires=1781167500&signature=24d31afd239492339b9cdccf807f57abf977e5d8cd9d6b9750ae3d7a0af25491&req=dSEuHsh2mYhbFb4f3HP0gMmBiBUnMLMYwwWTHAyw3xLPTPv7hRFWrVcIdwQa%0AIko%3D%0A)

That's it! You've finished configuring Megaport with Telnyx.

[Back to Top](#h_931a5218c3)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Megaport documentation](https://docs.megaport.com/)
* [Megaport support](https://docs.megaport.com/support/contact/)
* [Megaport resource center](https://www.megaport.com/resources/)

---

Related Articles

[Configuring a Vicidial IP trunk with Telnyx](https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx)[Configuring Grandstream GXP16XX with Telnyx](https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx)[Configuring Linphone with Telnyx](https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx)[Google VPC: Telnyx Integration](https://support.telnyx.com/en/articles/2239449-google-vpc-telnyx-integration)[Polycom: Setup with Telnyx](https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx)

Did this answer your question?

😞😐😃

Table of contents
