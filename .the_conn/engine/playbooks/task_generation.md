# Playbook: Task Generation (任务生成)

## ⚠️ 核心公约加载 (Core Constitution)
**必须遵守**: `@engine/kernel/core.md`

## 🎭 技能装配 (Skill Assembly)

### 1. 核心角色 (Personas)
- **Primary**: Tech Architect (`@engine/personas/tech_arch.md`)
- **Secondary**: QA Auditor (`@engine/personas/qa_auditor.md`)

### 2. 动态注入 (Dynamic Injection)
```xml
<dynamic_injection>
    <inject ref="core/triage" reason="Context Analysis" stage="Step 1" />
    <inject ref="tech/testing" reason="Test Strategy" stage="Step 3" />
</dynamic_injection>
```

---

## 🧭 执行追踪 (Execution Trace)

**必须维护**:
```xml
<execution_trace>
    <step id="1" status="pending">Context Analysis (上下文分析)</step>
    <step id="2" status="pending">Manifest Generation (清单生成)</step>
    <step id="3" status="pending">Task Creation (任务创建)</step>
</execution_trace>
```

---

## 🛠️ 生成流程 (Generation Process)

### Step 1: 上下文分析 (Context Analysis)
- **Input**: `runtime/data/stories/...` + Session Profile
- **Action**:
    1.  **关键词提取**: 使用 Tech Architect 思维提取。
    2.  **Context 匹配**: 匹配 `runtime/context/` 下的相关设计文档。
    3.  **熔断检查 (Circuit Breaker)**: 检查 Migration (DB 变更), Config (环境变量)。

### Step 2: 上下文清单生成 (Manifest)
- **Target**: `context.manifest.json`
- **Purpose**: 为 Runtime 锁定上下文快照。

### Step 3: 任务文件生成 (Task Creation)
- **Target**: `task.md`
- **Focus**:
    - **验收标准**: 直接引用 Story 的验收标准。
    - **测试策略**: QA Auditor 定义 (TDD / BDD)。
    - **迭代流程**: 必须包含 "Red-Green-Refactor" 循环说明。

---

## 📝 输出规范 (Workspace Data)

### 1. context.manifest.json
**Path**: `.the_conn/runtime/workspace/EPIC-XX/TASK-XX.../context.manifest.json`

```json
{
  "task_id": "TASK-01",
  "story_id": "STORY-01",
  "contexts": [
    ".the_conn/runtime/context/global/Architecture.md",
    ".the_conn/runtime/context/epics/EPIC-01/Design.md"
  ],
  "source_story": ".the_conn/runtime/data/epics/.../STORY-01.md"
}
```

### 2. task.md
**Path**: `.the_conn/runtime/workspace/EPIC-XX/TASK-XX.../task.md`

---

## ✅ 生成后检查 (Self-Correction)

- [ ] **Tech Arch**: 任务粒度是否合适？(1 Story = 1-3 Tasks)
- [ ] **QA Auditor**: 测试策略是否覆盖了所有验收标准？
- [ ] **System**: 文件路径是否指向 `runtime/` 目录？
