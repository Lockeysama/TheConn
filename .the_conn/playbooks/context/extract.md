# Context 提取指南

从技术方案、需求文档或架构讨论中提取关键设计信息，生成 Context 文档。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

## 本 Playbook 的工作范围

**专注于**：

- ✅ **提取设计**：从材料中提取设计决策和架构信息
- ✅ **生成 Context 文档**：创建设计文档
- ✅ **使用代码片段**：通过代码片段说明设计（接口定义、数据结构、API 签名等）

**重要**：Context 文档是**设计文档**，关注"是什么"和"为什么"，严格避免实现逻辑细节。

---

## 输入

用户会提供：

- 技术方案文档
- 架构设计讨论
- 需求规范（PRD）
- 技术调研结果

---

## Context 类型系统

### 全局 Context (scope: global)

**⚠️ 重要：Global Context 固定为以下 4 个文件，不随意新增**

适用于整个项目的通用知识，所有 Epic 都可引用。

| Type               | 说明     | 固定文件名                      | 内容归类规则                                       |
| ------------------ | -------- | ------------------------------- | -------------------------------------------------- |
| `architecture`     | 系统架构 | `Architecture.md`               | 系统设计、模块关系、通信方式、架构原则等           |
| `tech_stack`       | 技术栈   | `Tech_Stack.md`                 | 语言、框架、工具、数据库、中间件等技术选型         |
| `coding_standard`  | 编码规范 | `Coding_Standard_{Language}.md` | 命名约定、错误处理、注释规范、最佳实践等           |
| `testing_strategy` | 测试策略 | `Testing_Strategy.md`           | 测试方法、覆盖率要求、BDD/TDD 策略、测试组织规范等 |

**公约归类原则**：
- ✅ 部署方案、API 约定、安全规范等 → 归入 `Architecture.md`
- ✅ 领域模型、数据模型通用规范 → 归入 `Architecture.md` 或 `Tech_Stack.md`
- ❌ 不创建新的 Global Context 文件（如 Deployment.md, API_Convention.md 等）
- 🔄 如需补充内容，使用 `@prompts/context/update.md` 更新已有文件

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
- `created`: 初次提取时的日期
- `updated`: 初次提取时与 `created` 相同
- `status`: 新提取的 Context 都是 `active`，过时后改为 `deprecated`
- `tags`: 可选但强烈推荐，有助于 Context 搜索

---

## 提取流程

### Step 1: 分析材料

阅读用户提供的材料，识别：

1. **知识类型**: 这是架构、设计、规范还是其他？
2. **作用范围**: 全局通用还是特定 Epic？
3. **关键决策**: 哪些设计决策需要记录？
4. **技术要点**: 哪些技术细节需要被后续任务引用？

### Step 2: 检查已有 Context（避免重复）

**重要**: 在提取新 Context 前，先检查已有的 Context，避免重复提取！

1. **查看全局 Context** (`.the_conn/context/global/`)：
   - 使用 `@prompts/context/search.md` 搜索相关 Context
   - 检查是否已有类似内容（如 Architecture.md、Tech_Stack.md 等）
   - 确认哪些内容已经在全局 Context 中

2. **查看 Epic Context** (`.the_conn/context/epics/EPIC-XX/`)（如果提取 Epic Context）：
   - 检查该 Epic 下是否已有相关 Context
   - 避免创建重复的 Context 文档

3. **判断是否需要提取**：
   - ✅ **需要提取**: 材料中包含**新的**设计决策、架构信息、接口约定
   - ❌ **无需提取**: 内容已在现有 Context 中覆盖
   - 🔄 **需要更新**: 内容与现有 Context 有重叠，但有新增或变化 → 使用 `@prompts/context/update.md`

### Step 3: 确定 Context 类型和作用域

**作用域判断原则**：

| 内容类型            | 作用域     | 归入文件                        | 说明                           |
| ------------------- | ---------- | ------------------------------- | ------------------------------ |
| 系统架构、设计原则  | **global** | `Architecture.md`               | 全项目通用的架构设计           |
| 部署方案、API 约定  | **global** | `Architecture.md`               | 作为架构的一部分归入           |
| 技术栈、工具选型    | **global** | `Tech_Stack.md`                 | 全项目通用的技术选择           |
| 编码规范、最佳实践  | **global** | `Coding_Standard_{Language}.md` | 全项目代码风格规范             |
| 测试策略、测试规范  | **global** | `Testing_Strategy.md`           | 全项目测试方法和组织           |
| 领域模型（跨 Epic） | **global** | `Architecture.md`               | 核心业务概念，作为架构的一部分 |
| 特定模块设计        | **epic**   | `Module_Design_XXX.md`          | 仅该 Epic 使用的模块           |
| Epic 专属数据模型   | **epic**   | `Data_Model_XXX.md`             | 仅该 Epic 使用的数据结构       |
| Epic 专属 API 规范  | **epic**   | `API_Spec_XXX.md`               | 仅该 Epic 的 API               |
| Epic 专属协议       | **epic**   | `Protocol_Design_XXX.md`        | 仅该 Epic 使用的通信协议       |
| Epic 专属算法       | **epic**   | `Algorithm_XXX.md`              | 仅该 Epic 使用的特殊算法       |

**⚠️ Global Context 更新优先规则**：

1. **判断是否属于 4 大公约类型**：
   - 架构/设计相关 → 更新 `Architecture.md`
   - 技术选型相关 → 更新 `Tech_Stack.md`
   - 编码规范相关 → 更新 `Coding_Standard_{Language}.md`
   - 测试策略相关 → 更新 `Testing_Strategy.md`

2. **不创建新的 Global Context 文件**：
   - ❌ 不创建 `Deployment.md`, `API_Convention.md`, `Security.md` 等
   - ✅ 这些内容应该归入已有的 4 个文件中
   - 🔄 使用 `@prompts/context/update.md` 更新已有文件

3. **Epic Context 自由创建**：
   - 特定 Epic 的专属设计可以自由创建新文件
   - 但要避免与 Global Context 重复

**判断标准**:

- 如果内容适用于**多个 Epic** 或**整个项目** → 归入 global 的 4 个文件之一
- 如果内容仅适用于**单个 Epic** → 创建 epic Context
- **公约类型的内容必须归入 global 的 4 个文件，不创建新文件**

根据分析结果，确定：

- **Type**: 从枚举中选择最匹配的类型
- **Scope**: global（更新已有 4 个文件）或 epic:EPIC-XX（创建新文件）
- **Descriptor**: 如何简洁准确地描述这个 Context（仅 Epic Context 需要）

### Step 4: 提取核心内容

**提取原则 - 关注"是什么"和"为什么"，而非"怎么做"**:

**避免重复原则**:

- 如果某些内容已在 global Context 中，Epic Context 应**引用而非复制**
- 在 Epic Context 中可以写："参考 Architecture.md 的微服务架构设计"
- 只提取该 Epic **独有的、差异化的**设计内容

1. **设计决策优先**: 记录"为什么这样设计"、"有哪些选择"、"为什么选这个方案"
2. **接口和边界**: 记录模块接口、数据格式、协议约定、边界职责
3. **约束和原则**: 记录设计约束、性能要求、安全要求、编码原则
4. **架构层面**: 记录组件关系、数据流向、依赖关系、通信方式
5. **保持抽象**: 停留在设计层面，不深入具体实现逻辑

**应该提取的内容**:

- ✅ 模块职责和边界（"用户认证模块负责..."）
- ✅ 接口定义（"API 接口格式为 JSON，字段包括..."）
- ✅ 设计约束（"单个文件不超过 1MB"）
- ✅ 架构决策（"采用事件驱动架构，因为..."）
- ✅ 数据模型（"用户表包含字段..."）
- ✅ 协议规范（"消息格式为..."）

**严格避免的内容**:

- ❌ 具体代码逻辑（"在第 10 行调用 xxx 函数"）
- ❌ 实现算法细节（"使用 for 循环遍历..."）
- ❌ 函数内部实现（"首先判断 x>0，然后..."）
- ❌ 变量命名和赋值（"定义变量 count = 0"）
- ❌ 错误处理细节（"catch 异常后打印日志"）
- ❌ 项目背景和动机（应在 Epic/Story 中）
- ❌ 显而易见的常识（"Python 是动态语言"）

### Step 5: 组织内容结构

根据 Context 类型使用对应的模板（见下方"内容结构模板"）。

**引用全局 Context 的方式**:
如果 Epic Context 需要依赖全局 Context，在文档开头说明：

```markdown
## 依赖的全局 Context

- `Architecture.md` - 微服务架构设计
- `Tech_Stack.md` - Go 技术栈
- `Coding_Standard_Go.md` - Go 编码规范

本文档假设读者已了解上述全局 Context，仅描述本 Epic 专属的设计。
```

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

## 提取原则

1. **类型准确**: 选择最准确的 type，不要强行归类
2. **范围合理**: 全局 Context 应该真正全局通用
3. **粒度适中**: 一个 Context 聚焦一个主题，不要过大或过小
4. **语言精炼**: 简洁明了，避免冗长描述
5. **及时更新**: 提取时标记 `created` 和 `updated`，后续更新使用 @prompts/context/update.md

---

## 示例

### 示例 1: 提取系统架构

**输入材料**（摘要）:
```

系统采用微服务架构：

- 用户服务（Go）
- 认证服务（Go + JWT）
- 数据服务（Go + PostgreSQL）
- 网关（Nginx）

服务间通信使用 gRPC，对外 API 使用 REST。

```

**提取结果**:

**文件**: `.the_conn/context/global/Architecture.md`

```markdown
---
type: architecture
scope: global
title: 系统架构设计
created: 2025-12-11
updated: 2025-12-11
status: active
tags:
  - microservices
  - grpc
  - rest
---

# 系统架构设计

## 1. 概述与目标

采用微服务架构，实现服务解耦和独立部署。

## 2. 核心设计

### 2.1 服务拆分

| 服务     | 语言  | 职责               |
| -------- | ----- | ------------------ |
| 用户服务 | Go    | 用户信息管理       |
| 认证服务 | Go    | JWT 令牌管理       |
| 数据服务 | Go    | 数据存储和查询     |
| 网关     | Nginx | 请求路由和负载均衡 |

### 2.2 通信方式

- **服务间通信**: gRPC（高性能、类型安全）
- **对外 API**: REST over HTTP（标准、易集成）

## 3. 技术选型

| 类别       | 选择       | 理由                |
| ---------- | ---------- | ------------------- |
| 服务语言   | Go         | 高性能、并发支持好  |
| 服务间通信 | gRPC       | 高效、类型安全      |
| 数据库     | PostgreSQL | 可靠性高、ACID 保证 |
| 网关       | Nginx      | 成熟稳定、配置灵活  |

## 4. 关键约束

- 每个服务独立部署，拥有独立数据库
- 服务间调用超时限制：3s
- 网关层负责认证和限流
- 禁止服务间直接访问数据库

## 5. 注意事项

- gRPC 调用需要设计降级策略
- 避免服务间循环依赖
```

---

### 示例 2: 提取模块设计

**输入材料**（摘要）:

```
DataStream 可靠传输模块设计：

核心思想：3次冗余 + Packet去重 + Event排序

发送端：
- 维护历史窗口（最近5个事件）
- 每个事件发送3次（T+0ms, T+20ms, T+40ms）
- 使用seq区分Packet

接收端：
- Packet去重（基于seq）
- Event去重（基于id）
- 排序后交付（基于timestamp）
```

**提取结果**:

**文件**: `.the_conn/context/epics/EPIC-02/Module_Design_DataStream.md`

```markdown
---
type: module_design
scope: epic:EPIC-02
title: DataStream 可靠传输模块设计
created: 2025-12-11
updated: 2025-12-11
status: active
tags:
  - udp
  - reliability
  - redundancy
---

# DataStream 可靠传输模块设计

## 1. 概述与目标

解决 UDP 丢包问题，实现 99.9% 事件到达率，低延迟（无 ACK 等待）。

## 2. 核心设计

### 2.1 冗余策略

每个事件发送 3 次：
- T+0ms: 首次发送
- T+20ms: 第1次冗余
- T+40ms: 第2次冗余

### 2.2 Packet 结构

```json
{
  "h": {
    "seq": 5001,        // Packet 序号
    "ts": 1699999001    // 时间戳
  },
  "d": [
    {"id": 101, "event": "..."}  // Event 列表
  ]
}
```

### 2.3 去重与排序

**Packet 去重**: 基于 `seq`，丢弃重复 Packet

**Event 去重**: 基于 `id`，保留最早收到的 Event

**排序**: 基于 `timestamp`，确保有序交付

## 3. 接口设计

### 3.1 发送端接口

```go
type Sender interface {
    Send(event Event) error
    GetHistoryWindow() []Event
}
```

### 3.2 接收端接口

```go
type Receiver interface {
    Receive() (Event, error)
    DeduplicateAndSort() []Event
}
```

## 4. 关键约束

- 历史窗口大小: 默认 5 个事件（可配置）
- 冗余发送间隔: 20ms（可配置）
- seq 序列号: 单调递增，64 位整数
- Event id: 全局唯一性要求
- 并发安全: 历史窗口需要线程安全

## 5. 注意事项

- 去重哈希表需要设计过期清理机制
- timestamp 可能存在时钟偏移问题
- 避免内存无限增长

```

---

## 常见问题

**Q: 何时创建 global Context，何时创建 epic Context？**

A: 
- **Global**: 适用于整个项目，多个 Epic 都会用到（如架构、编码规范）
- **Epic**: 仅该 Epic 使用，其他 Epic 不关心（如特定模块的设计）

**Q: 一个技术方案可以生成多个 Context 吗？**

A: 可以。如果方案包含多个主题（如架构 + 协议 + 数据模型），应拆分为多个 Context。

**Q: Context 内容多详细合适？**

A: 足够让 AI 完成开发任务即可。避免：
- 过于宏观（如"系统要高性能"）
- 过于细节（如"第10行代码这样写"）

**Q: 提取时发现材料不完整怎么办？**

A: 提示用户补充关键信息，或在 Context 中标注"待补充"，后续使用 @prompts/context/update.md 更新。

**Q: 如何避免重复提取 Context？**

A: **必须先检查已有 Context**！
1. 使用 `@prompts/context/search.md` 搜索相关主题
2. 如果内容已存在 global Context，Epic Context 应引用而非复制
3. 如果内容部分重叠，考虑更新现有 Context 而非创建新的
4. 原则：**优先复用全局 Context，Epic Context 只包含该 Epic 独有的内容**

**Q: 如何判断内容应该放在 global 还是 epic？**

A: 
- **global**: 适用于多个 Epic 或整个项目的通用知识
- **epic**: 仅适用于单个 Epic 的专属内容
- **有疑问时，优先选择 global**（便于复用，后续可重构）

---

现在，请根据用户提供的材料提取 Context 文档。

**提醒**: 提取前先使用 `@prompts/context/search.md` 检查是否已有相关 Context！
