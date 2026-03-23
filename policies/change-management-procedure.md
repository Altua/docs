# Change management procedure

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 23, 2026 | Engineering | Initial documented procedure for GitHub-based change review, approval, and deployment. |

## Purpose

This document defines how Grunt AS manages changes to production systems through its normal GitHub-based engineering workflow.

The goal is to ensure that changes are reviewed, tested, approved, deployed in a controlled way, and documented through the systems already used by engineering.

## Scope

This procedure applies to changes that can affect Grunt AS production services or the security, availability, confidentiality, or integrity of systems and data, including:

- Application code and release packages
- APIs and backend services
- Infrastructure and platform configuration
- Cloud resources and access-controlled services
- Databases and data-processing components
- Security tooling and monitoring configuration
- Third-party SaaS platforms that support business-critical functions

## Core approach

Grunt AS manages changes through the same workflow used for normal software delivery:

- Changes are implemented in a branch and submitted through a pull request.
- Automated checks run in CI before merge or release.
- A reviewer approves the pull request before the change is merged.
- Changes are validated in test or staging when the workflow requires it.
- Production deployment follows the normal release and approval workflow.
- GitHub, CI, and deployment tooling provide the primary audit trail.

## Change types

### Standard changes

Standard changes are low-risk and repeatable changes that still go through the normal engineering workflow.

Examples include routine dependency updates, minor configuration updates, and maintenance changes that use an established implementation path.

### Normal changes

Normal changes are the default category and include most product, infrastructure, configuration, integration, and security-related changes.

These changes follow the normal pull request, review, testing, and deployment process.

### Emergency changes

Emergency changes are changes that must be implemented quickly to resolve an active incident, address a critical vulnerability, restore service, or reduce immediate operational risk.

Emergency changes may use an expedited workflow, but they must still be documented and reviewed after implementation.

## Standard workflow

### Implement the change

The developer or engineer implements the change in the relevant repository or managed system.

When useful, the change should include notes about:

- What is changing
- Why the change is needed
- Any known impact or deployment considerations
- Any rollback, mitigation, or follow-up notes

### Open a pull request

Production-bound code and configuration changes are submitted through a pull request.

The pull request serves as the primary change record and should make the scope of the change understandable to a reviewer.

### Run automated checks

Automated checks run through CI as defined by the repository and release workflow.

These checks may include:

- Build validation
- Unit and integration tests
- Security scanning
- Other required repository or deployment checks

### Review and approval

At least one appropriate reviewer must approve the pull request before merge.

The reviewer is expected to confirm that:

- The change is understandable
- Required checks have passed
- Testing is appropriate for the scope and risk of the change
- Any deployment concerns are documented when relevant

### Validate before production when needed

When the change affects user workflows, integrations, infrastructure behavior, permissions, or release packaging, it should be validated in test or staging before production deployment when such an environment is available.

Validation may include manual QA, smoke testing, review of logs or telemetry, or confirmation that the system behaves as expected.

### Deploy through the release workflow

Production deployment must follow the normal release workflow used by Grunt AS.

This may include deployment pipeline approvals, release checklist steps, or other repository-linked controls already used by engineering.

### Confirm outcome

After deployment, engineering confirms that the change completed successfully.

This confirmation may include:

- Review of deployment status
- Review of logs, telemetry, or alerts
- Verification of affected functionality
- Documentation of rollback or follow-up actions if something went wrong

## Emergency change handling

Emergency changes may bypass parts of the normal sequence when delay would materially increase risk to Grunt AS systems, customer service, or security.

Emergency changes must still:

- Be approved by an authorized person such as engineering leadership, the CTO, or the incident lead
- Be documented in GitHub or the relevant engineering system as soon as practical
- Include the reason for the emergency path
- Be reviewed after implementation to confirm outcome and identify any follow-up actions

## Roles and responsibilities

| Role | Responsibilities |
|------|------------------|
| Developer or implementer | Make the change, document relevant context in the pull request or release workflow, and address issues found during review or testing. |
| Reviewer | Review the pull request, confirm the change is understandable, and verify that required checks and testing are appropriate. |
| Release approver or deployer | Confirm the change is ready for production based on the normal release workflow and approvals in use. |
| Engineering leadership | Support decisions on higher-risk or emergency changes when additional oversight is needed. |

## Required change records

Evidence supporting this procedure may include:

- Pull requests and reviewer approvals
- CI or build logs
- Test or staging validation evidence
- Security scan results when applicable
- Deployment pipeline logs or release history
- Release approval records
- Rollback notes or incident follow-up records

These records are primarily retained in GitHub and the connected CI/CD and deployment systems used by Grunt AS.

## Related policies and processes

This procedure should be read together with:

- QA process
- Security integration tests
- Secure code vulnerability scanning
- System configuration baseline
- Data retention policy

## Exceptions

Exceptions to this procedure require documented approval from engineering leadership.

An approved exception must define the reason, affected systems, duration, and any temporary safeguards that will be used.

## Review

Engineering reviews this procedure at least annually and whenever material changes are made to the release process, deployment controls, or production operating model.
