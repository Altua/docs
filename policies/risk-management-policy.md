# Risk management policy

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 2.1 | May 12, 2026 | Mads Gedde | Imported and reformatted the risk management policy for the documentation repository. |
| 2.0 | February 9, 2026 | Mads Gedde | Updated risk management policy. Approved by Einar Bjering. |
| 1.0 | December 10, 2025 | Mads Gedde | Initial documented policy. Approved by Einar Bjering. |

## Purpose

This policy defines how Grunt AS identifies, assesses, treats, monitors, and reports information security risks.

It also defines how Grunt AS sets and tracks information security and privacy objectives.

## Scope

This policy applies to:

- All Grunt AS IT systems that process, store, or transmit confidential, private, or business-critical data
- Strategic and operational risks that may affect Grunt AS objectives
- Day-to-day risks encountered when delivering Grunt AS services
- All employees, contractors, consultants, suppliers, vendors, business partners, and other third parties with access to Grunt AS systems, networks, or data

Risk management activities must provide practical value without creating unnecessary administrative burden.

Grunt AS considers the materiality of risk when designing risk management processes and controls.

## Risk management statement

Inadequate risk management can expose Grunt AS to compromise of company or customer systems, service disruption, cyber attacks, contractual issues, legal issues, privacy issues, and business interruption.

Grunt AS manages risk as part of governance, operational planning, project work, vendor management, and information security management.

Risk management supports the achievement of Grunt AS business objectives and information security objectives.

## Risk management approach

Grunt AS maintains processes to identify risks that may prevent the achievement of strategic, operational, security, and privacy objectives.

Risk management activities include:

- Identifying risks to systems, data, people, suppliers, and operations
- Assessing risks based on likelihood and impact
- Prioritizing risks based on business and security relevance
- Recording risks in a risk register
- Selecting and documenting appropriate risk responses
- Tracking treatment plans to completion
- Reporting risk status to leadership
- Reviewing the risk management process at least annually

Risk assessments are based on ISO/IEC 27005 principles and align with ISO/IEC 27001 requirements.

Grunt AS performs a formal information security risk assessment at least annually and when material changes occur.

Penetration testing and vulnerability management results are considered as risk inputs according to the related security policies.

## Risk categories

Grunt AS considers risks across the organization, including:

- Access control
- Artificial intelligence
- Asset management
- Business continuity and disaster recovery
- Communications security
- Compliance
- Cryptography
- Environmental, social, and governance
- Fraud
- Incident response management
- Information security operations
- Information security policies
- Operations security
- People operations
- Physical and environmental security
- Privacy
- Software development and acquisition
- Trustworthiness
- Vendor relationships

## Risk criteria

Grunt AS evaluates risks based on the likelihood and impact of an event that could adversely affect:

- Confidentiality, integrity, availability, or privacy
- Grunt AS information and systems
- Customer information and systems
- Personally identifiable information (PII)
- Business operations and service delivery

Risk inputs may come from risk assessments, vulnerability scans, penetration tests, vendor reviews, security incidents, audits, customer requirements, regulatory obligations, and management review.

Management may adjust a risk rating based on system criticality, data sensitivity, exposure, exploitability, business impact, or other relevant factors.

## Risk scoring

Each risk is assessed using likelihood and impact scores from 1 to 5.

| Score | Likelihood | Description |
|-------|------------|-------------|
| 1 | Very unlikely | The event is not expected to occur. Existing controls prevent or significantly impede exploitation. |
| 2 | Unlikely | The event is unlikely, but there is a slight possibility it may occur. Existing controls reduce the likelihood. |
| 3 | Somewhat likely | The event may occur. The threat source has motivation or capability, but controls may reduce successful exploitation. |
| 4 | Likely | The event is likely to occur. The threat source has motivation, capability, and resources, but some controls may reduce the likelihood. |
| 5 | Very likely | The event is highly likely. Controls are missing, ineffective, or unlikely to prevent exploitation. |

| Score | Impact | Description |
|-------|--------|-------------|
| 1 | Very low impact | The event would have almost no adverse effect on operations, assets, individuals, customers, or other organizations. |
| 2 | Low impact | The event would have a limited adverse effect, such as minor service degradation, minor damage, or minor financial loss. |
| 3 | Medium impact | The event would have a serious adverse effect, such as reduced capability, significant resource impact, or meaningful operational disruption. |
| 4 | High impact | The event would have a severe adverse effect, such as major damage, major financial loss, or loss of one or more primary functions. |
| 5 | Very high impact | The event would have multiple severe or catastrophic effects across operations, assets, individuals, customers, or other organizations. |

Overall risk score is calculated as:

```text
Likelihood x Impact = Risk score
```

| Risk level | Score range | Description |
|------------|-------------|-------------|
| Low | 1-4 | The event would have a limited adverse effect. |
| Medium | 5-14 | The event would have a serious adverse effect. |
| High | 15-25 | The event would have a severe adverse effect. |

## Risk assessment process

### Establish context

The risk owner defines the scope, boundaries, assumptions, constraints, business objectives, legal requirements, and information sources for the assessment.

The risk owner identifies the systems, assets, data, processes, suppliers, and people included in the assessment.

### Identify risks

The risk owner identifies and documents:

- Threats that may cause harm
- Vulnerabilities that may be exploited
- Assets or processes requiring protection
- Existing controls
- Potential consequences if the risk occurs

### Analyze risks

The risk owner estimates likelihood and impact using the scoring criteria in this policy.

The analysis should consider existing controls, threat activity, exposure, data sensitivity, business criticality, and regulatory or contractual obligations.

### Evaluate risks

The risk owner compares the analyzed risk against Grunt AS risk criteria and determines whether the risk should be accepted, treated, transferred, or avoided.

Risks above the acceptable threshold are prioritized for treatment.

Lower-level risks may be accepted, monitored, or handled through normal operational planning.

### Treat risks

The risk owner selects an appropriate risk response and documents any required treatment actions, owners, due dates, and evidence.

Treatment plans must align with Grunt AS business objectives and risk appetite.

### Communicate and consult

Relevant stakeholders are informed of risk assessment results, treatment decisions, and material changes to risk status.

Risk reporting should be clear enough to support timely decisions by leadership and system owners.

### Monitor and review

Risks and treatment plans are reviewed at least annually and when significant changes occur.

Reviews should consider changes in threats, vulnerabilities, assets, suppliers, regulations, business objectives, incidents, or control effectiveness.

## Risk responses

Grunt AS uses the following risk responses:

| Response | Description |
|----------|-------------|
| Mitigate | Reduce the likelihood or impact of the risk by implementing controls or changing processes. |
| Accept | Acknowledge and monitor the risk when it is within acceptable levels or when treatment is not practical at the time. |
| Transfer | Shift or share the risk through contractual terms, outsourcing, insurance, or another approved mechanism. |
| Avoid | Stop or change the activity that creates the risk. |

When Grunt AS chooses mitigation or transfer, the risk owner must document a risk treatment plan.

Accepted risks must be documented with the reason for acceptance, approving role, and review date.

## Risk register and treatment plan

Grunt AS maintains a risk register and treatment plan.

The current risk register is maintained in Vanta.

Each risk record should include:

- Risk description
- Risk category
- Affected assets, systems, processes, or suppliers
- Likelihood score
- Impact score
- Overall risk level
- Risk owner
- Selected risk response
- Treatment actions, if applicable
- Due dates and status
- Approval or acceptance notes, if applicable

Risks are prioritized based on likelihood, impact, business relevance, cost, work effort, resource availability, and treatment urgency.

Multiple risk treatments may be performed at the same time when appropriate.

Regular risk reports are provided to Grunt AS leadership so risks can be reviewed against business priorities and objectives.

## Information security in project management

Grunt AS considers information security risk in technical projects and in other projects that may create risk for the company.

Project risk management should include:

- Initial information security risk assessment
- Early identification of security and privacy requirements
- Ongoing assessment of material project risks
- Mitigation of risks before production release when appropriate
- Documentation of unresolved or accepted risks

## Roles and responsibilities

| Role | Responsibility |
|------|----------------|
| CEO | Ultimately responsible for acceptance or treatment of organizational risks. |
| Chief Technology Officer | May approve avoidance, mitigation, transfer, or acceptance of risks recorded in the risk register. |
| Information Security Officer | Identifies information security risks, develops treatment plans, communicates risks to management, and implements risk treatment direction. |
| Risk owner | Assesses assigned risks, maintains risk records, coordinates treatment actions, and keeps status current. |
| System owner | Provides system context, assesses technical impact, and supports implementation of risk treatments. |
| Employees and contractors | Report suspected risks, security weaknesses, incidents, or control failures. |

## Evidence and records

Evidence supporting this policy may include:

- Risk register records
- Risk treatment plans
- Risk acceptance decisions
- Vulnerability scan results
- Penetration test reports
- Vendor risk assessments
- Incident reports
- Management review notes
- Project risk assessments
- Evidence of implemented controls

## Related policies and resources

This policy should be read together with:

- ISMS statement of applicability
- Vulnerability identification and prioritization process
- Penetration testing
- Incident response plan
- Business continuity and disaster recovery plan
- Third-party and subcontractor policy
- Change management procedure

The risk management process supports ISO/IEC 27001 clauses 6.1 and 6.2.

## Review

The Information Security Officer reviews this policy at least annually and when material changes occur to the ISMS, business objectives, risk criteria, regulatory obligations, or operating environment.
