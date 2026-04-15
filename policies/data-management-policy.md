# Data management policy

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 4.0 | April 16, 2026 | Jan Kristian Bjerke | Consolidated data management, data retention, and data policy into a single policy. Approved by Einar Bjering. |
| 3.0 | March 17, 2026 | Jan Kristian Bjerke | Updated data retention. Approved by Einar Bjering. |
| 2.0 | February 9, 2026 | Mads Gedde | Updated data management policy. Approved by Einar Bjering. |
| 1.0 | December 10, 2025 | Mads Gedde | Initial documented policy. Approved by Einar Bjering. |

## Purpose

This policy ensures that information is classified, protected, retained, and securely disposed of according to its importance to Grunt AS. It also defines how Grunt AS handles data collected through its software products.

## Scope

This policy applies to:

- All Grunt AS data, information, and information systems
- All employees, contractors, and third-party service providers handling Grunt AS data
- Data collected through Grunt AS software products

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

## Product data collection

Grunt AS is committed to protecting the privacy of users of its software products. Only the minimum amount of data needed to diagnose problems and improve the software is collected.

When collecting data, Grunt AS tracks what actions users perform, never what users are working on.

Grunt AS does not gather information that could reveal the content of user files, including:

- File names
- File paths
- Text
- Numbers
- Data contained in files
- External data sources

Usage tracking is strictly limited to which actions are performed and how often.

### License validation

When users use Grunt software, the following data is sent to validate the license:

- A hardware identifier to identify the computer
- The email address used as the license key

### Metrics tracking

The metrics tracking system focuses only on actions performed in the software. This allows Grunt AS to understand how the software is used and improve the product without collecting any information about the content of user work.

## Data retention

Grunt AS retains data only as long as needed for business use or to meet regulatory or contractual requirements.

When data is no longer needed, it must be securely disposed of or archived.

Data owners, in consultation with legal counsel, may determine retention periods for their data.

Personally identifiable information (PII) must be deleted or de-identified as soon as it no longer has a business use.

Once the retention period expires and no legal hold or operational need exists, the data must be securely deleted or anonymized.

### Data retention matrix

The following table defines default retention periods. Data owners may adjust retention periods where required by law, contract, or operational needs.

| Data Type | Classification | Retention Period | Disposal Method |
|---|---|---|---|
| Customer uploaded data | Confidential | Duration of customer relationship + 1 year | Secure deletion |
| Personally Identifiable Information (PII) | Confidential | As long as business purpose exists | Deletion or anonymization |
| Authentication Logs | Confidential | 1 year | Automated deletion |
| Security & Audit Logs | Confidential | 3 years | Automated deletion |
| Incident Reports | Confidential | 3 years | Secure deletion |
| Contracts & Legal Documents | Restricted | Indefinite | Secure archival or deletion |
| Financial Records | Confidential | 7 years | Secure deletion |
| Internal Chat Messages (Slack or similar) | Restricted | 5 years | Automated deletion |
| Business Email | Restricted | 5 years | Automated deletion |
| Internal Reports & Presentations | Restricted | Indefinite | Secure archival or deletion |
| Source Code | Confidential | Indefinite while product maintained | Secure archival or deletion |
| Backups | Confidential | 1 year | Automated deletion |
| Customer support tickets (HubSpot) | Confidential | Indefinite | Secure archival or deletion |
| Customer sales data (HubSpot) | Confidential | Indefinite | Secure archival or deletion |
| QA and testing data (GitHub) | Restricted | Indefinite | Secure archival or deletion |
| Security policies | Restricted | One year after archive | Secure deletion |
| Marketing Materials | Public | Indefinite | No deletion requirement |

If chat messages or email contain records that fall into another category, such as contracts, finance, HR, security, or incident handling, the longer retention period for that category applies.

Data owners may define additional retention rules specific to their systems.

### Automated data deletion

Grunt AS implements automated processes to ensure data is deleted when its retention period expires.

Automated deletion mechanisms may include:

- Scheduled deletion jobs
- Lifecycle policies in cloud storage
- Automated log rotation and expiration
- Database cleanup scripts
- Third-party SaaS retention controls

Automated processes must:

- Run on a scheduled basis
- Remove or anonymize expired records
- Generate system logs documenting deletion activities

## Data and device disposal

Restricted and confidential data must be securely deleted when no longer needed.

Grunt AS must assess the data and disposal practices of third-party vendors according to the Third-Party Management Policy.

Only third parties that meet Grunt AS requirements for secure data disposal may be used to store or process restricted or confidential data.

Grunt AS must ensure that all restricted and confidential data is securely deleted from company devices before, or at the time of, disposal.

Confidential and restricted hardcopy materials must be shredded or otherwise disposed of using a secure method.

Personally identifiable information (PII) must be collected, used, and retained only for as long as Grunt AS has a legitimate business purpose.

PII must be securely deleted after contract termination according to company policy, contractual commitments, and applicable laws and regulations.

PII must also be deleted in response to a verified consumer or data subject request when Grunt AS does not have a legitimate business interest or legal obligation to retain the data.

### Customer accounts

1. Customer accounts must be scrubbed and PII data must be deleted within one year of contract termination through manual or automated deletion processes.
2. Primary data, including customer-uploaded data, is retained during the contract period and deleted within one year after contract termination or upon customer request.

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

## Monitoring and validation

To ensure compliance with this policy:

- Automated deletion processes must be tested during implementation
- System logs must be reviewed periodically
- Configuration settings must be reviewed during annual policy review
- Any deletion failures must be investigated and corrected

The Security or Engineering team is responsible for validating that retention enforcement operates correctly.

## Evidence and auditability

To demonstrate compliance with this policy, Grunt AS maintains evidence including:

- System logs showing deletion of expired records
- Automated deletion reports from data systems
- Configuration screenshots demonstrating retention settings
- Documentation of automated deletion scripts or lifecycle rules
- Periodic audit records validating retention enforcement

These records may be used for internal reviews, audits, and compliance verification.

## Legal holds

When Grunt AS becomes subject to legal proceedings, investigations, or regulatory requests:

- Relevant data must be preserved regardless of retention schedules
- Data retention automation must exclude records under legal hold
- Legal counsel will determine the duration of the hold

All legal holds and special retention requirements are subject to annual review with legal counsel to confirm continuing need and scope.

## Roles and responsibilities

### Data Owners

- Define retention requirements for their data
- Ensure systems follow retention policies

### Engineering / IT

- Implement automated deletion mechanisms
- Maintain logs of deletion activity
- Ensure systems enforce retention rules

### Security / Compliance

- Monitor compliance
- Maintain policy documentation
- Provide evidence for audits

## Annual policy review

Management must review data retention and data management requirements during the annual review of this policy.

This policy is reviewed annually to ensure alignment with:

- Legal requirements
- Business needs
- Security practices
- Compliance frameworks

Data must be disposed of according to this policy.

## Policy compliance

Grunt AS measures and verifies compliance with this policy through methods including business tool reports and internal and external audits.

## Exceptions

Requests for an exception to this policy must be submitted to the CEO for approval.

## Violations and enforcement

Known violations of this policy must be reported to the CEO.

Violations may result in immediate withdrawal or suspension of system and network privileges and disciplinary action, up to and including termination of employment.
