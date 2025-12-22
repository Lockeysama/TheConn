# Task 生成指南

你是一位注重工程质量的技术领航员。你的任务是将 Story 转化为可执行的 Task 简报，**根据 Story 的 type 字段**指导 AI 使用合适的开发流程：

- **E2E Story (`type: e2e_test`)** → BDD 测试先行 + 迭代修复
- **普通 Story (`type: dev`)** → 单元测试先行（TDD）+ 迭代修复
- **Bug Fix Story (`type: bug_fix`)** → 单元测试 + 回归测试 + 迭代修复

**重要**：
- 通过检查 Story 的 `type` 字段判断测试策略，不要自行判断
- Task 必须包含明确的**测试执行与迭代修复**流程，确保交付给领航员的代码已通过所有测试
- 修复测试失败时只能修改业务代码，严禁为了通过测试而修改测试本身

---

## 输入

用户会提供：

- Story 文件（包含 frontmatter、验收标准和技术要点）


## 输出要求

### 1. 输出目录路径

```text
.the_conn/ai_workspace/EPIC-{序号}/TASK-{序号}_STORY-{序号}_{PascalCaseName}/
```

**示例**: `.the_conn/ai_workspace/EPIC-01/TASK-01_STORY-01_Create_Structure/`

### 2. 命名与格式规范

**ID 命名规则**：

- **格式**: `TASK-{序号}`
- **序号**: Epic 内顺序编号，两位数字，从 01 开始
- **说明**: Task ID 按 Epic 内执行顺序递增，一个 Story 可能对应多个 Task
- **示例**:

```text
TASK-01 → STORY-01 (首次开发)
TASK-02 → STORY-01 (补充测试)
TASK-03 → STORY-02 (首次开发)
TASK-04 → STORY-02.1 (Bug 修复)
```

**目录命名规则**：

- **格式**: `TASK-{序号}_STORY-{序号}_{PascalCaseName}/`
- **PascalCase**: 每个单词首字母大写，无分隔符
- **示例**: `TASK-01_STORY-01_Create_Structure/`

### 3. Task 粒度控制 ⚠️

**重要原则**: 避免过分细分 Task，以免浪费 tokens 和降低效率。

**推荐粒度**:

- ✅ **1 Story = 1 Task**（默认，适用于大多数情况）
- ✅ **1 Story = 2-3 Tasks**（仅在必要时拆分）

**何时拆分 Task**:

- Story 工作量超过 3 天
- Story 包含明显独立的子任务
- Story 的不同部分可以并行开发

**何时不拆分**:

- ❌ 不要为"写测试"和"写代码"分别创建 Task
- ❌ 不要为每个小函数创建单独的 Task
- ❌ 不要过度细分导致 Task 数量激增


## 输出文件

在输出目录下生成两个文件：

### 1. context.manifest.json

**生成前必须执行上下文分析流程（见下方"上下文分析流程"章节）**

```json
{
  "task_id": "TASK-{序号}",
  "story_id": "STORY-{序号}",
  "epic": "EPIC-{序号}",
  "feature": "FEAT-{序号}",
  "description": "{任务简要描述}",
  "contexts": [
    ".the_conn/context/global/Architecture.md",
    ".the_conn/context/epics/EPIC-{序号}/Module_Design_XXX.md"
  ],
  "source_story": ".the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{Name}/stories/STORY-{序号}_{Name}.md"
}
```

### 2. task.md

**根据 Story 的 `type` 字段生成相应的 Task 简报：**

**判断依据**：

- 检查 Story 的 frontmatter 中的 `type` 字段
- 如果 `type: e2e_test` → 使用"格式 A: E2E Story (BDD 测试)"
- 如果 `type: dev` → 使用"格式 B: 普通 Story (单元测试)"
- 如果 `type: bug_fix` → 使用"格式 B: 普通 Story (单元测试)"

**重要**：
- ✅ task.md 只包含任务目标、验收标准、开发流程、技术要点、工作范围
- ❌ 不要包含"参考资料"、"上下文文件列表"等已在 context.manifest.json 中定义的信息
- ❌ 不要复制 base_rules.md 或其他公约文件的内容（执行时会自动加载）

#### 格式 A：E2E Story（使用 BDD 测试）

```markdown
# Task 简报: [TASK-{序号}] {任务名称}

**关联 Story**: STORY-{序号}
**Story 类型**: E2E 测试 (`type: e2e_test`)
**测试策略**: BDD 场景驱动

## 1. 核心目标

{用 1-2 句话概括任务目标}

## 2. 验收标准 (BDD Scenarios)

你必须实现能让以下 Gherkin 场景通过的测试代码。这些场景定义了你的工作的"完成标准"。

```gherkin
{从 Story 复制的 BDD 场景}
```

## 3. 开发流程 (BDD 测试先行)

⚠️ **重要**: 请严格按照以下顺序执行，测试先行！

### Step 1: 创建 BDD 特性文件

- 在 `tests/bdd/features/{module}/` 下创建 `.feature` 文件
- 将上述 Gherkin 场景写入文件

### Step 2: 实现 Step Definitions

- 创建对应的测试文件（如 `tests/bdd/{name}_test.go`）
- 实现每个步骤的测试逻辑
- 此时运行测试应该 **失败**（因为被测试的模块还不存在）

### Step 3: 实现被测试的功能模块

- 根据测试需求实现业务代码
- 编写最少的代码使所有 BDD 测试通过
- 遵循 KISS 原则，不要过度设计

### Step 4: 测试执行与迭代修复

⚠️ **关键迭代环节**：此步骤可能需要多次循环，直到所有测试通过

**4.1 首次测试执行**
- 运行所有 BDD 测试
- 记录所有失败的测试用例和错误信息

**4.2 失败分析与修复**

如果测试失败，必须遵循以下原则：

✅ **正确做法**：
- 分析测试失败的根本原因（逻辑错误、边界条件、异常处理等）
- 修改**业务代码**以符合测试预期
- 确保修复不偏离原始的测试目的和验收标准
- 保持代码简洁，不过度设计

❌ **严格禁止**：
- 为了让测试通过而修改测试代码（除非测试本身写错了）
- 修改 Gherkin 场景以"适应"错误的实现
- 绕过测试逻辑或添加特殊处理使测试"看起来"通过
- 注释掉失败的测试用例

**4.3 迭代循环**

重复以下流程直到所有测试通过：
1. 执行测试 → 2. 分析失败原因 → 3. 修复代码 → 4. 再次执行测试

**4.4 测试全通过后的验证**
- 确保所有 BDD 场景都是绿色通过
- 检查代码是否符合 KISS 原则
- 检查是否有遗漏的边界条件

### Step 5: 重构与质量检查

**仅在所有测试通过后**才进行重构：
- 优化代码结构，消除重复
- 改善命名和可读性
- 运行 linter 检查代码质量
- **每次重构后必须重新运行测试**，确保功能未被破坏

## 4. 技术实现要点

{从 Story 提取的技术要点}

## 5. 工作范围与边界

### 需要创建

{文件列表}

### 需要创建的测试

- BDD Feature 文件: `tests/bdd/features/{module}/{name}.feature`
- Step Definitions: `tests/bdd/{name}_test.{ext}`

### 绝对禁止

{禁止修改的范围}

## 6. 任务闭环流程

**重要**: 任务开发完成后，需要经过人工 Review 确认，然后执行以下闭环步骤：

### Step 6: 生成变更摘要

**执行时机**: 用户 Review 代码并确认通过后

使用 Prompt: `@prompts/execution/change_summary.md`

生成本次任务的完整变更摘要：

- 记录所有新增/修改的文件
- 记录 BDD 测试结果（包含最终的测试通过状态）
- 记录依赖变更
- 记录测试迭代过程中的主要修复点
- 提供清晰的文件变更列表

输出文件: `.the_conn/ai_workspace/EPIC-{序号}/TASK-{序号}_STORY-{序号}_{Name}/change_summary.md`

### Step 7: 同步 Story

**执行时机**: 变更摘要生成后

使用 Prompt: `@prompts/execution/story_sync.md`

更新原始 Story 文档：

- 将 `status` 字段更新为 `done`
- 同步 BDD 场景与实际测试代码
- 同步"涉及文件"列表与实际创建的文件
- 确保验收标准的预期结果与代码实现完全匹配

更新文件: `.the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{Name}/stories/STORY-{序号}_{Name}.md`

```

**注意**：不要在 task.md 中包含"参考资料"或"上下文文件"列表，这些信息已经在 `context.manifest.json` 中定义，执行时会自动加载。

---

#### 格式 B：普通 Story（使用单元测试）

```markdown
# Task 简报: [TASK-{序号}] {任务名称}

**关联 Story**: STORY-{序号}
**Story 类型**: 普通 Story (`type: dev` 或 `type: bug_fix`)
**测试策略**: 单元测试驱动（TDD）

## 1. 核心目标

{用 1-2 句话概括任务目标}

## 2. 验收标准（功能清单）

完成以下功能要求：

{从 Story 复制的功能清单}

## 3. 开发流程 (TDD 测试先行)

⚠️ **重要**: 请严格按照以下顺序执行，测试先行！

### Step 1: 创建单元测试
- 根据编程语言习惯创建测试文件
  - Go: 与源代码同目录，`*_test.go`
  - Python: `tests/` 目录下，`test_*.py`
  - 其他语言按语言习惯
- 编写覆盖核心逻辑的单元测试
- 根据验收清单编写测试用例
- 此时运行测试应该 **失败**（因为业务代码还不存在）

### Step 2: 实现业务代码
- 编写最少的代码使所有测试通过
- 遵循 KISS 原则，不要过度设计
- 确保满足验收清单的所有功能要求

### Step 3: 测试执行与迭代修复

⚠️ **关键迭代环节**：此步骤可能需要多次循环，直到所有测试通过

**3.1 首次测试执行**
- 运行所有单元测试
- 记录所有失败的测试用例和错误信息

**3.2 失败分析与修复**

如果测试失败，必须遵循以下原则：

✅ **正确做法**：
- 分析测试失败的根本原因（逻辑错误、边界条件、异常处理等）
- 修改**业务代码**以符合测试预期
- 确保修复不偏离原始的测试目的和验收标准
- 保持代码简洁，不过度设计

❌ **严格禁止**：
- 为了让测试通过而修改测试代码（除非测试本身写错了）
- 修改验收标准以"适应"错误的实现
- 绕过测试逻辑或添加特殊处理使测试"看起来"通过
- 注释掉失败的测试用例

**3.3 迭代循环**

重复以下流程直到所有测试通过：
1. 执行测试 → 2. 分析失败原因 → 3. 修复代码 → 4. 再次执行测试

**3.4 测试全通过后的验证**
- 确保所有单元测试都是绿色通过
- 检查代码覆盖率是否符合要求
- 检查是否有遗漏的边界条件

### Step 4: 重构与质量检查

**仅在所有测试通过后**才进行重构：
- 运行 linter 检查代码质量并修复所有问题
- 优化代码结构，消除重复
- 改善命名和可读性
- 如果有性能要求，运行性能测试验证
- **每次重构后必须重新运行测试**，确保功能未被破坏

## 4. 技术实现要点

{从 Story 提取的技术要点}

## 5. 工作范围与边界

### 需要创建
{文件列表}

### 需要创建的测试
- 单元测试文件（按语言习惯组织）

### 绝对禁止
{禁止修改的范围}

## 6. 任务闭环流程

**重要**: 任务开发完成后，需要经过人工 Review 确认，然后执行以下闭环步骤：

### Step 5: 生成变更摘要

**执行时机**: 用户 Review 代码并确认通过后

使用 Prompt: `@prompts/execution/change_summary.md`

生成本次任务的完整变更摘要：
- 记录所有新增/修改的文件
- 记录单元测试结果（包含最终的测试通过状态）
- 记录依赖变更
- 记录测试迭代过程中的主要修复点
- 提供清晰的文件变更列表

输出文件: `.the_conn/ai_workspace/EPIC-{序号}/TASK-{序号}_STORY-{序号}_{Name}/change_summary.md`

### Step 6: 同步 Story

**执行时机**: 变更摘要生成后

使用 Prompt: `@prompts/execution/story_sync.md`

更新原始 Story 文档：
- 将 `status` 字段更新为 `done`
- 同步功能清单完成状态
- 同步"涉及文件"列表与实际创建的文件
- 确保验收标准与代码实现完全匹配

更新文件: `.the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{Name}/stories/STORY-{序号}_{Name}.md`

```

**注意**：不要在 task.md 中包含"参考资料"或"上下文文件"列表，这些信息已经在 `context.manifest.json` 中定义，执行时会自动加载。

---

## 生成原则

1. **类型判断准确**：必须检查 Story 的 `type` 字段，不要猜测
2. **测试先行**：开发流程必须强调先写测试、后写实现
3. **测试迭代必要性**：必须包含明确的测试-修复迭代流程，确保交付的代码通过所有测试
4. **验收驱动**：Story 的验收标准是任务完成的唯一标准，测试失败时修改代码而非测试
5. **上下文精准**：manifest 只包含真正需要的文件
6. **边界明确**：清晰列出"禁止"范围，避免 AI 越界
7. **避免重复**：不要在 task.md 中重复 context.manifest.json 中的信息（如上下文文件列表、原始 Story 路径等）


## 上下文分析流程

**在生成 `context.manifest.json` 之前，必须执行以下分析流程：**

### Phase 1: Story 内容分析

仔细阅读用户提供的 Story，提取以下关键信息：

1. **功能领域识别**: 该 Story 涉及哪些功能模块？（如：协议层、传输层、缓存、调度等）
2. **技术关键词提取**: 从验收标准和技术要点中提取关键技术术语
3. **依赖关系识别**: 该 Story 是否依赖其他 Story 或现有模块？

---

## 技术关键词提取（标准化流程）

**⚠️ 重要**: 关键词提取直接影响 Context 搜索精度，必须遵循标准流程


### 提取规则

#### 规则 1: 多层次提取

从 Story 的不同部分提取关键词：

| 提取源          | 关键词类型 | 示例                                                 |
| --------------- | ---------- | ---------------------------------------------------- |
| **Story 标题**  | 核心功能词 | "Create_Structure" → ["structure", "create", "init"] |
| **验收标准**    | 功能关键词 | "目录创建" → ["directory", "folder", "filesystem"]   |
| **技术要点**    | 技术术语   | "使用 pathlib" → ["pathlib", "path", "file"]         |
| **Frontmatter** | 标签和类型 | tags: ["cli", "init"] → ["cli", "init"]              |
| **依赖 Story**  | 关联功能   | depends_on: STORY-01 → 读取 STORY-01 的关键词        |

#### 规则 2: 技术术语优先

优先选择具有技术含义的关键词：

| 优先级 | 关键词类型  | 示例                                   |
| ------ | ----------- | -------------------------------------- |
| **高** | 框架/库名称 | pathlib, asyncio, gRPC, Redis          |
| **高** | 架构模式    | microservices, event-driven, REST      |
| **高** | 技术领域    | authentication, caching, queue         |
| **中** | 功能模块    | user-management, payment, notification |
| **中** | 数据结构    | tree, graph, hash-table                |
| **低** | 通用动词    | create, update, delete                 |

#### 规则 3: 英文关键词提取

如果 Story 内容为中文，需要提取对应的英文技术术语：

| 中文     | 英文关键词                        |
| -------- | --------------------------------- |
| 用户认证 | authentication, auth, user, login |
| 缓存管理 | cache, caching, redis, memory     |
| 消息队列 | queue, message, mq, kafka         |
| 数据库   | database, db, sql, nosql          |
| API 接口 | api, rest, graphql, endpoint      |

#### 规则 4: 关键词归一化

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

#### 规则 5: 关键词数量控制

- **最少**: 3 个关键词
- **推荐**: 4-6 个关键词
- **最多**: 8 个关键词

#### 规则 6: 排除通用词

排除以下通用词（除非有特殊含义）：

- 通用动词: create, update, delete, read, write
- 通用名词: file, data, system, module, function
- 修饰词: new, old, simple, complex

**除非**这些词与技术术语结合（如 "file system", "data model", "create index"）

### 提取步骤

#### Step 1: 初步提取

从 Story 的各个部分提取所有可能的关键词（10-15 个）

**Step 2: 优先级排序**

按照"规则 2: 技术术语优先"对关键词排序

#### Step 3: 归一化

应用"规则 4: 关键词归一化"统一格式

#### Step 4: 去重与精简

- 去除重复词
- 去除通用词
- 保留 4-6 个最具代表性的关键词

#### Step 5: 验证

检查关键词是否能准确描述 Story 的技术特征

### 提取模板

```markdown
## 关键词提取记录

#### Step 1: 初步提取

| 提取源   | 原始词 | 归一化后   |
| -------- | ------ | ---------- |
| 标题     | {词1}  | {词1-norm} |
| 验收标准 | {词2}  | {词2-norm} |
| 技术要点 | {词3}  | {词3-norm} |
| 标签     | {词4}  | {词4-norm} |

#### Step 2: 优先级排序

1. 🔴 高优先级: {词A}, {词B} (框架/架构/技术领域)
2. 🟡 中优先级: {词C}, {词D} (功能模块/数据结构)
3. ⚪ 低优先级: {词E}, {词F} (通用词)

#### Step 3: 最终关键词列表

```json
["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"]
```

#### Step 4: 验证说明

{为什么选择这些关键词？它们能否准确描述 Story 的技术特征？}
```

### 示例

**输入 Story**: STORY-01_Create_Structure

```yaml
---
title: 创建 The Conn 框架的标准目录结构
type: dev
tags:
  - initialization
  - project-structure
  - cli
---
```

**验收标准**:
- 创建 `.the_conn/` 目录
- 创建 `tests/bdd/features/` 目录

**技术要点**:
- 使用 `pathlib` 处理路径
- 实现幂等性（重复执行不报错）

**提取过程**:

```markdown
## 关键词提取记录

#### Step 1: 初步提取

| 提取源   | 原始词                                 | 归一化后                               |
| -------- | -------------------------------------- | -------------------------------------- |
| 标题     | Create, Structure                      | create, structure                      |
| 验收标准 | directory, tests, bdd, features        | directory, test, bdd, feature          |
| 技术要点 | pathlib, idempotent                    | pathlib, idempotent                    |
| 标签     | initialization, project-structure, cli | initialization, project structure, cli |

#### Step 2: 优先级排序

1. 🔴 高优先级: pathlib, cli, bdd (技术术语)
2. 🟡 中优先级: initialization, project structure (功能模块)
3. ⚪ 低优先级: create, directory (通用词)

#### Step 3: 最终关键词列表

```json
["pathlib", "cli", "bdd", "initialization", "project structure"]
```

#### Step 4: 验证说明

这 5 个关键词准确描述了 Story 的技术特征：

- pathlib: 核心技术栈
- cli: 交互方式
- bdd: 测试策略
- initialization: 功能领域
- project structure: 核心目标
```

### Phase 2: Context 文件搜索

**优先使用 Context 搜索工具**:

调用 `@playbooks/context/search.md` 搜索相关 Context

**输入参数**:
- **关键词**: {从 Phase 1 提取的技术关键词数组}
- **任务类型**: task_generation
- **Epic**: {Story 所属 Epic ID}
- **类型过滤**（可选）: 根据 Story 类型指定（如 `module_design`, `architecture` 等）

**返回结果示例**:
```json
{
  "contexts": [
    ".the_conn/context/global/Architecture.md",
    ".the_conn/context/global/Tech_Stack.md",
    ".the_conn/context/epics/EPIC-01/Module_Design_Auth.md"
  ],
  "total": 3
}
```

将返回的 Context 文件路径直接用于 `context.manifest.json` 的 `contexts` 数组。

---

**备选方案**：如果未使用搜索工具，手动扫描 `.the_conn/context/` 目录，根据 Phase 1 的分析结果匹配相关文件：

**扫描路径**:

1. `.the_conn/context/global/` - 公共 Context
2. `.the_conn/context/epics/EPIC-{序号}/` - Epic 专属 Context

**匹配规则（分级加载）**:

#### 级别 1：核心 Global Context（几乎总是包含）

| Context 文件                    | 包含条件  | 理由             |
| ------------------------------- | --------- | ---------------- |
| `Architecture.md`               | 所有 Task | 理解系统整体设计 |
| `Coding_Standard_{Language}.md` | 所有 Task | 确保代码风格一致 |

#### 级别 2：按 Story 类型包含

| Context 文件          | 包含条件                                | 理由                        |
| --------------------- | --------------------------------------- | --------------------------- |
| `Testing_Strategy.md` | Story type 为 `e2e_test` 或 `perf_test` | 测试相关 Story 需要测试策略 |
| `Tech_Stack.md`       | Story type 为 `dev` 且涉及技术选型      | 了解可用的技术栈            |

#### 级别 3：按功能领域包含

| 匹配规则                 | 示例                                                         |
| ------------------------ | ------------------------------------------------------------ |
| 文件名包含功能领域关键词 | Story 涉及 "DataStream" → 包含 `Module_Design_DataStream.md` |
| Frontmatter type 匹配    | Story 涉及模块设计 → 包含 `type: module_design` 的文档       |

**排除规则**：

- ❌ 不引用测试文件：排除 `*_test.*`, `tests/*`

### Phase 3: 相关代码文件识别

分析 Story 可能需要修改或参考的现有代码：

1. **直接相关代码**: Story 明确提到要修改的文件
2. **接口依赖代码**: 需要实现或调用的接口定义文件
3. **模型/类型定义**: 相关的数据结构定义文件
4. **测试参考**: 类似功能的现有测试文件（作为编写风格参考）

### Phase 4: 文件列表整合

将以上分析结果整合到 `contexts` 数组中，按以下优先级排序：

1. **核心 Global Context** - 几乎总是需要
   - `Architecture.md`
   - `Coding_Standard_{Language}.md`

2. **按需 Global Context** - 根据 Story 类型和领域
   - `Testing_Strategy.md` (E2E/性能测试 Story)
   - `Tech_Stack.md` (涉及技术选型)
   - 其他领域特定的 Global Context

3. **Epic Context** (`.the_conn/context/epics/EPIC-{序号}/*.md`) - Epic 专属设计

4. **接口定义** (`src/**/interfaces.*`, `src/**/types.*` 等)

5. **相关实现代码** (直接相关的源码文件)

6. **依赖 Story** (如果 Story 依赖其他 Story，包含前置 Story 文件)

**注意**:

- ✅ 只包含真正需要的文件，避免信息过载（通常 4-8 个文件）
- ✅ 每个文件的包含都应有明确理由
- ✅ 不要盲目包含所有 Global Context，按需选择
- ✅ 估算上下文大小：Global (2-3 个) + Epic (1-2 个) + 代码 (2-3 个) = 5-8 个文件


## 示例

### 示例 1: 普通 Story 的 Task

**输入**: Story 文件 `STORY-01_Create_Structure.md` (type: dev)

**输出**:

**目录**: `.the_conn/ai_workspace/EPIC-01/TASK-01_STORY-01_Create_Structure/`

**context.manifest.json**:

```json
{
  "task_id": "TASK-01",
  "story_id": "STORY-01",
  "epic": "EPIC-01",
  "feature": "FEAT-01",
  "description": "创建 The Conn 框架的标准目录结构",
  "contexts": [
    ".the_conn/context/global/Architecture.md",
    ".the_conn/context/global/Coding_Standard_Python.md",
    ".the_conn/context/epics/EPIC-01/Module_Design_Init.md"
  ],
  "source_story": ".the_conn/epics/EPIC-01_Base_Init/features/FEAT-01_Init_Project/stories/STORY-01_Create_Structure.md"
}
```

### 示例 2: E2E Story 的 Task

**输入**: Story 文件 `STORY-99_E2E_Auth_Flow.md` (type: e2e_test)

**输出**:

**目录**: `.the_conn/ai_workspace/EPIC-01/TASK-05_STORY-99_E2E_Auth_Flow/`

**context.manifest.json**:

```json
{
  "task_id": "TASK-05",
  "story_id": "STORY-99",
  "epic": "EPIC-01",
  "feature": "FEAT-01",
  "description": "E2E 测试：验证用户认证完整流程",
  "contexts": [
    ".the_conn/context/global/Architecture.md",
    ".the_conn/context/global/Testing_Strategy.md",
    ".the_conn/context/epics/EPIC-01/Module_Design_Auth.md",
    ".the_conn/epics/EPIC-01_Auth/features/FEAT-01_User_Auth/stories/STORY-01_Register.md",
    ".the_conn/epics/EPIC-01_Auth/features/FEAT-01_User_Auth/stories/STORY-02_Login.md"
  ],
  "source_story": ".the_conn/epics/EPIC-01_Auth/features/FEAT-01_User_Auth/stories/STORY-99_E2E_Auth_Flow.md"
}
```

---

## 执行检查点

### ✓ 检查点 1: Story 内容分析完成

**已完成**:

- [x] 功能领域识别
- [x] 技术关键词提取（使用标准化流程）
- [x] 依赖关系识别

**产出**:

- 功能领域清单
- 关键词列表（4-6 个）
- 依赖 Story 列表

**下一步**: Context 文件搜索


### ✓ 检查点 2: Context 搜索完成

**已完成**:

- [x] 调用 context/search.md
- [x] 获取相关 Context 文件列表
- [x] 按优先级排序

**产出**:

- Context 文件路径列表

**下一步**: 文件列表整合


### ✓ 检查点 3: 文件列表整合完成

**已完成**:

- [x] 整合 Global Context
- [x] 整合 Epic Context
- [x] 整合接口定义文件
- [x] 整合依赖 Story 文件
- [x] 估算上下文大小（5-8 个文件）

**产出**:

- 完整的 `contexts` 数组

**下一步**: 生成 context.manifest.json


### ✓ 检查点 4: context.manifest.json 生成完成

**已完成**:

- [x] 生成 JSON 文件
- [x] 填写所有必填字段
- [x] 包含完整的 contexts 数组

**产出**:

- `.the_conn/ai_workspace/EPIC-{序号}/TASK-{序号}_STORY-{序号}_{Name}/context.manifest.json`

**下一步**: 生成 task.md


### ✓ 检查点 5: task.md 生成完成

**已完成**:

- [x] 判断 Story type（e2e_test / dev / bug_fix）
- [x] 选择对应的 Task 格式（格式 A / 格式 B）
- [x] 填写核心目标
- [x] 填写验收标准
- [x] 填写开发流程（包含测试迭代）
- [x] 填写技术实现要点
- [x] 填写工作范围与边界
- [x] 填写任务闭环流程

**产出**:

- `.the_conn/ai_workspace/EPIC-{序号}/TASK-{序号}_STORY-{序号}_{Name}/task.md`

**质量检查**:

- [ ] task.md 包含明确的测试执行与迭代修复流程
- [ ] task.md 强调了"测试先行"原则
- [ ] task.md 禁止了为通过测试而修改测试代码
- [ ] task.md 没有包含重复信息（如上下文文件列表）

**任务完成**


现在，请根据用户提供的 Story 生成 Task 简报。
