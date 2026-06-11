---
source_url: https://support.telnyx.com/en/articles/8006189-port-out-pin-protection
scraped: 2026-06-11
---

Port Out PIN Protection | Telnyx Help Center

[Skip to main content](#main-content)

# Port Out PIN Protection

This article explains how to properly set up Port Out PIN protection on your account

Written by Patrick Budzinski

March 20, 2025

Table of contents

The purpose of this article is to provide an overview of the Port Out PIN Settings found in the [Telnyx Portal](https://portal.telnyx.com/#/app/home) along with a brief description of all the options available:

* What happens if I enable Port Out PIN Protection?
* Enabling PIN Protection and Setting Your Default PIN for Phone Numbers
* Individual PIN Settings
* Applicable Port Out Orders vs. Non-applicable Port Out Orders

# **What happens if I enable Port Out PIN Protection?**

When a Port Out request is created, the PIN provided by the losing carrier will be validated against your account settings. If the PIN matches your Port Out PIN, the order will be successfully created and sent to you, exactly like before, for review. If the Port Out PIN does not match your settings (or is not provided), the order will be automatically rejected. You will be able to view auto-rejected orders on the [Port Out Requests](https://portal.telnyx.com/#/app/numbers/port-outs) page in the Mission Control Portal.

By default, this feature is turned off for your account. If you leave this feature toggled off, no PIN validation will occur on your Port Out Requests.

## **Enabling PIN Protection and Setting Your Default PIN for Phone Numbers**

[![Breaking Line](https://downloads.intercomcdn.com/i/o/226386386/3c4f259763c3dcf431d063f0/line.png?expires=1781168400&signature=7e14382c855e9142f171398878f64835d8a158d1230881a6cc5084a57644568a&req=diIhFcF4nolZFb4f3HP0gKpZ4b%2BSF%2Bt2pS0%2FD2ArTrsj8xyqjwDUt%2FrgJ1Ss%0Acx7NuiVyrIbEVp%2B5Dw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/226386386/3c4f259763c3dcf431d063f0/line.png?expires=1781168400&signature=7e14382c855e9142f171398878f64835d8a158d1230881a6cc5084a57644568a&req=diIhFcF4nolZFb4f3HP0gKpZ4b%2BSF%2Bt2pS0%2FD2ArTrsj8xyqjwDUt%2FrgJ1Ss%0Acx7NuiVyrIbEVp%2B5Dw%3D%3D%0A)

In the top right, select your profile, and select `Account Settings` (link [here](https://portal.telnyx.com/#/app/account/general)).

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1432802584/42ade9ca88805aac652f710e65f6/image.png?expires=1781168400&signature=47dcf8fabb0ff0a1875e3c61cc062b2ce03696cfe2df29a3c9de072e806f936a&req=dSQkFMF%2Bn4RXXfMW1HO4zUuWM50yHvIM66W57vD2%2BXNvvqHfWJlhF5brRCtG%0AAkrnK3EyZxWLw2H8oKE%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1432802584/42ade9ca88805aac652f710e65f6/image.png?expires=1781168400&signature=47dcf8fabb0ff0a1875e3c61cc062b2ce03696cfe2df29a3c9de072e806f936a&req=dSQkFMF%2Bn4RXXfMW1HO4zUuWM50yHvIM66W57vD2%2BXNvvqHfWJlhF5brRCtG%0AAkrnK3EyZxWLw2H8oKE%3D%0A)

Once the web page updates, please ensure that you select `Security`

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1432803417/9c05e60ce0918984e9163249e7e1/image.png?expires=1781168400&signature=fca393d5a20da7d53260985b472d33b681566a2e04ad218cf1ffe9b9476b72fc&req=dSQkFMF%2BnoVeXvMW1HO4zUrJDcvAqcaVBjjR1NkU7E0PG5%2BSQWjlEN0kM9yc%0AxImDesyJa0JDju%2FEx8k%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1432803417/9c05e60ce0918984e9163249e7e1/image.png?expires=1781168400&signature=fca393d5a20da7d53260985b472d33b681566a2e04ad218cf1ffe9b9476b72fc&req=dSQkFMF%2BnoVeXvMW1HO4zUrJDcvAqcaVBjjR1NkU7E0PG5%2BSQWjlEN0kM9yc%0AxImDesyJa0JDju%2FEx8k%3D%0A)

Scroll down to the `Security` section on the page. You should see:

* `Default PIN for Phone Numbers`: This is the account level port out pin. Assuming you have port out pins enabled and you do not have a unique Port Out PIN associated with a phone number (more on that in the `Individual PIN Settings` section of this guide), this pin will apply for Port Out PIN validation.
* `Enable Port out Pins`: You can toggle on or off Port Out PIN validation for your account. By default, this feature is toggled off for all accounts.

[![Default Pin section on the mission control portal. ](https://downloads.intercomcdn.com/i/o/762869979/6e9863e6e987791c5eb084ff/Screenshot+2023-06-13+at+3.47.08+PM.png?expires=1781168400&signature=890498d3242db3ed35e80c96d680da7218a6aa4017b544171effd664ab2f04e6&req=cyYlHs93lIZWFb4f3HP0gNs78MpvHZ%2BfoWu2neqyB0LTDRvLDf1135Y3eUU5%0Ajvanfn9DxRqR86CMxQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/762869979/6e9863e6e987791c5eb084ff/Screenshot+2023-06-13+at+3.47.08+PM.png?expires=1781168400&signature=890498d3242db3ed35e80c96d680da7218a6aa4017b544171effd664ab2f04e6&req=cyYlHs93lIZWFb4f3HP0gNs78MpvHZ%2BfoWu2neqyB0LTDRvLDf1135Y3eUU5%0Ajvanfn9DxRqR86CMxQ%3D%3D%0A)

**NOTE:** Port-out PIN protection is available for on-net US numbers only. Customers that use PIN protection must adhere to all Telnyx and FCC rules related to PINS, including that any service provider must provide the PIN to its end users/resellers, to ensure that legitimate port outs are not blocked. Accordingly, Customer agrees to immediately provide the PIN to its customers/end-user/resellers. PIN Protection service may be immediately revoked by Telnyx if Customer does not follow these rules, or if Customer otherwise abuses the process to prevent legitimate port-outs. By using PIN protection, Customer accepts all liability for any claims that Customer has violated any rules relating to port-outs or the law.

## **Individual PIN Settings**

You can specify Port Out PINs for individual phone numbers. To update the Port Out PIN for a particular phone number:

1. Go to the [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers-beta) page in the Portal
2. On the right side of the table underneath the `Actions` header, click on the `Edit` icon for the phone number you wish to update  
   ​

   [![Actions section on the mission control portal. ](https://downloads.intercomcdn.com/i/o/762874921/99c535e1cfcc093dbf797ee2/Screenshot+2023-06-13+at+3.50.41+PM.png?expires=1781168400&signature=6313dd171b7d8867bc2f0d799b7537e6801e4a494e2b5837930fabea98c6a725&req=cyYlHs56lINeFb4f3HP0gC2vA9XTE%2BgtH3ENWCvmu0cGqEqFo0tKtAQEotpI%0A06A%3D%0A)](https://downloads.intercomcdn.com/i/o/762874921/99c535e1cfcc093dbf797ee2/Screenshot+2023-06-13+at+3.50.41+PM.png?expires=1781168400&signature=6313dd171b7d8867bc2f0d799b7537e6801e4a494e2b5837930fabea98c6a725&req=cyYlHs56lINeFb4f3HP0gC2vA9XTE%2BgtH3ENWCvmu0cGqEqFo0tKtAQEotpI%0A06A%3D%0A)
3. On the `Settings` tab, scroll down to the `Porting` section. If there is no value for `PIN`, then the default account PIN is applied (see section above `Setting your Default PIN for Phone Numbers`  
   ​

   [![Porting section on the mission control portal. ](https://downloads.intercomcdn.com/i/o/762540829/62ba72d69d734a74f8dff789/image.png?expires=1781168400&signature=12dfd5eb1ea8540ce3bc843f06ea62a543e8bd1dfa6d38dd801ddb21e0379df0&req=cyYlE81%2BlYNWFb4f3HP0gFBRifQJT6KJAasnLsfg0BcuxR47rXq9hJGuM4ez%0ADac%3D%0A)](https://downloads.intercomcdn.com/i/o/762540829/62ba72d69d734a74f8dff789/image.png?expires=1781168400&signature=12dfd5eb1ea8540ce3bc843f06ea62a543e8bd1dfa6d38dd801ddb21e0379df0&req=cyYlE81%2BlYNWFb4f3HP0gFBRifQJT6KJAasnLsfg0BcuxR47rXq9hJGuM4ez%0ADac%3D%0A)
4. To update the PIN for that specific phone number, enter in the code in the `PIN` field and click `Save Changes` at the bottom of the page  
   ​

   [![PIN section on the mission control portal. ](https://downloads.intercomcdn.com/i/o/762877026/a065d2e2960814489b83491d/Screenshot+2023-06-13+at+3.57.54+PM.png?expires=1781168400&signature=1422e45e203f70e90acbf75d42729cf306da93e0892f7dc63cbce7c4d235a025&req=cyYlHs55nYNZFb4f3HP0gNDHDaf9mSv2OU%2F1rnwrjqnIJNeESlM4SUBKe%2BM6%0AlUM%3D%0A)](https://downloads.intercomcdn.com/i/o/762877026/a065d2e2960814489b83491d/Screenshot+2023-06-13+at+3.57.54+PM.png?expires=1781168400&signature=1422e45e203f70e90acbf75d42729cf306da93e0892f7dc63cbce7c4d235a025&req=cyYlHs55nYNZFb4f3HP0gNDHDaf9mSv2OU%2F1rnwrjqnIJNeESlM4SUBKe%2BM6%0AlUM%3D%0A)

**Note**: This will only update the PIN for the currently selected number. If nothing is provided, the default account level Port Out PIN will be used.

## **Applicable Port Out Orders vs. Non-applicable Port Out Orders**

[![Port Out Requests section on the mission control portal. ](https://downloads.intercomcdn.com/i/o/762552460/66bb33c7ccd809dfb59dd4af/image.png?expires=1781168400&signature=f01aab7e6ea8c0ec05d0bb542e10d0377454a5621fa6bd5a6028bc4921c39ffa&req=cyYlE8x8mYdfFb4f3HP0gIXtELUmvPz5JolaMh8cvNY7Wt9fCGlywSCLhAuM%0AeLSzo2WZEt6cRbMq2Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/762552460/66bb33c7ccd809dfb59dd4af/image.png?expires=1781168400&signature=f01aab7e6ea8c0ec05d0bb542e10d0377454a5621fa6bd5a6028bc4921c39ffa&req=cyYlE8x8mYdfFb4f3HP0gIXtELUmvPz5JolaMh8cvNY7Wt9fCGlywSCLhAuM%0AeLSzo2WZEt6cRbMq2Q%3D%3D%0A)

Please note that Port Out PIN protection is available for on-net US numbers only. As a Port Out request is created for your account, you will notice a new column titled `PIN Validation` listing either `Eligible` or `Non-Eligible`. PIN validation will only occur on `Eligible` Port Out requests.

---

Related Articles

[I Received a Port-Out Notification](https://support.telnyx.com/en/articles/2030667-i-received-a-port-out-notification)[Port your Microsoft MS Teams Numbers](https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers)[Port away from voip.ms](https://support.telnyx.com/en/articles/5595770-port-away-from-voip-ms)[Porting away from Skype](https://support.telnyx.com/en/articles/10715399-porting-away-from-skype)[Porting Numbers Away from Aircall to Telnyx](https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx)

Did this answer your question?

😞😐😃

Table of contents
