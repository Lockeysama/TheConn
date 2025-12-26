# Playbook: Change Summary (变更摘要)

## ⚠️ 核心公约加载 (Core Constitution)
**必须遵守**: `@engine/kernel/core.md`

## 🎭 技能装配 (Skill Assembly)

### 1. 核心角色 (Personas)
- **Primary**: Tech Architect (`@engine/personas/tech_arch.md`)

### 2. 动态注入 (Dynamic Injection)
```xml
<dynamic_injection>
    <!-- 注入代码审查技能用于分析变更 -->
    <inject ref="tech/code_review" reason="Diff Analysis" stage="Step 1" />
</dynamic_injection>
```

---

## 🧭 执行追踪 (Execution Trace)

```xml
<execution_trace>
    <step id="1" status="pending">Diff Analysis (变更分析)</step>
    <step id="2" status="pending">Impact Assessment (影响评估)</step>
    <step id="3" status="pending">Summary Generation (摘要生成)</step>
</execution_trace>
```

---

## 🛠️ 生成流程 (Generation Process)

### Step 1: 变更分析 (Diff Analysis)
- **Input**: `git diff` or Staged files.
- **Action**: 识别修改了哪些模块 (Frontend, Backend, Config)。

### Step 2: 影响评估 (Impact Assessment)
- **Check**:
    - 是否修改了 API 契约？(Breaking Change?)
    - 是否引入了新的依赖？(Supply Chain Risk?)
    - 是否触及核心领域逻辑？(Risk Level)

### Step 3: 摘要生成 (Summary Generation)
生成 `PR_DESCRIPTION.md` 或 Commit Message。

**Template**:
```markdown
## 📝 变更摘要
- [Feat/Fix/Chore]: 简要描述 (One-liner)

## 🔍 技术细节
- Modulo A: ...
- Module B: ...

## ⚠️ 风险与注意事项
- Breaking Change: No/Yes
- Migration: No/Yes
```

---

## ✅ 自检 (Self-Check)
- [ ] 摘要是否准确反映了 diff 内容？
- [ ] 是否遗漏了隐蔽的配置变更？
