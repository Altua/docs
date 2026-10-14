# Grunt control self-assessment

**Product:** Grunt PowerPoint add-in

**Prepared for:** Turner & Townsend

**Date:** October 14, 2026

## Grunt CSA page 1 - AI[35].pdf

**Question (A1 - AI dependencies):** Does the app or tool provide or use AI capabilities?

**Answer:** Yes. Grunt provides optional AI functionality. It processes content submitted by the user when those features are invoked. Core PowerPoint add-in functionality does not require AI.

**Question (A2 - GenAI):** Does the application generate new content (such as text, images, code, audio, or video) using patterns learned from data?

**Answer:** Yes. Grunt uses generative AI to produce outputs based on user-provided inputs and the capabilities of the underlying models. Customer content is processed only when the user invokes an AI feature.

**Question (A3 - Agentic AI):** Can the application autonomously plan and execute actions to achieve goals with minimal human intervention?

**Answer:** Yes. The AI workflow inside the PowerPoint add-in uses an externally managed model and Grunt-provided tools. It can make several tool calls to carry out a user's request. The user must accept the final slide changes before they are applied locally.

**Question (A4 - MaaS (Model as a Service) AI):** Does the application consume AI models through externally managed APIs or platforms rather than hosting or training the models itself?

**Answer:** Yes. The add-in consumes externally managed AI models through Azure OpenAI. Grunt does not host or deploy the underlying models itself.

**Question (A5 - A2A (Agent-to-Agent) AI):** Does the application involve multiple AI agents that interact or coordinate with each other to complete tasks?

**Answer:** No. The PowerPoint add-in does not use multiple AI agents that communicate or coordinate with each other to complete tasks.

**Question (A6 - Endpoint AI):** Does the application perform automated actions powered by AI outputs locally on the user's device (e.g., laptop, mobile, desktop)?

**Answer:** Yes, after user approval. Once the user accepts AI-generated changes, the PowerPoint add-in automatically applies them locally in PowerPoint.

**Question (A7 - Model scans (OSS)):** Are open-source model scans performed for security and compliance?

**Answer:** Not applicable to model artifacts hosted or deployed by Grunt. Grunt uses externally managed models and does not host or deploy the underlying models. Code and dependency scanning applies to Grunt's application and integrations.

**Question (A8 - Red teaming for control validation):** Is red teaming performed to validate AI security controls?

**Answer:** No structured AI red teaming program is currently in place. Grunt has general external penetration testing, but no structured program specifically validating AI controls against adversarial prompts and other AI attacks.

**Question (A9 - Explainability via provenance and observability):** Is explainability ensured through provenance and observability mechanisms?

**Answer:** No, for full provenance and explainability. Request-level observability is in place: Grunt logs model name/version, request ID, timestamps, token counts, processing steps, and success/failure. Logs contain only metadata. Input content is never logged for privacy reasons, and requests are not linked to source content through source identifiers.

**Question (A10 - Token rate limit enforcement and monitoring):** Are token rate limits enforced and monitored for misuse?

**Answer:** Yes. Grunt limits and monitors both request counts and token consumption. AI generation requests exceeding rate limits receive a 429 Too Many Requests response.

**Question (A11 - Data pipeline security):** Is data pipeline security implemented to prevent tampering or leakage?

**Answer:** Yes, for application-level data pipeline controls. The AI workflow uses Azure OpenAI with a fixed list of Grunt-provided tools, permission checks, and validation of tool arguments and model responses. Encryption, access controls, network segregation, and restrictions on model training protect the flow. Users must accept final slide changes before local application. These controls do not include comprehensive AI data provenance or poisoning detection.

**Question (A12 - Sensitive data refinement):** Is differential privacy or anonymization applied to sensitive datasets?

**Answer:** No, for customer content submitted to AI features. Grunt sends the submitted content as is, without anonymization, masking, or differential privacy before submission. Separately, non-production testing requires synthetic, masked, anonymized, or sanitized data.

**Question (A13 - Runtime model monitoring):** Are runtime model scans implemented to detect vulnerabilities?

**Answer:** Not applicable to Grunt-managed model artifacts. Grunt uses externally managed models and does not manage model weights or inference infrastructure. Runtime model scanning is outside Grunt's direct operation.

**Question (A14 - Incident response playbooks for AI):** Are incident response playbooks established and tested for AI-related failures or security incidents?

**Answer:** No dedicated AI incident playbooks. AI-related incidents follow Grunt's general incident response plan, which covers information security and privacy incidents and requires annual testing. There is no separately tested AI-specific playbook.

**Question (A15 - Adversarial prompt guardrails):** Are adversarial prompt guardrails implemented?

**Answer:** Partially. Azure OpenAI's standard content filters are enabled. Grunt restricts the AI workflow to a fixed tools list, applies permission checks, and validates tool arguments and model responses. Grunt adds no separate prompt/output filters beyond that validation. Dedicated prompt injection or jailbreak defenses are not claimed.

**Question (A16 - Human in the loop):** Is a human in the loop?

**Answer:** Yes, for approval of the final slide changes. The user must accept those changes before the add-in applies them. Intermediate tool calls do not require individual approval. Customers are required to review and validate AI output before relying on it.

## Grunt CSA page 2 - Prevent.pdf

**Question (P0 - AI access authentication):** Is authentication enforced for AI system access?

**Answer:** Yes. The AI API endpoints used by the add-in require fingerprint or bearer authentication.

**Question (P1 - Endpoint security):** Is CrowdStrike deployed to all servers and containers?

**Answer:** No. Grunt does not deploy CrowdStrike/Falcon to its production servers or containers. The add-in APIs run in Azure Container Apps.

**Question (P2 - Privilege account management):** Are all privileged human accounts onboarded to either CyberArk or Delinea?

**Answer:** No. Grunt uses administrator accounts managed in Microsoft Entra ID, with least privilege and administrator MFA. These accounts are not onboarded to CyberArk or Delinea.

**Question (P3 - Access fulfillment):** Is user access fulfilled by an automated process (myID) or manually by the User Access Administration (UAA) Team?

**Answer:** Grunt supports automated user provisioning and deprovisioning through Microsoft Entra ID/SCIM. License managers can also manage users in the Grunt portal. myID and the UAA team are customer-operated processes that Grunt does not administer.

**Question (P4 - Access reviews):** Is the application integrated with myID for periodic user access reviews?

**Answer:** Integration with customer-operated myID access reviews is not confirmed. Grunt reviews its own internal access rights annually and adjusts them as needed.

**Question (P5 - MFA):** Is MFA (Multifactor Authentication) enabled for the application or tool?

**Answer:** Yes. Grunt requires MFA. Microsoft Entra ID SSO also applies the organization's conditional access policies.

**Question (P6 - SSO):** Is the application or tool onboarded to the CBRE IdP (Identity Provider) solution with SSO (Single Sign-on) enabled?

**Answer:** Grunt supports Microsoft Entra ID SSO. When SSO is enabled for an organization's email domain, users authenticate through Entra ID and the organization's conditional access policies apply. Onboarding to the specifically named CBRE IdP is not confirmed.

**Question (P7 - Privilege access management):** Are privileged access accounts onboarded to the CBRE PAM (privileged account management tool)?

**Answer:** No. Grunt's administrator accounts are managed in Microsoft Entra ID and are not onboarded to CBRE's PAM platform.

**Question (P8 - Secrets detection):** Are source code repositories enrolled in the CBRE secrets detection platform?

**Answer:** No. Grunt's repositories are not connected to the CBRE secrets detection platform. Grunt uses Claude for secrets checks.

**Question (P9 - Secrets vaulting):** Are production secrets stored in and fetched from the enterprise secrets vault?

**Answer:** Yes, for Grunt-operated services. All production secrets are stored in and retrieved from Azure Key Vault, including passwords, tokens, API keys, and certificates.

**Question (P10 - Encryption at rest):** Is encryption at rest implemented?

**Answer:** Yes. Grunt-managed storage and databases use AES-256 encryption at rest. Backups are encrypted. Customer-managed local files follow the customer environment's controls.

**Question (P11 - Encryption in transit):** Is encryption in transit implemented?

**Answer:** Yes. Grunt uses TLS 1.2/1.3 for data in transit.

**Question (P12 - Web application firewall (WAF) - external):** Has a WAF (Web Application Firewall) been implemented with blocking mode enabled?

**Answer:** No. A blocking-mode WAF is not implemented for the public add-in API endpoints. The APIs use public Azure Container Apps ingress. Grunt uses Cloudflare elsewhere, but not for these APIs.

## Grunt CSA page 3 - Limit Damage.pdf

**Question (L1 - Incident response integration):** Are application security events sent to the Incident Response platform (e.g., Databahn)?

**Answer:** No dedicated incident response platform integration. Grunt handles application security events through Azure logs and alerts and follows its general incident response plan. There is no reported integration with a customer incident response platform such as Databahn.

**Question (L2 - Secrets detection):** Are source code repositories enrolled in the CBRE secrets detection platform?

**Answer:** No. Grunt's repositories are not connected to the CBRE secrets detection platform. Grunt uses Claude for secrets checks.

**Question (L3 - Static application security testing (SAST)):** Have production components completed static analysis scanning?

**Answer:** Yes. All production components are scanned with SonarCloud. Scans run on pull requests and main branch updates. Failed quality gates or critical security issues block merges.

**Question (L4 - Open source management - third party dependency vulnerabilities):** Have production repositories been scanned for open source and third party dependency vulnerabilities?

**Answer:** Not applicable under the questionnaire guidance because all source code and deployment scripting is managed by Grunt, with no CBRE-managed source code or deployment scripting. Grunt maintains Dependabot dependency vulnerability monitoring for its own repositories.

## Grunt CSA page 4 - Respond & Recover.pdf

**Question (R1 - Backup location):** Are the following copies of the application and data available: (1) Local running copy, (2) Local backup, and (3) Remote backup?

**Answer:** No, for a remote backup copy of the production backend database. The database has seven-day native PostgreSQL backups, with geo-redundant backup disabled. There are no separate database exports or backups in another account or region. The full running-copy/local-backup/remote-backup arrangement is therefore not in place for this database.

**Question (R2 - Backup rotation):** Are backups conducted at a frequency according to the application's RPO (Recovery Point Objective) and retained no longer than necessary?

**Answer:** Daily native PostgreSQL backups support Grunt's 24-hour RPO. Production backend database backups are retained for seven days. There are no separate database exports or archives.

**Question (R3 - Immutable):** Are backups unable to be altered, deleted, or changed in any way once they are created?

**Answer:** No locked backup immutability policy is in place in the inspected Azure setup. The production database uses native PostgreSQL backups, with no separate immutable archive. The separate backup blob container has no immutability policy or legal hold.

**Question (R4 - Disaster recovery plan and testing):** Has disaster recovery (DR) requirements for the application been satisfied?

**Answer:** Yes, for Grunt's recovery objectives. A restore/disaster recovery test on April 21, 2026 met both the 24-hour RTO and the 24-hour RPO. This does not certify separate CBRE-specific acceptance requirements.
