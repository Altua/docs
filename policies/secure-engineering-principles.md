# Secure engineering principles and planning

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.1 | March 16, 2026 | Engineering | Updated to align with Vanta guidance for standards alignment, lifecycle practices, approval, and training. |
| 1.0 | March 13, 2026 | Engineering | Initial documented secure engineering principles policy. |

## Document control

| Field | Value |
|-------|-------|
| Owner | Engineering |
| Approved by | Engineering leadership or designated security governance personnel |
| Review cadence | Annual, and after major architectural or software delivery changes |

## Purpose

This document defines Grunt AS's guiding principles for secure engineering.

It provides a common framework for designing, building, testing, deploying, operating, and maintaining systems in a way that reduces security risk and supports reliable operations.

These principles support Grunt AS security objectives and are informed by secure engineering practices described in standards and guidance such as SOC 2, OWASP, and NIST SP 800-160 revision 1.

## Scope

This policy applies to:

- Applications, services, APIs, and integrations developed or maintained by Grunt AS
- Supporting infrastructure and deployment configurations
- Engineering employees, contractors, and third-party development partners
- All phases of the software and system lifecycle

The principles in this document should be maintained in collaboration with engineering, product, and security stakeholders so that they continue to reflect current architecture, delivery practices, and risk priorities.

## Guiding principles

### Security by design

Security considerations must be incorporated from the earliest stages of requirements, design, and architecture work.

Engineering should identify security-relevant assumptions, trust boundaries, data flows, and misuse cases before implementation begins.

Threat modeling should be performed when changes introduce new architecture, data flows, trust boundaries, external integrations, authentication paths, or other meaningful security risk.

### Least privilege and access control

Users, services, applications, and administrators must receive only the access needed to perform their intended function.

Access must be reviewed and controlled through authenticated and authorized mechanisms, with stronger controls for privileged or production access.

### Defense in depth

Security controls must not rely on a single point of protection.

Grunt AS uses layered controls across identity, application logic, infrastructure configuration, logging, monitoring, and operational response.

### Secure defaults

Systems and applications must be deployed with secure defaults enabled.

Insecure settings, legacy options, anonymous access, and unnecessary services must be disabled unless there is a documented business need and approved exception.

### Data protection and environment separation

Sensitive data must be protected according to its classification throughout the engineering lifecycle.

Production data must not be used in development or test environments except in accordance with approved masking, anonymization, or other documented controls.

### Transparency and auditability

Security-relevant actions must be logged with enough detail to support investigation, review, and compliance verification.

Logs, deployment records, pull request history, and security scan results must be retained in the systems that generate them.

### Resilience and recovery

Systems should be designed to tolerate faults, recover from failure, and limit business disruption.

Engineering should consider redundancy, backups, rollback paths, and operational recovery requirements when designing and changing production systems.

### Secure software delivery

Security checks must be integrated into the software delivery process rather than deferred until release.

Code changes should pass review, testing, and security validation before deployment to production.

### Continuous improvement

Engineering practices must evolve based on incidents, vulnerability findings, audit observations, architectural changes, and changes in threat conditions.

Recurring issues should feed back into design patterns, tooling, standards, and training.

## Secure engineering practices across the lifecycle

| Phase | Engineering practices | Security expectations | Example evidence |
|-------|-----------------------|-----------------------|------------------|
| Requirements | Define business and technical requirements, including data sensitivity and environment use | Security-relevant requirements and constraints are identified early | Tickets, design notes, architecture notes |
| Design | Review architecture, data flows, dependencies, trust boundaries, failure modes, and threat scenarios | Security by design, least privilege, threat modeling, and data handling requirements are considered before build | Design documents, architecture diagrams, threat models, risk notes |
| Implementation | Use secure coding practices, approved libraries, and peer review through pull requests | Security-impacting changes are visible, reviewable, and traceable | Pull requests, code review approvals, commit history |
| Testing | Run unit tests, integration tests, QA validation, and automated security checks | Functional and security defects are identified before release | GitHub Actions workflow logs, test reports, SonarCloud results |
| Deployment | Release through approved deployment and change processes | Production changes are validated, approved, and deployed with secure configuration | Deployment history, release approvals, change records |
| Operations | Monitor systems, logs, alerts, and anomalous behavior | Security events can be detected, investigated, and acted on | Monitoring dashboards, log exports, alert records |
| Maintenance | Patch systems and dependencies, review vulnerabilities, and improve controls | Known weaknesses are remediated and lessons learned are applied | Dependabot alerts, remediation pull requests, patch records |

## Engineering control expectations

The following controls are expected as part of secure engineering at Grunt AS:

- Security-relevant design review for material changes
- Threat modeling for changes with meaningful security impact
- Pull requests for production code changes
- Peer review before merge
- Secure coding practices during implementation
- Automated build and test validation
- Static analysis and security scanning where configured
- Dependency vulnerability monitoring and remediation
- QA validation for changes that affect user-facing or critical workflows
- Release approval before production deployment
- Logging and monitoring for production systems
- Protection of sensitive data according to classification and environment rules

## Roles and responsibilities

| Role | Responsibilities |
|------|------------------|
| Engineering | Apply these principles in design, implementation, testing, deployment, and maintenance work. |
| Product stakeholders | Contribute business context, workflow impact, and risk-relevant requirements during planning and review. |
| Reviewers and approvers | Confirm that changes meet review, testing, and security expectations before release. |
| Engineering leadership | Maintain engineering standards, approve exceptions where appropriate, and ensure secure delivery practices remain effective. |
| Security or compliance | Support policy review, evidence collection, and follow-up on control gaps or audit findings. |

## Evidence and records

Evidence supporting this policy may include:

- Architecture or design records
- Pull request history and review approvals
- GitHub Actions workflow logs
- SonarCloud scan results
- Dependabot alerts and remediation records
- QA or release validation records
- Deployment and change approval records
- Production monitoring and alert records

## Communication and training

Engineering personnel must be informed of these principles and how they apply to day-to-day design, implementation, review, and release work.

Training or awareness activities should cover:

- How to apply secure design and threat modeling during planning
- Secure coding and peer review expectations
- Dependency management and vulnerability remediation responsibilities
- Release, QA, and approval expectations before production deployment
- Protection of sensitive and production data during engineering work

## Related policies and processes

This policy should be read together with:

- QA Process
- Secure Code Vulnerability Scanning
- Production Data in Non-Production Environments Policy
- Data Management Policy

## Exceptions

Exceptions to these principles require documented approval from management and the relevant owner.

Any approved exception must define scope, duration, risk, and compensating controls.

## Review

Engineering reviews this policy at least annually and whenever material changes are made to the software delivery lifecycle, engineering tooling, or security requirements.
