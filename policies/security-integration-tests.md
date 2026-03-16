# Security integration tests

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 16, 2026 | Engineering | Initial documented process for automated security testing in CI/CD. |

## Purpose

This document defines how Grunt AS integrates automated security testing into the software delivery lifecycle.

The goal is to identify security weaknesses early, block risky changes before release, and maintain evidence that security testing is continuously applied during development and deployment workflows.

## Scope

This process applies to source code, dependencies, and release workflows for Grunt AS applications and services that are developed through GitHub-based engineering workflows.

## Security testing approach

Grunt AS integrates automated security testing into CI/CD so that code changes are reviewed for security issues during normal development workflows.

The current automated security testing model includes:

- Static Application Security Testing (SAST) through SonarCloud
- Software Composition Analysis (SCA) and dependency monitoring through GitHub Dependabot
- CI/CD enforcement through GitHub Actions or equivalent GitHub-integrated workflow controls

Dynamic Application Security Testing (DAST) may be performed when applicable to an exposed application or service, but it is not the primary standard control documented in this process.

## Testing tools and coverage

| Test type | Tool or method | Purpose | Execution point |
|-----------|----------------|---------|-----------------|
| SAST | SonarCloud | Identify code quality issues, security issues, and insecure coding patterns in application source code | Pull requests and main branch updates through GitHub CI integration |
| SCA | GitHub Dependabot | Identify vulnerable third-party packages and dependency risks | Continuous monitoring with alerts and remediation through pull requests |
| CI enforcement | GitHub Actions or GitHub-integrated workflow controls | Ensure automated checks run before merge or release | Pull request and build pipeline execution |
| DAST | Performed when applicable | Validate running application behavior for internet-facing or high-risk services when needed | Outside the standard baseline unless specifically required |

## CI/CD integration

Security testing is integrated into the development workflow through GitHub-based CI.

For repositories that use SonarCloud, scans are triggered automatically during pull request validation and on relevant branch updates.

The pipeline is expected to:

- Run automated build and validation steps
- Run SonarCloud analysis as part of CI
- Surface scan results in the pull request or connected dashboard
- Prevent merge or require remediation when quality gates or required checks fail

Dependabot continuously monitors dependencies and creates security alerts when vulnerable packages are identified.

## Frequency

Automated security testing runs according to the following cadence:

- SAST: On pull requests and relevant branch updates
- SCA: Continuously through dependency monitoring and security alerts
- DAST: When applicable to the system under review or when explicitly required for a release, project, or risk review

## Review and remediation process

When a security issue is identified:

- Engineering reviews the finding
- The issue is triaged based on severity, exploitability, and affected scope
- Fixes are implemented through pull requests
- Updated code is rescanned through the normal CI workflow
- The issue is considered resolved when the remediation is merged and the required checks pass

Dependency findings are reviewed and remediated through package upgrades, configuration changes, or documented risk decisions where appropriate.

## Roles and responsibilities

| Role | Responsibilities |
|------|------------------|
| Engineering | Maintain secure code, review findings, remediate valid issues, and ensure fixes pass CI before release. |
| Reviewers and approvers | Confirm that required security checks passed and that unresolved findings are handled appropriately before merge or deployment. |
| Engineering leadership | Maintain the testing approach, ensure tooling remains in use, and support remediation priorities when material issues are identified. |
| Security or compliance | Support evidence collection, review control effectiveness, and follow up on recurring or unresolved security findings. |

## Evidence and records

Evidence supporting this process may include:

- SonarCloud dashboards and scan reports
- GitHub Actions workflow logs or pull request status checks showing security scans
- Dependabot security alerts
- Pull requests that remediate security or dependency findings
- Quality gate results tied to pull requests
- Security testing screenshots or exported reports

These records provide the primary evidence that security testing is integrated into the engineering workflow.

## Dashboards and monitoring

SonarCloud dashboards and GitHub security views provide ongoing visibility into identified issues, code quality gates, and dependency findings.

Engineering and relevant reviewers use these systems to monitor open findings and verify that required security checks have run as expected.

## Training and awareness

Engineering personnel should be informed of:

- How SonarCloud findings appear in the development workflow
- How to review and remediate SAST findings
- How Dependabot alerts are triaged and resolved
- When additional dynamic testing may be required
- The expectation that security testing is part of normal pull request and release work

Training records, team guidance, or onboarding materials may be retained as supporting evidence.

## Related policies and processes

This document should be read together with:

- Secure Code Vulnerability Scanning
- Secure Engineering Principles and Planning
- QA Process

## Review

Engineering reviews this process at least annually and whenever material changes are made to CI/CD tooling, repository controls, or the automated security testing approach.
