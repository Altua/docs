# Production data in non-production environments policy

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 13, 2026 | Engineering | Initial documented policy prohibiting the use of production data in development and test environments. |

## Purpose

This policy prohibits the use of production data in development, test, QA, and other non-production environments.

The goal is to reduce the risk of unauthorized exposure of customer data, personally identifiable information (PII), confidential business information, and other sensitive records outside production systems.

## Scope

This policy applies to:

- Development environments
- Test and QA environments
- Staging environments used for validation
- Local developer machines
- Sandbox, demo, and training environments
- All employees, contractors, and service providers who handle Grunt AS systems or data

## Policy statement

Production data must not be copied, restored, replicated, queried into, or otherwise used in non-production environments.

This prohibition applies to full datasets, partial datasets, backups, database exports, logs, support dumps, screenshots, attachments, and any other records derived from production systems when those records contain sensitive or customer-specific information.

If representative data is needed for development or testing, Grunt AS must use one of the following instead:

- Synthetic test data
- Masked data
- Anonymized data
- Sanitized fixtures created for test purposes

## Data classification and handling requirements

The following data must be treated as prohibited in non-production environments unless it has been transformed so that it no longer exposes sensitive production information:

- Customer data
- Personally identifiable information (PII)
- Authentication data
- Secrets and private keys
- Financial records
- Support data containing customer context
- Error logs or diagnostic records containing sensitive fields

Data masking or anonymization must remove or replace values that could identify a customer, user, device, account, or business record.

Masked or anonymized datasets must be reviewed to confirm that re-identification risk is not reasonably possible in the intended non-production environment.

## Approved testing data sources

Non-production environments must use data from approved sources such as:

- Synthetic datasets generated for testing
- Seed data created by engineering for known test scenarios
- Masked or anonymized extracts approved for non-production use
- Demo data created for training or product demonstrations

Production backups, production database snapshots, and raw production exports must not be restored into non-production environments.

## Environment separation and technical controls

Grunt AS maintains separation between production and non-production environments through technical and administrative controls.

These controls include:

- Separate production and non-production systems, accounts, or environments
- Access controls that limit who can retrieve or transfer production data
- Data masking or anonymization before approved use outside production
- Use of synthetic data where possible instead of transformed production data
- Audit logging for access to production data and any approved transformation or transfer process
- Review of automation and scripts that move or prepare data between environments

Non-production systems must not be configured to pull live production data for routine development, testing, QA, or training use.

## Temporary operational access

If production investigation is required for troubleshooting or incident response, review of production data must occur within approved production access controls.

Operational troubleshooting does not permit copying raw production data into a non-production environment.

When a lower-risk representation of production behavior is needed for debugging, engineering must create masked, anonymized, or synthetic data before using it outside production.

## Roles and responsibilities

| Role | Responsibilities |
|------|------------------|
| Engineering | Build and maintain non-production environments that do not rely on raw production data, and implement masking, anonymization, or synthetic data generation where needed. |
| Data owners | Classify data, approve any sanctioned transformed datasets, and confirm that non-production use does not expose sensitive production information. |
| Security or compliance | Review compliance with this policy, review audit evidence, and support investigations of potential violations. |
| Employees and contractors | Follow this policy, use approved test data sources, and report any suspected misuse of production data. |

## Monitoring and review

Grunt AS reviews relevant audit logs, environment configurations, and data handling practices on a periodic basis to verify compliance with this policy.

Reviews may include:

- Access logs for production systems
- Export or backup activity logs
- Records of masking or anonymization jobs
- Environment configuration reviews
- Investigation of unusual transfers or data access patterns

Potential violations must be investigated and remediated promptly.

## Training and awareness

Personnel involved in engineering, QA, support, and system administration must be informed of this policy and trained on the correct handling of production and non-production data.

Training and awareness materials should cover:

- The prohibition on using production data in non-production environments
- Approved alternatives such as synthetic, masked, or anonymized data
- Secure handling of logs, exports, and support artifacts
- How to report suspected violations or control gaps

## Evidence and records

Evidence supporting this policy may include:

- This policy document in the version-controlled documentation repository
- Screenshots or records from masking, anonymization, or synthetic data tooling
- Audit logs showing access and transfer activity
- Environment configuration records showing production and non-production separation
- Training materials or acknowledgments
- Investigation records for suspected policy violations

## Exceptions

Exceptions to this policy require documented approval from management and the data owner, with security review where appropriate.

Any approved exception must define scope, duration, compensating controls, and evidence of review.

Exceptions must not permit unrestricted use of raw production data in non-production environments.

## Review

Engineering reviews this policy at least annually and whenever material changes are made to the development lifecycle, environment architecture, or data handling processes.
