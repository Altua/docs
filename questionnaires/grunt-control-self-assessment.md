# Grunt control self-assessment

**Status:** Draft; initially prepared from repository documentation on 2026-10-13. Updated with confirmations through 2026-10-14.

**Product scope:** Grunt PowerPoint add-in. External AI clients and standalone MCP integrations are outside this assessment.

**Customer:** Turner & Townsend, confirmed on 2026-10-14. The supplied PDFs identify the assessment as Grunt (T&T) and use CBRE-labelled internal controls. Answers describe Grunt's controls and capabilities. Customer-operated identity and review processes are identified separately; this response does not certify the customer's internal configuration.

**Confirmed in conversation:** 2026-10-13; product scope, A3, A5, A6, A7, A8, A9, A10, A12, A13, tool restrictions and permission checks relevant to A11/A15, and user acceptance relevant to A16.

**Further confirmations:** 2026-10-14; Azure OpenAI and standard content filters, application validation, final-change-only approval, the general incident response plan, Entra administrator accounts and required MFA, no CrowdStrike/Falcon deployment, Azure Key Vault for all production secrets, Azure logs/alerts, SonarCloud coverage, Grunt code ownership, and Claude secrets checks without customer-platform integration. The April 21, 2026 recovery test met the 24-hour RTO/RPO. Read-only Azure checks on 2026-10-14 verified the inspected API WAF and database backup configuration; the findings appear below.

This document combines the four supplied questionnaire PDFs. Answers use repository documentation and confirmations supplied in conversation. Each question is followed by an answer and links to supporting repo documents where available. **Needs confirmation** means a complete answer is still outstanding; it does not mean the control is absent. Unconfirmed proposals in the earlier AI response draft are not treated as independent evidence.

All 36 visible form questions are included, plus the standalone authentication question on the Prevent page (P0). The portal counters differ from the visible questions. The repeated secrets detection question is preserved in both sections. PDF selections are not treated as verified Grunt answers, and questionnaire guidance is used only to interpret the control being asked about.

## Grunt CSA page 1 - AI[35].pdf

**Question (A1 - AI dependencies):** Does the app or tool provide or use AI capabilities?

**Answer:** Yes. Grunt provides optional AI functionality. It processes content you submit when you use those features. Core PowerPoint add-in functionality does not require AI. See the [IT FAQ](../powerpoint-add-in/it/faq.mdx#data-and-privacy) and [privacy policy](../policies/privacy-policy.md#customer-content-processed-by-product-features).

**Question (A2 - GenAI):** Does the application generate new content (such as text, images, code, audio, or video) using patterns learned from data?

**Answer:** Yes. Grunt uses AI or machine learning to generate output from your inputs and the underlying models. This does not imply support for every output type listed in the question. See [AI features in the terms and conditions](../policies/terms-and-conditions.md#5-ai-features).

**Question (A3 - Agentic AI):** Can the application autonomously plan and execute actions to achieve goals with minimal human intervention?

**Answer:** Yes. The AI workflow inside the PowerPoint add-in uses an externally managed model and Grunt-provided tools. It can make several tool calls to carry out a user's request before the user accepts the final changes. Those changes require user acceptance before they are applied locally. Confirmed in conversation on 2026-10-13.

**Question (A4 - MaaS (Model as a Service) AI):** Does the application consume AI models through externally managed APIs or platforms rather than hosting or training the models itself?

**Answer:** Yes. The add-in consumes externally managed AI models through Azure OpenAI. Grunt does not host or deploy the underlying models itself. The current provider was confirmed in conversation on 2026-10-14.

**Question (A5 - A2A (Agent-to-Agent) AI):** Does the application involve multiple AI agents that interact or coordinate with each other to complete tasks?

**Answer:** No. The PowerPoint add-in does not use multiple AI agents that communicate or coordinate with each other to complete tasks. Confirmed in conversation on 2026-10-13.

**Question (A6 - Endpoint AI):** Does the application perform automated actions powered by AI outputs locally on the user's device (e.g., laptop, mobile, desktop)?

**Answer:** Yes, after user approval. Once the user accepts AI-generated changes, the PowerPoint add-in automatically applies them locally in PowerPoint. The changes are not applied before acceptance. Confirmed in conversation on 2026-10-13.

**Question (A7 - Model scans (OSS)):** Are open-source model scans performed for security and compliance?

**Answer:** N/A for model artifacts hosted or deployed by Grunt. The add-in uses externally managed AI models. Grunt does not host or deploy the underlying models itself. General [code and dependency scanning](../policies/secure-code-vulnerabilities.md) still applies to Grunt's application and integrations. This answer does not assert that the external providers perform any particular model scans. Model hosting was confirmed in conversation on 2026-10-13.

**Question (A8 - Red teaming for control validation):** Is red teaming performed to validate AI security controls?

**Answer:** No structured AI red teaming program is currently in place. Grunt documents [general external penetration testing](../policies/penetration-testing.md), but does not have a structured program specifically validating AI controls against adversarial prompts and other AI attacks. Confirmed in conversation on 2026-10-13.

**Question (A9 - Explainability via provenance and observability):** Is explainability ensured through provenance and observability mechanisms?

**Answer:** No, for the full provenance and explainability control described in the questionnaire. Request-level observability is in place: Grunt logs model name/version, request ID, timestamps, token counts, processing steps, and success/failure. Logs contain only that metadata. Input content is never logged for privacy reasons, and requests are not linked back to source content through source identifiers. The logging scope was confirmed in conversation on 2026-10-13.

**Question (A10 - Token rate limit enforcement and monitoring):** Are token rate limits enforced and monitored for misuse?

**Answer:** Yes. Grunt limits and monitors both request counts and token consumption. The [Grunt Pro API reference](../grunt-pro-api/index.mdx#status-code-notes) also documents a 429 Too Many Requests response for AI generation rate limits. Request and token controls were confirmed in conversation on 2026-10-13.

**Question (A11 - Data pipeline security):** Is data pipeline security implemented to prevent tampering or leakage?

**Answer:** Yes, for the add-in's application-level data pipeline controls. The AI workflow uses Azure OpenAI with a fixed list of Grunt-provided tools, permission checks, and validation of tool arguments and model responses. Users must accept final changes before the add-in applies them locally. [Encryption and access controls](../policies/baseline-configuration.md), [network segregation](../policies/network-segregation.md), and [restrictions on model training](../policies/privacy-policy.md#customer-content-processed-by-product-features) also protect the flow. This answer covers those controls; it does not establish comprehensive AI data provenance or poisoning detection. Validation was confirmed in conversation on 2026-10-14.

**Question (A12 - Sensitive data refinement):** Is differential privacy or anonymization applied to sensitive datasets?

**Answer:** No, for customer content submitted to the AI features. Grunt sends the submitted content as is, without applying anonymization, masking, or differential privacy before submission. The [non-production data policy](../policies/production-data-in-non-production.md#policy-statement) separately requires synthetic, masked, anonymized, or sanitized testing data. Production AI submission behavior was confirmed in conversation on 2026-10-13.

**Question (A13 - Runtime model monitoring):** Are runtime model scans implemented to detect vulnerabilities?

**Answer:** N/A for integrity scanning of Grunt-managed model artifacts. The add-in uses externally managed models, so Grunt does not manage the model weights or inference infrastructure to be scanned. Provider runtime model monitoring is outside Grunt's direct operation; this answer does not assert a specific provider control. Model hosting was confirmed in conversation on 2026-10-13.

**Question (A14 - Incident response playbooks for AI):** Are incident response playbooks established and tested for AI-related failures or security incidents?

**Answer:** No dedicated AI incident playbooks. AI-related incidents follow Grunt's [general incident response plan](../policies/incident-response-plan.md), which covers all information security and privacy incidents and requires annual testing. This does not establish a separately tested AI-specific playbook. Use of the general plan was confirmed in conversation on 2026-10-14.

**Question (A15 - Adversarial prompt guardrails):** Are adversarial prompt guardrails implemented?

**Answer:** Partially. Azure OpenAI's standard content filters are enabled. Grunt restricts the AI workflow to a fixed tools list, applies permission checks, and validates tool arguments and model responses. Grunt adds no separate prompt/output filters beyond that validation. This describes the confirmed provider filtering and application controls; dedicated prompt injection or jailbreak defenses are not claimed. Filter settings and the absence of additional Grunt filters were confirmed in conversation on 2026-10-14.

**Question (A16 - Human in the loop):** Is a human in the loop?

**Answer:** Yes, for approval of the final slide changes. The user must accept those changes before the add-in applies them. Intermediate tool calls do not require individual human approval, so human review does not cover every AI input and output as described in the questionnaire guidance. The [terms and conditions](../policies/terms-and-conditions.md#5-ai-features) also require customers to review and validate AI output before relying on it. The approval scope was confirmed in conversation on 2026-10-14.

## Grunt CSA page 2 - Prevent.pdf

**Question (P0 - AI access authentication):** Is authentication enforced for AI system access?

**Answer:** Yes, for the documented AI API endpoints used by the add-in. The [Grunt Pro API reference](../grunt-pro-api/index.mdx#authenticated-endpoints) lists the AI routes as requiring fingerprint or bearer authentication.

**Question (P1 - Endpoint security):** Is CrowdStrike deployed to all servers and containers?

**Answer:** No. Grunt does not deploy CrowdStrike/Falcon to its production servers or containers. Confirmed in conversation on 2026-10-14. The inspected add-in APIs run in Azure Container Apps. See the [Azure verification evidence](evidence/grunt-csa-azure-2026-10-14.json).

**Question (P2 - Privilege account management):** Are all privileged human accounts onboarded to either CyberArk or Delinea?

**Answer:** No. Grunt uses administrator accounts managed in Microsoft Entra ID, rather than CyberArk or Delinea. The [configuration baseline](../policies/baseline-configuration.md#cloud-infrastructure) documents least privilege and administrator MFA. Account management was confirmed in conversation on 2026-10-14.

**Question (P3 - Access fulfillment):** Is user access fulfilled by an automated process (myID) or manually by the User Access Administration (UAA) Team?

**Answer:** Grunt supports automated user provisioning and deprovisioning through [Microsoft Entra ID/SCIM](../powerpoint-add-in/it/scim.mdx). License managers can also manage users in the Grunt portal. myID and the UAA team are customer-operated access processes; Grunt does not administer those processes. This answer describes Grunt's available provisioning methods.

**Question (P4 - Access reviews):** Is the application integrated with myID for periodic user access reviews?

**Answer:** Grunt reviews its own internal access rights annually and adjusts them as needed. See [access-control practices](../powerpoint-add-in/it/faq.mdx#access-control). Integration with customer-operated myID access reviews is not established by this assessment; Grunt's internal reviews do not certify that integration.

**Question (P5 - MFA):** Is MFA (Multifactor Authentication) enabled for the application or tool?

**Answer:** Yes. Grunt requires MFA. [Microsoft Entra ID SSO](../powerpoint-add-in/it/sso.mdx) also applies the organization's conditional access policies. The MFA requirement was confirmed in conversation on 2026-10-14.

**Question (P6 - SSO):** Is the application or tool onboarded to the CBRE IdP (Identity Provider) solution with SSO (Single Sign-on) enabled?

**Answer:** Grunt supports [Microsoft Entra ID SSO](../powerpoint-add-in/it/sso.mdx). Grunt enables SSO for an organization's email domain, after which users authenticate through Entra ID and the organization's conditional access policies apply. This confirms Grunt's SSO capability; onboarding to the specifically named CBRE IdP is not established by this assessment.

**Question (P7 - Privilege access management):** Are privileged access accounts onboarded to the CBRE PAM (privileged account management tool)?

**Answer:** No. Grunt's administrator accounts are managed in Microsoft Entra ID and are not onboarded to CBRE's PAM platform. Confirmed in conversation on 2026-10-14.

**Question (P8 - Secrets detection):** Are source code repositories enrolled in the CBRE secrets detection platform?

**Answer:** No. Grunt's repositories are not connected to a customer-operated secrets-scanning platform. Claude is used for secrets checks. This confirmation does not specify an automated or continuous scanning process. The tool and lack of customer-platform integration were confirmed in conversation on 2026-10-14.

**Question (P9 - Secrets vaulting):** Are production secrets stored in and fetched from the enterprise secrets vault?

**Answer:** Yes, for Grunt-operated services. All production secrets are stored in and retrieved from Azure Key Vault. This covers production credentials such as passwords, tokens, API keys, and certificates. Confirmed in conversation on 2026-10-14. The [IT FAQ](../powerpoint-add-in/it/faq.mdx#security) also documents Azure Key Vault for encryption keys.

**Question (P10 - Encryption at rest):** Is encryption at rest implemented?

**Answer:** Yes, for Grunt-managed storage and databases. The [configuration baseline](../policies/baseline-configuration.md#cloud-infrastructure) requires encryption at rest, and the [IT FAQ](../powerpoint-add-in/it/faq.mdx#security) specifies AES-256. The [backup plan](../policies/business-continuity-and-disaster-recovery.md#backup-strategy) also documents encrypted backups. Customer-managed local files follow the customer environment's controls.

**Question (P11 - Encryption in transit):** Is encryption in transit implemented?

**Answer:** Yes. The [configuration baseline](../policies/baseline-configuration.md#cloud-infrastructure) requires TLS for all services. The [IT FAQ](../powerpoint-add-in/it/faq.mdx#security) specifies TLS 1.2/1.3 for data in transit.

**Question (P12 - Web application firewall (WAF) - external):** Has a WAF (Web Application Firewall) been implemented with blocking mode enabled?

**Answer:** No, for the public add-in API endpoints inspected on 2026-10-14. No Azure WAF, Front Door, Application Gateway, or WAF policy resource was found in the accessible subscription. The API domains resolve directly to public Azure Container Apps ingress. Grunt uses Cloudflare elsewhere, but not for the APIs, as confirmed on 2026-10-14. A blocking-mode WAF is therefore not established on these API paths. See the [Azure verification evidence](evidence/grunt-csa-azure-2026-10-14.json).

## Grunt CSA page 3 - Limit Damage.pdf

**Question (L1 - Incident response integration):** Are application security events sent to the Incident Response platform (e.g., Databahn)?

**Answer:** No dedicated incident response platform integration reported. Grunt handles application security events through Azure logs and alerts and follows its [incident response plan](../policies/incident-response-plan.md). Azure logging and alerting were confirmed in conversation on 2026-10-14; this does not establish integration with a customer incident response platform such as Databahn.

**Question (L2 - Secrets detection):** Are source code repositories enrolled in the CBRE secrets detection platform?

**Answer:** No. Grunt's repositories are not connected to a customer-operated secrets-scanning platform. Claude is used for secrets checks. This repeats P8 and uses the same confirmation supplied on 2026-10-14; the scan process is not specified.

**Question (L3 - Static application security testing (SAST)):** Have production components completed static analysis scanning?

**Answer:** Yes. All production components are scanned with SonarCloud. This coverage was confirmed in conversation on 2026-10-14. [Secure code vulnerability scanning](../policies/secure-code-vulnerabilities.md#static-code-analysis) documents scans on pull requests and main branch updates, with failed quality gates or critical security issues blocking merges. Dated scan evidence can be retrieved from GitHub, SonarCloud, or Vanta if requested; it is not stored in this repo.

**Question (L4 - Open source management - third party dependency vulnerabilities):** Have production repositories been scanned for open source and third party dependency vulnerabilities?

**Answer:** Not Applicable under the questionnaire guidance. All source code and deployment scripting is managed by Grunt, rather than the customer. The PDF guidance specifies Not Applicable when there is no CBRE-managed source code or deployment scripting. Ownership was confirmed in conversation on 2026-10-14. Grunt still maintains [Dependabot dependency monitoring](../policies/secure-code-vulnerabilities.md#dependency-vulnerability-monitoring) for its own repositories.

## Grunt CSA page 4 - Respond & Recover.pdf

**Question (R1 - Backup location):** Are the following copies of the application and data available: (1) Local running copy, (2) Local backup, and (3) Remote backup?

**Answer:** No, for a remote backup copy of the production backend database. The inspected PostgreSQL server has seven-day native backups and geo-redundant backup is disabled. Grunt confirmed that there are no separate database exports or backups in another account or region. A separate geo-redundant blob account exists, but its presence does not establish a remote copy of this database. The full production/local-backup/remote-backup arrangement is not in place for the inspected database. See the [Azure verification evidence](evidence/grunt-csa-azure-2026-10-14.json).

**Question (R2 - Backup rotation):** Are backups conducted at a frequency according to the application's RPO (Recovery Point Objective) and retained no longer than necessary?

**Answer:** Daily native backups are available, supporting the documented 24-hour RPO. The inspected backend PostgreSQL configuration retains native backups for seven days; Grunt confirmed there are no separate database exports or archives. This differs from the one-year retention stated in the [business continuity plan](../policies/business-continuity-and-disaster-recovery.md#backup-strategy) and [retention matrix](../policies/data-management-policy.md#data-retention-matrix). Do not describe the current database backup retention as one year. See the [live configuration evidence](evidence/grunt-csa-azure-2026-10-14.json) and [Microsoft's native backup documentation](https://learn.microsoft.com/en-us/azure/postgresql/backup-restore/concepts-backup-restore).

**Question (R3 - Immutable):** Are backups unable to be altered, deleted, or changed in any way once they are created?

**Answer:** No locked backup immutability policy was found in the inspected Azure setup. The separate backup blob container has no immutability policy or legal hold, and the inspected Recovery Services vault has no immutability setting and no protected items. The production database uses native PostgreSQL backups; no separate immutable archive was confirmed. This does not establish the administrator-proof, unchangeable backup control asked for. See the [Azure verification evidence](evidence/grunt-csa-azure-2026-10-14.json) and [Microsoft's immutable storage documentation](https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview).

**Question (R4 - Disaster recovery plan and testing):** Has disaster recovery (DR) requirements for the application been satisfied?

**Answer:** Yes, for Grunt's documented recovery objectives. A restore/disaster recovery test on April 21, 2026 met both the 24-hour RTO and the 24-hour RPO. The test date and outcome were confirmed in conversation on 2026-10-14. The [business continuity plan](../policies/business-continuity-and-disaster-recovery.md#recovery-objectives) defines these objectives, and the [restore test procedure](../procedures/data-restore-test.md) describes the testing process. Separate CBRE-specific acceptance requirements are not established by this confirmation.

## Confirmation status

All requested Grunt owner confirmations have been recorded. No further answers are pending from you. Customer-specific integrations and unavailable standards remain qualified in the relevant answers and response notes.

## Response notes

P3, P4, and P6 describe Grunt's provisioning, access reviews, and SSO capabilities. They do not assert integration with customer-operated myID/UAA or the specifically named CBRE IdP. Customer configuration is not a prerequisite for recording Grunt's vendor response. If the form requires a binary answer for those integrations, the capability statements alone do not establish Yes.

The customer's referenced cryptography standard was not supplied. P10 and P11 state Grunt's documented encryption controls without claiming conformance to that unavailable standard. Customer-specific control applicability and acceptance remain with the questionnaire recipient.

## Azure verification on 2026-10-14

[Sanitized configuration evidence](evidence/grunt-csa-azure-2026-10-14.json) records the inspected resources and method. Checks used existing read-only Azure access and DNS lookups. No infrastructure settings, permissions, credentials, or policies were changed.

| Check | Observed result | Effect on the response |
| --- | --- | --- |
| API WAF | No matching Azure WAF/Front Door/Application Gateway resource; API domains resolve directly to Azure Container Apps; owner confirmed Cloudflare is not used for the APIs | P12 answers No for the inspected API paths |
| Backend database backups | Seven-day native retention; geo-redundancy disabled; owner confirmed no separate database exports | R1 cannot claim a remote database backup; R2 states seven days |
| Backup immutability | Separate backup container has no immutability policy or legal hold; inspected vault has no immutability setting and no protected items | R3 cannot claim locked immutable backup protection |
| CrowdStrike | No named sensor/sidecar image in inspected production manifests; no matching deployment source | P1 answers No; owner confirmed Grunt does not deploy CrowdStrike/Falcon |

The live seven-day database retention conflicts with the policy's one-year statement. Record the current configuration accurately and reconcile the policy or backup strategy through the normal change process. This assessment does not change either.

The separate geo-redundant storage account does not by itself prove database backup coverage. Data-plane access to list backup contents was denied, and no access keys or broader permissions were used to bypass that limit.
