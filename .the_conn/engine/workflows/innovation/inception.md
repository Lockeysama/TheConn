# Phase: Inception (创意与定义)

## ⚠️ 核心公约加载
**必须遵守**: `@engine/kernel/core.md`

## 🎯 阶段目标
- **Input**: 原始用户输入或模糊需求。
- **Output**: 经过澄清和设计批准的 `requirements.md` (或 Session Context).

## 🎭 技能装配
- **Primary**: Product Manager & Tech Architect

```xml
<dynamic_injection>
    <inject ref="core/communication" reason="Clarify 5W" stage="Thinking" />
    <inject ref="tech/system_design" reason="Feasibility Check" stage="Design" />
    <inject ref="tech/security_audit" reason="Risk Assessment" stage="Review" />
</dynamic_injection>
```

## 🪜 执行步骤

### Step 1: 价值澄清 (Value Clarification)
- 调用 `Communication.Clarify(Input)`。
- 确保识别出 **Who**, **What**, **Why**。

### Step 2: 技术方案 (Technical Feasibility)
- 引用 `domain/rules` 进行初步设计。
- 识别关键技术难点和依赖。

### Step 3: 风险审查 (Risk Review)
- 运行 `Security Audit`。
- 如果存在 High Risk，必须在方案中明确缓解措施。

## ✅ 阶段验收
- [ ] 需求是否清晰且有价值？
- [ ] 技术方案是否可行？
- [ ] 安全风险是否已识别？
