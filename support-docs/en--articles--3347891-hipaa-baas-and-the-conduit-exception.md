---
source_url: https://support.telnyx.com/en/articles/3347891-hipaa-baas-and-the-conduit-exception
title: "HIPAA, BAAs and the Conduit Exception"
description: "In this article, we will explain HIPAA, BAAs, the Conduit Exception, and how Telnyx approaches BAA requests."
scraped: 2026-07-08
updated_at: 2026-09-29
content_hash: bb4df187f513c17c6b78dc2aca4533b4d490e2204b9039a1c8653952729f3e31
---

# HIPAA, BAAs and the Conduit Exception

In this article, we will explain HIPAA, BAAs, the Conduit Exception, and how Telnyx approaches BAA requests. This article describes how the Telnyx platform works and how Telnyx approaches BAA requests. It is general information, not legal advice, and it does not determine whether your use of Telnyx is HIPAA compliant or whether you need a BAA. Those are determinations for you and your counsel based on your own configuration and use of the Services. See Telnyx's published documents for more details.

## What is HIPAA and a BAA?

The Health Insurance Portability & Accountability Act (HIPAA) governs the confidentiality and security of protected health information (PHI) within the United States for "covered entities" and their "business associates." HIPAA requires covered entities, such as healthcare providers, hospital systems and pharmacies, to implement policies and procedures to ensure the protection of this highly sensitive information. Additionally, the HIPAA rules generally require a covered entity to enter into a Business Associate Agreement (BAA) with certain third-party vendors who access, receive, transmit or store the PHI (aka business associates).

Whether or not a third-party vendor should fall within the definition of a "business associate" and be required to sign a BAA is very fact specific, and that determination is yours to make with your own counsel. Telnyx does not assess whether your use of the platform is HIPAA compliant or whether you need a BAA.

## What is the Conduit Exception?

Some third-party vendors fall within the HIPAA "conduit exception" and are therefore not required to enter into a BAA. Telecommunications companies often fall within this conduit exception. A BAA is not needed for an individual or organization that "acts merely as a conduit for protected health information, for example, the US Postal Service, certain private couriers, and their electronic equivalents." Temporarily storing PHI incident to a transmission does not disqualify such an individual or organization from the conduit exception. [See Department of Health and Human Services, 78 FR 5571-72.](https://www.govinfo.gov/content/pkg/FR-2013-01-25/pdf/2013-01073.pdf)

In general, Telnyx's core connectivity services (voice and messaging transmission) fall within this conduit exception under HIPAA. Whether the exception applies to your configuration depends on how you use the platform. Features that store or process content beyond incidental transmission, such as call recording, transcription, storage and AI features, are a different analysis, and you should review them with your counsel.

## Does Telnyx offer a BAA?

Yes. Telnyx offers a BAA to customers who meet its commercial thresholds and who architect their use of the platform in line with Architecting HIPAA on Telnyx. See Architecting guidelines found at [https://telnyx.com/resources/architecting-hipaa-telnyx](https://telnyx.com/resources/architecting-hipaa-telnyx).

To request a BAA or ask about eligibility, contact [sales@telnyx.com](mailto:sales@telnyx.com).
