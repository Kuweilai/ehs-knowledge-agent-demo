# Dify Workflow Notes

This file describes a public-safe Dify workflow design. It does not contain Dify source code, Docker volumes, database files, admin credentials, or real API keys.

## Suggested Workflow

```text
User Question
  -> Scenario Classification
  -> Knowledge Retrieval
  -> Risk Analysis
  -> Checklist Generation
  -> Safety Disclaimer
  -> Final Answer
```

## Knowledge Base

Upload only sanitized demo Markdown files from `sample_knowledge_base/`.

Do not upload:

- Real company EHS manuals
- Real incident records
- Real inspection reports
- Customer or employee data
- Screenshots containing accounts or keys

## Environment Variables

Use private environment variables or Dify secret management for values such as:

```text
DIFY_API_KEY=YOUR_DIFY_API_KEY
MODEL_ENDPOINT=YOUR_MODEL_ENDPOINT_HERE
MODEL_API_KEY=YOUR_API_KEY_HERE
```

## Output Rules

The Dify answer node should:

- Prioritize retrieved knowledge base content
- Avoid hallucinating laws or standard numbers
- Generate structured Chinese answers
- Include a high-risk work disclaimer

