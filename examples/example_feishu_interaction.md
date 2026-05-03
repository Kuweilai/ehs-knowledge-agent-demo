# Example Feishu Interaction

> This is a public-safe simulated interaction. It does not contain real Feishu credentials, real users, real chat logs, or enterprise data.

## User

```text
进入地下井进行有限空间检查作业前，需要做哪些准备？
```

## Feishu Bot

```text
根据模拟 EHS 知识库，地下井检查通常应按有限空间作业管理。

作业前请重点确认：
1. 是否完成现场审批或作业确认；
2. 是否识别缺氧、中毒、可燃气体、滑倒、坠落和被困风险；
3. 是否完成气体检测并确认结果可接受；
4. 是否具备通风、照明、通讯和撤离条件；
5. 是否设置外部监护人；
6. 是否准备合适 PPE 和应急联络方式。

如果气体环境不明、无监护、无应急准备或检测异常，不应进入。

安全提醒：该回答仅用于 Demo。实际有限空间作业必须按企业制度和专业 EHS 审核执行。
```

## Implementation Notes

- Real Feishu app credentials must stay outside this repository.
- Bot callbacks should verify request signatures in a private backend.
- Screenshots must be redacted before being added to `screenshots/`.

