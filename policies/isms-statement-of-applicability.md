# ISMS statement of applicability

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.1 | May 11, 2026 | Jan Kristian Bjerke | Reformatted the statement of applicability for the documentation repository, removed duplicate control rows, updated controls 8.4, 8.6, and 8.14 to be in scope, and marked all applicable controls as implemented. |
| 1.0 | February 9, 2026 | Mads Gedde | Initial statement of applicability. Approved by Einar Bjering. |

## Purpose

This statement of applicability defines which ISO/IEC 27001:2022 Annex A controls apply to the Grunt AS information security management system (ISMS).

It records control applicability, implementation status, and exclusions.

## Scope

This document applies to the Grunt AS ISMS and the systems, people, processes, and third-party services that support Grunt AS products and operations.

## Applicability approach

Grunt AS includes controls when they are required by legal, regulatory, contractual, business, or risk-based needs.

Controls marked as excluded are not applicable to the current Grunt AS operating model. Exclusion justifications are documented in this statement.

Implementation evidence and detailed control tracking are maintained in Vanta.

## Status definitions

| Status | Meaning |
|--------|---------|
| Implemented | The control is implemented and evidence is maintained. |
| In progress | The control is applicable and implementation or evidence collection is in progress. |
| Not started | The control is applicable but implementation has not started. |
| Excluded | The control is not applicable to the current ISMS scope. |

## Summary

| Status | Count |
|--------|-------|
| Implemented | 90 |
| In progress | 0 |
| Not started | 0 |
| Excluded | 3 |
| Total unique controls | 93 |

## Organizational controls

| Control | Name | Applicability | Status | Notes |
|---------|------|---------------|--------|-------|
| 5.1 | Policies for information security | Applicable | Implemented | |
| 5.2 | Information security roles and responsibilities | Applicable | Implemented | |
| 5.3 | Segregation of duties | Applicable | Implemented | |
| 5.4 | Management responsibilities | Applicable | Implemented | |
| 5.5 | Contact with authorities | Applicable | Implemented | |
| 5.6 | Contact with special interest groups | Applicable | Implemented | |
| 5.7 | Threat intelligence | Applicable | Implemented | |
| 5.8 | Information security in project management | Applicable | Implemented | |
| 5.9 | Inventory of information and other associated assets | Applicable | Implemented | |
| 5.10 | Acceptable use of information and other associated assets | Applicable | Implemented | |
| 5.11 | Return of assets | Applicable | Implemented | |
| 5.12 | Classification of information | Applicable | Implemented | |
| 5.13 | Labelling of information | Applicable | Implemented | |
| 5.14 | Information transfer | Applicable | Implemented | |
| 5.15 | Access control | Applicable | Implemented | |
| 5.16 | Identity management | Applicable | Implemented | |
| 5.17 | Authentication information | Applicable | Implemented | |
| 5.18 | Access rights | Applicable | Implemented | |
| 5.19 | Information security in supplier relationships | Applicable | Implemented | |
| 5.20 | Addressing information security within supplier agreements | Applicable | Implemented | |
| 5.21 | Managing information security in the ICT supply chain | Applicable | Implemented | |
| 5.22 | Monitoring, review, and change management of supplier services | Applicable | Implemented | |
| 5.23 | Information security for use of cloud services | Applicable | Implemented | |
| 5.24 | Information security incident management planning and preparation | Applicable | Implemented | |
| 5.25 | Assessment and decision on information security events | Applicable | Implemented | |
| 5.26 | Response to information security incidents | Applicable | Implemented | |
| 5.27 | Learning from information security incidents | Applicable | Implemented | |
| 5.28 | Collection of evidence | Applicable | Implemented | |
| 5.29 | Information security during disruption | Applicable | Implemented | |
| 5.30 | ICT readiness for business continuity | Applicable | Implemented | |
| 5.31 | Legal, statutory, regulatory, and contractual requirements | Applicable | Implemented | |
| 5.32 | Intellectual property rights | Applicable | Implemented | |
| 5.33 | Protection of records | Applicable | Implemented | |
| 5.34 | Privacy and protection of PII | Applicable | Implemented | |
| 5.35 | Independent review of information security | Applicable | Implemented | |
| 5.36 | Compliance with policies, rules, and standards for information security | Applicable | Implemented | |
| 5.37 | Documented operating procedures | Applicable | Implemented | |

## People controls

| Control | Name | Applicability | Status | Notes |
|---------|------|---------------|--------|-------|
| 6.1 | Screening | Applicable | Implemented | |
| 6.2 | Terms and conditions of employment | Applicable | Implemented | |
| 6.3 | Information security awareness, education, and training | Applicable | Implemented | |
| 6.4 | Disciplinary process | Applicable | Implemented | |
| 6.5 | Responsibilities after termination or change of employment | Applicable | Implemented | |
| 6.6 | Confidentiality or non-disclosure agreements | Applicable | Implemented | |
| 6.7 | Remote working | Applicable | Implemented | |
| 6.8 | Information security event reporting | Applicable | Implemented | |

## Physical controls

| Control | Name | Applicability | Status | Notes |
|---------|------|---------------|--------|-------|
| 7.1 | Physical security perimeters | Applicable | Implemented | |
| 7.2 | Physical entry | Applicable | Implemented | |
| 7.3 | Securing offices, rooms, and facilities | Applicable | Implemented | |
| 7.4 | Physical security monitoring | Applicable | Implemented | |
| 7.5 | Protecting against physical and environmental threats | Applicable | Implemented | |
| 7.6 | Working in secure areas | Applicable | Implemented | |
| 7.7 | Clear desk and clear screen | Applicable | Implemented | |
| 7.8 | Equipment siting and protection | Applicable | Implemented | |
| 7.9 | Security of assets off-premises | Applicable | Implemented | |
| 7.10 | Storage media | Applicable | Implemented | |
| 7.11 | Supporting utilities | Not applicable | Excluded | Grunt AS does not operate company-managed data centers, server rooms, or production hosting facilities. Supporting utilities for production infrastructure are managed by third-party cloud and hosting providers. |
| 7.12 | Cabling security | Not applicable | Excluded | Grunt AS does not manage physical network or power cabling for production infrastructure. Cabling security for hosting environments is managed by third-party cloud and hosting providers. |
| 7.13 | Equipment maintenance | Not applicable | Excluded | Grunt AS does not operate physical server or network equipment for production infrastructure. Maintenance of hosting infrastructure is managed by third-party providers, while employee endpoint devices are covered by endpoint and asset handling controls. |
| 7.14 | Secure disposal or re-use of equipment | Applicable | Implemented | |

## Technological controls

| Control | Name | Applicability | Status | Notes |
|---------|------|---------------|--------|-------|
| 8.1 | User endpoint devices | Applicable | Implemented | |
| 8.2 | Privileged access rights | Applicable | Implemented | |
| 8.3 | Information access restriction | Applicable | Implemented | |
| 8.4 | Access to source code | Applicable | Implemented | Grunt AS maintains proprietary product source code, so repository access is within the ISMS scope and must be restricted to authorized personnel. |
| 8.5 | Secure authentication | Applicable | Implemented | |
| 8.6 | Capacity management | Applicable | Implemented | Grunt AS operates hosted services for license validation, APIs, online features, and supporting systems, so capacity management is within the ISMS scope even when infrastructure is provided by cloud hosting providers. |
| 8.7 | Protection against malware | Applicable | Implemented | |
| 8.8 | Management of technical vulnerabilities | Applicable | Implemented | |
| 8.9 | Configuration management | Applicable | Implemented | |
| 8.10 | Information deletion | Applicable | Implemented | |
| 8.11 | Data masking | Applicable | Implemented | |
| 8.12 | Data leakage prevention | Applicable | Implemented | |
| 8.13 | Information backup | Applicable | Implemented | |
| 8.14 | Redundancy of information processing facilities | Applicable | Implemented | Redundancy is addressed through cloud provider resilience, backups, continuity planning, and Grunt-managed monitoring controls. |
| 8.15 | Logging | Applicable | Implemented | |
| 8.16 | Monitoring activities | Applicable | Implemented | |
| 8.17 | Clock synchronization | Applicable | Implemented | |
| 8.18 | Use of privileged utility programs | Applicable | Implemented | |
| 8.19 | Installation of software on operational systems | Applicable | Implemented | |
| 8.20 | Networks security | Applicable | Implemented | |
| 8.21 | Security of network services | Applicable | Implemented | |
| 8.22 | Segregation of networks | Applicable | Implemented | |
| 8.23 | Web filtering | Applicable | Implemented | |
| 8.24 | Use of cryptography | Applicable | Implemented | |
| 8.25 | Secure development life cycle | Applicable | Implemented | |
| 8.26 | Application security requirements | Applicable | Implemented | |
| 8.27 | Secure system architecture and engineering principles | Applicable | Implemented | |
| 8.28 | Secure coding | Applicable | Implemented | |
| 8.29 | Security testing in development and acceptance | Applicable | Implemented | |
| 8.30 | Outsourced development | Applicable | Implemented | |
| 8.31 | Separation of development, test, and production environments | Applicable | Implemented | |
| 8.32 | Change management | Applicable | Implemented | |
| 8.33 | Test information | Applicable | Implemented | |
| 8.34 | Protection of information systems during audit testing | Applicable | Implemented | |

## Review

The ISMS owner reviews this statement of applicability at least annually and when there are material changes to the ISMS scope, risk assessment, legal obligations, supplier model, or control implementation status.
