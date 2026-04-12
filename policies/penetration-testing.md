# Penetration testing

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | April 10, 2026 | Engineering | Initial documented penetration testing policy. |

## Purpose

This policy defines how Grunt AS conducts penetration testing to identify security vulnerabilities in its external-facing systems and services.

## Scope

Penetration testing covers all Grunt AS external-facing infrastructure, APIs, and web applications.

## Testing program

| Aspect | Details |
|--------|---------|
| Type | External penetration testing |
| Frequency | Monthly |
| Performed by | Qualified third-party security testing provider |

## Process

1. Testing scope is defined and agreed upon with the testing provider
2. The provider conducts testing against external-facing systems
3. Findings are documented in a report with severity ratings and remediation guidance
4. Engineering reviews findings and prioritizes remediation
5. Remediation is tracked through the standard vulnerability management process (see vulnerability identification and prioritization policy)
6. Retesting confirms that critical and high-severity findings have been addressed

## Severity and remediation targets

Remediation timelines follow the vulnerability identification and prioritization policy:

| Severity | Target remediation |
|----------|-------------------|
| Critical | 7 days |
| High | 30 days |
| Medium | 90 days |
| Low | Normal engineering backlog |

## Roles and responsibilities

| Role | Responsibility |
|------|---------------|
| CTO | Oversees the testing program and reviews results |
| Engineering | Remediates identified vulnerabilities |
| Third-party provider | Conducts testing and delivers reports |

## Records

Penetration test reports are retained and available for review during audits and compliance assessments.

## Review

This policy is reviewed annually and updated based on changes to infrastructure, services, or risk profile.
