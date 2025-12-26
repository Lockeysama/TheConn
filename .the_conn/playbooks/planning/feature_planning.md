# Feature 规划生成指南

根据需求文档或 Epic 生成 Feature 规划文件。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@rules/base_rules.md` 中定义的所有基础公约。**

**📋 规范引用**：

本 Playbook 依赖以下规范文件（AI 必须先加载）：
- **基础公约**: `@rules/base_rules.md` - 禁止事项、文件路径约定、质量标准
- **测试策略**: `@rules/test_strategy_rules.md` - Story 类型判断、测试决策规则
- **复杂度评估**: `@rules/complexity_rules.md` - 复杂度评分标准

## 本 Playbook 的工作范围

**专注于**：生成 Feature 规划文档（创建 Feature README.md 文件）

---

## 命名与格式规范

### ID 命名规则

- **格式**: `FEAT-{序号}`
- **序号**: Epic 内唯一，两位数字，从 01 开始
- **示例**: `FEAT-01`, `FEAT-02`, `FEAT-10`

### 目录命名规则

- **格式**: `FEAT-{序号}_{PascalCaseName}`
- **PascalCase**: 每个单词首字母大写，无分隔符
- **示例**: `FEAT-01_Init_Project`, `FEAT-02_Generate_Templates`

### 文件路径

```text
.the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{PascalCaseName}/README.md
```

**示例**: `.the_conn/epics/EPIC-01_Base_Init/features/FEAT-01_Init_Project/README.md`

### Frontmatter 规范

```yaml
---
id: FEAT-01
status: pending
created: yyyy-mm-dd
depends_on: []
---
```

**字段说明**：

- `status`: `pending` (未完成) 或 `done` (已完成)
- `created`: 格式 `yyyy-mm-dd`
- `depends_on`: 依赖的其他 Feature ID 列表，无依赖写 `[]`

---

## 输出格式

### Standard Mode 格式

```markdown
# Feature: FEAT-{序号} {Feature 名称}

- **所属 Epic**: EPIC-{序号}
- **目标**: {一句话说明功能目标}
- **包含的故事**: STORY-{序号}, STORY-{序号}, ...
- **验收标准**:
  - {端到端验收项1}
  - {端到端验收项2}
- **创建日期**: {yyyy-mm-dd}
```

### Pro Mode 格式⭐

```markdown
# Feature: FEAT-{序号} {Feature 名称}（聚合）

- **所属 Epic**: EPIC-{序号}
- **目标**: {一句话说明功能目标}
- **包含的故事**: STORY-{序号}, STORY-{序号}, ...
- **验收标准**:
  - {端到端验收项1}
  - {端到端验收项2}
- **创建日期**: {yyyy-mm-dd}

## 聚合设计

| 要素 | 内容 |
|------|------|
| **聚合根** | {名称，如 Order} |
| **实体** | {列举，如 OrderItem} |
| **值对象** | {列举，如 Address, Money} |
| **不变性规则** | {业务规则，如 "总价 = Σ(单价×数量) - 折扣"} |
| **事务边界** | {说明，如 "单个 Order + 关联的所有 OrderItem"} |

## 一致性边界

| 维度 | 策略 |
|------|------|
| **聚合内一致性** | 强一致（本地事务） |
| **聚合间一致性** | 最终一致（领域事件） |
| **跨上下文一致性** | 最终一致（Saga / 事件驱动） |
| **实现机制** | {说明，如 "数据库事务 + Kafka 事件"} |

**参考**: Review Phase 2.2 战术层讨论 / ADR-XXX

## 领域事件（如果有）

| 事件名称 | 触发时机 | 携带数据 | 订阅者 | 对应 Story |
|---------|---------|---------|--------|-----------|
| OrderCreated | 订单创建成功 | orderId, items, totalPrice | 库存、支付 | STORY-XX |
| OrderCancelled | 订单取消 | orderId, reason | 库存、支付 | STORY-YY |

```

---

## 生成原则

1. **目标描述**: 从用户/业务视角描述，说明"为什么"和"价值是什么"
2. **Story 拆分**: 按功能模块或职责边界拆分，每个 Story 有清晰的实现范围
3. **验收标准**: 端到端的用户流程，可实际验证
4. **命名规范**: Feature 名称使用 PascalCase
5. **粒度控制**: 优先按完整功能模块划分，每个 Feature 包含 2-5 个 Story 即可
6. **便于 AI 编码**: 确保每个 Story 的边界清晰，接口明确，依赖关系简单
7. **测试规划**: 根据 Feature 特征自动规划测试 Story

---

## 自动生成测试 Story (智能引导)

### 测试 Story 决策逻辑

```mermaid
graph TD
    A[开始判断] --> B{完整用户旅程?}
    B -->|是| C[✅ 必须 E2E]
    B -->|否| D{多模块/服务集成≥2个?}
    D -->|是| C
    D -->|否| E{核心业务流程?}
    E -->|是| F[💡 建议 E2E]
    E -->|否| G{功能Story数量≥3个?}
    G -->|是| F
    G -->|否| H[❌ 无需E2E<br/>单元测试足够]
```

**判断标准**:
- **完整用户旅程**: 用户从开始到结束的完整操作流程
- **多模块集成**: 涉及数据库、缓存、API、消息队列等多个系统
- **核心业务流程**: 直接影响业务目标的关键功能
- **Story 数量**: ≥3 个功能 Story 时建议增加集成验证

### 性能测试判断

```mermaid
graph TD
    A[开始判断] --> B{明确性能指标要求?}
    B -->|是| C[✅ 必须性能测试]
    B -->|否| D{高并发/大数据处理?}
    D -->|是| E[💡 建议性能测试]
    D -->|否| F{实时性要求?}
    F -->|是| E
    F -->|否| G[❌ 无需性能测试<br/>按需添加]
```

**性能测试 Story 特点**:
- ID: STORY-97（Feature 级） | Type: `perf_test`
- 验收标准: 性能指标（响应时间、吞吐量、并发等）
- 测试场景: 负载测试、压力测试、容量测试、峰值测试、稳定性测试
- 生成方式: 使用 `@playbooks/planning/performance_test_story.md`

### 生成的 Feature 文档中的测试输出格式

**规则**：
1. ✅ 只列出需要的测试 Story 及简要理由（1-2 句话）
2. ✅ 按功能开发顺序排列
3. ❌ 不包含详细的多维度评估过程
4. ❌ 不包含决策框架说明

**输出格式**：

```markdown
## 包含的 Story

### 功能开发 Story
- STORY-01: {功能1描述}
- STORY-02: {功能2描述}
- STORY-03: {功能3描述}

### 测试 Story（按开发顺序）

**STORY-99: E2E_{FeatureName}_Flow**
- **类型**: E2E 测试 (type: e2e_test)
- **目的**: 验证 STORY-01 → STORY-02 → STORY-03 的完整集成
- **理由**: Feature 包含 3 个功能 Story 且涉及数据库和 API 集成
- **测试路径**: `tests/bdd/features/{module}/{feature}_flow.feature`
- **执行顺序**: STORY-01, STORY-02, STORY-03 完成后

**STORY-97: Performance_{FeatureName}**（如果需要）
- **类型**: 性能测试 (type: perf_test)
- **目的**: 验证高并发场景下的性能表现
- **理由**: 涉及实时数据处理，需要验证性能指标
- **执行顺序**: STORY-99 完成后
```

### 测试 Story 命名规范

| Story 类型 | 命名格式                             | Story Type  | 示例                            |
| --- | --- | --- | --- |
| E2E 测试   | `STORY-99_E2E_{FeatureName}_Flow`    | `e2e_test`  | `STORY-99_E2E_Auth_Flow`        |
| 集成测试   | `STORY-98_Integration_{FeatureName}` | `e2e_test`  | `STORY-98_Integration_Payment`  |
| 性能测试   | `STORY-97_Performance_{FeatureName}` | `perf_test` | `STORY-97_Performance_DataSync` |

**编号约定**: 测试 Story 使用 97-99 编号，与功能 Story 区分

**Story type 字段**：

- E2E 测试 Story: `type: e2e_test`
- 性能测试 Story: `type: perf_test`
- 生成方式: 使用 `@playbooks/planning/e2e_story.md` 生成 E2E Story

### 决策示例

| 场景     | Feature  | Story数/平均复杂度 | 分析维度                | 决策                        |
| --- | --- | --- | --- | --- |
| 核心业务 | 用户认证 | 4个/5.0分          | ✅完整流程+高集成+高风险 | ✅必须STORY-99:E2E_Auth_Flow |
| 技术模块 | 配置管理 | 2个/2.3分          | ❌内部模块+低集成+低风险 | ❌无需E2E，单元测试足够      |

---

## Feature 复杂度评估

| 评分维度          | 计算公式                 | 说明                                                                       |
| --- | --- | --- |
| Story数量影响     | Story数量×0.5（上限3.0） | -                                                                          |
| 平均Story复杂度   | Σ(Story复杂度)/Story数量 | -                                                                          |
| 集成复杂度        | 低(1.0)/中(2.0)/高(3.0)  | 低:单一模块依赖少<br/>中:2-3个模块少量外部依赖<br/>高:≥4个模块多个外部依赖 |
| **Feature复杂度** | **三者之和**             | 1.0-4.0:低复杂度✅<br/>4.1-7.0:中等复杂度⚠️<br/>7.1-10.0+:高复杂度🔴          |

**评分示例**:

| Feature  | Story数 | 平均复杂度 | 集成复杂度 | 总分  | 等级 |
| --- | --- | --- | --- | --- | --- |
| 用户认证 | 4个→2.0 | 4.875      | 高(3.0)    | 9.875 | 🔴高  |
| 配置管理 | 2个→1.0 | 2.25       | 低(1.0)    | 4.25  | ⚠️中  |

---

## 示例

### 示例 1: Standard Mode - 不需要测试 Story 的 Feature

```markdown
# Feature: FEAT-01 初始化项目结构

- **所属 Epic**: EPIC-01
- **目标**: 提供 CLI 命令一键初始化 The Conn 项目结构
- **包含的故事**: STORY-01, STORY-02
- **验收标准**:
  - 用户执行 `theconn init` 后，所有必需目录和文件创建成功
  - 生成的模板文件内容完整且格式正确
  - 重复执行不会覆盖已有文件
- **创建日期**: 2025-12-11

## 包含的 Story

### 功能开发 Story
- STORY-01: 创建目录结构
- STORY-02: 生成模板文件

### 测试 Story
无需 Feature 级 E2E 测试（仅 2 个独立 Story，单元测试足够）
```

### 示例 2: Pro Mode - 需要测试 Story 的 Feature⭐

```markdown
# Feature: FEAT-01 Order 聚合（订单核心逻辑）

- **所属 Epic**: EPIC-02（订单上下文）
- **目标**: 实现订单聚合的核心业务逻辑，确保订单状态一致性
- **包含的故事**: STORY-01, STORY-02, STORY-03, STORY-04, STORY-99
- **验收标准**:
  - 订单创建后正确计算总价（含折扣）
  - 订单状态流转符合业务规则（待支付 → 已支付 → 已完成）
  - 订单取消时正确发布 OrderCancelled 事件
  - 所有业务规则的不变性得到保证
- **创建日期**: 2025-12-25

## 聚合设计

| 要素 | 内容 |
|------|------|
| **聚合根** | Order（订单） |
| **实体** | OrderItem（订单项） |
| **值对象** | Money（金额）, Address（地址）, Discount（折扣） |
| **不变性规则** | • 总价 = Σ(单价×数量) - 折扣<br>• 已支付订单不可修改<br>• 订单项数量必须 > 0 |
| **事务边界** | 单个 Order + 关联的所有 OrderItem（原子操作） |

## 一致性边界

| 维度 | 策略 |
|------|------|
| **聚合内一致性** | 强一致（数据库事务） |
| **聚合间一致性** | 最终一致（领域事件 OrderCreated） |
| **跨上下文一致性** | 最终一致（Saga，与支付/库存上下文） |
| **实现机制** | PostgreSQL 事务 + Kafka 事件发布 |

**参考**: Review Phase 2.2 聚合设计表 / ADR-003（最终一致性策略）

## 领域事件

| 事件名称 | 触发时机 | 携带数据 | 订阅者 | 对应 Story |
|---------|---------|---------|--------|-----------|
| OrderCreated | 订单创建成功 | orderId, items, totalPrice, userId | 库存上下文、支付上下文 | STORY-02 |
| OrderCancelled | 订单取消 | orderId, reason, cancelledAt | 库存上下文、支付上下文 | STORY-04 |

## 包含的 Story

### 功能开发 Story
- STORY-01: 实现 Order 聚合根逻辑（Domain Logic）
- STORY-02: 发布 OrderCreated 事件（Event Publisher）
- STORY-03: 实现 OrderRepository（持久化）
- STORY-04: 订单取消与补偿逻辑（Saga 补偿）

### 测试 Story（按开发顺序）

**STORY-99: E2E_Order_Flow**
- **类型**: E2E 测试 (type: e2e_test)
- **目的**: 验证订单创建 → 事件发布 → 持久化的完整流程
- **理由**: Feature 构成完整业务闭环，涉及聚合根、事件、持久化的集成
- **测试路径**: `tests/bdd/features/order/order_flow.feature`
- **执行顺序**: STORY-01, STORY-02, STORY-03, STORY-04 完成后

**STORY-97: Performance_Order**
- **类型**: 性能测试 (type: perf_test)
- **目的**: 验证订单创建的高并发性能
- **理由**: 核心域聚合，峰值需支持 1000 TPS，P95 < 500ms
- **执行顺序**: STORY-99 完成后
```

---

## ✅ Feature 生成后检查清单

**AI 必须在生成 Feature 文档后执行以下检查**：

### 基础检查
- [ ] **文件路径正确**: `.the_conn/epics/EPIC-XX_*/features/FEAT-XX_*/README.md`
- [ ] **Feature ID 格式正确**: FEAT-XX（两位数字，Epic 内唯一）
- [ ] **目录命名规范**: PascalCase，无空格
- [ ] **Frontmatter 完整**: id / status / created / depends_on

### 模式检查
- [ ] **模式继承正确**: Feature 模式与 Epic 模式一致
- [ ] **Standard Mode**: 基础格式（目标 + Story列表 + 验收标准）
- [ ] **Pro Mode**: + 聚合设计 / 领域事件 / 不变性规则（如适用）

### 内容检查
- [ ] **目标明确**: 一句话说明 Feature 的功能目标
- [ ] **验收标准清晰**: 端到端验收项，可测试
- [ ] **Story 列表完整**: 包含所有功能开发 Story
- [ ] **Story ID 正确**: STORY-XX 格式，Epic 内唯一

### 测试 Story 检查
- [ ] **E2E 测试决策**: 已根据规则判断是否需要 E2E Story
- [ ] **E2E Story 位置**: 如需要，已列在"测试 Story"部分
- [ ] **E2E Story ID**: STORY-99（E2E）或 STORY-98（第二个 E2E）
- [ ] **E2E Story 执行顺序**: 已明确说明在哪些 Story 完成后执行
- [ ] **性能测试决策**: 已根据规则判断是否需要性能测试 Story
- [ ] **性能测试 Story ID**: STORY-97（性能）或 STORY-96（第二个性能）

### Pro Mode 额外检查（如适用）
- [ ] **聚合设计完整**: 
  - 聚合根 / 实体 / 值对象 / 不变性规则 / 事务边界
- [ ] **一致性边界明确**: 
  - 聚合内 / 聚合间 / 跨上下文一致性策略
  - 实现机制（数据库事务 / 事件发布）
- [ ] **领域事件列表**: 
  - 事件名称 / 触发时机 / 携带数据 / 订阅者 / 对应 Story
- [ ] **ADR 引用**: 如有架构决策，已引用相关 ADR
- [ ] **聚合设计与 Review 一致**: 与 requirements_review Phase 2.2 的聚合设计表一致

### 依赖关系检查
- [ ] **depends_on 正确**: 列出了所有前置 Feature
- [ ] **无循环依赖**: Feature A 依赖 B，B 不能依赖 A
- [ ] **依赖存在**: 所有 depends_on 的 Feature 都已规划

### Story 顺序检查
- [ ] **功能 Story 在前**: 功能开发 Story 编号在测试 Story 之前
- [ ] **测试 Story 在后**: E2E/性能测试 Story 使用 STORY-99/98/97/96
- [ ] **执行顺序清晰**: 测试 Story 明确说明依赖哪些功能 Story

### Standard Mode 特定检查
- [ ] **格式简洁**: 仅包含目标、Story列表、验收标准
- [ ] **验收标准实用**: 端到端验收项，不涉及领域概念

### Pro Mode 特定检查
- [ ] **聚合根唯一**: 每个 Feature 通常对应一个聚合根
- [ ] **事务边界明确**: 说明了聚合的事务边界
- [ ] **不变性规则具体**: 列出了具体的业务规则
- [ ] **一致性策略合理**: 聚合内强一致，聚合间最终一致

### E2E 测试决策验证
- [ ] **判断依据正确**: 按照以下规则判断
  - Feature 构成完整业务闭环 → 需要 E2E ✅
  - Feature 仅是技术组件/单一CRUD → 不需要 E2E ❌
- [ ] **测试路径已规划**: BDD Feature 文件路径已列出
- [ ] **测试场景已概述**: 简要说明测试覆盖的场景

### 性能测试决策验证
- [ ] **判断依据正确**: 按照以下规则判断
  - 高并发/大数据量/实时响应要求 → 需要性能测试 ✅
  - 普通CRUD/低并发 → 不需要性能测试 ❌
- [ ] **性能指标已定义**: TPS/响应时间/并发数等指标
- [ ] **测试工具已说明**: 使用什么工具进行性能测试

---

现在，请根据用户提供的材料生成 Feature 规划。
