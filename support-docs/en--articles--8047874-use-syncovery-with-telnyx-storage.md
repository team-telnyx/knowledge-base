---
source_url: https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage
title: "Use Syncovery with Telnyx Storage"
description: "Explore how to configure Syncovery with Telnyx Storage for seamless file transfer, synchronization, See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: c80a106e775081db735161d33398975f4f9762001bfaeadad0736f5af5ad03f8
---







# Use Syncovery with Telnyx Storage

Explore how to configure Syncovery with Telnyx Storage for seamless file transfer, synchronization, See Telnyx guidance and requirements.




[Syncovery](https://www.syncovery.com/) is a versatile file synchronization and backup software that provides users with a range of powerful features for managing their data. By integrating Syncovery with [Telnyx Storage](https://telnyx.com/products/cloud-storage), you can take advantage of Telnyx's reliable and scalable storage solution to ensure the safety and accessibility of your files.

---

## How to configure Syncovery to work with Telnyx Storage

## Step 1

**Download and Install Syncovery:** Start by downloading and installing the latest version of Syncovery from the official website. You can find the download link [here!](https://www.syncovery.com/)

## Step 2

**Launch Syncovery:** Once Syncovery is installed, launch the application on your computer.

![Profile overview section of Syncovery. ](_images/263e26fd4404ba65.png)

## Step 3

**Create a New Profile:** click on the ‘green plus button’ to create a new synchronization or backup profile.
​

![New Profile section of Syncovery. ](_images/567f14e127a5f906.png)

## Step 4

**Select Source and Destination:** In the profile configuration window, click on the “Internet” button
​

![Source and destination profile section of Syncovery. ](_images/48547ad210e82f23.png)

## Step 5

**Enter Telnyx Storage Details:** In the Internet Protocol Settings window, enter the following information and then click on `OK`:

1. **Protocol:** Select **S3** from the dropdown menu
2. **Access ID:** Copy your API key from your account settings in the [Telnyx portal.](https://portal.telnyx.com/#/app/api-keys)
3. **Secret key:** Input your Access ID - the access ID is not used by Telnyx Storage, but is needed by Syncovery. Type out anything you want here, as long as it doesn't include spaces, quoting, or special characters of any kind.
4. **Provider:** Select the “custom” option from the dropdown
5. **Bucket:** Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
6. **Folder:** Select the folder to backup on your PC
   ​

   ![Internet protocol settings section. ](_images/d44de1d00f7fdd23.jpg)

## Step 6

Select the path you are synchronizing to from the options below; it can be from your local storage - **Browse…, Internet…** or a **Device**
​

![Browse, internet, and device buttons. ](_images/e30741c2897b9ebf.png)

## Step 7

To save your new profile, click on **OK**
​

![Okay button. ](_images/8c283a528946aed1.png)

And that’s all there is to it! You are now ready to use Syncovery with Telnyx Storage to back up and synchronize your files.

Enjoy the convenience and reliability of Syncovery combined with the scalability and security of Telnyx Storage for effective data management.

---

**Additional Resources**

For more information on Syncovery and its features, refer to the official [documentation](https://www.syncovery.com/category/documentation/).
​
