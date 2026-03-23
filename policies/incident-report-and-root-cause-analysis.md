# Incident report and root cause analysis

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 23, 2026 | Engineering | Initial documented process for incident reporting, investigation, root cause analysis, and follow-up actions. |

## Purpose

This document defines how Grunt AS records incidents, investigates what happened, documents root cause, and tracks follow-up actions.

The goal is to make sure meaningful incidents are written down clearly, reviewed after the fact, and used to improve systems and processes.

## Scope

This process applies to operational, security, service, and deployment incidents that affect Grunt AS systems, customer-facing services, or internal operations in a meaningful way.

## System of record

The primary system of record for incidents is the Grunt AS Notion incidents table:

[Incidents](https://www.notion.so/Incidents-304eae9cb946802fa7c4dfe73f98c10c?p=304eae9cb946805a8ce9c04a59f254be&pm=s)

Each incident should have one main record in that table.

If investigation notes, logs, screenshots, pull requests, or follow-up tasks live in other systems, the incident record should link to them.

The Notion entry title should be a short description of the incident.

## When to create an incident record

An incident record should be created when one or more of the following applies:

- A production issue causes a customer-facing outage or service degradation
- A security incident or suspected security incident occurs
- A deployment, configuration change, or infrastructure issue causes material impact
- Data is exposed, lost, corrupted, or put at risk
- A problem requires emergency response, rollback, or unusual operational handling
- The team decides the issue is important enough to review and learn from

Minor issues that are resolved quickly without meaningful impact do not always require a full RCA, but they may still be logged if the team wants a record.

## Incident record template

The Notion incident record currently uses the following properties:

- Title of the incident entry
- `ID`
- `Date`
- `Owner`
- `Reported by`
- `Severity`
- `Status`
- `Root cause`
- `Corrective action`
- `Preventive action`

These fields should be used as follows:

- `Title`: Short description of the incident
- `ID`: Unique incident number from the Notion table
- `Date`: Date of the incident or the date the incident was recorded
- `Owner`: Person responsible for maintaining the incident record and follow-up
- `Reported by`: Source of the incident, such as a customer, internal team member, monitoring alert, or system notification
- `Severity`: Relative impact level such as low, medium, or high
- `Status`: Current state such as open, in progress, or closed
- `Root cause`: Clear explanation of why the incident happened
- `Corrective action`: What was done to fix or contain the issue
- `Preventive action`: What should change to reduce the chance of the issue happening again

If extra context is needed, the body of the Notion page can be used for:

- A short incident summary
- Timeline notes
- Links to logs, dashboards, pull requests, or related tasks
- Lessons learned or extra investigation details

## Investigation and reporting workflow

### Create the incident record

As soon as practical, create an incident entry in the Notion table.

The initial record does not need to be complete, but it should capture enough information for the team to track the incident while response is ongoing.

At minimum, the entry should have a clear title, date, owner, severity, status, and a short note in the relevant fields or page body.

### Record the timeline

During or after the incident, record the important events in time order.

This should include:

- When the issue started or was first noticed
- When responders were engaged
- What was investigated
- What changes were made
- When the issue was mitigated or resolved

The timeline does not need to be long. It only needs to be clear enough that someone else can understand how the incident unfolded.

If the current Notion properties do not include a dedicated timeline field, the timeline can be written in the page body.

### Document impact and resolution

The incident report should describe:

- What users or systems were affected
- How serious the impact was
- How the issue was contained, mitigated, or fixed
- Whether rollback, emergency change, or manual intervention was required

This information can be captured partly in `Severity`, `Corrective action`, and `Root cause`, with any extra detail written in the page body.

## Root cause analysis approach

Grunt AS uses a practical root cause analysis process focused on understanding why the incident happened and what should change.

The RCA should answer:

- What actually failed
- Why it failed
- Why existing checks or safeguards did not catch it earlier
- What changes will reduce the chance of the same issue happening again

The analysis does not need to be long or formal. It should be clear, specific, and useful.

If helpful, the reviewer may use a simple method such as:

- Asking "why" repeatedly until the underlying cause is clear
- Separating the primary cause from contributing factors
- Distinguishing between the triggering event and the process gap that allowed impact

## When a full RCA is expected

A full RCA should be completed when the incident involves:

- A security event or suspected security event
- Meaningful customer impact
- Extended service disruption
- Data loss, corruption, or exposure risk
- Rollback of a production change
- A repeated issue that the team has seen before

For smaller incidents, the team may record only a short summary, impact, resolution, and any obvious follow-up actions.

## Follow-up actions

If the incident identifies missing safeguards, weak processes, or needed fixes, those items should be recorded as follow-up actions.

In the current Notion template, the main follow-up fields are:

- `Corrective action` for what was done to resolve the issue
- `Preventive action` for what should change going forward

If a follow-up action needs separate tracking, the incident page should link to the implementation work in GitHub, Notion, or another system.

Follow-up actions may include code changes, infrastructure changes, monitoring improvements, documentation updates, testing improvements, or process changes.

## Lessons learned

Each meaningful incident review should capture a short lessons learned section.

This may include:

- What worked well during response
- What slowed down investigation or recovery
- What should change in tooling, monitoring, deployment, or communication
- Whether existing policies or workflows should be updated

## Roles and responsibilities

| Role | Responsibilities |
|------|------------------|
| Incident lead or owner | Create or maintain the incident record, coordinate the write-up, and ensure root cause and follow-up actions are documented. |
| Responders | Contribute facts, timeline details, technical findings, and remediation notes. |
| Engineering | Review the incident, complete technical follow-up work, and improve systems or workflows where needed. |
| Engineering leadership or CTO | Review more serious incidents, support prioritization of follow-up actions, and ensure meaningful issues are not left unresolved. |

## Evidence and records

Evidence supporting this process may include:

- The Notion incident record
- Timeline notes
- Logs, dashboards, or alert screenshots
- Pull requests or deployment records linked to the incident
- Rollback notes
- Root cause summary
- Follow-up tasks and completion records

## Related policies and processes

This process should be read together with:

- Change management procedure
- QA process
- Secure engineering principles and planning
- Vulnerability identification and prioritization process

## Review

Engineering reviews this process at least annually and whenever the incident handling workflow changes in a meaningful way.
