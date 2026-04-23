# Data restore test procedure

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | April 23, 2026 | Engineering | Initial documented data restore test procedure. |

## Purpose

This procedure defines how Grunt AS verifies that backups can be reliably restored, ensuring recoverability of production data in the event of a disruption, data loss, or disaster recovery scenario.

## Scope

This procedure applies to all production data backups covered by the [Business continuity and disaster recovery plan](../policies/business-continuity-and-disaster-recovery.md).

## Frequency

Data restore tests are performed **annually**, at minimum. Additional tests may be performed following significant changes to backup systems, storage locations, or data architecture.

## Procedure

1. **Plan the test**
   - Identify the backup(s) to be restored
   - Select a non-production environment as the restore target
   - Notify relevant stakeholders of the scheduled test

2. **Execute the restore**
   - Retrieve the selected backup from its storage location
   - Restore the backup to the non-production environment
   - Record the time taken to complete the restore

3. **Verify integrity**
   - Confirm the restored data is complete and readable
   - Validate that the restored environment functions as expected
   - Compare key data against known reference values where applicable

4. **Document results**
   - Record the test date, backup used, restore duration, and verification outcome
   - Note any issues encountered and remediation steps taken
   - Confirm whether recovery met the Recovery Time Objective (RTO) and Recovery Point Objective (RPO) defined in the business continuity and disaster recovery plan

5. **Review and follow-up**
   - Review test results with Engineering and the CTO
   - Address any failures or deficiencies identified
   - Update backup and recovery procedures as needed

## Roles and responsibilities

| Role | Responsibility |
|------|---------------|
| Engineering | Plan and execute the restore test, document results, remediate issues |
| CTO | Review results and approve any changes to backup or recovery procedures |

## Records

Results of each annual data restore test are retained for a minimum of three years.

## Review

This procedure is reviewed annually and updated as needed to reflect changes in systems or backup strategy.
