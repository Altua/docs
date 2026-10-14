# Grunt – AI control self-assessment (CSA)

**Status:** Draft

**Product scope:** Grunt PowerPoint add-in. External AI clients and standalone MCP integrations are outside this assessment.

**Owner:** Not assigned

**Added:** 2026-10-13

**Last reviewed:** Not reviewed

**Reviewed by:** Not reviewed

**Source:** Full questionnaire and initial responses supplied while preparing a customer CSA. Product scope and AI behavior were confirmed in conversation on 2026-10-13 and 2026-10-14. Provider settings, application validation, incident response scope, and final-change-only approval were confirmed on 2026-10-14. The answer limitations are documented below. Questionnaire version not supplied.

## 1. AI dependencies

**Question:** Does the app or tool provide or use AI capabilities?

**Answer:** Yes

**Comments:**

Grunt provides optional AI-powered functionality as part of its software offering. AI features process user-submitted content to generate requested outputs. These features are initiated by the user and are not required for the core PowerPoint add-in functionality.

**References:**

- [IT FAQ: Data and privacy](../powerpoint-add-in/it/faq.mdx#data-and-privacy)

**Review notes:** The IT FAQ describes optional AI processing separately from standard Excel and PowerPoint functionality. The scope of this assessment is the PowerPoint add-in.

## 2. GenAI

**Question:** Does the application generate new content (such as text, images, code, audio, or video) using patterns learned from data?

**Answer:** Yes

**Comments:**

Grunt offers generative AI functionality that produces outputs based on user-provided inputs and the capabilities of underlying AI models. Customer content is processed only when the user explicitly invokes the relevant AI feature.

**References:**

- [IT FAQ: Data and privacy](../powerpoint-add-in/it/faq.mdx#data-and-privacy)

**Review notes:** Preserve the examples in the original question without implying that Grunt supports every listed output type. User invocation was confirmed in conversation on 2026-10-13.

## 3. Agentic AI

**Question:** Can the application autonomously plan and execute actions to achieve goals with minimal human intervention?

**Answer:** Yes

**Comments:**

The AI workflow inside the PowerPoint add-in uses an externally managed model and Grunt-provided tools. It can make several tool calls to carry out a user request before the user accepts the final changes. User acceptance is required before those changes are applied locally.

**References:**

- [MCP server overview](../mcp-server/index.mdx)
- [MCP tool reference](../mcp-server/tools.mdx)

**Review notes:** Confirmed in conversation on 2026-10-13. The tool workflow runs inside the add-in.

## 4. MaaS (Model as a Service) AI

**Question:** Does the application consume AI models through externally managed APIs or platforms rather than hosting or training the models itself?

**Answer:** Yes

**Comments:**

The PowerPoint add-in consumes externally managed models through Azure OpenAI. Grunt does not host or deploy the underlying models itself. These models support the AI features integrated into the add-in.

**Review notes:** Azure OpenAI was confirmed as the current provider in conversation on 2026-10-14.

## 5. A2A (Agent-to-Agent) AI

**Question:** Does the application involve multiple AI agents that interact or coordinate with each other to complete tasks?

**Answer:** No

**Comments:**

The PowerPoint add-in does not use multiple independent AI agents that communicate or coordinate with one another to complete tasks.

**Review notes:** Confirmed in conversation on 2026-10-13.

## 6. Endpoint AI

**Question:** Does the application perform automated actions powered by AI outputs locally on the user's device (e.g., laptop, mobile, desktop)?

**Answer:** Yes, after user approval

**Comments:**

Once the user accepts AI-generated changes, the PowerPoint add-in automatically applies them locally in PowerPoint. Changes are not applied before acceptance.

**Review notes:** Confirmed in conversation on 2026-10-13.

## 7. Model scans (OSS)

**Question:** Are open-source model scans performed for security and compliance?

**Answer:** N/A for model artifacts hosted or deployed by Grunt

**Comments:**

The add-in uses externally managed models. Grunt does not host or deploy the underlying models itself. Model artifact scanning is therefore outside Grunt's direct operation. General application code and dependency scanning still applies.

**References:**

- [Security integration tests: General software scanning](../policies/security-integration-tests.md)

**Review notes:** Model hosting was confirmed in conversation on 2026-10-13. This answer does not assert a specific model scanning control at the external provider.

## 8. Red teaming for control validation

**Question:** Is red teaming performed to validate AI security controls?

**Answer:** No structured AI red teaming program

**Comments:**

Grunt maintains general security testing, including external penetration testing. A structured AI red teaming program specifically validating controls against adversarial prompts and other AI attacks is not currently in place.

**References:**

- [IT FAQ: General security testing](../powerpoint-add-in/it/faq.mdx#security)

**Review notes:** Confirmed in conversation on 2026-10-13.

## 9. Explainability via provenance and observability

**Question:** Is explainability ensured through provenance and observability mechanisms?

**Answer:** No for the full provenance and explainability control

**Comments:**

Grunt logs model name/version, request ID, timestamps, token counts, processing steps, and success/failure. Logs contain only this request metadata. Input content is never logged for privacy reasons, and requests are not linked to source content through source identifiers. Request-level observability is available, but the comprehensive data provenance described by the questionnaire is not.

**References:**

- [IT FAQ: Application operations](../powerpoint-add-in/it/faq.mdx#operations)

**Review notes:** The metadata fields and metadata-only logging scope were confirmed in conversation on 2026-10-13.

## 10. Token rate limit enforcement and monitoring

**Question:** Are token rate limits enforced and monitored for misuse?

**Answer:** Yes

**Comments:**

Grunt limits and monitors both AI request counts and token consumption.

**References:**

- [Grunt Pro API: Status code notes](../grunt-pro-api/index.mdx#status-code-notes)

**Review notes:** Confirmed in conversation on 2026-10-13.

## 11. Data pipeline security

**Question:** Is data pipeline security implemented to prevent tampering or leakage?

**Answer:** Yes for application-level data pipeline controls

**Comments:**

The in-add-in AI workflow uses Azure OpenAI, a fixed Grunt-provided tools list, permission checks, and validation of tool arguments and model responses. Users must accept final changes before the add-in applies them locally. Encryption, access controls, network segregation, and restrictions on model training are documented. This answer covers these controls and does not establish comprehensive AI provenance or poisoning detection.

**References:**

- [IT FAQ: Data and privacy](../powerpoint-add-in/it/faq.mdx#data-and-privacy)
- [Data management policy](../policies/data-management-policy.md)
- [Network segregation policy](../policies/network-segregation.md)

**Review notes:** Validation was confirmed in conversation on 2026-10-14. The named workflow controls are confirmed.

## 12. Sensitive data refinement

**Question:** Is differential privacy or anonymization applied to sensitive datasets?

**Answer:** No, for customer content submitted to AI features

**Comments:**

Grunt sends customer content to the AI service as submitted. It does not apply anonymization, masking, or differential privacy before submission. The separate non-production data policy requires synthetic, masked, anonymized, or sanitized testing data.

**References:**

- [Production data in non-production environments policy](../policies/production-data-in-non-production.md)
- [IT FAQ: Data and privacy](../powerpoint-add-in/it/faq.mdx#data-and-privacy)

**Review notes:** Production AI submission behavior was confirmed in conversation on 2026-10-13.

## 13. Runtime model monitoring

**Question:** Are runtime model scans implemented to detect vulnerabilities?

**Answer:** N/A for integrity scanning of Grunt-managed model artifacts

**Comments:**

Grunt uses externally managed models and does not manage the model weights or inference infrastructure. Runtime model artifact integrity scanning is outside Grunt's direct operation. Grunt remains responsible for monitoring its own application and AI integrations.

**Review notes:** Model hosting was confirmed in conversation on 2026-10-13. This answer does not assert a specific runtime monitoring control at the external provider.

## 14. Incident response playbooks for AI

**Question:** Are incident response playbooks established and tested for AI-related failures or security incidents?

**Answer:** No dedicated AI incident playbooks

**Comments:**

AI-related incidents follow the general Incident Response Plan, which covers all information security and privacy incidents and requires annual testing. This does not establish a separately tested AI-specific playbook.

**References:**

- [Incident response plan](../policies/incident-response-plan.md)

**Review notes:** Use of the general incident response plan was confirmed in conversation on 2026-10-14.

## 15. Adversarial prompt guardrails

**Question:** Are adversarial prompt guardrails implemented?

**Answer:** Partial; provider content filtering and application controls

**Comments:**

Azure OpenAI's standard content filters are enabled. Grunt restricts the workflow to a fixed tools list, applies permission checks, and validates tool arguments and model responses. It adds no separate prompt/output filters beyond validation. Dedicated prompt injection or jailbreak defenses are not claimed.

**References:**

- [Secure engineering principles](../policies/secure-engineering-principles.md)
- [Security integration tests](../policies/security-integration-tests.md)

**Review notes:** Filter settings and the absence of additional Grunt filters were confirmed in conversation on 2026-10-14.

## 16. Human in the loop

**Question:** Is a human in the loop?

**Answer:** Yes for final slide changes; not every intermediate input or output

**Comments:**

Users must accept the final slide changes before the add-in applies them. Intermediate tool calls do not require individual human approval. Human review therefore does not cover every AI input and output as described in the questionnaire guidance. The terms and conditions also require customers to review and validate AI output before relying on it.

**References:**

- [Terms and conditions](../policies/terms-and-conditions.md)

**Review notes:** The final-change-only approval scope was confirmed in conversation on 2026-10-14.
