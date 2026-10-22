# Grunt ONE
## Organization integration guide

**For developers and integration administrators**

**Review draft · 21 October 2026**

This optional guide covers backend access to Grunt's MCP services using organization credentials. It is intended for a service integration that operates without an interactively signed-in user.

Users connecting Claude or another supported assistant through Grunt sign-in should follow **Grunt ONE - Getting started**. They do not need to create an organization client for that workflow.

### Access and ownership

An administrator creates an integration client. The backend exchanges its client ID and secret for an access token, then uses that token to call Grunt's MCP service.

Assets created through this integration belong to the organization and are accessible to its other MCP clients. They are separate from user-owned assets and do not automatically appear in a user's personal asset list. Organization credentials do not convert existing personal assets into organization assets.

### Prerequisites

| Requirement | Purpose |
| --- | --- |
| Organization access and administrator permissions | Create the integration client in the Client Portal. |
| Backend secret store | Protect the client secret outside prompts, user devices and shared documents. |
| OAuth client-credentials implementation | Obtain access tokens and request replacements on expiry. |
| Compatible MCP implementation | Call the service over Streamable HTTP and handle its tools and responses. |
| Integration owner | Maintain credentials, application access and operational support. |

See the **Solution overview - Evaluation scope** for included access and the **IT and security overview** for service controls. This integration needs an MCP client/runtime that supports backend authentication.

> **INPUT NEEDED - G01/G14:** Enabled organization access, administrator role and supported backend client/runtime.

References: [Connection and authentication](https://docs.grunt.io/mcp-server/connect-and-authenticate) · [Asset ownership](https://docs.grunt.io/mcp-server/index)

<!-- pagebreak -->

## Configure the integration

### Create the client

1. Open the organization's **Integrations** page in the Client Portal.
2. Select **Create client**.
3. Choose **MCP server** under **Access**.
4. Capture the one-time secret and store it in the integration backend's secret store.
5. Under **MCP connection details**, copy the MCP server URL, token endpoint, resource and scope for your environment. Retain these with the client ID in the integration configuration.

If the Integrations page is unavailable, check permissions and enablement with the organization administrator or Grunt support. Never put client secrets in assistant prompts or distribute them to ordinary assistant users.

### Obtain and use an access token

The hosted MCP endpoint is `https://mcp.grunt.io/mcp`, with production authorization at `https://auth.grunt.io/`. Use the token endpoint and exact resource copied from the Client Portal for your environment.

Request a token with the `client_credentials` grant, client ID, client secret, `mcp.access` scope and exact advertised resource. Send the returned access token as a bearer token when calling MCP. The scope includes creation, reading and updates; it is not a read-only grant.

The [authentication guide](https://docs.grunt.io/mcp-server/connect-and-authenticate) provides token-request and tool-discovery examples. Use an MCP SDK to handle initialization and protocol negotiation, then use the current tool names and input schemas returned by the server.

Organization access tokens currently last five minutes. Use the returned expiry to request a replacement token. The client-credentials flow does not issue a refresh token.

> **INPUT NEEDED - G14:** Tested backend client/runtime configuration and successful tool-call example for this environment, plus applicable rate limits, timeout and retry behavior.

### Verify the connection

Use approved sample data to discover tools, create an asset and inspect its values. Check that the asset belongs to the organization and that access from another authorized organization client behaves as expected. Record the tested environment, configuration and date.

Complete the asset checks as well as token acquisition. If the integration supplies PowerPoint or web outputs, check those outputs separately.

References: [Full authentication procedure](https://docs.grunt.io/mcp-server/connect-and-authenticate) · [Tool reference](https://docs.grunt.io/mcp-server/tools)

<!-- pagebreak -->

## Credentials and operations

### Credential lifecycle

Integration credentials are created, rotated and revoked through the Client Portal. The integration owner should maintain a procedure for updating the backend secret store and checking dependent services after a credential change.

Keep client secrets and access tokens out of application logs, support requests, screenshots and prompts. Token renewal is a backend responsibility; users should not have to refresh the service integration manually.

> **INPUT NEEDED - G14:** Exact credential rotation/revocation procedure, replacement-secret rollout and the effect on already-issued access tokens.

### Asset and link access

Revoking an integration credential must not be treated as withdrawal of an already distributed asset link. MCP view links expose underlying data, do not expire and cannot currently be revoked. Sharing, deletion and offboarding require separate treatment from service authentication.

See **Getting started - Collaboration and handover** for account-transfer procedures and **IT and security overview** for processing locations, access controls, retention and deletion.

For timeouts or transient errors, check whether the asset was created or updated before retrying. Repeating a creation call can create another asset.

### Troubleshooting

| Symptom | First check |
| --- | --- |
| Integrations page is missing | Organization role and MCP product enablement. |
| Token request fails | Environment, client ID/secret, scope and token-request configuration. |
| Calls later become unauthorized | Returned expiry, replacement-token acquisition and credential status. |
| Asset is missing | Organization ownership context and the integration identity used. |
| Tool fails after authentication | Tool discovery, current schema and the returned error/reference ID. |

For support, include the endpoint, approximate UTC time, tool name and reference ID. Exclude tokens and secrets. Contact [Grunt support](mailto:support@grunt.pro).

References: [Credential handling and troubleshooting](https://docs.grunt.io/mcp-server/connect-and-authenticate) · [Sharing rules](https://docs.grunt.io/mcp-server/tools#share-an-asset)
