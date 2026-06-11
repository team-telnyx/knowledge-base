---
source_url: https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage
scraped: 2026-06-11
---

Use ExpanDrive with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use ExpanDrive with Telnyx Storage

Learn how to integrate ExpanDrive, a powerful cloud storage client, with Telnyx Storage for seamless access and management of your files.

Written by Telnyx Engineering

June 6, 2024

Table of contents

[ExpanDrive](https://www.expandrive.com/) is a versatile cloud storage client that allows you to mount cloud storage as a local drive on your computer. It provides a unified interface to access and manage files across multiple cloud storage providers, including Telnyx Storage. With ExpanDrive, you can easily navigate and interact with your Telnyx Storage files as if they were stored locally.

---

# **How to configure ExpanDrive to work with Telnyx Storage**

## Step 1

Download and install the latest version of ExpanDrive [here!](https://www.expandrive.com/desktop/)

## Step 2

Launch the ExpanDrive application click on **“ExpanDrive”** and then “**New Connection”.**  
​

[![ExpanDrive section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770445594/ee998d85fe28ebdb7f293b1a/Sh-K7kmIeGHkkP4eCBdwilXT-xPizYpZhclYJxDiQTz22_jF9e2lX4_WMFY8drOc1vJTBeswWmHCMLdkgX08sdINKQeiIhyFVs8JFFCpRgBArq5zwKKaGoRsPYCx_j2YXaNszhGoEIuD9mJF2voRjQ?expires=1781168400&signature=5a0379e55235d6b39c5b0695eb258ba976537716f96c718e4776e2f3ba73cb31&req=cycnEs17mIhbFb4f3HP0gBJN%2BH%2BSsRPwcPZXRttIQ%2F28Nc0bk26smfRF5kjx%0Agqfp7v0rzQUPMEGvdw%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770445594/ee998d85fe28ebdb7f293b1a/Sh-K7kmIeGHkkP4eCBdwilXT-xPizYpZhclYJxDiQTz22_jF9e2lX4_WMFY8drOc1vJTBeswWmHCMLdkgX08sdINKQeiIhyFVs8JFFCpRgBArq5zwKKaGoRsPYCx_j2YXaNszhGoEIuD9mJF2voRjQ?expires=1781168400&signature=5a0379e55235d6b39c5b0695eb258ba976537716f96c718e4776e2f3ba73cb31&req=cycnEs17mIhbFb4f3HP0gBJN%2BH%2BSsRPwcPZXRttIQ%2F28Nc0bk26smfRF5kjx%0Agqfp7v0rzQUPMEGvdw%3D%3D%0A)

## Step 3

Select **"Amazon S3"** from the list of storage options.  
​

[![Amazon s3 button. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770445600/c67a9c951f3eb44fa1a90476/1AbZmwEiSfOioXwxiQA4PW8xW7vj8juhLn_sQw2gN5yf44b2bpAOyrQce5mN1dspMcURiAgFMhHbU_oNsSNsTS3mE8fF8EOKzkpFlZe0vSxK4ByRZqf4wlNV4yiGODunhgzP-fgz56C8sLPDOoOdiA?expires=1781168400&signature=7649a4dd452e5c6d95d50f8cd0b42889d11042e8c94a10113ca00cf6be30ee87&req=cycnEs17m4FfFb4f3HP0gEaA1KeSY%2FM%2FxOvRDPIAmyQHaPTaxQkT3GaQL9y1%0AHF0lndbKOKAH5QY7ew%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770445600/c67a9c951f3eb44fa1a90476/1AbZmwEiSfOioXwxiQA4PW8xW7vj8juhLn_sQw2gN5yf44b2bpAOyrQce5mN1dspMcURiAgFMhHbU_oNsSNsTS3mE8fF8EOKzkpFlZe0vSxK4ByRZqf4wlNV4yiGODunhgzP-fgz56C8sLPDOoOdiA?expires=1781168400&signature=7649a4dd452e5c6d95d50f8cd0b42889d11042e8c94a10113ca00cf6be30ee87&req=cycnEs17m4FfFb4f3HP0gEaA1KeSY%2FM%2FxOvRDPIAmyQHaPTaxQkT3GaQL9y1%0AHF0lndbKOKAH5QY7ew%3D%3D%0A)

## Step 4

Fill in the storage options with the information below:

1. **Server:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
2. **Access Key:** Copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field.
3. **Secret Key:** You can type out anything you want here, as long as it doesn’t include spaces, quoting, or special characters of any kind.
4. **Custom Region:** Copy and paste the matching region from [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints). For example, if you chose the [https://us-central-1.telnyxstorage.com](https://us-central-1.telnyxstorage.com/) endpoint, you will use us-central-1 as the region.
5. **Nickname:** Use your nickname or whatever name you want.
6. **Bucket:** You can enter the bucket name on your Telnyx storage on leave it blank.
7. **Drive Letter:** Select the drive letter from your local storage. It could be any of the letters.  
   ​

   [![Storage options section. ](https://downloads.intercomcdn.com/i/o/888743947/4b19a2c90a85704e91658926/Screenshot+2023-11-20+at+12.00.09%E2%80%AFPM.jpg?expires=1781168400&signature=c704c62253e0dddda87a58b2e0498d66c50b3616b2386ed56d67de88b944cd2b&req=fCgvEc19lIVYFb4f3HP0gIyfgCjUDtOEkpVtjA1cRApW0%2Bl%2FUj8chlrdxU8P%0AbXM%3D%0A)](https://downloads.intercomcdn.com/i/o/888743947/4b19a2c90a85704e91658926/Screenshot+2023-11-20+at+12.00.09%E2%80%AFPM.jpg?expires=1781168400&signature=c704c62253e0dddda87a58b2e0498d66c50b3616b2386ed56d67de88b944cd2b&req=fCgvEc19lIVYFb4f3HP0gIyfgCjUDtOEkpVtjA1cRApW0%2Bl%2FUj8chlrdxU8P%0AbXM%3D%0A)

## Step 5

1. Click on the "**Save**" button to set up the connection. ExpanDrive will authenticate your Telnyx Storage account using the provided API Key.

Once the authentication is successful, you can access your Telnyx Storage files through the ExpanDrive interface, which will appear as a mounted drive on your computer.

[![Telnyx Storage files section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770445612/166f806fb6531eb62fc4a129/IVLkKwcOoPauWEk4V9XbYV62gjhKnchb3BTLR11prrkMLbruboErkFA7--5lU3UHk2DE6onbpD_bzoDtyzOLEp04bD8Esu62OusRISLdaXCaHyXw8YDHFt8gE41Ib2GchH8KqW7N9ViDnye9U1yD1Q?expires=1781168400&signature=0e5e4c409d4be2d4a73c3eb2e54907bbd2c4406d8d1cd5f3b1effb7a199c2038&req=cycnEs17m4BdFb4f3HP0gNs42hpsKJGCOAhjikYUA6m8gwkq%2Bg7Xprla29qu%0AR%2FxGxSJvDCquYIvqKA%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770445612/166f806fb6531eb62fc4a129/IVLkKwcOoPauWEk4V9XbYV62gjhKnchb3BTLR11prrkMLbruboErkFA7--5lU3UHk2DE6onbpD_bzoDtyzOLEp04bD8Esu62OusRISLdaXCaHyXw8YDHFt8gE41Ib2GchH8KqW7N9ViDnye9U1yD1Q?expires=1781168400&signature=0e5e4c409d4be2d4a73c3eb2e54907bbd2c4406d8d1cd5f3b1effb7a199c2038&req=cycnEs17m4BdFb4f3HP0gNs42hpsKJGCOAhjikYUA6m8gwkq%2Bg7Xprla29qu%0AR%2FxGxSJvDCquYIvqKA%3D%3D%0A)

---

**Additional Resources**

For more information on how to use ExpanDrive and its features, check out their [blog.](https://www.expandrive.com/)

---

Related Articles

[Use Cloudmounter with Telnyx Storage](https://support.telnyx.com/en/articles/8047914-use-cloudmounter-with-telnyx-storage)[Use ODrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage)[Use WebDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage)[Use NetDrive3 with Telnyx Storage](https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
