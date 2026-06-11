---
source_url: https://support.telnyx.com/en/articles/7873510-use-duplicati-with-telnyx-storage
scraped: 2026-06-11
---

Use Duplicati with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use Duplicati with Telnyx Storage

Discover how to set up Duplicati, an open-source backup solution, with Telnyx Storage for secure and automated backup and recovery.

Written by Telnyx Engineering

June 19, 2024

Table of contents

Duplicati is an open-source backup software that provides users with a simple and reliable way to back up their files and data to various cloud storage providers, including Amazon S3, Google Drive, Dropbox, and now Telnyx Storage. It features strong encryption, incremental and full backups, versioning, and scheduling, as well as options for customization and automation.

---

## How to configure Duplicati to work with Telnyx Storage

1. Download and install the latest version of Duplicati [here](https://duplicati.com/)!
2. Open the Duplicati application.
3. Click on **Add Backup**, select **Configure a new backup** and click **Next** to continue

[![New backup configuration settings. ](https://downloads.intercomcdn.com/i/o/735634672/df8341a611c813ebfe36e2b8/duplicati1.JPG?expires=1781168400&signature=3230bbec9219d3923d03c91285b15641650a6bc8dd7f379a8931e78ab6fb18d6&req=cyMiEMp6m4ZdFb4f3HP0gCD4PsqruSTxdW8jracsg9dzPzj1Sj7HDsFyaVs7%0ANrMX02k%2FLEGWi7K5IA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/735634672/df8341a611c813ebfe36e2b8/duplicati1.JPG?expires=1781168400&signature=3230bbec9219d3923d03c91285b15641650a6bc8dd7f379a8931e78ab6fb18d6&req=cyMiEMp6m4ZdFb4f3HP0gCD4PsqruSTxdW8jracsg9dzPzj1Sj7HDsFyaVs7%0ANrMX02k%2FLEGWi7K5IA%3D%3D%0A)

## Telnyx Storage Configuration

There are 5 steps to creating a new backup. This guide will only focus on Step 2: Destination, where we will configure Telnyx Storage as the backup destination.

[![Destination's button. ](https://downloads.intercomcdn.com/i/o/735635771/e0afbf4d77de1e87aab29807/duplicati2.JPG?expires=1781168400&signature=5eb090b676a5dddec975e031182dfff19fc86b61d2ad5771e09f091d6b9a4a93&req=cyMiEMp7moZeFb4f3HP0gI45jNPADmUgb16LQNX7M3PRuymkPyxc1Z0j5PQM%0ASSLFT3UIiNhhnQprWA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/735635771/e0afbf4d77de1e87aab29807/duplicati2.JPG?expires=1781168400&signature=5eb090b676a5dddec975e031182dfff19fc86b61d2ad5771e09f091d6b9a4a93&req=cyMiEMp7moZeFb4f3HP0gI45jNPADmUgb16LQNX7M3PRuymkPyxc1Z0j5PQM%0ASSLFT3UIiNhhnQprWA%3D%3D%0A)

In the **Storage Type** dropdown menu, select **S3 Compatible**

[![Storage type settings. ](https://downloads.intercomcdn.com/i/o/735635815/10ac920aa8fc4af49eb16685/duplicati3.JPG?expires=1781168400&signature=c54fb85e777b92740051f8514bb8a25d0a3ef1dddaf2d46e416cafa9e25715a3&req=cyMiEMp7lYBaFb4f3HP0gO9v89zGaGrz%2FdzPfndLdyL836fjLIGpLBBU8XSS%0AnkF4oyniPChRtFMgPA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/735635815/10ac920aa8fc4af49eb16685/duplicati3.JPG?expires=1781168400&signature=c54fb85e777b92740051f8514bb8a25d0a3ef1dddaf2d46e416cafa9e25715a3&req=cyMiEMp7lYBaFb4f3HP0gO9v89zGaGrz%2FdzPfndLdyL836fjLIGpLBBU8XSS%0AnkF4oyniPChRtFMgPA%3D%3D%0A)

For the remaining fields, enter the following information:

1. **Use SSL**: toggled on
2. **Server:** in the dropdown menu, select `Custom Server URL ( )` and then enter copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
3. **Bucket Name:** either type the name of an existing bucket, or enter the name for a bucket you want to create
4. **Bucket Create Region:** Copy and paste the matching region from [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints). For example, if you chose the [https://us-central-1.telnyxstorage.com](https://us-central-1.telnyxstorage.com/) endpoint, you will use us-central-1 as the region.
5. **Storage class**: (default) ( )
6. **AWS Access ID:** copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field
7. **AWS Access Key:** The secret access key is not used by Telnyx Storage, but Duplicati will complain if it doesn’t exist. Type out anything you want here, as long as it doesn't include spaces, quoting, or special characters of any kind.
8. **Client library to use**: Amazon AWS SDK  
   ​

   [![Backup destination settings. ](https://downloads.intercomcdn.com/i/o/885794893/622e731a50340d51dcd3b8d2/Screenshot+2023-11-16+at+12.38.48%E2%80%AFPM.jpg?expires=1781168400&signature=0f4b05499b55f31e2d75bf7344bf6f05ae7d88b252928e68d276396134a4ca26&req=fCgiEcB6lYhcFb4f3HP0gHUzm8BGr3TM4TB%2BHMNd85%2BdvHYWJ%2B3LA9oaA5It%0AfxM%3D%0A)](https://downloads.intercomcdn.com/i/o/885794893/622e731a50340d51dcd3b8d2/Screenshot+2023-11-16+at+12.38.48%E2%80%AFPM.jpg?expires=1781168400&signature=0f4b05499b55f31e2d75bf7344bf6f05ae7d88b252928e68d276396134a4ca26&req=fCgiEcB6lYhcFb4f3HP0gHUzm8BGr3TM4TB%2BHMNd85%2BdvHYWJ%2B3LA9oaA5It%0AfxM%3D%0A)

And that's all there is to it! You can complete the other remaining steps for configuring a new backup. Once the new backup is created, your data will be stored on Telnyx Storage.

---

## **Additional Resources**

For more information on how to use Duplicati, check out their [manuals here](https://duplicati.readthedocs.io/en/latest/).

---

Related Articles

[Use WAL-G with Telnyx Storage](https://support.telnyx.com/en/articles/6966381-use-wal-g-with-telnyx-storage)[Use Arq Backup with Telnyx Storage](https://support.telnyx.com/en/articles/7869213-use-arq-backup-with-telnyx-storage)[Use Backup4all with Telnyx Storage](https://support.telnyx.com/en/articles/7869264-use-backup4all-with-telnyx-storage)[Use Syncovery with Telnyx Storage](https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage)[Use GoodSync with Telnyx Storage](https://support.telnyx.com/en/articles/8047898-use-goodsync-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
