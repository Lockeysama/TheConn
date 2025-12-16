# The Conn Playbooks 基础公约

本文档定义了所有 AI Playbooks 必须遵守的基础规则和约束。

**重要性**：所有 Playbook 都必须严格遵守本公约，除非在特定 Playbook 中有明确的例外说明。

---

## 1. 核心原则

### 1.1 职责分离原则

- **规划与实现分离**：规划阶段只生成文档，实现阶段才编写代码
- **意图与执行分离**：人类定义"做什么"，AI 执行"怎么做"
- **文档与代码同步**：确保规划文档与代码实现保持一致

### 1.2 The Conn 工作流

```
规划阶段 (Playbooks)
    ↓ 生成文档
Task 执行阶段 (唯一允许编写代码的环节)
    ↓ 编写实现
同步阶段 (Playbooks)
    ↓ 更新文档
```

---

## 2. 严格禁止事项 ❌

### 2.1 代码实现

**禁止编写以下类型的代码**：
- ❌ 实际的业务逻辑实现代码
- ❌ 实际的测试实现代码（BDD step definitions、单元测试）
- ❌ 构建脚本、部署脚本
- ❌ 配置文件的具体实现

**例外**：只有 `execution/task_generation.md` Playbook 可以指导 AI 编写代码。

### 2.2 文件修改限制

**严格禁止修改以下目录/文件**：
- ❌ `.the_conn/docs/` 目录下的所有文件（用户文档）
- ❌ 项目源代码目录（除 .the_conn 以外的所有文件但不包括用户指定的存储目录）
- ❌ 已存在的测试代码

**例外**：
- ✅ 可以创建新的规划文档（epics/、context/ 目录）
- ✅ 可以更新 Story 状态（story_sync.md）
- ✅ 可以生成临时工作文件（ai_workspace/ 目录）

### 2.3 操作限制

**禁止执行以下操作**：
- ❌ 执行任何开发任务（编译、构建、测试）
- ❌ 修改项目依赖配置（package.json、requirements.txt、go.mod 等）
- ❌ 执行 Git 操作（commit、push、branch 等）
- ❌ 部署或发布操作

---

## 3. 允许事项 ✅

### 3.1 设计说明中的代码片段

**允许在文档中使用代码片段来说明设计**：
- ✅ 接口定义（interface、protocol）
- ✅ 数据结构定义（struct、class、type）
- ✅ API 签名（function signature）
- ✅ 示例代码（用于说明用法）
- ✅ 伪代码（用于说明算法）

**关键区别**：
```markdown
✅ 允许（设计说明）：
```go
// 接口定义
type Sender interface {
    Send(event Event) error
}
```

❌ 禁止（实际实现）：
```go
// 完整的实现代码
func (s *DefaultSender) Send(event Event) error {
    // 实现逻辑
    return s.queue.Push(event)
}
```
```

### 3.2 文档操作

**允许创建和修改以下文档**：
- ✅ Epic/Feature/Story 规划文档
- ✅ Context 文档（设计、架构、技术方案）
- ✅ Task 工作文档（ai_workspace/ 目录）
- ✅ 变更摘要、同步文档

---

## 4. 文件路径约定

### 4.1 目录结构

```
.the_conn/
├── docs/                # 用户文档（禁止修改）
├── playbooks/           # AI 操作剧本（本文件所在目录）
├── context/             # 知识库（可创建和修改）
├── epics/               # 规划文档（可创建和修改）
└── ai_workspace/        # 临时工作区（可创建和修改）
```

### 4.2 引用规则

**在 Playbook 中引用其他文件时**：
- 使用相对路径：`@playbooks/core/base_rules.md`
- 或使用绝对路径：`.the_conn/playbooks/core/base_rules.md`

**在 Playbook 中引用用户文档时**：
- 只读引用：`@docs/GUIDE.md`（仅用于告知用户，不可修改）

---

## 5. 文档生成规范

### 5.1 Markdown 格式

- 使用标准 Markdown 语法
- 代码块必须指定语言（如 ```go、```python）
- 表格必须对齐
- 使用合适的标题层级（# ## ### ####）

### 5.2 Frontmatter 规范

**Story/Epic/Feature 文档必须包含 Frontmatter**：
```yaml
---
id: STORY-01
type: dev
status: pending
created: 2025-12-16
---
```

**Context 文档必须包含 Frontmatter**：
```yaml
---
type: architecture
scope: global
title: 系统架构设计
created: 2025-12-16
updated: 2025-12-16
status: active
---
```

### 5.3 ID 命名规范

| 类型    | 格式                    | 示例         |
| ------- | ----------------------- | ------------ |
| Epic    | `EPIC-{序号}`           | `EPIC-01`    |
| Feature | `FEAT-{序号}`           | `FEAT-01`    |
| Story   | `STORY-{序号}`          | `STORY-01`   |
| Bug Fix | `STORY-{序号}.{子序号}` | `STORY-01.1` |
| Task    | `TASK-{序号}`           | `TASK-01`    |

### 5.4 语言使用规范

**核心原则**：AI 默认使用用户输入或对话使用的语言来生成所有文档。

**规则说明**：

1. **文档语言跟随对话语言**
   - 用户使用中文交流 → 生成中文文档
   - 用户使用英文交流 → 生成英文文档
   - 用户使用其他语言 → 生成相应语言的文档

2. **BDD Feature 语言双重判断**
   
   BDD Feature 需要判断两个维度的语言：
   
   **维度 1：编程语言（决定测试框架）**
   - 项目使用 Go → 使用 godog
   - 项目使用 Python → 使用 pytest-bdd 或 behave
   - 项目使用 JavaScript/TypeScript → 使用 cucumber-js
   - 项目使用 Java → 使用 Cucumber JVM
   
   **维度 2：自然语言（决定 Gherkin 关键词）**
   - 检查该 BDD 框架是否支持用户对话使用的自然语言
   - 如果支持 → 使用对话自然语言的 Gherkin 关键词
   - 如果不支持 → 使用英文 Gherkin 关键词（默认）
   
   **判断流程**：
   ```
   1. 识别项目编程语言 → 确定 BDD 框架（用户可指定）
   2. 识别用户对话自然语言 → 确定期望的 Gherkin 语言
   3. AI 自行分析框架文档/配置 → 确定框架支持的自然语言和关键词
   4. 根据分析结果 → 决定实际使用的 Gherkin 关键词
   ```
   
   **⚠️ 重要说明**：
   - 不同 BDD 框架对同一自然语言的关键词实现可能不同
   - 例如：中文关键词在不同框架中可能是 "功能/场景" 或 "特性/情景"
   - **AI 必须先查阅框架文档或分析项目配置，再确定使用的关键词**
   - 用户可以指定任意 BDD 框架，不限于参考表中列出的框架

**示例：**

**注意**：以下示例中的中文关键词（功能/场景/假如/当/那么）是基于 godog 框架的。不同框架可能使用不同的中文关键词，AI 必须先分析具体框架的语法支持。

**场景 1：Go 项目 + 中文对话**
```
编程语言: Go → BDD 框架: godog
对话语言: 中文 → 期望: 中文 Gherkin
godog 支持中文: ✅ 是 → 使用中文关键词
```
```gherkin
功能: 用户登录

  场景: 用户成功登录
    假如 用户已注册
    当 用户输入正确的用户名和密码
    那么 用户应该成功登录
    而且 页面应该跳转到首页
```

**场景 2：Python 项目 + 中文对话**
```
编程语言: Python → BDD 框架: pytest-bdd
对话语言: 中文 → 期望: 中文 Gherkin
pytest-bdd 支持中文: ❌ 否 → 使用英文关键词
```
```gherkin
Feature: User Login  # 框架不支持中文，使用英文

  Scenario: User logs in successfully
    Given the user is registered
    When the user enters correct username and password
    Then the user should be logged in
    And the page should redirect to home
```

**场景 3：JavaScript 项目 + 英文对话**
```
编程语言: JavaScript → BDD 框架: cucumber-js
对话语言: 英文 → 期望: 英文 Gherkin
cucumber-js 支持英文: ✅ 是 → 使用英文关键词
```
```gherkin
Feature: User Login

  Scenario: User logs in successfully
    Given the user is registered
    When the user enters correct username and password
    Then the user should be logged in
    And the page should redirect to home
```

**场景 4：Go 项目 + 英文对话**
```
编程语言: Go → BDD 框架: godog
对话语言: 英文 → 期望: 英文 Gherkin
godog 支持英文: ✅ 是 → 使用英文关键词
```
```gherkin
Feature: User Login

  Scenario: User logs in successfully
    Given the user is registered
    When the user enters correct username and password
    Then the user should be logged in
    And the page should redirect to home
```

**BDD 框架语言支持参考表**：

| 编程语言      | 常用 BDD 框架 | 支持中文 | 支持英文 | 其他语言支持 |
| ------------- | ------------- | -------- | -------- | ------------ |
| Go            | godog         | ✅        | ✅        | 多语言支持   |
| Python        | pytest-bdd    | ❌        | ✅        | 仅英文       |
| Python        | behave        | ✅        | ✅        | 多语言支持   |
| JavaScript/TS | cucumber-js   | ✅        | ✅        | 多语言支持   |
| Java          | Cucumber JVM  | ✅        | ✅        | 多语言支持   |
| Ruby          | cucumber      | ✅        | ✅        | 多语言支持   |
| C#            | SpecFlow      | ✅        | ✅        | 多语言支持   |

**⚠️ 重要说明**：
1. **此表仅供参考**，不限制用户只能使用表中的框架
2. **用户可以指定任意 BDD 框架**，AI 需要自行分析该框架的语法支持
3. **不同框架的关键词可能不同**，即使都支持中文，关键词也可能有差异
4. **AI 工作流程**：
   - 用户指定框架 → AI 查阅框架文档
   - 分析框架支持的自然语言和关键词
   - 根据分析结果生成正确的 Gherkin 语法
5. **具体支持情况请参考项目实际使用的框架版本文档**

**特殊情况处理**：

- 如果用户在中文对话中明确要求使用英文文档 → 使用英文
- 如果用户在英文对话中明确要求使用中文文档 → 使用中文
- 技术术语（如类名、函数名、变量名）→ 始终使用项目约定的命名规范，通常为英文
- 如果无法确定框架的语言支持 → 默认使用英文 Gherkin 关键词

---

## 6. 复杂度评估（不使用时间估算）

**重要**：在 The Conn 框架中，**不使用时间估算**，而使用**复杂度评分**。

### 6.1 复杂度评分标准

- **范围**：1.0 - 10.0 分（支持浮点数）
- **评分考虑因素**：
  - 技术难度
  - 工作量
  - 依赖复杂度
  - 风险等级

### 6.2 评分示例

| 复杂度 | 描述   | 示例                   |
| ------ | ------ | ---------------------- |
| 1.0    | 极简单 | 简单的数据结构定义     |
| 3.0    | 简单   | 基础的 CRUD 操作       |
| 5.0    | 中等   | 带业务逻辑的功能模块   |
| 7.0    | 复杂   | 多模块集成、算法实现   |
| 10.0   | 极复杂 | 核心架构设计、复杂算法 |

---

## 7. 与用户交互规范

### 7.1 讨论与决策

- **主动质疑**：对不合理的需求要勇于指出
- **提供选项**：给出 2-3 个方案供用户选择
- **等待确认**：重大决策前必须等待用户确认
- **记录决策**：重要的技术决策要记录理由

### 7.2 输出格式

- **清晰分段**：使用标题、列表、表格组织内容
- **突出重点**：使用 ⚠️、✅、❌ 等符号标记重要信息
- **简洁明了**：避免冗长的解释，突出关键信息

---

## 8. 质量标准

### 8.1 文档质量

- ✅ 语言精炼，表达准确
- ✅ 结构清晰，层次分明
- ✅ 格式规范，易于阅读
- ✅ 内容完整，无遗漏

### 8.2 设计质量

- ✅ 遵循 KISS 原则（Keep It Simple, Stupid）
- ✅ 避免过度设计
- ✅ 考虑可维护性和可扩展性
- ✅ 基于最佳实践

---

## 9. 检查清单

**在完成 Playbook 执行前，自检以下项目**：

- [ ] 是否遵守了所有禁止事项？
- [ ] 是否修改了 `docs/` 目录？（禁止！）
- [ ] 是否编写了实现代码？（禁止！）
- [ ] 生成的文档格式是否规范？
- [ ] Frontmatter 是否完整？
- [ ] ID 命名是否符合规范？
- [ ] 是否使用了复杂度评分而非时间估算？

---

## 10. 例外情况

### 10.1 Task 执行阶段

**唯一例外**：`execution/task_generation.md` 生成的 Task 简报会指导 AI 编写实际代码。

这是 The Conn 框架中**唯一允许编写实现代码的环节**。

### 10.2 紧急修复

在极特殊情况下（如安全漏洞修复），可以在用户明确授权后突破某些限制，但必须：
1. 获得用户明确授权
2. 详细记录例外原因
3. 事后同步更新文档

---

## 遵守声明

**所有 Playbook 在开头应包含以下声明**：

```markdown
## ⚠️ 重要：遵守基础公约

本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。
```

---

**最后更新**: 2025-12-16
**维护者**: The Conn Framework Team

