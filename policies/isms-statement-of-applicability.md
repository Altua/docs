# ISMS statement of applicability

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.1 | May 11, 2026 | Mads Gedde | Reformatted the statement of applicability for the documentation repository and removed duplicate control rows. |
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
| Implemented | 14 |
| In progress | 64 |
| Not started | 11 |
| Excluded | 4 |
| Total unique controls | 93 |

## Organizational controls

| Control | Name | Applicability | Status | Notes |
|---------|------|---------------|--------|-------|
| 5.1 | Policies for information security | Applicable | In progress | |
| 5.2 | Information security roles and responsibilities | Applicable | Implemented | |
| 5.3 | Segregation of duties | Applicable | In progress | |
| 5.4 | Management responsibilities | Applicable | In progress | |
| 5.5 | Contact with authorities | Applicable | Not started | |
| 5.6 | Contact with special interest groups | Applicable | In progress | |
| 5.7 | Threat intelligence | Applicable | In progress | |
| 5.8 | Information security in project management | Applicable | In progress | |
| 5.9 | Inventory of information and other associated assets | Applicable | In progress | |
| 5.10 | Acceptable use of information and other associated assets | Applicable | Implemented | |
| 5.11 | Return of assets | Applicable | In progress | |
| 5.12 | Classification of information | Applicable | Implemented | |
| 5.13 | Labelling of information | Applicable | Implemented | |
| 5.14 | Information transfer | Applicable | In progress | |
| 5.15 | Access control | Applicable | In progress | |
| 5.16 | Identity management | Applicable | In progress | |
| 5.17 | Authentication information | Applicable | In progress | |
| 5.18 | Access rights | Applicable | In progress | |
| 5.19 | Information security in supplier relationships | Applicable | In progress | |
| 5.20 | Addressing information security within supplier agreements | Applicable | In progress | |
| 5.21 | Managing information security in the ICT supply chain | Applicable | In progress | |
| 5.22 | Monitoring, review, and change management of supplier services | Applicable | In progress | |
| 5.23 | Information security for use of cloud services | Applicable | Implemented | |
| 5.24 | Information security incident management planning and preparation | Applicable | In progress | |
| 5.25 | Assessment and decision on information security events | Applicable | In progress | |
| 5.26 | Response to information security incidents | Applicable | In progress | |
| 5.27 | Learning from information security incidents | Applicable | In progress | |
| 5.28 | Collection of evidence | Applicable | Not started | |
| 5.29 | Information security during disruption | Applicable | Not started | |
| 5.30 | ICT readiness for business continuity | Applicable | Not started | |
| 5.31 | Legal, statutory, regulatory, and contractual requirements | Applicable | Not started | |
| 5.32 | Intellectual property rights | Applicable | In progress | |
| 5.33 | Protection of records | Applicable | In progress | |
| 5.34 | Privacy and protection of PII | Applicable | Not started | |
| 5.35 | Independent review of information security | Applicable | In progress | |
| 5.36 | Compliance with policies, rules, and standards for information security | Applicable | In progress | |
| 5.37 | Documented operating procedures | Applicable | Not started | |

## People controls

| Control | Name | Applicability | Status | Notes |
|---------|------|---------------|--------|-------|
| 6.1 | Screening | Applicable | In progress | |
| 6.2 | Terms and conditions of employment | Applicable | In progress | |
| 6.3 | Information security awareness, education, and training | Applicable | In progress | |
| 6.4 | Disciplinary process | Applicable | Implemented | |
| 6.5 | Responsibilities after termination or change of employment | Applicable | In progress | |
| 6.6 | Confidentiality or non-disclosure agreements | Applicable | In progress | |
| 6.7 | Remote working | Applicable | Implemented | |
| 6.8 | Information security event reporting | Applicable | In progress | |

## Physical controls

| Control | Name | Applicability | Status | Notes |
|---------|------|---------------|--------|-------|
| 7.1 | Physical security perimeters | Applicable | In progress | |
| 7.2 | Physical entry | Applicable | In progress | |
| 7.3 | Securing offices, rooms, and facilities | Applicable | Implemented | |
| 7.4 | Physical security monitoring | Applicable | In progress | |
| 7.5 | Protecting against physical and environmental threats | Applicable | Implemented | |
| 7.6 | Working in secure areas | Applicable | Implemented | |
| 7.7 | Clear desk and clear screen | Applicable | In progress | |
| 7.8 | Equipment siting and protection | Applicable | Implemented | |
| 7.9 | Security of assets off-premises | Applicable | In progress | |
| 7.10 | Storage media | Applicable | Implemented | |
| 7.11 | Supporting utilities | Not applicable | Excluded | Managed by third-party hosting providers. |
| 7.12 | Cabling security | Not applicable | Excluded | Managed by third-party hosting providers. |
| 7.13 | Equipment maintenance | Not applicable | Excluded | Managed by third-party hosting providers. |
| 7.14 | Secure disposal or re-use of equipment | Applicable | In progress | |

## Technological controls

| Control | Name | Applicability | Status | Notes |
|---------|------|---------------|--------|-------|
| 8.1 | User endpoint devices | Applicable | In progress | |
| 8.2 | Privileged access rights | Applicable | In progress | |
| 8.3 | Information access restriction | Applicable | In progress | |
| 8.4 | Access to source code | In scope | In progress | Grunt AS maintains proprietary product source code, so repository access is within the ISMS scope and must be restricted to authorized personnel. |
| 8.5 | Secure authentication | Applicable | In progress | |
| 8.6 | Capacity management | In scope | In progress | Grunt AS operates hosted services for license validation, APIs, online features, and supporting systems, so capacity management is within the ISMS scope even when infrastructure is provided by cloud hosting providers. |
| 8.7 | Protection against malware | Applicable | In progress | |
| 8.8 | Management of technical vulnerabilities | Applicable | In progress | |
| 8.9 | Configuration management | Applicable | In progress | |
| 8.10 | Information deletion | Applicable | In progress | |
| 8.11 | Data masking | Applicable | In progress | |
| 8.12 | Data leakage prevention | Applicable | In progress | |
| 8.13 | Information backup | Applicable | In progress | |
| 8.14 | Redundancy of information processing facilities | Not applicable | Excluded | Redundancy of underlying processing facilities is managed by third-party hosting providers. |
| 8.15 | Logging | Applicable | In progress | |
| 8.16 | Monitoring activities | Applicable | Not started | |
| 8.17 | Clock synchronization | Applicable | Not started | |
| 8.18 | Use of privileged utility programs | Applicable | In progress | |
| 8.19 | Installation of software on operational systems | Applicable | In progress | |
| 8.20 | Networks security | Applicable | In progress | |
| 8.21 | Security of network services | Applicable | In progress | |
| 8.22 | Segregation of networks | Applicable | Not started | |
| 8.23 | Web filtering | Applicable | Not started | |
| 8.24 | Use of cryptography | Applicable | In progress | |
| 8.25 | Secure development life cycle | Applicable | Implemented | |
| 8.26 | Application security requirements | Applicable | Implemented | |
| 8.27 | Secure system architecture and engineering principles | Applicable | In progress | |
| 8.28 | Secure coding | Applicable | In progress | |
| 8.29 | Security testing in development and acceptance | Applicable | In progress | |
| 8.30 | Outsourced development | Applicable | In progress | |
| 8.31 | Separation of development, test, and production environments | Applicable | In progress | |
| 8.32 | Change management | Applicable | In progress | |
| 8.33 | Test information | Applicable | In progress | |
| 8.34 | Protection of information systems during audit testing | Applicable | In progress | |

## Review

The ISMS owner reviews this statement of applicability at least annually and when there are material changes to the ISMS scope, risk assessment, legal obligations, supplier model, or control implementation status.
