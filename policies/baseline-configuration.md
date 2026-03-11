# System Configuration Baseline – Grunt

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 11, 2026 | Jan Kristian Bjerke | Initial documented baseline configuration. |

## Standards Referenced

Grunt aligns its system configuration baselines with widely recognized security standards:

- CIS Benchmarks
- NIST SP 800-53
- Cloud provider security best practices (e.g., Azure Security Baseline / AWS Well-Architected Security Pillar)

These baselines define minimum security settings for systems in scope for the company’s SOC 2 program.

---

# 1. Operating Systems

| Control | Baseline Configuration | Standard Reference |
|-------|------------------------|-------------------|
| Automatic updates | Enabled for all systems | CIS |
| Firewall | OS firewall enabled | CIS |
| Admin access | Restricted to authorized engineers only | NIST AC-2 |
| Logging | System logs enabled | NIST AU |
| SSH | Key-based authentication only, password login disabled | CIS |

---

# 2. Cloud Infrastructure

| Control | Baseline |
|-------|----------|
| Multi-Factor Authentication | Required for all administrator accounts |
| Identity and Access Management | Least privilege enforced |
| Root/Owner accounts | Not used for daily operations |
| Logging | Cloud activity logging enabled (e.g., Azure Activity Logs / AWS CloudTrail) |
| Monitoring | Cloud monitoring enabled |
| Encryption at rest | Enabled for storage and databases |
| Encryption in transit | TLS required for all services |

---

# 3. Servers / Compute Instances

| Control | Baseline |
|-------|----------|
| Operating system images | Standard hardened images used |
| Security patches | Automatically applied or patched monthly |
| Admin access | Restricted through identity provider roles |
| Monitoring | Infrastructure metrics and logs enabled |

---

# 4. Endpoint Software

| Control | Baseline |
|-------|----------|
| Disk encryption | Enabled on all company devices |
| Endpoint protection | Installed and active |
| Automatic updates | Enabled for operating system and applications |
| Screen lock | Automatic lock after inactivity |

---

# 5. Network Infrastructure

| Control | Baseline |
|-------|----------|
| Firewall rules | Default deny inbound access |
| Security groups / firewall policies | Least privilege access rules |
| Network segmentation | Public and private network segments separated |
| Network logging | Flow logs enabled where available |

---

# 6. Databases

| Control | Baseline |
|-------|----------|
| Encryption at rest | Enabled for all databases |
| Encryption in transit | TLS required |
| Public access | Disabled |
| Backups | Automated backups enabled |
| Access control | Role-based access controls enforced |

---

# 7. Monitoring and Logging

Logging and monitoring are configured to detect suspicious activity and support security investigations.

| Control | Baseline |
|-------|----------|
| Infrastructure logs | Enabled |
| Authentication logs | Captured |
| Security alerts | Generated through cloud monitoring tools |
| Log retention | Maintained according to company security policies |

---

# 8. Review Process

Configuration baselines are reviewed:

- **Quarterly**
- After **major infrastructure or architecture changes**

Ownership of baseline maintenance: **Engineering**

Changes to configuration baselines require review through the engineering change management process.

---

# 9. Scope

This baseline applies to:

- Operating systems
- Cloud infrastructure and services
- Servers / compute instances
- Endpoint devices
- Network infrastructure
- Databases

All systems supporting Grunt production services must adhere to these baseline configurations.

---
