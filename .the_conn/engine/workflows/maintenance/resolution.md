# Phase: Resolution (修复与验证)

## ⚠️ 核心公约加载
**必须遵守**: `@engine/kernel/core.md`

## 🎯 阶段目标
- **Input**: Triage 的结果 (方案)。
- **Output**: 修复后的代码和通过的测试。

## 🎭 技能装配
- **Primary**: QA Auditor & Tech Architect

```xml
<dynamic_injection>
    <inject ref="tech/testing" reason="Regression" stage="Verify" />
</dynamic_injection>
```

## 🪜 执行步骤

### Step 1: 快速修复 (Quick Fix)
- 应用代码变更。
- 优先保证 "最小改动原则" (Least Surprise).

### Step 2: 回归验证 (Regression)
- 运行相关单元测试。
- 验证 Bug 是否复现无效化。

## ✅ 阶段验收
- [ ] Bug 是否已修复？
- [ ] 是否引入了副作用？
