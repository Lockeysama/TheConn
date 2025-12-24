# The Conn 使用指南

## 框架简介

The Conn 为采用 AI 辅助开发的团队提供了一套端到端的人机协作工作流。它将人类工程师的战略洞察与 AI 的编码执行能力相结合，通过结构化、版本化的项目管理流程，实现高效的开发协作。

## 核心设计原则

The Conn 框架基于以下五个核心原则设计：

1. **意图与实现的分离**: 人类领航员定义"做什么"（意图），AI 编码引擎负责"怎么做"（实现）。

2. **规划即代码 (Planning as Code)**: 所有规划（Epics, Features, Stories）都作为 Markdown 文件存放在代码库中，与源代码同步版本化管理。

3. **上下文精准投喂**: 通过清单机制，为每个任务动态组合最相关的上下文，避免信息过载，提升 AI 输出的准确性。

4. **双向同步**: 不仅从"意图"驱动"实现"，也要在"实现"完成后，将变更同步回"意图"，确保文档与代码的持续一致。

5. **用户文档保护**: `.the_conn/docs/` 目录下的所有文档是用户使用文档，任何 AI Playbook **严格禁止修改** `docs/` 目录中的任何文件。

---

## 工作流程概览

The Conn 框架将 AI 辅助开发分为四个阶段：

### 阶段一：战略规划与意图定义

在 `epics/` 目录下，将业务需求转化为结构化的 Markdown 文件。

1. **定义 Epic 与 Feature**: 通过 `README.md` 文件定义高阶的目标和功能模块。
2. **撰写 Story**: 在 `stories/` 目录下，为每个可开发任务创建详尽的 Story 文件。

### 阶段二：任务执行准备

为 AI 准备好所有执行材料。

1. **生成工作区**: 在 `.the_conn/ai_workspace/{TASK-ID}/` 下创建任务目录。
2. **准备上下文**: 创建 `context.manifest.json` 和 `task.md`。
3. **组装 Prompt**: 加载模板，填充上下文和任务简报，发送给 AI。

### 阶段三：代码实现与审查

AI 根据指令执行开发任务。

1. **AI 生成代码**: 根据 Story 中的 BDD 场景，创建测试和业务逻辑代码。
2. **提交 PR**: AI 将变更提交为 Pull Request。
3. **人类审查**: 领航员审查代码的逻辑、架构符合性。

### 阶段四：同步与闭环

PR 合并后，确保"意图"与"实现"的一致性。

1. **合并 PR**: 领航员将通过审查的 PR 合并。
2. **触发同步**: 使用同步模板更新 Story 文档。
3. **确认提交**: 领航员确认并提交 Story 的更新。

---

## 详细工作流程

### 流程零：项目初始化

**场景**: 首次使用 The Conn 框架，需要初始化项目结构和公共 Context。

**步骤**:

1. **项目初始化**：

   ```
   @playbooks/initialization/project_init.md 帮我初始化 The Conn 项目
   ```

   → 创建目录结构：`.the_conn/epics/`, `.the_conn/context/`, `.the_conn/ai_workspace/`

2. **定义初始公共 Context**：
   根据项目特点，创建必要的全局 Context：
   - `Architecture.md` - 系统架构
   - `Tech_Stack.md` - 技术栈
   - `Coding_Standard_{Language}.md` - 编码规范
   - `Testing_Strategy.md` - 测试策略

### 流程一：从需求到规划

**场景**: 收到外部需求文档（PRD、用户故事等），需要拆解为可执行的开发任务。

**步骤**:

#### 方案 A: 批量生成（推荐，快速高效）

1. **需求评审与拆解**：

   ```
   @{需求文档} @playbooks/planning/requirements_review.md 开始评审
   ```

   → 与 AI 讨论需求和技术方案，确认后自动触发批量生成

2. **提取 Context 文档**（规划完成后）：

   ```
   @{技术方案文档} @playbooks/context/add.md 帮我提取 Context 文档
   ```

   → 输出到 `.the_conn/context/global/` 或 `.the_conn/context/epics/EPIC-XX/`

3. **提取 Epic 专属 Context**（Epic 规划完成后）：

   ```
   @.the_conn/epics/EPIC-XX_Name/README.md @playbooks/context/add.md 帮我提取 Epic 专属 Context
   ```

   → 输出到 `.the_conn/context/epics/EPIC-XX/`
   → 包含模块设计、数据模型、API 规范等 Epic 专属的技术细节

#### 方案 B: 逐个生成（精细控制）

1. **需求评审**：

   ```
   @{需求文档} @playbooks/planning/requirements_review.md 开始评审
   ```

   → 与 AI 讨论需求和技术方案

2. **提取 Context 文档**：

   ```
   @{技术方案文档} @playbooks/context/add.md 帮我提取 Context 文档
   ```

   → 输出到 `.the_conn/context/global/` 或 `.the_conn/context/epics/EPIC-XX/`

3. **生成 Epic 规划**：

   ```
   @{需求文档} @playbooks/planning/epic_planning.md 帮我生成 Epic 规划
   ```

   → 输出到 `.the_conn/epics/EPIC-XX_Name/README.md`
   → AI 会自动处理 Epic 目录结构初始化

4. **生成 Feature 规划**：

   ```
   @{需求文档} @playbooks/planning/feature_planning.md 帮我生成 Feature 规划
   ```

   → 输出到 `.the_conn/epics/EPIC-XX_Name/features/FEAT-XX_Name/README.md`

5. **生成 Story**：

   ```
   # 生成普通 Story（功能开发）
   @{需求文档} @playbooks/planning/story_writing.md 帮我拆解为 Story
   
   # 生成 E2E Story（Feature 集成测试）
   @{Feature信息} @playbooks/planning/e2e_story.md 帮我生成 E2E Story
   
   # 生成性能测试 Story（性能验证）
   @{性能需求} @playbooks/planning/performance_test_story.md 帮我生成性能测试 Story
   
   # 生成快速变更 Story（小改进/Bug修复）
   @{变更描述} @playbooks/planning/quick_router.md 帮我创建快速变更
   ```

   → 输出到 `.the_conn/epics/.../stories/STORY-XX_Name.md`

6. **提取 Epic 专属 Context**（Epic 规划完成后）：

   ```
   @.the_conn/epics/EPIC-XX_Name/README.md @playbooks/context/add.md 帮我提取 Epic 专属 Context
   ```

   → 输出到 `.the_conn/context/epics/EPIC-XX/`

7. 审查 AI 生成的文档，确认后提交

### 流程二：从 Story 到 Task

**场景**: Story 已就绪，需要为 AI 准备任务执行材料。

**步骤**:

1. 使用 Playbook 生成任务简报：

   ```
   @{Story文件} @playbooks/execution/task_generation.md 帮我生成 Task
   ```

2. AI 会在 `.the_conn/ai_workspace/EPIC-XX/TASK-XX_STORY-XX_Name/` 下生成：
   - `task.md` - 任务简报（根据 Story type 决定测试策略）
     - E2E Story (`type: e2e_test`): BDD 测试先行
     - 普通 Story (`type: dev`): 单元测试先行（TDD）
   - `context.manifest.json` - 上下文清单

3. 审查生成的文件，补充必要的上下文引用

**注意**:

- Task ID 在 Epic 内顺序编号，一个 Story 可能对应多个 Task
- Task 生成会根据 Story 的 `type` 字段自动选择测试策略：
  - `type: dev` → 单元测试先行（TDD）
  - `type: e2e_test` → BDD 测试先行
  - `type: perf_test` → 性能测试
  - `type: bug_fix` → 单元测试 + 回归测试

### 流程三：执行开发任务

**场景**: Task 已准备好，开始 AI 辅助编码。

**步骤**:

1. 启动任务（使用 task_execution.md）：

   ```
   @.the_conn/ai_workspace/EPIC-XX/TASK-XX_STORY-XX_Name/ @playbooks/execution/task_execution.md 开始任务
   ```

2. AI 按测试策略执行：
   - **E2E Story** (`type: e2e_test`): 先创建 `.feature` 文件和 Step Definitions，再实现业务逻辑
   - **性能测试 Story** (`type: perf_test`): 先准备性能测试环境和脚本，再实现/优化业务代码
   - **普通/Bug Fix Story** (`type: dev`, `type: bug_fix`): 先创建单元测试，再实现业务逻辑使测试通过
   - 运行测试并迭代修复

3. **人工 Review 检查点** ⚠️：
   - AI 完成开发后会暂停并等待确认
   - 审查代码实现
   - 审查测试覆盖
   - 确认符合预期

4. 确认通过后，AI 自动执行任务闭环（Step 11-12）：

   ```
   用户输入：确认
   ```

   - AI 自动生成变更摘要（change_summary.md）
   - AI 自动同步 Story 状态（story_sync.md）

### 流程四：任务闭环

**场景**: 代码实现完成，需要同步文档并归档。

**步骤**:

**注意**: 如果在流程三执行了任务闭环（Step 6-7），则此步骤已自动完成，无需重复执行。

如果需要单独执行：

1. 生成变更摘要：

   ```
   @playbooks/execution/change_summary.md 生成本次任务的变更摘要
   ```

2. 同步 Story 文档：

   ```
   @{原始Story文件} @playbooks/execution/story_sync.md 开始同步
   ```

3. 审查并提交所有变更

### 流程五：Bug 修复

**场景**: 已完成的 Story 在测试或生产环境发现 Bug。

**步骤**:

1. 创建 Bug Fix Story：

   ```
   @playbooks/planning/bug_fix_story.md 帮我生成 Bug Fix Story
   
   父 Story: STORY-01
   发现于: 集成测试
   现象: ...
   ```

   → 输出到 `.the_conn/epics/.../stories/STORY-XX.X_Name.md`

2. 后续按流程二到流程四执行修复

---

## 模板速查

### 初始化 Playbooks

| Playbook                                   | 用途       | 输入     | 输出位置              |
| --- | --- | --- | --- |
| `playbooks/initialization/project_init.md` | 项目初始化 | 项目信息 | `.the_conn/` 目录结构 |

### Context 管理 Playbooks

| Playbook                      | 用途                   | 输入                   | 输出位置             |
| --- | --- | --- | --- |
| `playbooks/context/add.md`    | 添加/提取 Context 文档 | Context 内容或技术方案 | `.the_conn/context/` |
| `playbooks/context/update.md` | 更新 Context 文档      | Context 变更           | 更新现有 Context     |

### 规划层 Playbooks

| Playbook                                       | 用途                             | 输入              | 输出位置                        |
| --- | --- | --- | --- |
| `playbooks/planning/requirements_review.md`    | 需求评审（确认后自动触发拆解）   | 需求想法          | Epic+Feature+Story              |
| `playbooks/planning/requirements_breakdown.md` | 需求拆解（仅在review确认后触发） | 需求文档+技术方案 | Epic+Feature+Story              |
| `playbooks/planning/epic_planning.md`          | 生成 Epic 规划（含自动初始化）   | 需求文档          | `.the_conn/epics/EPIC-XX_Name/` |
| `playbooks/planning/epic_init.md`              | Epic 目录初始化（高级用法）      | Epic 信息         | Epic 目录结构                   |
| `playbooks/planning/feature_planning.md`       | 生成 Feature 规划                | 需求/Epic         | `.the_conn/epics/.../features/` |
| `playbooks/planning/story_writing.md`          | 生成普通 Story                   | 需求/Feature      | `.the_conn/epics/.../stories/`  |
| `playbooks/planning/e2e_story.md`              | 生成 E2E Story                   | Feature 信息      | `.the_conn/epics/.../stories/`  |
| `playbooks/planning/performance_test_story.md` | 生成性能测试 Story               | 性能需求          | `.the_conn/epics/.../stories/`  |
| `playbooks/planning/quick_router.md`           | 快速变更（智能路由）             | 变更描述          | `.the_conn/epics/.../stories/`  |

### 执行层 Playbooks

| Playbook                                 | 用途           | 输入              | 输出位置                  |
| --- | --- | --- | --- |
| `playbooks/execution/task_generation.md` | 生成 Task 简报 | Story 文件        | `.the_conn/ai_workspace/` |
| `playbooks/execution/task_execution.md`  | 执行 Task      | Task 工作目录     | 代码 + 测试               |
| `playbooks/execution/change_summary.md`  | 生成变更摘要   | 任务记录          | `.the_conn/ai_workspace/` |
| `playbooks/execution/story_sync.md`      | 同步 Story     | Story + 代码      | 更新原 Story              |

---

## 关键概念

### ID 命名规范

| 类型    | 格式                    | 示例         |
| --- | --- | --- |
| Epic    | `EPIC-{序号}`           | `EPIC-01`    |
| Feature | `FEAT-{序号}`           | `FEAT-01`    |
| Story   | `STORY-{序号}`          | `STORY-01`   |
| Bug Fix | `STORY-{序号}.{子序号}` | `STORY-01.1` |
| Task    | `TASK-{序号}`           | `TASK-01`    |

### Story 类型与状态

**Type (类型)**:
- `dev` - 新功能开发
- `bug_fix` - 缺陷修复
- `e2e_test` - E2E 集成测试
- `perf_test` - 性能测试

**Status (状态)**:
- `pending` - 未完成
- `done` - 已完成

### 文件命名规范

**格式**: `{ID}_{PascalCaseName}.md`

**示例**:

- Epic 目录: `EPIC-01_Base_Init/`
- Feature 目录: `FEAT-01_Init_Project/`
- Story 文件: `STORY-01_Create_Structure.md`
- Task 目录: `TASK-01_STORY-01_Create_Structure/`
- Context 文件: `Module_Design_DataStream.md`

---

## 目录约定

```
.the_conn/
├── epics/                              # 规划层
│   └── EPIC-01_Base_Init/
│       ├── README.md
│       └── features/
│           └── FEAT-01_Init_Project/
│               ├── README.md
│               └── stories/
│                   ├── STORY-01_Create_Structure.md
│                   └── STORY-01.1_Fix_Bug.md
│
├── context/                            # 知识层
│   ├── global/                         # 公共 Context
│   │   ├── Architecture.md
│   │   └── Tech_Stack.md
│   └── epics/                          # Epic 专属 Context
│       └── EPIC-01/
│           └── Module_Design_Core.md
│
├── rules/                              # 规则层（核心规则和约束）
│   ├── base_rules.md
│   ├── test_strategy_rules.md
│   ├── complexity_rules.md
│   └── bdd_language_rules.md
│
├── playbooks/                          # 工具层（AI 操作剧本）
│   ├── initialization/
│   ├── planning/
│   ├── context/
│   └── execution/
│
├── docs/                               # 用户文档（AI 严禁修改）
│   ├── README.md
│   └── GUIDE.md                        # 本文件
│
└── ai_workspace/                       # 执行层（临时工作区）
    └── EPIC-01/
        └── TASK-01_STORY-01_Create_Structure/
            ├── task.md
            ├── context.manifest.json
            └── change_summary.md
```

---

## 团队协作

### 版本控制

**提交到 Git**:
- `.the_conn/epics/` - 规划文档
- `.the_conn/context/` - Context 文档
- `src/`, `tests/` - 代码和测试

**不提交** (添加到 `.gitignore`):
```gitignore
.the_conn/ai_workspace/
.the_conn/playbooks/
.the_conn/docs/
*.log
*.tmp
```

### 分支策略

```
main
  ↓
epic/EPIC-01
  ↓
story/STORY-01 (可选)
```

### ID 冲突避免

在 Epic README.md 中维护 ID 分配表：

```markdown
## ID 分配记录

| 类型  | 下一个可用 ID | 最后分配者 | 更新时间   |
| --- | --- | --- | --- |
| Story | STORY-06      | @user1     | 2025-12-22 |
| Task  | TASK-08       | @user2     | 2025-12-22 |
```

### 协作检查清单

开始协作前：
- [ ] 定义分支策略
- [ ] 创建 `.gitignore`
- [ ] 设置 ID 分配记录表

每次提交前：
- [ ] 拉取最新代码
- [ ] 运行 `@tc.md sync` 更新 Story 状态
- [ ] 更新 ID 分配记录（如有新建）
