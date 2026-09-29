---
title: "Distinguish your outbound profiles & DIDs"
summary: "Here we will explain how to distinguish between your different outbound profiles and DIDs and how you can organize them… See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--1130721-distinguish-your-outbound-profiles-dids.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--1130721-distinguish-your-outbound-profiles-dids.md -->

# Distinguish your outbound profiles & DIDs

Here we will explain how to distinguish between your different outbound profiles and DIDs and how you can organize them… See Telnyx guidance and requirements.




Telnyx Mission Control is designed to make it easy to segregate and differentiate your inbound and outbound traffic.

## SIP Connections:

The first layer of organization is SIP Connections. SIP Connections are used for both inbound and outbound traffic. When pulling usage reports, you can select "By Connection" as your Aggregation Type and you will get a breakdown of inbound and outbound usage for each connection. You can also generate Customer Detail Records (CDRs) which produces a record of all the calls (inbound and outbound) that match your selected criteria. Each record in the CDR will include the connection. We also enable you to add additional filtering when generating the CDR. You can choose to filter on:

* SIP Connections
* Record Type (Complete, Incomplete, Errors)
* Call Type (Inbound, Outbound)
* CLI (from number)
* CLD (to number)
* Tags (discussed below)

**Tagging Feature:**

Beyond using connections, Telnyx Mission Control has a Tagging feature to provide additional filtering and organization of your services. On both the Numbers and Outbound Profile pages, you will see the Tag icon (

![](_images/9108303e058f525c.png)

) next to each record. When hovering over the icon, you can see all the Tags associated with that service. By clicking on the icon, you will bring up the Tags Modal/Window which will allow you to add/remove Tags associated with that Number or Outbound Profile. These tags can then be used as filters when pulling CDRs (as noted above). We will also include all the Tags associated with a Number or Outbound Profile as part of the record within a CDR. This makes viewing CDRs much easier and allows for quick sorting/filtering of the records.

Common Uses for Tagging Feature:

* Tagging services with the Department/End-User they belong to
* Tagging services with the Office Location they belong to
* Tagging Numbers with their purchase date
* Tagging services to group together all of a single client's services
* Tagging services before performing troubleshooting for easier identification

**NOTE:**

For inbound calls, where DID's are tagged, the CDR report will show the DID's associated tag.

For outbound calls, the CDR report will show the tag assigned to the outbound voice profile only and not the tag that was assigned at the DID.
