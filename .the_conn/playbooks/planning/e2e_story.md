# E2E Story 生成指南

你是一位资深的质量工程师。你的任务是为 Feature 或 Epic 生成端到端（E2E）测试 Story，使用 BDD 场景验证完整的业务流程。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

## 本 Playbook 的工作范围

**专注于**：

- ✅ **生成 E2E Story 文档**：创建端到端测试 Story 文件
- ✅ **编写 BDD 场景**：使用 Gherkin 格式描述完整业务流程
- ✅ **设计测试策略**：规划集成测试的范围和重点

**📋 规范引用**：

- **测试策略**：`@playbooks/core/test_strategy_rules.md`
- **BDD 语言配置**：`@playbooks/core/bdd_language_rules.md`

---

## E2E Story 类型

### Feature E2E Story

- **用途**：验证一个 Feature 内多个 Story 的集成流程
- **ID 范围**：STORY-97 ~ STORY-99
- **触发时机**：Feature 的功能 Story 全部完成后
- **依赖**：依赖该 Feature 的所有功能 Story

### Epic E2E Story

- **用途**：验证跨 Feature 的完整用户旅程
- **ID 范围**：STORY-997 ~ STORY-999
- **触发时机**：Epic 的所有 Feature 完成后
- **依赖**：依赖多个 Feature 的关键 Story

---

## ⚠️ 前置检查：BDD 配置

**生成 E2E Story 前，需要确认以下信息：**

1. **项目编程语言**（如 Go, Python, JavaScript）→ 决定默认 BDD 框架
2. **测试框架/库**（用户可指定任意框架）
3. **项目交互语言** → 决定描述文本的语言（AI 根据 Context 指定或用户对话语言自动判断）

**BDD 语言配置规则（强制执行）**：

1. **关键字 (Keywords)**: **统一使用英文** (`Feature`, `Scenario`, `Given`, `When`, `Then`, `And` 等)。
2. **描述 (Descriptions)**: **使用项目交互的自然语言**（AI 自动适配，参考 `@playbooks/core/bdd_language_rules.md`）。

**⚠️ 重要提醒**：

- 如果用户未提供编程语言或测试框架信息，**必须先提醒用户提供，不要自行假设**。
- 生成 BDD 场景时，严禁翻译 Gherkin 关键字。

---

## 命名与格式规范

### ID 命名规则

| E2E 类型    | ID 范围         | 示例        | 说明                      |
| ----------- | --------------- | ----------- | ------------------------- |
| Feature E2E | STORY-97 ~ 99   | `STORY-99`  | Feature 内唯一，建议用 99 |
| Epic E2E    | STORY-997 ~ 999 | `STORY-999` | Epic 内唯一，建议用 999   |
| 性能测试    | STORY-97        | `STORY-97`  | 如需要性能测试            |

### 文件命名规则

| E2E 类型    | 格式                                     | 示例                                 |
| ----------- | ---------------------------------------- | ------------------------------------ |
| Feature E2E | `STORY-{序号}_E2E_{FeatureName}_Flow.md` | `STORY-99_E2E_Auth_Flow.md`          |
| Epic E2E    | `STORY-{序号}_Epic_E2E_{EpicName}.md`    | `STORY-999_Epic_E2E_User_Journey.md` |

### 文件路径

```
.the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{Name}/stories/STORY-{序号}_E2E_{Name}.md
```

### Frontmatter 规范

```yaml
---
id: STORY-99
type: e2e_test
epic: EPIC-01
feature: FEAT-01
status: pending
created: yyyy-mm-dd
depends_on:
  - STORY-01
  - STORY-02
  - STORY-03
---
```

**字段说明**：

- `type`: 固定为 `e2e_test`
- `depends_on`: 列出被测试的所有功能 Story

---

## 输出格式

### Feature E2E Story 模板

```markdown
---
id: STORY-99
type: e2e_test
epic: EPIC-{序号}
feature: FEAT-{序号}
status: pending
created: yyyy-mm-dd
depends_on:
  - STORY-01
  - STORY-02
  - STORY-03
---

# Story: E2E_{FeatureName}_Flow

## 1. 目标

验证 {Feature 名称} 的完整用户旅程，确保所有功能 Story 集成后能正确协同工作。

## 2. 验收标准（BDD 场景）

{根据项目的 BDD 配置生成，关键字统一使用英文}

Feature: {Feature 名称完整流程}

  Scenario: {端到端场景1 - Happy Path}
    Given {用户初始状态}
    When {执行完整操作流程}
    Then {最终业务结果}
    And {系统状态验证}

  Scenario: {端到端场景2 - 异常处理}
    Given {某个前置条件}
    When {触发异常情况}
    Then {系统正确处理}
    And {用户收到明确反馈}

  Scenario: {端到端场景3 - 数据一致性}
    Given {初始数据状态}
    When {跨模块操作}
    Then {数据保持一致}

## 3. 测试范围

**集成的 Stories**:
- STORY-01: {功能描述}
- STORY-02: {功能描述}
- STORY-03: {功能描述}

**测试重点**:
- 模块间接口集成
- 数据流转正确性
- 端到端业务流程
- 异常情况处理
- 数据一致性验证

## 4. 实现指导

**测试文件位置**:
- BDD Feature: `tests/bdd/features/{module}/{feature_name}_flow.feature`
- Step Definitions: `tests/bdd/{language}_test.{ext}`

**测试策略**:
- 使用真实组件集成（避免过度 Mock）
- 模拟用户真实操作路径
- 验证关键业务指标
- 测试主要的异常路径

**测试数据**:
- 使用 fixtures 准备测试数据
- 测试前清理环境
- 测试后恢复状态
```

### Epic E2E Story 模板

```markdown
---
id: STORY-999
type: e2e_test
epic: EPIC-{序号}
feature: FEAT-{最后一个}
status: pending
created: yyyy-mm-dd
depends_on:
  - STORY-{关键Story1}
  - STORY-{关键Story2}
  - STORY-{关键Story3}
---

# Story: Epic_E2E_{EpicName}

## 1. 目标

验证 {Epic 名称} 的完整用户旅程，确保跨 Feature 的业务流程端到端正常工作。

## 2. 验收标准（BDD 场景）

{根据项目的 BDD 配置生成，关键字统一使用英文}

Feature: {Epic 名称端到端用户旅程}

  Scenario: 完整用户旅程 - Happy Path
    Given {用户从零开始}
    When {执行跨 Feature 的完整流程}
    Then {达成 Epic 的业务目标}
    And {所有关键指标满足}

  Scenario: 跨模块异常处理
    Given {某个 Feature 出现异常}
    When {用户继续操作}
    Then {系统优雅降级}
    And {用户体验不受重大影响}

## 3. 测试范围

**涉及的 Features**:
- FEAT-01: {功能描述}
- FEAT-02: {功能描述}
- FEAT-03: {功能描述}

**关键 Stories**:
- STORY-{X}: {关键功能点}
- STORY-{Y}: {关键功能点}

**测试重点**:
- 跨 Feature 的数据流转
- 用户完整业务旅程
- Feature 间的依赖关系
- 端到端性能表现

## 4. 实现指导

**测试文件位置**:
- BDD Feature: `tests/bdd/features/{epic_name}_journey.feature`
- Step Definitions: `tests/bdd/{epic_name}_test.{ext}`

**测试策略**:
- 完全端到端测试（最小化 Mock）
- 模拟真实用户场景
- 关注关键业务指标
- 验证跨模块集成点
```

---

## BDD 场景编写规则

### Gherkin 语法示例

```gherkin
Feature: {名称}
  Scenario: {场景}
    Given {前置}
    When {动作}
    Then {结果}
    And {附加验证}
```

**AI 工作流程**：强制使用英文关键字 → 识别项目自然语言 → 生成描述文本

### 场景编写原则

1. **端到端视角**：从用户视角描述完整流程
2. **业务语言**：使用业务术语，避免技术实现细节
3. **独立可验证**：每个场景独立运行
4. **具体可操作**：步骤明确，易于实现
5. **覆盖关键路径**：Happy Path + 主要异常路径

### 场景数量建议

- **Feature E2E**: 2-4 个场景
  - 1 个 Happy Path（必须）
  - 1-2 个异常处理场景
  - 1 个数据一致性场景（如需要）

- **Epic E2E**: 1-3 个场景
  - 1 个完整用户旅程（必须）
  - 1 个跨模块异常处理
  - 1 个性能/压力场景（如需要）

---

## 生成原则

1. **依赖明确**：`depends_on` 必须列出所有被测试的功能 Story
2. **场景完整**：覆盖端到端的主要流程和关键异常
3. **测试路径规范**：遵循 `tests/bdd/features/{module}/` 结构
4. **避免过度设计**：聚焦核心流程，不要测试每个细节
5. **真实集成**：尽量使用真实组件，减少 Mock

---

## 示例

### 示例 1: Feature E2E Story（Go + godog + 中文）

```markdown
---
id: STORY-99
type: e2e_test
epic: EPIC-01
feature: FEAT-01
status: pending
created: 2025-12-16
depends_on:
  - STORY-01
  - STORY-02
  - STORY-03
---

# Story: E2E_Auth_Flow

## 1. 目标

验证用户认证功能的完整流程，确保注册、登录、权限检查等模块正确集成。

## 2. 验收标准

Feature: 用户认证完整流程

  Scenario: 新用户完整认证旅程
    Given 系统中不存在该用户
    When 用户提交注册信息
    And 用户使用注册信息登录
    Then 用户应该成功进入系统
    And 用户应该拥有默认权限

  Scenario: 登录失败后重试
    Given 用户已注册
    When 用户首次使用错误密码登录
    And 用户使用正确密码重新登录
    Then 用户应该成功登录
    And 系统应该记录登录历史

  Scenario: 权限验证集成
    Given 用户已登录
    When 用户访问需要特定权限的功能
    Then 系统应该正确验证权限
    And 无权限用户应该收到明确提示

## 3. 测试范围

**集成的 Stories**:
- STORY-01: 用户注册模块
- STORY-02: 用户登录模块
- STORY-03: 权限验证模块

**测试重点**:
- 注册→登录数据流转
- Session 管理正确性
- 权限检查集成
- 错误处理和用户提示

## 4. 实现指导

**测试文件位置**:
- BDD Feature: `tests/bdd/features/auth/auth_flow.feature`
- Step Definitions: `tests/bdd/auth_test.go`

**测试策略**:
- 使用真实数据库（测试环境）
- 使用真实 Session 存储
- 测试前清理测试用户数据
```

---

现在，请根据用户提供的 Feature 或 Epic 信息生成 E2E Story。
