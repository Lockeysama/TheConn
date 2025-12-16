# The Conn 操作手册

欢迎使用 The Conn 框架！本文档介绍如何使用 `@tc` 命令系统与 AI 协作，高效管理项目规划、开发和执行。

---

## 🚀 快速开始

### 使用 @tc.md 命令（推荐）

The Conn 提供了统一的命令入口 `@tc`，让你无需记住复杂的 Playbook 路径：

```bash
# 初始化项目
@tc.md init

# 创建规划
@tc.md epic 用户管理系统
@tc.md feature 用户认证
@tc.md story 登录功能

# 查看状态
@tc.md status
@tc.md next

# 生成任务
@tc.md task STORY-01
```

**详细文档**：

- 📘 [快速开始指南](QUICK_START.md) - 5 分钟上手
- 📗 [命令参考手册](COMMANDS.md) - 完整命令列表
- 📙 [命令映射表](COMMAND_MAPPING.md) - 命令与 Playbook 对照

### 传统方式（直接使用 Playbook）

如果你更习惯直接使用 Playbook 文件：

```bash
@playbooks/initialization/project_init.md
@playbooks/planning/story_writing.md
```

---

## 📚 @tc.md 命令体系

### 命令格式

```bash
@tc.md <模块> <命令> [参数]
```

或使用一级快捷命令：

```bash
@tc.md <命令> [参数]
```

### 主要模块

| 模块 | 说明 | 示例命令 |
|------|------|---------|
| **init** | 初始化 | `@tc.md init` |
| **plan** | 规划管理 | `@tc.md plan story`, `@tc.md plan status` |
| **ctx** | 上下文管理 | `@tc.md ctx add`, `@tc.md ctx search` |
| **exec** | 执行管理 | `@tc.md exec task`, `@tc.md exec sync` |
| **help** | 帮助系统 | `@tc.md help`, `@tc.md list` |

### 常用命令速查

| 功能 | @tc.md 命令 | 缩写 | Playbook 文件 |
|------|---------|------|--------------|
| **初始化** | `@tc.md init` | - | `initialization/project_init.md` |
| **项目状态** | `@tc.md status` | `@tc.md plan st` | `planning/project_status.md` |
| **下一步建议** | `@tc.md next` | `@tc.md plan n` | `planning/next_step_advisor.md` |
| **生成 Epic** | `@tc.md epic` | `@tc.md plan e` | `planning/epic_planning.md` |
| **生成 Feature** | `@tc.md feature` | `@tc.md plan f` | `planning/feature_planning.md` |
| **生成 Story** | `@tc.md story` | `@tc.md plan s` | `planning/story_writing.md` |
| **Bug 修复** | `@tc.md bugfix` | `@tc.md plan bf` | `planning/bug_fix_story.md` |
| **需求拆解** | `@tc.md plan breakdown` | `@tc.md plan bd` | `planning/requirements_breakdown.md` |
| **需求评审** | `@tc.md plan review` | `@tc.md plan rv` | `planning/requirements_review.md` |
| **需求变更** | `@tc.md plan change` | `@tc.md plan chg` | `planning/requirements_change.md` |
| **提取 Context** | `@tc.md ctx extract` | `@tc.md ctx e` | `context/extract.md` |
| **添加 Context** | `@tc.md ctx add` | `@tc.md ctx a` | `context/add.md` |
| **更新 Context** | `@tc.md ctx update` | `@tc.md ctx u` | `context/update.md` |
| **搜索 Context** | `@tc.md ctx search` | `@tc.md ctx s` | `context/search.md` |
| **生成 Task** | `@tc.md task` | `@tc.md exec t` | `execution/task_generation.md` |
| **同步 Story** | `@tc.md sync` | `@tc.md exec sy` | `execution/story_sync.md` |
| **变更摘要** | `@tc.md summary` | `@tc.md exec sum` | `execution/change_summary.md` |

完整命令列表请查看 [命令参考手册](COMMANDS.md)

---

## 📂 Playbooks 分类

### 统一入口

| 文件 | 用途 |
|------|------|
| `playbooks/tc.md` | **@tc.md 命令路由入口**（推荐使用）|

### 初始化 Playbooks

| Playbook 文件 | @tc.md 命令 | 用途 |
|--------------|---------|------|
| `playbooks/initialization/project_init.md` | `@tc.md init` | 初始化项目结构 |

### Context 管理 Playbooks

| Playbook 文件 | @tc.md 命令 | 用途 |
|--------------|---------|------|
| `playbooks/context/extract.md` | `@tc.md ctx extract` | 提取 Context 文档 |
| `playbooks/context/add.md` | `@tc.md ctx add` | 添加 Context 文档 |
| `playbooks/context/update.md` | `@tc.md ctx update` | 更新 Context 文档 |
| `playbooks/context/search.md` | `@tc.md ctx search` | 搜索 Context 文档 |

### 规划层 Playbooks

| Playbook 文件 | @tc.md 命令 | 用途 |
|--------------|---------|------|
| `playbooks/planning/requirements_review.md` | `@tc.md plan review` | 需求与方案评审 |
| `playbooks/planning/requirements_breakdown.md` | `@tc.md plan breakdown` | 批量生成规划 |
| `playbooks/planning/requirements_change.md` | `@tc.md plan change` | 需求变更管理 |
| `playbooks/planning/project_status.md` | `@tc.md status` | 项目状态查看 |
| `playbooks/planning/next_step_advisor.md` | `@tc.md next` | 下一步建议 |
| `playbooks/planning/epic_planning.md` | `@tc.md epic` | 生成 Epic |
| `playbooks/planning/feature_planning.md` | `@tc.md feature` | 生成 Feature |
| `playbooks/planning/story_writing.md` | `@tc.md story` | 生成 Story |
| `playbooks/planning/bug_fix_story.md` | `@tc.md bugfix` | 生成 Bug Fix |

### 执行层 Playbooks

| Playbook 文件 | @tc.md 命令 | 用途 |
|--------------|---------|------|
| `playbooks/execution/task_generation.md` | `@tc.md task` | 生成任务简报 |
| `playbooks/execution/story_sync.md` | `@tc.md sync` | 同步 Story |
| `playbooks/execution/change_summary.md` | `@tc.md summary` | 生成变更摘要 |

### 核心指南

| 文档 | 内容 |
|------|------|
| `playbooks/core/core.md` | AI 领航员敏捷工作流 |
| `playbooks/core/base_rules.md` | 基础公约与规则 |
| `playbooks/core/test_strategy_rules.md` | 测试策略规范 |
| `playbooks/core/complexity_rules.md` | 复杂度评估规范 |
| `playbooks/core/bdd_language_rules.md` | BDD 语言配置 |

---

## 🔄 工作流程图

### 标准开发流程（使用 @tc.md 命令）

```
0. 初始化阶段
   └── @tc.md init
                ↓
1. 评审阶段
   └── @tc.md plan review
                ↓
2. 规划阶段
   ├── @tc.md ctx extract → 提取 Context
   ├── 方案 A（批量规划 - 推荐）:
   │   └── @tc.md plan breakdown → 批量生成 Epic/Feature/Story
   └── 方案 B（逐个创建 - 精细控制）:
       ├── @tc.md epic 用户系统
       ├── @tc.md feature 用户认证
       └── @tc.md story 登录功能
                ↓
3. 查看状态
   ├── @tc.md status → 查看项目状态
   └── @tc.md next → 获取下一步建议
                ↓
4. 准备阶段
   └── @tc.md task STORY-01 → 生成任务简报
                ↓
5. 执行阶段
   ├── AI 执行开发和测试
   ├── 人工 Review 检查点 ⚠️
   └── @tc.md sync STORY-01 → 同步 Story 状态
```

### Bug Fix 流程（使用 @tc.md 命令）

```
Story 完成并合并
        ↓
   发现 Bug ❌
        ↓
1. 创建 Bug Fix Story
   └── @tc.md bugfix STORY-01 描述问题
        ↓
2. 生成 Task
   └── @tc.md task STORY-01.1
        ↓
3. 执行修复
   └── AI 执行修复和测试
        ↓
4. 同步更新
   └── @tc.md sync STORY-01.1
```

### 传统流程（直接使用 Playbook）

如果你更习惯使用 Playbook 路径：

```
0. 初始化: @playbooks/initialization/project_init.md
1. 评审: @playbooks/planning/requirements_review.md
2. 规划: @playbooks/planning/requirements_breakdown.md
3. 任务: @playbooks/execution/task_generation.md
4. 同步: @playbooks/execution/story_sync.md
```

---

## 关键概念

### ID 命名规范

| 类型    | 格式                    | 示例         |
| ------- | ----------------------- | ------------ |
| Epic    | `EPIC-{序号}`           | `EPIC-01`    |
| Feature | `FEAT-{序号}`           | `FEAT-01`    |
| Story   | `STORY-{序号}`          | `STORY-01`   |
| Bug Fix | `STORY-{序号}.{子序号}` | `STORY-01.1` |
| Task    | `TASK-{序号}`           | `TASK-01`    |

### Story 类型与状态

**Type**: `dev` (新功能) | `bug_fix` (缺陷修复)

**Status**: `pending` (未完成) | `done` (已完成)

### 文件命名规范

**格式**: `{ID}_{PascalCaseName}.md`

**示例**:

- `EPIC-01_Base_Init/`
- `STORY-01_Create_Structure.md`
- `TASK-01_STORY-01_Create_Structure/`

### Task 与 Story 关系

- **1:1** - 正常：一个 Story → 一个 Task
- **1:N** - 迭代：一个 Story → 多个 Task（开发 + 优化 + 修复）

---

## 💡 快速使用示例

### 使用 @tc.md 命令（推荐）

#### 项目初始化

```bash
@tc.md init
```

#### 完整开发流程

```bash
# 1. 创建 Epic
@tc.md epic 用户管理系统

# 2. 创建 Feature
@tc.md feature 用户认证 --epic=EPIC-01

# 3. 创建 Story
@tc.md story 实现用户登录 --feature=FEAT-01

# 4. 查看状态
@tc.md status

# 5. 生成 Task
@tc.md task STORY-01

# 6. 完成后同步
@tc.md sync STORY-01

# 7. 查看下一步
@tc.md next
```

#### 批量生成规划

```bash
# 拆解需求文档
@tc.md plan breakdown requirements.md

# 或使用缩写
@tc.md plan bd requirements.md
```

#### Context 管理

```bash
# 添加架构文档
@tc.md ctx add --type=architecture

# 搜索 Context
@tc.md ctx search 架构

# 更新 Context
@tc.md ctx update Architecture.md
```

#### Bug 修复流程

```bash
# 1. 创建 Bug Fix Story
@tc.md bugfix STORY-05 登录失败处理不当

# 2. 生成 Task
@tc.md task STORY-05.1

# 3. 完成后同步
@tc.md sync STORY-05.1
```

### 使用 Playbook 路径（传统方式）

#### 项目初始化

```bash
@playbooks/initialization/project_init.md 帮我初始化 The Conn 项目
```

#### 评审需求和方案

```bash
@{需求文档} @playbooks/planning/requirements_review.md 开始评审
```

#### 批量生成规划

```bash
@{需求文档} @playbooks/planning/requirements_breakdown.md 开始拆解
```

#### 单独创建 Story

```bash
@playbooks/planning/story_writing.md 帮我生成 Story
```

---

## 目录结构

```
.the_conn/
├── epics/                          # 规划层
│   └── EPIC-01_Base_Init/
│       └── features/
│           └── FEAT-01_Init_Project/
│               └── stories/
│                   └── STORY-01_Create_Structure.md
│
├── context/                        # 知识层
│   ├── global/                     # 公共 Context
│   │   ├── Architecture.md
│   │   └── Tech_Stack.md
│   └── epics/                      # Epic 专属 Context
│       └── EPIC-01/
│           └── Module_Design.md
│
├── playbooks/                      # 工具层（AI 操作剧本）
│   ├── core/
│   │   ├── core.md
│   │   └── base_rules.md
│   ├── initialization/
│   ├── planning/
│   ├── context/
│   └── execution/
│
├── docs/                           # 用户文档（AI 严禁修改）
│   ├── README.md                   # 本文件
│   └── GUIDE.md                    # 使用指南
│
└── ai_workspace/                   # 执行层（临时工作区）
    └── EPIC-01/
        └── TASK-01_STORY-01_Create_Structure/
            ├── task.md
            └── context.manifest.json
```

---

## 📖 相关文档

### 命令系统文档

- 📘 [快速开始指南](QUICK_START.md) - 5 分钟快速上手 @tc.md 命令
- 📗 [命令参考手册](COMMANDS.md) - 完整的命令列表和详细说明
- 📙 [命令映射表](COMMAND_MAPPING.md) - @tc.md 命令与 Playbook 对照表

### 核心文档

- 📕 [核心工作流](../playbooks/core/core.md) - AI 领航员敏捷工作流
- 📔 [基础公约](../playbooks/core/base_rules.md) - 框架基础规则
- 📓 [使用指南](GUIDE.md) - 详细使用指南

### 统一入口

- 🚀 [tc.md](../playbooks/tc.md) - @tc.md 命令路由入口 Playbook

---

## 🆘 获取帮助

不确定使用什么命令？

```bash
# 查看所有命令
@tc.md help

# 查看特定模块帮助
@tc.md help plan
@tc.md help ctx
@tc.md help exec

# 列出所有命令
@tc.md list

# 获取下一步建议
@tc.md next
```

---

**开始使用 The Conn，让 AI 成为你的最佳开发伙伴！** 🚀
