# Grunt ONE
## IT and security overview

**Review draft · 21 October 2026**

This document explains the service boundaries, data flows and access controls relevant to a technical assessment. Connection steps are in **Grunt ONE - Getting started**.

### Hosted architecture

<!-- graphic:hosted -->

An external assistant receives the user's prompt and supplied data, calls Grunt tools, and receives the results. Tool results can include underlying values and object structure as well as previews and links. The assistant provider therefore processes both user inputs and returned tool content.

The Web Editor connects to Grunt's asset services to retrieve content and save changes. Assets and versions persist for continued editing and reuse.

Two AI routes have separate processing arrangements. In the external-assistant route shown above, the assistant provider handles the conversation and returned Grunt tool content. In Grunt-managed AI, content supplied to the AI feature passes through Grunt's AI service and its model provider, and the result returns to the Grunt interface. The service details on the final page identify the provider, content categories and processing locations still to be confirmed for each enabled route.

References: [MCP services](https://docs.grunt.io/mcp-server/index) · [Tool reference](https://docs.grunt.io/mcp-server/tools) · [Desktop data handling](https://docs.grunt.io/powerpoint-add-in/it/faq)

<!-- pagebreak -->

## Identity and ownership

<!-- graphic:identity -->

### User sign-in

A compatible assistant opens Grunt sign-in and authorization. Assets created through this connection are associated with the signed-in user's account.

### Organization integration

A backend integration creates assets under the organization's account. Other MCP clients for that organization can access them; they do not automatically appear in a user's personal asset list.

These are account and access distinctions. Contractual rights to customer content are governed by the applicable terms.

Organization integration is a separate developer-managed route, not an additional step in ordinary assistant onboarding. Implementation details are in **Grunt ONE - Organization integration guide**.

### Access across connected tools

The selected setup needs to specify sign-in and permissions for the assistant connection, Web Editor and PowerPoint integration. Existing desktop access does not automatically grant access to every service. Account removal also needs to address saved assets and previously distributed links.

> **INPUT NEEDED - G10/G11:** Sign-in requirements for each service, applicable SSO/MFA and administrator controls, and the effect of account removal on access and saved work.

References: [MCP authentication](https://docs.grunt.io/mcp-server/connect-and-authenticate) · [Hosting and access](https://docs.grunt.io/grunt-one/hosting-and-access)

<!-- pagebreak -->

## Security and data lifecycle

### Security controls

Grunt's Trust Center provides security information and its ISO/IEC 27001:2022 certificate. The certificate covers Grunt AS's information security management system for its PowerPoint add-in business, including Azure infrastructure. Its scope should be reviewed against the services under assessment.

The applicable DPA and service security documentation describe the controls for the selected Grunt ONE services. The final page identifies the service-specific security details still needed for this assessment.

### AI processing

Content submitted to Grunt's AI functionality is not used for model training. Grunt contractually prohibits its AI subprocessors from using that content for training. A customer-selected external assistant has its own processing terms.

Provider, processing region and applicable terms remain to be confirmed for each AI route in the service details.

### Storage, retention and exit

Grunt's privacy and data-management policies govern content handling. Temporary AI processing and persistent asset storage serve different purposes: saved assets and versions support continued editing and reuse.

The retention periods and deletion procedures for saved assets, versions, uploads, logs and backups remain to be supplied in the service details.

Under the published terms, customers can request export of content on Grunt-operated infrastructure within 30 days of contract termination or expiry. Subsequent deletion follows the privacy policy, subject to legally required retention. Copies already delivered to recipients remain with those recipients.

References: [Trust Center](https://trust.grunt.pro/resources) · [Privacy policy](https://app.grunt.pro/privacy-policy) · [Subprocessors](https://trust.grunt.pro/subprocessors) · [Terms, section 4.4](https://app.grunt.pro/terms)

<!-- pagebreak -->

## Sharing and operational requirements

<!-- graphic:sharing -->

An edit link grants broader access, including the model needed for local Grunt editing. Asset creation may return a permanent view link, so underlying-data access is relevant before a separate sharing action.

Forwarding a link or a file containing it can extend access. Removing an assistant connection, clearing a conversation or revoking integration credentials must not be treated as withdrawal of an existing asset link. Time-limited or revocable access requirements need to be resolved before relying on these links.

### Service dependencies

| Area | Assessment requirement |
| --- | --- |
| Network | MCP, authentication, editor and asset services, the assistant provider and integration-specific endpoints. Service allowlist: to be supplied in the service details. |
| Subscriptions | Grunt product access and seats, Grunt AI allowance, and any external assistant subscription or API charges. |
| Ownership | User-owned versus organization-owned assets, administrator roles and offboarding responsibilities. |
| Operations | Credential storage and rotation, software updates, support ownership and incident procedures. |

Authentication tokens authorize access; they are not AI usage credits. AI allowances and external assistant subscriptions are separate commercial items. The included products, allowances and separately supplied subscriptions are listed in the Solution overview's evaluation scope.

References: [Sharing rules](https://docs.grunt.io/mcp-server/tools#share-an-asset) · [Network guidance](https://docs.grunt.io/powerpoint-add-in/it/network-and-security) · [Hosting and usage](https://docs.grunt.io/grunt-one/hosting-and-access)

<!-- pagebreak -->

## Hosting options and service details

| Option | Scope and current position |
| --- | --- |
| Grunt-hosted | Grunt operates the MCP and asset services. An external assistant has its own processing boundary, as shown in the architecture diagram. |
| Customer-hosted / on-premises | Intended to cover MCP, Web Editor, asset storage, history, rendering and exports. A localhost pilot is documented; production deployment remains in development. Hosting these services does not also host the external assistant or AI model. |

Customer hosting is not a fully disconnected setup. Its design includes external AI connectivity and service connections for identity, entitlement, usage and releases. A production deployment also needs storage, backups, TLS and an update process. Any proposed pilot needs its own configuration and operating responsibilities.

### Service and security details

> **INPUT NEEDED - G11:** For each enabled service and AI route: operator, content processed, storage/processing region, DPA and subprocessors, service endpoint/port allowlist, and supported model-provider configuration.

> **INPUT NEEDED - G11:** Applicable encryption, tenant/access boundaries, SSO/MFA, administrative access, audit visibility, backup/recovery arrangements, and security incident contact and process.

### Retention, deletion and export

> **INPUT NEEDED - G12:** Retention periods and deletion/export procedures for assets, versions, uploads, logs and backups; the effect of deletion on published links; and the release's available link controls.

These fields are not yet specified for the evaluation configuration. The applicable policy and operational schedule will provide the service-specific details; no retention period is stated in this draft.

References: [Hosting and access](https://docs.grunt.io/grunt-one/hosting-and-access) - [Privacy policy](https://app.grunt.pro/privacy-policy) - [Terms](https://app.grunt.pro/terms)
