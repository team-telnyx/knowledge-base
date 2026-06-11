---
source_url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
scraped: 2026-06-11
---

Understanding Configuration Propagation Delays in Mission Control Portal and API | Telnyx Help Center

[Skip to main content](#main-content)

# Understanding Configuration Propagation Delays in Mission Control Portal and API

Learn how Telnyx updates move through the platform and how to optimize design around short propagation windows.

Written by Telnyx Engineering

November 21, 2025

Table of contents

## Background

When you make changes in the Telnyx Mission Control Portal or through the Telnyx API, those updates must propagate across a globally distributed infrastructure. Telnyx runs multiple instances across data centers worldwide, and each change needs to reach all of them before it becomes fully effective.

## **Propagation Timing**

* **Minimum:** ~1 second
* **Average:** ~1.5 seconds
* **Maximum:** ~3 seconds

This propagation window applies to **all** configuration updates, including but not limited to:

* Creating or modifying **On-Demand SIP Credentials.**
* Updating call control settings.
* Modifying connection configurations.
* Editing messaging profiles or number settings.

Because of this short but unavoidable delay, customers should design their workflows with propagation time in mind. For example, if you create new SIP credentials and attempt to use them immediately, authentication may fail until propagation completes. Adding a small delay before first use—or pre-creating credentials ahead of time—avoids potential issues.

Building this expectation into your application logic ensures a smoother and more reliable experience when interacting with the Telnyx platform.

---

Related Articles

[Configuring a Cisco CME Credentials Trunk](https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk)[Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)[Configuring Linphone with Telnyx](https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx)[Vicidial: Configure Vicidial Credentials](https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)

Did this answer your question?

😞😐😃

Table of contents
