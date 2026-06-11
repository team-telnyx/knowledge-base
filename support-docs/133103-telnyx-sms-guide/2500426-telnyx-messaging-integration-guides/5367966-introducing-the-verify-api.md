---
source_url: https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api
scraped: 2026-06-11
---

Introducing the Verify API | Telnyx Help Center

[Skip to main content](#main-content)

# Introducing the Verify API

This article will explain how to set up Verify API to utilize within the Telnyx Portal.

Written by Telnyx Engineering

June 6, 2024

Table of contents

Verify API has reduced all of the unnecessary steps for sending 2FA codes to devices, making it easier than ever to secure login requests, confirm account changes, and authenticate devices.

It takes just two steps in our [portal](https://portal.telnyx.com/#/app/verify/profiles) to set up a 2FA profile with Telnyx Verify API.

* Step 1: Create a 2FA profile that contains the configurations for sending out two factor authentication codes.
* Step 2: Create a 2FA verification using the 2FA profile ID and the end user’s phone number.

To get started, you can access our in-depth [documentation](https://developers.telnyx.com/docs/identity/verify/quickstart) here. SDK updates on Python, Ruby, Node, PHP, Java, and .NET coming soon.

---

# **Creating Verify Profile**

To begin, navigate to your Telnyx admin portal and click on the **Verify** Icon as shown below.

[![Verify profiles page. ](https://downloads.intercomcdn.com/i/o/356078703/b88c0d75f9c64a901be17caf/image.png?expires=1781168400&signature=52e1080008ecbe0de15e3d4beadd509b1e551f1f5311eb487040eb2e4e9e6fce&req=dyUhFs52moFcFb4f3HP0gGvnGzab%2FOxKSHZQiJklFPS4dXCMsywIZR%2F67ZWf%0A2mzNSnYFKluCkkZoTw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/356078703/b88c0d75f9c64a901be17caf/image.png?expires=1781168400&signature=52e1080008ecbe0de15e3d4beadd509b1e551f1f5311eb487040eb2e4e9e6fce&req=dyUhFs52moFcFb4f3HP0gGvnGzab%2FOxKSHZQiJklFPS4dXCMsywIZR%2F67ZWf%0A2mzNSnYFKluCkkZoTw%3D%3D%0A)

On the page click on **New Verify Profile** icon**.**

[![Verify profile icon settings page. ](https://downloads.intercomcdn.com/i/o/356082297/fd1f0b83aa32ad459a420495/image.png?expires=1781168400&signature=993012b207b92d2bde8f9fcb67df6fe2220c9b4fda148c871c0b286346eed5a6&req=dyUhFsF8n4hYFb4f3HP0gCWK1jOEHyYMxkwcFOdiCzoeKwuSxY%2BN7GcerthB%0Azthf09Fw%2BL2maYYY%2Bg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/356082297/fd1f0b83aa32ad459a420495/image.png?expires=1781168400&signature=993012b207b92d2bde8f9fcb67df6fe2220c9b4fda148c871c0b286346eed5a6&req=dyUhFsF8n4hYFb4f3HP0gCWK1jOEHyYMxkwcFOdiCzoeKwuSxY%2BN7GcerthB%0Azthf09Fw%2BL2maYYY%2Bg%3D%3D%0A)

Enter your **Profile Name** and click **Create.** You have now made a **Verify Profile.**

[![Verify profile credentials page. ](https://downloads.intercomcdn.com/i/o/356085356/69e163e4f812620b9705a9ec/image.png?expires=1781168400&signature=cb661ac44b47b4cd80ee80a630ce513289874936f2425c115af47379e6271072&req=dyUhFsF7noRZFb4f3HP0gPGeeKwpx4mKI%2B5aCrQJtdQCIbIpKeKqcY2wYHv%2F%0AH9IoG%2BVZn3iTtn6YIQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/356085356/69e163e4f812620b9705a9ec/image.png?expires=1781168400&signature=cb661ac44b47b4cd80ee80a630ce513289874936f2425c115af47379e6271072&req=dyUhFsF7noRZFb4f3HP0gPGeeKwpx4mKI%2B5aCrQJtdQCIbIpKeKqcY2wYHv%2F%0AH9IoG%2BVZn3iTtn6YIQ%3D%3D%0A)

## **Creating Verify API**

To begin, navigate to your Telnyx admin portal and click on the **Verify** Icon as shown below.

[![Telnyx Admin portal. ](https://downloads.intercomcdn.com/i/o/356085356/69e163e4f812620b9705a9ec/image.png?expires=1781168400&signature=cb661ac44b47b4cd80ee80a630ce513289874936f2425c115af47379e6271072&req=dyUhFsF7noRZFb4f3HP0gPGeeKwpx4mKI%2B5aCrQJtdQCIbIpKeKqcY2wYHv%2F%0AH9IoG%2BVZn3iTtn6YIQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/356085356/69e163e4f812620b9705a9ec/image.png?expires=1781168400&signature=cb661ac44b47b4cd80ee80a630ce513289874936f2425c115af47379e6271072&req=dyUhFsF7noRZFb4f3HP0gPGeeKwpx4mKI%2B5aCrQJtdQCIbIpKeKqcY2wYHv%2F%0AH9IoG%2BVZn3iTtn6YIQ%3D%3D%0A)

Now enter the tab at the top of the page, **Learn & Build** to configure the **Verify API**.

[![Learn and Build tab. ](https://downloads.intercomcdn.com/i/o/356087783/289498c9ea80812136411d69/image.png?expires=1781168400&signature=be8180bac496bc214e7a5dd76edaffab8152cf864c276cdd1e830811e4c6ce3e&req=dyUhFsF5molcFb4f3HP0gOAIpTBFnQqEpPkLk3SICOdycgWgVt0coY%2FlYTwJ%0AtJb3YQSdHyiIxh2pYw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/356087783/289498c9ea80812136411d69/image.png?expires=1781168400&signature=be8180bac496bc214e7a5dd76edaffab8152cf864c276cdd1e830811e4c6ce3e&req=dyUhFsF5molcFb4f3HP0gOAIpTBFnQqEpPkLk3SICOdycgWgVt0coY%2FlYTwJ%0AtJb3YQSdHyiIxh2pYw%3D%3D%0A)

Check Step 1 to verify that the Verification Profile you have chosen is the correct profile. For example purposes we have chosen **TelnyxTest** as our Verification Profile. Once you have chosen your desired Verification Profile click **Next: Send a Verification Code** to proceed to Step 2.

[![Profile verification section of the Learn and Build tab. ](https://downloads.intercomcdn.com/i/o/356091529/11d2611aea809a0b770be7fe/image.png?expires=1781168400&signature=4ca6975ed007ff51dcb313d59b3fcce0bb56a717424358fe55a6415095647540&req=dyUhFsB%2FmINWFb4f3HP0gGqjC54QkS9Y%2BPTqRz9av%2BJo6b%2F5NW16c0r57vFu%0AoAL33C6LWUqFuN9USA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/356091529/11d2611aea809a0b770be7fe/image.png?expires=1781168400&signature=4ca6975ed007ff51dcb313d59b3fcce0bb56a717424358fe55a6415095647540&req=dyUhFsB%2FmINWFb4f3HP0gGqjC54QkS9Y%2BPTqRz9av%2BJo6b%2F5NW16c0r57vFu%0AoAL33C6LWUqFuN9USA%3D%3D%0A)

You will be presented with the following field:

* Fill in the **Phone Number Receipt** with the phone number you desire.

Once completed click on the icon **Send Verification Code** to send a verification to the desired phone number.

[![Verification code page. ](https://downloads.intercomcdn.com/i/o/356095770/94e238a4ea61e79f85f3c044/image.png?expires=1781168400&signature=8352057b76962ff4ca321329572ef9f4cfbf46555959a389b97723b7e9f3cd6a&req=dyUhFsB7moZfFb4f3HP0gK0ZtCWiFnMjX6dOdpNz%2B%2B5ZigDKJFW14sNkIKzs%0AMjCT9AZRh%2Burp%2BIfKw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/356095770/94e238a4ea61e79f85f3c044/image.png?expires=1781168400&signature=8352057b76962ff4ca321329572ef9f4cfbf46555959a389b97723b7e9f3cd6a&req=dyUhFsB7moZfFb4f3HP0gK0ZtCWiFnMjX6dOdpNz%2B%2B5ZigDKJFW14sNkIKzs%0AMjCT9AZRh%2Burp%2BIfKw%3D%3D%0A)

Now enter the received Verification Code into the following field and hit **Verify**. You have now sent and verified your first verification through Telnyx Verify API!

A detailed workflow including [expected API webhook responses is shown here](https://developers.telnyx.com/docs/identity/verify/quickstart).

## **Other general information relating to this API.**

**Verify API now offers Voice and Flash Call as channels for sending 2FA codes**

The new features supported are:

* Delivering a verification code through voice call
* Delivering a verification code through flash call
* Delivering a verification code specific to the PSD2 use case
* Specifying the language for a verification code delivered through voice call or SMS

With these new features, we introduced some changes to the verification API while doing our best to maintain backward compatibility. Users who have already integrated with the API should read the release notes carefully and make the appropriate planning to accommodate the changes.

---

Related Articles

[Account Verification](https://support.telnyx.com/en/articles/1130595-account-verification)[How to Sign Up for a Telnyx account](https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account)[Telnyx Verify: 2FA made easy](https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy)[Verified Numbers](https://support.telnyx.com/en/articles/6988813-verified-numbers)[How to Verify Phone Numbers behind an IVR](https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr)

Did this answer your question?

😞😐😃

Table of contents
