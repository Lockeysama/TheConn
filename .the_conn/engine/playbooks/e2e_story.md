# Playbook: E2E Testing Story (端到端测试)

## ⚠️ 核心公约加载 (Core Constitution)
**必须遵守**: `@engine/kernel/core.md`

## 🎭 技能装配 (Skill Assembly)

### 1. 核心角色 (Personas)
- **Primary**: QA Auditor (`@engine/personas/qa_auditor.md`)
- **Secondary**: Product Manager (User Journey Owner)

### 2. 动态注入 (Dynamic Injection)
```xml
<dynamic_injection>
    <inject ref="tech/testing" reason="E2E Planning" stage="Step 2" />
</dynamic_injection>
```

---

## 🧭 执行追踪 (Execution Trace)

```xml
<execution_trace>
    <step id="1" status="pending">Journey Selection (旅程选择)</step>
    <step id="2" status="pending">Scenario Design (场景设计)</step>
    <step id="3" status="pending">Script Generation (脚本生成)</step>
</execution_trace>
```

---

## 🛠️ 测试流程 (Testing Process)

### Step 1: 关键旅程选择 (Critical User Journey)
- 从 `runtime/data/epics/` 中提取高优先级的 User Stories。
- 组合成完整的用户操作流 (e.g., Login -> Search -> Buy -> Pay)。

### Step 2: 场景设计 (Scenario Design)
- **Happy Path**: 用户顺利完成操作。
- **Rainy Path**: 网络超时、支付失败、库存不足。

### Step 3: Cypress/Playwright 脚本生成
- 生成伪代码或实际测试脚本框架。

**Template (Cypress-like)**:
```javascript
describe('User Journey: Purchase Flow', () => {
  it('should complete purchase successfully', () => {
    // 1. Login
    cy.login(user);
    // 2. Add to Cart
    cy.get('.product').click();
    // 3. Checkout
    cy.get('.checkout').click();
    // 4. Verification
    cy.contains('Order Success');
  });
});
```

---

## ✅ 验收标准 (DoD)
- [ ] 测试用例覆盖了 Happy Path 和至少一个 Rainy Path。
- [ ] 测试脚本具有独立性 (不依赖上次运行状态)。
