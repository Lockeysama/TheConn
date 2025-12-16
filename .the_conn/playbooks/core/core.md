# AI 领航员的敏捷工作流

## 引言

本 playbook 为采用 AI 辅助开发的团队，提供了一套端到端的人机协作工作流。它将人类工程师的战略洞察与 AI 的编码执行能力相结合，通过结构化、版本化的项目管理流程，实现高效的开发协作。

---

## 第一部分：核心原则

1. **意图与实现的分离**: 人类领航员定义"做什么"（意图），AI 编码引擎负责"怎么做"（实现）。

2. **规划即代码 (Planning as Code)**: 所有规划（Epics, Features, Stories）都作为 Markdown 文件存放在代码库中，与源代码同步版本化管理。

3. **上下文精准投喂**: 通过清单机制，为每个任务动态组合最相关的上下文，避免信息过载，提升 AI 输出的准确性。

4. **双向同步**: 不仅从"意图"驱动"实现"，也要在"实现"完成后，将变更同步回"意图"，确保文档与代码的持续一致。

5. **用户文档保护**: `.the_conn/docs/` 目录下的所有文档（README.md、GUIDE.md）是用户使用文档，任何 AI Playbook **严格禁止修改** `docs/` 目录中的任何文件。

---

## 第二部分：项目目录结构

```
my_project/
├── .the_conn/                  # [The Conn 框架完整工作区]
│   ├── docs/                   # [文档层] 用户文档（AI 禁止修改）
│   │   ├── README.md           # 框架使用说明
│   │   └── GUIDE.md            # 详细使用指南
│   │
│   ├── epics/                  # [规划层] 所有规划文档
│   │   └── EPIC-01_Base_Init/
│   │       ├── README.md
│   │       └── features/
│   │           └── FEAT-01_Init_Project/
│   │               ├── README.md
│   │               └── stories/
│   │                   ├── STORY-01_Create_Structure.md
│   │                   └── STORY-01.1_Fix_Bug.md
│   │
│   ├── context/                # [知识层] 项目上下文知识库
│   │   ├── global/             # 公共 Context（全局共享）
│   │   │   ├── Architecture.md
│   │   │   ├── Tech_Stack.md
│   │   │   ├── Coding_Standard_Go.md
│   │   │   └── Testing_Strategy.md
│   │   └── epics/              # Epic 专属 Context
│   │       ├── EPIC-01/
│   │       │   ├── Module_Design_Core.md
│   │       │   └── Integration_Plan.md
│   │       └── EPIC-02/
│   │           └── Module_Design_DataStream.md
│   │
│   ├── playbooks/              # [工具层] AI 操作剧本
│   │   ├── core/
│   │   │   └── core.md
│   │   ├── initialization/
│   │   │   └── project_init.md
│   │   ├── context/
│   │   │   ├── extract.md
│   │   │   ├── add.md
│   │   │   └── update.md
│   │   ├── planning/
│   │   │   ├── requirements_review.md
│   │   │   ├── epic_planning.md
│   │   │   ├── feature_planning.md
│   │   │   ├── story_writing.md
│   │   │   └── bug_fix_story.md
│   │   └── execution/
│   │       ├── task_generation.md
│   │       ├── story_sync.md
│   │       └── change_summary.md
│   │
│   └── ai_workspace/           # [执行层] AI 任务工作区（临时，可 .gitignore）
│       └── EPIC-01/
│           ├── TASK-01_STORY-01_Create_Structure/
│           │   ├── task.md
│           │   ├── context.manifest.json
│           │   └── change_summary.md
│           └── TASK-02_STORY-01_Add_Tests/
│
├── src/                        # [实现层] 项目源代码
│
└── tests/                      # [验证层] 所有测试代码
    ├── bdd/
    │   ├── features/           # BDD Gherkin 特性文件
    │   └── step_defs/
    └── unit/
```

---

## 第三部分：四阶段工作流程

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

## 第四部分：关键概念与约定

### ID 命名规范

| 类型    | 格式                    | 示例         | 说明                    |
| ------- | ----------------------- | ------------ | ----------------------- |
| Epic    | `EPIC-{序号}`           | `EPIC-01`    | 全局唯一，从 01 开始    |
| Feature | `FEAT-{序号}`           | `FEAT-01`    | Epic 内唯一，从 01 开始 |
| Story   | `STORY-{序号}`          | `STORY-01`   | Epic 内唯一，从 01 开始 |
| Bug Fix | `STORY-{序号}.{子序号}` | `STORY-01.1` | Bug Fix 继承父 Story ID |
| Task    | `TASK-{序号}`           | `TASK-01`    | Epic 内顺序编号         |

### 文件命名规范

**规则**: `{ID}_{PascalCaseName}.md`

| 类型         | 示例                                 |
| ------------ | ------------------------------------ |
| Epic 目录    | `EPIC-01_Base_Init/`                 |
| Feature 目录 | `FEAT-01_Init_Project/`              |
| Story 文件   | `STORY-01_Create_Structure.md`       |
| Bug Fix 文件 | `STORY-01.1_Fix_Permission.md`       |
| Task 目录    | `TASK-01_STORY-01_Create_Structure/` |
| Context 文件 | `Module_Design_DataStream.md`        |

### Story 类型与状态

**Type (类型)**:
- `dev` - 新功能开发
- `bug_fix` - 缺陷修复

**Status (状态)**:
- `pending` - 未完成
- `done` - 已完成

### Context 类型枚举

**Global Context Types**:
- `architecture` - 系统架构
- `tech_stack` - 技术栈
- `coding_standard` - 编码规范
- `testing_strategy` - 测试策略
- `deployment` - 部署方案
- `api_convention` - API 约定
- `domain_model` - 核心领域模型

**Epic Context Types**:
- `module_design` - 模块设计
- `data_model` - 数据模型
- `api_spec` - API 规范
- `integration` - 集成方案
- `algorithm` - 算法说明
- `protocol` - 协议设计
- `migration` - 迁移方案

### Task 与 Story 关系

**关系类型**:
- **1:1** - 正常场景：一个 Story → 一个 Task（首次开发）
- **1:N** - 迭代场景：一个 Story → 多个 Task（开发 + 优化 + Bug 修复）

**示例**:
```
STORY-01 → TASK-01 (首次开发)
        → TASK-02 (补充测试)
        → TASK-04 (Bug 修复)
STORY-02 → TASK-03 (首次开发)
```

---

## 附录：Playbook 索引

### 🚀 统一命令入口（推荐使用）

| 用途             | 文件路径              | 说明                                        |
| ---------------- | --------------------- | ------------------------------------------- |
| **统一命令入口** | `playbooks/tc.md`     | 通过 @tc 命令路由到所有 playbooks，新手友好 |
| 快速开始指南     | `docs/QUICK_START.md` | @tc 命令的快速参考指南                      |
| 命令参考手册     | `docs/COMMANDS.md`    | 完整的命令列表和详细说明                    |

**推荐使用方式**：

使用 `@tc.md` 命令而不是直接 @ 具体的 playbook 文件：

```bash
# 在 AI IDE 中使用 @ 符号引用 tc.md 文件
# 一级快捷命令
@tc.md init                    # 代替 @initialization/project_init.md
@tc.md story 用户登录          # 代替 @planning/story_writing.md
@tc.md next                    # 代替 @planning/next_step_advisor.md
@tc.md status                  # 代替 @planning/project_status.md

# 二级命令
@tc.md plan breakdown          # 代替 @planning/requirements_breakdown.md
@tc.md ctx add                 # 代替 @context/add.md
@tc.md exec task STORY-01      # 代替 @execution/task_generation.md

# 使用缩写
@tc.md plan bd                 # breakdown 的缩写
@tc.md plan s 用户注册         # story 的缩写
@tc.md ctx a                   # add 的缩写
```

**命令结构**：
```
@tc.md <模块> <命令> [参数]
```

**支持的模块**：
- `plan` - 规划模块（epic, feature, story, status, next 等）
- `ctx` - 上下文管理模块（add, update, search, extract）
- `exec` - 执行模块（task, sync, summary）

详见：`docs/QUICK_START.md` 和 `docs/COMMANDS.md`

### 核心规范文件

| 用途           | 文件                          |
| -------------- | ----------------------------- |
| 基础公约       | `core/base_rules.md`          |
| 测试策略规范   | `core/test_strategy_rules.md` |
| 复杂度评估规范 | `core/complexity_rules.md`    |
| BDD 语言配置   | `core/bdd_language_rules.md`  |

**说明**：命名规范已内嵌到各规划 Playbook 中（`epic_planning.md`、`feature_planning.md`、`story_writing.md`、`task_generation.md`、`context/add.md`）

### 初始化 Playbooks

| 用途       | Playbook 文件                    |
| ---------- | -------------------------------- |
| 项目初始化 | `initialization/project_init.md` |

### 规划层 Playbooks

| 用途                 | Playbook 文件                        |
| -------------------- | ------------------------------------ |
| 需求与方案评审       | `planning/requirements_review.md`    |
| 需求拆解（批量生成） | `planning/requirements_breakdown.md` |
| 需求变更管理         | `planning/requirements_change.md`    |
| 项目状态查看         | `planning/project_status.md`         |
| 生成 Epic            | `planning/epic_planning.md`          |
| 生成 Feature         | `planning/feature_planning.md`       |
| 生成 Story           | `planning/story_writing.md`          |
| 生成 Bug Fix Story   | `planning/bug_fix_story.md`          |
| **下一步行动建议**   | `planning/next_step_advisor.md`      |

### Context 管理 Playbooks

| 用途              | Playbook 文件        |
| ----------------- | -------------------- |
| 提取 Context 文档 | `context/extract.md` |
| 添加 Context 文档 | `context/add.md`     |
| 更新 Context 文档 | `context/update.md`  |
| 搜索 Context 文档 | `context/search.md`  |

### 执行层 Playbooks

| 用途           | Playbook 文件                  |
| -------------- | ------------------------------ |
| 生成 Task 简报 | `execution/task_generation.md` |
| 同步 Story     | `execution/story_sync.md`      |
| 生成变更摘要   | `execution/change_summary.md`  |
