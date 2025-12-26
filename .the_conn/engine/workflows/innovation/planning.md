# Phase: Planning (规划与拆解)

## ⚠️ 核心公约加载
**必须遵守**: `@engine/kernel/core.md`

## 🎯 阶段目标
- **Input**: 批准的需求 (`requirements.md`).
- **Output**: 用户故事 (`stories/`) 和 任务清单 (`task.md`).

## 🎭 技能装配
- **Primary**: Product Manager & Tech Architect

```xml
<dynamic_injection>
    <inject ref="agile/user_story" reason="Story Generation" stage="Breakdown" />
    <inject ref="agile/acceptance" reason="AC Definition" stage="Detailing" />
    <inject ref="core/critical_thinking" reason="Plan Verification" stage="Check" />
</dynamic_injection>
```

## 🪜 执行步骤

### Step 1: 故事拆分 (Story Breakdown)
- 将大需求拆分为独立的 INVEST Stories。
- 如果是 "Pro Mode"，需关联架构决策 (ADR)。

### Step 2: 任务生成 (Task Generation)
- 对每个 Story 进行技术任务拆解 (1 Story -> N Tasks).
- 生成 `context.manifest.json` 锁定上下文。

### Step 3: 测试策略 (Test Planning)
- 定义验收标准 (AC)。
- 明确测试层级 (Unit vs Integration vs E2E)。

## ✅ 阶段验收
- [ ] Story 是否满足 INVEST 原则？
- [ ] 任务是否足够细粒度 (1-4小时)？
- [ ] 每个任务是否有明确的验收标准？
