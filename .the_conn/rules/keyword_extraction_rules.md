# 关键词提取规范

本规范定义了从需求、Story、或任务描述中提取技术关键词的标准化流程，供所有 Playbook 统一使用。

---

## 适用场景

本规范适用于以下场景的关键词提取：

1. **需求评审**（requirements_review.md）：从需求文档中提取关键词，用于搜索相关 Context
2. **Task 生成**（task_generation.md）：从 Story 中提取关键词，用于搜索相关 Context
3. **Context 添加**（context/add.md）：从技术方案中提取关键词，用于搜索是否已有相关 Context
4. **快速变更**（quick_change.md）：从变更描述中提取关键词，用于定位相关模块

---

## 提取规则（6 层）

### 规则 1: 多层次提取

从不同部分提取关键词：

| 提取源          | 关键词类型 | 示例                                                 |
| --------------- | ---------- | ---------------------------------------------------- |
| **标题/主题**   | 核心功能词 | "Create_Structure" → ["structure", "create", "init"] |
| **描述/需求**   | 功能关键词 | "目录创建" → ["directory", "folder", "filesystem"]   |
| **技术要点**    | 技术术语   | "使用 pathlib" → ["pathlib", "path", "file"]         |
| **标签/分类**   | 领域标签   | tags: ["cli", "init"] → ["cli", "init"]              |
| **依赖关系**    | 关联功能   | depends_on: STORY-01 → 读取 STORY-01 的关键词        |

### 规则 2: 技术术语优先

优先选择具有技术含义的关键词：

| 优先级 | 关键词类型  | 示例                                   |
| ------ | ----------- | -------------------------------------- |
| **高** | 框架/库名称 | pathlib, asyncio, gRPC, Redis          |
| **高** | 架构模式    | microservices, event-driven, REST      |
| **高** | 技术领域    | authentication, caching, queue         |
| **中** | 功能模块    | user-management, payment, notification |
| **中** | 数据结构    | tree, graph, hash-table                |
| **低** | 通用动词    | create, update, delete                 |

### 规则 3: 英文关键词提取

如果内容为中文，需要提取对应的英文技术术语：

| 中文     | 英文关键词                        |
| -------- | --------------------------------- |
| 用户认证 | authentication, auth, user, login |
| 缓存管理 | cache, caching, redis, memory     |
| 消息队列 | queue, message, mq, kafka         |
| 数据库   | database, db, sql, nosql          |
| API 接口 | api, rest, graphql, endpoint      |

### 规则 4: 关键词归一化

统一关键词格式：

- 全部转为小写
- 使用单数形式（除非复数有特殊含义）
- 去除连字符和下划线
- 保留技术术语的标准拼写

**示例**：
```
原始词: "User-Management", "APIs", "data_models"
归一化: "user management", "api", "data model"
```

### 规则 5: 关键词数量控制

- **最少**: 3 个关键词
- **推荐**: 4-6 个关键词
- **最多**: 8 个关键词

### 规则 6: 排除通用词

排除以下通用词（除非有特殊含义）：

- 通用动词: create, update, delete, read, write
- 通用名词: file, data, system, module, function
- 修饰词: new, old, simple, complex

**除非**这些词与技术术语结合（如 "file system", "data model", "create index"）

---

## 提取步骤（5步）

### Step 1: 初步提取

从各个部分提取所有可能的关键词（10-15 个）

**示例**：
```markdown
输入: "实现用户认证模块，使用 JWT Token 验证"

初步提取:
- 标题: ["user", "authentication", "module"]
- 描述: ["JWT", "token", "verification"]
- 技术: ["auth", "security"]

初步结果: ["user", "authentication", "module", "JWT", "token", "verification", "auth", "security"]
```

### Step 2: 优先级排序

按照"规则 2: 技术术语优先"对关键词排序

**示例**：
```markdown
排序结果:
1. 🔴 高优先级: JWT, authentication, token (技术术语)
2. 🟡 中优先级: user, auth, security (功能模块)
3. ⚪ 低优先级: module, verification (通用词)
```

### Step 3: 归一化

应用"规则 4: 关键词归一化"统一格式

**示例**：
```markdown
归一化前: ["User", "Authentication", "JWT-Token"]
归一化后: ["user", "authentication", "jwt token"]
```

### Step 4: 去重与精简

- 去除重复词
- 去除通用词
- 保留 4-6 个最具代表性的关键词

**示例**：
```markdown
精简前: ["user", "authentication", "jwt token", "auth", "security", "module", "verification"]
去重: ["user", "authentication", "jwt token", "security"] (移除 "auth"重复, "module", "verification"通用词)
精简后: ["authentication", "jwt token", "user", "security"]
```

### Step 5: 验证

检查关键词是否能准确描述内容的技术特征

**验证清单**：
- [ ] 关键词数量在 3-6 个之间
- [ ] 至少包含 2 个技术术语（高优先级）
- [ ] 没有重复或近义词
- [ ] 没有通用词（除非有特殊含义）
- [ ] 能够代表内容的核心技术特征

---

## 提取模板

### 模板 1: 需求评审场景

```markdown
## 关键词提取记录

**输入内容**: {需求描述}

### Step 1: 初步提取

| 提取源 | 原始词                  | 归一化后                |
| ------ | ----------------------- | ----------------------- |
| 标题   | {词1, 词2}              | {词1-norm, 词2-norm}    |
| 需求   | {词3, 词4}              | {词3-norm, 词4-norm}    |
| 技术点 | {词5, 词6}              | {词5-norm, 词6-norm}    |

### Step 2: 优先级排序

1. 🔴 高优先级: {词A}, {词B} (框架/架构/技术领域)
2. 🟡 中优先级: {词C}, {词D} (功能模块/数据结构)
3. ⚪ 低优先级: {词E}, {词F} (通用词)

### Step 3: 最终关键词列表

```json
["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"]
```

### Step 4: 验证说明

{为什么选择这些关键词？它们能否准确描述内容的技术特征？}
```

### 模板 2: Task 生成场景

```markdown
## 关键词提取记录（Story 分析）

**Story 标题**: {Story 标题}
**Story 类型**: {type: dev / e2e_test / bug_fix}

### Step 1: 初步提取

| 提取源   | 原始词 | 归一化后   |
| -------- | ------ | ---------- |
| 标题     | {词1}  | {词1-norm} |
| 验收标准 | {词2}  | {词2-norm} |
| 技术要点 | {词3}  | {词3-norm} |
| 标签     | {词4}  | {词4-norm} |

### Step 2: 优先级排序

1. 🔴 高优先级: {技术术语列表}
2. 🟡 中优先级: {功能模块列表}
3. ⚪ 低优先级: {通用词列表}

### Step 3: 最终关键词列表

```json
["keyword1", "keyword2", "keyword3", "keyword4"]
```

### Step 4: 验证说明

这 {N} 个关键词准确描述了 Story 的技术特征：
- {keyword1}: {为什么选择}
- {keyword2}: {为什么选择}
- ...
```

---

## 完整示例

### 示例 1: 需求评审 - 用户认证系统

**输入内容**:
```
需求: 实现用户认证系统
描述: 支持用户注册、登录、JWT Token 验证，使用 Redis 缓存会话
技术栈: Python + Flask + Redis
```

**提取过程**:

```markdown
### Step 1: 初步提取

| 提取源 | 原始词                                  | 归一化后                          |
| ------ | --------------------------------------- | --------------------------------- |
| 标题   | User, Authentication, System            | user, authentication, system      |
| 描述   | Register, Login, JWT, Token, Redis, Session | register, login, jwt, token, redis, session |
| 技术栈 | Python, Flask, Redis                    | python, flask, redis              |

### Step 2: 优先级排序

1. 🔴 高优先级: authentication, jwt, redis, flask (技术术语)
2. 🟡 中优先级: user, login, session (功能模块)
3. ⚪ 低优先级: system, register, token (通用词或重复)

### Step 3: 最终关键词列表

```json
["authentication", "jwt", "redis", "flask", "user", "session"]
```

### Step 4: 验证说明

这 6 个关键词准确描述了需求的技术特征：
- authentication: 核心功能领域
- jwt: 认证方案
- redis: 缓存技术
- flask: Web 框架
- user: 功能模块
- session: 会话管理
```

### 示例 2: Task 生成 - 创建项目结构

**Story 标题**: "创建 The Conn 框架的标准目录结构"

**Story 内容**:
```yaml
---
title: 创建 The Conn 框架的标准目录结构
type: dev
tags:
  - initialization
  - project-structure
  - cli
---

验收标准:
- 创建 `.the_conn/` 目录
- 创建 `tests/bdd/features/` 目录

技术要点:
- 使用 `pathlib` 处理路径
- 实现幂等性（重复执行不报错）
```

**提取过程**:

```markdown
### Step 1: 初步提取

| 提取源   | 原始词                                 | 归一化后                               |
| -------- | -------------------------------------- | -------------------------------------- |
| 标题     | Create, Structure                      | create, structure                      |
| 验收标准 | directory, tests, bdd, features        | directory, test, bdd, feature          |
| 技术要点 | pathlib, idempotent                    | pathlib, idempotent                    |
| 标签     | initialization, project-structure, cli | initialization, project structure, cli |

### Step 2: 优先级排序

1. 🔴 高优先级: pathlib, cli, bdd (技术术语)
2. 🟡 中优先级: initialization, project structure (功能模块)
3. ⚪ 低优先级: create, directory (通用词)

### Step 3: 最终关键词列表

```json
["pathlib", "cli", "bdd", "initialization", "project structure"]
```

### Step 4: 验证说明

这 5 个关键词准确描述了 Story 的技术特征：
- pathlib: 核心技术栈（路径处理）
- cli: 交互方式（命令行工具）
- bdd: 测试策略（行为驱动开发）
- initialization: 功能领域（初始化）
- project structure: 核心目标（项目结构）
```

---

## 常见错误

### 错误 1: 关键词过多

❌ **错误示例**:
```json
["user", "authentication", "login", "register", "jwt", "token", "redis", "cache", "session", "flask", "python", "api"]
```
- 问题: 12 个关键词，超过推荐范围（4-6 个）
- 影响: 搜索结果过于宽泛，噪音增多

✅ **正确示例**:
```json
["authentication", "jwt", "redis", "flask", "session"]
```
- 5 个关键词，覆盖核心技术特征

### 错误 2: 通用词过多

❌ **错误示例**:
```json
["create", "implement", "system", "module", "function"]
```
- 问题: 都是通用词，没有技术特征
- 影响: 无法精确定位相关 Context

✅ **正确示例**:
```json
["authentication", "jwt", "redis", "user management"]
```
- 技术术语为主，能够精确描述功能

### 错误 3: 中英文混用

❌ **错误示例**:
```json
["用户认证", "authentication", "JWT", "缓存"]
```
- 问题: 中英文混用，无法统一匹配
- 影响: 搜索效率降低

✅ **正确示例**:
```json
["authentication", "jwt", "cache", "user"]
```
- 统一使用英文技术术语

### 错误 4: 未归一化

❌ **错误示例**:
```json
["User-Management", "APIs", "data_models", "Authentication"]
```
- 问题: 格式不统一（连字符、下划线、大小写）
- 影响: 匹配失败

✅ **正确示例**:
```json
["user management", "api", "data model", "authentication"]
```
- 统一格式（小写、空格分隔）

---

## 最佳实践

1. **优先提取技术术语**：框架、库、架构模式比通用词更有价值
2. **保持关键词数量适中**：4-6 个关键词是最佳范围
3. **使用标准英文术语**：便于跨语言项目复用
4. **验证覆盖度**：确保关键词能代表内容的核心特征
5. **记录提取过程**：便于后续审查和优化

---

现在，请根据本规范提取关键词。

