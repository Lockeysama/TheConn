# Workflow: Feature Innovation (路线一：创新交付)

<meta>
    <type>Pipeline</type>
    <description>适用于不确定性较高的大型任务，涵盖从需求澄清到最终交付的全生命周期。</description>
</meta>

## 🔄 流程编排 (Orchestration)

### Phase 1: Inception (创意与定义)
- **File**: `inception.md`
- **Goal**: 明确需求价值与可行性，产出设计文档。
- **Skills**: `Communication` (澄清), `System Design` (方案), `Security Audit` (风控)。
- **Transition**:
    - IF `Approved` -> Goto **Phase 2**.
    - IF `Need More Info` -> Loop **Phase 1**.

### Phase 2: Planning (规划与拆解)
- **File**: `planning.md`
- **Goal**: 将需求转化为可执行的 Story 和 Task，并制定测试策略。
- **Skills**: `User Story` (拆分), `Critical Thinking` (检查), `Testing` (策略)。
- **Transition**: -> Goto **Phase 3**.

### Phase 3: Delivery (执行与交付)
- **File**: `delivery.md`
- **Goal**: 编码实现，执行测试，并生成变更摘要。
- **Skills**: `Code Review` (质量), `E2E Testing` (验证), `Summary` (文档)。
- **Transition**: -> **End Lifecycle**.

## 🛑 统一熔断机制 (Circuit Breaker)
- 任何阶段如果检测到 `Security Risk` 且无法缓解，必须立即通过 `notify_user` 暂停流程。
