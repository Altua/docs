# Data management policy

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 2.0 | February 9, 2026 | Mads Gedde | Updated data management policy. Approved by Einar Bjering. |
| 1.0 | December 10, 2025 | Mads Gedde | Initial documented policy. Approved by Einar Bjering. |

## Purpose

This policy ensures that information is classified, protected, retained, and securely disposed of according to its importance to Grunt AS.

## Scope

This policy applies to all Grunt AS data, information, and information systems.

## General requirements

Grunt AS classifies data and information systems according to legal requirements, sensitivity, and business criticality to ensure that information receives the appropriate level of protection.

Data owners are responsible for identifying any additional requirements for specific data or exceptions to standard handling requirements.

Information systems and applications must be classified according to the highest classification of data that they store or process.

## Data classification

Grunt AS uses three data classes to define protection requirements.

### Confidential

Confidential data is highly sensitive and requires the highest level of protection.

Access is restricted to specific employees or departments.

Confidential data may only be shared with others when approved by the data owner or a company executive.

Examples include:

- Customer data
- Personally identifiable information (PII)
- Company financial and banking data
- Salary, compensation, and payroll information
- Strategic plans
- Incident reports
- Risk assessment reports
- Technical vulnerability reports
- Authentication credentials
- Secrets and private keys
- Source code
- Litigation data

### Restricted

Restricted data is Grunt AS proprietary information that requires thorough protection.

Access is limited to personnel with a business need to know.

Restricted data may only be distributed outside the company with approval.

Restricted is the default classification for company information unless stated otherwise.

Examples include:

- Internal policies
- Legal documents
- Meeting minutes and internal presentations
- Contracts
- Internal reports
- Slack messages
- Email

### Public

Public data is intended for public consumption and may be freely distributed outside Grunt AS.

Examples include:

- Marketing materials
- Product descriptions
- Release notes
- External-facing policies

### Labeling

Confidential data should be labeled `confidential` whenever paper or digital copies are produced for distribution.

## Data handling

### Confidential data handling

Confidential data is subject to the following requirements:

- Access for non-preapproved roles requires documented approval from the data owner
- Access is restricted to specific employees, roles, or departments
- Confidential systems must not allow unauthenticated or anonymous access
- Confidential customer data must not be used or stored in non-production environments
- Confidential data must be encrypted at rest and in transit over public networks in accordance with the Cryptography Policy
- Mobile device hard drives containing confidential data, including laptops, must be encrypted
- Mobile devices storing or accessing confidential data must be protected by a password, passcode, or equivalent control such as biometrics, and must lock after 10 minutes of non-use
- Backups must be encrypted
- Confidential data must not be stored on personal phones, personal devices, or removable media such as USB drives, CDs, or DVDs
- Paper records must be labeled `confidential` and securely stored and disposed of according to approved data handling and destruction procedures
- Hardcopy records should only be created when there is a business need and should be avoided whenever possible
- Hard drives and mobile devices used to store confidential information must be securely wiped before disposal or physically destroyed
- Transfers of confidential data outside the company require a legal contract or arrangement and explicit written permission from management or the data owner

### Restricted data handling

Restricted data is subject to the following requirements:

- Access is restricted to users with a business need to know
- Restricted systems must not allow unauthenticated or anonymous access
- Transfers of restricted data outside the company require management approval and must be covered by a legal contract, arrangement, or data owner permission
- Paper records must be securely stored and disposed of according to approved data handling and destruction procedures
- Hard drives and mobile devices used to store restricted information must be securely wiped before disposal or physically destroyed

### Public data handling

Public data does not require special protection or handling controls and may be freely distributed.

## Data retention

Grunt AS retains data only as long as needed for business use or to meet regulatory or contractual requirements.

When data is no longer needed, it must be securely disposed of or archived.

Data owners, in consultation with legal counsel, may determine retention periods for their data.

Personally identifiable information (PII) must be deleted or de-identified as soon as it no longer has a business use.

Retention periods must be documented in the data retention matrix in Appendix B of this policy.

## Data and device disposal

Restricted and confidential data must be securely deleted when no longer needed.

Grunt AS must assess the data and disposal practices of third-party vendors according to the Third-Party Management Policy.

Only third parties that meet Grunt AS requirements for secure data disposal may be used to store or process restricted or confidential data.

Grunt AS must ensure that all restricted and confidential data is securely deleted from company devices before, or at the time of, disposal.

Confidential and restricted hardcopy materials must be shredded or otherwise disposed of using a secure method.

Personally identifiable information (PII) must be collected, used, and retained only for as long as Grunt AS has a legitimate business purpose.

PII must be securely deleted after contract termination according to company policy, contractual commitments, and applicable laws and regulations.

PII must also be deleted in response to a verified consumer or data subject request when Grunt AS does not have a legitimate business interest or legal obligation to retain the data.

## Annual data review

Management must review data retention requirements during the annual review of this policy.

Data must be disposed of according to this policy.

## Legal requirements

Grunt AS may become subject to legal proceedings that require the retention of data associated with legal holds, lawsuits, or other matters identified by legal counsel.

These records are exempt from the other retention requirements in this policy and must be retained according to requirements identified by the legal department.

All legal holds and special retention requirements are subject to annual review with legal counsel to confirm continuing need and scope.

## Policy compliance

Grunt AS measures and verifies compliance with this policy through methods including business tool reports and internal and external audits.

## Exceptions

Requests for an exception to this policy must be submitted to the CEO for approval.

## Violations and enforcement

Known violations of this policy must be reported to the CEO.

Violations may result in immediate withdrawal or suspension of system and network privileges and disciplinary action, up to and including termination of employment.

## Appendix A: Internal retention and disposal procedure

Grunt AS's Technology Team is responsible for setting and enforcing data retention and disposal procedures for Grunt-managed accounts and devices.

### Customer accounts

1. Customer accounts must be scrubbed and PII data must be deleted within one year of contract termination through manual or automated deletion processes.
2. Primary data, including customer-uploaded data, is retained during the contract period and deleted within 30 to 90 days after contract termination or upon customer request.

### Devices

1. Employee devices must be collected promptly upon employee termination.
2. Remote employees must be sent a shipping label and return of the device must be monitored.
3. Collected devices must be cleared for reprovisioning or removed from inventory.
4. Grunt AS must securely erase a device when reprovisioning it.
5. Device images may be retained at management's discretion for business purposes.

### Destroying devices or electronic media

If a device is damaged and Grunt AS cannot access the recovery partition to erase the drive, Grunt AS may use an e-waste service that includes data destruction with a certificate.

Grunt AS keeps certificates of destruction on record for one year.

Physical destruction is optional if the device is verified to be encrypted with full-disk encryption and the risk of data recovery is therefore mitigated.

Management reviews this procedure at least annually.

## Appendix B: Data retention matrix

| System or application | Data description | Retention period |
|-----------------------|------------------|------------------|
| Grunt SaaS products | PII end-user data | Up to one year after contract termination |
| Grunt data metrics | Customer metrics describing user actions | Indefinite |
| Grunt error logs | Customer error reports, metadata, and debugging data | Indefinite |
| Grunt customer support tickets (`HubSpot`) | Support tickets and cases | Indefinite |
| Grunt customer sales (`HubSpot`) | Opportunity and sales data | Indefinite |
| Grunt AS QA and testing data (`GitHub`) | QA, testing scenarios, and results data | Indefinite |
| Security policies | Security policy documents | One year after archive |
