# Context 添加指南

根据用户提供的内容，创建新的 Context 文档。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

**📋 规范引用**：

本 Playbook 依赖以下规范文件（AI 必须先加载）：
- **基础公约**: `@playbooks/core/base_rules.md` - 禁止事项、文件路径约定、质量标准

本 Playbook **不依赖**以下规范：
- ❌ `test_strategy_rules.md` - Context 添加不涉及测试策略决策
- ❌ `bdd_language_rules.md` - Context 添加不涉及 BDD

**原因**: context/add 只负责创建 Context 文档，不涉及测试策略规划

## 本 Playbook 的工作范围

**专注于**：创建新的 Context 文档

**重要**：Context 文档是**设计文档**，关注"是什么"和"为什么"，严格避免实现逻辑细节。

---

## 使用场景

- 需要添加新的架构设计
- 需要记录新的模块设计
- 需要定义新的 API 规范
- 需要补充遗漏的 Context

---

## Context 类型系统

### 全局 Context (scope: global)

**⚠️ 重要：Global Context 固定为以下 4 个文件，不随意新增**

适用于整个项目的通用知识，所有 Epic 都可引用。

| Type               | 说明     | 固定文件名                      | 内容归类规则                                                 |
| ------------------ | -------- | ------------------------------- | ------------------------------------------------------------ |
| `architecture`     | 系统架构 | `Architecture.md`               | 系统设计、模块关系、通信方式、架构原则、部署方案、API 约定等 |
| `tech_stack`       | 技术栈   | `Tech_Stack.md`                 | 语言、框架、工具、数据库、中间件等技术选型                   |
| `coding_standard`  | 编码规范 | `Coding_Standard_{Language}.md` | 命名约定、错误处理、注释规范、最佳实践等                     |
| `testing_strategy` | 测试策略 | `Testing_Strategy.md`           | 测试方法、覆盖率要求、BDD/TDD 策略、测试组织规范等           |

**⚠️ Global Context 添加规则**：
- ❌ **不创建新的 Global Context 文件**
- ✅ **公约类型的内容必须归入已有的 4 个文件**
- 🔄 **使用 `@prompts/context/update.md` 更新已有文件，而不是创建新文件**

**示例**：
- 需要添加部署方案 → 更新 `Architecture.md` 添加新章节
- 需要添加 API 约定 → 更新 `Architecture.md` 添加新章节
- 需要添加安全规范 → 更新 `Architecture.md` 添加新章节
- 需要添加性能优化实践 → 更新 `Coding_Standard_{Language}.md` 添加新章节

### Epic Context (scope: epic:EPIC-XX)

特定 Epic 的专属知识，仅该 Epic 使用。

| Type            | 说明     | 典型文件名                |
| --------------- | -------- | ------------------------- |
| `module_design` | 模块设计 | `Module_Design_Init.md`   |
| `data_model`    | 数据模型 | `Data_Model_User.md`      |
| `api_spec`      | API 规范 | `API_Spec_REST.md`        |
| `integration`   | 集成方案 | `Integration_OAuth.md`    |
| `algorithm`     | 算法说明 | `Algorithm_Scheduling.md` |
| `protocol`      | 协议设计 | `Protocol_Design_UDP.md`  |
| `migration`     | 迁移方案 | `Migration_V1_To_V2.md`   |

---

## 输入要求

用户需要提供：

1. **Context 类型**: 从上述枚举中选择
2. **Context 作用域**: global 或 EPIC-XX
3. **Context 内容**: 技术方案、设计文档、讨论结果等

---

## 输出要求

### 1. 文件路径格式

```
{Scope 目录}/{Type}_{Descriptor}.md
```

**全局 Context**:

```
.the_conn/context/global/{Type}_{Descriptor}.md
```

**Epic Context**:

```
.the_conn/context/epics/EPIC-{序号}/{Type}_{Descriptor}.md
```

**命名规则**:

- `{Type}`: 从类型枚举中选择（小写）
- `{Descriptor}`: 描述性名称，使用 PascalCase
- 特殊情况：纯类型名不加 Descriptor（如 `Architecture.md`）

**示例**:

- `.the_conn/context/global/Architecture.md`
- `.the_conn/context/global/Tech_Stack.md`
- `.the_conn/context/global/Coding_Standard_Go.md`
- `.the_conn/context/epics/EPIC-01/Module_Design_Init.md`
- `.the_conn/context/epics/EPIC-02/Protocol_Design_UDP.md`

---

### 2. Frontmatter 规范

```yaml
---
type: {类型}
scope: {global 或 epic:EPIC-XX}
title: {标题}
created: {yyyy-mm-dd}
updated: {yyyy-mm-dd}
status: active
tags:
  - {tag1}
  - {tag2}
---
```

**字段说明**:

| 字段      | 类型   | 说明             | 示例                       | 必填 |
| --------- | ------ | ---------------- | -------------------------- | ---- |
| `type`    | enum   | Context 类型     | `architecture`             | 是   |
| `scope`   | string | 范围             | `global` 或 `epic:EPIC-01` | 是   |
| `title`   | string | 标题             | `系统架构设计`             | 是   |
| `created` | date   | 创建日期         | `2025-12-11`               | 是   |
| `updated` | date   | 最后更新日期     | `2025-12-11`               | 是   |
| `status`  | enum   | 状态             | `active` / `deprecated`    | 是   |
| `tags`    | array  | 标签（便于搜索） | `[microservices, grpc]`    | 否   |

**字段约束**:

- `type`: 必须从类型枚举中选择
- `scope`: 格式必须是 `global` 或 `epic:EPIC-{序号}`
- `created`: 创建时的日期
- `updated`: 初次创建时与 `created` 相同
- `status`: 新创建的 Context 都是 `active`
- `tags`: 可选但强烈推荐，有助于 Context 搜索

---

## 生成原则

**核心原则: Context 是设计文档，不是实现手册**

**⚠️ 添加前必须先检查已有 Context！**

0. **避免重复 + Global Context 更新优先**:
   - 使用 `@prompts/context/search.md` 搜索是否已有相关 Context
   - **如果是公约类型内容（架构、技术栈、编码规范、测试策略）**：
     - ❌ **不创建新的 Global Context 文件**
     - ✅ **必须使用 `@prompts/context/update.md` 更新已有的 4 个 Global Context 文件**
   - 如果与 global Context 重叠，Epic Context 应引用而非复制
   - 原则：**Global Context 固定 4 个文件，Epic Context 自由创建**

1. **类型准确**: 根据内容选择最合适的 type
2. **范围判断**: 
   - **公约类型** → 必须归入 global 的 4 个固定文件
   - **Epic 专属** → 可以创建新的 Epic Context 文件
3. **命名清晰**: Descriptor 应简洁明确，使用 PascalCase（仅 Epic Context）
4. **结构清晰**: 使用标题层级组织内容
5. **抽象层次**: 聚焦设计决策、接口约定、架构原则，**严格避免实现细节**
6. **聚焦"是什么"和"为什么"**: 记录设计意图和架构决策，而非"怎么做"
7. **保持精简**: 只包含 AI 理解设计所必需的信息

**应该记录的内容**:

- ✅ 设计决策和理由（"选择异步架构是因为..."）
- ✅ 模块职责和边界（"认证模块负责..."）
- ✅ 接口定义和约定（"API 返回格式为..."）
- ✅ 数据结构和模型（"用户实体包含字段..."）
- ✅ 约束和要求（"响应时间不超过 100ms"）

**严格禁止的内容**:

- ❌ 代码实现逻辑（"在函数内部先判断..."）
- ❌ 算法步骤细节（"使用循环遍历数组..."）
- ❌ 变量和函数命名（"定义变量 x = ..."）
- ❌ 错误处理实现（"try-catch 捕获异常..."）
- ❌ 日志和调试信息（"打印日志到控制台..."）

---

## 内容结构模板

### 架构/设计类 (architecture, module_design, protocol)

```markdown
# {标题}

## 1. 概述与目标

{简要说明设计目标和适用场景，1-3 句话}

## 2. 核心设计

### 2.1 {设计要点1}

{说明}

### 2.2 {设计要点2}

{说明}

## 3. 技术选型（如适用）

| 类别   | 选择   | 理由         |
| ------ | ------ | ------------ |
| {类别} | {技术} | {为什么选择} |

## 4. 接口定义（如适用）

{API 签名、模块接口、数据结构定义}

## 5. 关键约束

- {设计约束、性能要求、安全要求}
- {技术限制、依赖要求}

## 6. 注意事项

- {使用注意事项、已知限制}

---

**注意**: 保持在设计和架构层面，避免深入具体实现逻辑
```

---

### API/数据模型类 (api_spec, data_model, api_convention)

```markdown
# {标题}

## 1. 概述

{API/模型用途，1-2 句话}

## 2. 定义

### 2.1 {接口/模型1}

{定义或签名}

### 2.2 {接口/模型2}

{定义或签名}

## 3. 示例

{使用示例，帮助理解}

## 4. 约束与规则

- {验证规则}
- {限制条件}
```

---

### 集成/迁移/部署类 (integration, migration, deployment)

```markdown
# {标题}

## 1. 背景

{为什么需要，1-3 句话}

## 2. 方案概述

{方案简要说明}

## 3. 关键步骤

1. {步骤1}
2. {步骤2}

## 4. 配置说明（如适用）

{配置项说明}

## 5. 风险与对策

| 风险   | 影响   | 应对措施 |
| ------ | ------ | -------- |
| {风险} | {影响} | {措施}   |
```

---

### 规范/策略类 (coding_standard, testing_strategy, domain_model)

```markdown
# {标题}

## 1. 目标

{规范的目的}

## 2. 规则

### 2.1 {规则类别1}

{具体规则}

### 2.2 {规则类别2}

{具体规则}

## 3. 示例

**好的做法**:
```{language}
{示例代码}
```

**不好的做法**:

```{language}
{示例代码}
```

## 4. 检查清单

- [ ] {检查项1}
- [ ] {检查项2}

```

---

## 示例

### 示例 1: 添加编码规范

**用户输入**:
```

类型: coding_standard
作用域: global
语言: Go
内容: Go 编码规范 - 错误处理、命名约定、注释规范

```

**输出**:

**文件**: `.the_conn/context/global/Coding_Standard_Go.md`

```markdown
---
type: coding_standard
scope: global
title: Go 编码规范
created: 2025-12-11
updated: 2025-12-11
status: active
tags:
  - golang
  - coding-style
  - best-practices
---

# Go 编码规范

## 1. 目标

确保 Go 代码风格统一，提高可读性和可维护性。

## 2. 规则

### 2.1 命名约定

- **变量**: 驼峰命名，首字母小写（如 `userName`）
- **常量**: 驼峰命名，首字母大写（如 `MaxRetries`）
- **函数**: 驼峰命名，导出函数首字母大写（如 `GetUser`）
- **接口**: 单方法接口以 `-er` 结尾（如 `Reader`, `Writer`）

### 2.2 错误处理

- 不忽略错误，明确处理或返回
- 错误信息使用小写，不以标点结尾
- 使用 `errors.New()` 创建简单错误
- 使用 `fmt.Errorf()` 添加上下文

### 2.3 注释规范

- 导出函数必须有注释，以函数名开头
- 注释使用完整句子，以句号结尾
- 复杂逻辑添加行内注释

## 3. 示例

**好的做法**:
```go
// GetUser retrieves user information by ID.
func GetUser(id int) (*User, error) {
    user, err := db.Query(id)
    if err != nil {
        return nil, fmt.Errorf("failed to get user %d: %w", id, err)
    }
    return user, nil
}
```

**不好的做法**:

```go
// get user
func getUser(id int) *User {
    user, _ := db.Query(id) // 忽略错误
    return user
}
```

## 4. 检查清单

- [ ] 所有导出函数都有注释
- [ ] 所有错误都被处理
- [ ] 命名符合 Go 惯例
- [ ] 使用 `gofmt` 格式化代码

```

---

### 示例 2: 添加模块设计

**用户输入**:
```

类型: module_design
作用域: EPIC-01
内容: 初始化模块设计 - 负责创建项目目录结构

```

**输出**:

**文件**: `.the_conn/context/epics/EPIC-01/Module_Design_Init.md`

```markdown
---
type: module_design
scope: epic:EPIC-01
title: 初始化模块设计
created: 2025-12-11
updated: 2025-12-11
status: active
tags:
  - initialization
  - project-structure
  - cli
---

# 初始化模块设计

## 1. 概述与目标

提供 CLI 命令一键创建 The Conn 框架的标准目录结构和必要配置文件。

## 2. 核心设计

### 2.1 目录结构定义

使用常量定义标准目录树：
```python
PROJECT_STRUCTURE = {
    ".the_conn": {
        "epics": {},
        "context": {
            "global": {},
            "epics": {}
        },
        "ai_workspace": {}
    },
    "src": {},
    "tests": {
        "bdd": {
            "features": {},
            "step_defs": {}
        },
        "unit": {}
    }
}
```

### 2.2 幂等性设计

重复执行不覆盖已有文件：

- 检查目标文件是否存在
- 存在则跳过，输出提示
- 不存在则创建

## 3. 接口设计

```python
def init_project(
    target_path: Path,
    overwrite: bool = False,
    template_set: str = "default"
) -> InitResult:
    """
    初始化 The Conn 项目结构
    
    Args:
        target_path: 目标目录
        overwrite: 是否覆盖已有文件
        template_set: 模板集名称
        
    Returns:
        InitResult: 初始化结果（成功文件列表、跳过文件列表）
    """
```

## 4. 关键约束

- 路径处理需跨平台兼容（支持 Unix/Windows）
- 文件权限: Unix 644, Windows 默认
- 目录权限: Unix 755, Windows 默认
- 需要检查目标目录写权限

## 5. 注意事项

- 大量文件创建时建议提供进度反馈
- 考虑失败时的回滚策略

```

---

### 示例 3: 添加协议设计

**用户输入**:
```

类型: protocol
作用域: EPIC-02
内容: UDP 可靠传输协议（3次冗余 + 动态捎带）

```

**输出**:

**文件**: `.the_conn/context/epics/EPIC-02/Protocol_Design_UDP.md`

```markdown
---
type: protocol
scope: epic:EPIC-02
title: UDP 可靠传输协议设计
created: 2025-12-11
updated: 2025-12-11
status: active
tags:
  - udp
  - reliability
  - protocol
  - redundancy
---

# UDP 可靠传输协议设计

## 1. 概述与目标

解决 UDP 丢包问题，实现 99.9% 事件到达率，无需 ACK 等待，低延迟。

## 2. 核心设计

### 2.1 协议结构

```json
{
  "h": {
    "seq": 5001,        // Packet 序号（单调递增）
    "ts": 1699999001    // 发送时间戳（毫秒）
  },
  "d": [
    {
      "id": 101,        // Event 唯一 ID
      "event": "..."    // Event 数据
    }
  ]
}
```

### 2.2 冗余策略

每个 Event 发送 3 次：

- **T+0ms**: 首次发送
- **T+20ms**: 第 1 次冗余
- **T+40ms**: 第 2 次冗余

动态捎带：后续 Packet 可携带历史 Event（最近 3-5 个）

### 2.3 去重机制

**发送端**:

- 维护历史窗口（最近 5 个 Event）
- seq 单调递增，溢出后从 0 重新开始

**接收端**:

- Packet 去重：基于 `seq`，HashSet 存储已处理的 seq
- Event 去重：基于 `id`，HashSet 存储已处理的 id

### 2.4 排序机制

基于 Event 的 `timestamp` 或 `id` 排序后交付上层。

## 3. 技术选型

| 类别     | 选择       | 理由             |
| -------- | ---------- | ---------------- |
| 编码格式 | JSON       | 易调试、跨语言   |
| 冗余间隔 | 20ms       | 平衡延迟和可靠性 |
| 历史窗口 | 5 个 Event | 覆盖常见丢包场景 |

## 4. 关键约束

- seq 序列号: 64 位整数，避免溢出
- Event id: 全局唯一性要求（UUID 或分布式 ID）
- 去重集合需要过期清理机制
- 历史窗口大小需可配置
- 并发安全要求

## 5. 注意事项

- 时钟偏移可能影响排序，考虑逻辑时钟方案
- 网络抖动可能导致包乱序
- 高频发送需控制 Packet 大小，避免超过 MTU

```

---

## 常见问题

**Q: 何时使用 add.md，何时使用 extract.md？**

A:
- **add.md**: 用户已经整理好内容，直接创建 Context
- **extract.md**: 用户提供原始材料（技术方案、讨论记录），需要 AI 提取关键信息

**Q: 如何避免重复创建 Context？**

A: **添加前必须先检查**！
1. 使用 `@prompts/context/search.md` 搜索相关主题
2. **如果是公约类型内容**：
   - ❌ 不创建新的 Global Context 文件
   - ✅ 使用 `@prompts/context/update.md` 更新已有的 4 个 Global Context 文件
3. Epic Context 应引用 global Context，而非复制内容
4. 原则：**Global Context 固定 4 个，Epic Context 可自由创建**

**Q: Global Context 为什么固定为 4 个文件？**

A: 
- **避免文件碎片化**：所有公约类型内容集中管理
- **便于查找和维护**：4 个文件覆盖所有全局规范
- **减少上下文冗余**：Task 加载时只需这 4 个核心文件
- **归类原则**：
  - 架构/设计/部署/API 约定 → `Architecture.md`
  - 技术选型/工具/框架 → `Tech_Stack.md`
  - 编码规范/最佳实践 → `Coding_Standard_{Language}.md`
  - 测试方法/策略 → `Testing_Strategy.md`

**Q: 如果需要添加安全规范、性能优化等内容怎么办？**

A: 归入已有的 4 个文件：
- 安全规范 → 更新 `Architecture.md` 添加"安全设计"章节
- 性能优化 → 更新 `Coding_Standard_{Language}.md` 添加"性能优化"章节
- 部署方案 → 更新 `Architecture.md` 添加"部署架构"章节
- API 约定 → 更新 `Architecture.md` 添加"API 设计约定"章节

**Q: 如何判断 Context 是 global 还是 epic？**

A:
- **Global**: 多个 Epic 都会用到 → **必须归入 4 个固定文件**
- **Epic**: 仅特定 Epic 使用 → **可以自由创建新文件**

**Q: 一个主题应该创建一个 Context 还是多个？**

A: 根据主题复杂度：
- 简单主题（如 "Go 编码规范"）: 一个 Context
- 复杂主题（如 "微服务架构 + gRPC 协议 + 数据模型"）: 拆分为多个 Context

**Q: Context 内容应该多详细？**

A: 足够让 AI 理解设计意图即可：
- ✅ 包含：设计决策、技术选型理由、接口约定、架构原则
- ❌ 不包含：项目背景故事、冗长的讨论过程、显而易见的常识、具体实现细节

---

现在，请根据用户提供的信息创建 Context 文档。

**提醒**: 创建前先使用 `@prompts/context/search.md` 检查是否已有相关 Context！
