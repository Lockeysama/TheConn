# Workflow: Maintenance & Fix (路线二：快速修复)

<meta>
    <type>Pipeline</type>
    <description>适用于确定性较高的小型任务，如 Bug 修复、配置调整或微小特性。</description>
</meta>

## 🔄 流程编排 (Orchestration)

### Phase 1: Triage (分析与分诊)
- **File**: `triage.md`
- **Goal**: 识别变更类型 (Bug/Hotfix)，定位根因，并生成解决方案。
- **Skills**: `Triage` (分类), `Critical Thinking` (5-Why), `Communication` (确认)。
- **Transition**:
    - IF `Solution Found` -> Goto **Phase 2**.
    - IF `Complex Feature` -> Route to `innovation/workflow.md`.

### Phase 2: Resolution (修复与验证)
- **File**: `resolution.md`
- **Goal**: 应用修复，执行回归测试，确保无副作用。
- **Skills**: `Code Review` (审查), `Testing` (回归).
- **Transition**: -> **End Lifecycle**.

## ⚡️ 快速通道 (Fast Track)
- 对于 `Hotfix` 类型的变更，如果 `Impact Analysis` 显示仅影响非核心路径，可跳过部分可测试性检查。
