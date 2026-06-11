---
source_url: https://support.telnyx.com/en/articles/6964249-use-msp360-cloudberry-explorer-with-telnyx-storage
scraped: 2026-06-11
---

Use MSP360 Cloudberry Explorer with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use MSP360 Cloudberry Explorer with Telnyx Storage

Learn how to setup MSP360 Cloudberry Explorer, an intuitive file explorer, with Telnyx Storage for effective file management and transfer.

Written by Telnyx Engineering

June 6, 2024

Table of contents

[MSP360 Cloudberry Explorer](https://www.msp360.com/explorer/) is a powerful, user-friendly file manager, enabling you to manage and transfer data to and from many different cloud storage providers. With Cloudberry Explorer, you can easily upload, download, and organize your files, as well as perform advanced operations such as setting object metadata, versioning, and access control policies.

---

# How to configure MSP360 Cloudberry Explorer to work with Telnyx Storage

1. Download and install the latest version of the MSP360 Cloudberry Explorer [here](https://www.msp360.com/explorer/)!
2. Open the MSP360 Cloudberry Explorer application
3. Select the option to open a new "**Connection"**  
   ​

   [![MSP360 Cloudberry Explorer application page. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/665753087/e83d7235cfb8995d57916237/tdOBT3DNH5lTX77J1s8Pohp4HUZfqV4Xoeo7ifTj24YHvEUycg6cBVF3hYFimqWnceORHAcNZ7fPD4MGb2o0HgSTsI4uAm-kCxay3d2r2KnGmwgDtHViujCe-jQU_teJKOYVcf8UDT6VLjZmkAXmdqs?expires=1781168400&signature=4079a5e0fda56b8054e4c4ca00a60eecfde38b8a4d4818828e105e25b7c18cf5&req=ciYiEcx9nYlYFb4f3HP0gHfSBFTNb5iL4pTIYTboshkfd3mFpfnPJJths95a%0AlK4%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/665753087/e83d7235cfb8995d57916237/tdOBT3DNH5lTX77J1s8Pohp4HUZfqV4Xoeo7ifTj24YHvEUycg6cBVF3hYFimqWnceORHAcNZ7fPD4MGb2o0HgSTsI4uAm-kCxay3d2r2KnGmwgDtHViujCe-jQU_teJKOYVcf8UDT6VLjZmkAXmdqs?expires=1781168400&signature=4079a5e0fda56b8054e4c4ca00a60eecfde38b8a4d4818828e105e25b7c18cf5&req=ciYiEcx9nYlYFb4f3HP0gHfSBFTNb5iL4pTIYTboshkfd3mFpfnPJJths95a%0AlK4%3D%0A)
4. When prompted with the connection type, select "**S3 compatible"**  
   ​

   [![MSP360 Cloudberry Explorer application options for choosing connection type. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/665753090/b858de78e9128cdaa97239b1/JdIGZBFpRYqMU8rFpoNTZ6hQmBt3uE5RjhKDUXIlGA3R9RVVl0GeSnoyffTRKBsCr6hdQRWuit5qgHrKUIYPMJd5l_JAS096oaHQis447aGhF91eLjl2rFHXjj9c3BA6YOO5dXHU4VF7Sn6cmBo0XXQ?expires=1781168400&signature=211fdfb2b44de531a5ec0fb70a76f24350a23dd19cafa3a1334a0a9e7e610c89&req=ciYiEcx9nYhfFb4f3HP0gKUEAr1QDsTUwLJrOYL%2F%2Ba9CmWh9q5eBeLd9ENwP%0ARgs%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/665753090/b858de78e9128cdaa97239b1/JdIGZBFpRYqMU8rFpoNTZ6hQmBt3uE5RjhKDUXIlGA3R9RVVl0GeSnoyffTRKBsCr6hdQRWuit5qgHrKUIYPMJd5l_JAS096oaHQis447aGhF91eLjl2rFHXjj9c3BA6YOO5dXHU4VF7Sn6cmBo0XXQ?expires=1781168400&signature=211fdfb2b44de531a5ec0fb70a76f24350a23dd19cafa3a1334a0a9e7e610c89&req=ciYiEcx9nYhfFb4f3HP0gKUEAr1QDsTUwLJrOYL%2F%2Ba9CmWh9q5eBeLd9ENwP%0ARgs%3D%0A)
5. A new window will pop up to specify your connection settings. Enter in the following information, and then click "**OK"**:  
   ​

   ## **S3 compatible fields**

   1. **Display Name**: anything you want! Give this connection a nickname of your choosing.
   2. **Access Key**: copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field.
   3. **Secret Key**: The secret access key is not used by TelnyxStorage, but WAL-G will complain if it doesn’t exist. Type out anything you want here, as long as it doesn't include spaces, quoting, or special characters of any kind.
   4. **Endpoint**: Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   5. **Signature Version:** Select AWS4  
      ​

      [![S3 compatible fields. ](https://downloads.intercomcdn.com/i/o/884865456/d75ab9795bf16c2270cae206/Screenshot+2023-11-13+at+1.44.26%E2%80%AFPM+%281%29+%281%29.jpg?expires=1781168400&signature=030e9bef26ec1a95f0db9bd4686d901ffcafe709b6d497d0c79a834a3ad13fcd&req=fCgjHs97mYRZFb4f3HP0gK%2FBwvFXjESfmzxgKX0Mghsim6ymqRa5bcREhpV3%0A4Q8%3D%0A)](https://downloads.intercomcdn.com/i/o/884865456/d75ab9795bf16c2270cae206/Screenshot+2023-11-13+at+1.44.26%E2%80%AFPM+%281%29+%281%29.jpg?expires=1781168400&signature=030e9bef26ec1a95f0db9bd4686d901ffcafe709b6d497d0c79a834a3ad13fcd&req=fCgjHs97mYRZFb4f3HP0gK%2FBwvFXjESfmzxgKX0Mghsim6ymqRa5bcREhpV3%0A4Q8%3D%0A)
6. A new Connection should appear on the navigation bar with the same name as the value you entered in "**Display Name"**. If you click on that connection, your buckets will appear in the user interface.  
   ​

   [![Various buckets in the S3 compatible fields. ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/665753103/18a23d70ab8e2890c118e263/8CtmevE0W8Ciw5at_4rFwsVM3Bve_YKINboJ3xPlwXhVCWYnWCGQdGNdXU8CF8zGE1SIMuubuk3PCvI4ZgbieG6vwnzldlWon2XzdzLlM3ykE_ZVNDRlGcKkns18XyXjPzRkHO-tnF_W7jG8LDQFVXk?expires=1781168400&signature=55e2e5de827ba5f91df4e7b4af6b71cfe6cb7e3a9686497b3d1cfa1c4134383c&req=ciYiEcx9nIFcFb4f3HP0gA8jZ3eytjUu4oPsHXPgiSJDMVzSIT%2Fgy21T0KJ2%0A3Rs%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/665753103/18a23d70ab8e2890c118e263/8CtmevE0W8Ciw5at_4rFwsVM3Bve_YKINboJ3xPlwXhVCWYnWCGQdGNdXU8CF8zGE1SIMuubuk3PCvI4ZgbieG6vwnzldlWon2XzdzLlM3ykE_ZVNDRlGcKkns18XyXjPzRkHO-tnF_W7jG8LDQFVXk?expires=1781168400&signature=55e2e5de827ba5f91df4e7b4af6b71cfe6cb7e3a9686497b3d1cfa1c4134383c&req=ciYiEcx9nIFcFb4f3HP0gA8jZ3eytjUu4oPsHXPgiSJDMVzSIT%2Fgy21T0KJ2%0A3Rs%3D%0A)

And that’s all there is to it! You have now connected MSP360 Cloudberry Explorer to Telnyx Storage.

---

**Additional Resources**

For more information on how to use MSP360 explorer, check out their [guides for Windows](https://help.msp360.com/explorer), as well as their [guides for Macs](https://help.msp360.com/explorer-for-macos).

---

Related Articles

[Use Cyberduck with Telnyx Storage](https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage)[Use WinSCP with Telnyx Storage](https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage)[Use Syncovery with Telnyx Storage](https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage)[Use CrossFTP with Telnyx Storage](https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage)[Use ExpanDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
