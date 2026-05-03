# OpenClaw Demo

## Demo 角色

OpenClaw Demo 用于展示偏工程化的 EHS Agent 构建方式。它强调通过 Agent workspace、Skills、Prompts 和知识库材料，把一个通用大语言模型约束成面向 EHS 场景的知识助手。

## 设计思路

OpenClaw Agent 可以接收用户问题，检索模拟 EHS 知识库，并按照预设回答格式输出安全建议。回答应优先引用知识库内容；当知识库没有明确答案时，应说明不确定性，而不是编造法规、标准或企业制度。

## Workspace 概念

在真实 Demo 中，OpenClaw 可能通过本地 workspace 管理 Agent 配置、Prompt、Skills 和知识库。公开仓库不包含真实 workspace 配置，只保留概念说明和脱敏示例。

## Knowledge Base Q&A

知识库材料可按 Markdown 文件组织，例如：

- `working_at_height_safety.md`
- `hot_work_safety.md`
- `confined_space_safety.md`
- `temporary_electrical_safety.md`
- `ppe_requirements.md`
- `hazard_rectification.md`
- `chemical_use_emergency_response.md`
- `new_employee_ehs_training.md`

Agent 回答时应优先使用这些材料，并在必要时提醒用户进行专业 EHS 审核。

## Feishu Channel Integration

OpenClaw Demo 可通过 Feishu Bot 接入企业聊天场景。公开仓库仅提供配置示例，真实 appId、appSecret、事件订阅地址、加密 key 和 webhook 必须保存在私有环境中。

## Prompt 与回答格式

推荐使用三类 Prompt：

- System Prompt：定义 Agent 身份、安全边界和知识库优先原则
- Answer Format Prompt：约束结构化回答格式
- Risk Analysis Prompt：用于隐患和作业场景的风险分析

## 不包含内容

本仓库不包含真实 OpenClaw 配置、真实模型密钥、真实飞书凭证、本地运行日志或 OpenClaw 官方源码。

