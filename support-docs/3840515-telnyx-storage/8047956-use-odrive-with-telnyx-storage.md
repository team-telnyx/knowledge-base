---
source_url: https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage
scraped: 2026-06-11
---

Use ODrive with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use ODrive with Telnyx Storage

Learn how to set up ODrive, a synchronization tool, with Telnyx Storage for seamless integration and synchronization of your files.

Written by Telnyx Engineering

June 6, 2024

Table of contents

[ODrive](https://www.odrive.com/) is a powerful synchronization tool that allows users to easily sync and access files across multiple devices and cloud storage services. It supports a wide range of cloud storage providers, including [Telnyx Storage](https://telnyx.com/products/cloud-storage), enabling you to integrate and synchronize your files effortlessly.

---

# **How to configure ODrive to work with Telnyx Storage**

## Step 1

Download and install the latest version of ODrive from [here!](https://docs.odrive.com/docs/odrive-usage-guide#install-desktop-sync)

## Step 2

Launch the application and click **"Link Storage"** to add Telnyx Storage as a storage provider.  
​

[![Link storage section. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770447782/2a3977986f8d3f29932c38f4/Wjm1wo1zvrl7Gca2nZ7XtGRoJJFtdcGPJvzEIfxvB8MYeFUZjIOeBIf6czs_S8x0wFtoSqqIGCJjHeHlVfotG6L5NEp18XbPaFMwBt1-YrfgGlDb_u5ll78xlK_bDEoxFESrEAolvyt230tsZSCClg?expires=1781168400&signature=47d592f60c87e757121c680af5d5ff96476f55eaa2e308a0bc790fda4906ea5b&req=cycnEs15moldFb4f3HP0gNXRh6xi4jzYOW8vxMtnw03ksm%2BrhEnC884J2Tw4%0Aegms9PUphxJNimLOpQ%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770447782/2a3977986f8d3f29932c38f4/Wjm1wo1zvrl7Gca2nZ7XtGRoJJFtdcGPJvzEIfxvB8MYeFUZjIOeBIf6czs_S8x0wFtoSqqIGCJjHeHlVfotG6L5NEp18XbPaFMwBt1-YrfgGlDb_u5ll78xlK_bDEoxFESrEAolvyt230tsZSCClg?expires=1781168400&signature=47d592f60c87e757121c680af5d5ff96476f55eaa2e308a0bc790fda4906ea5b&req=cycnEs15moldFb4f3HP0gNXRh6xi4jzYOW8vxMtnw03ksm%2BrhEnC884J2Tw4%0Aegms9PUphxJNimLOpQ%3D%3D%0A)

## Step 3

In the "Link Storage" window, select locate **"Amazon S3/S3 Compatible"** from the list of available storage providers. Click on it to proceed.  
​

[![Various storage choices. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770447783/e8e33f70db8f96d3bde9262c/bkFMij429o2GEqadB5HkUBGdiglfLYnzrP0YUNaFkbRMOahrKg7ju_l_D8XU-4znbP6Ou9_rqa5cj6Eg_vbFKj6fDqiVwB-IOvS5mK-5l21zxIeKEdfbQUCwcFjdWZjxBN5kgecjI68mw2tvGqHORA?expires=1781168400&signature=02a78b54b4c7cccf5ce72084c1c45cba1512639070a4d16cddd513b563188348&req=cycnEs15molcFb4f3HP0gF4DKIVTibA283fQ1k0iUDRwaHoeDk0pX1ScE4Aa%0ABE8Lp%2BEO9FNOAOSnbQ%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770447783/e8e33f70db8f96d3bde9262c/bkFMij429o2GEqadB5HkUBGdiglfLYnzrP0YUNaFkbRMOahrKg7ju_l_D8XU-4znbP6Ou9_rqa5cj6Eg_vbFKj6fDqiVwB-IOvS5mK-5l21zxIeKEdfbQUCwcFjdWZjxBN5kgecjI68mw2tvGqHORA?expires=1781168400&signature=02a78b54b4c7cccf5ce72084c1c45cba1512639070a4d16cddd513b563188348&req=cycnEs15molcFb4f3HP0gF4DKIVTibA283fQ1k0iUDRwaHoeDk0pX1ScE4Aa%0ABE8Lp%2BEO9FNOAOSnbQ%3D%3D%0A)

## Step 4

Fill in the fields with the information below:

1. **Name:** Use a name to remember this connection, can be your nickname.
2. **Host:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
3. **Bucket Name:** enter the name of the bucket you created in [Telnyx Storage](https://portal.telnyx.com/#/app/storage/buckets).
4. **Access Key ID:** copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field.
5. **Secret Key ID:** You can type out anything you want here, as long as it doesn’t include spaces, quoting, or special characters.
6. **Default Storage Class:** leave it as “**Standard**”**.**

**Directory Structure:** leave it as “Simple’/’Delimited”.  
​

[![Directory structure. ](https://downloads.intercomcdn.com/i/o/885908373/65c9e16c9ea4104efc7bb2c5/Screenshot+2023-11-16+at+3.14.48%E2%80%AFPM.jpg?expires=1781168400&signature=26f1b3e6fa29fc59af8e84a44955c51e6fa05983d5b2fe6daa3f23973056e521&req=fCgiH8l2noZcFb4f3HP0gGdg%2Fjs0hYMNSV9CNFUGK0l9jY2J22WHKoWgm6P4%0ALz996GfOEyGjXq0c5w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/885908373/65c9e16c9ea4104efc7bb2c5/Screenshot+2023-11-16+at+3.14.48%E2%80%AFPM.jpg?expires=1781168400&signature=26f1b3e6fa29fc59af8e84a44955c51e6fa05983d5b2fe6daa3f23973056e521&req=fCgiH8l2noZcFb4f3HP0gGdg%2Fjs0hYMNSV9CNFUGK0l9jY2J22WHKoWgm6P4%0ALz996GfOEyGjXq0c5w%3D%3D%0A)

## Step 5

After authorizing ODrive, you'll be redirected back to the ODrive app, and Telnyx Storage will be successfully linked as a storage provider.  
​

[![ODrive App. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770447792/3c19c9355f946f7553cbfcd4/_E8AdgcAeNnTJBy7wmk5BYDscwg-sLqyhwlMb9787dKqTRERhyXY2GZqbKS30C3NZctbxIMbq29FV6nDdVVYsPORkAmBdvOsJJM96vMoACUigKPgLTf7g_y23IYqvZ6_W49u3TtryX5xswSmVsnTSw?expires=1781168400&signature=7fed00ac3ee6f6cf4d5979b0c64e1dbd44b090947b5cb09cf71b7eed5da1135b&req=cycnEs15mohdFb4f3HP0gPmZN2DgEueyB0%2FqT%2BWyLtamTHF7Vo8wW3gJG8lj%0ApFeuAPYRLoRSfw1D3A%3D%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/770447792/3c19c9355f946f7553cbfcd4/_E8AdgcAeNnTJBy7wmk5BYDscwg-sLqyhwlMb9787dKqTRERhyXY2GZqbKS30C3NZctbxIMbq29FV6nDdVVYsPORkAmBdvOsJJM96vMoACUigKPgLTf7g_y23IYqvZ6_W49u3TtryX5xswSmVsnTSw?expires=1781168400&signature=7fed00ac3ee6f6cf4d5979b0c64e1dbd44b090947b5cb09cf71b7eed5da1135b&req=cycnEs15mohdFb4f3HP0gPmZN2DgEueyB0%2FqT%2BWyLtamTHF7Vo8wW3gJG8lj%0ApFeuAPYRLoRSfw1D3A%3D%3D%0A)

Now, you can use the ODrive interface to browse and sync your files with Telnyx Storage. You can create folders, upload files, and manage your files' synchronization settings.

That's it! You have successfully integrated ODrive with Telnyx Storage, allowing you to sync and manage your files seamlessly across multiple devices and storage platforms.

---

**Additional Resources**

For further information and advanced usage of ODrive, you can refer to their [documentation](https://docs.odrive.com/docs).

​

---

Related Articles

[Use GoodSync with Telnyx Storage](https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage)[Use ExpanDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage)[Use WebDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage)[Use NetDrive3 with Telnyx Storage](https://support.telnyx.com/en/articles/8048024-use-netdrive3-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
