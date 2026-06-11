---
source_url: https://support.telnyx.com/en/articles/6964207-use-cyberduck-with-telnyx-storage
scraped: 2026-06-11
---

Use Cyberduck with Telnyx Storage | Telnyx Help Center

[Skip to main content](#main-content)

# Use Cyberduck with Telnyx Storage

Learn how to set up Cyberduck, a popular FTP client, with Telnyx Storage for seamless file transfer and storage management.

Written by Telnyx Engineering

June 6, 2024

Table of contents

[Cyberduck](https://cyberduck.io/) is a free, open-source file transfer client for macOS and Windows. With Cyberduck, you can easily upload, download, and manage files, as well as perform advanced operations such as setting object metadata, versioning, and lifecycle policies.

---

# How to configure Cyberduck to work with Telnyx Storage

1. Download and install the latest version of Cyberduck [here](https://cyberduck.io/download/)!
2. Open the Cyberduck application. Then, click on the option to Open Connection  
   ​

   [![Options dropdown of the Open Connection section of the Cybertruck application ](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/665745677/226e8d4a60c83a2268e82769/Vac49ZztSb--1VS1LjzOXABlqUrLnfQ6WBouVEzPgKzSQ6WCnGzlMaL27hGcANHhwhNEHbhHEiwCBGKa9bhVlSwO3olex5aaLNUbAVubDvGDHUDc3xjrzzBJbiQttQXoh35UnKlrNZoVnFDqHLNqCig?expires=1781168400&signature=b074bfb3f7b70889123d7247a3809f50c90e986bee89c2fbb532e1395853049c&req=ciYiEc17m4ZYFb4f3HP0gM25JadOvh37PDfTMf3vXYx1qRZoEYNW2ED%2FrSgL%0AIR8%3D%0A)](https://telnyx-48416ce2297b.intercom-attachments-7.com/i/o/665745677/226e8d4a60c83a2268e82769/Vac49ZztSb--1VS1LjzOXABlqUrLnfQ6WBouVEzPgKzSQ6WCnGzlMaL27hGcANHhwhNEHbhHEiwCBGKa9bhVlSwO3olex5aaLNUbAVubDvGDHUDc3xjrzzBJbiQttQXoh35UnKlrNZoVnFDqHLNqCig?expires=1781168400&signature=b074bfb3f7b70889123d7247a3809f50c90e986bee89c2fbb532e1395853049c&req=ciYiEc17m4ZYFb4f3HP0gM25JadOvh37PDfTMf3vXYx1qRZoEYNW2ED%2FrSgL%0AIR8%3D%0A)

   ​
3. A new window will pop up to specify your connection settings. Choose Amazon S3 as the connection type from the drop down.

   [![Cyberduck Amazon s3 interface.](https://downloads.intercomcdn.com/i/o/882777361/b30672f35be63af9ccb1ce1b/Screenshot+2023-11-13+at+3.11.30%E2%80%AFPM.png?expires=1781168400&signature=f54821d31d5e7b3676172d1073f76b422b1c88448005a2554c46f3aab3e953c7&req=fCglEc55nodeFb4f3HP0gJYaHlDYgXgsPq3pjIiGdcX4iGGIeEAV8c7SADYe%0Aa1A%3D%0A)](https://downloads.intercomcdn.com/i/o/882777361/b30672f35be63af9ccb1ce1b/Screenshot+2023-11-13+at+3.11.30%E2%80%AFPM.png?expires=1781168400&signature=f54821d31d5e7b3676172d1073f76b422b1c88448005a2554c46f3aab3e953c7&req=fCglEc55nodeFb4f3HP0gJYaHlDYgXgsPq3pjIiGdcX4iGGIeEAV8c7SADYe%0Aa1A%3D%0A)
4. In the window, enter in the following information:

   1. **Server**: Copy and paste one of our available [API Endpoints](https://developers.telnyx.com/docs/cloud-storage/api-endpoints).
   2. **Port**: 443
   3. **Access Key ID**: copy and paste your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) in this field
   4. **Secret Access Key**: The secret access key is not used by TelnyxStorage, but Cyberduck will complain if it doesn’t exist. Type out anything you want here, as long as it doesn't include spaces, quoting, or special characters of any kind.
5. Click Connect

   ​

   And that’s all there is to it! All of your buckets should now appear on the Cyberduck UI, and you are ready to start using Cyberduck to manage your data on Telnyx Storage!

###

---

## Additional Resources

For more information on how to use Cyberduck, check out their [developer documentation](https://docs.cyberduck.io/cyberduck/).

---

---

Related Articles

[Use WinSCP with Telnyx Storage](https://support.telnyx.com/en/articles/7903390-use-winscp-with-telnyx-storage)[Use CrossFTP with Telnyx Storage](https://support.telnyx.com/en/articles/8047941-use-crossftp-with-telnyx-storage)[Use ExpanDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047945-use-expandrive-with-telnyx-storage)[Use WebDrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047969-use-webdrive-with-telnyx-storage)[Use AirExplorer with Telnyx Storage](https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage)

Did this answer your question?

😞😐😃

Table of contents
