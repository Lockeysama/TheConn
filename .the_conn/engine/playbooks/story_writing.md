# Playbook: Story Writing (故事编写)

## ⚠️ 核心公约加载 (Core Constitution)
**必须遵守**: `@engine/kernel/core.md`

## 🎭 技能装配 (Skill Assembly)

### 1. 核心角色 (Personas)
- **Primary**: Product Manager (`@engine/personas/product_mgr.md`)

### 2. 动态注入 (Dynamic Injection)
```xml
<dynamic_injection>
    <!-- 注入 Story 编写这一核心技能 -->
    <inject ref="agile/user_story" reason="Core Task" stage="Step 3" />
    
    <!-- 注入验收标准编写技能 -->
    <inject ref="agile/acceptance" reason="Quality Assurance" stage="Step 3" />
    
    <!-- 注入批判性思维用于风险检查 -->
    <inject ref="core/critical_thinking" reason="Self-Correction" stage="Step 4" />
</dynamic_injection>
```

---

## 🧭 生成流程 (Authentication Process)

### Step 1: 模式判定 (Mode Selection)
- **Input**: Session Profile + Demand (需求)
- **Output**: `Mode` ("Standard" | "Pro")

### Step 2: 需求信息提取 (Extraction)
- **Focus**: User (用户), Action (动作), Benefit (收益), Constraints (约束)。

### Step 3: Story 生成 (Generation)
- **Call Skill**: `agile/user_story.WriteStory(Requirements, Mode)`
- **Constraint**: 必须引用 **Domain Rules** (例如: 特定框架模式)。
- **Pro Mode**: 必须链接到 `related_adr` (相关架构决策)。

### Step 4: 交叉检查 (Cross-Check)
- **Call Skill**: `core/critical_thinking.Think(Story, "Devil's Advocate", DomainStrategy)`
- **Check**: "INVEST 验证", "可测试性检查 (Testability)"。

---

## 📝 输出规范 (Runtime Data)

### 文件路径 (File Paths)
- **Target**: `.the_conn/runtime/data/epics/EPIC-XX.../stories/STORY-XX.md`
- **Reference**: `.the_conn/runtime/context/...`

### Frontmatter (YAML)
**Pro Mode 必须包含**:
```yaml
related_adr: [...]      # 关联架构决策
domain_event: "Name"    # 领域事件
aggregate: "Name"       # 聚合根
```

### 内容结构 (Content Structure)
1.  **目标 (Goal)**: 用户价值 (PM Persona)
2.  **验收标准 (AC)**: BDD / 清单 (QA Persona)
3.  **实现指导 (Implementation Guide)**:
    - **Stack Specifics**: 引用加载的 Domain Rules (e.g., React Hooks, Go Gin)
    - **Complexity**: 引用加载的 Complexity Rules
    - **Impact Analysis**: 引用 Project Context

---

## ✅ 生成后检查 (Self-Correction)

在生成文档前，必须对照 **Loaded Personas** 进行自检：
- [ ] **PM 视角**: 价值是否明确？
- [ ] **QA 视角**: 验收标准是否可测？
- [ ] **Arch 视角**: 是否符合 Domain Rules 中的架构约束？
