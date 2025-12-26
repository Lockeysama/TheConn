# Phase: Delivery (执行与交付)

## ⚠️ 核心公约加载
**必须遵守**: `@engine/kernel/core.md`

## 🎯 阶段目标
- **Input**: 任务清单 (`task.md`).
- **Output**: 代码变更, 测试报告, 变更摘要.

## 🎭 技能装配
- **Primary**: Tech Architect & QA Auditor

```xml
<dynamic_injection>
    <inject ref="tech/testing" reason="E2E Verification" stage="Verification" />
    <inject ref="tech/code_review" reason="Self Check" stage="Review" />
</dynamic_injection>
```

## 🪜 执行步骤

### Step 1: 编码与测试 (Implementation)
- 遵循 Red-Green-Refactor 循环。
- 从 `task.md` 中逐项执行。

### Step 2: 端到端验证 (E2E Verification)
- 运行 `e2e_story` 逻辑。
- 验证关键用户旅程 (Critical User Journey)。

### Step 3: 交付总结 (Change Summary)
- 运行 `change_summary` 逻辑。
- 生成 Release Notes 或 PR Description。

## ✅ 阶段验收
- [ ] 所有测试通过？
- [ ] 没有引入新的 Lint 错误？
- [ ] 变更摘要是否准确？
