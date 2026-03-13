# QA process

Effective date: March 13, 2026

Owner: Engineering

Review cadence: Annual, and after material changes to the development lifecycle

Source of record: `policies/qa-process.md` in the company version-controlled documentation repository

## Purpose

This document defines how Grunt tests software changes before release to production.

The goal is to ensure that each release passes automated checks, receives the required review, and is validated in a test or staging environment before deployment.

## Scope

This process applies to production-bound changes for:

- PowerPoint add-in releases
- Web applications
- APIs and backend services
- Infrastructure changes that can affect application behavior

## Workflow overview

Software changes move through the following QA workflow:

```text
Development
  -> Pull request
  -> Automated checks in CI
  -> Peer review
  -> Deploy to test or staging
  -> Manual QA or UAT
  -> Release approval
  -> Production deployment
```

## Roles and responsibilities

| Role | Responsibilities |
|------|------------------|
| Developer | Implement the change, write or update automated tests, document change-specific QA notes, and fix defects found during testing. |
| Peer reviewer | Review the pull request, confirm the change is understandable and testable, and verify that required automated checks have passed. |
| QA tester, product manager, or designated business reviewer | Perform manual validation or user acceptance testing for changes that affect user workflows, and record the outcome. |
| Release approver | Confirm that required QA evidence exists, that blocking defects are resolved, and that the change is approved for production release. |

## QA steps

### 1. Development and local verification

Before opening a pull request, the developer:

- Implements the change
- Updates unit or integration tests when behavior changes
- Runs relevant local checks when practical
- Records any known limitations or test notes in the pull request

### 2. Pull request and automated checks

All production code changes must be submitted through a pull request.

The CI pipeline runs automated checks such as:

- Unit tests
- Integration tests
- Build validation
- Static analysis and security scanning

When used for a repository, GitHub Actions workflow runs and SonarCloud quality gates serve as the primary system evidence for these checks.

### 3. Peer review

At least one qualified reviewer must review the pull request before merge.

The reviewer confirms:

- The change matches the stated scope
- Required automated checks passed
- Test coverage is appropriate for the risk of the change
- Deployment or rollback concerns are documented when needed

### 4. Test or staging environment validation

After merge, the change is validated in a test or staging environment when the release process includes one.

Validation may include:

- Smoke testing of core workflows
- Verification of configuration changes
- API or integration checks
- Review of logs, alerts, or telemetry for abnormal behavior

### 5. Manual QA and user acceptance testing

Manual QA is required when a change affects user-facing behavior, critical workflows, integrations, permissions, billing, or release packaging.

Manual QA or UAT may be completed by a QA tester, product manager, or another designated reviewer who can validate expected behavior.

Manual validation should cover:

- Primary user workflows
- Regression checks for affected areas
- Error handling and edge cases relevant to the change
- Any release-specific acceptance criteria

### 6. Release approval

Production deployment requires an explicit release approval after required QA steps are complete.

Approval may be recorded through:

- Pull request approval
- Deployment workflow approval
- Release checklist completion
- Ticket or release note sign-off

## Release readiness requirements

Before a release moves to production, the following conditions must be satisfied:

- Code changes were submitted through a pull request
- Required unit tests passed
- Required integration tests passed
- Build and CI checks passed
- Static analysis and security scans passed
- Peer review approval was recorded
- Test or staging validation was completed when applicable
- Manual QA or UAT was completed for user-impacting changes
- QA results were documented in the pull request, ticket, or release notes
- Release approval was recorded before production deployment

## Required QA records

The following records may be used as audit evidence:

- Pull requests with reviewer approvals
- CI or GitHub Actions workflow logs showing test stages
- SonarCloud scan results or quality gate status
- Test coverage reports
- Manual QA checklists
- Regression test notes
- User acceptance testing notes or sign-off
- Screenshots or excerpts of release pipeline stages
- Deployment records showing the approval gate before production

## Evidence retention and storage

Grunt stores this process document in a shared, version-controlled location in the company documentation repository.

QA evidence is retained in the systems that produce it, such as source control, CI/CD tooling, test management notes, and release records.

## Review and maintenance

Engineering reviews this process at least annually and whenever the release workflow changes materially.

Updates must reflect current engineering practices, tooling, and approval responsibilities.

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 13, 2026 | Engineering | Initial documented QA process for pre-release testing, review, and approval. |
