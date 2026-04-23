# Patch management

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | April 10, 2026 | Engineering | Initial documented patch management policy. |

## Purpose

This policy defines how Grunt AS identifies, evaluates, and applies patches and updates to its systems, applications, and infrastructure.

## Scope

This policy applies to all Grunt AS systems, including:

- Operating systems
- Cloud infrastructure and services
- Servers and compute instances
- Endpoint devices
- Applications and dependencies
- Network infrastructure

## Patching approach

| System type | Approach | Frequency |
|-------------|----------|-----------|
| Operating systems | Automatic updates enabled | Continuous |
| Endpoint devices | Automatic OS and application updates enabled | Continuous |
| Servers / compute instances | Automatically applied or patched monthly | Monthly |
| Application dependencies | Monitored via GitHub Dependabot with security alerts | Continuous monitoring |
| Cloud infrastructure | Managed service patches applied by provider; configuration reviewed quarterly | Ongoing |

## Prioritization

Patches are prioritized based on severity and exploitability, following the vulnerability identification and prioritization policy:

| Severity | Target |
|----------|--------|
| Critical (actively exploited, RCE, auth bypass) | 7 days |
| High (serious weakness with production impact) | 30 days |
| Medium (valid issue, moderate impact) | 90 days |
| Low (low impact, low exploitability) | Normal engineering backlog |

## Process

1. Patches are identified through automated monitoring (Dependabot, OS update services, cloud provider advisories)
2. Critical and high-severity patches are evaluated and applied promptly
3. Patches are tested where applicable before deployment to production
4. Deployment is verified and monitored for issues
5. Patching activity is recorded through CI/CD logs, deployment records, and Dependabot alerts

## Roles and responsibilities

| Role | Responsibility |
|------|---------------|
| Engineering | Apply patches, verify deployment, monitor for issues |
| CTO | Oversee patching program, approve exceptions for deferred patches |

## Exceptions

If a patch cannot be applied within the target timeline, the exception must be documented with a justification and an alternative remediation plan.

## Review

This policy is reviewed annually and updated based on changes to infrastructure, tooling, or risk profile.
