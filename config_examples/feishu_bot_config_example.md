# Feishu Bot Config Example

This is a sanitized example. Never commit real Feishu credentials.

## Placeholder Values

```text
FEISHU_APP_ID=YOUR_FEISHU_APP_ID
FEISHU_APP_SECRET=YOUR_FEISHU_APP_SECRET
FEISHU_BOT_WEBHOOK_URL=YOUR_BOT_WEBHOOK_URL
FEISHU_VERIFICATION_TOKEN=YOUR_FEISHU_VERIFICATION_TOKEN
FEISHU_ENCRYPT_KEY=YOUR_FEISHU_ENCRYPT_KEY
```

## Integration Flow

```text
Feishu User Message
  -> Feishu Bot Callback
  -> Private Backend
  -> OpenClaw or Dify Agent
  -> EHS Knowledge Base Retrieval
  -> Structured Answer
  -> Feishu Bot Reply
```

## Security Requirements

- Keep app secrets in private environment variables.
- Verify Feishu callback signatures in the backend.
- Do not log raw user messages if they may contain enterprise data.
- Do not upload bot logs, callback payloads, or screenshots with real accounts.

