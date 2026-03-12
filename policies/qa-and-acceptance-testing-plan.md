# QA and Acceptance Testing Plan
ISO 27001 – Acceptance Testing Control

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 11, 2026 | Jan Kristian Bjerke | Initial documented |


## Purpose

This document defines the quality assurance and acceptance testing process used prior to releasing software to production. The goal is to ensure that software releases meet functional, performance, and security requirements and reduce the risk of introducing vulnerabilities or regressions.

The process integrates automated testing, static analysis, and manual verification before deployment.

---

# Scope

This process applies to all production releases and significant changes to the software systems developed by the organization.

Systems in scope include:

- PowerPoint plugin
- Web services and APIs
- Supporting backend services

---

# Quality Assurance Process

Quality assurance is performed throughout the development lifecycle using automated testing and code quality analysis.

## Unit Testing

Unit tests verify that individual components behave correctly.

Unit tests are executed automatically as part of the continuous integration pipeline.

Purpose:

- Validate business logic
- Prevent regressions
- Ensure predictable behavior of isolated components

Evidence:

- CI pipeline test results
- Test coverage reports

---

## Integration Testing

Integration tests verify that multiple components interact correctly.

These tests validate interactions such as:

- Service-to-service communication
- API behavior
- Data flow between components

Integration tests are executed automatically in the CI pipeline.

Evidence:

- CI test execution logs
- Integration test reports

---

## Static Code Analysis and Security Scanning

All pull requests are scanned using **SonarCloud** to identify:

- Code quality issues
- Security vulnerabilities
- Code smells
- Maintainability problems

This helps detect issues related to common vulnerabilities including those described in the **OWASP Top 10**, such as:

- Injection risks
- Security misconfiguration
- Vulnerable dependencies
- Improper error handling

Pull requests must pass the SonarCloud quality gate before merging.

Evidence:

- SonarCloud scan reports
- Pull request quality gate status

---

# Pull Request Review Process

All code changes must be submitted via a pull request.

Pull requests require:

- Successful CI pipeline execution
- Passing unit and integration tests
- Successful SonarCloud scan
- Peer code review approval

Evidence:

- Pull request history
- Code review approvals
- CI pipeline logs

---

# Acceptance Testing

After a pull request is merged, the changes are deployed to a test environment where acceptance testing is performed.

Acceptance testing may include:

- Manual verification of functionality
- Automated end-to-end tests when applicable
- Verification of user workflows
- Validation that security controls behave as expected

Testing verifies that:

- Functional requirements are satisfied
- The system behaves correctly under normal usage
- No obvious regressions or security issues are present

Evidence:

- Test notes
- Screenshots
- Test logs
- CI test reports (when automated tests are used)

---

# Security Considerations

Security is addressed throughout the development and testing process.

Security controls include:

- Static code analysis through SonarCloud
- Peer code review
- Dependency vulnerability scanning
- Validation of authentication and authorization mechanisms

These practices help identify and mitigate vulnerabilities described in the **OWASP Top 10**.

---

# Evidence Collection

Evidence supporting acceptance testing is maintained through the development and CI/CD tooling.

Examples of evidence include:

- CI pipeline logs
- Unit and integration test results
- SonarCloud analysis reports
- Pull request approvals
- Acceptance testing notes or screenshots

These artifacts demonstrate that required functional, performance, and security checks were completed before deployment.

---

# Final Approval and Deployment

Before deployment to production:

- All automated tests must pass
- SonarCloud quality gates must pass
- Code review approval must be obtained
- Acceptance testing must be completed

Once these requirements are satisfied, the release can be approved for deployment.

Approval is documented through the pull request and deployment pipeline history.