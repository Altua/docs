# Secure code vulnerability scanning

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 11, 2026 | Jan Kristian Bjerke | Initial documented |

## Purpose
This document describes the process used by the engineering team to identify and remediate security vulnerabilities in application code and dependencies before deployment. The process ensures that code changes are automatically scanned and reviewed as part of the development workflow.

## Scope
This process applies to all application source code maintained in Grunt AS GitHub repositories.

## Tools used
The following tools are used to detect vulnerabilities in source code and dependencies:

- **SonarCloud** – Static Application Security Testing (SAST) and code quality analysis
- **GitHub Dependabot** – Dependency vulnerability detection
- **GitHub Actions** – CI/CD pipeline used to run automated scans
- **Vanta** – Security monitoring and compliance reporting

## Vulnerability scanning process

### Static code analysis
All code changes are scanned using **SonarCloud**.

- SonarCloud scans are automatically triggered via **GitHub Actions**.
- Scans run on:
  - Every **Pull Request**
  - Updates to **main branches**
- The CI/CD pipeline blocks merges if the SonarCloud quality gate fails or if critical security issues are detected.
- Scan results include timestamps, vulnerability details, and remediation guidance.

### Dependency vulnerability monitoring
All repositories have **Dependabot security alerts** enabled.

Dependabot continuously monitors project dependencies against known vulnerability databases. When a vulnerable dependency is detected:

1. GitHub generates a security alert.
2. Notifications are sent to repository maintainers.
3. Vanta monitors Dependabot alerts and surfaces them as compliance notifications.
4. The engineering team reviews the alert and upgrades the dependency to a secure version.

### Vulnerability remediation
When vulnerabilities are identified:

- The engineering team reviews the issue and determines remediation steps.
- Fixes are implemented through pull requests in GitHub.
- Updated code is rescanned by SonarCloud as part of the pull request workflow.
- The issue is considered resolved once the vulnerability is remediated and the scan passes.

## Roles and responsibilities
The **CTO** is responsible for overseeing the vulnerability scanning configuration and ensuring that identified vulnerabilities are reviewed and remediated.

All engineers are responsible for addressing vulnerabilities identified in their code during the pull request review process.

## Evidence and records
Evidence demonstrating the operation of this control may include:

- SonarCloud scan reports and dashboards
- GitHub Actions workflow logs showing security scans
- Dependabot security alerts
- Pull requests addressing dependency upgrades
- Vanta alerts and remediation records

These records include timestamps and responsible personnel and can be retrieved from GitHub, SonarCloud, and Vanta for audit purposes.

## Review
This process is reviewed annually by Grunt AS to ensure continued effectiveness.
