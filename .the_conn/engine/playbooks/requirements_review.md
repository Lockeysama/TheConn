# Playbook: Requirements & Technical Review (需求与技术评审)

## ⚠️ 核心公约加载
**必须遵守**: `@engine/kernel/core.md`

## 🎭 技能装配 (Skill Assembly)

### 1. 核心角色 (Personas)
- **Primary**: Tech Architect (`@engine/personas/tech_arch.md`)
- **Secondary**: Product Manager (`@engine/personas/product_mgr.md`)

### 2. 动态注入 (Dynamic Injection)
```xml
<dynamic_injection>
    <!-- 需求澄清阶段注入沟通技能 -->
    <inject ref="core/communication" reason="Requirement Clarification" stage="Step 2" />
    
    <!-- 设计阶段注入系统设计技能 -->
    <inject ref="tech/system_design" reason="Architecture Design" stage="Step 4" />
    
    <!-- 全程注入批判性思维 -->
    <inject ref="core/critical_thinking" reason="Risk Analysis" stage="Always" />
</dynamic_injection>
```

---

## 🧭 评审流程 (Review Process)

### Step 1: 初步分析 (Analysis)
- **Action**: Tech Architect 使用 `core/triage` 技能快速分析输入。
- **Output**: 关键词与初始上下文。

### Step 2: 需求澄清 (Clarification)
- **Call Skill**: `core/communication.Clarify(Requirements)`
- **Focus**: "5个关键问题" (Value, User, Success Criteria, Constraints, Legacy)。

### Step 3: 模式判定 (Mode Selection)
根据 **Session Profile** 和 **Domain Constraints** 判定：
- **Standard**: CRUD, 单服务 -> 直达技术选型。
- **Pro**: 跨服务, 核心域 -> 完整 DDD 流程。

### Step 4: 架构设计 (Design)
- **Call Skill**: `tech/system_design.DesignSystem(Reqs, DomainStrategy)`
- **Pro Mode**: 执行领域驱动设计 (Domain Driven Design)。
- **All Modes**: 执行技术选型 (Stack Selection)。

### Step 5: 风险评估 (Risk Assessment)
- **Call Skill**: `core/critical_thinking.Think(Design, "Inversion", DomainStrategy)`
- **Check**: 单点故障 (SPOF)、过度设计 (YAGNI)、遗留兼容性。

---

## ✅ 输出规范 (Artifacts)
- **Target**: `runtime/workspace/design_docs/...`
- **Format**: Markdown with Mermaid diagrams.
