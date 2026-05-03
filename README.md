# EHS Knowledge Agent Demo

> An AI agent demo for EHS knowledge management, built with OpenClaw, Dify, RAG Knowledge Base, and Feishu Bot integration.

## 项目简介

本项目是一个面向企业 EHS 安全管理场景的 AI Agent Demo 展示仓库，用于说明大语言模型、RAG Knowledge Base、Agent workflow 和企业聊天入口在安全管理工作中的应用方式。

项目内容来自一组模拟 EHS 知识库材料，并整理为可公开展示的 GitHub repository。仓库不包含真实企业数据、真实账号、真实密钥、本地部署文件、数据库或 Docker volumes。

## Demo 场景

这个 Demo 关注以下典型 EHS 工作：

- EHS 知识问答
- 有限空间、动火、高处作业等高风险作业的安全准备
- 作业前安全检查清单生成
- 现场隐患识别与整改建议
- PPE 佩戴与个人防护要求查询
- Feishu Bot 企业聊天入口集成
- 基于知识库的 RAG 回答

## 两条实现路径

### OpenClaw Demo

OpenClaw 用于展示偏工程化的 Agent workspace 实现路径。Demo 通过 Agent prompt、知识库材料、回答格式约束和 Feishu Bot 接入，模拟一个企业内部 EHS 知识助手。

### Dify Demo

Dify 用于展示低代码 Agent / Workflow / Knowledge Base 的实现路径。它适合快速搭建知识库问答、流程编排、API 调用和 Web 嵌入能力，也便于与 OpenClaw 路线做方案比较。

## 仓库内容

```text
ehs-knowledge-agent-demo/
├── README.md
├── docs/
├── screenshots/
├── prompts/
├── sample_knowledge_base/
├── examples/
├── config_examples/
├── scripts/
├── safety-notes.md
├── .gitignore
└── LICENSE
```

## 快速查看

- [项目概览](docs/01_project_overview.md)
- [架构说明](docs/02_architecture.md)
- [OpenClaw Demo 说明](docs/03_openclaw_demo.md)
- [Dify Demo 说明](docs/04_dify_demo.md)
- [模拟知识库](sample_knowledge_base/)
- [示例问答](examples/example_answer_01.md)
- [敏感信息安全说明](safety-notes.md)

## 示例问题

```text
进入地下井进行有限空间检查作业前，需要做哪些准备？
```

Agent 应优先基于知识库回答，并输出结构化内容，例如作业许可、风险识别、通风与气体检测、PPE、监护人、应急准备、作业前检查清单和整改建议。

## 安全声明

本项目仅用于 AI Agent Demo 和技术展示。`sample_knowledge_base/` 中的内容均为模拟资料，不构成正式法律法规、企业制度或专业 EHS 审核意见。涉及高风险作业时，必须以所在国家/地区法律法规、企业正式制度和专业 EHS 人员现场审核为准。

## 敏感信息扫描

仓库内提供了一个只读扫描脚本：

```bash
python scripts/scan_sensitive_files.py
```

脚本会报告疑似真实密钥、占位符和技术说明词。占位符如 `YOUR_API_KEY_HERE` 可以保留；真实密钥、真实账号、真实 token、真实企业数据必须删除。

