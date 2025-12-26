# Phase: Triage (分析与分诊)

## ⚠️ 核心公约加载
**必须遵守**: `@engine/kernel/core.md`

## 🎯 阶段目标
- **Input**: 简单的 Bug 报告或优化请求。
- **Output**: 明确的分类 (Bug/Optimization) 和初步方案。

## 🎭 技能装配
- **Primary**: QA Auditor

```xml
<dynamic_injection>
    <inject ref="core/triage" reason="Classification" stage="Analyze" />
</dynamic_injection>
```

## 🪜 执行步骤

### Step 1: 变更分析 (Analysis)
- 使用关键词匹配 (crash, fix, typo vs optimize, add)。
- 确定是否可以进入 "Fast Track" (纯配置修改)。

### Step 2: 方案制定 (Solution)
- 如果是 Bug -> 执行 5-Why 根因分析。
- 如果是 Optimization -> 确认改动范围。

## ✅ 阶段验收
- [ ] 类别是否准确？
- [ ] 是否可以直接进入 Resolution 阶段？(如果甚至需要大量重构，应转入 Innovation 路线)。
