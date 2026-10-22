# Grunt ONE
## Getting started

**Review draft - 21 October 2026**

Connect Claude to Grunt, create a sample chart, refine it in the Web Editor and place it in PowerPoint. This guide assumes the Grunt add-in is installed; it focuses on the Grunt ONE connection and workflow.

### Before you start

| You need | Details |
| --- | --- |
| Grunt ONE access | Grunt account, enabled products and user access. Activation is arranged through Sales or Customer Success. |
| A supported Claude client | Application and plan with permission to add the Grunt connection. |
| Compatible PowerPoint setup | Supported PowerPoint and Grunt add-in builds for the chosen import workflow. |
| Approved sample data | Use the fictional figures in this guide for your first task. |

An existing PowerPoint license does not automatically activate Grunt ONE. Your assistant uses Grunt user sign-in for this workflow; you do not need to create a backend integration client.

<!-- graphic:setup -->

See **Solution overview** for release status and **IT and security overview** for data handling and access requirements. Highlighted fields identify setup details still to be supplied for this review draft.

<!-- pagebreak -->

## Connect Claude and create a chart

> **INPUT NEEDED - G01:** Included products and AI allowance, activation steps, administrator role, separate assistant subscription and any model-provider key requirements.

> **INPUT NEEDED - G02:** Supported Claude application/plan, operating system, connector policy, PowerPoint version and Grunt add-in build.

### 1. Add the Grunt connection

1. Open the assistant's MCP or connector settings.
2. Add the remote server `https://mcp.grunt.io/mcp`.
3. Connect, sign in to Grunt and approve access.
4. Check that Grunt tools are available to the assistant.

> **INPUT NEEDED - G03:** Exact settings path, connector fields and approval steps for the selected Claude client, with connection and sign-in screenshots.

**Expected result:** The assistant can discover Grunt tools. Continue with the sample chart to check that it can use them.

**Administrator note:** The client must support remote MCP over Streamable HTTP with OAuth. Production authorization uses `https://auth.grunt.io/`. Assets created through user sign-in are associated with that user's Grunt account.

### 2. Create and inspect a chart

**Before supplying data:** Asset creation may return a permanent view link. Anyone with the link can access the visual and its underlying data. These links do not expire and cannot currently be revoked. Use the fictional sample below.

> Create a revenue waterfall in millions: opening revenue 120, expansion +18, new customers +12, churn -5. Show the closing total and explain the values used.

**Expected result:** The closing value is **145**. Check the labels and units, and ask the assistant to inspect the chart's data as well as its image.

> **INPUT NEEDED - G04:** Example result showing the chart, its asset reference and the action that opens it in the Web Editor.

References: [Connect an assistant](https://docs.grunt.io/mcp-server/connect-and-authenticate) - [Assets and tools](https://docs.grunt.io/mcp-server/tools)

<!-- pagebreak -->

## Refine the chart and use it in PowerPoint

### 3. Edit in the browser

Open the chart using its editor link. Inspect the data, change a label or color, and save a version.

> **INPUT NEEDED - G05:** Editor entry action, required sign-in or edit permission, save control and saved-version confirmation, with screenshots.

**Expected result:** The saved chart includes your change and you can identify the version to use in PowerPoint.

### 4. Place the chart in PowerPoint

Use the import or insertion route supported by your Grunt add-in. Eligible placements become editable Grunt objects; their data and formatting are edited with Grunt's tools.

> **INPUT NEEDED - G06:** Exact transfer steps, supported chart/table types and placement formats, required builds, and whether the result is editable, linked or fixed. Include a screenshot of the inserted result.

**Expected result:** The chart in PowerPoint matches the saved values and formatting, with the editing behavior specified for this setup.

### 5. Revise and check the result

Change new-customer revenue from +12 to +10 in the source asset. The expected closing total becomes **143**. Apply the supported replacement, re-import or refresh action to the presentation.

> **INPUT NEEDED - G07:** Revision steps, local-formatting behavior, how to preserve an approved version, and recipient viewing/editing requirements.

A local imported object saves PowerPoint edits in the presentation without automatically publishing them back to the web asset. Multidirectional synchronization is planned and is not in the first wave. Review any commentary affected by a change to the figures.

### Completion check

You can create a chart, inspect its data, edit and save it, place it in PowerPoint, and reproduce the revised total. Confirm that the intended recipient can open the presentation and that its links and embedded data are appropriate to share.

References: [Editing and output workflows](https://docs.grunt.io/grunt-one/connected-workflows)

<!-- pagebreak -->

## Other outputs, shared work and support

### HTML reports

The HTML workflow combines written analysis and Grunt visuals in a browser-readable report. Interactive refresh and offline saving are still in development.

> **INPUT NEEDED - G08:** Supported authoring client and HTML skill/setup, creation and delivery steps, recipient access, and whether data is embedded or fetched. Specify the released offline behavior.

### Other assistants

Each assistant needs a supported connection and authentication route; MCP support alone does not confirm compatibility with every Grunt operation.

> **INPUT NEEDED - G09:** Other supported clients/plans and their connection instructions, or confirmation that none are included in this evaluation.

### Collaboration and handover

Assets created through your sign-in are associated with your Grunt account. Sharing a link does not transfer the asset to another account. The IT and security overview explains access and offboarding considerations.

> **INPUT NEEDED - G10:** How colleagues find and edit shared work, supported account-transfer procedures, and how the organization retains access when a user leaves.

### Troubleshooting

| Symptom | First check |
| --- | --- |
| Cannot add the connection | Supported client and administrator connector policy. |
| Sign-in fails or expires | Grunt access and permissions; reconnect and complete authorization. |
| Asset is missing | The account used to create it and the account currently signed in. |
| A tool fails | Refresh the tool list and check the current tool name and input requirements. |
| A revision does not reach PowerPoint | The import, replacement or refresh procedure for this placement. |

Contact [Customer Success](mailto:cs@grunt.pro) for access and onboarding, or [Grunt support](mailto:support@grunt.pro) for technical help. Include the attempted action, client/add-in version, approximate UTC time and any reference ID. For MCP errors, include the endpoint and tool name. Do not include tokens or credentials.

References: [MCP troubleshooting](https://docs.grunt.io/mcp-server/connect-and-authenticate#troubleshooting) - [HTML and connected outputs](https://docs.grunt.io/grunt-one/connected-workflows)
