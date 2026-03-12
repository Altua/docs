# Data Retention Policy

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 11, 2026 | Jan Kristian Bjerke | Initial documented |


## Purpose
This Data Retention Policy defines how long Grunt AS retains different categories of data and how expired data is automatically deleted or securely disposed of. The policy ensures compliance with legal, contractual, and operational requirements and aligns with the Grunt AS Data Management Policy.

## Scope
This policy applies to:

- All Grunt AS information systems
- All data stored or processed by Grunt AS
- All employees, contractors, and third-party service providers handling company data

## Guiding Principles

Grunt AS retains data only for as long as necessary to:

- Fulfill legitimate business purposes
- Meet legal or regulatory requirements
- Meet contractual obligations
- Maintain security and operational integrity

Once the retention period expires and no legal hold or operational need exists, the data must be securely deleted or anonymized.

Personally Identifiable Information (PII) must be deleted or de-identified as soon as it no longer has a business use.

Legal holds override retention schedules until the hold is lifted by legal counsel.

## Data Classification

Retention requirements are applied according to the classification defined in the Data Management Policy:

| Classification | Description |
|---|---|
| Confidential | Highly sensitive data requiring the highest level of protection |
| Restricted | Proprietary internal data requiring protection |
| Public | Data intended for public distribution |

## Data Retention Matrix

The following table defines default retention periods. Data owners may adjust retention periods where required by law, contract, or operational needs.

| Data Type | Classification | Retention Period | Disposal Method |
|---|---|---|---|
| Customer Data | Confidential | Duration of customer relationship + 30 days | Secure deletion |
| Personally Identifiable Information (PII) | Confidential | As long as business purpose exists | Deletion or anonymization |
| Authentication Logs | Confidential | 1 year | Automated deletion |
| Security & Audit Logs | Confidential | 2 years | Automated deletion |
| Incident Reports | Confidential | 3 years | Secure deletion |
| Contracts & Legal Documents | Restricted | 7 years | Secure deletion |
| Financial Records | Confidential | 7 years | Secure deletion |
| Internal Chat Messages (Slack or similar) | Restricted | 5 years | Automated deletion |
| Business Email | Restricted | 5 years | Automated deletion |
| Internal Reports & Presentations | Restricted | 3 years | Secure deletion |
| Source Code | Confidential | Indefinite while product maintained | Secure archival or deletion |
| Marketing Materials | Public | Indefinite | No deletion requirement |

If chat messages or email contain records that fall into another category, such as contracts, finance, HR, security, or incident handling, the longer retention period for that category applies.

Data owners may define additional retention rules specific to their systems.

## Automated Data Deletion

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

## Monitoring and Validation

To ensure compliance with this policy:

- Automated deletion processes must be tested during implementation
- System logs must be reviewed periodically
- Configuration settings must be reviewed during annual policy review
- Any deletion failures must be investigated and corrected

The Security or Engineering team is responsible for validating that retention enforcement operates correctly.

## Evidence and Auditability

To demonstrate compliance with this policy, Grunt AS maintains evidence including:

- System logs showing deletion of expired records
- Automated deletion reports from data systems
- Configuration screenshots demonstrating retention settings
- Documentation of automated deletion scripts or lifecycle rules
- Periodic audit records validating retention enforcement

These records may be used for internal reviews, audits, and compliance verification (e.g., SOC 2).

## Legal Holds

When Grunt AS becomes subject to legal proceedings, investigations, or regulatory requests:

- Relevant data must be preserved regardless of retention schedules
- Data retention automation must exclude records under legal hold
- Legal counsel will determine the duration of the hold

## Roles and Responsibilities

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

## Policy Review

This policy is reviewed annually as part of the Data Management Policy review process to ensure alignment with:

- Legal requirements
- Business needs
- Security practices
- Compliance frameworks
