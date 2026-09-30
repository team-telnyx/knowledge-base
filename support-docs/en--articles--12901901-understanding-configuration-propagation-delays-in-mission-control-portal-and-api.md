---
source_url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
title: "Understanding Configuration Propagation Delays in Mission Control Portal and API"
description: "Learn how Telnyx updates move through the platform and how to optimize design around short propagation windows. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 0016433143eb0c5c7df2c9f6c0f5d501d5dcf3138af8c13a7bc66c1d5e3f50b1
---







# Understanding Configuration Propagation Delays in Mission Control Portal and API

Learn how Telnyx updates move through the platform and how to optimize design around short propagation windows. See Telnyx guidance and requirements.




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
