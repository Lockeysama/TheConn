# Context 提取指南

从技术方案、需求文档或架构讨论中提取关键设计信息，生成 Context 文档。

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

适用于整个项目的通用知识，所有 Epic 都可引用。

| Type               | 说明         | 典型文件名              |
| ------------------ | ------------ | ----------------------- |
| `architecture`     | 系统架构     | `Architecture.md`       |
| `tech_stack`       | 技术栈       | `Tech_Stack.md`         |
| `coding_standard`  | 编码规范     | `Coding_Standard_Go.md` |
| `testing_strategy` | 测试策略     | `Testing_Strategy.md`   |
| `deployment`       | 部署方案     | `Deployment.md`         |
| `api_convention`   | API 约定     | `API_Convention.md`     |
| `domain_model`     | 核心领域模型 | `Domain_Model.md`       |

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

### Step 2: 确定 Context 类型和路径

根据分析结果，确定：
- **Type**: 从枚举中选择最匹配的类型
- **Scope**: global 或 epic:EPIC-XX
- **Descriptor**: 如何简洁准确地描述这个 Context

### Step 3: 提取核心内容

**提取原则**:
1. **聚焦决策**: 记录"为什么这样设计"，而非显而易见的细节
2. **保持精简**: 只包含 AI 完成任务必需的信息
3. **结构清晰**: 使用标题层级组织内容
4. **技术准确**: 使用准确的技术术语，避免模糊描述

**避免提取**:
- 项目背景和动机（应在 Epic/Story 中描述）
- 实现细节的逐行解释
- 显而易见的常识性内容
- 与开发任务无关的讨论过程

### Step 4: 组织内容结构

根据 Context 类型使用对应的模板（见下方"内容结构模板"）。

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

## 4. 接口设计（如适用）

{API 签名、函数定义、数据结构}

## 5. 实施要点

- {关键实现细节1}
- {关键实现细节2}

## 6. 注意事项

- {约束、限制、已知问题}
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

## 4. 实施要点

- 每个服务独立部署，独立数据库
- 使用 Protobuf 定义服务接口
- 网关层处理认证和限流

## 5. 注意事项

- 服务间调用需要超时控制（建议 3s）
- gRPC 调用失败需要降级策略
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

## 4. 实施要点

- 历史窗口大小: 5 个事件（可配置）
- 冗余间隔: 20ms（可配置）
- seq 生成: 单调递增，溢出后从 0 开始
- Event id: 全局唯一（UUID 或递增 ID）

## 5. 注意事项

- 历史窗口需要并发安全（使用 mutex）
- 去重哈希表需要定期清理，避免内存泄漏
- timestamp 依赖系统时钟，需考虑时钟偏移
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

---

现在，请根据用户提供的材料提取 Context 文档。
