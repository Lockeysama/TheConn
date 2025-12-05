# Feature 规划生成指南

根据需求文档或 Epic 生成 Feature 规划文件（`epics/{EPIC-ID}/features/{FEAT-ID}/README.md`）。

## 输出格式

```markdown
# Feature: {FEAT-ID} {Feature 名称}

- **目标**: {一句话说明功能目标}
- **包含的故事**: {Story ID 列表}
- **验收标准**:
  - {端到端验收项1}
  - {端到端验收项2}
```

## 生成原则

1. 目标从用户视角描述
2. Story 拆分粒度适中（1-3天可完成）
3. 验收标准是端到端的用户流程

现在，请根据用户提供的材料生成 Feature 规划。
