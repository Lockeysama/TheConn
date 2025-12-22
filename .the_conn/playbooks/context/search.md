# Context 搜索指南

帮助 AI 快速查找项目中相关的 Context 文档。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

**📋 规范引用**：

本 Playbook 依赖以下规范文件（AI 必须先加载）：
- **基础公约**: `@playbooks/core/base_rules.md` - 禁止事项、文件路径约定、质量标准

本 Playbook **不依赖**以下规范：
- ❌ `test_strategy_rules.md` - Context 搜索不涉及测试策略决策
- ❌ `bdd_language_rules.md` - Context 搜索不涉及 BDD

**原因**: context/search 只负责搜索 Context 文档，不涉及测试策略规划

## 本 Playbook 的工作范围

**专注于**：

- ✅ **搜索文档**：查找相关的 Context 文档
- ✅ **生成报告**：输出搜索结果

**重要**：此 Playbook 是只读的，不修改任何文档。

---

## 使用场景

1. **任务生成时**: 找到与当前 Story 相关的 Context
2. **需求评审时**: 查找现有的架构或设计文档
3. **Context 管理**: 检查是否已有类似的 Context
4. **依赖分析**: 找到某个模块相关的所有 Context

---

## 搜索策略

### Strategy 1: 按关键词搜索

**输入**: 关键词列表

**逻辑**:

1. 在 Context 文件名中搜索
2. 在 Context Frontmatter 的 `title` 和 `tags` 中搜索
3. 在 Context 正文的标题和关键段落中搜索

**示例**:

```
关键词: "authentication", "用户认证"
结果:
- Architecture_Auth.md (文件名匹配)
- Module_Design_User.md (tags: [authentication, user])
- API_Specification.md (正文提到 "authentication flow")
```

---

### Strategy 2: 按 Context 类型搜索

**输入**: Context 类型（architecture, module_design 等）

**逻辑**: 读取所有 Context 的 Frontmatter，筛选匹配 `type` 的文档

**示例**:

```
类型: architecture
结果:
- Architecture.md
- Architecture_Auth.md
- Architecture_DataFlow.md
```

---

### Strategy 3: 按 Epic 范围搜索

**输入**: Epic ID

**逻辑**:

1. 搜索 `context/epics/EPIC-XX/` 下的所有 Context
2. 搜索 `context/global/` 下 `scope: global` 的 Context

**示例**:

```
Epic: EPIC-01
结果:
- context/epics/EPIC-01/Module_Design_Core.md (Epic 专属)
- context/global/Architecture.md (全局，所有 Epic 可用)
- context/global/Tech_Stack.md (全局，所有 Epic 可用)
```

---

### Strategy 4: 按相关性评分搜索（智能推荐）

**输入**: Story 内容或 Task 描述

**逻辑**:

1. 提取 Story 的关键信息（目标、涉及文件、技术点）
2. 为每个 Context 计算相关性评分
3. 返回评分最高的 Top N 个 Context

**评分规则**:

```
基础分 = 0

# 文件名匹配
if Context 文件名包含 Story 中的关键词: +3 分

# Frontmatter 匹配
if Context.type 与 Story 需求匹配: +5 分
if Context.tags 包含 Story 关键词: +2 分/个
if Context.scope == "epic:{Story.epic}": +3 分

# Epic 匹配
if Context 在 Story 所属 Epic 目录下: +5 分

# 内容匹配
if Context 正文提到 Story 涉及的文件路径: +4 分
if Context 正文包含 Story 的技术关键词: +1 分/个

# 时效性（如果有 expires 或 status）
if Context.status == "deprecated": -10 分
if Context.expires < today: -5 分
```

**示例**:

```
Story: STORY-03 实现用户登录缓存
涉及文件: src/auth/cache.go

相关性评分:
1. Module_Design_Auth.md: 15 分
   - type: module_design (+5)
   - Epic 匹配 (+5)
   - tags: [auth, cache] (+4)
   - 文件名匹配 (+3)
   - 正文提到 cache.go (-2, 部分匹配)

2. Architecture.md: 8 分
   - type: architecture (+5)
   - scope: global (+0)
   - 正文提到 "caching strategy" (+3)

3. Coding_Standard_Go.md: 3 分
   - 文件名包含 "Go" (+3)

推荐: Module_Design_Auth.md (最相关)
```

---

## 输出格式

### 格式 1: 列表模式（默认）

```markdown
# Context 搜索结果

**搜索条件**: {关键词 / 类型 / Epic}
**找到**: {N} 个相关 Context

---

## 搜索结果

### 1. Architecture.md ⭐⭐⭐⭐⭐ (相关性: 95%)

**路径**: `.the_conn/context/global/Architecture.md`
**类型**: architecture
**范围**: global
**标签**: [system-design, microservices]
**创建**: 2025-12-01 | **更新**: 2025-12-10

**匹配原因**:
- 文件名包含搜索关键词 "Architecture"
- 正文提到 "authentication flow"

**摘要**: 
系统采用微服务架构，包含用户服务、认证服务、数据服务...

---

### 2. Module_Design_Auth.md ⭐⭐⭐⭐ (相关性: 85%)

**路径**: `.the_conn/context/epics/EPIC-01/Module_Design_Auth.md`
**类型**: module_design
**范围**: epic:EPIC-01
**标签**: [auth, jwt, session]
**创建**: 2025-12-05 | **更新**: 2025-12-11

**匹配原因**:
- Epic 匹配 (EPIC-01)
- 标签包含 "auth"
- 正文详细描述认证模块设计

**摘要**:
认证模块负责用户登录、Token 管理、权限校验...

---

### 3. Tech_Stack.md ⭐⭐⭐ (相关性: 60%)

...

---

## 建议

- **最相关**: Architecture.md, Module_Design_Auth.md（推荐优先阅读）
- **可选**: Tech_Stack.md（如需了解技术选型）
```

---

### 格式 2: 简洁模式

```markdown
# Context 搜索结果 (简洁)

找到 3 个相关 Context:

1. ⭐⭐⭐⭐⭐ Architecture.md (global)
2. ⭐⭐⭐⭐ Module_Design_Auth.md (epic:EPIC-01)
3. ⭐⭐⭐ Tech_Stack.md (global)
```

---

### 格式 3: 路径模式（用于批量读取）

```markdown
# Context 路径列表

.the_conn/context/global/Architecture.md
.the_conn/context/epics/EPIC-01/Module_Design_Auth.md
.the_conn/context/global/Tech_Stack.md
```

---

## 搜索参数

| 参数                 | 类型     | 说明                 | 示例                      |
| -------------------- | -------- | -------------------- | ------------------------- |
| `keywords`           | string[] | 关键词列表           | ["auth", "cache"]         |
| `type`               | string   | Context 类型         | "architecture"            |
| `epic`               | string   | Epic ID              | "EPIC-01"                 |
| `scope`              | string   | 范围                 | "global" / "epic"         |
| `limit`              | number   | 返回数量上限         | 5 (默认 10)               |
| `format`             | string   | 输出格式             | "list" / "brief" / "path" |
| `include_deprecated` | boolean  | 是否包含废弃 Context | false (默认)              |

---

## 高级搜索

### 组合条件

```markdown
搜索 EPIC-01 下所有架构相关的 Context:

参数:
- epic: "EPIC-01"
- type: "architecture"
- scope: "epic" (排除 global)
```

### 排除条件

```markdown
搜索所有有效的模块设计文档（排除废弃）:

参数:
- type: "module_design"
- include_deprecated: false
```

### 全文搜索

```markdown
在所有 Context 中搜索 "Redis" 相关内容:

参数:
- keywords: ["Redis"]
- search_in: ["filename", "frontmatter", "content"]
```

---

## 使用示例

### 示例 1: 为 Story 查找 Context

```
我正在处理 STORY-03（实现用户登录缓存）

@prompts/context/search.md 帮我找相关的 Context

关键词: ["登录", "缓存", "auth", "cache"]
Epic: EPIC-01
```

### 示例 2: 检查重复 Context

```
我准备创建一个关于数据库设计的 Context

@prompts/context/search.md 帮我检查是否已有类似 Context

关键词: ["数据库", "database", "schema"]
类型: "data_model"
```

### 示例 3: 查看 Epic 的所有 Context

```
@prompts/context/search.md 列出 EPIC-02 的所有 Context

Epic: EPIC-02
格式: list
```

---

## 在 Task Generation 中使用

在 `task_generation.md` 中，可以这样集成搜索：

```markdown
## Step 1: 搜索相关 Context

使用 @prompts/context/search.md：
- 关键词: {从 Story 中提取}
- Epic: {Story.epic}
- 类型: {根据 Story 需求推断}

根据搜索结果，选择相关性最高的 3-5 个 Context 加入 context.manifest.json
```

---

## 搜索优化建议

### 提高搜索准确性

1. **使用多个关键词**: 单个关键词可能过于宽泛
2. **指定 Epic**: 限制搜索范围，提高相关性
3. **排除废弃 Context**: 避免使用过时信息
4. **查看多个结果**: 不要只看第一个，综合判断

### 当搜索结果为空

如果没找到相关 Context：

1. 检查关键词是否过于具体
2. 尝试更通用的类型（如 architecture）
3. 搜索 global 范围的 Context
4. 考虑是否需要创建新 Context（使用 @prompts/context/add.md）

---

## 注意事项

1. **相关性非绝对**: 评分仅供参考，需结合实际判断
2. **Context 质量**: 搜索只能找到文档，不保证文档质量
3. **及时更新**: Context 过时会影响搜索准确性，定期使用 @prompts/context/update.md
4. **避免过度依赖**: 搜索是辅助工具，关键决策需人工判断

---

现在，请告诉我您要搜索什么，我将帮您找到相关的 Context 文档。
