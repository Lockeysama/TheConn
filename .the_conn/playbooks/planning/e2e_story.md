# E2E Story 生成指南

你是一位资深的质量工程师。你的任务是为 Feature 或 Epic 生成端到端（E2E）测试 Story，使用 BDD 场景验证完整的业务流程。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@rules/base_rules.md` 中定义的所有基础公约。**

**📋 规范引用**：

本 Playbook 依赖以下规范文件（AI 必须先加载）：
- **基础公约**: `@rules/base_rules.md` - 禁止事项、文件路径约定、质量标准
- **测试策略**: `@rules/test_strategy_rules.md` - Story 类型判断、测试策略
- **BDD 语言配置**: `@rules/bdd_language_rules.md` - BDD 关键字和描述语言规范

## 本 Playbook 的工作范围

**专注于**：

- ✅ **生成 E2E Story 文档**：创建端到端测试 Story 文件
- ✅ **编写 BDD 场景**：使用 Gherkin 格式描述完整业务流程
- ✅ **设计测试策略**：规划集成测试的范围和重点

---

## 🔄 执行流程追踪

**AI 必须在执行过程中维护以下追踪表格**：

```markdown
## 🔄 E2E Story 生成执行追踪

| Phase | 内容               | 状态 | 输出 | 备注   |
| ----- | ------------------ | ---- | ---- | ------ |
| 1     | 范围分析与策略     | ⏳    | -    | 待开始 |
| 2     | BDD 场景设计       | ⏳    | -    | 待开始 |
| 3     | 生成 Story 文档    | ⏳    | -    | 待开始 |

**图例**：✅ 已完成 | 🔄 进行中 | ⏳ 等待中 | ❌ 失败
```

### Phase 1: 范围分析与策略

#### ✅ 策略与配置检查点

**AI 必须确认以下项目后才能进入场景设计**：

- [ ] **BDD 配置**: 已确认语言、框架、feature 文件位置 (从 Context 读取)
- [ ] **测试类型**: Feature E2E vs Epic E2E
- [ ] **依赖 Story**: 已列出所有需集成的 Story
- [ ] **测试重点**: 明确了集成验证的核心目标
- [ ] **执行追踪表格**: Phase 1 状态为 ✅

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

## 📋 BDD 配置自动读取

**AI 应自动从以下位置读取 BDD 配置**：

1. **优先读取**：`.the_conn/context/global/Testing_Strategy.md`
   - 编程语言
   - BDD 框架
   - 描述语言
   - Feature 文件位置

2. **如果配置不完整**：
   - 仅询问缺失的配置项
   - 不要重复询问已有的配置

3. **BDD 语言配置规则（强制执行）**：
   - **关键字 (Keywords)**: **统一使用英文** (`Feature`, `Scenario`, `Given`, `When`, `Then`, `And` 等)
   - **描述 (Descriptions)**: **使用项目交互的自然语言**（从 Context 读取或根据用户对话语言自动判断）

**⚠️ 重要**：生成 BDD 场景时，严禁翻译 Gherkin 关键字。

---

## 命名与格式规范

### ID 命名规则

| E2E 类型    | ID 范围         | 示例        | 说明                      |
| --- | --- | --- | --- |
| Feature E2E | STORY-97 ~ 99   | `STORY-99`  | Feature 内唯一，建议用 99 |
| Epic E2E    | STORY-997 ~ 999 | `STORY-999` | Epic 内唯一，建议用 999   |
| 性能测试    | STORY-97        | `STORY-97`  | 如需要性能测试            |

### 文件命名规则

| E2E 类型    | 格式                                     | 示例                                 |
| --- | --- | --- |
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

## 输出格式速查

### Feature E2E vs Epic E2E 对比

| 维度 | Feature E2E | Epic E2E |
| --- | --- | --- |
| **ID范围** | STORY-97~99（推荐99） | STORY-997~999（推荐999） |
| **文件名** | `STORY-99_E2E_{Feature}_Flow.md` | `STORY-999_Epic_E2E_{Epic}.md` |
| **触发时机** | Feature所有功能Story完成后 | Epic所有Feature完成后 |
| **depends_on** | 该Feature的所有功能Story | 跨Feature的关键Story |
| **BDD场景数** | 2-4个（Happy+异常+数据一致性） | 1-3个（完整旅程+跨模块异常+性能） |
| **测试范围** | Feature内多个Story集成 | 跨Feature完整用户旅程 |
| **测试重点** | 模块间接口/数据流转/端到端流程 | 跨Feature数据流转/Feature间依赖 |
| **测试策略** | 真实组件集成（避免过度Mock） | 完全端到端（最小化Mock） |

### 统一模板结构

```markdown
---
id: STORY-{99或999}
type: e2e_test
epic: EPIC-XX
feature: FEAT-XX
status: pending
created: yyyy-mm-dd
depends_on: [{Story列表}]
---

# Story: {E2E_FeatureName_Flow 或 Epic_E2E_EpicName}

## 1. 目标
验证 {Feature/Epic 名称} 的完整{用户旅程/业务流程}，确保{集成/跨Feature}后正确协同工作。

## 2. 验收标准（BDD 场景）
Feature: {完整流程名称}
  Scenario: {场景名}
    Given {前置条件}
    When {操作流程}
    Then {业务结果}
    And {状态验证}

## 3. 测试范围
**集成的Stories**: {列表}
**测试重点**: {接口集成/数据流转/端到端流程/异常处理/数据一致性}

## 4. 实现指导
**测试文件**: `tests/bdd/features/{module}/{name}.feature`
**测试策略**: {真实组件/用户路径/关键指标/异常路径}
**测试数据**: 使用Factory Pattern管理（Setup创建+Teardown清理+数据隔离）
```

**测试数据Factory Pattern核心**：
- ✅ 工厂类：`{Entity}Factory.create_{entity}(opts)` 提供默认值+自定义
- ✅ Setup：清理旧数据+初始化环境+Factory创建基础数据
- ✅ Teardown：清理测试数据+恢复状态+关闭连接
- ✅ 隔离：独立测试库+特殊标识（如`test_`前缀）

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

## 示例（Feature E2E - Go + godog + 中文）

```markdown
---
id: STORY-99
type: e2e_test
epic: EPIC-01
feature: FEAT-01
status: pending
created: 2025-12-16
depends_on: [STORY-01, STORY-02, STORY-03]
---

# Story: E2E_Auth_Flow

## 1. 目标
验证用户认证功能的完整流程，确保注册、登录、权限检查等模块正确集成。

## 2. 验收标准（BDD 场景）
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
**集成Stories**: STORY-01(注册)/STORY-02(登录)/STORY-03(权限)
**测试重点**: 注册→登录数据流转/Session管理/权限检查集成/错误处理

## 4. 实现指导
**测试文件**: `tests/bdd/features/auth/auth_flow.feature` + `tests/bdd/auth_test.go`
**测试策略**: 真实数据库+真实Session+Factory Pattern管理测试数据

**Factory示例（Go）**:
```go
type UserFactory struct{}
func (f *UserFactory) CreateUser(opts ...UserOption) *User {
    user := &User{Email: fmt.Sprintf("test_user_%s@example.com", randomID()), Password: "Test@1234"}
    for _, opt := range opts { opt(user) }
    return user
}
// 使用: user := UserFactory{}.CreateUser(WithEmail("test@example.com"))
```
```

---

## ✅ E2E Story 生成后检查清单

**AI 必须在生成 Story 文档后执行以下检查**：

### 基础检查
- [ ] **ID 规范**: STORY-99/999 (推荐) 或 90+
- [ ] **Type**: 固定为 `e2e_test`
- [ ] **Depends On**: 完整列出了所有依赖的功能 Story

### 内容检查
- [ ] **BDD 格式**: Given/When/Then 结构清晰
- [ ] **关键字**: 英文关键字 (Scenario, Given, ...)
- [ ] **描述语言**: 符合项目语言 (中文/英文)
- [ ] **场景完整**: 包含 Happy Path 和 异常场景

### 质量检查
- [ ] **Factory Pattern**: 提供了测试数据工厂示例
- [ ] **测试独立性**: 场景之间无强依赖
- [ ] **执行追踪表格**: 所有 Phase 状态为 ✅

---

现在，请根据用户提供的 Feature 或 Epic 信息生成 E2E Story。
