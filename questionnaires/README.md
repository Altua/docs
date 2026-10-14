# Questionnaire answers

Use this folder to store reusable answers to customer questionnaires and vendor assessments. Keep general product guidance in the IT FAQ and formal policies in `policies/`.

These are standalone Markdown records. They are not part of the Mintlify navigation. Repository permissions determine who can access them.

## Available responses

| Questionnaire | Status | Scope |
| --- | --- | --- |
| [Grunt control self-assessment](grunt-control-self-assessment.md) | Draft; Grunt confirmations complete, Azure findings recorded | Turner & Townsend; PowerPoint add-in; all four supplied CSA PDFs |
| [Customer reply](grunt-control-self-assessment-response.md) | Prepared October 14, 2026; questions and answers only | Turner & Townsend; PowerPoint add-in |
| [AI control self-assessment](ai-control-self-assessment.md) | Draft; AI confirmations recorded | PowerPoint add-in AI capabilities |

## Add or update answers

For similar questionnaires, start with `grunt-control-self-assessment-response.md`. It contains the wording you can copy into a reply. Use `grunt-control-self-assessment.md` for supporting references and the dated Azure configuration findings. Recheck settings that can change, such as AI providers, backup retention, and WAF coverage, before reusing an answer.

1. Create a file with a descriptive name, such as `ai-control-self-assessment.md`. Reuse the file when another questionnaire asks equivalent questions.
2. Record the product scope, status, owner, and last review date. Use `Not assigned` or `Not reviewed` when needed.
3. Preserve the original question and any required answer choices. Keep the answer and comments separate so you can copy them into a customer form.
4. Link to supporting product documentation or policies. Mark missing evidence and incomplete answers explicitly.
5. Review the response for the customer's product scope before you send it. Record the reviewer and review date when you mark it reviewed.
6. Update related FAQ answers when a reviewed response changes a shared product fact.

Keep review notes outside the answer and comments. Distinguish Grunt's own capabilities from those of an external AI client that calls Grunt tools.

If you need a record of a submitted response, save a dated copy with its questionnaire version and product scope. Keep customer-specific or confidential material in a repository or system with suitable access controls.

## Export a reply

Update the recipient, date, scope, and relevant answers in the customer response. Keep confirmation history and internal evidence outside the reply.

Use the repository's Markdown export tool:

```bash
npm install
npm run md-to-pdf -- questionnaires/grunt-control-self-assessment-response.md
```

The command creates a PDF next to the Markdown source. Review the PDF before you send it. Generated questionnaire PDFs and files in `output/pdf/` are ignored by Git.

## Response format

```markdown
# Questionnaire title

**Status:** Draft
**Product scope:** Product and features covered
**Owner:** Not assigned
**Last reviewed:** Not reviewed
**Reviewed by:** Not reviewed
**Source:** Questionnaire name and version, or supplied questions

## 1. Topic

**Question:** Original question

**Answer:** Yes / No / Not applicable / To confirm

**Comments:**
Response you can copy into the questionnaire.

**References:**
- Link to supporting documentation or policy

**Review notes:** Missing information or scope limitations
```
