# Grunt ONE: information needed to complete the guides

Internal working list · Updated 21 October 2026

The identifiers below match visible INPUT NEEDED placeholders and configuration fields in the PDFs. Owner roles are suggestions; no individual has been contacted. All fourteen items remain open, but documented portions should not be researched from scratch.

Primary locations: Getting started contains G01–G10; IT and security overview contains G11–G12 and a shared G10/G11 access field; Solution overview contains G13 and shared G01/G02/G11 evaluation fields; the optional Organization integration guide contains G14 and a shared G01/G14 prerequisite field.

## Prioritized follow-up checklist

Start with items 1 and 2. Item 3 can run in parallel once the evaluation configuration is named. Conditional workflows do not need to delay the standard package if they are explicitly excluded from the offer.

| Done | Priority / action | Ask whom | What to bring back | IDs |
| --- | --- | --- | --- | --- |
| [ ] | **1. Define the actual evaluation offer.** Identify included products, released versus pilot capabilities, activation, subscriptions and required clients. | Product + CS/commercial owner | One dated configuration sheet: release/build, eligible customers, enabled tools, assistant app/plan, add-in/Office requirements, included allowance, separately supplied subscriptions/keys, and activation owner/action. Mark excluded items explicitly. | G01/G02/G13 |
| [ ] | **2. Demonstrate one complete first-user workflow.** Fresh Claude connection, chart, editor/save, PowerPoint placement, revision and recipient check. | CS + Engineering | One annotated recording or screenshots using the 120 + 18 + 12 - 5 sample, then revise 12 to 10. Record builds, exact steps, expected outputs and failures. Totals: 145, then 143. | G02–G07 |
| [ ] | **3. Obtain the ONE-specific IT answers.** Cover data flows, controls, retention and link access for the named configuration. | Security + Engineering | Completed service/security schedule and original policy sections, with applicability to ONE. Include providers/regions, data categories, DPA, allowlist, encryption, tenant/access controls, MFA/SSO, audit access, backup/recovery, incident handling, deletion/export and current sharing-link behavior. | G11/G12 |
| [ ] | **4. Confirm team continuity.** Establish how users share work and what happens when someone leaves. | Product + Engineering/Security | Supported discovery/edit/transfer/offboarding procedure, account-access effects and treatment of distributed links. Distinguish technical account ownership from contractual content rights. | G10/G11/G12 |
| [ ] | **5. Complete optional user routes, if offered.** HTML and additional assistants. | Web Product + Integrations Engineering | Tested setup/delivery instructions, client plans, recipient/offline behavior; otherwise record that the route is outside this evaluation. | G08/G09 |
| [ ] | **6. Complete the backend guide, if needed.** Validate implementation and operations. | Integrations Engineering + Security | Tested SDK/runtime and tool call, applicable limits/retry behavior, rotation/revocation procedure and issued-token behavior. Existing published token examples are already linked. | G14 |
| [ ] | **7. Confirm later-wave wording and hosting scope.** Keep the roadmap distinct from the current offer. | Product + Engineering | Approved status wording, supported sync directions/update/conflict/version controls; no invented dates. For a hosting evaluation, identify the actual pilot package, limitations, connectivity, identity and operational responsibilities. | G13/G11 |
| [ ] | **8. Final editorial and distribution check.** Resolve placeholders for included routes, review actual offer and regenerate PDFs. | Product + Security + CS; communications owner if available | Named review of the applicable copy, verified links and tested workflow. An official tone guide if available; otherwise review the proposed plain, direct style. | All applicable items |

Items 1–4 support the standard customer package. Items 5–7 become necessary where the corresponding capabilities are included. A localhost pilot is not evidence of production hosting readiness. No item is complete merely because documentation exists.

## Detailed requests: access and Claude-to-PowerPoint walkthrough

| ID | Information needed | Suggested owner |
| --- | --- | --- |
| G01 | Per-workflow Grunt entitlements, activation action/owner, administrator role, assistant subscription and model API-key requirements. Distinguish model keys from OAuth credentials. | Product / CS / commercial owner |
| G02 | Exact tested Claude application, plan, version/OS where relevant, organization connector policy, Grunt add-in and Office builds; verification date. | Engineering / CS |
| G03 | Exact Claude settings path, connector fields, administrator approval, OAuth screens and successful connection state. Supply setup and connected-state screenshots. | Engineering / CS |
| G04 | Successful sample waterfall prompt/output: preview, asset reference, available actions and the action opening the editor. Supply a result screenshot and test record. | Engineering / CS |
| G05 | Editor entry action/URL, authentication/edit permission, save action and saved-version confirmation. Supply entry/save screenshots. | Product / Engineering |
| G06 | Exact PowerPoint export/import/insertion steps, supported objects/formats, minimum builds, template constraints and editable/linked/fixed behavior. Supply transfer and inserted-object screenshots. | PowerPoint Engineering / CS |
| G07 | How a revised asset reaches the existing slide; formatting preservation and snapshot handling; recipient viewing/editing and retained data/links. Verify 145 changes to 143 in the sample. | Engineering / CS |

## Detailed requests: alternate outputs and shared use

| ID | Information needed | Suggested owner |
| --- | --- | --- |
| G08 | HTML authoring setup/skill, creation/export steps, hosting or file delivery, reader access/network needs, embedded versus fetched data and actual offline behavior. | Web Product / Engineering |
| G09 | Additional supported assistant clients/plans and individually tested connection instructions. Explicitly state if none are verified. | Integrations Engineering |
| G10 | Asset discovery/reuse by colleagues, edit permissions, ownership transfer, employee departure and unsupported operations/support path. | Product / Engineering / Security |

## Required for the technical assessment

| ID | Information needed | Suggested owner |
| --- | --- | --- |
| G11 | Route-specific content categories/providers/regions/operators, DPA/subprocessors, customer model-key support, endpoint/port allowlist and security/support contact. ONE-specific encryption, tenant/access boundaries, SSO/MFA, administrator access, audit visibility, backup/recovery, incident process and account-removal effects. For a hosting pilot: named package, external dependencies and operating responsibilities. | Security / Engineering |
| G12 | Original applicable retention schedule, per-asset/version/upload/log/backup deletion and export behavior, policy amendment covering ONE, effect on URLs and current link controls. | Security / Product / Engineering |

G08–G10 become onboarding prerequisites when those workflows are included. G11–G12 are material to the IT assessment and are not optional release polish.

## Efficient way to supply the answers

Provide one annotated screen recording or step-by-step capture of: fresh Claude connection → sample chart → editor → saved revision → PowerPoint insertion → revision → recipient check. Include application/build details and use sample data only. This can resolve G02–G07 together.

For every item record: answer, source or named owner, date, applicable environment/release, evidence location and any limitations. Screenshots must omit credentials and personal/customer information.

## Existing evidence to preserve

The endpoint `https://mcp.grunt.io/mcp`, OAuth route, organization credential procedure and ownership distinction are already documented. Keep them unless newer evidence changes them. Permanent MCP links currently have documented underlying-data access and no expiry/revocation; no replacement revocation behavior is established. Live deck control and customer hosting remain development-scoped.

The existing R01–R18 decision register remains authoritative for research history. Mapping: G01→R05/R11/R12/R17; G02–G04→R01/R02/R17/R18; G05–G07→R07/R14/R16/R18; G08→R01/R16; G09→R02; G10→R03/R07; G11→R05/R06/R08/R10/R14; G12→R06/R07/R08.


## Release and roadmap confirmation — added 21 October

| ID | Information needed | Suggested owner |
| --- | --- | --- |
| G13 | Confirm released, limited-access and planned capabilities by wave, with build/date, eligibility and supported integrations. Synchronization is not in the first wave, per the user's clarification. Specify later-wave update directions, automatic versus explicit behavior, conflicts and snapshot controls. Do not infer dates. | Product / Engineering / commercial owner |

G13 maps to R01/R09/R16/R18. The user's clarification confirms first-wave exclusion of synchronization; it does not independently confirm release status for other capabilities.


## Optional Organization integration guide

| ID | Information needed | Suggested owner |
| --- | --- | --- |
| G14 | Validate the published token request in the target environment; tested MCP SDK/runtime, initialization and sample tool call. Confirm applicable limits/throttling, timeout/retry behavior, exact portal credential rotation/revocation, replacement-secret rollout and already-issued token behavior. | Integrations Engineering / Security |

G14 maps to R02/R04/R17/R18 and appears only in the optional Organization integration guide. G01/G10/G11/G12 remain shared references for enablement, ownership and service data handling. Getting started now contains user sign-in only.

## Evidence update and policy action - 21 October

Internal Support access was restored. Approved documentation at commit `89c80a8412f5b94ac83d5ca34573b67542d7bead` supplies portal connection-detail fields, the client-credentials token request, tool-list example, SDK guidance and duplicate-creation warning. These are documented instructions, not a test performed for this package. The Grunt ONE index describes a localhost hosting pilot and keeps production deployment in development. The guides now reflect these distinctions; no full G item is closed.

Sources: [Authentication](https://github.com/Altua/Oak/blob/89c80a8412f5b94ac83d5ca34573b67542d7bead/docs/public/mcp-server/connect-and-authenticate.mdx) - [Grunt ONE](https://github.com/Altua/Oak/blob/89c80a8412f5b94ac83d5ca34573b67542d7bead/docs/public/grunt-one/index.mdx) - [Connected workflows](https://github.com/Altua/Oak/blob/89c80a8412f5b94ac83d5ca34573b67542d7bead/docs/public/grunt-one/connected-workflows.mdx).

Retain the user's instruction to assume existing policies apply equally to ONE for drafting. Security/Product must make the policy wording explicitly cover assets, versions, uploads, logs and backups, and revise guide wording if actual handling differs. This amendment action is internal, not customer-facing copy. The original one-year retention claims remain independently unverified. The communication profile remains unavailable; the style is an editorial recommendation, not certified brand compliance.
