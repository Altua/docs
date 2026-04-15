# Incident Response Plan

## Version history

| Version | Date | Description | Author | Approver |
|---------|------|-------------|--------|----------|
| 1.0 | Feb 26, 2026 | Version 1.0 | Mads Gedde | Einar Bjering |

## Purpose

This document establishes the plan for managing information security incidents and events, and offers guidance for employees or incident responders who believe they have discovered, or are responding to, a security incident.

## Scope

This policy covers all information security or data privacy events or incidents.

## Incident and event definitions

A **security event** is an observable occurrence relevant to the confidentiality, availability, integrity, or privacy of company controlled data, systems or networks.

A **security incident** is a security event which results in loss or damage to the confidentiality, availability, integrity, or privacy of company controlled data, systems or networks.

## Reporting

If a Grunt AS employee, contractor, user, or customer becomes aware of an information security event or incident, possible incident, imminent incident, unauthorized access, policy violation, security weakness, or suspicious activity, then they shall immediately report the information using one of the following communication channels:

- Huma whistleblowing portal

Reporters should act as a good witness and behave as if they are reporting a crime. Reports should include specific details about what has been observed or discovered.

## Severity

CEO shall monitor incident and event tickets and shall assign a ticket severity based on the following categories.

### P2/P3 - Medium and Low Severity

Issues meeting this severity are simply suspicions or odd behaviors. They are not verified and require further investigation. There is no clear indicator that systems have tangible risk and do not require emergency response. This includes lost/stolen laptop with disk encryption, suspicious emails, outages, strange activity on a laptop, etc.

### P1 - High Severity

High severity issues relate to problems where an adversary or active exploitation hasn't been proven yet, and may not have happened, but is likely to happen. This may include lost/stolen laptop without encryption, vulnerabilities with direct risk of exploitation, threats with risk or adversarial persistence on our systems (e.g., backdoors, malware), malicious access of business data (e.g., passwords, vulnerability data, payments information).

### P0 - Critical Severity

Critical issues relate to actively exploited risks and involve a malicious actor or threats that put any individual at risk of physical harm. Identification of active exploitation is required to meet this severity category.

## Escalation and internal reporting

The incident escalation contacts can be found below in Appendix A.

| Severity | Escalation Path |
|----------|-----------------|
| P0 - Critical Severity | P0 issues require immediate notification to the Technology team and GLT. |
| P1 - High Severity | A support ticket must be created and the appropriate contacts (see P0 above) must also be notified via email or Slack with a reference to the ticket number. |
| P2/P3 - Medium and Low Severity | A support ticket must be created and assigned to the appropriate team for response. |

## Documentation

All reported security events, incidents, and response activities shall be documented and adequately protected in Notion.

A root cause analysis may be performed on all verified P0 security incidents. A root cause analysis report shall be documented and referenced in the incident ticket. The root cause analysis shall be reviewed by the Information Security Officer who shall determine if a post-mortem meeting will be called.

## Incident response process

For critical issues, the response team will follow an iterative response process designed to investigate, contain exploitation, eradicate the threat, recover system and services, remediate vulnerabilities, and document a post-mortem report including the lessons learned from the incident.

### Summary

- Event reported
- Triage and analysis
- Investigation
- Containment & neutralization (short term/triage)
- Recovery & vulnerability remediation
- Hardening & Detection improvements (lessons learned, long term response)

### Detailed

- Information Security Officer will manage the incident response effort
- If necessary, a central "War Room" will be designated, which may be a physical or virtual location (i.e Slack channel)
- A recurring Incident Response Meeting will occur at regular intervals until the incident is resolved
- Legal and executive staff will be informed as required

### Incident response meeting agenda

- Update Incident Ticket and timelines
- Document new Indicators of Compromise (IOCs)
- Perform investigative Q&A
- Apply emergency mitigations
- External Reporting / Breach Reporting
- Plan long term mitigations
- Document Root Cause Analysis (RCA)
- Additional items as needed

## Special considerations

### Internal issues

Issues where the malicious actor is an internal employee, contractor, vendor, or partner requires sensitive handling. The incident manager shall contact CEO directly and will not discuss with other employees. These are critical issues where follow-up must occur.

### Compromised communication

Incident responders must have Slack arranged before listing themselves as part of the incident response team. If there are IT communication risks, an out of band solution will be chosen, and communicated to incident responders via WhatsApp.

### Additional requirements

- Suspected and reported events and incidents shall be documented
- Suspected incidents shall be assessed and classified as either an event or an incident
- Incident response shall be performed according to this plan and any associated procedures
- All incidents shall be formally documented, and a documented root cause analysis shall be performed
- Incident responders shall collect, store, and preserve incident-related evidence in accordance with industry guidance and best practices such as NIST SP 800-86 'Guide to Integrating Forensic Techniques into Incident Response'
- Suspected and confirmed unauthorized access events shall be reviewed by the Incident Response Team. Breach determinations shall only be made by the Information Security Officer
- Grunt AS shall promptly and properly notify customers, partners, users, affected parties, and regulatory agencies of relevant incidents or breaches in accordance with Grunt AS policies, contractual commitments, and regulatory requirements, as determined by the CEO
- This Incident Response Plan shall be reviewed and formally tested at least annually. Results of IR plan testing activities including findings and lessons learned will be formally documented and maintained to support security, compliance and audit requirements

## External communications and breach reporting

Legal and executive staff shall confer with technical teams in the event of unauthorized access to company or customer systems, networks, and/or data. Legal staff along with the CEO shall determine if breach reporting or external communications are required. Breaches shall be reported to customers, consumers, data subjects and regulators without undue delay and in accordance with all contractual commitments and applicable legislation.

No personnel may disclose information regarding incident or potential breaches to any third party or unauthorized person without the approval of legal and/or executive management.

## Mitigation and remediation

Legal and executive staff shall determine any immediate or long term mitigations or remedial actions that need to be taken as a result of an incident or breach. In the event that mitigations or remedial actions are needed, executive staff shall direct personnel with respect to planning, communicating and executing those activities.

## Cooperation with customers, Data Controller, and authorities

As needed and determined by legal and executive staff, the company shall cooperate with customers, Data Controllers and regulators to fulfill all of its obligations in the event of an incident or data breach.

## Roles & responsibilities

Every employee and user of any Grunt AS information resources has responsibilities toward the protection of the information assets. The table below establishes the specific responsibilities of the incident responder roles.

### Response Team Members

| Role | Responsibility |
|------|----------------|
| Incident Manager | The primary and ultimate decision maker during the response period. Ultimately responsible for resolving the incident and formally closing incident response actions. See Appendix A for contact information. Responsibilities include: ensuring the right people from all functions are actively involved as appropriate; communicating status updates to the appropriate person or teams at regular intervals; resolving incidents in the immediate term; determining necessary follow-up actions; assigning follow-up activities to the appropriate people; promptly reporting incident details which may trigger breach reporting, in writing to the CEO. |
| Incident Response Team (IRT) | The individuals who have been engaged and are actively working on the incident. All members of the IRT will remain engaged in incident response until the incident is formally resolved, or they are formally dismissed by the Incident Manager. |
| Engineers (Support and Development) | Qualified engineers will be placed into the on-call rotation and may act as the Incident Manager (if primary resources are not available) or a member of the IRT when engaged to respond to an incident. Engineers are responsible for understanding the technologies and components of the information systems, the security controls in place including logging, monitoring, and alerting tools, appropriate communications channels, incident response protocols, escalation procedures, and documentation requirements. When Engineers are engaged in incident response, they become members of the IRT. |
| Users | Employees and contractors of Grunt AS. Users are responsible for following policies, reporting problems, suspected problems, weaknesses, suspicious activity, and security incidents and events. |
| Customers | Customers are responsible for reporting problems with their use of Grunt AS services. Customers are responsible for verifying that reported problems are resolved. |
| Legal Counsel | Responsible, in conjunction with the CEO and executive management, for determining if an incident presents legal or regulatory exposure as well as whether an incident shall be considered a reportable breach. Counsel shall review and approve in writing all external breach notices before they are sent to any external party. |
| Executive Management | Responsible, in conjunction with the CEO and Legal Counsel, for determining if an incident shall be considered a reportable breach. An appropriate company officer shall review and approve in writing all external breach notices before they are sent to any external party. Grunt AS shall seek stakeholder consensus when determining whether a breach has occurred. The Grunt AS CEO shall make a final breach determination in the event that consensus cannot be reached. |

## Management commitment

Grunt AS management has approved this policy and commits to providing the resources, tools and training needed to reasonably respond to identified security events and incidents with the potential to adversely affect the company or its customers.

## Exceptions

Requests for an exception to this Policy must be submitted to and authorized by the CEO for approval. Exceptions shall be documented.

## Violations & enforcements

Any known violations of this policy should be reported to the CEO. Violations of this policy may result in immediate withdrawal or suspension of system and network privileges and/or disciplinary action in accordance with company procedures up to and including termination of employment.

## Appendix A — Contact information

Contacts for IT and Engineering Management as well as executive staff and can be found Huma - https://grunt.humahr.com/people.
