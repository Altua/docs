# Grunt ONE
## Solution overview

**Review draft - 21 October 2026**

Grunt ONE brings AI-assisted creation, visual editing and reuse of charts and tables into one workflow across PowerPoint and web reports. Start with a question and your data, refine the result, and use it in the format your audience needs.

A saved Grunt asset contains the chart or table's data, formatting and versions. Keeping that work behind the visual makes it possible to revise and reuse the analysis as it moves between tools.

### From a question to a presentation or report

<!-- graphic:workflow -->

For a monthly performance review, an analyst can ask an assistant to create a revenue waterfall, adjust its labels and colors in the Web Editor, and use the result in a presentation or web report. The same approach supports financial analysis and consulting reports where a visual needs both analytical review and precise editing.

Grunt ONE is being delivered in stages. The following pages explain the tools, the proposed evaluation scope and the roadmap.

Further reading: [Grunt ONE](https://docs.grunt.io/grunt-one/index) - [Connected workflows](https://docs.grunt.io/grunt-one/connected-workflows)

<!-- pagebreak -->

## Tools and ways to work

| Tool or connection | What you use it for |
| --- | --- |
| **Grunt in an external assistant** | Ask a compatible assistant, such as a supported Claude client, to create, inspect and revise Grunt charts and tables. |
| **Web Editor** | Open a Grunt asset in your browser to edit its data and appearance, then save a version. |
| **Grunt in PowerPoint** | Use Grunt assets in presentations. Supported placements can be imported as editable Grunt objects with a compatible add-in. |
| **HTML reports** | Combine written analysis and Grunt visuals in a browser-readable report using an assistant and the HTML workflow. |
| **Asset services** | Store Grunt assets and saved versions for continued editing and reuse. Access depends on the account that created the asset and its sharing permissions. |

**MCP (Model Context Protocol)** is the connection that lets an assistant use Grunt's tools. It is one part of Grunt ONE, alongside storage, editing and output workflows.

### Grunt AI, Claude and PowerPoint

**Grunt AI in PowerPoint** is Grunt's own AI experience, with Grunt-managed AI processing. **Claude using Grunt through MCP** starts in an external assistant, with that provider's account and processing terms. Access and subscriptions for each route are listed in the evaluation scope below.

**Live control of an open PowerPoint presentation** is a separate capability in development. Connecting Claude to Grunt's MCP server does not, by itself, give Claude control of your open presentation.

### Evaluation scope

| Item | Configuration to confirm |
| --- | --- |
| Included tools and access | **G01:** Grunt products, seats, activation steps and included AI allowance. |
| Customer-supplied applications | **G01/G02:** Supported assistant and plan, Microsoft/PowerPoint requirements, and separate subscription or model-provider charges. |
| Hosting and data processing | **G11:** Hosting arrangement, operators, processing locations and applicable AI providers. |
| Enabled capabilities | **G13:** Released or limited-access features, supported objects and release/build. |

> **INPUT NEEDED - G01/G02/G11/G13:** The evaluation configuration above is not yet specified. These fields identify what the customer receives and what the customer needs to supply.

<!-- pagebreak -->

## Availability and roadmap

**Status reviewed: 21 October 2026.** Availability for the proposed evaluation remains to be confirmed where indicated.

| Capability | Current position |
| --- | --- |
| MCP chart and table tools | Connection procedures are published; enabled tools depend on endpoint and access. Evaluation availability: **G13**. |
| Web editing and saved versions | Evaluation editor configuration and availability: **G13**. |
| PowerPoint placement and import | Supported objects, add-in build and evaluation availability: **G02/G06/G13**. |
| HTML authoring and delivery | Included authoring and delivery workflow: **G08/G13**. Interactive refresh and offline saving remain in development. |
| Multidirectional synchronization | Planned; **not included in the first release wave**. Timing and update controls: **G13**. |
| Live control of an open PowerPoint presentation | In development. Supported client and release timing: **G13**. |
| Customer-hosted services | Localhost pilot documented; production deployment remains in development. Offered pilot scope: **G13**. |

The synchronization roadmap connects changes made in supported editing tools and outputs. Its update directions, automatic versus explicit behavior, conflict handling and version controls still need confirmation. A saved version or local PowerPoint import does not by itself create ongoing synchronization.

> **INPUT NEEDED - G13:** Released and limited-access capabilities, eligible customers, supported release/build, and the scope of later waves. Synchronization behavior and dates remain to be confirmed.

### Getting started with Grunt ONE

Grunt ONE access is arranged through Sales or Customer Success. Platform access, user entitlements and external assistant subscriptions are separate considerations.

**IT and security overview** explains data flows, hosting, account access and sharing. **Getting started** follows a first task from Claude through browser editing to PowerPoint. **Organization integration guide** is optional, for developers building a backend service; it is not required for ordinary user sign-in.

Further reading: [Rollout status](https://docs.grunt.io/grunt-one/index#rollout-status) - [Hosting and access](https://docs.grunt.io/grunt-one/hosting-and-access)
