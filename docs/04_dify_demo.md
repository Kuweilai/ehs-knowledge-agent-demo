# Dify Demo

## Demo 角色

Dify Demo 用于展示低代码方式构建 EHS Agent 的可能性。它适合快速搭建 Knowledge Base、Agent、Workflow、API 调用和 Web 嵌入能力。

## Knowledge Base Setup

在 Dify 中，可以将模拟 EHS 文档导入知识库，并让 Agent 根据检索结果回答问题。知识库应使用公开安全的模拟材料，不应导入真实企业制度、事故报告、客户资料或内部聊天记录。

## Workflow / Agent 思路

一种可行流程是：

```text
User Question
  -> Query Classification
  -> Knowledge Retrieval
  -> Risk Analysis
  -> Structured Answer
  -> Safety Disclaimer
```

对于复杂问题，可以把“风险识别”“检查清单”“整改建议”拆成不同节点，再合并为最终答案。

## Web / API Integration

Dify 可以通过 Web App、API 或嵌入页面提供访问入口。若接入企业 IM，所有 API keys、endpoint、webhook 和回调地址都必须保存在私有配置中，不能上传到公开仓库。

## 与 OpenClaw 的差异

- Dify 更适合快速搭建和低代码编排
- OpenClaw 更适合探索 Agent workspace、Skills 和工程化集成
- Dify 的可视化工作流便于演示
- OpenClaw 的配置方式更接近代码化 Agent 项目

## 不包含内容

本仓库不包含 Dify 官方源码、Docker Compose 真实部署目录、Postgres / Redis / Weaviate 数据、Dify storage 或管理员密码。

