# Grunt ONE customer information package

Working drafts for review by Product, Engineering, Security, Sales and Customer Success. The documents explain Grunt ONE, its technical and security considerations, and how customers get started. They sit between a sales presentation and implementation documentation.

This import preserves the current Markdown and PDFs without editorial changes. The four guide drafts are dated 21 October 2026; the full checklist PDF was prepared on 22 October. Unresolved facts are marked **INPUT NEEDED** and mapped to G01-G14.

## Read and review

| Document | Intended reader | Editable source | PDF snapshot |
| --- | --- | --- | --- |
| Solution overview | Business sponsor and evaluator | [Markdown](drafts/grunt-one-solution-overview.md) | [PDF](output/pdf/grunt-one-solution-overview.pdf) |
| IT and security overview | IT architect and security reviewer | [Markdown](drafts/grunt-one-it-security-overview.md) | [PDF](output/pdf/grunt-one-it-security-overview.pdf) |
| Getting started | First user and onboarding administrator | [Markdown](drafts/grunt-one-getting-started.md) | [PDF](output/pdf/grunt-one-getting-started.pdf) |
| Organization integration guide | Developer and integration administrator; optional | [Markdown](drafts/grunt-one-organization-integration.md) | [PDF](output/pdf/grunt-one-organization-integration.pdf) |
| Complete follow-up checklist | Reviewers and people supplying missing answers | [Markdown](drafts/grunt-one-missing-information.md) | [PDF](output/pdf/grunt-one-follow-up-checklist.pdf) |

The standard customer package is the first three guides. The organization integration guide is only for customers building backend integrations.

## How to collaborate

1. Start with the prioritized follow-up checklist. The G identifiers connect requested answers to the relevant guide fields.
2. Suggest wording changes in the Markdown or comment on the pull request. Markdown is the source of truth; PDFs are review snapshots.
3. For a factual answer, record its source or responsible owner, date, applicable release/environment and any remaining limitation. Update the corresponding guide and checklist together.
4. Leave unresolved facts visible. Documentation of a capability does not establish that a customer's configuration has been tested or that a roadmap feature is released.
5. Regenerate and visually check the PDFs after editing. Do not edit a PDF independently of its Markdown source.

Owner roles in the checklist are suggestions, not assignments. No product, security, commercial or publication approval is implied by this import.

## Website exclusion

The repository's `.mintignore` explicitly excludes `grunt-one/customer-information-package/`. This package is not added to `docs.json` or the website navigation. Review and publication are separate steps; publishing would require an explicit change to that exclusion and the relevant site content/configuration.

This is a **public GitHub repository**. The exclusion prevents website inclusion, not public access to GitHub files, commits or pull requests.

The existing Grunt ONE product documentation is being developed in [PR #15](https://github.com/Altua/docs/pull/15). This package does not replace or modify those pages.

## Diagrams and PDF generation

The guide Markdown retains custom `<!-- graphic:... -->` markers and explicit page breaks. GitHub's Markdown preview does not render these diagrams; the included PDFs do. Editable vector diagram definitions are in `scripts/customer_guide_graphics.py`.

The scripts are preserved from the working package. They currently require Python, ReportLab and Windows Arial fonts at `C:/Windows/Fonts/arial.ttf` and `arialbd.ttf`. Their draft dates are fixed to match the current snapshots; update dates deliberately when preparing a new revision. No automated publishing or PDF-generation workflow is introduced.

From this package directory, with those dependencies available:

```powershell
python scripts/build_package.py
```

This rebuilds all five PDFs from the local Markdown. Render and visually inspect every changed PDF page before committing updated snapshots. Generated Python caches are excluded from version control.

The Markdown checklist preserves references to the historical R01-R18 research register. That historical research is not part of this import; the complete G01-G14 follow-up requests are included here.
