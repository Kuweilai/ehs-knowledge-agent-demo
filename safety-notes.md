# Safety Notes

## Public Repository Boundary

This repository is a sanitized showcase version of an EHS AI Agent demo. It is not a copy of a real OpenClaw, Dify, Feishu, Docker, or enterprise deployment environment.

Do not upload:

- `.env` or `.env.*`
- Real API keys, app secrets, passwords, tokens, access tokens, refresh tokens, or webhook URLs
- Real Feishu appId or appSecret
- Real OpenClaw or Dify local configuration
- Docker volumes, Postgres, Redis, Weaviate, SQLite, or other local databases
- Logs, real chat history, real incident records, real customer data, or real enterprise documents
- Screenshots that expose accounts, tokens, internal URLs, enterprise names, or sensitive operations

## Placeholder Policy

The following placeholder values are safe to keep in public examples:

- `YOUR_API_KEY_HERE`
- `YOUR_FEISHU_APP_ID`
- `YOUR_FEISHU_APP_SECRET`
- `YOUR_MODEL_ENDPOINT_HERE`
- `YOUR_DIFY_API_KEY`
- `YOUR_BOT_WEBHOOK_URL`
- `YOUR_WORKSPACE_ID`

If a value can be used to authenticate, identify a real enterprise system, or access private data, it must not be committed.

## EHS Content Disclaimer

The knowledge base content in this repository is demo / simulated data. It is intended to show how an AI Agent could structure safety answers. It does not replace laws, regulations, company procedures, site permits, risk assessments, or review by qualified EHS professionals.

For high-risk work such as confined space entry, hot work, work at height, temporary electrical work, or chemical handling, always follow the official requirements of the site and obtain professional review before work begins.

