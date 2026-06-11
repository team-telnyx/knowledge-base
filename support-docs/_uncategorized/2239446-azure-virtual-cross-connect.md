---
source_url: https://support.telnyx.com/en/articles/2239446-azure-virtual-cross-connect
scraped: 2026-06-11
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

   [![The Azure portal interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831081/101181279d21e698c596fcc0/oBjhKBCL8Y7XFxdVbW1jE-bCv1Fu6NkQFct8_slLwRRIYZ0fd0D4iywWZ1Hc-SDwCb57TXi5a8D1jDEeATIykC8RhoP6YJ9Pv0jxUZsx9KyEOUEUNxmnw4oBbcW_-FcDhJz7-STbO8TpU38viw?expires=1781167500&signature=0e5ff65d623042495aa9d703cc1e4e8f86f6191f8df74187a7eab8988c841e4e&req=dSUnHsp%2FnYleFb4f3HP0gDKQRZVn1xTzpt%2F%2BnXbepmzDPT1A4LSyQAAShXfe%0A08Q%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831081/101181279d21e698c596fcc0/oBjhKBCL8Y7XFxdVbW1jE-bCv1Fu6NkQFct8_slLwRRIYZ0fd0D4iywWZ1Hc-SDwCb57TXi5a8D1jDEeATIykC8RhoP6YJ9Pv0jxUZsx9KyEOUEUNxmnw4oBbcW_-FcDhJz7-STbO8TpU38viw?expires=1781167500&signature=0e5ff65d623042495aa9d703cc1e4e8f86f6191f8df74187a7eab8988c841e4e&req=dSUnHsp%2FnYleFb4f3HP0gDKQRZVn1xTzpt%2F%2BnXbepmzDPT1A4LSyQAAShXfe%0A08Q%3D%0A)
2. ### **Perform a search for *express route* and click on *Express Route Circuits.***

   [![An open search tab for express route circuits. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831086/5ff07cb5d545fd2a0179962e/MK8lsNwx8omYx5HVoWX9hRxkpVM8-6CGiupriRIwSbgGQS8HBJQROo4nWBME7v4vtbuJGZWO28hR3EmpqM3fnlEiBofOFs4-qAV_rTyIia_qp_exuTWKeXnr36dyom_oz0ZCpKXhX8gjEhiPag?expires=1781167500&signature=01c2758a6287f2249431fe4e5df551fe06f8aa5d2c5155e4bdadaa0c07e9f56a&req=dSUnHsp%2FnYlZFb4f3HP0gCYMKx63LkzRgiNJbpCSZgAlWnhpE7SEUMu5P6DX%0AZAo%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831086/5ff07cb5d545fd2a0179962e/MK8lsNwx8omYx5HVoWX9hRxkpVM8-6CGiupriRIwSbgGQS8HBJQROo4nWBME7v4vtbuJGZWO28hR3EmpqM3fnlEiBofOFs4-qAV_rTyIia_qp_exuTWKeXnr36dyom_oz0ZCpKXhX8gjEhiPag?expires=1781167500&signature=01c2758a6287f2249431fe4e5df551fe06f8aa5d2c5155e4bdadaa0c07e9f56a&req=dSUnHsp%2FnYlZFb4f3HP0gCYMKx63LkzRgiNJbpCSZgAlWnhpE7SEUMu5P6DX%0AZAo%3D%0A)
3. ### **Click on Add -> Provider. This provider *must* be *Equinix*, *do \*NOT\** select *Allow Classic Operations*. Rename other fields at your discretion.**

   [![Provider addition tab. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831091/d1faa165b115c49c093cef54/rSqKeI10ErmqJ9Tt2AJ8cDSUisqED1inpuiM1Qd4qdPe39Z9mah_hwjASCTaR7zDwFFVdqtWKGGF7ZQhCyf5KG2WjqLi89kAQ3e69ZZgS7AmEKa3l0uJtFpbbMxk_KIzqMGWM-NNuNC_QMPahA?expires=1781167500&signature=fee6b8cb1927fedd7b91d96ce1525d0e475c5d549ee71b0f425d46334458c521&req=dSUnHsp%2FnYheFb4f3HP0gK980YWEsK%2BLqCkYivuM%2B%2Bqs7MpSUC7Rxtj68W9u%0AKNI%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831091/d1faa165b115c49c093cef54/rSqKeI10ErmqJ9Tt2AJ8cDSUisqED1inpuiM1Qd4qdPe39Z9mah_hwjASCTaR7zDwFFVdqtWKGGF7ZQhCyf5KG2WjqLi89kAQ3e69ZZgS7AmEKa3l0uJtFpbbMxk_KIzqMGWM-NNuNC_QMPahA?expires=1781167500&signature=fee6b8cb1927fedd7b91d96ce1525d0e475c5d549ee71b0f425d46334458c521&req=dSUnHsp%2FnYheFb4f3HP0gK980YWEsK%2BLqCkYivuM%2B%2Bqs7MpSUC7Rxtj68W9u%0AKNI%3D%0A)

   [![Microsoft Azure dashboard. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831095/387f16e82b2cec6d7d7bbb84/H8BjT1Sepv9rg6s6iz75_fEI27uAoI3WiNk3-BK3J-EE92qSTw6UCQrHVsjn2H0oJlcpdsU5FMLiljaIeMTkyiIonJ62UbxPoRPyZoEcqTjWQLJec6w7f2EoG6TvGLlf_G9bCJVJwbGbabEKJg?expires=1781167500&signature=c711d01031afb66da4414e05ef2cdf3129d3a463daff22d2c5aa4a475582ede9&req=dSUnHsp%2FnYhaFb4f3HP0gMfWQKD2FikvWvb%2F1%2F%2FlLyokXyUUauhmMk5pyOgy%0A%2FRY%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831095/387f16e82b2cec6d7d7bbb84/H8BjT1Sepv9rg6s6iz75_fEI27uAoI3WiNk3-BK3J-EE92qSTw6UCQrHVsjn2H0oJlcpdsU5FMLiljaIeMTkyiIonJ62UbxPoRPyZoEcqTjWQLJec6w7f2EoG6TvGLlf_G9bCJVJwbGbabEKJg?expires=1781167500&signature=c711d01031afb66da4414e05ef2cdf3129d3a463daff22d2c5aa4a475582ede9&req=dSUnHsp%2FnYhaFb4f3HP0gMfWQKD2FikvWvb%2F1%2F%2FlLyokXyUUauhmMk5pyOgy%0A%2FRY%3D%0A)
4. ### **Click OK.**
5. ### **Once the deployment completes, you will see your newly-provisioned Azure Express Route.**

   [![Newly-provisioned Azure express route.](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831097/03b2a5436e8ea16a394bca51/P_GdRhTZNEg_QIIqkFMzYJn1YlBRl0RgSJFX3ohxccxDug82gPNj2nP77RI2F-xZkGqoT9aDJhQOWV-UgxIuvEr9ob2ScoB3b7klOA-QlG86HdiQpNBklaik_XHbqA4RMbCvz4X3RLGlfmQLhA?expires=1781167500&signature=b69024f0215121171518b70480e2965db7d0826f8a4c04a1d259e8086ce7e4f7&req=dSUnHsp%2FnYhYFb4f3HP0gNExkbne%2BR1KKkN0%2F%2FcPY1AeuaatbMdcb7Cr%2Frhi%0AZ2c%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831097/03b2a5436e8ea16a394bca51/P_GdRhTZNEg_QIIqkFMzYJn1YlBRl0RgSJFX3ohxccxDug82gPNj2nP77RI2F-xZkGqoT9aDJhQOWV-UgxIuvEr9ob2ScoB3b7klOA-QlG86HdiQpNBklaik_XHbqA4RMbCvz4X3RLGlfmQLhA?expires=1781167500&signature=b69024f0215121171518b70480e2965db7d0826f8a4c04a1d259e8086ce7e4f7&req=dSUnHsp%2FnYhYFb4f3HP0gNExkbne%2BR1KKkN0%2F%2FcPY1AeuaatbMdcb7Cr%2Frhi%0AZ2c%3D%0A)

[Back to Top](#h_c4436070ec)

## 2. Set up the VXC in your Telnyx Mission Control Portal

1. ### **Log into your [Telnyx Mission Control Portal](https://portal.telnyx.com).**
2. ### **Click on "Networking" in the left-hand menu**

   [![Telnyx Mission Control Portal. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831098/42306168e0084fb90bba3778/RbhJiP_F1fbxftbxm7Ahk62i6m1rVjp4FcWFn7zlNQppIzh2FN2GYDWFHiwdv83iURaths6n26HhGcIaEDFtIoUt7ZuLLkfgWcQo9MVEdaQsipZtKTM_vwuvFosioaG5FDmeYqJKAXrcJe4ICg?expires=1781167500&signature=05a07a5cb8237ecb759cbfcaacf2c94ae1b3013c5661336c213f171f5d01716b&req=dSUnHsp%2FnYhXFb4f3HP0gKagVNVpRKffi5nxoSBDFsoaxl%2BqwZvRwmJPzIub%0ADPc%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831098/42306168e0084fb90bba3778/RbhJiP_F1fbxftbxm7Ahk62i6m1rVjp4FcWFn7zlNQppIzh2FN2GYDWFHiwdv83iURaths6n26HhGcIaEDFtIoUt7ZuLLkfgWcQo9MVEdaQsipZtKTM_vwuvFosioaG5FDmeYqJKAXrcJe4ICg?expires=1781167500&signature=05a07a5cb8237ecb759cbfcaacf2c94ae1b3013c5661336c213f171f5d01716b&req=dSUnHsp%2FnYhXFb4f3HP0gKagVNVpRKffi5nxoSBDFsoaxl%2BqwZvRwmJPzIub%0ADPc%3D%0A)
3. ### **Click on the "Create New Network" button on the top-right.**

   [!["Create New Network" button. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831099/c0f8c94d832ba0e9f03b8c5e/S9CcjxldjYDVhbkbqg7cEgB12TDEm4CW_jE9VtLCK78ya15N-LNWO0w1881LWisbMYsG4DnTNv0nzbaZgvu55svui36XZPkEO5ABMNn4DXlj3ilOY3sJTGdLmsfbALIBmPXz9dfKZKD80QcTMQ?expires=1781167500&signature=1f13f07af84b0471456b654c47bc564b5c7a0749b23d0256f6bed823722c5fee&req=dSUnHsp%2FnYhWFb4f3HP0gOwgRGnZN0uOonapSeVhStxpUJ%2F%2BJK173cdBKmIg%0AZRk%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831099/c0f8c94d832ba0e9f03b8c5e/S9CcjxldjYDVhbkbqg7cEgB12TDEm4CW_jE9VtLCK78ya15N-LNWO0w1881LWisbMYsG4DnTNv0nzbaZgvu55svui36XZPkEO5ABMNn4DXlj3ilOY3sJTGdLmsfbALIBmPXz9dfKZKD80QcTMQ?expires=1781167500&signature=1f13f07af84b0471456b654c47bc564b5c7a0749b23d0256f6bed823722c5fee&req=dSUnHsp%2FnYhWFb4f3HP0gOwgRGnZN0uOonapSeVhStxpUJ%2F%2BJK173cdBKmIg%0AZRk%3D%0A)
4. ### **Give your network a name and click on the "Create Network" button**

   [!["Create Network" button. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831101/8d25a68c94a67948f5dac811/wM4K-j0F65xhQNqktsrm25k93ApAdS2fRt-XIwiaZrkwlgd9hiX4XD42LI8FLOSeEuCa_BeCPc3wCnoftXBkngYNOPQa_YOaisGpzEzQ6o73ArFM40h5_nhm8YocbwSd9H2rNm0n9YnQvJ6wPg?expires=1781167500&signature=33ffe427a07c787e72eae6d994eeae8b3ad661cb01d53d725f452ac15146d501&req=dSUnHsp%2FnIFeFb4f3HP0gGcdJ98NuVLXyRq%2BzM0kPwW4DpodBWByLlc5fyd5%0AHsc%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831101/8d25a68c94a67948f5dac811/wM4K-j0F65xhQNqktsrm25k93ApAdS2fRt-XIwiaZrkwlgd9hiX4XD42LI8FLOSeEuCa_BeCPc3wCnoftXBkngYNOPQa_YOaisGpzEzQ6o73ArFM40h5_nhm8YocbwSd9H2rNm0n9YnQvJ6wPg?expires=1781167500&signature=33ffe427a07c787e72eae6d994eeae8b3ad661cb01d53d725f452ac15146d501&req=dSUnHsp%2FnIFeFb4f3HP0gGcdJ98NuVLXyRq%2BzM0kPwW4DpodBWByLlc5fyd5%0AHsc%3D%0A)
5. ### **Once the Network is Created, Next step is to add the site. Click on the "Add a Site" button.**

   [!["Add a site" button. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831105/50cc32927d306a510bcf24e5/RmiwTzKNtrFQFk0c-M6P1cEIC51tumxzfczZ_rkRoh0qK1MvdcIYQRsB5w4S8w6iLtAThRLrdzX2pB-crxU5beHXGEgArbtQFGhOEGBzdmwddgbVtr8qwdvfHiKYs-HxgvI84U65KYo7r6dqtg?expires=1781167500&signature=c3121b402a4e133d80463a6b04dde9e601da8597d9dcef12f1c8e54d67df7d50&req=dSUnHsp%2FnIFaFb4f3HP0gHndTxAkUEIjVExgn9QL7bcnPeVQn%2BrL42Mfc1tY%0AG9E%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831105/50cc32927d306a510bcf24e5/RmiwTzKNtrFQFk0c-M6P1cEIC51tumxzfczZ_rkRoh0qK1MvdcIYQRsB5w4S8w6iLtAThRLrdzX2pB-crxU5beHXGEgArbtQFGhOEGBzdmwddgbVtr8qwdvfHiKYs-HxgvI84U65KYo7r6dqtg?expires=1781167500&signature=c3121b402a4e133d80463a6b04dde9e601da8597d9dcef12f1c8e54d67df7d50&req=dSUnHsp%2FnIFaFb4f3HP0gHndTxAkUEIjVExgn9QL7bcnPeVQn%2BrL42Mfc1tY%0AG9E%3D%0A)
6. ### **Choose the Telnyx Backbone Network you want to peer with.**

   [![Telnyx Backbone Network selection table. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831113/086dd01be5478d32d2db447c/djt8lB0KTTLmbmS1P2J_zelT6zYE1Ku2q4H_cpxvYEoTGWhNxZJYGQIOVu1fxfoIE5C3WwLnDMGtI2g8r76oX2G3ko-HYWFiaMOqVpUCRvwlV9r5x9lclAu96rzjK62cjTMGFJCuPYsJDq3V8g?expires=1781167500&signature=53ee7a24aed4aca3841ad596e2f7b44f189f1274c7cd9fbce49f2b3f73bd3f8f&req=dSUnHsp%2FnIBcFb4f3HP0gBSqw3Lwf02JgTwWwQyJm0%2Fbz1inQUGCmHLlXiXv%0AJws%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831113/086dd01be5478d32d2db447c/djt8lB0KTTLmbmS1P2J_zelT6zYE1Ku2q4H_cpxvYEoTGWhNxZJYGQIOVu1fxfoIE5C3WwLnDMGtI2g8r76oX2G3ko-HYWFiaMOqVpUCRvwlV9r5x9lclAu96rzjK62cjTMGFJCuPYsJDq3V8g?expires=1781167500&signature=53ee7a24aed4aca3841ad596e2f7b44f189f1274c7cd9fbce49f2b3f73bd3f8f&req=dSUnHsp%2FnIBcFb4f3HP0gBSqw3Lwf02JgTwWwQyJm0%2Fbz1inQUGCmHLlXiXv%0AJws%3D%0A)
7. ### **Add the VXC, by clicking on "Create VXC".**

   [!["Create VXC" add button. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831119/1ada1fac6c852f2357e04fde/gv1p-4ptKLBeX2vl81wTlhlFl5ZPKX6W_Q2Gj9R7k8kftKdAS6EdIIAmVCzm8DC2-_w5ZqGBVXevJjhXkr2RRimMPSce7sH4H2WhVc3g0R6sDw9Jx0_j8gMh1vq_LOTLzfR0pV9HNXjhFbLhHw?expires=1781167500&signature=f71fc0ac700aee9e6f949f50bb2c45bdf691a451f52fb1c4f7e6b54ca30a483f&req=dSUnHsp%2FnIBWFb4f3HP0gCc78VyDExp54PCvLiaA5dnURy49k2KvIcxpP850%0AA68%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831119/1ada1fac6c852f2357e04fde/gv1p-4ptKLBeX2vl81wTlhlFl5ZPKX6W_Q2Gj9R7k8kftKdAS6EdIIAmVCzm8DC2-_w5ZqGBVXevJjhXkr2RRimMPSce7sH4H2WhVc3g0R6sDw9Jx0_j8gMh1vq_LOTLzfR0pV9HNXjhFbLhHw?expires=1781167500&signature=f71fc0ac700aee9e6f949f50bb2c45bdf691a451f52fb1c4f7e6b54ca30a483f&req=dSUnHsp%2FnIBWFb4f3HP0gCc78VyDExp54PCvLiaA5dnURy49k2KvIcxpP850%0AA68%3D%0A)
8. ### **Create an Azure Express Route.**

   #### Note that in order to complete this section, Stage 1 needs to have been completed.

   [![Azure Express Route creation portal. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831125/2959bda66baa6a50eb52d6fd/NEOGMM0fs4-ZEBoCQaiQACGp2YD0SRSznShjYkYsu17lePbikTaS6RSLSqmuWATog6v5sUlUa--Wst_7H_XirTc7ul4MrBW8StJe-QdYEERQU82HOh7A1LWlJaK3CRkaQ9X4s2bdJ40SD_6X9w?expires=1781167500&signature=561b4e02f63af0d99df64ca22360d7d9d96857e59a200c991c8d63eb44537991&req=dSUnHsp%2FnINaFb4f3HP0gIEg6Lb6jw5VLDn3kiXTQIj8PgQfyYRl9t0gR%2Bfg%0Ard0%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831125/2959bda66baa6a50eb52d6fd/NEOGMM0fs4-ZEBoCQaiQACGp2YD0SRSznShjYkYsu17lePbikTaS6RSLSqmuWATog6v5sUlUa--Wst_7H_XirTc7ul4MrBW8StJe-QdYEERQU82HOh7A1LWlJaK3CRkaQ9X4s2bdJ40SD_6X9w?expires=1781167500&signature=561b4e02f63af0d99df64ca22360d7d9d96857e59a200c991c8d63eb44537991&req=dSUnHsp%2FnINaFb4f3HP0gIEg6Lb6jw5VLDn3kiXTQIj8PgQfyYRl9t0gR%2Bfg%0Ard0%3D%0A)

   ​
9. ### **Key in Azure Service Key and Microsoft Azure ASN. Typically it is 12076**

   [![Azure Service Key and Microsoft Azure ASN credentials input. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831127/caaf30ec0d070d0bd0f48757/52HTnuPtkaOtFLrtT4T_hday0F-HSM02PeqmsP4sCPHCUgEEPZuC2hwELTXtkCYleQW-7PwrNY7krBioQVbe4_S-GONOr7saYWU6VmJLFA7IQctbG1uIrGFJBNBbcLzxHasP-KRtdDGrEilWWQ?expires=1781167500&signature=2d733038e61ae7f39bee1c344561299f600c344adf0712b0c185c8dba07d16b0&req=dSUnHsp%2FnINYFb4f3HP0gG%2B8mgwLwEtNVOWTwCRaR2cs3%2FifNb4zIlrLUMGi%0AQNQ%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831127/caaf30ec0d070d0bd0f48757/52HTnuPtkaOtFLrtT4T_hday0F-HSM02PeqmsP4sCPHCUgEEPZuC2hwELTXtkCYleQW-7PwrNY7krBioQVbe4_S-GONOr7saYWU6VmJLFA7IQctbG1uIrGFJBNBbcLzxHasP-KRtdDGrEilWWQ?expires=1781167500&signature=2d733038e61ae7f39bee1c344561299f600c344adf0712b0c185c8dba07d16b0&req=dSUnHsp%2FnINYFb4f3HP0gG%2B8mgwLwEtNVOWTwCRaR2cs3%2FifNb4zIlrLUMGi%0AQNQ%3D%0A)

   #### **You can see a sample Service Key and ASN Displayed Below**

   [![Sample Service Key and ASN display. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831131/ed94343917d218797d7418fb/NA_5F_1mqUBvMVlGXHH36HJpCwBq1FzP0dMsc7eJ2uXViIsT7izeTRMniHurG8NtdbSBFa4qMLhEmDgPC8v6Bg06aazYv4URav09uh2Mbtcx7qeU-s4kk1GEhCipuHI6om2lnnC8KlzpYjWw0w?expires=1781167500&signature=7e1b9b20b57a29024a9ae68cfb4b0ca073a76528ef701c9082e7b43c9ce57dbe&req=dSUnHsp%2FnIJeFb4f3HP0gNMoHTBVcKNYH3crgZVBpxNguBJ2nVCPTcdJTe9p%0A%2B3I%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831131/ed94343917d218797d7418fb/NA_5F_1mqUBvMVlGXHH36HJpCwBq1FzP0dMsc7eJ2uXViIsT7izeTRMniHurG8NtdbSBFa4qMLhEmDgPC8v6Bg06aazYv4URav09uh2Mbtcx7qeU-s4kk1GEhCipuHI6om2lnnC8KlzpYjWw0w?expires=1781167500&signature=7e1b9b20b57a29024a9ae68cfb4b0ca073a76528ef701c9082e7b43c9ce57dbe&req=dSUnHsp%2FnIJeFb4f3HP0gNMoHTBVcKNYH3crgZVBpxNguBJ2nVCPTcdJTe9p%0A%2B3I%3D%0A)
10. ### **Now create your VXC and submit it to Telnyx Network team.**

    [![VXC creation portal and submission button. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831133/f8f96c966e2de25647d94f9c/bN85CrNqmAzB8yrnarnIKqMl_APGXo57iSg5-r5rwtlV0OGRYiQz-lRjZsRBINwkQdnJG7d4w2sLZle5sh2_SfBKQONHupJXzox_PLa6WjqruNMIUzQRUraeeK8zfgUWd-JuhvvBGWFiJRSoAg?expires=1781167500&signature=b164c51c8a31370f4b7a2e8c6a56e3493c0640e700d1dc2b57ad25cf4cbe37e7&req=dSUnHsp%2FnIJcFb4f3HP0gD0gMr4eSaBvnHaX05Q6wAqF%2F7yMlb0gctxMc8aJ%0Amwc%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831133/f8f96c966e2de25647d94f9c/bN85CrNqmAzB8yrnarnIKqMl_APGXo57iSg5-r5rwtlV0OGRYiQz-lRjZsRBINwkQdnJG7d4w2sLZle5sh2_SfBKQONHupJXzox_PLa6WjqruNMIUzQRUraeeK8zfgUWd-JuhvvBGWFiJRSoAg?expires=1781167500&signature=b164c51c8a31370f4b7a2e8c6a56e3493c0640e700d1dc2b57ad25cf4cbe37e7&req=dSUnHsp%2FnIJcFb4f3HP0gD0gMr4eSaBvnHaX05Q6wAqF%2F7yMlb0gctxMc8aJ%0Amwc%3D%0A)

    #### Connection acceptance will be TELNYX Network Team.

    [![Routing and NAT configuration interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831138/1d28a23b0d34b75d29bb100b/3STyQbErQiL61P3ZxTkatKiuC-vHtfo-qnVMXyD5hPu--HZ6kdSONTH3dj1KZB9aDRn4qcJz5PTEJvTgJ3aP3wW4zPXIbxkNU1lcjcdPoeHm_QPkd3UnHsWTipKtAlyx6TiQTGR04gGw2AaN1g?expires=1781167500&signature=28fd5724e5ddea7a7eefbad644ec6a9d977ffdebfe900539b08c972433771173&req=dSUnHsp%2FnIJXFb4f3HP0gBhpI0Pz0nwoYD%2FWNLkHyxANs5MEvs%2BY6MTa1Ssc%0Azbg%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831138/1d28a23b0d34b75d29bb100b/3STyQbErQiL61P3ZxTkatKiuC-vHtfo-qnVMXyD5hPu--HZ6kdSONTH3dj1KZB9aDRn4qcJz5PTEJvTgJ3aP3wW4zPXIbxkNU1lcjcdPoeHm_QPkd3UnHsWTipKtAlyx6TiQTGR04gGw2AaN1g?expires=1781167500&signature=28fd5724e5ddea7a7eefbad644ec6a9d977ffdebfe900539b08c972433771173&req=dSUnHsp%2FnIJXFb4f3HP0gBhpI0Pz0nwoYD%2FWNLkHyxANs5MEvs%2BY6MTa1Ssc%0Azbg%3D%0A)

|  |
| --- |
| ***IMPORTANT:*** *Do NOT Enable Routing status via the slider, this step has to be coordinated in sync with Telnyx Network Team, as enabling this without Backend configuration may blackhole your voice traffic.* |

[Back to Top](#h_c4436070ec)

## 3. Turning up Routing and NAT configuration

1. Arrange a Maintenance activity and co-ordinate with TELNYX Network engineering to turn on the Routing. Please [contact our Support Team](https://telnyx.com/contact-us) to assist with this.   
   ​  
   ​***Note:*** *This activity has to be co-ordinate with the Network team to complete Back-end configuration during the Maintenance window.*
2. Once you enable the circuit using the Routing Status slider, you should see a routing table in Express Route similar to the following:

   [![Routing and NAT configuration interface. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831140/a514826b54b95264e18c0c24/hh0Crt_yHGArKuxmJbd06JpDqqCnEQvI1LMlfs63xD2TsrCjHU5rtSoAgK9dzig4MaIknKzsbYekVI69eWUetyL3U4F4_L1XVSQ-7bmP1hpozdOMoWiKVczUkWioxQGtDBBJY0p_Z4pFhhZK7A?expires=1781167500&signature=23f00b296103e7ad1037f32c8a1163cd245864cfc556b2998fb1ff712cabcf7d&req=dSUnHsp%2FnIVfFb4f3HP0gPcayNNY7lUkka6SpPshvso9midfQwYBvGO%2FHtLU%0Az80%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831140/a514826b54b95264e18c0c24/hh0Crt_yHGArKuxmJbd06JpDqqCnEQvI1LMlfs63xD2TsrCjHU5rtSoAgK9dzig4MaIknKzsbYekVI69eWUetyL3U4F4_L1XVSQ-7bmP1hpozdOMoWiKVczUkWioxQGtDBBJY0p_Z4pFhhZK7A?expires=1781167500&signature=23f00b296103e7ad1037f32c8a1163cd245864cfc556b2998fb1ff712cabcf7d&req=dSUnHsp%2FnIVfFb4f3HP0gPcayNNY7lUkka6SpPshvso9midfQwYBvGO%2FHtLU%0Az80%3D%0A)

### **Once enabled with Routing, you'll see Telnyx public ranges via Express Route Circuit. This will ensure that these are preferred over the Internet Routing Table.**

[![Routing table display. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831143/52c2d1df5b9fdd4522eb5840/wcBpJ0bOqeqr26q2pEZnnJGtX9ceBEXSyLp2tKvQv0TnH_K1-8t-S4_Ni0tksjOnZ6OkhR6j2OulH251GTKRpL3Jg9jRAAvJhTdVgDNjuqlIpM9hKk1NQn9PTzmy8LiwZCoY2gKuO5z9PVc-qg?expires=1781167500&signature=41d9b1904f2e9860c292495b3619dac48436e95154a7196fe6275b5fcc1fb02a&req=dSUnHsp%2FnIVcFb4f3HP0gFX4BVYO1JSJUtGWzMmXgXrqHucNxpTuMqdCu3Cv%0Aejh5XuLRwBqwoozaRQ%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/150831143/52c2d1df5b9fdd4522eb5840/wcBpJ0bOqeqr26q2pEZnnJGtX9ceBEXSyLp2tKvQv0TnH_K1-8t-S4_Ni0tksjOnZ6OkhR6j2OulH251GTKRpL3Jg9jRAAvJhTdVgDNjuqlIpM9hKk1NQn9PTzmy8LiwZCoY2gKuO5z9PVc-qg?expires=1781167500&signature=41d9b1904f2e9860c292495b3619dac48436e95154a7196fe6275b5fcc1fb02a&req=dSUnHsp%2FnIVcFb4f3HP0gFX4BVYO1JSJUtGWzMmXgXrqHucNxpTuMqdCu3Cv%0Aejh5XuLRwBqwoozaRQ%3D%3D%0A)

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
