# Playbook: Quick Fix (快速修复)

## ⚠️ 核心公约加载 (Core Constitution)
**必须遵守**: `@engine/kernel/core.md`

## 🎭 技能装配 (Skill Assembly)

### 1. 核心角色 (Personas)
- **Primary**: QA Auditor (`@engine/personas/qa_auditor.md`)
- **Secondary**: Tech Architect (`@engine/personas/tech_arch.md`)

### 2. 动态注入 (Dynamic Injection)
```xml
<dynamic_injection>
    <inject ref="core/triage" reason="Classification" stage="Step 1" />
    <inject ref="tech/testing" reason="Regression" stage="Step 4" />
</dynamic_injection>
```

---

## 🧭 执行追踪 (Execution Trace)

```xml
<execution_trace>
    <step id="1" status="pending">Context Analysis (变更分析)</step>
    <step id="2" status="pending">Classification (类型判定)</step>
    <step id="3" status="pending">Story Generation (生成故事)</step>
</execution_trace>
```

---

## 🧪 变更分析与类型判定

**判定逻辑** (QA Auditor 思维):

| 类型 | 关键词特征 | 判定标准 | 处理策略 |
| :--- | :--- | :--- | :--- |
| **Bug Fix** | 崩溃, 失败, error, exception, 慢 | 违反现有验收标准 / 功能异常 | 5-Why 根因分析 -> 修复 -> 回归测试 |
| **Hotfix** | 优化, 增加, 调整, log, config | 功能正常但需改进 / 新增非功能需求 | 方案设计 -> 实现 -> 验证 |

**归属推断**:
- 尝试关联父 Story (`STORY-XX`).
- 尝试关联 Epic/Feature.
- 生成子 ID: `STORY-XX.Y`.

---

## 📝 输出规范 (Runtime Data)

### Story 文件生成
**Path**: `.the_conn/runtime/data/stories/STORY-XX.Y.md`

#### Bug Fix Template
```markdown
# Bug Fix: {Title}
## 1. 问题描述 (Problem)
- 现象: ...
- 期望: ...
## 2. 根因分析 (RCA - 5 Whys)
- Why 1: ...
## 3. 修复方案 (Solution)
- 修改点: ...
## 4. 验收标准 (Acceptance Criteria)
- [ ] 复现步骤无效化 (Bug 已修复)
- [ ] 回归测试通过
```

#### Hotfix Template
```markdown
# Hotfix: {Title}
## 1. 改进目标 (Goal)
- ...
## 2. 实现方案 (Plan)
- ...
## 3. 验收标准 (AC)
- [ ] 新功能可用
- [ ] 无副作用
```

---

## 🚀 自动衔接 (Auto-Transition)

Quick Fix 可以在生成 Story 后自动进入执行阶段。

**AI 动作**:
1. 询问用户: "Story 已生成 (STORY-XX.Y)。是否立即生成执行任务 (task_generation)？"
2. 用户确认 -> 调用 `@engine/playbooks/task_generation.md`.
