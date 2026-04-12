# Business continuity and disaster recovery plan

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | April 10, 2026 | Engineering | Initial documented business continuity and disaster recovery plan. |

## Purpose

This document defines how Grunt AS maintains service continuity and recovers from disruptions to its systems, infrastructure, or operations.

## Scope

This plan covers all Grunt AS production systems, internal infrastructure, and supporting services.

## Service architecture and resilience

The Grunt PowerPoint add-in is installed and runs locally within the user's environment. Core functionality, including creating and editing charts and visualizations, remains available without a network connection.

The add-in can operate without renewing its license for up to 14 days, after which a connection to the license validation service is required.

This architecture limits the impact of service disruptions on end users.

## Recovery objectives

| Objective | Target |
|-----------|--------|
| Recovery Time Objective (RTO) | 24 hours for hosted services (license validation, online features) |
| Recovery Point Objective (RPO) | 24 hours (daily backups) |

## Backup strategy

| Control | Configuration |
|---------|---------------|
| Backup frequency | Daily |
| Backup retention | 1 year |
| Encryption | Backups encrypted at rest and in transit |
| Storage | Backups stored in a separate location from production systems |

Backup integrity is verified periodically to confirm recoverability.

## Service restoration

In the event of a disruption to hosted services:

1. Engineering assesses the scope and severity of the disruption
2. Affected services are restored from the most recent backup or redeployed from source
3. Data integrity is verified after restoration
4. Stakeholders are notified of the disruption and resolution

## Communication

| Audience | Communication method |
|----------|---------------------|
| Internal team | Direct communication channels (e.g., Slack, email) |
| Affected customers | Email notification describing the issue, impact, and resolution |

## Roles and responsibilities

| Role | Responsibility |
|------|---------------|
| Engineering | Execute recovery procedures, restore services, verify data integrity |
| CTO | Oversee recovery, approve communication to customers |

## Testing and review

This plan is reviewed annually and after any significant incident that triggers recovery procedures.

Recovery procedures are tested periodically to confirm that backups can be restored and services can be brought back online within the stated recovery objectives.
