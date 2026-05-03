# Architecture

## Conceptual Flow

```text
User Question
    |
    v
Feishu Bot / Web Chat
    |
    v
OpenClaw Agent or Dify Agent
    |
    v
RAG Knowledge Base
    |
    v
LLM Reasoning
    |
    v
Structured EHS Answer
```

## 模块说明

### User Question

用户可以提出自然语言问题，例如“进入地下井进行有限空间检查作业前，需要做哪些准备？”

### Feishu Bot / Web Chat

企业聊天入口用于降低使用门槛，让员工可以在熟悉的协作工具中提问。公开仓库只保留配置说明，不包含真实 appId、appSecret 或 webhook。

### OpenClaw Agent or Dify Agent

OpenClaw 和 Dify 是两条不同实现路径：

- OpenClaw 更偏 Agent workspace、Skills、Prompt 和工程化集成
- Dify 更偏低代码 Knowledge Base、Workflow、API 和 Web 嵌入

### RAG Knowledge Base

知识库由模拟 EHS Markdown 文件组成，覆盖高处作业、动火作业、有限空间、临时用电、PPE、隐患整改、化学品和新员工培训。

### LLM Reasoning

模型负责理解问题、检索上下文、组织答案和补充必要的安全提醒。Prompt 会约束模型不要编造法律法规、标准编号或企业制度。

### Structured EHS Answer

最终答案应包含风险、准备事项、检查清单、整改建议和免责声明，便于现场人员理解和复核。

## 数据安全边界

公开仓库不保存真实工厂数据、真实用户聊天记录、真实企业制度、真实配置文件或任何密钥。所有配置示例都必须使用占位符。

