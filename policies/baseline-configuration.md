# System configuration baseline

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 11, 2026 | Jan Kristian Bjerke | Initial documented baseline configuration. |

## Standards referenced

Grunt AS aligns its system configuration baselines with widely recognized security standards:

- CIS Benchmarks
- NIST SP 800-53
- Cloud provider security best practices (e.g., Azure Security Baseline / AWS Well-Architected Security Pillar)

These baselines define minimum security settings for systems supporting Grunt AS production services.

## Operating systems

| Control | Baseline Configuration | Standard Reference |
|-------|------------------------|-------------------|
| Automatic updates | Enabled for all systems | CIS |
| Firewall | OS firewall enabled | CIS |
| Admin access | Restricted to authorized engineers only | NIST AC-2 |
| Logging | System logs enabled | NIST AU |
| SSH | Key-based authentication only, password login disabled | CIS |

## Cloud infrastructure

| Control | Baseline |
|-------|----------|
| Multi-Factor Authentication | Required for all administrator accounts |
| Identity and Access Management | Least privilege enforced |
| Root/Owner accounts | Not used for daily operations |
| Logging | Cloud activity logging enabled (e.g., Azure Activity Logs / AWS CloudTrail) |
| Monitoring | Cloud monitoring enabled |
| Encryption at rest | Enabled for storage and databases |
| Encryption in transit | TLS required for all services |

## Servers / compute instances

| Control | Baseline |
|-------|----------|
| Operating system images | Standard hardened images used |
| Security patches | Automatically applied or patched monthly |
| Admin access | Restricted through identity provider roles |
| Monitoring | Infrastructure metrics and logs enabled |

## Endpoint software

| Control | Baseline |
|-------|----------|
| Disk encryption | Enabled on all Grunt AS-managed devices |
| Endpoint protection | Installed and active |
| Automatic updates | Enabled for operating system and applications |
| Screen lock | Automatic lock after inactivity |

## Network infrastructure

| Control | Baseline |
|-------|----------|
| Firewall rules | Default deny inbound access |
| Security groups / firewall policies | Least privilege access rules |
| Network segmentation | Public and private network segments separated |
| Network logging | Flow logs enabled where available |

## Databases

| Control | Baseline |
|-------|----------|
| Encryption at rest | Enabled for all databases |
| Encryption in transit | TLS required |
| Public access | Disabled |
| Backups | Automated backups enabled |
| Access control | Role-based access controls enforced |

## Monitoring and logging

Logging and monitoring are configured to detect suspicious activity and support security investigations.

| Control | Baseline |
|-------|----------|
| Infrastructure logs | Enabled |
| Authentication logs | Captured |
| Security alerts | Generated through cloud monitoring tools |
| Log retention | Maintained according to Grunt AS security policies |

## Review process

Configuration baselines are reviewed:

- **Quarterly**
- After **major infrastructure or architecture changes**

Ownership of baseline maintenance: **Engineering**

Changes to configuration baselines require review through the engineering change management process.

## Scope

This baseline applies to:

- Operating systems
- Cloud infrastructure and services
- Servers / compute instances
- Endpoint devices
- Network infrastructure
- Databases

All systems supporting Grunt AS production services must adhere to these baseline configurations.
